---
applyTo: ["src/**/*.py", "tests/**/*.py"]
---

# Python Code Instructions

## Code Style Requirements

### Type Hints (MANDATORY)
- All functions and methods MUST have complete type hints
- Use `from typing import` for complex types (List, Dict, Optional, Union, etc.)
- Function return types are required, use `-> None` for functions that don't return values
- Class attributes should have type annotations

Example:
```python
from typing import List, Optional, Dict, Any

def process_data(
    items: List[str], 
    config: Dict[str, Any], 
    max_count: Optional[int] = None
) -> List[Dict[str, str]]:
    """Process a list of items according to configuration."""
    # Implementation here
    return processed_items
```

### Docstrings (MANDATORY)
- Use Google-style docstrings for all public functions and classes
- Include parameter descriptions, return value descriptions, and examples when helpful
- Document exceptions that may be raised

Example:
```python
def validate_config(config_path: str) -> Dict[str, Any]:
    """Validate and load configuration from YAML file.
    
    Args:
        config_path: Path to the YAML configuration file
        
    Returns:
        Parsed and validated configuration dictionary
        
    Raises:
        FileNotFoundError: If the config file doesn't exist
        ValueError: If the config contains invalid data
        
    Example:
        >>> config = validate_config("configs/ai-tools.yaml")
        >>> print(config["claude"]["api_key"])
    """
```

### Error Handling
- Use specific exception types rather than generic `Exception`
- Provide descriptive error messages that help with debugging
- Use context managers for resource management
- Validate inputs early and fail fast

### Testing Patterns
- Test file names should mirror source files: `src/module.py` → `tests/test_module.py`
- Use descriptive test method names that explain what is being tested
- Include both positive and negative test cases
- Use pytest fixtures for common test setup
- Test edge cases and error conditions

Example test structure:
```python
import pytest
from src.module import MyClass

class TestMyClass:
    """Test suite for MyClass functionality."""
    
    @pytest.fixture
    def sample_instance(self) -> MyClass:
        """Create a sample MyClass instance for testing."""
        return MyClass(config={"test": True})
    
    def test_normal_operation(self, sample_instance: MyClass) -> None:
        """Test that normal operation works as expected."""
        result = sample_instance.process("test_data")
        assert result == expected_result
    
    def test_invalid_input_raises_error(self, sample_instance: MyClass) -> None:
        """Test that invalid input raises appropriate error."""
        with pytest.raises(ValueError, match="Invalid input"):
            sample_instance.process(None)
```

## Project-Specific Patterns

### Configuration Loading
- Use the established pattern in existing code for loading YAML configs
- Always validate configuration after loading
- Provide sensible defaults where appropriate
- Use environment variables for sensitive data (API keys, etc.)

### Cross-Platform Compatibility
- Use `pathlib.Path` instead of string manipulation for file paths
- Test file operations on different operating systems when possible
- Be aware of different line endings and path separators

### AI Integration Patterns
- Follow existing patterns for integrating with AI tools
- Use the configuration system for AI service settings
- Handle API errors gracefully with retry logic where appropriate
- Log AI interactions for debugging when needed

## Code Quality Standards

### Performance Considerations
- Use list comprehensions and generator expressions where appropriate
- Avoid unnecessary loops and redundant operations
- Consider memory usage for large data processing
- Use appropriate data structures (sets for membership testing, etc.)

### Security Best Practices
- Never hardcode API keys or sensitive data
- Validate all external inputs
- Use secure methods for file operations
- Be cautious with `eval()` and `exec()` - avoid them when possible

### Maintainability
- Keep functions focused and single-purpose
- Use meaningful variable names
- Avoid deeply nested code structures
- Comment complex algorithms or business logic
- Consider future extensibility in design choices