# AGENTS.md

## Cursor Cloud specific instructions

This repository holds materials for a CASTEP surface-adsorption assignment:

- Chinese markdown translations / memos (when present on the branch)
- `Assignment_template.ipynb` — bilingual fill-in scaffold for the student study
- `LICENSE` and a Python-template `.gitignore`

There is:

- **No application package** to build (`package.json`, `requirements.txt`, etc.).
- **No test suite** and **no lint configuration**.
- **No runnable CASTEP** in this environment: calculations are meant for an
  external university HPC cluster (`%%sbatch` on the `aqmtcm` partition).

### Notebook template

`Assignment_template.ipynb` is the organised student template derived from the
uploaded `Assignment_template_revised (1).ipynb`:

| Section | What it contains |
|---|---|
| Parts 0–2 | Fill-in code scaffold (bulk cutoff / k-points / a₀, slab layers / γ) |
| Part 2.3 + Parts 3–6 | Structure, blanks, and summary table — student writes the jobs |
| Submit | Checklist for `~/submission/surface_study/` |

Prefer editing `Assignment_template.ipynb` (clean name). Do not paste answers
into the `____` blanks when “organising” the template — blanks are intentional.

To sanity-check the notebook JSON locally:

```bash
python3 -c "import json; json.load(open('Assignment_template.ipynb')); print('ok')"
```
