# Build Clarify skill packages for Claude Desktop.
# Produces one zip per skill under build/:
#   - clarify.zip            (router: root SKILL.md)
#   - clarify-<task>.zip     (one per folder in skills/)
# Each zip is self-contained: it bundles the shared .clarify/ reference pack.
#
# Usage:  pwsh ./build-skill.ps1 [-SkipLint]
param([switch]$SkipLint)

$ErrorActionPreference = 'Stop'
$root  = $PSScriptRoot
$pack  = Join-Path $root '.clarify'
$build = Join-Path $root 'build'

if (-not $SkipLint) {
    & (Join-Path $root 'lint-skill.ps1') -Quiet
    if ($LASTEXITCODE -ne 0) {
        throw "Invariant lint failed — fix the violations above, or rerun with -SkipLint."
    }
}

if (-not (Test-Path $pack)) { throw "Missing .clarify/ pack at $pack" }
if (Test-Path $build) { Remove-Item -Recurse -Force $build }
New-Item -ItemType Directory -Force -Path $build | Out-Null

function New-SkillZip([string]$name, [string]$skillMd) {
    $stage = Join-Path $build $name
    New-Item -ItemType Directory -Force -Path $stage | Out-Null
    Copy-Item $skillMd -Destination (Join-Path $stage 'SKILL.md')
    Copy-Item $pack    -Destination $stage -Recurse
    $zip = Join-Path $build "$name.zip"
    Compress-Archive -Path $stage -DestinationPath $zip -Force
    $kb = [math]::Round((Get-Item $zip).Length / 1KB, 1)
    "  {0,-22} {1,6} KB" -f "$name.zip", $kb
}

Write-Host "Building Clarify skill packages..."
# Router skill (root SKILL.md, name: clarify)
New-SkillZip 'clarify' (Join-Path $root 'SKILL.md')

# Specialized skills (one folder each under skills/)
Get-ChildItem (Join-Path $root 'skills') -Directory | ForEach-Object {
    New-SkillZip $_.Name (Join-Path $_.FullName 'SKILL.md')
}

Write-Host "Done. Upload each .zip in build/ via Claude Desktop -> Settings -> Capabilities -> Skills."
