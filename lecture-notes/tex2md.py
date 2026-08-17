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
% SCET slash notation: use \not{.} (GitHub MathJax-friendly)
\newcommand{\nsl}{\not{n}}
\newcommand{\nbsl}{\not{\bar{n}}}
\newcommand{\Dsl}{\not{D}}
\newcommand{\psl}{\not{p}}
\newcommand{\ksl}{\not{k}}
\newcommand{\lsl}{\not{\ell}}
\newcommand{\qsl}{\not{q}}
\newcommand{\Asl}{\not{A}}
\newcommand{\dsl}{\not{\partial}}
\newcommand{\epsl}{\not{\varepsilon}}
\newcommand{\vsl}{\not{v}}
\newcommand{\Bsl}{\not{B}}
\newcommand{\pperp}{\boldsymbol{p}_\perp}
\newcommand{\kperp}{\boldsymbol{k}_\perp}
\newcommand{\qperp}{\boldsymbol{q}_\perp}
\newcommand{\as}{\alpha_s}
\newcommand{\CF}{C_F}
\newcommand{\CA}{C_A}
\newcommand{\TF}{T_F}
\newcommand{\muMS}{\overline{\mathrm{MS}}}
\newcommand{\LQCD}{\Lambda_{\mathrm{QCD}}}
\newcommand{\Gcusp}{\Gamma_{\mathrm{cusp}}}
\newcommand{\SCETI}{\mathrm{SCET}_{I}}
\newcommand{\SCETII}{\mathrm{SCET}_{II}}
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
    body = re.sub(r"\\bm\s+([A-Za-z])", r"\\boldsymbol{\1}", body)
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


def _replace_cmd_one_arg(text: str, cmd: str, left: str, right: str) -> str:
    """Replace \\cmd{...} allowing one nesting level of braces."""
    out = []
    i = 0
    token = "\\" + cmd
    n = len(text)
    while i < n:
        if text.startswith(token, i) and (i + len(token) >= n or not text[i + len(token)].isalpha()):
            j = i + len(token)
            if j < n and text[j] == "*":
                j += 1
            if j < n and text[j] == "{":
                depth = 0
                k = j
                while k < n:
                    if text[k] == "{":
                        depth += 1
                    elif text[k] == "}":
                        depth -= 1
                        if depth == 0:
                            break
                    k += 1
                if depth == 0:
                    inner = text[j + 1 : k]
                    out.append(left + inner + right)
                    i = k + 1
                    continue
        out.append(text[i])
        i += 1
    return "".join(out)


def fix_github_math(md: str) -> str:
    """Make math GitHub-MathJax friendly."""
    # Expand macros GitHub does not know (safety net if pandoc left them)
    slash = {
        r"\nsl": r"\not{n}",
        r"\nbsl": r"\not{\bar{n}}",
        r"\Dsl": r"\not{D}",
        r"\psl": r"\not{p}",
        r"\ksl": r"\not{k}",
        r"\lsl": r"\not{\ell}",
        r"\qsl": r"\not{q}",
        r"\Asl": r"\not{A}",
        r"\dsl": r"\not{\partial}",
        r"\epsl": r"\not{\varepsilon}",
        r"\vsl": r"\not{v}",
        r"\Bsl": r"\not{B}",
    }
    # longer names first
    for k in sorted(slash, key=len, reverse=True):
        md = re.sub(re.escape(k) + r"(?![A-Za-z])", lambda m, v=slash[k]: v, md)

    simple = {
        r"\pperp": r"\boldsymbol{p}_\perp",
        r"\kperp": r"\boldsymbol{k}_\perp",
        r"\qperp": r"\boldsymbol{q}_\perp",
        r"\as": r"\alpha_s",
        r"\CF": r"C_F",
        r"\CA": r"C_A",
        r"\TF": r"T_F",
        r"\muMS": r"\overline{\mathrm{MS}}",
        r"\LQCD": r"\Lambda_{\mathrm{QCD}}",
        r"\Gcusp": r"\Gamma_{\mathrm{cusp}}",
        r"\SCETI": r"\mathrm{SCET}_{I}",
        r"\SCETII": r"\mathrm{SCET}_{II}",
    }
    for k in sorted(simple, key=len, reverse=True):
        md = re.sub(re.escape(k) + r"(?![A-Za-z])", lambda m, v=simple[k]: v, md)

    md = _replace_cmd_one_arg(md, "norm", r"\left\lVert ", r"\right\rVert")
    md = _replace_cmd_one_arg(md, "abs", r"\left\lvert ", r"\right\rvert")
    md = md.replace(r"\qedhere", "")
    md = md.replace(r"\bm{", r"\boldsymbol{")
    md = re.sub(r"\\bm\s+([A-Za-z])", r"\\boldsymbol{\1}", md)
    # strip labels inside math (GitHub ignores them; they can confuse parsers)
    md = re.sub(r"\\label\{[^}]*\}", "", md)
    # \text{\emph{...}} -> \textit{...} for MathJax
    md = re.sub(r"\\text\{\\emph\{([^{}]*)\}\}", r"\\textit{\1}", md)

    # Convert \[ \] if any remain
    md = re.sub(
        r"\\\[(.+?)\\\]",
        lambda m: f"\n\n$$\n{m.group(1).strip()}\n$$\n\n",
        md,
        flags=re.S,
    )

    # Isolate every $$...$$ block onto its own lines (GitHub requirement)
    def isol(m: re.Match) -> str:
        body = m.group(1).strip()
        # tidy spaces before _ or ^ after delimiters
        body = re.sub(r"\\right\\rVert\s+([_^])", r"\\right\\rVert\1", body)
        body = re.sub(r"\\right\\rvert\s+([_^])", r"\\right\\rvert\1", body)
        return f"\n\n$$\n{body}\n$$\n\n"

    md = re.sub(r"\$\$(.+?)\$\$", isol, md, flags=re.S)

    # Blockquote-aware math lines
    lines = md.splitlines()
    out_lines = []
    in_bq = False
    in_math = False
    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith(">"):
            in_bq = True
        elif stripped == "":
            in_bq = False
        if line.strip() == "$$":
            in_math = not in_math
            if in_bq and not stripped.startswith(">"):
                out_lines.append("> " + line)
                continue
        if in_math and in_bq and line.strip() and not stripped.startswith(">"):
            out_lines.append("> " + line)
            continue
        out_lines.append(line)
    md = "\n".join(out_lines)
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md


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
    md = re.sub(r"\(\(([^()\n]+)\)\)", r"(\1)", md)
    md = re.sub(r"（\(([^()\n]+)\)）", r"（\1）", md)
    md = re.sub(r"（\(([^()\n]+)\)\)", r"（\1）", md)

    md = fix_github_math(md)
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
        "公式已按 GitHub 渲染要求处理（独立公式块、常用宏已展开）。"
        "若仍有个别公式异常，请对照同目录 `.tex`。\n"
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
