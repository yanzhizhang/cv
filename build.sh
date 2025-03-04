#!/usr/bin/env bash

docker build -t zzz/latex .
docker run --rm -i -v "$PWD":/data zzz/latex pdflatex yanzhi_zhang_cv_en.tex
docker run --rm -i -v "$PWD":/data zzz/latex pdflatex yanzhi_zhang_cv_cn.tex
