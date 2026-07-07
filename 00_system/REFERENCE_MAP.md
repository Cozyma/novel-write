# REFERENCE_MAP.md — 作業ケース別の参照領域マップ（トークン節約）

目的: タスク着手時に「何を読み、何を読まないか」を即決するための手がかり。
運用: **[Hook: タスク着手時]**（`ARCHITECTURE.md` 3章）で本マップを参照し、最小参照セットを決めてから読み込む。
更新: 正本の移動・新しい作業ケースの発生時に、決定事項フックとセットで本マップを更新する。

## 1. 概念→正本パス索引（「あれはどこか」の即答表）

| 概念 | 正本 |
|---|---|
| 7変数の定義・スコープ | `00_system/variable_rules.md` |
| 面白さの核の階層検査（catharsis_engine→sub_catharsis→catharsis_core） | `00_system/ARCHITECTURE.md` 2.2 |
| アーク構造のメソッド（カタルシス曲線・不可逆点・embodiment・roadmap・ハリウッド式の最小借用） | `00_system/ARCHITECTURE.md` 2.3 |
| 死語・廃止語彙（残骸の機械検査） | `00_system/deprecated_terms.yaml` |
| 加護の二類型（普遍/固有）・神の履歴・対抗文化・真信者・分配則 | `01_static_database/world/setting_worldview.yaml`（dogmatism配下） |
| 組織（ギルド/斡旋所/第零機関/ヴェルミ）・社会語彙（査定官/無加護/濁り血/清血） | `setting_worldview.yaml`（organizations / vocabulary） |
| 古い血（種族の実体・氷山） | `setting_worldview.yaml` / old_blood |
| 旧神（力の根・不在の神・氷山＝中身は凍結） | `setting_worldview.yaml` / divine_economy.pantheon.old_god |
| 命名規則（ノルド語ベース＋アレンジ・レジスタ分け） | `setting_worldview.yaml` / naming_rules |
| ノルクの手札①〜⑤と誤読対・切り札の概要 | `01_static_database/characters.yaml` / nork combat_style |
| 切り札の制約詳細（生体負荷・感情ノイズ・隠匿・遮断）・条項告発・遺技ロード・破礼具 | `01_static_database/world/setting_magic.yaml` |
| バディ対比（二種類の自前） | `setting_magic.yaml` / combat_contrast.buddy_contrast |
| 報酬番号の台帳（有形1〜5・無形1〜4） | `04_meso_plot/arc_01/arc_summary.yaml` / reward_chain |
| アークのカタルシス曲線・sub_catharsis・roadmap_step・章割当 | `04_meso_plot/arc_01/arc_summary.yaml` / acts（setup→buildup→despair→catharsis。role＝構造役割のみ）・macro_linkage。章→段の束ねは `chapter_sequence.csv` の episode_id 列 |
| 成長ロードマップ（バディ二人制・最重要・暫定） | ノルク=`concept.yaml`/protagonist_growth_roadmap、マーレン=`characters.yaml`/marlen.growth_roadmap、二人制検査=`ARCHITECTURE.md` 2.3 |
| 章の核・ビート（正本。CSV・arc_summaryは派生） | `04_meso_plot/arc_01/chapter_XX_summary.yaml` |
| 長距離伏線（muddy_blood_paradox・第零機関の種） | `02_dynamic_states/resources_states.yaml` |
| 累積カウンタ（金銭・ツケ等の真の合算値のみ。exposure_level・誤読台帳は廃止 2026-07-07＝ARCHITECTURE 2.1） | `02_dynamic_states/character_states.yaml` |
| 第1アーク凍結レイヤー（仲間・第零機関・ヴェルミ・遺技ロード）の運用規律 | `03_macro_concept/concept.yaml` 冒頭コメント（2026-07-05） |
| 没案の退避先 | `_workspace/archive/01_macro_notes/discarded_ideas.md` |
| 部隊ロスター草案（仮置き・未確定） | `_workspace/archive/01_macro_notes/squad_roster_draft.md` |
| **A2再構成の拘束文書（憲章・骨格・戦闘カノン）** | `_workspace/canon/`（最上位＝arc01_rebuild_charter.md。権威マップ＝README §1b） |
| 試作台帳（判定ログ・注意台帳）とレンダー | `_workspace/probes/arc01_probes.md`（親専用）・`_workspace/probes/renders/`（コールドの参照面） |

## 2. 作業ケース→最小参照セット

### ケースA: 世界法則・設定の壁打ち（新設・変更）
- **必読**: `CONTEXT.md`直近 / `TODO.md` / `SELF_REVIEW.md`（世界法則の帰結検証・氷山の規律）/ 対象の設定ファイル（worldview・magic・charactersの該当キャラ）
- **必要時**: `concept.yaml`（主従ルール・catharsis_engineとの矛盾チェック＝還流）
- **読まない**: 章サマリー全件——整合確認はgrepで全列挙し、ヒットした章だけ読む
- **終了時**: 死語が出たら `deprecated_terms.yaml` へ登録。正本→派生の順で一括同期

### ケースB: 章の核・プロットの壁打ち（対象1〜2章）
- **必読**: `template_chapter_summary.yaml` / 対象章＋前後章のsummary / `SELF_REVIEW.md`【面白さの核の実在検証】
- **必要時**: `characters.yaml`（登場キャラのみ）/ `concept.yaml`（catharsis_engine・misunderstanding_escalation）/ `arc_summary.yaml` 該当幕(acts) / CSV該当行
- **読まない**: 関係しない章。worldview・magicは該当項目のみ（全文不要）。**第1アーク凍結レイヤー**（仲間・第零機関・ヴェルミ・遺技ロードの深層＝nork background深層・legacy_load・zero_institution/vermi）——章設計の材料にしない（concept.yaml冒頭の凍結規律・2026-07-05）

### ケースC: スキーマ移行・全章一括の整合作業
- **必読**: 対象テンプレート / 対象全ファイル / CSV / `arc_summary.yaml`
- **同梱**: 意味残骸の監査（deprecated_termsのスイープ＋精読時の文意チェック）——全件を読む機会は希少なので監査を相乗りさせる

### ケースD: 語彙・設定の変更（決定事項の波及処理）
- **手順固定**: grep全列挙→スコープ宣言→正本→派生→`deprecated_terms.yaml`登録（ARCHITECTURE 3章・決定事項フック）
- **読むのはgrepヒット箇所のみ**。ファイル全文の読み込みは不要

### ケースE: コミット
- コミット前フックのみ（deprecated_termsスイープ＋CONTEXT/TODO反映確認）。追加の読み込み不要

### ケースF: L4執筆（シーン生成。CH01 scene_01/02 の実績で更新 2026-07-02）
- **必読**: 対象章summary（catharsis_coreゲート確認）/ `template_scene_input.yaml` / ARCHITECTURE [Hook: L4執筆時] / `00_system/prompt_templates/scene_generation_prompt.md`（レンダー規律の正本＝ミクロ変数の定量制御・描写厳守3点）/ `SELF_REVIEW.md` §1・§2＋§3c（レンダー層セルフパス）/ `characters.yaml`の登場キャラ（output_hook・appearance・dialogue_samples・speech_rule）
- **必要時**: 直前シーンの scene_input＋本文（継続性——固有名の初出管理・段1反動の引き継ぎで実績あり）/ `setting_magic.yaml` biological_cost（代償描写の単一出典＝TODO.md E項）/ `02_dynamic_states`の3台帳（長距離・累積・誤読。初期投入後）
- **読まない**: `_workspace`内の旧ドラフト（旧語彙が残存。TODO.md E項）。**第1アーク凍結レイヤー**（仲間・第零機関・ヴェルミ・遺技ロードの深層）——本文へ開示しない・材料にしない（concept.yaml冒頭の凍結規律・2026-07-05。接点はCH05一行／CH16-17相棒破損リスク／CH19引きの3点のみ）
- **生成前ゲート**: `00_system/validate.py` でスキーマ・open_questions全resolved・【負荷】上限を機械検査（④自動バリデーションの検査器）

### ケースG: A2第1アーク再構成（試作ループ・2026-07-07新設）
- **必読（親セッション＝設計・判定記帳役）**: `_workspace/canon/` 3本（憲章=最上位／骨格／戦闘カノン）＋ `_workspace/probes/arc01_probes.md`（試作台帳＝判定ログ・注意台帳。**親専用**）
- **コールドレンダー**: 渡すのはパケット（`_workspace/probes/renders/`）＋憲章＋骨格のみ。**試作台帳・旧ドラフト（06）・characters.yaml は渡さない**（台帳汚染の実測＝試作1 v4・注意⓮パケット方式）
- **読まない**: 01〜06のプール全般（参照は「候補」扱い・借用は decision_log で申告＝憲章§2。再承認済みキー＝`# status: reapproved` は拘束あり）／CONTEXT の直近セッションより前／`_workspace/archive/`
- **判定**: 人間の読了判定が終了条件。複数項目はレビューシート方式（ARCHITECTURE §3 [Hook: 複数項目フィードバック時]）
