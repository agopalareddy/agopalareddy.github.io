# Talk Map Tooling

This repository includes a small toolchain to generate an interactive Leaflet map showing locations of your talks based on the front matter in `_talks/*.md`.

## What it does
- Scrapes the `location:` field from each Markdown file in `_talks/`.
- Geocodes locations using Nominatim via `geopy`.
- Uses `getorg` to produce a clustered Leaflet map.
- Writes the data and page assets into `talkmap/` so the site can serve the map statically.

Outputs (committed to the repo):
- `talkmap/org-locations.js`
- `talkmap/map.html`
- `talkmap/leaflet_dist/` (Leaflet assets)

## Prerequisites
- Windows with Python 3 installed (recommended: Python 3.8+)
- Optional: a virtual environment
- Python packages: `geopy`, `getorg`, `requests`, `pyyaml`, `jinja2`

Install deps (PowerShell):

```powershell
# from the repo root
py -3 -m venv .venv    # optional but recommended
.\.venv\Scripts\Activate.ps1
pip install geopy getorg requests pyyaml jinja2
```

## Generate or update the map
1. Ensure your talks are in `_talks/` with front matter including a `location:` string.
2. Run the generator from inside `_talks/` so relative paths line up (as expected by the script):

```powershell
Set-Location _talks
python ..\talkmap.py
Set-Location ..
```

This will (re)create the following:
- `talkmap\org-locations.js` with geocoded coordinates
- `talkmap\map.html` to view the map standalone
- `talkmap\leaflet_dist` assets (if missing)

3. Commit the updated files so they are served by GitHub Pages:

```powershell
git add talkmap\org-locations.js talkmap\map.html talkmap\leaflet_dist
```

## Viewing locally
You can open `talkmap\map.html` directly in a browser, or serve the Jekyll site and link to it:

```powershell
bundle exec jekyll serve --livereload --config _config.yml,_config.dev.yml
```

## Notes and troubleshooting
- Geocoding is rate-limited. If you have many talks, run the script sparingly and avoid rapid retries.
- If a location isn’t found, try making it more specific (e.g., "City, State, Country").
- The map assets are static; no runtime API keys are required.
- Licensing: Leaflet and related assets are under their respective licenses included in `talkmap/leaflet_dist`. See the main repository `LICENSE` for the site content license, and Minimal Mistakes/academicpages MIT license.

## Updating dependencies
These Python tools are not part of the GitHub Pages build. If you change this tooling or add notebooks (e.g., `talkmap.ipynb`), commit only the outputs in `talkmap/` so the site remains fully static in production.
