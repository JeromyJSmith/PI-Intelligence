# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "altair==6.2.2",
#   "duckdb==1.5.5",
#   "marimo",
#   "mcp>=1",
#   "nbformat==5.11.1",
#   "openai==3.3.0",
#   "polars[pyarrow]==1.43.2",
#   "pydantic>=2",
#   "pytest==9.1.1",
#   "python-lsp-ruff==2.3.3",
#   "python-lsp-server==1.15.0",
#   "ruff==0.16.3",
#   "sherlock-project",
#   "sqlglot==30.17.0",
#   "vegafusion==2.0.3",
#   "vl-convert-python==1.9.0.post1",
#   "websockets==17.0.1",
# ]
# ///

import marimo

__generated_with = "0.24.0"
app = marimo.App()


@app.cell
def _():
    import subprocess

    import marimo as mo

    return mo, subprocess


@app.cell
def _(mo):
    mo.md("""
    # Sherlock smoke test

    This notebook is a bounded launcher for authorized OSINT work. The
    default test uses a synthetic username and a single site so the
    environment can be verified without targeting a real person.
    """)
    return


@app.cell
def _(mo):
    username = mo.ui.text(
        value="doubleaught_sherlock_smoke_20260818",
        label="Username",
    )
    site = mo.ui.text(value="GitHub", label="Site (optional; blank = all sites)")
    run = mo.ui.run_button(label="Run Sherlock")
    mo.vstack([username, site, run])
    return run, site, username


@app.cell
def _(subprocess):
    def run_sherlock(username_value, site_value="", timeout_seconds=10):
        command = [
            "sherlock",
            username_value,
            "--print-found",
            "--no-color",
            "--no-txt",
            "--timeout",
            str(timeout_seconds),
        ]
        if site_value.strip():
            command.extend(["--site", site_value.strip()])
        completed = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=max(timeout_seconds * 3, 30),
            check=False,
        )
        return {
            "command": command,
            "returncode": completed.returncode,
            "stdout": completed.stdout,
            "stderr": completed.stderr,
        }

    return (run_sherlock,)


@app.cell
def _(mo, run, run_sherlock, site, username):
    if run.value:
        result = run_sherlock(username.value, site.value)
        _display = mo.vstack(
            [
                mo.md(f"**Command:** `{' '.join(result['command'])}`"),
                mo.md(f"**Return code:** `{result['returncode']}`"),
                mo.md(
                    "```text\n"
                    + (result["stdout"] or result["stderr"] or "(no output)")
                    + "\n```"
                ),
                mo.md(
                    "Treat every hit as a lead only. Corroborate profile attributes "
                    "with independent sources and preserve the URL and timestamp."
                ),
            ]
        )
    else:
        _display = mo.md(
            "Set an authorized test username and press **Run Sherlock**."
        )
    _display
    return


if __name__ == "__main__":
    app.run()
