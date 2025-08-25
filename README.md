A Github Pages template for academic websites. This was forked (then detached) by [Stuart Geiger](https://github.com/staeiou) from the [Minimal Mistakes Jekyll Theme](https://mmistakes.github.io/minimal-mistakes/), which is © 2016 Michael Rose and released under the MIT License. See LICENSE.md.

I think I've got things running smoothly and fixed some major bugs, but feel free to file issues or make pull requests if you want to improve the generic template / theme.

### Note: if you are using this repo and now get a notification about a security vulnerability, delete the Gemfile.lock file. 

# Instructions

1. Register a GitHub account if you don't have one and confirm your e-mail (required!)
1. Fork [this repository](https://github.com/academicpages/academicpages.github.io) by clicking the "fork" button in the top right. 
1. Go to the repository's settings (rightmost item in the tabs that start with "Code", should be below "Unwatch"). Rename the repository "[your GitHub username].github.io", which will also be your website's URL.
1. Set site-wide configuration and create content & metadata (see below -- also see [this set of diffs](http://archive.is/3TPas) showing what files were changed to set up [an example site](https://getorg-testacct.github.io) for a user with the username "getorg-testacct")
1. Upload any files (like PDFs, .zip files, etc.) to the files/ directory. They will appear at https://[your GitHub username].github.io/files/example.pdf.  
1. Check status by going to the repository settings, in the "GitHub pages" section
1. (Optional) Use the Jupyter notebooks or python scripts in the `markdown_generator` folder to generate markdown files for publications and talks from a TSV file.

See more info at https://academicpages.github.io/

## To run locally (not on GitHub Pages, to serve on your own computer)

1. Clone the repository and made updates as detailed above
1. Make sure you have ruby-dev, bundler, and nodejs installed: `sudo apt install ruby-dev ruby-bundler nodejs`
1. Run `bundle clean` to clean up the directory (no need to run `--force`)
1. Run `bundle install` to install ruby dependencies. If you get errors, delete Gemfile.lock and try again.
1. Run `bundle exec jekyll serve --livereload --config _config.yml,_config.dev.yml` to generate the HTML and serve it from `localhost:4000`; the local server will automatically rebuild and refresh pages on change.

# Changelog -- bugfixes and enhancements

There is one logistical issue with a ready-to-fork template theme like academic pages that makes it a little tricky to get bug fixes and updates to the core theme. If you fork this repository, customize it, then pull again, you'll probably get merge conflicts. If you want to save your various .yml configuration files and markdown files, you can delete the repository and fork it again. Or you can manually patch. 

To support this, all changes to the underlying code appear as a closed issue with the tag 'code change' -- get the list [here](https://github.com/academicpages/academicpages.github.io/issues?q=is%3Aclosed%20is%3Aissue%20label%3A%22code%20change%22%20). Each issue thread includes a comment linking to the single commit or a diff across multiple commits, so those with forked repositories can easily identify what they need to patch.

---

## Windows-friendly local workflow (recommended)

Use PowerShell and the pinned GitHub Pages environment via Bundler so local builds mirror production. Node.js 14 or newer is required for the JS pipeline.

Prerequisites (Windows):
- Ruby (RubyInstaller for Windows with MSYS2/DevKit recommended)
- Bundler (`gem install bundler` if missing)
- Node.js >= 14 (`node -v` to verify) and pnpm (`npm i -g pnpm` or use Corepack: `corepack enable && corepack prepare pnpm@9 --activate`)

One-time setup:
- `bundle clean`
- `bundle install`
- `pnpm install`  (preferred; npm install also works)

Develop with live reload:
- `bundle exec jekyll serve --livereload --config _config.yml,_config.dev.yml`
  - This sets `url: http://localhost:4000`, disables analytics and comments in development, and expands Sass for easier debugging.

Build without serving:
- `bundle exec jekyll build --config _config.yml,_config.dev.yml`

JavaScript pipeline:
- Build JS once: `pnpm run build:js` (or `npm run build:js`)
- Watch JS files and rebuild on change: `pnpm run watch:js` (or `npm run watch:js`)
- Convenience build (JS + Jekyll build): `pnpm run build` (or `npm run build`)

Important: GitHub Pages does not run Node tasks. If you change any JS under assets\js that impacts the bundle, you must commit the generated `assets\js\main.min.js` so production sees the update.

Troubleshooting:
- Always prefix Jekyll commands with `bundle exec` to use the pinned versions.
- If you see `cannot load such file -- webrick`, ensure `webrick` is installed (it is already in the Gemfile) and re-run with `bundle exec`.
- If file watching doesn’t pick up changes on Windows, ensure `wdm` is installed (Bundler installs it from the Gemfile) and that you’re running PowerShell with appropriate permissions.
- If `bundle install` reports version conflicts, try deleting `Gemfile.lock`, then run `bundle install` again.

### Local dev WEBrick NoMethodError workaround (Jekyll 3.9.x)

When serving locally you may see repeated errors like:

```
NoMethodError: undefined method `key?' for nil:NilClass
  .../jekyll-3.9.x/lib/jekyll/commands/serve/servlet.rb:...:in `conditionally_inject_charset'
```

This is a known incompatibility in Jekyll 3.9.x with newer WEBrick versions during live-serve. This repository ships a small dev-only patch at `_plugins/charset_injection_patch.rb` that defensively guards that method and preserves original return values. GitHub Pages ignores plugins, so this does not affect production builds.

- Keep this patch only for local development. After upgrading to Jekyll 4 (or when upstream fixes this in your environment), you can remove `_plugins/charset_injection_patch.rb`.
- Alternative: if you prefer not to load the patch, you can use `bundle exec jekyll serve --livereload --config _config.yml,_config.dev.yml` instead of `liveserve`.

## License and Notices

- Repository license: MIT (see `LICENSE`).
- Theme attribution: This site is based on Minimal Mistakes and academicpages, both released under the MIT License. Attribution to Michael Rose (Minimal Mistakes) and academicpages is retained in this repository.
- JavaScript/CSS third-party assets:
  - Leaflet and related assets under `talkmap/leaflet_dist` are included as distributed and are licensed under their respective licenses (Leaflet is BSD-2-Clause). See headers/NOTICE files in that directory for details.
- Site content (Markdown, images, PDFs) is © the site owner (Aadarsha Gopala Reddy) or the respective rights holders. Do not reuse without permission unless otherwise stated.
- Any additional third-party fonts/embeds used by pages/posts retain their own licenses/terms.

If you add new third-party assets, include appropriate attribution and license files in the repository (e.g., alongside the asset or in a NOTICE file).
