#!/usr/bin/env python3
"""Preprocess lecture-note .tex then convert to GitHub Flavored Markdown via pandoc."""
from __future__ import annotations

import argparse
import re
import subprocess
import tempfile
from pathlib import Path

ENV_LABELS = {
    "definition": "定义",
    "theorem": "定理",
    "lemma": "引理",
    "proposition": "命题",
    "corollary": "推论",
    "example": "例",
    "exercise": "练习",
    "remark": "注",
    "keypoint": "要点",
    "warning": "注意",
    "proof": "证明",
}

MACRO_HEADER = r"""
\usepackage{amsmath,amssymb,amsfonts,mathtools,bm}
\newcommand{\R}{\mathbb{R}}
\newcommand{\E}{\mathbb{E}}
\newcommand{\Prob}{\mathbb{P}}
\newcommand{\D}{\mathcal{D}}
\newcommand{\Loss}{\mathcal{L}}
\newcommand{\Hyp}{\mathcal{H}}
\newcommand{\dd}{\mathrm{d}}
\newcommand{\T}{^{\mathsf{T}}}
\newcommand{\ZZ}{\mathbb{Z}}
\newcommand{\RR}{\mathbb{R}}
\newcommand{\CC}{\mathbb{C}}
\newcommand{\Uone}{\mathrm{U}(1)}
\newcommand{\Ugrp}{\mathrm{U}}
\newcommand{\SUgrp}{\mathrm{SU}}
\newcommand{\SOgrp}{\mathrm{SO}}
\newcommand{\Op}{\mathcal{O}}
\newcommand{\Mfd}{\mathcal{M}}
\newcommand{\Lag}{\mathcal{L}}
\newcommand{\Ham}{\mathcal{H}}
\newcommand{\Ssurf}{\Sigma}
\newcommand{\Tr}{\mathrm{Tr}}
\newcommand{\Vol}{\mathrm{vol}}
\newcommand{\Link}{\mathrm{Link}}
\newcommand{\Pexp}{\mathbf{P}\exp}
\newcommand{\ext}{\mathrm{d}}
\newcommand{\hs}{\star}
\newcommand{\Uop}{U}
\newcommand{\Dop}{\mathcal{D}}
\newcommand{\PD}[2]{\frac{\partial #1}{\partial #2}}
\newcommand{\pform}[1]{#1\text{-form}}
\newcommand{\eng}[1]{\textup{(#1)}}
\newcommand{\en}[1]{\textup{(#1)}}
\DeclarePairedDelimiter{\norm}{\lVert}{\rVert}
\DeclarePairedDelimiter{\abs}{\lvert}{\rvert}
\DeclareMathOperator*{\argmin}{arg\,min}
\DeclareMathOperator*{\argmax}{arg\,max}
\DeclareMathOperator{\tr}{tr}
\DeclareMathOperator{\rank}{rank}
\DeclareMathOperator{\sgn}{sign}
\DeclareMathOperator{\diag}{diag}
\DeclareMathOperator{\Var}{Var}
\DeclareMathOperator{\Cov}{Cov}
\DeclareMathOperator{\softmax}{softmax}
\DeclareMathOperator{\ReLU}{ReLU}
\DeclareMathOperator{\KL}{KL}
"""


def strip_comments(tex: str) -> str:
    out = []
    for line in tex.splitlines():
        buf, i, n = [], 0, len(line)
        while i < n:
            if line[i] == "\\" and i + 1 < n:
                buf.append(line[i : i + 2])
                i += 2
                continue
            if line[i] == "%":
                break
            buf.append(line[i])
            i += 1
        out.append("".join(buf).rstrip())
    return "\n".join(out)


def extract_field(tex: str, cmd: str) -> str:
    m = re.search(rf"\\{cmd}\{{((?:[^{{}}]|{{[^{{}}]*}})*)\}}", tex, re.S)
    if not m:
        return ""
    raw = m.group(1)
    raw = re.sub(r"\\\[[^\]]*\]", " — ", raw)
    raw = re.sub(r"\\\\", " — ", raw)
    raw = re.sub(r"\\(?:textbf|bfseries|large|Large)\s*\{([^{}]*)\}", r"\1", raw)
    raw = re.sub(r"\\(?:textbf|bfseries|large|Large)\b", "", raw)
    raw = re.sub(r"\\[a-zA-Z]+\{([^{}]*)\}", r"\1", raw)
    raw = re.sub(r"\s+", " ", raw).strip(" —")
    return raw


def replace_theorem_envs(body: str) -> str:
    for name, title in ENV_LABELS.items():

        def repl(m: re.Match, title=title) -> str:
            opt = m.group(1)
            content = m.group(2).strip()
            head = title + (f"（{opt}）" if opt else "")
            return f"\n\n\\textbf{{{head}。}}\n\n{content}\n\n"

        body = re.sub(
            rf"\\begin\{{{name}\}}(?:\[([^\]]*)\])?(.*?)\\end\{{{name}\}}",
            repl,
            body,
            flags=re.S,
        )
    return body


def preprocess(tex: str) -> tuple[str, str, str]:
    tex = strip_comments(tex)
    title = extract_field(tex, "title")
    author = extract_field(tex, "author")
    m = re.search(r"\\begin\{document\}(.*)\\end\{document\}", tex, re.S)
    body = m.group(1) if m else tex
    body = re.sub(r"\\maketitle", "", body)
    body = re.sub(r"\\tableofcontents", "", body)
    body = re.sub(r"\\newpage", r"\\clearpage", body)
    body = re.sub(r"\\texorpdfstring\{([^{}]*)\}\{[^{}]*\}", r"\1", body)
    # GitHub MathJax: prefer \boldsymbol over ams \bm
    body = body.replace(r"\bm{", r"\boldsymbol{")
    body = replace_theorem_envs(body)

    # abstract -> quote
    body = re.sub(
        r"\\begin\{abstract\}(.*?)\\end\{abstract\}",
        lambda m: "\\begin{quote}\n\\textbf{摘要}\\par\n" + m.group(1) + "\\end{quote}",
        body,
        flags=re.S,
    )

    wrapped = (
        "\\documentclass{article}\n"
        + MACRO_HEADER
        + "\\begin{document}\n"
        + body
        + "\n\\end{document}\n"
    )
    return wrapped, title, author


def postprocess(md: str, title: str, author: str) -> str:
    # drop empty YAML / leftover pandoc title blocks if any
    md = re.sub(r"^---\n.*?\n---\n+", "", md, count=1, flags=re.S)
    # pandoc sometimes emits HTML for \textup / font switches
    md = re.sub(r'<span class="upright">\((.*?)\)</span>', r"(\1)", md)
    md = re.sub(r'<span class="upright">(.*?)</span>', r"\1", md)
    md = re.sub(r"</?span[^>]*>", "", md)
    md = re.sub(
        r'<a href="[^"]*" data-reference-type="(?:ref|eqref)"[^>]*>(.*?)</a>',
        r"\1",
        md,
    )
    md = re.sub(r'<div class="center">\s*', "", md)
    md = re.sub(r"</div>", "", md)
    md = re.sub(r"</?div[^>]*>", "", md)
    md = md.replace(r"\bm{", r"\boldsymbol{")
    md = re.sub(r"\(\(([^()\n]+)\)\)", r"(\1)", md)
    md = re.sub(r"（\(([^()\n]+)\)）", r"（\1）", md)
    md = re.sub(r"（\(([^()\n]+)\)\)", r"（\1）", md)
    # normalize excessive blank lines
    md = re.sub(r"\n{3,}", "\n\n", md).strip() + "\n"

    def clean_title(t: str) -> str:
        t = t.replace("\\ —", " —").replace("\\—", " —").replace("\\", "")
        t = re.sub(r"\s+", " ", t).strip(" —")
        return t

    header = []
    if title:
        header.append(f"# {clean_title(title)}\n")
    if author:
        header.append(f"*{author}*\n")
    header.append(
        "> 本文由 LaTeX 课前讲义转换为 Markdown，可在 GitHub 直接阅读。"
        "数学公式使用 `$...$` / `$$...$$`。"
        "排版以同目录 `.tex` 为准；若个别公式显示异常，请对照源文件。\n"
    )
    return "\n".join(header) + "\n" + md


def convert_file(inp: Path, out: Path) -> None:
    tex = inp.read_text(encoding="utf-8")
    wrapped, title, author = preprocess(tex)
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td) / "in.tex"
        tmp.write_text(wrapped, encoding="utf-8")
        proc = subprocess.run(
            [
                "pandoc",
                str(tmp),
                "-f",
                "latex",
                "-t",
                "gfm",
                "--wrap=none",
                "--markdown-headings=atx",
            ],
            capture_output=True,
            text=True,
        )
        if proc.returncode != 0:
            raise RuntimeError(f"pandoc failed on {inp}:\n{proc.stderr}")
        md = postprocess(proc.stdout, title, author)
    out.write_text(md, encoding="utf-8")
    print(f"Wrote {out} ({len(md.splitlines())} lines, {out.stat().st_size} bytes)")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("inputs", nargs="+", type=Path)
    args = ap.parse_args()
    for inp in args.inputs:
        convert_file(inp, inp.with_suffix(".md"))


if __name__ == "__main__":
    main()
