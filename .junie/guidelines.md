# Project Development Guidelines (agopalareddy.github.io)

This repository is a Jekyll site based on the academicpages/minimal-mistakes stack, configured for GitHub Pages. It uses:
- Ruby + Bundler (via the `github-pages` meta-gem) to build and serve the site.
- A small Node-based pipeline to concatenate and minify theme JavaScript into `assets\js\main.min.js`.
- Optional Python helpers in `markdown_generator` for generating Markdown from TSV/other sources.

These notes focus on repo-specific behavior, plugins, and reliable local workflows on Windows.

## 1) Build and Configuration

Prerequisites (Windows):
- Ruby (prefer RubyInstaller for Windows with MSYS2/DevKit). `github-pages` will pin Jekyll and plugin versions.
- Bundler (`gem install bundler` if missing).
- Node.js (14+ recommended) for the JS pipeline.

Gems of note (see `Gemfile`):
- `github-pages` (drives the exact Jekyll/plugins set used by GitHub Pages),
- `webrick` (needed for Ruby 3 local serving),
- `wdm` (Windows file watching),
- `tzinfo`, `tzinfo-data` (Windows time zone support),
- Plugins used in-site: `jekyll-sitemap`, `jekyll-feed`, `jekyll-redirect-from`, `jekyll-last-modified-at`, and others. `jekyll-archives` is present in the Gemfile but is not enabled in `_config.yml` by default.

Node pipeline (see `package.json`):
- `npm run build:js` (alias for `npm run uglify`) concatenates and minifies JS listed in `scripts.uglify` into `assets\js\main.min.js`.
- `npm run watch:js` uses `onchange` to rebuild when JS sources under `assets\js` change.

Initial setup (PowerShell):
- Clean and install Ruby dependencies (matching GitHub Pages versions):
  - `bundle clean`
  - `bundle install`
- Install Node deps (if you need to rebuild JS):
  - `npm install`

Serving locally:
- Recommended dev run with livereload and dev overrides from `_config.dev.yml`:
  - `bundle exec jekyll serve --livereload --config _config.yml,_config.dev.yml`
- Optional/legacy alternative (hawkins liveserve) exists but is not recommended; prefer the built-in `bundle exec jekyll serve --livereload --config _config.yml,_config.dev.yml`.

Dev configuration overrides (`_config.dev.yml`):
- Sets `url: http://localhost:4000`, disables analytics in dev, and expands Sass for easier debugging. These are merged with `_config.yml` when passed via `--config`.

Build for inspection (no server):
- `bundle exec jekyll build --config _config.yml,_config.dev.yml`
- Output is written to `_site`. This matches what GitHub Pages will produce (modulo the dev overrides you pass).

Deployment context:
- Because `github-pages` pins versions to the GitHub Pages environment, using `bundle exec` locally closely mirrors production.
- GitHub Pages does not execute your Node pipeline; if you change JS sources that affect `assets\js\main.min.js`, commit the built `main.min.js` so production sees the update.

## 2) Testing

The repo does not include a formal automated test suite; practical smoke tests are recommended to guard the critical paths: the JS bundle and the Jekyll build.

Verified example (JS build smoke test):
- Command executed and verified during guideline creation:
  - `npm run build:js`
- Expected result:
  - `assets\js\main.min.js` exists and is non-empty; timestamps update when inputs change.
  - Console shows the `uglifyjs` invocation completing without errors.

How to add/run further checks:
- JS pipeline:
  - After editing any file under `assets\js`, run `npm run build:js`. If you add new vendor/plugins, update the command in `package.json -> scripts.uglify` to include the new file(s) in the correct order.
  - For iterative work, use `npm run watch:js` to auto-rebuild on changes.
- Jekyll build integrity:
  - Run `bundle exec jekyll build --config _config.yml,_config.dev.yml --verbose` and watch for build errors/warnings.
  - Sanity-check that `_site\index.html` and key pages are generated. You can diff `_site` between commits if desired.
- Content addition sanity check (manual):
  - Add a small draft or a dated post with required front matter under `_posts` (see Additional Development Info below for defaults), build locally, and confirm routing and layout.
- Optional CI idea (not included in repo):
  - A GitHub Actions workflow that runs `bundle exec jekyll build` and (optionally) `npm run build:js` can prevent broken builds from being pushed.

Notes for Windows:
- File watching uses `wdm`; if file changes aren’t detected, ensure `wdm` is installed (Bundler handles it from the Gemfile) and run PowerShell/Terminal with appropriate permissions.
- If you see `cannot load such file -- webrick`, ensure `webrick` is installed (present in Gemfile) and that you’re using `bundle exec`.
- If `bundle install` reports version conflicts, deleting `Gemfile.lock` and trying again is acceptable per this project’s README.

## 3) Additional Development Information

Content structure highlights:
- Pages and collections:
  - `_pages`, `_posts`, `_projects`, `_publications`, `_portfolio`, `_talks`, `_teaching` (and more) are present; defaults for layouts/flags are defined under `defaults:` in `_config.yml`.
  - Permalinks: `/:categories/:title/`.
- Front matter conventions (see `_config.yml -> defaults`):
  - Many content types default to `layout: single` and `author_profile: true`. Some types enable `share` and `comments` by default.
  - Talks use `layout: talk`.
- Plugins configured in `_config.yml`:
  - `jekyll-paginate`, `jekyll-sitemap`, `jekyll-gist`, `jekyll-feed`, `jekyll-redirect-from`, `jekyll-last-modified-at`.
  - A whitelist is set to mimic GitHub Pages `--safe` behavior.
  - Archives are configured via Liquid (`category_archive`/`tag_archive`). The `jekyll-archives` plugin is installed but commented out in config; enable it if you want plugin-driven archives.
- Sass:
  - Source under `_sass`; output style defaults to `compressed` (overridden to `expanded` in dev via `_config.dev.yml`).
- Assets/JS:
  - The minified bundle `assets\js\main.min.js` is the only output of the Node pipeline. The concatenation order is explicitly set in `package.json` and should be maintained to preserve dependency order (e.g., jQuery first, then plugins, then `_main.js`).
- Data/content generators:
  - `markdown_generator\*.py` and `*.ipynb` can generate Markdown for projects, publications, and talks from TSV/Bib files. Use Python 3 and review each script’s `readme.md` for input and output conventions.
- Analytics/SEO:
  - Analytics provider is set to `custom` or disabled in dev. `jekyll-sitemap` and `jekyll-feed` are enabled by default.

Common pitfalls and tips:
- Always run Jekyll via `bundle exec` to respect the pinned versions from `github-pages`.
- If local serve fails after updates, try: `bundle clean`, delete `Gemfile.lock`, then `bundle install`.
- When adding a new content type or changing defaults, update `_config.yml -> defaults` accordingly to keep layouts consistent.
- Since GitHub Pages doesn’t run Node tasks, remember to commit updated `assets\js\main.min.js` after JS changes.

---

Quick command reference (PowerShell):
- One-time setup: `bundle install`, `npm install`
- Dev server: `bundle exec jekyll serve --livereload --config _config.yml,_config.dev.yml`
- Build (no serve): `bundle exec jekyll build --config _config.yml,_config.dev.yml`
- JS build: `npm run build:js`
- JS watch: `npm run watch:js`

Verified now: `npm run build:js` succeeds and updates `assets\js\main.min.js`.
