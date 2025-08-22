# Backup and Restore Guide

This repository is a Jekyll site that can be fully restored on a new machine using the steps below.

Prerequisites:
- Ruby + Bundler (use RubyInstaller + MSYS2 on Windows)
- Node.js (14+) and pnpm (via Corepack or npm i -g pnpm)

Steps to restore locally (Windows PowerShell):
1) Clone the repo
- git clone https://github.com/agopalareddy/agopalareddy.github.io.git
- cd agopalareddy.github.io

2) Install dependencies
- bundle clean
- bundle install
- pnpm install

3) Optional: Rebuild JS bundle
- pnpm run build:js

4) Serve/build site
- bundle exec jekyll liveserve --config _config.yml,_config.dev.yml
  or
- bundle exec jekyll build --config _config.yml,_config.dev.yml

5) Verify output
- Check _site/index.html exists after a build.

Notes:
- GitHub Pages does not run Node tasks; commit assets\js\main.min.js after any JS source changes.
- If gem conflicts occur, delete Gemfile.lock, run bundle install again.
- If file watching is unreliable on Windows, ensure the wdm gem is installed (Bundler handles it) and run your terminal with sufficient permissions.
