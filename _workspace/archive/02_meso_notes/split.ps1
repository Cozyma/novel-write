$content = Get-Content -Path "c:\Users\pn-t-kojima\Documents\novel-write\_workspace\02_meso_notes\chapter_summaries_draft.md" -Raw -Encoding UTF8

$regex = '(?s)## 第(\d+)話.*?```yaml\r?\n(.*?)\r?\n```'
$matches = [regex]::Matches($content, $regex)

foreach ($match in $matches) {
    $num = [int]$match.Groups[1].Value
    $yaml = $match.Groups[2].Value.Trim()
    
    $filename = "chapter_{0:D2}_summary.yaml" -f $num
    $filepath = Join-Path "c:\Users\pn-t-kojima\Documents\novel-write\04_meso_plot\arc_01" $filename
    
    Set-Content -Path $filepath -Value $yaml -Encoding UTF8
    Write-Host "Created $filename"
}
