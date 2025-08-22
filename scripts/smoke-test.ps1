param(
  [switch]$VerboseMode
)

$ErrorActionPreference = 'Stop'

Write-Host 'Running JS build with pnpm...' -ForegroundColor Cyan
pnpm run build:js | Out-Host

Write-Host 'Building Jekyll site...' -ForegroundColor Cyan
bundle exec jekyll build --config _config.yml,_config.dev.yml | Out-Host

$indexPath = Join-Path -Path (Resolve-Path .) -ChildPath '_site\index.html'
if (Test-Path $indexPath) {
  Write-Host "Smoke test passed: $indexPath exists." -ForegroundColor Green
  exit 0
} else {
  Write-Host 'Smoke test failed: _site\\index.html not found.' -ForegroundColor Red
  exit 1
}
