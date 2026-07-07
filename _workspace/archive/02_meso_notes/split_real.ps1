$ErrorActionPreference = "Stop"
$src = "c:\Users\pn-t-kojima\Documents\novel-write\_workspace\02_meso_notes\chapter_summaries_draft.md"
$text = [System.IO.File]::ReadAllText($src, [System.Text.Encoding]::UTF8)

$matches = [regex]::Matches($text, '(?s)chapter_id: "(CH_\d+)".*?has_clear_stimulus: true')

foreach ($m in $matches) {
    $id = $m.Groups[1].Value
    $yaml = $m.Value
    $numStr = $id.Substring(3)
    $filename = "chapter_" + $numStr + "_summary.yaml"
    $outPath = "c:\Users\pn-t-kojima\Documents\novel-write\04_meso_plot\arc_01\" + $filename
    
    # Write using UTF8 without BOM to be safe, but UTF8 with BOM is fine too.
    $utf8NoBom = New-Object System.Text.UTF8Encoding $false
    [System.IO.File]::WriteAllText($outPath, $yaml, $utf8NoBom)
    Write-Host "Created $filename"
}
