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
