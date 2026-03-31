#!/usr/bin/env bash
set -euo pipefail

docker build -t zzz/latex .
docker run --rm -i -v "$PWD":/data zzz/latex pdflatex -interaction=nonstopmode yanzhi_zhang_cv_en.tex
docker run --rm -i -v "$PWD":/data zzz/latex xelatex  -interaction=nonstopmode yanzhi_zhang_cv_cn.tex

echo "Done. Generated PDFs:"
ls -lh yanzhi_zhang_cv_en.pdf yanzhi_zhang_cv_cn.pdf 2>/dev/null
