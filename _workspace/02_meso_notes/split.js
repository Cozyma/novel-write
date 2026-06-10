var fso = new ActiveXObject("Scripting.FileSystemObject");
var ForReading = 1, ForWriting = 2;
var srcPath = "c:\\Users\\pn-t-kojima\\Documents\\novel-write\\_workspace\\02_meso_notes\\chapter_summaries_draft.md";

// Open text file as ADODB.Stream to support UTF-8
var inStream = new ActiveXObject("ADODB.Stream");
inStream.Type = 2; // Text
inStream.Charset = "utf-8";
inStream.Open();
inStream.LoadFromFile(srcPath);
var content = inStream.ReadText();
inStream.Close();

var lines = content.split('\n');
var inYaml = false;
var currentLines = [];
var chapterNum = 0;

for (var i = 0; i < lines.length; i++) {
    var line = lines[i].replace(/\r$/, '');
    var match = line.match(/^## 第(\d+)話/);
    if (match) {
        chapterNum = parseInt(match[1], 10);
    } else if (line.match(/^```yaml/)) {
        inYaml = true;
        currentLines = [];
    } else if (line.match(/^```/) && inYaml) {
        inYaml = false;
        if (chapterNum > 0) {
            var numStr = chapterNum < 10 ? "0" + chapterNum : "" + chapterNum;
            var filename = "chapter_" + numStr + "_summary.yaml";
            var outPath = "c:\\Users\\pn-t-kojima\\Documents\\novel-write\\04_meso_plot\\arc_01\\" + filename;
            
            var outStream = new ActiveXObject("ADODB.Stream");
            outStream.Type = 2;
            outStream.Charset = "utf-8";
            outStream.Open();
            outStream.WriteText(currentLines.join('\n'));
            outStream.SaveToFile(outPath, 2); // adSaveCreateOverWrite
            outStream.Close();
        }
    } else if (inYaml) {
        currentLines.push(line);
    }
}
