# Project Improvement Plan

Date: 2025-08-21
Scope: agopalareddy.github.io (Jekyll site using Minimal Mistakes/academicpages, GitHub Pages deployment, Node-based JS minification pipeline)
Source Basis: Inferred from repository state (README.md, _config.yml), docs/tasks.md, and the provided Windows-oriented development guidelines. GitHub Pages environment and best practices guide the constraints.

---

## Executive Summary
This plan outlines a pragmatic, low-risk modernization and hardening of the site’s build pipeline, content structure, and operational practices. It focuses on:
- Reliability and reproducibility of local and GitHub Pages builds
- Modernizing the JS pipeline while preserving compatibility
- Improving SEO, performance, and accessibility
- Establishing contribution, governance, and CI checks
- Clarifying comments/analytics decisions and privacy

The plan is organized by theme, with each section including rationale, proposed changes, and cross-references to the actionable checklist in docs/tasks.md.

---

## Goals
- Maintain a stable, GitHub Pages-compatible Jekyll site that builds cleanly on Windows using bundle exec with pinned github-pages versions.
- Keep production behavior aligned with local builds; commit generated assets that GitHub Pages will not build (e.g., minified JS).
- Reduce bundle size and improve site performance and accessibility.
- Standardize content IA and defaults to ensure consistent layouts and metadata.
- Establish lightweight CI to catch build/link issues before merging.
- Document clear contributor workflows and formatting conventions.

## Constraints and Assumptions
- GitHub Pages environment pins Jekyll/plugins via the github-pages gem; only safe/whitelisted plugins run in production.
- Node-based tasks do not run on GitHub Pages; artifacts like assets\js\main.min.js must be committed.
- Primary developer environment is Windows; use PowerShell-friendly commands and ensure file watching via wdm.
- Keep dependency surface minimal; prefer defaults and Liquid-driven archives over extra plugins unless justified.
- Avoid breaking URLs; use jekyll-redirect-from for any slug/permalink changes.

---

## 1) Build and Tooling (Ruby/Jekyll)
Rationale: Stable local builds that mirror production reduce surprises and speed iteration.
Proposed Changes:
- Enforce running Jekyll via bundle exec; document Windows-friendly commands (serve --livereload with --config _config.yml,_config.dev.yml).
- Ensure Gemfile includes webrick (Ruby 3) and wdm (Windows watching) — already present; keep.
- If jekyll-archives isn’t enabled in _config.yml, consider removing the gem to reduce surface area unless we add archive layouts (see Archives section).
- Keep timezone accurate in _config.yml for correct timestamps.
Related tasks: 2, 7, 38, 39, 48, 50.

---

## 2) JavaScript Pipeline Modernization
Rationale: Current uglify-js v2 is outdated and may struggle with modern JS. A predictable, minimal bundle reduces bugs and improves load time.
Proposed Changes:
- Update Node engine in package.json to ">=14" and migrate from uglify-js v2 to terser (or uglify-js v3) while preserving exact concatenation order.
- Keep jQuery first, then plugins, then assets/js/_main.js.
- Provide npm scripts: build:js (default), watch:js, and a convenience build script that also runs a Jekyll build for local verification.
- Commit assets\js\main.min.js after any JS changes because GitHub Pages won’t build it.
- Optional: Add ESLint (browser, jquery) and Prettier for consistency; add npm run lint and document usage.
Related tasks: 10, 11, 12, 13, 14, 15, 16, 44.

---

## 3) CSS/Sass Structure and Quality
Rationale: Organized Sass and basic linting prevent regressions and ease maintenance.
Proposed Changes:
- Keep dev Sass output expanded (_config.dev.yml) and production compressed.
- Review partial structure and centralize variables/mixins.
- Optional: Add stylelint with a minimal config for SCSS; add npm run lint:css.
Related tasks: 17, 18.

---

## 4) Information Architecture and Content Conventions
Rationale: Consistent metadata, permalinks, and collection defaults ensure predictable rendering and SEO.
Proposed Changes:
- Clarify defaults in _config.yml: where comments/share are on by default per collection; align to chosen comments strategy (see Section 7).
- Verify tag and category archive pages exist under _pages to match Liquid-driven archives config.
- Review permalink structure for consistency; add redirects for any changes.
- Update CONTRIBUTING.md with front matter conventions, categories/tags guidance, and file placement rules.
Related tasks: 3, 4, 8, 25, 26, 41, 49.

---

## 5) SEO, Social, and Metadata
Rationale: Filled-in metadata improves discoverability and social sharing previews.
Proposed Changes:
- Populate description, social.links, twitter username, and og_image in _config.yml.
- Populate author social fields (GitHub, LinkedIn, Scholar/ORCID if applicable) for richer JSON-LD.
- Optionally add site-level Person/Organization JSON-LD via an include using _config.yml fields.
- Verify jekyll-sitemap and jekyll-feed outputs.
Related tasks: 5, 28, 29.

---

## 6) Performance and Accessibility
Rationale: Faster, accessible pages improve UX and search ranking.
Proposed Changes:
- Audit with Lighthouse; defer/async non-critical scripts and preconnect to required origins (e.g., fonts).
- Adopt responsive images (srcset/sizes), lazy-load non-critical images, and include width/height attributes to reduce CLS.
- Ensure descriptive alt text; verify heading hierarchy, color contrast, focus outlines; add a skip-to-content link if missing.
- Minimize unused JS/CSS and consider removing unused plugins (e.g., magnific-popup) if not used.
Related tasks: 14, 19, 20, 21, 22, 23, 40.

---

## 7) Comments Strategy
Rationale: Avoid broken embeds and unnecessary trackers; clarify behavior across environments.
Proposed Changes:
- Decide between Disqus/Staticman or disabling comments by default.
- Ensure _config.dev.yml disables analytics and comments.
- If using Disqus, set shortname per environment and enable intentionally; otherwise set comments defaults to false where appropriate.
Related tasks: 4, 9, 27, 46.

---

## 8) Analytics and Privacy
Rationale: Transparent analytics aligned with user expectations and development hygiene.
Proposed Changes:
- Choose analytics provider (Google, custom, or none). Keep disabled in development via _config.dev.yml.
- Document the choice in README.
Related tasks: 27.

---

## 9) CI/CD and Quality Gates
Rationale: Lightweight CI prevents broken builds and regressions on PRs.
Proposed Changes:
- Add GitHub Actions workflow to run bundle exec jekyll build and npm run build:js on pull requests (no deploy).
- Optionally add html-proofer for internal link/image/HTML checks with allowlists.
- Add a simple PowerShell smoke-test script to run JS build and Jekyll build and verify _site\index.html exists.
Related tasks: 30, 31, 33.

---

## 10) Data/Content Generators
Rationale: Safe, repeatable generation avoids overwriting manual edits.
Proposed Changes:
- Document markdown_generator scripts (inputs, outputs, and steps) and ensure outputs are idempotent.
- Consider storing source-of-truth data under data/ with clear regeneration guidance.
Related tasks: 34, 35.

---

## 11) Repository Hygiene and Governance
Rationale: Consistent developer experience and maintainability.
Proposed Changes:
- Add/verify .editorconfig and .gitattributes for line endings and whitespace.
- Update .gitignore to exclude transient artifacts (.jekyll-cache, .DS_Store, Thumbs.db, notebook checkpoints).
- Add repository labels and issue templates to triage content vs. code changes.
- Add LICENSE/NOTICE section in README acknowledging theme and any assets licenses.
- Provide pre-commit guidance to run JS and Jekyll builds; optionally add Husky hooks for linting if Node tooling is adopted.
- Create a backup/export plan describing how to restore the site on a new machine.
Related tasks: 1, 36, 37, 43, 44, 42.

---

## 12) Archives and Taxonomy
Rationale: Archive pages must align with configuration to avoid broken links.
Proposed Changes:
- Use Liquid-driven archives as configured (category_archive, tag_archive) and ensure matching pages exist under _pages.
- If richer plugin-driven archives are desired, enable jekyll-archives in _config.yml and add layouts; otherwise remove the gem from Gemfile to slim dependencies.
Related tasks: 7, 8.

---

## 13) Pagination
Rationale: Keep navigation consistent and performant.
Proposed Changes:
- Verify whether pagination is needed; if enabled, configure paginate_path accordingly and ensure templates support it.
Related tasks: 39.

---

## 14) External Dependencies and Third-Party Scripts
Rationale: Privacy, performance, and reliability.
Proposed Changes:
- Audit external fonts/embeds; preconnect where needed; reduce third-party scripts to the minimum.
- Evaluate jemoji usage: enable if desired or remove from whitelist to avoid confusion.
Related tasks: 6, 40.

---

## Risks and Mitigations
- Plugin incompatibility with GitHub Pages: adhere to github-pages gem versions; test locally with bundle exec.
- JS minifier migration issues: preserve concatenation order; verify resulting main.min.js integrity; keep rollback path to legacy uglify.
- URL changes: use jekyll-redirect-from to avoid broken links.
- Windows file watching issues: ensure wdm is present and documented.

---

## Milestones and Suggested Sequence
1. Repo hygiene and documentation updates (README, CONTRIBUTING, .editorconfig/.gitattributes, .gitignore).
2. Decide comments/analytics strategy; update _config.yml defaults and _config.dev.yml.
3. JS pipeline modernization (Node engines, terser; update scripts); commit built assets.
4. IA and archives: verify _pages archives, pagination decision, permalink review with redirects as needed.
5. SEO/social metadata population; optional JSON-LD include.
6. Performance/accessibility pass (images, lazy-loading, Lighthouse-driven tweaks).
7. CI setup (build + optional html-proofer) and smoke-test script.
8. Document markdown_generator usage and ensure idempotency.

---

## Success Criteria and Measurement
- Local build (bundle exec jekyll build --config _config.yml,_config.dev.yml) completes without warnings; JS build succeeds; _site\index.html exists.
- Lighthouse scores improve for Performance, Accessibility, Best Practices, and SEO; CLS reduced via width/height attributes.
- PRs trigger CI and fail on build errors; optional html-proofer passes for internal links/images.
- README and CONTRIBUTING provide clear, Windows-friendly workflows; contributors can reproduce builds.
- JS bundle size reduced if unused plugins are removed; no regressions in site behavior.

---

## References
- GitHub Pages / github-pages gem versioning
- Minimal Mistakes / academicpages documentation
- Jekyll plugins used: jekyll-sitemap, jekyll-feed, jekyll-redirect-from, jekyll-last-modified-at, jekyll-paginate
- Node pipeline: terser or modern uglify-js v3; onchange for watch
