# AGENTS.md — Cat & Duck Studio site

Public GitHub Pages site (served from `main`; Actions stay on because Pages needs them): https://wobqqq.github.io/cat-and-duck-studio/ (EN at `/`, RU at `/ru/`).

- **Generated:** `index.html`, `ru/index.html`, `site.webmanifest` and `tool/logo.svg` (the cat-and-duck logo) all come from `python3 tool/build.py .`. Edit only `tool/build.py`: `GAMES` (slug, RU/EN name and line, RuStore link, accent colour), `T` (texts) and the CSS.
- **Game pages and icons** live in the `wobqqq.github.io` repo (`../wobqqq.github.io/<slug>/`); tiles link there and load `…/<slug>/icon_512.png`. Publish a new game's page first.
- **A game added or removed:** update `GAMES` here and in `../wobqqq.github.io/tool/build_home.py` (see the `game-site` skill in the game repos).
- **Publish:** branch → commit → `gh pr create --fill` → `gh pr merge --merge --delete-branch`, then check that `/` and `/ru/` return 200.
- **Commits** as `Sergey Zakharevich <wobqqq@gmail.com>`, with no Co-Authored-By or "Generated with" lines.
- **Language:** code and comments in English; only visible texts are RU/EN.
