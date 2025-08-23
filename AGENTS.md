# AI Coding Agent Guidelines

This file provides universal guidelines for AI coding agents working with this boilerplate project.

## Quick Reference

### Essential Commands
```bash
# Setup and Development
python init.py                           # Initialize project
source .venv/bin/activate                # Activate virtual environment
pytest                                   # Run all tests
pytest --cov=src --cov-report=term-missing  # Test with coverage
black .                                  # Format code
mypy src/                               # Type checking
```

### Project Standards
- **Python Version**: >=3.8.1, <4.0 (Poetry managed)
- **Code Style**: Black formatter with default settings (enforced via pre-commit)
- **Type Safety**: Type hints required for all functions and methods
- **Testing**: pytest with coverage reporting and markers
- **Cross-Platform**: PowerShell 7.0+ for scripts, pathlib for file operations

## Code Quality Standards

### Python Code Requirements

**Type Hints (Mandatory)**
```python
from typing import List, Dict, Optional, Any

def process_data(
    items: List[str], 
    config: Dict[str, Any], 
    max_count: Optional[int] = None
) -> List[Dict[str, str]]:
    """Process items according to configuration."""
    # Implementation here
    return processed_items
```

**Docstrings (Required)**
- Use Google/NumPy style docstrings for all public functions and classes
- Include parameter descriptions, return values, and raised exceptions
- Provide usage examples for complex functions

**Error Handling**
- Use specific exception types with descriptive messages
- Validate inputs early and fail fast
- Use context managers for resource management
- Handle cross-platform differences gracefully

### Testing Standards

**Test Structure**
```python
import pytest
from src.module import MyClass

class TestMyClass:
    """Test suite for MyClass functionality."""
    
    @pytest.fixture
    def sample_instance(self) -> MyClass:
        """Create a sample MyClass instance for testing."""
        return MyClass(config={"test": True})
    
    @pytest.mark.unit
    def test_normal_operation(self, sample_instance: MyClass) -> None:
        """Test that normal operation works as expected."""
        result = sample_instance.process("test_data")
        assert result == expected_result
    
    @pytest.mark.integration
    def test_invalid_input_raises_error(self, sample_instance: MyClass) -> None:
        """Test that invalid input raises appropriate error."""
        with pytest.raises(ValueError, match="Invalid input"):
            sample_instance.process(None)
```

**Test Markers**
- `@pytest.mark.unit` - Fast, isolated unit tests
- `@pytest.mark.integration` - Tests involving multiple components
- `@pytest.mark.slow` - Tests that take significant time to run

### File Organization

**Directory Structure**
```
src/                    # Source code with __init__.py files
├── module1/
│   ├── __init__.py
│   └── core.py
tests/                  # Tests mirroring src/ structure
├── test_module1/
│   └── test_core.py
scripts/                # PowerShell modules (.psm1)
configs/                # YAML configuration files
```

**Naming Conventions**
- **Files/Modules**: `snake_case.py`
- **Functions/Variables**: `snake_case`
- **Classes**: `PascalCase`
- **Constants**: `UPPER_SNAKE_CASE`
- **Private**: `_leading_underscore`

## Cross-Platform Development

### PowerShell Scripts
- Use PowerShell 7.0+ compatible syntax only
- Include proper parameter validation and error handling
- Test on multiple platforms when possible
- Use `Join-Path` for file path operations

```powershell
function Do-Something {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory=$true)]
        [string]$InputPath
    )
    
    $ErrorActionPreference = "Stop"
    
    if (-not (Test-Path $InputPath)) {
        throw "Path not found: $InputPath"
    }
    
    # Implementation here
}
```

### Python Cross-Platform Code
- Use `pathlib.Path` instead of string manipulation for file paths
- Handle different line endings appropriately
- Test file operations on different operating systems
- Consider platform-specific behavior differences

## Configuration Management

### YAML Configuration Files
```yaml
# Use consistent formatting
service_config:
  # Comments for complex options
  api_endpoint: "https://api.example.com"
  timeout: 30
  retry_attempts: 3
  
  # Environment variable references
  api_key: "${SERVICE_API_KEY}"
  
  # Nested configuration
  features:
    caching: true
    logging: 
      level: "INFO"
      format: "json"
```

### Environment Variables
- Document all required environment variables in `.env.example`
- Use consistent naming: `PROJECT_SECTION_SETTING`
- Provide sensible defaults for non-sensitive settings
- Never commit actual API keys or secrets

## AI Tool Integration

### GitHub Copilot Compatibility
- Use descriptive function and variable names
- Structure code in logical, predictable patterns
- Include comprehensive context in docstrings
- Maintain consistent coding patterns throughout the project

### Multi-AI Workflows
- Write self-documenting code that any AI can understand
- Use configuration files rather than hardcoded values
- Maintain clear separation of concerns
- Follow established project patterns consistently

## Performance and Security

### Performance Considerations
- Use appropriate data structures (sets for membership testing, etc.)
- Implement caching for expensive operations when beneficial
- Use list comprehensions and generator expressions appropriately
- Consider memory usage for large data processing

### Security Best Practices
- Validate all external inputs
- Use secure methods for file operations
- Never hardcode secrets or API keys
- Handle sensitive data appropriately
- Be cautious with `eval()` and `exec()` - avoid when possible

## Development Workflow

### Before Making Changes
1. **Understand the project structure** - Review existing patterns
2. **Run existing tests** - Ensure current functionality works
3. **Check configuration** - Verify all required environment variables

### Making Changes
1. **Write failing tests first** for new functionality
2. **Implement minimal code** to pass tests
3. **Add comprehensive type hints** and docstrings
4. **Update documentation** if needed
5. **Run quality checks** before committing

### Quality Assurance
```bash
# Run the full quality pipeline
pytest --cov=src --cov-report=term-missing
black .
mypy src/
pre-commit run --all-files
```

## Common Patterns

### Configuration Loading
```python
import yaml
from pathlib import Path
from typing import Dict, Any

def load_config(config_name: str) -> Dict[str, Any]:
    """Load configuration from YAML file."""
    config_path = Path("configs") / f"{config_name}.yaml"
    
    if not config_path.exists():
        raise FileNotFoundError(f"Config not found: {config_path}")
    
    with open(config_path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)
```

### Error Handling Pattern
```python
def robust_operation(data: Any) -> Any:
    """Perform operation with proper error handling."""
    try:
        # Validate inputs
        if not data:
            raise ValueError("Data cannot be empty")
        
        # Perform operation
        result = process(data)
        
        # Validate outputs
        if not result:
            raise RuntimeError("Operation produced no result")
            
        return result
        
    except (ValueError, TypeError) as e:
        # Handle expected errors
        logger.error(f"Invalid input: {e}")
        raise
    except Exception as e:
        # Handle unexpected errors
        logger.error(f"Unexpected error: {e}")
        raise RuntimeError("Operation failed") from e
```

---

**Remember**: This is a boilerplate project designed for AI-assisted development. All patterns should be optimized for AI tool understanding and extension.