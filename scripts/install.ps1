# PowerShell Installer Script for AI Code Assist Boilerplate

Write-Host "🚀 Starting installation..."

# Check if Poetry is installed
if (-not (Get-Command poetry -ErrorAction SilentlyContinue)) {
    Write-Host "📦 Installing Poetry..."
    Invoke-WebRequest -Uri https://install.python-poetry.org -OutFile install-poetry.py
    python install-poetry.py
    Remove-Item install-poetry.py
}

# Install dependencies using Poetry
Write-Host "📥 Installing dependencies with Poetry..."
poetry install

function Install-SuperClaude {
    param(
        [string]$TargetDir = "$env:HOME/.claude",
        [switch]$Update,
        [switch]$DryRun,
        [switch]$Verbose,
        [switch]$Force,
        [string]$LogFile
    )
    Write-Host ""
    Write-Host "--- Installing SuperClaude ---"
    if (-not (Get-Command bash -ErrorAction SilentlyContinue)) {
        Write-Host "❌ bash is required but not found in PATH. Please install bash and try again."
        return
    }
    if (-not (Test-Path "SuperClaude")) {
        git clone https://github.com/NomenAK/SuperClaude.git
    }
    $origDir = Get-Location
    Set-Location SuperClaude
    $cmd = "./install.sh"
    if ($TargetDir -ne "$env:HOME/.claude") { $cmd += " --dir '$TargetDir'" }
    if ($Update) { $cmd += " --update" }
    if ($DryRun) { $cmd += " --dry-run" }
    if ($Verbose) { $cmd += " --verbose" }
    if ($Force) { $cmd += " --force" }
    if ($LogFile) { $cmd += " --log '$LogFile'" }
    Write-Host "Running: $cmd"
    bash -c "$cmd"
    Set-Location $origDir
    Write-Host "--- SuperClaude installation complete ---"
}

# Prompt user for SuperClaude installation
$installSC = Read-Host "Would you like to install SuperClaude? (y/n)"
if ($installSC -eq 'y' -or $installSC -eq 'Y') {
    Install-SuperClaude
}

Write-Host "✅ Installation complete!"
