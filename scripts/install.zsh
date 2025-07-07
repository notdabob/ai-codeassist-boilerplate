#!/bin/zsh
# Cross-platform bootstrapper for AI Code Assist Boilerplate (zsh)
# Installs PowerShell if missing, then runs install.ps1

set -e

# Check for pwsh (PowerShell Core)
if ! command -v pwsh >/dev/null 2>&1; then
  echo "PowerShell not found. Installing PowerShell..."
  # macOS
  if [[ "$(uname)" == "Darwin" ]]; then
    if command -v brew >/dev/null 2>&1; then
      brew install --cask powershell
    else
      echo "Homebrew not found. Please install Homebrew first: https://brew.sh/"
      exit 1
    fi
  # Linux
  elif [[ -f /etc/debian_version ]]; then
    sudo apt-get update && sudo apt-get install -y wget apt-transport-https software-properties-common
    wget -q "https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/packages-microsoft-prod.deb"
    sudo dpkg -i packages-microsoft-prod.deb
    sudo apt-get update
    sudo apt-get install -y powershell
  else
    echo "Please install PowerShell manually: https://docs.microsoft.com/powershell/scripting/install/installing-powershell"
    exit 1
  fi
fi

# Run the PowerShell installer
pwsh "$(dirname $0)/install.ps1"
