# 小説執筆ハーネス — システム設計と運用ルール

本リポジトリは、人間とAIエージェントが協働して小説を設計・執筆・推敲するための**ハーネス（制作システム）**です。本READMEはその設計思想・ディレクトリ構造・実行フローを定義します（主にAIエージェント向け）。

> 📖 **物語そのもの（企画・面白さ・コンセプト・プロット）を知りたい方は → [OVERVIEW.md（企画概要）](OVERVIEW.md)**

## 1. 設計思想（コア原則）

このハーネスは「エンタメ性は検証項目化しきれない」という前提に立ち、**機械にできる統制は機械へ、できない判定は人間へ**を軸に設計されている。

- **4階層アーキテクチャ**: 物語設計を L1 コンセプト → L2 アーク → L3 章 → L4 シーンの4階層に分割し、下位の作成時は必ず直上の正本を参照する（完全チェーン）。各層は「そのスケールの面白さの核」フィールドと「親の核のインスタンスであることの検査」を対で持つ。→ 正本: [00_system/ARCHITECTURE.md](00_system/ARCHITECTURE.md) §1・§2
- **正本→派生の単方向同期**: 同一の事実が複数ファイルにある場合、必ず正本を1つ定め、修正は「正本→派生」の順で一括同期する。派生は構造・索引のみを持ち、出来事の再話（散文の複製）を持たない——再話派生は構造的に必ずドリフトする。執筆開始後、シーン内の事実の正本は**本文**であり、台帳（`02_dynamic_states/`）は「本文から再構成困難な状態」だけを持つ派生。→ 正本: ARCHITECTURE.md §2.1
- **語彙の単一出典**: 複数ファイルで使う固有名詞・用語は `01_static_database/` に定義を置いてから使う。廃止した語彙は `00_system/deprecated_terms.yaml` に死語登録し、コミット前フックが機械grepで残骸を検出する。
- **検証の分業**: 機械検査（`00_system/validate.py`・pre-commit フック）が担うのはスキーマ準拠・生成ゲート・負荷上限・語彙残骸など**検証可能な項目のみ**。「文章として面白いか」は検証項目化できない（検証可能性バイアス）ため、**人間の読了判定を執筆ループの終了条件**とし、自動ループで代替しない。
- **判断の可視化（decision_log）**: AIがサマリー・指示に無い判断（解釈・補完・発明）をした場合、必ず `decision_log` として本文とセットで提出する。暗黙に埋まった判断はそれらしく読めてしまい検出不能になる。
- **トークン規律**: 作業前に `00_system/REFERENCE_MAP.md` で作業ケース別の最小参照セットを決めてから読む。全ファイルの無差別読み込みをしない。

構造ルール・イベントフックの正本は [00_system/ARCHITECTURE.md](00_system/ARCHITECTURE.md)、エージェントの振る舞い規約は [AGENTS.md](AGENTS.md)、セルフレビュー指針は [00_system/SELF_REVIEW.md](00_system/SELF_REVIEW.md)。

## 1b. 権威マップ（A2再構成期間の特例・2026-07-06〜）

第1アーク全面再構成（人間決定・憲章参照）の期間中、権威の所在は通常の4階層と**異なる**：

- **拘束文書＝ `_workspace/canon/`**——`arc01_rebuild_charter.md`（憲章・最上位）→ `arc01_skeleton_draft.md`（骨格）→ `arc01_combat_canon_draft.md`（戦闘カノン）
- **`01_static_database/`〜`06_draft_output/` は提案プール**＝拘束力なし（各直下の `_POOL_NOTICE.md` 参照）。例外＝`# status: reapproved` コメント付きのキーのみ再承認済み＝拘束あり
- **`00_system/` は作業規約として全面有効**（設定ではなくプロセス。ただし文中の実例は旧設定を指すことがある＝再構成確定後に差し替え）
- 試作の実執筆は `_workspace/probes/`（台帳＝親専用／`renders/`＝コールドレンダーの参照面。最小参照セット＝REFERENCE_MAP ケースG）
- **再構成確定後**: 新世代正本は版付きサブディレクトリ（例 `04_meso_plot/arc_01_v2/`）へ着地し、本節を撤去して通常の4階層権威へ戻す（憲章 §7-3）

## 2. 全体ディレクトリ構造

```plaintext
/novel_framework_repo
├── README.md                 # 本指示書（ハーネス設計・運用フローの定義）
├── OVERVIEW.md               # 企画概要（編集者・レビュアー向け。物語の中身はこちら）
├── CLAUDE.md                 # Claude Code用エントリポイント（AGENTS.mdを読み込む）
├── AGENTS.md                 # 【AI規約】エージェントの振る舞い・運用ルール（AI必読）
├── _workspace/               # 【作業領域】（2026-07-07に3層へ再編）
│   ├── CONTEXT.md            # 作業文脈・決定事項ログ（セッション開始時に必読・直近のみ保持）
│   ├── TODO.md               # 執筆TODO（セッション開始時に必読）
│   ├── canon/                # 【現行の拘束文書】憲章・骨格・戦闘カノン（→ §1b 権威マップ）
│   ├── probes/               # 試作台帳（arc01_probes.md＝親専用）／renders/＝レンダー本文・パケット（コールドの参照面）
│   └── archive/              # 旧ログ（CONTEXT_archive）・旧notes・棚卸し記録（通常セッションでは読まない。旧語彙残存）
├── 00_system/                # 【システムルール】プロンプトと制約条件の定義
│   ├── ARCHITECTURE.md       # 4階層アーキテクチャ・参照チェーン・運用フック（構造ルールの正本）
│   ├── SELF_REVIEW.md        # AIの自己検証・メタチェック指針（フェーズ別 §3a/3b/3c）
│   ├── REFERENCE_MAP.md      # 作業ケース別の最小参照セット（トークン節約の索引）
│   ├── variable_rules.md     # 7変数の定義・判定基準（変数定義の正本。§0＝診断軸であり生成ターゲットにしない）
│   ├── UNIVERSAL_LESSONS.md  # プロジェクト非依存の普遍教訓（定式生成の不可能性・観測可能性ゲート・オラクル中心設計）
│   ├── deprecated_terms.yaml # 廃止語彙・死語台帳（コミット前フックが機械grep）
│   ├── validate.py           # scene_input／chapter_summary のスキーマ・負荷上限・生成ゲートの検査器
│   ├── git_hooks/            # バージョン管理された git フック（pre-commit＝残骸grep＋反映確認）
│   └── prompt_templates/     # 処理別（生成、推敲、状態抽出）のプロンプト
├── 01_static_database/       # 【不変データ】世界観・キャラクターの絶対的真実（語彙の単一出典）
│   ├── characters.yaml       # 人物DB（経歴、口調、story_hooks、output_hook）
│   └── world/                # 世界観、地理、用語集、歴史的ルール
├── 02_dynamic_states/        # 【動的データ】本文（正本）から再構成困難な状態のみの派生台帳（章完成時更新）
│   ├── character_states.yaml # 累積カウンタ（金銭・ツケ等の真の合算値のみ。exposure_level は廃止 2026-07-07）
│   ├── resources_states.yaml # 長距離の事実・チェーホフの銃台帳（隣接コンテキスト外で回収される仕込み）
│   └── reader_knowledge.yaml # 廃止（2026-07-07・トリガー付き保留＝ARCHITECTURE 2.1。ファイルはプール素材として残置）
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
│       └── scene_YY_draft*.md # 生成された本文テキスト（decision_log・セルフパス結果を必ず添付）
└── 07_final_text/            # 【最終成果物】人間が推敲・確定した最終原稿
```

※ `05_micro_scene/` 以下の格納は章（chapter）単位で切る。L3が章単位のため、シーンの親は常に章である。連載粒度はシーン単位＝1話（2026-06-18確定）。

### セットアップ（新規クローン時）

```sh
git config core.hooksPath 00_system/git_hooks   # コミット前フック（deprecated_terms残骸grep＋CONTEXT/TODO反映確認）を有効化
python 00_system/validate.py                    # scene_input／chapter_summary の機械検査（依存ライブラリ不要）
```

## 3. シーン執筆・自動更新の実行フロー（Hook仕様）

執筆ワークフロー全体の正本は `00_system/ARCHITECTURE.md` の「[Hook: L4執筆時]」（未決列挙→対話解決→初版自動生成＋判断ログ→自動バリデーション→人間判定→還流）。本節は状態管理に関わる差分のみを定義する。

**基本原則**: 執筆開始後、シーン内の事実の正本は**本文**である。`02_dynamic_states/` は「本文から再構成困難な状態」（長距離の事実・累積カウンタ・認識/誤読）のみを持つ派生台帳であり、短距離の物理状態（現在地・負傷・疲労・所持品）は台帳管理しない。

- **Step 1: Pre-Hook（前提条件の同期）**
  - **処理**: `05_micro_scene/` の指示ファイル（open_questions全解決済みであること）、直近の章サマリー・前シーン本文、および `02_dynamic_states/` の台帳を読み込む。
  - 短距離の状態は台帳ではなく直近コンテキスト（前シーン本文・章サマリー）から再構成する。台帳・直近本文と矛盾する描写を禁止する。
- **Step 2: Generation（描写のレンダリング）**
  - **処理**: ARCHITECTURE.mdのL4フローに従い本文を生成し、サマリーに無い判断を `decision_log` として添付する。
  - **出力先**: `06_draft_output/chapter_XX/scene_YY_draft*.md`
- **Step 3: 状態関連イベントの抽出**
  - **処理**: decision_logと本文から「台帳対象の変化」のみを抽出する——長距離の仕込み（チェーホフの銃＝planted/fired）と真の累積値（金銭・ツケ等）の加算のみ（認識・誤読台帳と目撃露出度は廃止 2026-07-07＝ARCHITECTURE 2.1）。短距離の物理変化は抽出対象外（本文が正本）。
- **Step 4: Commit（章完成時の台帳反映）**
  - **処理**: 毎シーンではなく**章（チャプター）完成・人間判定通過後**に、Step 3の抽出分を台帳へ反映する。「正本（本文）→派生（台帳）」の同期方向を厳守（ARCHITECTURE.md 2.1参照）。
- **Step 5: Validation-Hook（論理チェック）**
  - **処理**: 更新後の台帳が `01_static_database/` の世界観ルールと矛盾していないかを検証する。機械検査可能な項目（スキーマ準拠・open_questions全resolved＝生成ゲート・【負荷】上限80%・語彙）は `00_system/validate.py` が担う。論理破綻を検知した場合は処理を停止し、人間にアラートを出力する。

## 4. 7変数のスコープ（解像度）定義

変数定義の**正本は `00_system/variable_rules.md`**（シーン単位のマクロ駆動系4変数：探求・報酬・驚き・危機／段落単位のミクロ処理系3変数：負荷・感覚・共感、および【負荷】上限80%等の判定基準）。本READMEには定義の複製を置かない（正本→派生同期の片側更新を防ぐため。`00_system/ARCHITECTURE.md` 2.1参照）。

## 5. エージェントへの基本命令（Prompt Grounding）

> 「あなたはこのリポジトリ内のデータを統制・出力するAIエージェントです。執筆ワークフローは `00_system/ARCHITECTURE.md` の[Hook: L4執筆時]に従ってください。本文の生成は各ファイルに定義された事実（Fact）と変数指定に基づいて行い、サマリーやscene_inputに無い判断（解釈・補完・発明）を行った場合は、隠さず必ず `decision_log` として可視化し本文とセットで提出してください。生成の開始条件は、該当章の `catharsis_core` が具体的な仮核として成立しており、かつ scene_input の `open_questions` がすべて解決済みであることです。」
