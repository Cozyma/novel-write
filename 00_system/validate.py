# -*- coding: utf-8 -*-
"""validate.py — L4ワークフロー④自動バリデーションの検査器（ARCHITECTURE [Hook: L4執筆時] ④）

機械検査可能な項目のみを検査する：
  scene_input      : 必須キー / open_questions 全resolved（生成ゲート） / 【負荷】上限80%（variable_rules.md）
                     / sense・empathy 語彙（Low|Mid|High） / event_timeline の id-event 対 / テンプレ placeholder 残り
  chapter_summary  : 必須キー / catharsis_core 実在（placeholder不可） / peak_variable 語彙（マクロ4変数）
                     / ミニ三幕サブキー / validation_hook の false フラグ

検査しないもの（設計上の対象外）：
  「文章として面白いか」＝人間判定（⑤）がループ終了条件（検証可能性バイアス）。
  design_notes の消化・係り受けの自然さ＝レンダー層セルフパス（SELF_REVIEW §3c）と人間判定の領分。
  deprecated_terms の残骸＝コミット前フック（00_system/git_hooks/pre-commit）の領分。

依存ゼロ（PyYAML 不使用・行パース）。本プロジェクトのYAMLは整形が一定という前提の専用検査器であり、
汎用YAMLバリデータではない。

usage:
  python 00_system/validate.py                # 全 scene_input + 全 chapter_summary（template除外）
  python 00_system/validate.py <file> ...     # 指定ファイルのみ
exit code: 0=エラーなし / 1=エラーあり（WARNのみなら0）
"""
import glob
import io
import os
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

LOAD_MAX = 80  # 【負荷】上限値80%（00_system/variable_rules.md）
LEVELS = {"Low", "Mid", "High"}
PEAK_VARIABLES = {"探求", "報酬", "驚き", "危機"}  # マクロ駆動系4変数（variable_rules.md）

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def top_block(text, key):
    """トップレベルキーのブロック（次のトップレベルキーまで）を返す。無ければ None。"""
    m = re.search(rf"^{key}\s*:(.*)$", text, re.M)
    if not m:
        return None
    start = m.end()
    nxt = re.search(r"^[A-Za-z_]\w*\s*:", text[start:], re.M)
    return text[start:start + nxt.start()] if nxt else text[start:]


def has_top_key(text, key):
    return re.search(rf"^{key}\s*:", text, re.M) is not None


def value_of(block, key):
    """ブロック内の `key: "..."` の値を返す（無ければ None）。コメント行は無視。"""
    for line in block.splitlines():
        if line.lstrip().startswith("#"):
            continue
        m = re.match(rf'\s*(?:-\s+)?{key}\s*:\s*(.*)$', line)
        if m:
            v = m.group(1).strip()
            q = re.match(r'"([^"]*)"', v)  # 引用値はインラインコメントより前で閉じる
            if q:
                return q.group(1).strip()
            return v.split("#")[0].strip()
    return None


def is_placeholder(v):
    return v is None or v == "" or v.startswith("[") or v == "TBD"


def check_scene(path, text):
    errors, warns = [], []
    for key in ("scene_id", "place_time", "pov_character", "event_timeline",
                "scene_facts", "open_questions", "generation_blocks", "causality_next"):
        if not has_top_key(text, key):
            errors.append(f"必須キー欠落: {key}")

    for key in ("place_time", "pov_character", "causality_next"):
        if has_top_key(text, key) and is_placeholder(value_of(text, key)):
            errors.append(f"{key} が未記入（TBD/placeholder）")

    tl = top_block(text, "event_timeline")
    if tl is not None:
        ids = re.findall(r"-\s+id:", tl)
        events = [ln for ln in tl.splitlines()
                  if re.match(r"\s+event\s*:", ln) and not ln.lstrip().startswith("#")]
        if not ids:
            errors.append("event_timeline が空")
        elif len(ids) != len(events):
            errors.append(f"event_timeline: id {len(ids)}件 に対し event {len(events)}件（対の欠落）")

    sf = top_block(text, "scene_facts")
    if sf is not None:
        for key in ("goal", "opponent", "conflict", "pinch"):
            if is_placeholder(value_of(sf, key)):
                errors.append(f"scene_facts.{key} が未記入")

    oq = top_block(text, "open_questions")
    if oq is not None:
        items = re.split(r"(?=^\s*-\s+question\s*:)", oq, flags=re.M)
        n_unresolved = 0
        for item in items:
            if not re.match(r"^\s*-\s+question\s*:", item):
                continue
            q = value_of(item, "question")
            r = value_of(item, "resolution")
            if is_placeholder(r):
                n_unresolved += 1
                errors.append(f"open_questions 未resolved: {q}")
        if n_unresolved:
            errors.append(f"生成ゲート未通過（未resolved {n_unresolved}件。全resolvedまで初版生成に入らない）")

    gb = top_block(text, "generation_blocks")
    if gb is not None:
        blocks = re.findall(r"-\s+block\s*:", gb)
        facts = [ln for ln in gb.splitlines()
                 if re.match(r"\s+fact\s*:", ln) and not ln.lstrip().startswith("#")]
        if not blocks:
            errors.append("generation_blocks が空")
        elif len(blocks) != len(facts):
            errors.append(f"generation_blocks: block {len(blocks)}件 に対し fact {len(facts)}件")
        for m in re.finditer(r'load\s*:\s*"?(\d+)\s*%?"?', gb):
            if int(m.group(1)) > LOAD_MAX:
                errors.append(f"【負荷】上限超過: load {m.group(1)}% > {LOAD_MAX}%（variable_rules.md）")
        for m in re.finditer(r'(sense|empathy)\s*:\s*"?(\w+)"?', gb):
            if m.group(2) not in LEVELS:
                errors.append(f"{m.group(1)} の語彙不正: {m.group(2)}（Low|Mid|High）")

    return errors, warns


def check_chapter(path, text):
    errors, warns = [], []
    for key in ("chapter_id", "arc_linkage", "chapter_stimulus", "catharsis_core",
                "chapter_acts", "design_notes", "scenes", "validation_hook"):
        if not has_top_key(text, key):
            errors.append(f"必須キー欠落: {key}")

    if has_top_key(text, "catharsis_core") and is_placeholder(value_of(text, "catharsis_core")):
        errors.append("catharsis_core が未記入＝章は未設計（約束手形は不可）")

    stim = top_block(text, "chapter_stimulus")
    if stim is not None:
        pv = value_of(stim, "peak_variable")
        if pv is None:
            errors.append("chapter_stimulus.peak_variable 欠落")
        elif pv not in PEAK_VARIABLES:
            errors.append(f"peak_variable の語彙不正: {pv}（マクロ4変数: {'/'.join(sorted(PEAK_VARIABLES))}）")

    acts = top_block(text, "chapter_acts")
    if acts is not None:
        for key in ("hook", "build_up", "turn", "cliffhanger"):
            v = value_of(acts, key)
            if is_placeholder(v):
                errors.append(f"chapter_acts.{key} が未記入")

    vh = top_block(text, "validation_hook")
    if vh is not None:
        for key in ("is_linked_to_arc", "has_clear_stimulus", "has_catharsis_core"):
            v = value_of(vh, key)
            if v is not None and v.split("#")[0].strip() == "false":
                errors.append(f"validation_hook.{key} = false（品質ゲート未通過）")

    return errors, warns


def classify(path):
    name = os.path.basename(path)
    if name.startswith("template_"):
        return None
    if re.match(r"scene_\d+_input\.yaml$", name):
        return "scene"
    if re.match(r"chapter_\d+_summary\.yaml$", name):
        return "chapter"
    return None


def main(argv):
    if argv:
        paths = argv
    else:
        paths = (sorted(glob.glob(os.path.join(ROOT, "05_micro_scene", "**", "scene_*_input.yaml"), recursive=True))
                 + sorted(glob.glob(os.path.join(ROOT, "04_meso_plot", "**", "chapter_*_summary.yaml"), recursive=True)))

    n_err = n_files = 0
    for path in paths:
        kind = classify(path)
        if kind is None:
            print(f"SKIP {os.path.relpath(path, ROOT)}（対象外: scene_*_input / chapter_*_summary のみ）")
            continue
        n_files += 1
        with open(path, encoding="utf-8") as f:
            text = f.read()
        errors, warns = (check_scene if kind == "scene" else check_chapter)(path, text)
        rel = os.path.relpath(path, ROOT)
        if errors or warns:
            print(f"NG  {rel}")
            for e in errors:
                print(f"    ERROR: {e}")
            for w in warns:
                print(f"    WARN:  {w}")
            n_err += len(errors)
        else:
            print(f"OK  {rel}")
    print(f"--- {n_files}ファイル検査 / ERROR {n_err}件")
    return 1 if n_err else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
