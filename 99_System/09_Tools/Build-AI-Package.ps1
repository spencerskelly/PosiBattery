param(
    [Parameter(Mandatory=$true)]
    [string[]]$Packages,

    [switch]$IncludeObsidian,

    [string]$OutputPath = ""
)

$ErrorActionPreference = "Stop"

# This script is stored at <vault>/99_System/09_Tools/Build-AI-Package.ps1.
$VaultRoot = (Resolve-Path (Join-Path $PSScriptRoot "../..")).Path
$VaultName = Split-Path $VaultRoot -Leaf

# Fail before packaging if the production path contract is already broken.
& (Join-Path $PSScriptRoot "Check-Vault-Paths.ps1") -Root $VaultRoot -Quiet

if ([string]::IsNullOrWhiteSpace($OutputPath)) {
    $stamp = Get-Date -Format "yyyyMMdd-HHmmss"
    $OutputPath = Join-Path (Split-Path $VaultRoot -Parent) "${VaultName}_AI_${stamp}.zip"
} elseif (-not [System.IO.Path]::IsPathRooted($OutputPath)) {
    $OutputPath = Join-Path (Get-Location) $OutputPath
}

$Staging = Join-Path ([System.IO.Path]::GetTempPath()) ("MDSE_AI_" + [guid]::NewGuid().ToString("N"))
New-Item -ItemType Directory -Path $Staging | Out-Null

try {
    Copy-Item -Recurse -Force (Join-Path $VaultRoot "99_System") (Join-Path $Staging "99_System")

    foreach ($relative in $Packages) {
        $clean = $relative.Trim().TrimStart([char[]]"\\/").TrimEnd([char[]]"\\/")
        if ([string]::IsNullOrWhiteSpace($clean)) { continue }

        $source = Join-Path $VaultRoot $clean
        if (-not (Test-Path $source)) {
            throw "Package path does not exist: $clean"
        }

        if ((Get-Item $source).PSIsContainer -and -not (Test-Path (Join-Path $source "_PACKAGE.md"))) {
            Write-Warning "'$clean' has no _PACKAGE.md. It may be context rather than a supported replacement boundary."
        }

        $destination = Join-Path $Staging $clean
        New-Item -ItemType Directory -Force -Path (Split-Path $destination -Parent) | Out-Null
        Copy-Item -Recurse -Force $source $destination
    }

    if ($IncludeObsidian) {
        Copy-Item -Recurse -Force (Join-Path $VaultRoot ".obsidian") (Join-Path $Staging ".obsidian")
    }

    # Check the staged package too; this catches a problematic selected context path.
    & (Join-Path $PSScriptRoot "Check-Vault-Paths.ps1") -Root $Staging -Quiet

    $handoff = @"
# AI Work Package Handoff

Vault: $VaultName
Created: $(Get-Date -Format "yyyy-MM-dd HH:mm:ss")

Writable scope must be determined from the user's request and each `_PACKAGE.md` manifest.
`99_System` is context-only by default.

Included content paths:
$($Packages | ForEach-Object { "- ``$_``" } | Out-String)

Read `99_System/02_AI/AI_INSTRUCTIONS.md` before editing.
Return only complete replacement package folder(s) that changed.
Preserve the relative path contract documented in `99_System/01_Admin/Portable Path Policy.md`.
"@
    Set-Content -Path (Join-Path $Staging "AI_HANDOFF.md") -Value $handoff -Encoding UTF8

    if (Test-Path $OutputPath) { Remove-Item -Force $OutputPath }
    $items = Get-ChildItem -Force -LiteralPath $Staging
    $items | Compress-Archive -DestinationPath $OutputPath -CompressionLevel Optimal

    Write-Host "Created AI work package:"
    Write-Host $OutputPath
}
finally {
    if (Test-Path $Staging) { Remove-Item -Recurse -Force $Staging }
}
