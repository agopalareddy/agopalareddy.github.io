1. [x] Repository hygiene: add/verify .editorconfig and .gitattributes for consistent line endings (LF vs CRLF) and whitespace across Windows/macOS/Linux.
2. [x] Update README.md with Windows-friendly local workflow from guidelines (bundle exec jekyll liveserve --config _config.yml,_config.dev.yml; npm run build:js; troubleshooting tips for webrick/wdm).
3. [x] Add a CONTRIBUTING.md section on content conventions (front matter defaults, categories/tags, file locations for pages vs. collections).
4. [x] Establish a clear comments strategy: either configure Staticman/Disqus or disable comments by default in _config.yml and per-collection defaults.
5. [x] Fill in SEO/social metadata in _config.yml (site description, social.links, twitter username, og_image) and verify jekyll-sitemap/jekyll-feed output.
6. [x] Decide whether to enable the jemoji plugin (it is whitelisted but not enabled) or remove it from whitelist to reduce confusion.
7. [x] Review necessity of jekyll-archives: either enable it with proper layouts or remove the gem from Gemfile to reduce build surface area.
8. [x] Create/verify tag and category archive pages under _pages that match category_archive/tag_archive config (Liquid-driven archives).
9. [x] Ensure _config.dev.yml turns off analytics and comments provider for local dev; align with chosen comments strategy.
10. [x] Modernize Node toolchain: update engines.node (>=14) in package.json and plan migration from uglify-js v2 to terser or uglify-js v3 for ES compatibility.
11. [x] Replace legacy uglify script with a terser-based build (keeping exact concat order) and verify assets\js\main.min.js builds identically/minimally.
12. [x] Add an npm script alias "build" that runs both JS build and a Jekyll build for local inspection (document in README).
13. [x] Ensure assets\js\main.min.js is committed (since GitHub Pages won’t run Node); document this requirement in README.
14. [x] Audit assets/js/plugins and vendor usage; remove unused plugins (e.g., magnific-popup if not used) to shrink JS bundle size.
15. [x] Add ESLint with a minimal config (browser, jquery) to catch common JS issues; integrate as npm script (npm run lint).
16. [x] Add Prettier (or EditorConfig-only) for consistent code style; document formatting conventions in CONTRIBUTING.md.
17. [x] Review Sass structure under _sass; group partials logically and ensure variables/mixins are centralized; keep dev output expanded via _config.dev.yml.
18. [x] Add a simple stylelint config to catch Sass/CSS issues; integrate as npm script (npm run lint:css) if desired.
19. [ ] Optimize image assets: lossless compression of images/ and creation of appropriately sized variants where needed.
20. [ ] Adopt responsive images for large hero/portfolio media (srcset/sizes) and lazy-load (loading="lazy") where it doesn’t impact LCP.
21. [ ] Add width/height attributes to images to reduce CLS; ensure alt text is present and meaningful on all images.
22. [ ] Accessibility pass: verify heading hierarchy, color contrast, focus outlines, link text clarity, and add skip-to-content link in layout if missing.
23. [ ] Performance pass: audit with Lighthouse; defer or async non-critical scripts, preconnect to required origins (e.g., fonts), and minimize unused CSS/JS.
24. [x] Add a 404 page (if missing) and ensure it inherits site navigation and has helpful links.
25. [ ] Verify talk/project/publication collection layouts render required metadata; adjust defaults to set author_profile/share/comments appropriately per type.
26. [ ] Review permalink structure and existing content slugs for consistency and backward compatibility; add jekyll-redirect-from where URLs changed.
27. [ ] Decide on analytics provider (Google, custom, or none) and configure it; ensure analytics disabled in development via _config.dev.yml.
28. [ ] Populate author and social profile fields in _config.yml (GitHub, LinkedIn, Scholar, ORCID as applicable) for richer SEO JSON-LD.
29. [ ] Add structured data (JSON-LD) for Person/Organization in head include if desired, using fields from _config.yml.
30. [ ] Configure a GitHub Actions workflow to run bundle exec jekyll build and npm run build:js on pull requests to catch build errors (no deploy).
31. [ ] Optionally extend CI with html-proofer to check internal links, images, and HTML validity; allowlist external domains as needed.
32. [ ] Enable Dependabot (or Renovate) for Ruby and Node dependencies to surface security and update PRs.
33. [ ] Add a basic smoke-test script (PowerShell) that runs npm run build:js and bundle exec jekyll build --config _config.yml,_config.dev.yml and validates _site index exists.
34. [ ] Document the markdown_generator scripts: inputs (TSV/Bib), outputs, and a step-by-step guide to regenerate content safely.
35. [ ] Ensure markdown_generator outputs are idempotent and don’t overwrite manual edits; consider adding a data/ source-of-truth note.
36. [ ] Update .gitignore to exclude transient artifacts (e.g., .DS_Store, Thumbs.db, .jekyll-cache) and notebook checkpoints.
37. [ ] Add repository labels and issue templates for content requests vs. code changes to streamline contributions.
38. [x] Review timezone setting in _config.yml; set to the site owner’s actual timezone to ensure correct timestamps.
39. [ ] Verify pagination usage (jekyll-paginate) or remove if not needed; configure paginate_path if enabled.
40. [ ] Evaluate using minimal number of third-party scripts; audit external calls (fonts, embeds) for privacy/performance.
41. [ ] Ensure breadcrumbs and navigation reflect actual IA; update _data/navigation.yml (if present) or _includes to match desired structure.
42. [ ] Create a backup/export plan for assets and content (at minimum document how to restore site from repo on a new machine).
43. [ ] Add a LICENSE and NOTICE section in README summarizing theme attribution (already present) and any additional assets’ licenses.
44. [ ] Add pre-commit guidance (optional): run npm run build:js and jekyll build locally before pushing; consider Husky pre-commit hooks for linting.
45. [ ] Remove unused configuration stubs (e.g., staticman settings) if the associated service will not be used.
46. [ ] If using Disqus, set shortname per environment and enable via _config.yml; otherwise ensure comments: true defaults are turned off to avoid broken embeds.
47. [ ] Verify talkmap tooling (talkmap.py, talkmap.ipynb) is documented; include instructions and outputs under talkmap/.
48. [ ] Add a simple release checklist in docs (build JS, run Jekyll, verify _site, push) prior to merging to main.
49. [ ] Consider adding Jekyll includes for common elements (contact buttons, social icons) to reduce duplication across pages.
50. [ ] Periodically run bundle update (respecting github-pages constraints) and test locally; document steps for resolving Gem conflicts (delete Gemfile.lock, reinstall).
51. [x] Migrate Node package manager to pnpm: declare packageManager in package.json, prefer pnpm commands in docs, remove package-lock.json, and generate/commit pnpm-lock.yaml on next install.
