# Yanzhi Zhang — CV Factory

LaTeX-based CV with automated compilation. Push your edits → GitHub Actions compiles PDFs → auto-committed back to `main`.

## Files

| File | Language | Compiler |
|------|----------|----------|
| `yanzhi_zhang_cv_en.tex` | English | `pdflatex` |
| `yanzhi_zhang_cv_cn.tex` | Chinese | `xelatex` |

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

## License

Format is MIT. All data is owned by Yanzhi Zhang.
