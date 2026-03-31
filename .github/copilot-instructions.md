# Copilot Instructions — CV Factory

## Project Overview

This is a LaTeX-based CV repository with automated compilation and AI-powered job customization. The owner is Yanzhi Zhang.

## Repository Structure

- `yanzhi_zhang_cv_en.tex` — Main English CV (compile with `pdflatex`)
- `yanzhi_zhang_cv_cn.tex` — Main Chinese CV (compile with `xelatex`, uses `fontspec` + `ctex`)
- `jobs/*.md` — Job description files with YAML frontmatter (`company`, `role`, `url`)
- `jobs/_template.md` — Template for new job descriptions
- `scripts/customize_cv.py` — Python script that calls OpenAI GPT-4o to tailor the English CV for a JD
- `scripts/requirements.txt` — Python dependencies (`openai`, `pyyaml`)
- `customized/` — Output directory for AI-generated tailored CVs (`.tex` + `.pdf`)
- `.github/workflows/cv.yml` — Compiles base CVs on push to `main`, uploads artifacts, auto-commits PDFs, creates releases on tags
- `.github/workflows/customize.yml` — Triggers when `jobs/*.md` changes, runs `customize_cv.py`, compiles and commits results
- `Dockerfile` + `build.sh` — Local Docker-based build (TeX Live with XeLaTeX + CJK fonts)

## LaTeX Conventions

- Both CVs use custom commands defined in the preamble: `\resumeItem`, `\resumeSubheading`, `\resumeSubHeadingListStart`/`End`, `\resumeItemListStart`/`End`, `\resumeSubItem`.
- English CV: `\documentclass[letterpaper,11pt]{article}`, no `fontspec`/`ctex`.
- Chinese CV: `\documentclass[a4paper,10pt]{article}`, requires `fontspec` and `ctex` packages.
- Escape `%`, `&`, `$`, `#`, `_`, `{`, `}` properly in LaTeX content.
- Keep CVs ATS-parsable — no images, no multi-column layouts, use `\href` for links.

## When Editing CVs

- Never change the preamble (packages, custom commands, margins) unless explicitly asked.
- Preserve the section order unless reordering is specifically requested.
- Keep all facts truthful — do not fabricate experience, metrics, or skills.
- For Chinese CV, all content must be in Chinese except company names, technical terms, and proper nouns.
- Use `\resumeItem{Title}{Description}` for bullet points under a role.
- Use `\resumeSubItem{Title}{Description}` for items in the Additional Information section.

## When Editing Scripts

- `scripts/customize_cv.py` uses the OpenAI Python SDK v1+. Keep `OPENAI_API_KEY` from environment only.
- Job files use YAML frontmatter between `---` delimiters, parsed with PyYAML.
- Output filenames are slugified: `{company}_{role}_en.tex`.

## When Editing Workflows

- `cv.yml`: English CV uses `pdflatex`, Chinese CV uses `xelatex`. Both via `xu-cheng/latex-action@v3`.
- `customize.yml`: Only triggers on `jobs/*.md` changes. Uses path filter + `git diff` to detect new JDs.
- Auto-commit messages must include `[skip ci]` to prevent infinite loops.
- The `OPENAI_API_KEY` secret must be referenced as `${{ secrets.OPENAI_API_KEY }}`.

## Build Commands

- **Local Docker:** `./build.sh`
- **Local customization:** `OPENAI_API_KEY=sk-... python scripts/customize_cv.py jobs/some_role.md`
- **CI:** Push to `main` triggers automatic compilation.
- **Release:** `git tag v1.0.0 && git push --tags`
