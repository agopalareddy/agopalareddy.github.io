# Markdown Generator Helpers

This repository includes optional helpers under `markdown_generator/` to generate Markdown from TSV, BibTeX, and other sources for projects, publications, and talks.

Use Python 3. Steps below assume PowerShell on Windows (paths use backslashes).

## Folders and Inputs
- `markdown_generator/` contains scripts and example notebooks:
  - `projects.py`, `publications.py`, `talks.py` (names may vary) and corresponding `readme.md`
  - Example inputs like `*.tsv` or `*.bib`
- Outputs are written into the corresponding collections:
  - `_projects/`, `_publications/`, `_talks/`

Review each script’s `readme.md` for the expected columns/fields. Typical TSV fields include: title, venue, date (YYYY-MM-DD), authors, and links.

## One-time setup
- Install Python 3
- Create a virtual environment (optional but recommended)
- Install any dependencies listed in `markdown_generator/readme.md` or individual script docs

## How to run
1. Prepare your input file(s), e.g. `markdown_generator\publications.tsv`.
2. Run the generator (example):
   - `python markdown_generator\publications.py --input markdown_generator\publications.tsv --out _publications`
3. Inspect generated Markdown files in the target collection folder.
4. Build locally to verify:
   - `bundle exec jekyll build --config _config.yml,_config.dev.yml`

## Idempotency and Safety
- Generators should be idempotent: running them multiple times with the same inputs should not produce duplicate documents.
- To avoid overwriting manual edits:
  - Prefer generating new files rather than editing existing ones in-place.
  - If updating existing files, ensure the script preserves unknown front matter keys and custom content blocks.
  - Consider keeping the TSV/Bib as the source of truth and avoid manual edits in generated files. If manual edits are needed, document them and exclude those files from regeneration.

## Recommended Workflow
- Edit or update TSV/Bib inputs under `markdown_generator/`.
- Re-run the generator for the specific collection.
- Review diffs in Git to confirm only intended changes.
- Commit the updated Markdown files along with the inputs used to produce them.

## Troubleshooting
- If dates render incorrectly, confirm the site timezone in `_config.yml` and date formats in inputs.
- If links are broken, re-run the build with `--verbose` and fix paths.
- For Windows line endings, ensure `.editorconfig` is respected by your editor.
