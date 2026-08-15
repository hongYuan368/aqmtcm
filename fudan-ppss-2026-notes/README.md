# 复旦粒子物理暑期学校 2026 · 课前预习讲义

本目录包含三份**彼此独立、可单独编译**的中文课前讲义，对应 Indico 课表

- [Fudan Particle Physics Summer School 2026](https://indico.ihep.ac.cn/event/29307/)

中第一周的三门课。讲义从基础写起，推导尽量写全，并单独列出英文术语，供尚未系统学过相关高级内容的同学预习。

| 文件 | 课程 | 教师 | 课时 |
| --- | --- | --- | --- |
| `01_machine_learning_shih.tex` | Machine Learning | David Shih (Rutgers) | 4 讲（8/17–8/18 上午） |
| `02_generalized_symmetry_brennan.tex` | Generalized Symmetry | Daniel Brennan (Birmingham) | 4 讲（8/17–8/19） |
| `03_scet_neubert.tex` | SCET | Matthias Neubert (Mainz) | 5 讲（8/17–8/21 下午） |

## 性质与使用说明

- 这是**学生预习讲义**，不是三位老师的正式课堂讲义，也不替代课堂。
- 课堂若采用不同记号、不同例子或不同侧重点，以老师当场讲解为准。
- 每份讲义末尾有：课堂可能出现的公式与术语、常见困惑、听课重点、进一步学习路线、英文术语表。

## 编译

需要 XeLaTeX 与中文字体（如 Noto CJK）。在本目录执行：

```bash
make            # 编译三份 PDF
make ml         # 只编译机器学习
make symmetry   # 只编译广义对称性
make scet       # 只编译 SCET
```

或对单个文件：

```bash
latexmk -xelatex 01_machine_learning_shih.tex
```

## 课表摘录（Asia/Shanghai）

**8 月 17 日（周一）**

- 09:30–10:30, 10:50–11:50　Machine Learning (David Shih)
- 13:30–14:30　Generalized Symmetry (Daniel Brennan)
- 14:50–15:50　SCET (Matthias Neubert)

**8 月 18 日（周二）**

- 09:20–10:20, 10:40–11:40　Machine Learning (David Shih)
- 13:30–14:30　Generalized Symmetry (Daniel Brennan)
- 14:50–15:50　SCET (Matthias Neubert)

**8 月 19 日（周三）**

- 09:20–10:20, 10:40–11:40　Generalized Symmetry (Daniel Brennan)
- 16:10–17:10　SCET (Matthias Neubert)

**8 月 20–21 日（周四、周五）**

- 14:50–15:50　SCET (Matthias Neubert)
