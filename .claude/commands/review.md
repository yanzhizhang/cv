Review and proofread a CV `.tex` file for issues.

Check for:
1. **LaTeX errors**: Unmatched braces, unclosed environments, unescaped special characters (`%`, `&`, `$`, `#`, `_`, `{`, `}`).
2. **Structural issues**: Missing `\resumeItemListEnd`, mismatched `\resumeSubHeadingListStart`/`End` pairs.
3. **Content issues**: Inconsistent date formats, missing descriptions, overly long bullet points.
4. **ATS compatibility**: No images, no multi-column layouts, links use `\href`.
5. **Spelling and grammar**: Check English text for typos and awkward phrasing.

Read the target `.tex` file (default: `yanzhi_zhang_cv_en.tex`) and report all findings with line numbers. Suggest fixes but do not apply them without confirmation.
