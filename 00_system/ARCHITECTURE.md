# ARCHITECTURE.md — 4階層アーキテクチャとフック構造

## 1. 4階層アーキテクチャ（出力マッピング）
当プロジェクトは、エンタメ性と一貫性を担保するため以下の4階層で構成される。

- **L1: Macro Concept** → `03_macro_concept/` (作品全体の究極目標・危機)
- **L2: Meso Arc** → `04_meso_plot/arc_XX/` (4幕構造を持つ中長期シナリオ・章)
- **L3: Micro Chapter** → `04_meso_plot/arc_XX/` 内の `chapter_summary.yaml` (連載1話分の変数刺激管理とミニ三幕)
- **L4: Nano Scene** → `05_micro_scene/` (AI執筆用のパラメーター指示)

## 2. 完全チェーン・フック構造（必須参照ルール）
下位構造のドキュメントやプロンプトを作成するAIエージェントは、作業前に必ず**直上の上位構造ドキュメント**を読み込むこと。

- **Arc作成時**: `03_macro_concept/template_concept.yaml` を参照。
- **Chapter作成時**: 上位の `04_meso_plot/arc_XX/arc_summary.yaml` と `chapter_sequence.csv` を参照。
- **Scene作成時**: 上位の `04_meso_plot/arc_XX/chapter_YY_summary.yaml` を参照。
- **全AI共通**: 変数を操作・マッピングする際は必ず `00_system/variable_rules.md` を参照すること。
