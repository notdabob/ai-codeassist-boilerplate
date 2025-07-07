# Development Environment Setup

## Quick Start

Run the initialization script to set up your development environment:

```bash
python init.py
```

This will:
- Create a Python virtual environment
- Install all dependencies
- Set up environment configuration
- Create project directories
- Install git pre-commit hooks
- Configure Claude AI integration

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

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

Copy the example environment file and update with your API keys:

```bash
cp .env.example .env
```

Edit `.env` and add your:
- `CLAUDE_API_KEY`
- `GEMINI_API_KEY`

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
pytest --cov=src

# Run specific test markers
pytest -m unit
pytest -m "not slow"
```

### Code Quality

```bash
# Format code
black .

# Lint code
flake8

# Type checking
mypy src/
```

### Using AI Assistants

This boilerplate is configured for optimal use with:
- Claude CLI (`claude`)
- Gemini CLI (`gemini`)

The configuration files in `/configs` define:
- Supported languages and tools
- IDE integrations
- OS compatibility
- AI tool settings

## Project Structure

```
ai-codeassist-boilerplate/
├── .claude/           # Claude-specific configuration
├── configs/           # YAML configuration files
├── data/             # Data files (ignored by git)
├── docs/             # Documentation
├── external/         # External dependencies
├── scripts/          # Utility scripts
├── src/              # Source code
├── tests/            # Test files
├── .env              # Environment variables (create from .env.example)
├── init.py           # Project initialization script
├── pytest.ini        # Pytest configuration
├── requirements.txt  # Python dependencies
└── SETUP.md         # This file
```

## Troubleshooting

### Virtual Environment Issues

If you encounter issues with the virtual environment:

```bash
# Remove existing environment
rm -rf .venv

# Recreate
python -m venv .venv
```

### Permission Errors

On macOS/Linux, ensure the init script is executable:

```bash
chmod +x init.py
```

### API Key Issues

Ensure your `.env` file contains valid API keys. Never commit this file to version control.

## Next Steps

1. Review the configuration files in `/configs`
2. Customize `.claude/CLAUDE.md` for your project needs
3. Start building your AI-assisted application!

For more information, see the [main README](README.md).