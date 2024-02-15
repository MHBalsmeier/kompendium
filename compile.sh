#!/bin/bash
xelatex kompendium.tex
biber kompendium
xelatex kompendium.tex
makeindex kompendium.tex
xelatex kompendium.tex
