# Yanzhi Zhang — CV Factory

LaTeX-based CV with automated compilation. Push your edits → GitHub Actions compiles PDFs → auto-committed back to `main`.

## Repository Structure

```
yanzhi_zhang_cv_en.tex          # Main English CV (pdflatex)
yanzhi_zhang_cv_cn.tex          # Main Chinese CV (xelatex)
jobs/
  _template.md                  # JD template — copy this for each new job
  *.md                          # Your job descriptions (triggers AI customization)
scripts/
  customize_cv.py               # GPT-4o CV tailoring script
  requirements.txt              # Python deps (openai, pyyaml)
customized/                     # AI-generated tailored CVs (.tex + .pdf)
.github/
  workflows/cv.yml              # Base CV compilation pipeline
  workflows/customize.yml       # JD-triggered customization pipeline
  copilot-instructions.md       # GitHub Copilot project instructions
CLAUDE.md                       # Claude Code / Claude project instructions
Dockerfile + build.sh           # Local Docker build
```

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

## AI Assistant Instructions

This repo includes project-level instructions for AI coding assistants:

- **GitHub Copilot:** [`.github/copilot-instructions.md`](.github/copilot-instructions.md) — auto-loaded by Copilot Chat in VS Code
- **Claude:** [`CLAUDE.md`](CLAUDE.md) — auto-loaded by Claude Code and Claude projects

These files encode LaTeX conventions, build commands, editing guardrails (e.g. never fabricate experience), and workflow rules so that any AI assistant working in this repo understands the project context.

## License

Format is MIT. All data is owned by Yanzhi Zhang.
