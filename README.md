# AI Code Assist Boilerplate

A comprehensive template for setting up development environments optimized for AI-assisted coding with tools like Claude, Gemini, and GitHub Copilot.

## 🚀 Quick Start

### One-Click Installation

To install all dependencies and tools automatically, use one of the following commands based on your platform:

#### macOS/Linux (bash/sh)
```sh
sh scripts/install.sh
```

#### macOS/Linux (zsh)
```zsh
zsh scripts/install.zsh
```

#### Any platform with PowerShell (macOS, Linux, Windows)
```pwsh
pwsh scripts/install.ps1
```

These scripts will:
- Install PowerShell if missing (on macOS/Linux)
- Install Poetry if missing
- Install all Python dependencies
- Set up pre-commit hooks
- Create virtual environment
- Configure development tools

### Manual Setup
```bash
# Initialize project and dependencies
python init.py

# Activate virtual environment
source .venv/bin/activate  # Unix/macOS
.\.venv\Scripts\activate   # Windows

# Install dependencies and set up development environment
poetry install
pre-commit install
```

## 🛠️ Development Workflow

### Essential Commands
```bash
# Testing
pytest                                    # Run all tests
pytest --cov=src --cov-report=term-missing  # Run with coverage
pytest -m unit                           # Unit tests only

# Code Quality
black .          # Format code
mypy src/        # Type checking
pre-commit run --all-files  # Run all hooks

# Dependency Management
poetry add package_name      # Add new dependency
poetry update               # Update dependencies
```

### PowerShell Modules
```powershell
# Import and use cross-platform Python runner
Import-Module ./scripts/Run-Python.psm1
Run-Python "your_script.py"

# Fetch AI provider models
Import-Module ./scripts/Get-ProviderModels.psm1
Get-ProviderModels -Provider "claude" -OutputPath "./configs/claude_models.json"
```

## 🏗️ Project Architecture

### Directory Structure
```
├── src/                    # Python source code packages
├── tests/                  # Test suite (pytest)
├── scripts/                # Cross-platform installation and utility scripts
├── configs/                # YAML configuration files for tools and AI services
├── .github/                # GitHub workflows and Copilot instructions
├── .claude/                # Claude-specific configuration and commands
└── docs/                   # Additional documentation
```

### Key Technologies
- **Language**: Python (≥3.8.1, <4.0)
- **Package Manager**: Poetry for dependency management
- **Testing**: pytest with coverage reporting
- **Code Quality**: Black formatter, MyPy type checker
- **Cross-Platform**: PowerShell 7.0+ scripts
- **AI Integration**: Claude, Gemini, GitHub Copilot

## 🤖 AI Integration

### Supported AI Tools
- **Claude**: Anthropic's AI assistant for code analysis and generation
- **Gemini**: Google's AI model for development assistance  
- **GitHub Copilot**: AI pair programming with custom instructions

### Configuration
1. Copy `.env.example` to `.env`
2. Add your API keys:
   ```
   CLAUDE_API_KEY=your_claude_key
   GEMINI_API_KEY=your_gemini_key
   ```
3. AI tools are configured via YAML files in `configs/`

## 📋 Development Standards

### Python Code Requirements
- **Type hints required** for all functions and methods
- **Google/NumPy style docstrings** for documentation
- **Black formatting** enforced via pre-commit hooks
- **Testing** with pytest and coverage reporting
- **Import order**: standard library, third-party, then local

### Testing Standards
- Write tests for all new functionality
- Maintain code coverage above configured threshold  
- Use test markers: `@pytest.mark.unit`, `@pytest.mark.integration`, `@pytest.mark.slow`
- Test files should mirror source structure

### Cross-Platform Compatibility
- PowerShell 7.0+ for all scripts
- Use `pathlib.Path` for file operations
- Test on multiple platforms when possible

## 🔧 Configuration

### Environment Variables
Required environment variables (set in `.env`):
```bash
CLAUDE_API_KEY=your_claude_api_key
GEMINI_API_KEY=your_gemini_api_key
```

### Configuration Files
- `configs/ai-tools.yaml` - AI service configurations
- `configs/code-stack.yaml` - Development stack settings
- `pyproject.toml` - Poetry dependencies and project metadata
- `pytest.ini` - Test configuration with coverage settings

## 🚀 Getting Started with Development

1. **Clone and Setup**:
   ```bash
   git clone <repository-url>
   cd ai-codeassist-boilerplate
   sh scripts/install.sh  # or use PowerShell script
   ```

2. **Activate Environment**:
   ```bash
   source .venv/bin/activate
   ```

3. **Start Developing**:
   - Add your code to `src/` directory
   - Write tests in `tests/` directory
   - Use AI tools to assist with coding
   - Run tests frequently: `pytest`
   - Format code: `black .`

4. **Quality Assurance**:
   ```bash
   pytest --cov=src
   mypy src/
   pre-commit run --all-files
   ```

## 📚 Additional Resources

- See [SETUP.md](SETUP.md) for detailed setup instructions
- Check `.github/copilot-instructions.md` for GitHub Copilot configuration
- Review `configs/` directory for AI tool configurations
- Explore `.claude/` directory for Claude-specific commands

## 📄 License

[License details here - see LICENSE file]

---

**Note**: This is a template project designed to be cloned and customized. Remove this note and update the README with your specific project details.
