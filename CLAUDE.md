# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an AI Code Assist Boilerplate project - a template for setting up development environments optimized for AI-assisted coding with tools like Claude and Gemini.

## Development Commands

### Setup
```bash
# Quick install (recommended)
sh scripts/install.sh     # macOS/Linux
pwsh scripts/install.ps1  # Any platform with PowerShell

# Manual setup
python init.py

# Activate virtual environment
source .venv/bin/activate  # Unix/macOS
.\.venv\Scripts\activate   # Windows
```

### Testing
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=term-missing

# Run specific test types
pytest -m unit              # Unit tests only
pytest -m "not slow"        # Skip slow tests
pytest tests/test_file.py   # Single test file
```

### Code Quality
```bash
# Format code
black .

# Type checking
mypy src/
```

### PowerShell Module
```powershell
# Import the module
Import-Module ./scripts/Run-Python.psm1

# Run Python scripts
Run-Python "your_script.py"

# Test the module
pwsh -File ./tests/test_run_python.ps1
```

## Architecture

### Directory Structure
- `src/` - Python source code packages
- `tests/` - Test suite (pytest)
- `scripts/` - Cross-platform installation and utility scripts
- `configs/` - YAML configuration files for tools and AI services
- `data/` - Data files (git-ignored)
- `.claude/` - Claude-specific configuration
- `SuperClaude/` - SuperClaude framework (if installed)

### Key Technologies
- **Language**: Python (>=3.8.1, <4.0)
- **Package Manager**: Poetry
- **Testing**: Pytest with coverage
- **Code Formatter**: Black
- **Type Checker**: MyPy
- **Cross-Platform Scripts**: PowerShell 7.0+

### Configuration Files
- `pyproject.toml` - Poetry dependencies and project metadata
- `pytest.ini` - Test configuration with coverage settings
- `configs/ai-tools.yaml` - AI tool configurations
- `configs/superclaude.yaml` - SuperClaude settings

## Development Standards

### Python Code Style
- Type hints required for all functions
- Google/NumPy style docstrings
- snake_case for functions/variables
- PascalCase for classes
- Black formatting (automatically applied via pre-commit)

### Testing Requirements
- Write tests for all new functionality
- Maintain code coverage above configured threshold
- Use appropriate test markers: `@pytest.mark.unit`, `@pytest.mark.integration`, `@pytest.mark.slow`

### Environment Variables
Create a `.env` file with:
```
CLAUDE_API_KEY=your_claude_key
GEMINI_API_KEY=your_gemini_key
```

## Common Tasks

### Adding a New Python Module
1. Create module in `src/` directory
2. Add type hints to all functions
3. Write corresponding tests in `tests/`
4. Run `black .` and `mypy src/` before committing

### Updating Dependencies
```bash
# Add a new dependency
poetry add package_name

# Add a dev dependency
poetry add --dev package_name

# Update all dependencies
poetry update

# Regenerate requirements.txt
poetry export -f requirements.txt --output requirements.txt
```

### Running PowerShell Scripts
The project includes PowerShell modules for cross-platform automation:
- `Run-Python.psm1` - Manages Python execution with virtual environment handling
- `Get-ProviderModels.psm1` - Fetches AI provider model information

## AI Assistant Guidelines

When working with this codebase:
1. Always check existing patterns before implementing new features
2. Maintain consistency with the established code style
3. Use the configured tools (Poetry, Black, MyPy) for dependency and code management
4. Follow the testing patterns established in the `tests/` directory
5. Refer to `AGENTS.md` for detailed AI coding standards

## Notes

- The project supports Windows, macOS, and Linux
- PowerShell 7.0+ is required (auto-installed on Unix systems if needed)
- Pre-commit hooks are automatically configured during setup
- The `data/` directory is git-ignored for local data storage
- HTML coverage reports are generated in `htmlcov/` after running tests with coverage