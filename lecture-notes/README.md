# 课前预习讲义（Markdown 版）

在 GitHub 上直接点开下面的 `.md` 文件即可阅读（公式由 GitHub 渲染；请看渲染预览而非 Raw）。若公式仍异常，硬刷新页面，或对照同目录 `.tex`。如需精排 PDF，请编译同目录下的 `.tex`（`xelatex`，编译两次）。

| 讲义 | Markdown | LaTeX 源文件 |
|------|----------|--------------|
| Machine Learning（David Shih） | [01-machine-learning-david-shih.md](./01-machine-learning-david-shih.md) | [01-machine-learning-david-shih.tex](./01-machine-learning-david-shih.tex) |
| Generalized Symmetry（Daniel Brennan） | [02-generalized-symmetry-daniel-brennan.md](./02-generalized-symmetry-daniel-brennan.md) | [02-generalized-symmetry-daniel-brennan.tex](./02-generalized-symmetry-daniel-brennan.tex) |
| SCET（Matthias Neubert） | [03-scet-matthias-neubert.md](./03-scet-matthias-neubert.md) | [03-scet-matthias-neubert.tex](./03-scet-matthias-neubert.tex) |

重新从 `.tex` 生成 Markdown：

```bash
python3 tex2md.py *.tex
```
