# Release Checklist

This checklist helps ensure the site builds cleanly and production artifacts are committed before merging to main.

1. Pull latest changes and install deps.  
   - bundle install  
   - pnpm install
2. Lint and build JavaScript.  
   - pnpm run lint  
   - pnpm run build:js  
   - Commit updated assets\js\main.min.js if changed.
3. Lint Sass (optional).  
   - pnpm run lint:css
4. Build Jekyll locally.  
   - bundle exec jekyll build --config _config.yml,_config.dev.yml
5. Run smoke test script (PowerShell):  
   - .\scripts\smoke-test.ps1
6. Manual sanity check (open _site):  
   - Check index, posts, projects, publications, talks.
7. Commit and push.
8. If PR, ensure CI passes.
