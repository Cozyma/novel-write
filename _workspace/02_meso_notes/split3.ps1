$text = Get-Content "c:\Users\pn-t-kojima\Documents\novel-write\_workspace\02_meso_notes\chapter_summaries_draft.md" -Raw
$matches = [regex]::Matches($text, '(?s)chapter_id: "(CH_\d+)"(.*?)has_clear_stimulus: true')
foreach ($m in $matches) {
    $id = $m.Groups[1].Value
    $yaml = "chapter_id: `"" + $id + "`"" + $m.Groups[2].Value + "has_clear_stimulus: true"
    $file = "c:\Users\pn-t-kojima\Documents\novel-write\04_meso_plot\arc_01\chapter_" + $id.Substring(3) + "_summary.yaml"
    [IO.File]::WriteAllText($file, $yaml, [System.Text.Encoding]::UTF8)
}
