#!/usr/bin/env python3
"""
Customize a base CV for a specific job description using OpenAI GPT-4o.

Usage:
    python scripts/customize_cv.py jobs/company_role.md

Requires:
    OPENAI_API_KEY environment variable set.
    pip install openai pyyaml
"""

import argparse
import os
import re
import sys
from pathlib import Path

import yaml
from openai import OpenAI

REPO_ROOT = Path(__file__).resolve().parent.parent
BASE_CV_PATH = REPO_ROOT / "yanzhi_zhang_cv_en.tex"
OUTPUT_DIR = REPO_ROOT / "customized"

SYSTEM_PROMPT = """\
You are an expert LaTeX CV editor. You will receive:
1. A base CV in LaTeX format.
2. A job description for a target role.

Your task is to produce a TAILORED version of the CV that maximizes the candidate's \
fit for the target role. Follow these rules strictly:

CONTENT RULES:
- Reorder sections and bullet points to put the most relevant experience first.
- Rewrite bullet points to emphasize skills and achievements that match the job \
description's requirements and keywords. Use the terminology from the JD where truthful.
- You may condense or remove less relevant items to keep the CV concise (target ~1 page, \
max 2 pages). Prioritize recent and relevant roles.
- NEVER fabricate experience, skills, certifications, or metrics. Every claim must be \
supported by the base CV.
- Keep all dates, company names, job titles, and education details exactly as they appear \
in the base CV.

LATEX RULES:
- Output ONLY the complete, valid LaTeX document. No markdown, no explanations, no commentary.
- Preserve the exact preamble (everything before \\begin{document}) unchanged.
- Use only the custom commands defined in the preamble (\\resumeItem, \\resumeSubheading, \
\\resumeSubHeadingListStart, etc.). Do not define new commands.
- Ensure all braces, environments, and special characters are properly escaped.
- The output must compile successfully with pdflatex.

FORMAT:
- Output the LaTeX source code directly. Do not wrap it in code fences or any other markup.
"""

USER_PROMPT_TEMPLATE = """\
## Base CV (LaTeX)

```latex
{base_cv}
```

## Target Job Description

**Company:** {company}
**Role:** {role}
**URL:** {url}

{jd_body}

## Instructions

Produce the tailored LaTeX CV now. Output ONLY the LaTeX source code, nothing else.
"""


def parse_job_file(job_path: Path) -> dict:
    """Parse a job description markdown file with YAML frontmatter."""
    text = job_path.read_text(encoding="utf-8")

    # Split YAML frontmatter from body
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", text, re.DOTALL)
    if not match:
        print(f"Error: {job_path} missing YAML frontmatter (---/--- block)", file=sys.stderr)
        sys.exit(1)

    frontmatter = yaml.safe_load(match.group(1))
    body = match.group(2).strip()

    return {
        "company": frontmatter.get("company", "Unknown"),
        "role": frontmatter.get("role", "Unknown"),
        "url": frontmatter.get("url", ""),
        "lang": frontmatter.get("lang", "en"),
        "body": body,
    }


def slugify(text: str) -> str:
    """Convert text to a filesystem-safe slug."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "_", text)
    return text.strip("_")


def customize_cv(base_cv: str, job: dict, api_key: str) -> str:
    """Call OpenAI GPT-4o to produce a tailored CV."""
    client = OpenAI(api_key=api_key)

    user_prompt = USER_PROMPT_TEMPLATE.format(
        base_cv=base_cv,
        company=job["company"],
        role=job["role"],
        url=job["url"],
        jd_body=job["body"],
    )

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.3,
        max_tokens=16000,
    )

    content = response.choices[0].message.content

    # Strip code fences if the model wraps output despite instructions
    content = re.sub(r"^```(?:latex)?\s*\n", "", content)
    content = re.sub(r"\n```\s*$", "", content)

    return content


def main():
    parser = argparse.ArgumentParser(description="Customize CV for a job description")
    parser.add_argument("job_file", type=Path, help="Path to job description .md file")
    parser.add_argument(
        "--base-cv",
        type=Path,
        default=BASE_CV_PATH,
        help="Path to base CV .tex file",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=OUTPUT_DIR,
        help="Output directory for customized CVs",
    )
    args = parser.parse_args()

    # Validate inputs
    if not args.job_file.exists():
        print(f"Error: Job file not found: {args.job_file}", file=sys.stderr)
        sys.exit(1)
    if not args.base_cv.exists():
        print(f"Error: Base CV not found: {args.base_cv}", file=sys.stderr)
        sys.exit(1)

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable not set", file=sys.stderr)
        sys.exit(1)

    # Parse inputs
    job = parse_job_file(args.job_file)
    base_cv = args.base_cv.read_text(encoding="utf-8")

    slug = slugify(f"{job['company']}_{job['role']}")
    print(f"Customizing CV for: {job['company']} — {job['role']}")
    print(f"Slug: {slug}")

    # Call LLM
    customized_tex = customize_cv(base_cv, job, api_key)

    # Basic validation: must contain \begin{document} and \end{document}
    if r"\begin{document}" not in customized_tex or r"\end{document}" not in customized_tex:
        print("Warning: LLM output may be incomplete (missing document environment)", file=sys.stderr)

    # Write output
    args.output_dir.mkdir(parents=True, exist_ok=True)
    output_path = args.output_dir / f"{slug}_en.tex"
    output_path.write_text(customized_tex, encoding="utf-8")
    print(f"Written: {output_path}")


if __name__ == "__main__":
    main()
