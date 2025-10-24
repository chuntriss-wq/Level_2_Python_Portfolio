## Repo overview

This is a small learning / utility Python workspace with a few single-file scripts: `attack.py`, `code_debug.py`, `goals.py`, and `Web_Scraper.py` (currently empty). The code is not a packaged application — expect procedural, top-level scripts rather than modules or services.

## What to know up-front for code edits

- Files are single-file scripts meant to be run directly with the Python interpreter (e.g., `python attack.py`). No virtualenv, package manifest, or tests are present.
- Conventions in this workspace:
  - Use top-level procedural code for simple examples (see `goals.py` and `code_debug.py`).
  - Functions are small and educational (e.g., `calculate_damage` in `goals.py`). Keep changes minimal and consistent with the didactic style.
  - Pay attention to indentation and colon usage — several files include comments pointing out common Python mistakes (missing `:` or wrong indentation).

## Patterns & examples to follow

- Data flow: scripts usually compute values in functions and then run a short linear script that calls them and prints results. Example: `calculate_damage` -> update `player_health` -> print.
- I/O: Scripts use simple print output and synchronous HTTP requests (see `code_debug.py` which uses `requests` + `BeautifulSoup`). If you add network code, follow the same synchronous, dependency-light approach.
- Error handling: current project deliberately omits try/except. When adding error handling, be explicit and small-scoped (wrap only the network call in `code_debug.py` rather than changing whole file style).

## Developer workflows (discoverable from this repo)

- Run a script: `python <filename>.py` (Windows PowerShell). Example: `python attack.py`.
- Dependencies: `requests` and `beautifulsoup4` are used in `code_debug.py`. If you add dependency tracking, prefer `requirements.txt` with pinned versions.

## When editing or adding files

- Preserve the repo's educational tone: include short comments that explain intent for learners.
- Keep changes minimal and explicit. Avoid adding heavy frameworks, packaging, or CI without the user's request.
- If adding network requests, include a short comment describing the external URL and why it's safe to call.

## Files to reference when coding

- `attack.py` — linter-like helper that detects missing imports, missing colons and simple indentation errors in provided code snippets. Use it as an example for tiny static-analysis helpers.
- `code_debug.py` — example of synchronous scraping using `requests` + `BeautifulSoup` and printing results.
- `goals.py` — simple pure-Python function + top-level invocation pattern.

## What not to change without asking

- Do not convert the scripts into a package, tests, or CI pipelines unless requested. The repo is intentionally minimal and educational.

## Quick fixes suggestions (safe, low-risk)

- Fill `Web_Scraper.py` with a small, documented scraping example that follows `code_debug.py` patterns (use requests + BeautifulSoup and print one concise result).
- Add a `requirements.txt` if introducing persistent dependencies (list `requests` and `beautifulsoup4`).

## If you need more context

- Ask the user whether the workspace is intended for learning examples, demos, or a larger application. If it's a learning repo, prefer clarity and comments over optimization.

---
Please review this and tell me if you'd like more detail about any file or want the instructions tuned toward packaging, testing, or CI automation.
