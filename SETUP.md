# Development Environment Setup

## Quick Start

### One-Click Installation (Recommended)

Use the platform-appropriate installation script:

```bash
# macOS/Linux (bash)
sh scripts/install.sh

# macOS/Linux (zsh) 
zsh scripts/install.zsh

# Any platform with PowerShell
pwsh scripts/install.ps1
```

### Python Initialization

Alternatively, run the initialization script directly:

```bash
python init.py
```

This will:
- Create a Python virtual environment
- Install all dependencies via Poetry
- Set up environment configuration
- Create project directories
- Install git pre-commit hooks
- Configure development tools

## Manual Setup

If you prefer manual setup or need to customize the process:

### 1. Create Virtual Environment

```bash
# macOS/Linux
python -m venv .venv
source .venv/bin/activate

# Windows
python -m venv .venv
.\.venv\Scripts\activate
```

### 2. Install Dependencies

**With Poetry (Recommended):**
```bash
poetry install
```

**With pip:**
```bash
pip install -r requirements.txt
```

### 3. Configure Environment

Copy the example environment file and update with your API keys:

```bash
cp .env.example .env
```

Edit `.env` and add your:
- `CLAUDE_API_KEY` - Get from [Anthropic Console](https://console.anthropic.com/)
- `GEMINI_API_KEY` - Get from [Google AI Studio](https://makersuite.google.com/app/apikey)

### 4. Install Pre-commit Hooks

```bash
pre-commit install
```

## Development Workflow

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=term-missing

# Run specific test markers
pytest -m unit
pytest -m integration
pytest -m "not slow"
```

### Code Quality

```bash
# Format code
black .

# Type checking
mypy src/

# Run all pre-commit hooks
pre-commit run --all-files
```

### Using AI Assistants

This boilerplate is configured for optimal use with:
- **Claude**: Anthropic's AI assistant
- **Gemini**: Google's AI model  
- **GitHub Copilot**: With custom instructions in `.github/copilot-instructions.md`

The configuration files in `configs/` define:
- AI tool settings and API endpoints
- Development stack and dependencies
- IDE integrations
- Cross-platform compatibility settings

## Project Structure

```
ai-codeassist-boilerplate/
├── .claude/                    # Claude-specific configuration and commands
├── .github/                    # GitHub workflows and Copilot instructions
│   ├── copilot-instructions.md # Main GitHub Copilot instructions
│   └── instructions/           # Specific instruction files
├── configs/                    # YAML configuration files
│   ├── ai-tools.yaml          # AI service configurations
│   ├── code-stack.yaml        # Development stack settings
│   └── *.yaml                 # Other configuration files
├── scripts/                    # Cross-platform utility scripts
│   ├── Run-Python.psm1        # PowerShell Python runner
│   └── Get-ProviderModels.psm1 # AI model fetching utility
├── src/                        # Source code packages
├── tests/                      # Test files (pytest)
├── .env                        # Environment variables (create from .env.example)
├── .env.example               # Environment variable template
├── init.py                    # Project initialization script
├── pyproject.toml             # Poetry configuration and dependencies
├── pytest.ini                # Pytest configuration
├── requirements.txt           # Python dependencies (generated from Poetry)
└── README.md                  # Main project documentation
```

## PowerShell Module Usage

This project includes PowerShell modules for cross-platform automation:

```powershell
# Import and use Python runner
Import-Module ./scripts/Run-Python.psm1
Run-Python "your_script.py"

# Fetch AI provider models
Import-Module ./scripts/Get-ProviderModels.psm1  
Get-ProviderModels -Provider "claude" -OutputPath "./configs/claude_models.json"
```

## Troubleshooting

### Virtual Environment Issues

If you encounter issues with the virtual environment:

```bash
# Remove existing environment
rm -rf .venv

# Recreate with Python
python -m venv .venv

# Or recreate with Poetry
poetry env remove --all
poetry install
```

### Permission Errors

On macOS/Linux, ensure scripts are executable:

```bash
chmod +x init.py
chmod +x scripts/install.sh
```

### API Key Issues

1. Ensure your `.env` file contains valid API keys
2. Never commit `.env` to version control (it's in `.gitignore`)
3. Use `.env.example` as a template for required variables

### PowerShell Execution Policy (Windows)

If PowerShell scripts fail to run on Windows:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Poetry Installation Issues

If Poetry is not available:

```bash
# Install Poetry
curl -sSL https://install.python-poetry.org | python3 -

# Or use pip
pip install poetry
```

## Next Steps

1. **Review configurations**: Check files in `configs/` directory
2. **Read AI instructions**: Review `.github/copilot-instructions.md` and related files
3. **Understand the structure**: Familiarize yourself with the project layout
4. **Start developing**: Add your code to `src/` and tests to `tests/`
5. **Use AI tools**: Leverage the configured AI assistants for development

## Additional Resources

- [Main README](README.md) - Project overview and quick start
- [Claude Guidelines](CLAUDE.md) - Claude-specific development guidance  
- [AI Coding Standards](AGENTS.md) - Universal AI coding agent guidelines
- [GitHub Copilot Instructions](.github/copilot-instructions.md) - Copilot configuration

For questions or issues, refer to the documentation in the respective configuration files or the project's issue tracker.