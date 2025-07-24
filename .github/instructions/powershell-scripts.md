---
applyTo: ["scripts/**/*.ps1", "scripts/**/*.psm1"]
---

# PowerShell Scripts Instructions

## Overview
This project uses PowerShell 7.0+ for cross-platform script automation. Scripts must work identically on Windows, macOS, and Linux.

## PowerShell Standards

### Compatibility Requirements
- Use PowerShell 7.0+ compatible syntax only
- Test scripts on multiple platforms when possible
- Avoid Windows-specific cmdlets unless absolutely necessary
- Use cross-platform file path handling

### Module Structure
Follow the established pattern for PowerShell modules:

```powershell
# Module header with description
<#
.SYNOPSIS
    Brief description of the module's purpose
    
.DESCRIPTION
    Detailed description of what the module does
    
.EXAMPLE
    Import-Module ./scripts/ModuleName.psm1
    Use-ModuleFunction -Parameter "value"
#>

# Parameter validation
param(
    [Parameter(Mandatory=$true)]
    [string]$RequiredParam,
    
    [Parameter(Mandatory=$false)]
    [string]$OptionalParam = "DefaultValue"
)

# Error handling
$ErrorActionPreference = "Stop"

# Function definitions with proper documentation
function Get-SomethingUseful {
    <#
    .SYNOPSIS
        Brief description of function
        
    .PARAMETER InputValue
        Description of the parameter
        
    .EXAMPLE
        Get-SomethingUseful -InputValue "test"
    #>
    [CmdletBinding()]
    param(
        [Parameter(Mandatory=$true)]
        [string]$InputValue
    )
    
    # Implementation here
}

# Export functions
Export-ModuleMember -Function Get-SomethingUseful
```

### Error Handling
- Set `$ErrorActionPreference = "Stop"` for consistent error behavior
- Use try/catch blocks for operations that might fail
- Provide meaningful error messages
- Clean up resources in finally blocks when needed

Example:
```powershell
try {
    $result = Invoke-SomeOperation -Path $FilePath
    Write-Host "✅ Operation completed successfully"
    return $result
}
catch {
    Write-Error "❌ Failed to complete operation: $($_.Exception.Message)"
    throw
}
```

### Cross-Platform File Handling
- Use `Join-Path` for combining paths
- Use `Test-Path` before file operations
- Handle different path separators automatically
- Use appropriate file encoding (UTF-8)

Example:
```powershell
$ConfigPath = Join-Path $PSScriptRoot "config.yaml"
if (-not (Test-Path $ConfigPath)) {
    throw "Configuration file not found at: $ConfigPath"
}
```

## Project-Specific Patterns

### Python Integration
Follow the pattern established in `Run-Python.psm1`:
- Detect available Python installations (`python3`, `python`, `py`)
- Handle virtual environment activation
- Pass through command line arguments properly
- Provide clear success/failure feedback

### Installation Scripts
For installation scripts like `install.ps1`:
- Check for required dependencies before starting
- Provide progress indicators for long-running operations
- Handle both fresh installs and updates
- Give clear next steps after completion

### Output Formatting
- Use emoji or symbols for visual feedback: ✅ ❌ ⚠️ 🚀 📦 etc.
- Provide colored output when supported
- Include progress indicators for long operations
- Be consistent with messaging style across scripts

Example:
```powershell
Write-Host "🚀 Starting installation process..."
Write-Host "📦 Installing dependencies..." -ForegroundColor Blue
Write-Host "✅ Installation completed successfully!" -ForegroundColor Green
```

## Testing PowerShell Scripts

### Script Testing
- Create corresponding test files in `tests/` directory
- Test both success and failure scenarios
- Mock external dependencies when possible
- Test on multiple platforms if available

Example test structure:
```powershell
# tests/test_module.ps1
Describe "ModuleName Tests" {
    BeforeAll {
        Import-Module "$PSScriptRoot/../scripts/ModuleName.psm1" -Force
    }
    
    Context "Function Tests" {
        It "Should return expected result for valid input" {
            $result = Get-SomethingUseful -InputValue "test"
            $result | Should -Be "expected_value"
        }
        
        It "Should throw error for invalid input" {
            { Get-SomethingUseful -InputValue "" } | Should -Throw
        }
    }
}
```

### Manual Testing
- Test scripts manually on different platforms when possible
- Verify error handling works as expected
- Check that all dependencies are properly detected
- Ensure cleanup happens correctly on script termination

## Performance & Best Practices

### Efficiency
- Use pipeline operations where appropriate
- Avoid unnecessary loops and object creation
- Cache expensive operations when possible
- Use appropriate PowerShell constructs (`Where-Object`, `ForEach-Object`, etc.)

### Security
- Validate all input parameters
- Use `-WhatIf` and `-Confirm` for destructive operations when appropriate
- Avoid `Invoke-Expression` with user input
- Be cautious with file permissions and execution policies

### Maintainability
- Use clear, descriptive function and variable names
- Keep functions focused on single responsibilities
- Document complex logic with comments
- Use consistent formatting throughout scripts

## Integration with AI Tools

### AI-Friendly Code
- Write self-documenting code with clear intent
- Use meaningful variable names that describe their purpose
- Structure scripts in logical, predictable ways
- Include comprehensive help documentation

### Configuration Integration
- Follow established patterns for loading configuration from YAML files
- Respect environment variables for sensitive settings
- Provide sensible defaults for optional configurations
- Handle missing or invalid configuration gracefully