# Elixir Case Study Website

A polished, responsive, interactive static website showcasing an agile transformation case study for Elixir Technology.

## What is included

- `index.html`: full case study content and navigation.
- `styles.css`: styling, animations, dark mode, responsive design.
- `script.js`: dark mode, scroll progress, back-to-top, animated counters.
- `generate_charts.py`: generates 5 professional charts in `images/`.
- `images/`: generated chart PNGs.

## Quick start (Windows)

1. Open PowerShell in project directory:
   `cd "c:\Users\umer_\Documents\GitHub\Elixir"`
2. Create and activate venv (if not done):
   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```
3. Install dependencies:
   ```powershell
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   ```
4. Generate charts:
   ```powershell
   .venv\Scripts\python.exe generate_charts.py
   ```
5. Open website:
   - Double-click `index.html`, or open in browser via Live Server.

## Project structure

- `/images`: output charts (PNG at 300 DPI). 5 charts currently:
  1. 01_elixir_evolution_timeline.png
  2. 02_resilience_agility_framework.png
  3. 03_market_diversification.png
  4. 04_swot_analysis.png
  5. 05_business_focus_transition.png

- Source files:
  - `index.html`
  - `styles.css`
  - `script.js`
  - `generate_charts.py`

## Optional local server

```powershell
python -m http.server 8000
```
Then browse `http://localhost:8000`.

## Cleanup guidance

- Don’t commit `.venv/` (covered by `.gitignore`).
- Keep `images/` updated by re-running `generate_charts.py` when charts change.
- Use git to track source files; regenerate charts as needed.

## Notes

- `script.js` includes dark mode state in `localStorage`.
- CSS has print-specific style section.
- Fully client-side; ready for GitHub Pages deployment.
