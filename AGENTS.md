# AGENTS.md

## Cursor Cloud specific instructions

This repository is **documentation-only**. It contains Chinese-language markdown
translations of a physics assignment (CASTEP surface-adsorption study) plus a
`LICENSE` and a Python-template `.gitignore`. There is:

- **No application code**, source files, notebooks, or scripts to run.
- **No package manifest** (`package.json`, `requirements.txt`, `pyproject.toml`, etc.),
  so there are **no dependencies to install** and **nothing to build**.
- **No test suite** and **no lint configuration**.

Because of this, the environment update script is intentionally a no-op. There is
nothing to "start" — work here is editing/reviewing the `.md` files directly.

The assignment text itself describes work that a student would run on an external
university HPC cluster using proprietary **CASTEP** (via Slurm `%%sbatch` on the
`aqmtcm` partition). That software is **not** part of this repo and is not runnable
here; the repo only holds the translated assignment description.

To visually preview a markdown file, you can render it locally, e.g.:

```bash
pip install markdown            # one-off, not a repo dependency
python3 -m markdown <file>.md > /tmp/out.html
python3 -m http.server 8099     # then open the HTML in a browser
```
