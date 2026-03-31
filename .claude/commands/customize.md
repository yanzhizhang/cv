Customize the base English CV for a specific job description using the local Python script.

Usage: Provide the path to a job description file in `jobs/`.

Steps:
1. Verify `OPENAI_API_KEY` is set in the environment.
2. Ensure dependencies are installed: `pip install -r scripts/requirements.txt`
3. Run: `python scripts/customize_cv.py $ARGUMENTS`
4. Read the generated `.tex` file in `customized/` and verify it contains `\begin{document}` and `\end{document}`.
5. Try to compile it: `pdflatex -interaction=nonstopmode -output-directory=customized customized/*.tex`
6. Report success or diagnose any LaTeX compilation errors.

If OPENAI_API_KEY is not set, tell the user to export it first.
