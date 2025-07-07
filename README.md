# ai-codeassist-boilerplate

Creates our boilerplate best practices files and folder structure and configuration rules for working with our various AI tools

## 🚀 Quick Start: One-Click Installation

To install all dependencies and tools automatically, use one of the following commands based on your platform:

### macOS/Linux (bash/sh)

```sh
sh scripts/install.sh
```

### macOS/Linux (zsh)

```zsh
zsh scripts/install.zsh
```

### Any platform with PowerShell (macOS, Linux, Windows)

```pwsh
pwsh scripts/install.ps1
```

These scripts will:

- Install PowerShell if missing (on macOS/Linux)
- Install Poetry if missing
- Install all Python dependencies
- Install SuperClaude (AI tool)

No manual steps required—just run the script and you're ready to go!

## PowerShell Modules

### Run-Python

Reusable PowerShell cmdlet for cross-platform Python script execution. Automatically finds or installs Python (python3, python, or py) and runs the given script or arguments.

**Usage:**

```powershell
Import-Module ./scripts/Run-Python.psm1
Run-Python "your_script.py"
```

**Testing:**

```powershell
pwsh -File ./tests/test_run_python.ps1
```
