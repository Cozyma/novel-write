# 小説執筆・自動更新フレームワーク

本リポジトリは、人間とAIエージェントが協働して小説を執筆・推敲し、関連するデータを自動更新するためのフレームワークです。

> 📖 **企画・プロット草案へのフィードバックをお探しの方は → [OVERVIEW.md（企画概要とレビューの歩き方）](OVERVIEW.md)**
> 本READMEはシステム・運用ルールの定義（主にAIエージェント向け）です。

## 1. 全体ディレクトリ構造

```plaintext
/novel_framework_repo
├── README.md                 # 本指示書（システムルール・運用フローの定義）
├── CLAUDE.md                 # Claude Code用エントリポイント（AGENTS.mdを読み込む）
├── AGENTS.md                 # 【AI規約】エージェントの振る舞い・運用ルール（AI必読）
├── _workspace/               # 【自由検討領域】人間とAIの壁打ち・メモ（AIは指示なしに読み込まない）
│   ├── CONTEXT.md            # 作業文脈・決定事項ログ（セッション開始時に必読）
│   ├── TODO.md               # 執筆TODO（セッション開始時に必読）
│   ├── 01_macro_notes/       # 企画・キャラクター設計の検討ログ
│   ├── 02_meso_notes/        # 話数ごとの展開や変数のピーク調整
│   ├── 02_meso_plot/         # プロット草案（旧版含む。正式版は 04_meso_plot/ のみを参照）
│   ├── 03_micro_notes/       # シーン内の具体的な行動（Fact）の推敲
│   └── imported_settings/    # 旧プロジェクトから取り込んだ設定（精査済み・正式版はDBへ移行済み）
├── 00_system/                # 【システムルール】プロンプトと制約条件の定義
│   ├── ARCHITECTURE.md       # 4階層アーキテクチャ・参照チェーン・運用フック（構造ルールの正本）
│   ├── SELF_REVIEW.md        # AIの自己検証・メタチェック指針
│   ├── variable_rules.md     # 7変数の定義・判定基準（変数定義の正本）
│   ├── trait_patterns.yaml   # キャラ特性×変数寄与の抽象パターン定義（マッピング層）
│   └── prompt_templates/     # 処理別（生成、推敲、状態抽出）のプロンプト
├── 01_static_database/       # 【不変データ】世界観・キャラクターの絶対的真実（語彙の単一出典）
│   ├── characters.yaml       # 人物DB（経歴、口調、story_hooks、output_hook）
│   ├── world/                # 世界観、地理、用語集、歴史的ルール
│   └── timeline.md           # 絶対時間の総合年表（出来事が起きた時系列）
├── 02_dynamic_states/        # 【動的データ】本文（正本）から再構成困難な状態のみの派生台帳（章完成時更新）
│   ├── character_states.yaml # 累積カウンタ（exposure_level等：全話を読み返さないと合計できない値）
│   ├── resources_states.yaml # 長距離の事実・チェーホフの銃台帳（隣接コンテキスト外で回収される仕込み）
│   └── reader_knowledge.yaml # 認識・誤読台帳（キャラ別の対ノルク誤読モデル＋読者への開示状況）
├── 03_macro_concept/         # 【L1 作品方針】コンセプト・優先変数（concept.yaml / template_concept.yaml）
├── 04_meso_plot/             # 【L2/L3 プロット】アーク・チャプター構成（template_*.yaml がスキーマ正本）
│   └── arc_XX/
│       ├── arc_summary.yaml        # アーク全体のエピソード構成（L2）
│       ├── chapter_sequence.csv    # 章の並び・クエスト・引きの索引（派生）
│       └── chapter_XX_summary.yaml # 章のミニ三幕・catharsis_core（L3・ビートの正本）
├── 05_micro_scene/           # 【L4 執筆指示】AIへの直接的なインプット
│   └── chapter_XX/
│       └── scene_YY_input.yaml # 起こる事実（Fact）・open_questions・段落ごとの変数指定
├── 06_draft_output/          # 【AI生成結果】AIが出力した一次原稿
│   └── chapter_XX/
│       ├── scene_YY_draft.md  # 生成された本文テキスト（decision_logを必ず添付）
│       └── scene_YY_eval.json # テキストに対するAIの変数自己評価スコア
└── 07_final_text/            # 【最終成果物】人間が推敲・確定した最終原稿
```

※ `05_micro_scene/` 以下の格納は章（chapter）単位で切る。L3が章単位のため、シーンの親は常に章である。

## 2. 7変数のスコープ（解像度）定義

変数定義の**正本は `00_system/variable_rules.md`**（シーン単位のマクロ駆動系4変数：探求・報酬・驚き・危機／段落単位のミクロ処理系3変数：負荷・感覚・共感、および【負荷】上限80%等の判定基準）。本READMEには定義の複製を置かない（正本→派生同期の片側更新を防ぐため。`00_system/ARCHITECTURE.md` 2.1参照）。

## 3. シーン執筆・自動更新の実行フロー（Hook仕様）

執筆ワークフロー全体の正本は `00_system/ARCHITECTURE.md` の「[Hook: L4執筆時]」（未決列挙→対話解決→初版自動生成＋判断ログ→自動バリデーション→人間判定→還流）。本節は状態管理に関わる差分のみを定義する。

**基本原則**: 執筆開始後、シーン内の事実の正本は**本文**である。`02_dynamic_states/` は「本文から再構成困難な状態」（長距離の事実・累積カウンタ・認識/誤読）のみを持つ派生台帳であり、短距離の物理状態（現在地・負傷・疲労・所持品）は台帳管理しない。

- **Step 1: Pre-Hook（前提条件の同期）**
  - **処理**: `05_micro_scene/` の指示ファイル（open_questions全解決済みであること）、直近の章サマリー・前シーン本文、および `02_dynamic_states/` の台帳を読み込む。
  - 短距離の状態は台帳ではなく直近コンテキスト（前シーン本文・章サマリー）から再構成する。台帳・直近本文と矛盾する描写を禁止する。
- **Step 2: Generation（描写のレンダリング）**
  - **処理**: ARCHITECTURE.mdのL4フローに従い本文を生成し、サマリーに無い判断を `decision_log` として添付する。
  - **出力先**: `06_draft_output/episode_XX/scene_YY_draft.md`
- **Step 3: 状態関連イベントの抽出**
  - **処理**: decision_logと本文から「台帳対象の変化」のみを抽出する——長距離の仕込み（チェーホフの銃）、累積カウンタの加算（exposure_level等）、認識・誤読モデルの変化、読者への開示。短距離の物理変化は抽出対象外（本文が正本）。
- **Step 4: Commit（章完成時の台帳反映）**
  - **処理**: 毎シーンではなく**章（チャプター）完成・人間判定通過後**に、Step 3の抽出分を台帳へ反映する。「正本（本文）→派生（台帳）」の同期方向を厳守（ARCHITECTURE.md 2.1参照）。
- **Step 5: Validation-Hook（論理チェック）**
  - **処理**: 更新後の台帳が `01_static_database/` の世界観ルールやタイムラインと矛盾していないかを機械的に検証する。【負荷】が上限値（80%）を超えている場合、または論理破綻を検知した場合は処理を停止し、人間にアラートを出力する。

## 4. エージェントへの基本命令（Prompt Grounding）

> 「あなたはこのリポジトリ内のデータを統制・出力するAIエージェントです。執筆ワークフローは `00_system/ARCHITECTURE.md` の[Hook: L4執筆時]に従ってください。本文の生成は各ファイルに定義された事実（Fact）と変数指定に基づいて行い、サマリーやscene_inputに無い判断（解釈・補完・発明）を行った場合は、隠さず必ず `decision_log` として可視化し本文とセットで提出してください。生成の開始条件は、該当章の `catharsis_core` が具体的な仮核として成立しており、かつ scene_input の `open_questions` がすべて解決済みであることです。」
