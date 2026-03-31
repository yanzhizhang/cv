Prepare a release for the CV repository.

Steps:
1. Run `git status` to check for uncommitted changes. If any, list them and ask to commit first.
2. Run `git log --oneline -10` to show recent history.
3. Suggest the next version tag based on existing tags (`git tag --list 'v*' --sort=-v:refname | head -5`).
4. Show the user the proposed tag and ask for confirmation.
5. Remind the user to run `git tag <version> && git push --tags` to trigger the release workflow.

Do NOT run `git push` or `git tag` without explicit user confirmation.
