param(
  [switch]$Prod
)

$ErrorActionPreference = "Stop"

# Start transcript for logging
try {
  Start-Transcript -Path "build_log.txt" -Force | Out-Null
} catch {
  Write-Warning "Could not start transcript: $($_.Exception.Message)"
}

try {
  Write-Host "==> Ensuring JS dependencies and building bundle" -ForegroundColor Cyan
  $pnpm = Get-Command pnpm -ErrorAction SilentlyContinue
  if ($pnpm) {
    pnpm install --no-frozen-lockfile
    pnpm run build:js
  } else {
    Write-Warning "pnpm not found; falling back to npm"
    npm install
    npm run build:js
  }

  Write-Host "==> Building Jekyll site" -ForegroundColor Cyan
  $cfg = if ($Prod) { "_config.yml" } else { "_config.yml,_config.dev.yml" }
  bundle exec jekyll build --config $cfg --verbose

  $indexPath = Join-Path -Path "_site" -ChildPath "index.html"
  if (-not (Test-Path $indexPath)) {
    throw "Build succeeded but _site\\index.html was not found"
  }

  Write-Host "SUCCESS: JS and Jekyll build completed. Output at _site" -ForegroundColor Green
  exit 0
}
catch {
  Write-Error $_
  exit 1
}
finally {
  try { Stop-Transcript | Out-Null } catch {}
}
