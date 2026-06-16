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
| ノルクの手札①〜⑤と誤読対・切り札の概要 | `01_static_database/characters.yaml` / nork combat_style |
| 切り札の制約詳細（生体負荷・感情ノイズ・隠匿・遮断）・条項告発・遺技ロード・破礼具 | `01_static_database/world/setting_magic.yaml` |
| バディ対比（二種類の自前） | `setting_magic.yaml` / combat_contrast.buddy_contrast |
| 報酬番号の台帳（有形1〜5・無形1〜4） | `04_meso_plot/arc_01/arc_summary.yaml` / reward_chain |
| アークのカタルシス曲線・sub_catharsis・roadmap_step・章割当 | `04_meso_plot/arc_01/arc_summary.yaml` / acts（setup→buildup→despair→catharsis。role＝構造役割のみ）・macro_linkage。章→段の束ねは `chapter_sequence.csv` の episode_id 列 |
| 成長ロードマップ（バディ二人制・最重要・暫定） | ノルク=`concept.yaml`/protagonist_growth_roadmap、マーレン=`characters.yaml`/marlen.growth_roadmap、二人制検査=`ARCHITECTURE.md` 2.3 |
| 章の核・ビート（正本。CSV・arc_summaryは派生） | `04_meso_plot/arc_01/chapter_XX_summary.yaml` |
| 長距離伏線（muddy_blood_paradox・第零機関の種） | `02_dynamic_states/resources_states.yaml` |
| 累積カウンタ（nork.exposure_level） | `02_dynamic_states/character_states.yaml` |
| キャラ別誤読モデル・読者開示 | `02_dynamic_states/reader_knowledge.yaml` |
| 没案の退避先 | `_workspace/01_macro_notes/discarded_ideas.md` |
| 部隊ロスター草案（仮置き・未確定） | `_workspace/01_macro_notes/squad_roster_draft.md` |

## 2. 作業ケース→最小参照セット

### ケースA: 世界法則・設定の壁打ち（新設・変更）
- **必読**: `CONTEXT.md`直近 / `TODO.md` / `SELF_REVIEW.md`（世界法則の帰結検証・氷山の規律）/ 対象の設定ファイル（worldview・magic・charactersの該当キャラ）
- **必要時**: `concept.yaml`（主従ルール・catharsis_engineとの矛盾チェック＝還流）
- **読まない**: 章サマリー全件——整合確認はgrepで全列挙し、ヒットした章だけ読む
- **終了時**: 死語が出たら `deprecated_terms.yaml` へ登録。正本→派生の順で一括同期

### ケースB: 章の核・プロットの壁打ち（対象1〜2章）
- **必読**: `template_chapter_summary.yaml` / 対象章＋前後章のsummary / `SELF_REVIEW.md`【面白さの核の実在検証】
- **必要時**: `characters.yaml`（登場キャラのみ）/ `concept.yaml`（catharsis_engine・misunderstanding_escalation）/ `arc_summary.yaml` 該当幕(acts) / CSV該当行
- **読まない**: 関係しない章。worldview・magicは該当項目のみ（全文不要）

### ケースC: スキーマ移行・全章一括の整合作業
- **必読**: 対象テンプレート / 対象全ファイル / CSV / `arc_summary.yaml`
- **同梱**: 意味残骸の監査（deprecated_termsのスイープ＋精読時の文意チェック）——全件を読む機会は希少なので監査を相乗りさせる

### ケースD: 語彙・設定の変更（決定事項の波及処理）
- **手順固定**: grep全列挙→スコープ宣言→正本→派生→`deprecated_terms.yaml`登録（ARCHITECTURE 3章・決定事項フック）
- **読むのはgrepヒット箇所のみ**。ファイル全文の読み込みは不要

### ケースE: コミット
- コミット前フックのみ（deprecated_termsスイープ＋CONTEXT/TODO反映確認）。追加の読み込み不要

### ケースF: L4執筆（シーン生成。未実施・着手時に実績で更新すること）
- **必読**: 対象章summary（catharsis_coreゲート確認）/ `template_scene_input.yaml` / `characters.yaml`の登場キャラoutput_hook / ARCHITECTURE [Hook: L4執筆時]
- **必要時**: `02_dynamic_states`の3台帳（長距離・累積・誤読）/ 直前章summary・前シーン本文
- **読まない**: `_workspace`内の旧ドラフト（旧語彙が残存。TODO.md E項）
