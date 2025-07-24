---
applyTo: ["configs/**/*.yaml", "configs/**/*.yml"]
---

# Configuration Files Instructions

## YAML Configuration Standards

### File Structure
All configuration files should follow consistent YAML formatting:
- Use 2-space indentation (no tabs)
- Include descriptive comments for complex configurations
- Group related settings logically
- Use clear, descriptive key names

Example structure:
```yaml
# Configuration for AI tools integration
ai_services:
  # Claude AI configuration
  claude:
    api_endpoint: "https://api.anthropic.com"
    model_default: "claude-3-sonnet-20240229"
    max_tokens: 4096
    temperature: 0.7
    
  # Gemini AI configuration  
  gemini:
    api_endpoint: "https://generativelanguage.googleapis.com"
    model_default: "gemini-pro"
    safety_settings:
      harassment: "BLOCK_MEDIUM_AND_ABOVE"
      hate_speech: "BLOCK_MEDIUM_AND_ABOVE"

# Development tools configuration
development:
  python:
    version_min: "3.8.1"
    version_max: "4.0.0"
    formatter: "black"
    type_checker: "mypy"
    
  testing:
    framework: "pytest"
    coverage_threshold: 80
    markers:
      - "unit"
      - "integration" 
      - "slow"
```

### Security Considerations
- **Never include API keys or secrets in configuration files**
- Use placeholder values that reference environment variables
- Document required environment variables in comments
- Provide examples with fake/example values

Example:
```yaml
# API configuration - set actual values in .env file
api_keys:
  # Set CLAUDE_API_KEY environment variable
  claude: "${CLAUDE_API_KEY}"
  # Set GEMINI_API_KEY environment variable  
  gemini: "${GEMINI_API_KEY}"
  
# Example configuration (do not use in production)
example_config:
  api_key: "your_api_key_here"  # Replace with actual API key
  endpoint: "https://api.example.com/v1"
```

## Project-Specific Configuration Files

### ai-tools.yaml
Configuration for AI service integrations:
- Define supported AI services and their settings
- Include model names, endpoints, and default parameters
- Document required environment variables
- Provide fallback/default configurations

### superclaude.yaml
SuperClaude framework specific settings:
- Configure SuperClaude installation and usage
- Define custom commands and workflows
- Set integration parameters with other AI tools

### ide-tools.yaml
IDE and editor configuration settings:
- VSCode settings and extensions
- Language server configurations
- Debugging and development tool settings

### code-stack.yaml
Development stack configuration:
- Programming languages and versions
- Frameworks and libraries
- Build tools and dependencies
- Testing and quality assurance tools

## Configuration Validation

### Schema Requirements
When adding new configuration options:
1. **Document the purpose** of each configuration key
2. **Specify data types** (string, integer, boolean, array, object)
3. **Define required vs optional** fields
4. **Provide default values** where appropriate
5. **Include validation rules** (min/max values, allowed values, patterns)

Example with documentation:
```yaml
# Database configuration
database:
  # Connection settings (required)
  host: "localhost"        # string: Database hostname or IP
  port: 5432              # integer: Database port (1-65535)
  name: "myapp"           # string: Database name (required)
  
  # Connection pool settings (optional)
  pool:
    min_connections: 1    # integer: Minimum connections (default: 1)
    max_connections: 10   # integer: Maximum connections (default: 10) 
    timeout: 30          # integer: Connection timeout in seconds (default: 30)
    
  # Feature flags (optional)
  features:
    ssl_required: true   # boolean: Require SSL connection (default: true)
    auto_migrate: false  # boolean: Run migrations on startup (default: false)
```

### Environment Variable Integration
- Use consistent naming for environment variables
- Follow the pattern: `PROJECT_SECTION_SETTING` (e.g., `AI_CLAUDE_API_KEY`)
- Document all required environment variables
- Provide sensible defaults for non-sensitive settings

## Configuration Loading Patterns

### Python Integration
When loading YAML configs in Python code:
```python
import yaml
from pathlib import Path
from typing import Dict, Any
import os

def load_config(config_name: str) -> Dict[str, Any]:
    """Load and validate configuration from YAML file.
    
    Args:
        config_name: Name of config file (without .yaml extension)
        
    Returns:
        Parsed configuration dictionary with environment variable substitution
    """
    config_path = Path("configs") / f"{config_name}.yaml"
    
    if not config_path.exists():
        raise FileNotFoundError(f"Configuration file not found: {config_path}")
    
    with open(config_path, 'r', encoding='utf-8') as file:
        config = yaml.safe_load(file)
    
    # Substitute environment variables
    return substitute_env_vars(config)

def substitute_env_vars(config: Any) -> Any:
    """Recursively substitute environment variables in configuration."""
    if isinstance(config, dict):
        return {key: substitute_env_vars(value) for key, value in config.items()}
    elif isinstance(config, list):
        return [substitute_env_vars(item) for item in config]
    elif isinstance(config, str) and config.startswith("${") and config.endswith("}"):
        env_var = config[2:-1]
        return os.getenv(env_var, config)  # Return original if env var not found
    else:
        return config
```

### PowerShell Integration
When loading YAML configs in PowerShell scripts:
```powershell
function Import-YamlConfig {
    param(
        [Parameter(Mandatory=$true)]
        [string]$ConfigName
    )
    
    $ConfigPath = Join-Path "configs" "$ConfigName.yaml"
    
    if (-not (Test-Path $ConfigPath)) {
        throw "Configuration file not found: $ConfigPath"
    }
    
    # Use PowerShell-Yaml module if available, or python fallback
    try {
        $Config = Get-Content $ConfigPath | ConvertFrom-Yaml
    }
    catch {
        # Fallback to Python YAML parsing
        $Config = python -c "import yaml; print(yaml.safe_load(open('$ConfigPath')))"
    }
    
    return $Config
}
```

## Best Practices

### Organization
- Group related configurations in the same file
- Use consistent naming conventions across all config files
- Keep configuration files focused and not overly complex
- Separate environment-specific settings from general configuration

### Documentation
- Include header comments explaining the file's purpose
- Document each major section
- Provide examples for complex configurations
- Keep comments up-to-date with configuration changes

### Version Control
- Always commit configuration files (but never secrets)
- Use `.env.example` to document required environment variables
- Consider using different configuration files for different environments
- Tag configuration changes that require environment updates

### Maintenance
- Regularly review and clean up unused configuration options
- Validate that all documented options are actually used in code
- Update configuration documentation when adding new features
- Test configuration loading in automated tests