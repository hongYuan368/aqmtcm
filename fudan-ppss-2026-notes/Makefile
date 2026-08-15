# 复旦粒子物理暑期学校 2026 课前讲义
LATEXMK ?= latexmk
ENGINE  ?= -xelatex
FLAGS   ?= -interaction=nonstopmode -file-line-error -halt-on-error

ML       := 01_machine_learning_shih
SYMMETRY := 02_generalized_symmetry_brennan
SCET     := 03_scet_neubert

.PHONY: all ml symmetry scet clean

all: ml symmetry scet

ml:
	$(LATEXMK) $(ENGINE) $(FLAGS) $(ML).tex

symmetry:
	$(LATEXMK) $(ENGINE) $(FLAGS) $(SYMMETRY).tex

scet:
	$(LATEXMK) $(ENGINE) $(FLAGS) $(SCET).tex

clean:
	$(LATEXMK) -C $(ML).tex $(SYMMETRY).tex $(SCET).tex
	rm -f *.run.xml *.bbl *.synctex.gz
