import os
import re

draft_path = r"c:\Users\pn-t-kojima\Documents\novel-write\_workspace\02_meso_notes\chapter_summaries_draft.md"
out_dir = r"c:\Users\pn-t-kojima\Documents\novel-write\04_meso_plot\arc_01"

with open(draft_path, "r", encoding="utf-8") as f:
    content = f.read()

# Find all yaml blocks
pattern = re.compile(r'## 第(\d+)話.*?```yaml\n(.*?)\n```', re.DOTALL)
matches = pattern.findall(content)

for num_str, yaml_content in matches:
    num = int(num_str)
    filename = f"chapter_{num:02d}_summary.yaml"
    filepath = os.path.join(out_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(yaml_content.strip() + "\n")
    print(f"Created {filename}")
