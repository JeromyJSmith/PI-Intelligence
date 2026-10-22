"""Agent-editable browser helpers.

Add task-specific browser primitives here. Core helpers from browser_harness.helpers
load this file when BH_AGENT_WORKSPACE points at this directory, or when this
repo's default agent-workspace exists.
"""

from __future__ import annotations

import json
import time
from browser_harness.helpers import js


def ifclite_status() -> dict:
    """Return live @ifc-lite/viewer store status for IFCX layer stack and federated models."""
    return js(
        """(() => {
      const store = window.__MARPA_VIEWER_STORE__;
      if (!store) {
        return {
          hasStore: false,
          loading: false,
          error: 'window.__MARPA_VIEWER_STORE__ not mounted',
          progress: null,
          layerStackCount: 0,
          modelCount: 0,
          layers: [],
          models: [],
        };
      }
      const s = store.getState();
      const layers = (s.layerStack ?? []).map((l) => ({
        id: l.id,
        name: l.name,
        nodeCount: l.nodeCount,
        meshCount: l.meshCount ?? 0,
        colorHex: l.colorHex ?? null,
        authorKind: l.authorKind ?? null,
        intent: l.intent ?? null,
      }));
      const models = Array.from(s.models?.values?.() ?? []).map((m) => ({
        id: m.id,
        name: m.name,
        schemaVersion: m.schemaVersion,
        visible: m.visible,
        meshCount: m.geometryResult?.meshes?.length ?? 0,
        pointCloudCount: m.geometryResult?.pointClouds?.length ?? 0,
        pointCloudHandleId: m.pointCloudHandleId ?? null,
        federationAlignmentStatus: m.federationAlignmentStatus ?? null,
        horizontalCrs:
          m.spatialReference?.horizontal?.id ??
          m.ifcDataStore?.georeferencing?.projectedCRS?.name ??
          null,
        verticalCrs:
          m.spatialReference?.vertical?.id ??
          m.ifcDataStore?.georeferencing?.projectedCRS?.verticalDatum ??
          null,
      }));
      return {
        hasStore: true,
        loading: Boolean(s.loading),
        error: s.error ?? null,
        progress: s.progress ?? null,
        layerStackCount: layers.length,
        modelCount: models.length,
        distinctLayerColors: new Set(layers.map((l) => l.colorHex).filter(Boolean)).size,
        pointCloudAlignmentEnabled: Boolean(s.pointCloudAlignmentEnabled),
        pointCloudAlignmentAvailable: Boolean(s.pointCloudAlignmentAvailable),
        sidebarActivePanel: s.sidebarActivePanel ?? null,
        sidebarSecondaryPanel: s.sidebarSecondaryPanel ?? null,
        layers,
        models,
      };
    })()"""
    )


def ifclite_autoload_workbench(timeout: float = 120.0) -> dict:
    """Trigger or await federated load of /ifcx-model/workbench-autoload.json (11 IFCX layers + 6 LAZ scans)."""
    status = ifclite_status()
    if (
        status.get("hasStore")
        and not status.get("loading")
        and status.get("layerStackCount", 0) == 0
        and status.get("modelCount", 0) == 0
    ):
        # Trigger federated load via the viewer's custom event listeners if not already running
        js(
            """(async () => {
          const res = await fetch('/ifcx-model/workbench-autoload.json', { cache: 'no-store' });
          if (!res.ok) throw new Error('Failed to fetch /ifcx-model/workbench-autoload.json: ' + res.status);
          const manifest = await res.json();
          const layerSpecs = manifest.ifcx_layers ?? manifest.ifcxLayers ?? [];
          if (layerSpecs.length > 0) {
            const layerFiles = await Promise.all(
              layerSpecs.map(async (spec) => {
                const fileName = ('file' in spec && spec.file) ? spec.file : spec.name;
                const url = ('url' in spec && spec.url) ? spec.url : `/ifcx-model/${fileName}`;
                const r = await fetch(url, { cache: 'no-store' });
                if (!r.ok) throw new Error(`Failed to fetch IFCX layer ${url}: ${r.status}`);
                const buf = await r.arrayBuffer();
                return new File([buf], fileName, { type: 'application/json' });
              })
            );
            window.dispatchEvent(new CustomEvent('ifc-lite:load-layer-stack', { detail: layerFiles }));
            const waitStore = async (pred, maxMs = 60000) => {
              const t0 = Date.now();
              while (Date.now() - t0 < maxMs) {
                const st = window.__MARPA_VIEWER_STORE__?.getState();
                if (st && pred(st)) return true;
                await new Promise((r) => setTimeout(r, 200));
              }
              return false;
            };
            await waitStore((st) => !st.loading && (st.layerStack?.length ?? 0) === layerSpecs.length, 60000);
          }
          const scanSpecs = manifest.point_clouds ?? manifest.scans ?? [];
          for (const scan of scanSpecs) {
            const relFile = scan.file ?? scan.filename;
            const url = ('url' in scan && scan.url) ? scan.url : `/ifcx-model/${relFile}`;
            const baseFileName = relFile.split('/').pop() || relFile;
            const r = await fetch(url, { cache: 'no-store' });
            if (!r.ok) continue;
            const buf = await r.arrayBuffer();
            const scanFile = new File([buf], baseFileName, { type: 'application/octet-stream' });
            window.dispatchEvent(new CustomEvent('ifc-lite:add-model', { detail: scanFile }));
            const prevCount = window.__MARPA_VIEWER_STORE__?.getState()?.models?.size ?? 0;
            const t0 = Date.now();
            while (Date.now() - t0 < 60000) {
              const st = window.__MARPA_VIEWER_STORE__?.getState();
              if (st && !st.loading && (st.models?.size ?? 0) > prevCount) break;
              await new Promise((r) => setTimeout(r, 250));
            }
          }
          return true;
        })()"""
        )

    deadline = time.time() + timeout
    while time.time() < deadline:
        status = ifclite_status()
        if (
            status.get("hasStore")
            and not status.get("loading")
            and status.get("layerStackCount", 0) >= 11
            and status.get("modelCount", 0) >= 17
        ):
            break
        time.sleep(0.5)

    # Ensure both Layers and Properties panels are visible in a split right sidebar
    js(
        """(() => {
      const s = window.__MARPA_VIEWER_STORE__?.getState();
      if (!s) return;
      if ((s.layerStack?.length ?? 0) >= 2) {
        s.openWorkspacePanel('layers', 'programmatic');
        s.setSidebarSecondaryPanel('properties');
        s.setSidebarSplitRatio(0.42);
      } else {
        s.openWorkspacePanel('properties', 'programmatic');
      }
    })()"""
    )
    return ifclite_status()


def ifclite_select_by_path(ifcx_path: str) -> dict:
    """Select an entity by its IFCX path (or alias/name) and return its rendered provenance card and properties."""
    path_json = json.dumps(ifcx_path)
    return js(
        f"""(async () => {{
      const requestedPath = {path_json};
      const store = window.__MARPA_VIEWER_STORE__;
      if (!store) return {{ ok: false, error: 'window.__MARPA_VIEWER_STORE__ not mounted', requestedPath }};
      const s = store.getState();

      // Ensure PropertiesPanel is mounted in the sidebar (either primary or secondary split with Layers)
      if (s.sidebarActivePanel !== 'properties' && s.sidebarSecondaryPanel !== 'properties') {{
        if ((s.layerStack?.length ?? 0) >= 2) {{
          s.openWorkspacePanel('layers', 'programmatic');
          s.setSidebarSecondaryPanel('properties');
          s.setSidebarSplitRatio(0.42);
        }} else {{
          s.openWorkspacePanel('properties', 'programmatic');
        }}
      }}

      const pathToId = s.layerStackPathToId;
      const ds = s.ifcDataStore;
      let expressId = pathToId?.get(requestedPath);

      if (expressId === undefined && ds?.entities) {{
        const canonicalAliases = {{
          'Project_401Pearl/Site_401Pearl/Building_401Pearl/Storey_Level2/Roof_Gable_N_Slope_W_r3': 'Upper level walls',
          'Project_401Pearl/Site_401Pearl/Building_401Pearl/Storey_Level1/Wall_EXT_W_L1_SouthSeg': 'Stairwell south wall (exterior)',
          'Project_401Pearl/Site_401Pearl/Building_401Pearl/Storey_Level1/Stair_Main_1/StairFlight_1': 'Lower flight (straight, bullnose start)',
        }};
        const targetName = canonicalAliases[requestedPath] ?? requestedPath;
        for (let i = 0; i < ds.entities.count; i++) {{
          const id = ds.entities.expressId[i];
          const name = ds.entities.getName(id)?.trim();
          if (name === targetName || name === requestedPath) {{
            expressId = id;
            break;
          }}
        }}
      }}

      if (expressId === undefined) {{
        return {{ ok: false, error: `IFCX path not found: ${{requestedPath}}`, requestedPath }};
      }}

      const baseModel = Array.from(s.models.values()).find((m) => m.name === '00-base-interior-v4.ifcx')
        ?? Array.from(s.models.values())[0];
      const srcInfo = ds?._entitySourceLayer?.get(expressId);
      const modelId = (srcInfo?.layerId && s.models.has(srcInfo.layerId)) ? srcInfo.layerId : (baseModel?.id ?? 'layer-1');

      s.setSelectedEntityId(expressId);
      s.setSelectedEntity({{ modelId, expressId }});
      await new Promise((r) => setTimeout(r, 350));

      const card = document.querySelector('[data-testid="ifcx-source-layer-card"]');
      const entityName = ds?.entities?.getName?.(expressId) ?? null;
      const ifcClass = ds?.entities?.getTypeName?.(expressId) ?? null;
      const psets = (ds?.properties?.getForEntity?.(expressId) ?? []).map((pset) => ({{
        name: pset.name,
        properties: (pset.properties ?? []).map((p) => ({{ name: p.name, value: p.value }})),
      }}));
      const propContainer = card?.closest('.flex.flex-col');

      return {{
        ok: true,
        requestedPath,
        expressId,
        modelId,
        ifcxPath: srcInfo?.path ?? requestedPath,
        entityName,
        ifcClass,
        sourceLayer: srcInfo?.layerName ?? null,
        colorHex: srcInfo?.colorHex ?? null,
        cardFound: Boolean(card),
        cardText: card ? card.innerText : null,
        properties: psets,
        panelTextSample: propContainer ? propContainer.innerText.slice(0, 800) : null,
      }};
    }})()"""
    )
