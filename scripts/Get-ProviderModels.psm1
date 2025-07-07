function Get-ProviderModels {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [ValidateSet("claude", "gemini")]
        [string]$Provider,

        [string]$OutputPath = "./${Provider}_models.json"
    )

    switch ($Provider) {
        "claude" {
            # Anthropic Claude models endpoint (replace with real endpoint if available)
            $url = "https://api.anthropic.com/v1/models"
            $headers = @{}
            # If API key is needed, add: $headers["x-api-key"] = "YOUR_API_KEY"
        }
        "gemini" {
            # Google Gemini models endpoint (replace with real endpoint if available)
            $url = "https://generativelanguage.googleapis.com/v1beta/models"
            $headers = @{}
            # If API key is needed, add: $headers["Authorization"] = "Bearer YOUR_API_KEY"
        }
        default {
            throw "Provider '$Provider' is not supported."
        }
    }

    try {
        $response = Invoke-RestMethod -Uri $url -Headers $headers -Method Get
        # Normalize and extract model info for output
        switch ($Provider) {
            "claude" {
                $models = $response.models | ForEach-Object {
                    [PSCustomObject]@{
                        name        = $_.id
                        description = $_.description
                    }
                }
            }
            "gemini" {
                $models = $response.models | ForEach-Object {
                    [PSCustomObject]@{
                        name        = $_.name
                        description = $_.description
                    }
                }
            }
        }
        $models | ConvertTo-Json -Depth 3 | Set-Content -Path $OutputPath -Encoding UTF8
        Write-Host "$Provider models written to $OutputPath"
    } catch {
        Write-Error ("Failed to fetch models for {0}: {1}" -f $Provider, $_)
    }
}
Export-ModuleMember -Function Get-ProviderModels

function Install-ElevenLabsSDK {
    [CmdletBinding()]
    param()

    Write-Host "Installing ElevenLabs Python SDK..."
    pip install elevenlabs
    if ($LASTEXITCODE -eq 0) {
        Write-Host "ElevenLabs Python SDK installed successfully."
    } else {
        Write-Error "Failed to install ElevenLabs Python SDK. Please check your Python environment."
    }
}

Export-ModuleMember -Function Install-ElevenLabsSDK

function Configure-ElevenLabs {
    [CmdletBinding()]
    param()

    Write-Host "Configuring ElevenLabs..."
    $apiKey = Read-Host "Enter your ElevenLabs API key"

    $config = @{
        elevenlabs = @{
            api_key       = $apiKey
            default_voice = "Rachel"
        }
    }

    $config | ConvertTo-Yaml | Set-Content -Path "../configs/elevenlabs_config.yaml" -Encoding UTF8
    Write-Host "ElevenLabs configuration saved to ../configs/elevenlabs_config.yaml."
}

Export-ModuleMember -Function Configure-ElevenLabs
