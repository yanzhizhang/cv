# CLAUDE.md — CV Factory

## What This Repo Does

LaTeX CV factory for Yanzhi Zhang. Two base CVs (English + Chinese) are compiled by GitHub Actions on every push. Job descriptions dropped into `jobs/` trigger AI-powered customization via OpenAI GPT-4o.

## Key Files

```
yanzhi_zhang_cv_en.tex    # English CV — compile with pdflatex
yanzhi_zhang_cv_cn.tex    # Chinese CV — compile with xelatex (fontspec + ctex)
jobs/_template.md          # JD template: YAML frontmatter + body
jobs/*.md                  # Job descriptions (trigger customize workflow)
scripts/customize_cv.py    # GPT-4o CV tailoring script (Python, openai SDK v1+)
scripts/requirements.txt   # Python deps: openai, pyyaml
customized/                # Output: tailored .tex + .pdf
.github/workflows/cv.yml         # Base CV compilation pipeline
.github/workflows/customize.yml  # JD-triggered customization pipeline
Dockerfile + build.sh      # Local Docker build (TeX Live + XeLaTeX + CJK)
```

## Build & Run

```sh
# Compile base CVs locally via Docker
./build.sh

# Generate a customized CV locally
export OPENAI_API_KEY=sk-...
pip install -r scripts/requirements.txt
python scripts/customize_cv.py jobs/company_role.md

# CI: push to main triggers compilation
# Release: git tag v1.0.0 && git push --tags
```

## LaTeX Rules

- Both CVs use custom commands: `\resumeItem{Title}{Desc}`, `\resumeSubheading{Company}{Location}{Title}{Dates}`, `\resumeSubHeadingListStart`/`End`, `\resumeItemListStart`/`End`, `\resumeSubItem{Title}{Desc}`.
- English CV: `\documentclass[letterpaper,11pt]{article}`, pdflatex, no fontspec.
- Chinese CV: `\documentclass[a4paper,10pt]{article}`, xelatex, requires `fontspec` + `ctex`.
- Escape LaTeX specials: `%`, `&`, `$`, `#`, `_`, `{`, `}`.
- Keep ATS-parsable: no images, no multi-column, use `\href` for links.

## Editing Guidelines

- **Never change the preamble** (packages, custom commands, margins) unless explicitly asked.
- **Never fabricate** experience, metrics, skills, or certifications.
- **Preserve section order** unless reordering is requested.
- Chinese CV content must be in Chinese except company names, technical terms, proper nouns.
- Use `\resumeItem{Title}{Description}` for bullet points under a role.

## Workflow Rules

- `cv.yml`: English = `pdflatex`, Chinese = `xelatex`, both via `xu-cheng/latex-action@v3`.
- `customize.yml`: triggers only on `jobs/*.md` changes, uses `git diff` to detect new JDs.
- Auto-commit messages must include `[skip ci]` to prevent infinite loops.
- `OPENAI_API_KEY` comes from GitHub Secrets only — never hardcode.

## Script Rules

- `customize_cv.py` uses OpenAI Python SDK v1+ (`from openai import OpenAI`).
- Job files have YAML frontmatter (`company`, `role`, `url`, `lang`) between `---` delimiters.
- Output filenames: `customized/{company}_{role}_en.tex` (slugified).
