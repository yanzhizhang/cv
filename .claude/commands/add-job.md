Create a new job description file from the template.

1. Ask for the company name, role title, and job posting URL.
2. Copy `jobs/_template.md` to `jobs/{company}_{role}.md` (slugified, lowercase, underscores).
3. Fill in the YAML frontmatter with the provided company, role, and URL.
4. If the user provides JD text, paste it into the body section.
5. Remind the user to push to `main` to trigger the AI customization workflow.

Slugify rules: lowercase, replace spaces with underscores, remove special characters.
Example: "Google" + "Senior SWE" → `jobs/google_senior_swe.md`
