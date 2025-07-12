# AGENTS.md - AI Coding Agent Guidelines

## Build/Test Commands
- **Test all**: `pytest`
- **Test single file**: `pytest tests/test_filename.py`
- **Test with coverage**: `pytest --cov=src --cov-report=term-missing`
- **Format code**: `black .`
- **Type check**: `mypy src/`
- **Lint**: Use black for formatting (no separate linter configured)

## Code Style Guidelines
- **Python version**: >=3.8.1,<4.0 (Poetry managed)
- **Formatting**: Use Black formatter with default settings
- **Type hints**: Required for all functions and methods
- **Docstrings**: Use triple quotes, follow Google/NumPy style
- **Imports**: Standard library first, third-party, then local imports
- **Naming**: snake_case for functions/variables, PascalCase for classes
- **Error handling**: Use specific exceptions, include descriptive messages
- **Testing**: Use pytest with descriptive test names (test_*), include docstrings
- **Markers**: Use @pytest.mark.unit, @pytest.mark.integration, @pytest.mark.slow
- **File structure**: src/ for source, tests/ for tests, maintain __init__.py files

## Project Structure
- Virtual environment: `.venv/` (created by init.py)
- Source code: `src/` directory
- Tests: `tests/` directory with pytest configuration
- Cross-platform compatibility required (Windows/Unix)