# Yanzhi Zhang — CV Factory

LaTeX-based CV with automated compilation. Push your edits → GitHub Actions compiles PDFs → auto-committed back to `main`.

## Files

| File                     | Language | Compiler   |
| ------------------------ | -------- | ---------- |
| `yanzhi_zhang_cv_en.tex` | English  | `pdflatex` |
| `yanzhi_zhang_cv_cn.tex` | Chinese  | `xelatex`  |

## CI/CD Pipeline

On every push to `main`:

1. Both CVs are compiled via [xu-cheng/latex-action](https://github.com/xu-cheng/latex-action)
2. PDFs are uploaded as **downloadable artifacts** (retained 90 days)
3. Compiled PDFs are **auto-committed** back to `main`

On pull requests to `main`:

- CVs are compiled and uploaded as artifacts (no auto-commit)

### Tagged Releases

Tag a version to create a GitHub Release with PDF attachments:

```sh
git tag v1.0.0
git push --tags
```

## Local Build

### Using Docker

```sh
./build.sh
```

This builds a Docker image with TeX Live (including XeLaTeX + CJK fonts) and compiles both CVs.

### Using VS Code

Install [LaTeX Workshop](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop) and a compatible TeX Live distribution.

## AI-Powered Job Customization

Drop a job description into `jobs/` and push — GitHub Actions calls OpenAI GPT-4o to tailor your CV, then compiles and commits the result to `customized/`.

### Setup

Add your OpenAI API key as a GitHub repository secret:

**Settings → Secrets and variables → Actions → New repository secret**
- Name: `OPENAI_API_KEY`
- Value: your key (`sk-...`)

### Usage

1. Copy `jobs/_template.md` to a new file, e.g. `jobs/google_swe.md`
2. Fill in the YAML frontmatter (`company`, `role`, `url`) and paste the job description
3. Commit and push to `main`
4. GitHub Actions will:
   - Call GPT-4o to tailor `yanzhi_zhang_cv_en.tex` for the JD
   - Compile the customized `.tex` to PDF with `pdflatex`
   - Auto-commit both `.tex` and `.pdf` to `customized/`
   - Upload PDFs as downloadable artifacts

### Local Usage

```sh
export OPENAI_API_KEY=sk-...
pip install -r scripts/requirements.txt
python scripts/customize_cv.py jobs/google_swe.md
```

Output lands in `customized/{company}_{role}_en.tex`.

## License

Format is MIT. All data is owned by Yanzhi Zhang.
