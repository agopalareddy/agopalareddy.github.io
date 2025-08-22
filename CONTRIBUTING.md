Contributions are welcome! Please add issues and make pull requests. There are no stupid questions. All ideas are welcome. This is a volunteer project. Be excellent to each other.

Fork from master and go from there. This repository is intended to remain a generic, ready-to-fork template that demonstrates the features of academicpages.

If you make a pull request and change code, please make sure there is a closed issue tagged with 'code change' that has some comment linking to either the single commit (if the change was just one commit) or a diff comparing before/after the change (see [issue 21](https://github.com/academicpages/academicpages.github.io/issues/21) for example). This is so that those who have forked this repo and modified it for their purposes can more easily patch bugs and new features.

---

## Content conventions

To keep content consistent and easy to maintain, please follow these conventions.

- File locations
  - Pages: `_pages/` (top-level pages like about, cv). Use front matter `layout: single` unless a specialized layout is needed.
  - Posts: `_posts/` named `YYYY-MM-DD-title.md`. Posts inherit defaults set in `_config.yml`.
  - Collections: `_projects/`, `_publications/`, `_talks/`, `_teaching/`, `_portfolio/` with one Markdown file per item.
  - Assets: images under `images/` or collection-specific folders; downloadable files under `files/`.

- Front matter defaults (from `_config.yml`)
  - Layout: most content uses `layout: single` (talks use `layout: talk`).
  - Author profile: `author_profile: true` by default on most content types.
  - Comments: disabled by default site-wide. If a comments provider is configured in the future, you may opt-in per page with `comments: true`.
  - Sharing buttons: enabled for many types (see `_config.yml -> defaults`). Override per page with `share: true|false`.

- Categories and tags
  - Use lower-case, dash-separated slugs (e.g., `machine-learning`, `nlp`).
  - Categories affect URL structure (`/:categories/:title/`). Tags are optional and useful for discovery.

- Permalinks
  - The site uses `/:categories/:title/`. Avoid changing slugs; if you must, add `redirect_from:` entries to preserve old URLs.

- Images and accessibility
  - Always include meaningful `alt` text.
  - Prefer adding `width` and `height` attributes to reduce layout shift (CLS).
  - Use responsive images (`srcset`, `sizes`) for large media where appropriate.

- JavaScript and CSS
  - If you change any files under `assets/js`, run `npm run build:js` and commit the generated `assets/js/main.min.js` (GitHub Pages does not run Node tasks).
  - Keep Sass under `_sass/`; dev builds use expanded output for easier debugging.

## Local development

- Use Bundler to mirror the GitHub Pages environment:
  - One-time setup: `bundle install`, `npm install`
  - Live server: `bundle exec jekyll liveserve --config _config.yml,_config.dev.yml`
  - Build only: `bundle exec jekyll build --config _config.yml,_config.dev.yml`
  - JS build: `npm run build:js` (or `npm run build` to build JS and Jekyll together)

## Comments strategy

- Comments are disabled by default in `_config.yml` and in development via `_config.dev.yml`.
- If you plan to enable Disqus or another provider, document the provider configuration and only enable `comments: true` on specific pages.

## JavaScript linting and formatting

To keep code quality consistent and avoid style drift, please use the following tools:

- Lint JavaScript (ESLint):
  - Install deps: `npm install`
  - Run linter: `npm run lint`
  - Scope: Lints our main custom file `assets/js/_main.js` (vendor/plugins and minified files are ignored).
- Format code (Prettier):
  - Run formatter: `npm run format`
  - Scope: Formats `assets/js/_main.js`. Do not format vendor or minified files.

If you modify `assets/js/_main.js`, after linting/formatting, rebuild and commit the bundle `assets/js/main.min.js` using `npm run build:js` because GitHub Pages does not run Node tasks.

## Pull request guidelines

- Keep changes scoped and include a brief rationale in the PR description.
- Follow repository formatting (.editorconfig) and platform norms.
- For content additions, ensure front matter is present and follows the conventions above.
