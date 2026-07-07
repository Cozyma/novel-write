$lines = Get-Content "c:\Users\pn-t-kojima\Documents\novel-write\_workspace\02_meso_notes\chapter_summaries_draft.md" -Encoding UTF8
$inYaml = $false
$currentLines = @()
$chapterNum = 0

foreach ($line in $lines) {
    if ($line -match "## 第(\d+)話") {
        $chapterNum = [int]$matches[1]
    }
    elseif ($line -match "^```yaml") {
        $inYaml = $true
        $currentLines = @()
    }
    elseif ($line -match "^```" -and $inYaml) {
        $inYaml = $false
        if ($chapterNum -gt 0) {
            $filename = "chapter_{0:D2}_summary.yaml" -f $chapterNum
            $filepath = Join-Path "c:\Users\pn-t-kojima\Documents\novel-write\04_meso_plot\arc_01" $filename
            Set-Content -Path $filepath -Value $currentLines -Encoding UTF8
            Write-Host "Created $filename"
        }
    }
    elseif ($inYaml) {
        $currentLines += $line
    }
}
