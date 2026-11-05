<!-- One topic per PR. Title in Conventional Commits form: feat(scope): ..., fix(scope): ..., docs: ... -->

## What

<!-- One or two sentences: what changes and why. Link the issue if there is one: Closes #123 -->

## How

<!-- Anything a reviewer needs to know: design choices, alternatives rejected, follow-ups left out. -->

## Screenshots

<!-- Required for changes to the clip page: before/after. Delete this section otherwise. -->

## Checklist

- [ ] `flake8`, `black --check` and `pytest -q` pass (see CONTRIBUTING.md)
- [ ] New behaviour and bug fixes come with tests (a bug fix with a regression test that fails without the fix)
- [ ] New commands are hybrid (`!name` and `/name`) and have an entry in the locales and in `docs/source/commands.md`
- [ ] Docs in `README.md` and `docs/source/` and `CHANGELOG.md` updated when behaviour or configuration changes
- [ ] No Discord token, API key or private URL in the diff or the screenshots
