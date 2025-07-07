function Run-Python {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory=$true, Position=0)]
        [string]$ScriptOrArgs
    )
    $pythonCmd = $null
    foreach ($cmd in @('python3','python','py')) {
        if (Get-Command $cmd -ErrorAction SilentlyContinue) {
            $pythonCmd = $cmd
            break
        }
    }
    if (-not $pythonCmd) {
        Write-Host "Python not found. Attempting to install..."
        if ($IsMacOS) {
            if (Get-Command brew -ErrorAction SilentlyContinue) {
                brew install python
            } else {
                Write-Host "Homebrew not found. Please install Homebrew first: https://brew.sh/"
                exit 1
            }
        } elseif ($IsLinux) {
            sudo apt-get update && sudo apt-get install -y python3
            $pythonCmd = 'python3'
        } else {
            Write-Host "Please install Python manually: https://www.python.org/downloads/"
            exit 1
        }
        foreach ($cmd in @('python3','python','py')) {
            if (Get-Command $cmd -ErrorAction SilentlyContinue) {
                $pythonCmd = $cmd
                break
            }
        }
        if (-not $pythonCmd) {
            Write-Host "Python installation failed or not found in PATH."
            exit 1
        }
    }
    & $pythonCmd $ScriptOrArgs
}

Export-ModuleMember -Function Run-Python
