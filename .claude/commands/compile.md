Compile both base CVs locally using Docker. Run `./build.sh` and report the results.

If Docker is not available, try compiling directly:
- English CV: `pdflatex -interaction=nonstopmode yanzhi_zhang_cv_en.tex`
- Chinese CV: `xelatex -interaction=nonstopmode yanzhi_zhang_cv_cn.tex`

After compilation, list the generated PDF files with their sizes.
If any errors occur, read the `.log` file and diagnose the LaTeX issue.
