# GitHub Copilot Instructions for AI Code Assist Boilerplate

## Project Overview

This is an AI Code Assist Boilerplate project - a comprehensive template for setting up development environments optimized for AI-assisted coding with tools like Claude, Gemini, and GitHub Copilot itself. The project serves as a foundation for creating AI-enhanced development workflows.

## Architecture & Technologies

- **Language**: Python (>=3.8.1, <4.0)
- **Package Manager**: Poetry for dependency management
- **Testing**: pytest with coverage reporting
- **Code Quality**: Black formatter, MyPy type checker, pre-commit hooks
- **Cross-Platform Support**: PowerShell 7.0+ scripts for Windows, macOS, and Linux
- **AI Integration**: Configured for multiple AI coding assistants

## Development Standards

### Python Code Style
- **Type hints are required** for all functions and methods
- Use **Google/NumPy style docstrings** for all functions and classes
- Follow **snake_case** for functions and variables, **PascalCase** for classes
- **Black formatting** is enforced via pre-commit hooks
- **Import order**: standard library, third-party, then local imports

### Testing Requirements
- Write tests for all new functionality in the `tests/` directory
- Use pytest with descriptive test names (`test_*` pattern)
- Include test markers: `@pytest.mark.unit`, `@pytest.mark.integration`, `@pytest.mark.slow`
- Maintain code coverage above the configured threshold
- Test files should mirror the structure of `src/` directory

### File Organization
- **Source code**: Place in `src/` directory with proper `__init__.py` files
- **Tests**: Mirror source structure in `tests/` directory
- **Scripts**: Cross-platform PowerShell modules in `scripts/` directory
- **Configuration**: YAML files in `configs/` directory
- **Documentation**: Markdown files in root or `docs/` directory

## Key Commands & Workflows

### Setup & Installation
```bash
# Quick install (recommended)
sh scripts/install.sh     # macOS/Linux
pwsh scripts/install.ps1  # Any platform with PowerShell

# Manual setup
python init.py
source .venv/bin/activate  # Activate virtual environment
```

### Development Commands
```bash
# Testing
pytest                                    # Run all tests
pytest --cov=src --cov-report=term-missing  # Run with coverage
pytest -m unit                           # Unit tests only
pytest tests/test_specific.py            # Single test file

# Code Quality
black .          # Format code
mypy src/        # Type checking
pre-commit run --all-files  # Run all hooks
```

### PowerShell Module Usage
```powershell
Import-Module ./scripts/Run-Python.psm1
Run-Python "your_script.py"
```

## AI Coding Guidelines

### When Suggesting Code Changes
1. **Maintain existing patterns** - Follow the established code style and architecture
2. **Use configured tools** - Leverage Poetry, Black, MyPy for dependency and code management
3. **Write comprehensive tests** - Include both unit and integration tests
4. **Add type hints** - All functions must have proper type annotations
5. **Cross-platform compatibility** - Ensure code works on Windows, macOS, and Linux

### For New Features
1. **Check existing patterns** before implementing new functionality
2. **Create in appropriate directory** - `src/` for source, `tests/` for tests
3. **Update documentation** - Modify relevant markdown files if needed
4. **Add configuration** - Use YAML files in `configs/` for settings
5. **Consider AI integration** - How does this feature work with AI tools?

### For Bug Fixes
1. **Write a failing test first** to reproduce the issue
2. **Make minimal changes** to fix the specific problem
3. **Ensure existing tests pass** after your changes
4. **Update type hints** if function signatures change

## Project-Specific Context

### AI Tools Integration
- The project includes configuration for multiple AI coding assistants
- See `configs/ai-tools.yaml` for supported AI services
- The `.claude/` directory contains Claude-specific configurations
- PowerShell modules in `scripts/` handle cross-platform AI tool interactions

### Cross-Platform Considerations
- Use PowerShell 7.0+ for scripts to ensure cross-platform compatibility
- Test any shell commands on both Unix and Windows environments
- Use Python's `pathlib` for file system operations
- Environment variables are managed through `.env` files

### Configuration Management
- YAML files in `configs/` directory manage different aspects:
  - `ai-tools.yaml` - AI service configurations
  - `superclaude.yaml` - SuperClaude framework settings
  - `ide-tools.yaml` - IDE and editor configurations
- Environment variables are defined in `.env.example`
- Poetry manages Python dependencies in `pyproject.toml`

## Common Patterns

### Adding a New Python Module
1. Create module in `src/` directory with type hints
2. Add corresponding tests in `tests/` directory
3. Import and test the module functionality
4. Run `black .` and `mypy src/` before committing
5. Update documentation if the module is user-facing

### Adding Configuration
1. Create or update YAML file in `configs/` directory
2. Add schema validation if possible
3. Document the configuration options
4. Test configuration loading in tests

### Working with PowerShell Scripts
1. Use PowerShell 7.0+ compatible syntax
2. Include error handling and parameter validation
3. Test on multiple platforms if possible
4. Follow established patterns in existing scripts

## Error Handling & Best Practices

- Use specific exception types with descriptive messages
- Implement proper logging where appropriate
- Validate inputs and provide clear error messages
- Use context managers for resource management
- Follow the principle of least surprise in API design

Remember: This is a template project designed to be cloned and customized. Focus on maintaining flexibility and extensibility while following established patterns.