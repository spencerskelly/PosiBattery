param(
    [string]$Root = "",
    [int]$MaxRelativePath = 120,
    [int]$MaxFileName = 80,
    [int]$WarnRelativePath = 100,
    [switch]$Quiet
)

$ErrorActionPreference = "Stop"

if ([string]::IsNullOrWhiteSpace($Root)) {
    # Stored at <vault>/99_System/09_Tools/Check-Vault-Paths.ps1
    $Root = (Resolve-Path (Join-Path $PSScriptRoot "../..")).Path
} else {
    $Root = (Resolve-Path $Root).Path
}

$reserved = @('CON','PRN','AUX','NUL','COM1','COM2','COM3','COM4','COM5','COM6','COM7','COM8','COM9','LPT1','LPT2','LPT3','LPT4','LPT5','LPT6','LPT7','LPT8','LPT9')
$errors = @()
$warnings = @()

Get-ChildItem -LiteralPath $Root -Recurse -Force -File | ForEach-Object {
    $rel = $_.FullName.Substring($Root.Length).TrimStart([char[]]'\\/')
    $relLen = $rel.Length
    $nameLen = $_.Name.Length
    $stem = [System.IO.Path]::GetFileNameWithoutExtension($_.Name).ToUpperInvariant()

    if ($relLen -gt $MaxRelativePath) {
        $errors += "Relative path $relLen > $MaxRelativePath : $rel"
    } elseif ($relLen -gt $WarnRelativePath) {
        $warnings += "Relative path $relLen > $WarnRelativePath : $rel"
    }

    if ($nameLen -gt $MaxFileName) {
        $errors += "Filename $nameLen > $MaxFileName : $rel"
    }

    if ($reserved -contains $stem) {
        $errors += "Windows-reserved filename: $rel"
    }

    if ($_.Name -match '[<>:"/\\|?*]') {
        $errors += "Windows-invalid filename character: $rel"
    }

    if ($_.Name.EndsWith(' ') -or $_.Name.EndsWith('.')) {
        $errors += "Filename ends with a space or period: $rel"
    }
}

if (-not $Quiet) {
    Write-Host "Path portability check: $Root"
    Write-Host "Limits: relative <= $MaxRelativePath, filename <= $MaxFileName; warning > $WarnRelativePath"
    foreach ($w in $warnings) { Write-Warning $w }
    foreach ($e in $errors) { Write-Error $e -ErrorAction Continue }
}

if ($errors.Count -gt 0) {
    throw "Path portability check failed with $($errors.Count) error(s)."
}

if (-not $Quiet) {
    Write-Host "PASS: no path portability errors. Warnings: $($warnings.Count)."
}
