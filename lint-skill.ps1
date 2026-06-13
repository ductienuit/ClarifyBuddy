# Lint Clarify skill invariants. Run before committing; build-skill.ps1 runs it
# automatically (skip with -SkipLint there).
#
#   pwsh ./lint-skill.ps1 [-Quiet]
#
# Exit 0 = all invariants hold; exit 1 = violations (each printed).
param([switch]$Quiet)

$ErrorActionPreference = 'Stop'
$root = $PSScriptRoot
$failures = New-Object System.Collections.Generic.List[string]
function Fail([string]$msg) { $script:failures.Add($msg) }
function Info([string]$msg) { if (-not $Quiet) { Write-Host $msg } }
function MustContain([string]$relPath, [string]$needle, [string]$what) {
    $p = Join-Path $root $relPath
    if (-not (Test-Path $p)) { Fail "$relPath missing (needed for: $what)"; return }
    $text = [System.IO.File]::ReadAllText($p)
    if (-not $text.Contains($needle)) { Fail "$relPath : expected '$needle' ($what)" }
}

# ---------- 1. Actual counts from the filesystem ----------
$cmd = (Get-ChildItem (Join-Path $root '.claude/commands/clarify') -Filter *.md).Count
$wf  = (Get-ChildItem (Join-Path $root '.clarify/workflows') -Filter *.md).Count
$eng = (Get-ChildItem (Join-Path $root '.clarify/engine') -Filter *.md).Count
$tpl = (Get-ChildItem (Join-Path $root '.clarify/templates') -File).Count
$sub = (Get-ChildItem (Join-Path $root 'skills') -Directory).Count
$apYamlPath = Join-Path $root '.clarify/anti-patterns/anti-patterns.yaml'
$apYaml = Get-Content $apYamlPath
$apIds = @($apYaml | Where-Object { $_ -match '^\s{2}- id:\s*(\S+)' } | ForEach-Object { $Matches[1] })
$ap = $apIds.Count
Info "Actual counts: commands=$cmd workflows=$wf engines=$eng templates=$tpl anti-patterns=$ap sub-skills=$sub"

# ---------- 2. Docs state the actual counts ----------
MustContain 'CLAUDE.md'        "The $cmd commands"            'command count'
MustContain 'CLAUDE.md'        "$eng imperative engines"      'engine count'
MustContain 'CLAUDE.md'        "$tpl output shapes"           'template count'
MustContain 'CLAUDE.md'        "exactly **$ap**"              'anti-pattern count'
MustContain 'CLAUDE.md'        "for the $ap"                  'anti-pattern count (source-of-truth line)'
MustContain 'README.md'        "$ap-entry anti-pattern"       'anti-pattern count'
MustContain 'README.md'        "The $cmd commands"            'command count'
MustContain 'README.md'        "# $cmd slash-command adapters" 'repo-layout command count'
MustContain 'README.md'        "# $eng imperative engines"    'repo-layout engine count'
MustContain 'README.md'        "# $tpl output shapes"         'repo-layout template count'
MustContain 'ROADMAP.md'       "$cmd commands:"               'command count'
MustContain 'ROADMAP.md'       "$eng engines, $tpl templates, $wf workflows" 'counts line'
MustContain 'ROADMAP.md'       "$ap-entry anti-pattern"       'anti-pattern count'
MustContain 'CONTRIBUTING.md'  "Exactly **$ap**"              'anti-pattern count'
MustContain 'SKILL.md'         "$ap-entry anti-pattern"       'anti-pattern count'
MustContain 'skills/clarify-audit/SKILL.md' "$ap-entry anti-pattern" 'anti-pattern count'
# yaml header comment + md title
MustContain '.clarify/anti-patterns/anti-patterns.yaml' "Exactly $ap entries" 'yaml header count'
MustContain '.clarify/anti-patterns/anti-patterns.md'   "Catalog ($ap)"       'md title count'

# ---------- 3. yaml <-> md sync ----------
$apMdPath = Join-Path $root '.clarify/anti-patterns/anti-patterns.md'
$apMdText = [System.IO.File]::ReadAllText($apMdPath)
$mdEntryCount = ([regex]::Matches($apMdText, '(?m)^## \d+\. ')).Count
if ($mdEntryCount -ne $ap) { Fail "anti-patterns.md has $mdEntryCount numbered entries; yaml has $ap" }
foreach ($id in $apIds) {
    if (-not $apMdText.Contains('`' + $id + '`')) { Fail "anti-patterns.md missing id ``$id`` (in yaml)" }
}
$mdIds = [regex]::Matches($apMdText, '(?m)^## \d+\. .* — `([a-z-]+)`') | ForEach-Object { $_.Groups[1].Value }
foreach ($id in $mdIds) {
    if ($apIds -notcontains $id) { Fail "anti-patterns.md heading id ``$id`` not in yaml" }
}

# ---------- 4. Dimensions valid + weights sum 100 ----------
$rubric = Get-Content (Join-Path $root '.clarify/evaluators/scoring-rubric.yaml')
$dimIds = @($rubric | Where-Object { $_ -match '^\s{2}- id:\s*(\S+)' } | ForEach-Object { $Matches[1] })
$weights = @($rubric | Where-Object { $_ -match '^\s{4}weight:\s*(\d+)' } | ForEach-Object { [int]$Matches[1] })
$wsum = ($weights | Measure-Object -Sum).Sum
if ($wsum -ne 100) { Fail "scoring-rubric weights sum to $wsum, expected 100" }
foreach ($line in ($apYaml | Where-Object { $_ -match '^\s{4}dimension:\s*(\S+)' })) {
    $null = $line -match '^\s{4}dimension:\s*(\S+)'
    if ($dimIds -notcontains $Matches[1]) { Fail "anti-patterns.yaml dimension '$($Matches[1])' not a rubric dimension id" }
}

# ---------- 5. Referenced files exist ----------
$promptDirs = @('.clarify/engine', '.clarify/workflows', '.claude/commands/clarify', 'skills', '.')
$promptFiles = @()
foreach ($d in @('.clarify/engine', '.clarify/workflows', '.claude/commands/clarify')) {
    $promptFiles += Get-ChildItem (Join-Path $root $d) -Filter *.md
}
$promptFiles += Get-ChildItem (Join-Path $root 'skills') -Recurse -Filter SKILL.md
$promptFiles += Get-Item (Join-Path $root 'SKILL.md')
foreach ($f in $promptFiles) {
    $text = [System.IO.File]::ReadAllText($f.FullName)
    # templates/<file> references
    foreach ($m in [regex]::Matches($text, 'templates/([A-Za-z0-9.-]+\.(?:md|html|json))')) {
        $t = Join-Path $root (".clarify/templates/" + $m.Groups[1].Value)
        if (-not (Test-Path $t)) { Fail "$($f.Name): references missing template '$($m.Groups[1].Value)'" }
    }
    # workflows/<file> references
    foreach ($m in [regex]::Matches($text, 'workflows/([a-z-]+\.md)')) {
        $t = Join-Path $root (".clarify/workflows/" + $m.Groups[1].Value)
        if (-not (Test-Path $t)) { Fail "$($f.Name): references missing workflow '$($m.Groups[1].Value)'" }
    }
}
# engines named in workflow numbered sequences exist
foreach ($f in (Get-ChildItem (Join-Path $root '.clarify/workflows') -Filter *.md)) {
    foreach ($line in (Get-Content $f.FullName)) {
        if ($line -match '^\d+\.\s+`([a-z][a-z-]*)`') {
            $name = $Matches[1]
            if ($name.Contains('/') -or $name.Contains('.')) { continue }
            $isEngine = Test-Path (Join-Path $root ".clarify/engine/$name.md")
            $isWorkflow = Test-Path (Join-Path $root ".clarify/workflows/$name.md")  # e.g. from-spec step 1 runs "audit (via audit workflow logic)"
            if (-not ($isEngine -or $isWorkflow)) {
                Fail "$($f.Name): engine sequence names ``$name`` but no engine or workflow file with that name exists"
            }
        }
    }
}

# ---------- 6. Eval expected AP ids exist ----------
foreach ($f in (Get-ChildItem (Join-Path $root '.clarify/eval') -Filter *.expected.md)) {
    foreach ($line in (Get-Content $f.FullName)) {
        if ($line -match '^\|\s*([a-z]+(?:-[a-z]+)+)\s*\|') {
            $id = $Matches[1]
            if ($apIds -notcontains $id) { Fail "$($f.Name): expected anti-pattern ``$id`` not in yaml" }
        }
    }
}

# ---------- 7. Detect keys documented in scoring doc exist in yaml ----------
$scoreDoc = [System.IO.File]::ReadAllText((Join-Path $root '.clarify/evaluators/requirement-quality-score.md'))
$yamlText = [System.IO.File]::ReadAllText($apYamlPath)
foreach ($m in [regex]::Matches($scoreDoc, '`([a-z]+(?:_[a-z]+)+)`')) {
    $key = $m.Groups[1].Value
    if (-not $yamlText.Contains($key + ':')) { Fail "requirement-quality-score.md cites detect key '$key' not present in anti-patterns.yaml" }
}

# ---------- Report ----------
if ($failures.Count -gt 0) {
    Write-Host "LINT FAILED — $($failures.Count) violation(s):" -ForegroundColor Red
    $failures | ForEach-Object { Write-Host "  - $_" -ForegroundColor Red }
    exit 1
}
Info "LINT OK — all invariants hold."
exit 0
