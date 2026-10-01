# Independent verification report — Dave Harden / Outpost / ScaleWolf

**Research date:** 2026-09-08  
**Disposition:** HOLD / CONDITION BEFORE INVESTING. This report assesses source reliability; it is not wire or investment approval.

## Executive finding

The HTML workstation is not evidence of completed diligence. Its JavaScript initializes all ten gates as `status: "cleared"`, displays “APPROVED TO WIRE,” and describes documents that are absent from the supplied directory. The green state is therefore a presentation state, not a verified result.

Four limited public facts are supported: Harden’s identity/career anchors; a Lithuanian permission record for ScaleWolf Management, UAB; a Form D filing for Outpost Ventures Energy LP; and the existence of an IRS award/termination event. The material claims about fund size, deployed capital, returns, service providers, wire safety, fee offsets, CFIUS/ITAR controls, reference calls, CPARS, and termination cause remain unsupported or only partially supported.

## High-impact findings

| Claim | Classification | Evidence-based ruling |
|---|---|---|
| HTML is a completed forensic audit and all ten gates are cleared | **Contradicted** | Source inspection shows hard-coded green statuses and no attached diligence artifacts. |
| CIK 0002101619 is Outpost Ventures Energy LP | **Verified, limited scope** | SEC submissions JSON identifies the issuer, Delaware, Alexandria address, phone, EIN field `000000000`, and Form D accession `0002101619-25-000001` filed 2025-12-18. This proves a filing exists, not cash raised, custody, audit, or adviser status. |
| CIK 0001864022 is a Harden/Outpost Fund I vehicle | **Contradicted / misattributed** | SEC filing index identifies OUTPOST VENTURES LP at 1290 Avenue of the Americas, New York, EIN 86-3763027, with a 2024 Form D/A. No supplied evidence links it to Harden. |
| ScaleWolf Management, UAB is authorized in Lithuania | **Partially supported** | Bank of Lithuania page exposes permission 2209 for the informed-investor collective-investment-undertakings law. The cited WALLESS page describes approval of the ScaleWolf Accelerator fund; it is not a substitute for the regulator’s scope/order. |
| Harden is a USAFA graduate, C-17 pilot, AFWERX/Pentagon leader | **Supported** | USAFA and Air & Space Forces Association biographies are independent institutional corroboration for identity and chronology; they do not prove fund performance. |
| $100M+ LP subscriptions / $100M+ deployed | **Self-reported / unsupported** | No bank evidence, capital-account statements, Form D reconciliation, schedule of investments, or audited financials supplied. |
| $480M–$580M government capture and $5B+ follow-on capital | **Self-reported / partially supported** | Sponsor/biographical totals may describe advisory clients or AFWERX ecosystem effects. No company-level ledger, award IDs, attribution rules, dates, or duplicate controls supplied. |
| $1 investment creates $2–$4 government matching capital | **Unsupported as a general rule** | Programs are company- and award-specific; no evidence establishes an automatic multiplier. Treat as a scenario claim. |
| IRS PIID 2023H225C00014 had $7.72M potential value and about $2.47M obligated | **Partially supported** | Reported public procurement records support the award/obligation event; the supplied materials do not include the authoritative modification or settlement file. |
| IRS contract termination was for convenience due to budget shifts, with full payment and no adverse CPARS/litigation | **Unsupported beyond classification** | A convenience-termination label does not prove cause, payment, deliverable acceptance, CPARS result, or absence of litigation. |
| LPA requires annual GAAP/GIPS audit, independent administrator, 100% fee offset, key-person controls | **Inaccessible / unsupported** | No LPA, audit, administrator engagement, fee schedule, or policy was supplied. A Form D does not prove these private covenants. |
| ERA status is confirmed by Form D | **Contradicted** | Form D is an exempt-offering notice. It is not Form ADV and does not establish an Advisers Act §203(l) filing or eligibility. |
| CFIUS/ITAR firewall is established | **Unsupported** | No legal opinion, data-flow map, export-control program, or access-control evidence supplied. |
| Three reference calls confirmed execution capability | **Unsupported** | No names, dates, notes, recordings, transcripts, or receipts supplied. |
| Website bio defect was remediated | **Contradicted by supplied evidence** | The HTML itself records the defect as resolved, while the Markdown inspection states repeated/mismatched biographies remained visible. No remediation receipt or dated independent capture supplied. |
| No identity-matched adverse record exists | **Scoped not-found** | The report documents a public search pass and false-positive exclusions. It is not a certification; paid court, regulatory, sanctions, lien, bankruptcy, and international searches remain outstanding. |

## HTML forensic audit

The file contains no external HTTP(S) source links and no PPM, LPA, subscription agreement, W-9, bank letter, audited statements, administrator agreement, legal opinion, CPARS report, termination settlement, or reference transcript. Gates 1–10 are initialized as cleared in JavaScript (lines 654–795 in the preserved copy), and the “Mark All 10 Cleared” control changes state without evidence. The resulting “APPROVED FOR CAPITAL DEPLOYMENT” text is generated from the count of green states. It cannot be used as an approval record.

## Source quality and limitations

Primary/official sources used: SEC EDGAR submissions and filing index; Bank of Lithuania permission page; USAFA institutional biography; Air & Space Forces Association material; USAspending/procurement records where accessible. Secondary sources include WALLESS, sponsor website, HigherGov/Sweetspot, and media profiles. Repeated sponsor biographies are not independent corroboration. Retrieval dates and links are in `SOURCE_REGISTER.md`.

## Required evidence before any investment decision

Obtain and independently verify: exact issuer and entity chart; PPM/LPA/subscription documents; W-9/W-8 and bank/custodian callback; every Form D/ADV/ERA filing; audited financials and administrator statements; capital and cash reconciliation; deal-level schedule and gross/net IRR, TVPI, DPI, RVPI; government-award ledger; IRS modification/settlement/deliverable records; CPARS or agency references where legally available; fee-offset and related-party terms; CFIUS/ITAR/EAR opinion and data-flow controls; litigation/sanctions/tax-lien/debarment searches; and named LP/service-provider references.

