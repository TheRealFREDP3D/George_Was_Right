# George_Was_Right - CHANGELOG.md

|          |                                        |  
|   ---    |                  ---                   |  
|File      | CHANGELOG.md                           | 
|Author    | Frederick Pellerin <fredp3d@proton.me> | 
|Github    | <https://github.com/TheRealFREDP3D/>   |  
|Twitter/X | <https://x.com/TheRealFredP3D/>        |  
|Modified  | 04-03-2026                             |  



## [v0.6]

- Regenerated `requirements.txt` as clean ASCII; resolved silent `pip install` failure.
- Added minimal `pyproject.toml` with project metadata.
- Removed debug `print` statement from `src/config.py` that fired on every import.
- Fixed `create_editor_task` to use the timestamped `log_editor` path from `src/config.py` instead of a hardcoded static path.
- Consolidated `logging.basicConfig` to a single call in `main.py`; removed duplicate from `src/llm.py`.
- Refactored agent initialization: LLM instance created once in `create_crew()` and injected into all four agents, eliminating redundant `init_llm()` calls.
- Removed unused `Task` import from `src/agents.py`.
- Deleted dead code: `src/utils.py` (never imported) and `src/web/` static frontend (no backend connection).
- Fixed `log_dir` scoping bug in `app.py` (moved to module level).
- Replaced deprecated model fallback list in `app.py` with the configured default from `src/config.py`.
- Fixed "Update Model" in `app.py` to only update `LLM_MODEL_NAME`, not overwrite planning/fallback models.
- Added `SEARCH_COUNTRY` and `SEARCH_N_RESULTS` sidebar controls to Streamlit UI.
- Added missing `SEARCH_TOPIC` key to `.env.example`.
- Fixed broken image references, showcase links, and entry-point instructions in `README.md`.
- Updated `CHANGELOG.md` with v0.5 and v0.6 entries.

---

## [v0.5]

- Added `EditorAgent` as a fourth specialized agent for content quality and thematic cohesion.
- Introduced Streamlit-based GUI (`app.py`) as an interactive entry point alongside `main.py`.
- Scaffolded a static web frontend (`src/web/`) for future UI exploration.
- Added `start.py` TUI launcher for an alternative CLI entry point.

---

## [v0.4]

- Imported variables and constants from `src/config.py` into `main.py`.
- Added environment variable validation and error handling.
- Improved code structure and readability.
- Added new sections and subsections for better organization.

---

## [v0.3]

- Added new features and improvements.
- Fixed bugs and issues.

---

## [v0.2]

- Initial release with basic functionality.

--
