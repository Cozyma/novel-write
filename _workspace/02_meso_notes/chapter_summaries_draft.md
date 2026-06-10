# Chapter 1-19 ミニ三幕構造 草案

## 第1話（Chapter 1）
```yaml
chapter_id: "CH_01"
arc_linkage: "第1アーク / 導入（起）"

chapter_stimulus:
  peak_variable: "危機" # スィグナの死の危機による緊迫感

chapter_acts:
  act1_intro:
    hook: "スラムでの凄腕暗殺者との遭遇。情報屋スィグナが追い詰められる絶望的な状況。"
  act2_conflict:
    build_up: "護衛が次々と倒され、スィグナ自身の策も通用しない。暗殺者の圧倒的な実力（システム加護）による生存への脅威。"
  act3_climax:
    turn: "スィグナが死を覚悟した瞬間、路地裏から「場違いなほど覇気のない青年（ノルク）」が偶然通りかかる。"
    cliffhanger: "絶体絶命の窮地に、ただの巻き込まれに見える青年が介入してくるという謎の【探求】で引く。"

scenes:
  - scene_01: "スィグナと暗殺者の遭遇と絶望的な戦闘"
  - scene_02: "ノルクの不運な遭遇（面倒ごとへの巻き込まれ）"

validation_hook:
  is_linked_to_arc: true
  has_clear_stimulus: true
```

## 第2話（Chapter 2）
```yaml
chapter_id: "CH_02"
arc_linkage: "第1アーク / 導入（起）の解決"

chapter_stimulus:
  peak_variable: "報酬" # 圧倒的脅威を排除する無双カタルシスと勘違い

chapter_acts:
  act1_intro:
    hook: "暗殺者の凶刃がノルクに迫るが、彼が「面倒だ」と息を吐きながら防ぐ。"
  act2_conflict:
    build_up: "ノルクが「手抜き処理」のためにギリギリの攻防を装いながら、実際は最適化された挙動で暗殺者をいなす。暗殺者は手も足も出ず、圧倒的な実力差に恐怖して敗走する（ノルクは追わない）。"
  act3_climax:
    turn: "あっさりと脅威が去り、助かったスィグナは彼がただ者ではないと確信する。【無形報酬1: スィグナからの極めて高い評価】"
    cliffhanger: "スィグナに弱み（あるいは面倒事）を握られ、「明日、ギルドに登録して私の駒になりなさい」と強引に裏の所属【有形報酬1: 裏社会のコネ】を決められ、平穏から遠ざかる絶望で引く。"

scenes:
  - scene_01: "ノルクと暗殺者の戦闘（手抜きと暗殺者の敗走）"
  - scene_02: "スィグナによるノルクの強制ギルド登録指示"

validation_hook:
  is_linked_to_arc: true
  has_clear_stimulus: true
```

## 第3話（Chapter 3）
```yaml
chapter_id: "CH_03"
arc_linkage: "第1アーク / 展開（承）の入り口"

chapter_stimulus:
  peak_variable: "驚き" # 恐怖からの過剰評価というギャップ

chapter_acts:
  act1_intro:
    hook: "翌日、不本意ながらギルドへ登録にやってきたノルク。"
  act2_conflict:
    build_up: "受付で、昨夜の暗殺者（表の顔はギルドの上位者）が新人いびりでノルクに絡んでくる。しかしノルクの些細な仕草から、上位者が「昨夜の化け物だ」と気づいてしまう。"
  act3_climax:
    turn: "上位者が恐怖を完全に誤魔化すため、手のひらを返して震えながらノルクに過剰な高評価を与え、厄介払いしようとする。【無形報酬2: ギルド上位者からの畏怖】【有形報酬2: 特別枠の好待遇認定】"
    cliffhanger: "その理不尽な高評価のせいで、よりによって一番面倒な堅物エリート査定官（マーレン）との合同任務に放り込まれ、頭を抱えるノルクで引く。"

scenes:
  - scene_01: "ギルドでの上位者による新人いびりと正体露見（暗殺者視点の恐怖）"
  - scene_02: "恐怖の過剰評価とマーレンとの強制パーティー結成"

validation_hook:
  is_linked_to_arc: true
  has_clear_stimulus: true
```

## 第4話（Chapter 4）
```yaml
chapter_id: "CH_04"
arc_linkage: "第1アーク / 展開（承）"

chapter_stimulus:
  peak_variable: "探求" # 正体不明のプレッシャー

chapter_acts:
  act1_intro:
    hook: "街道調査に出発。道中、ノルクの適当な振る舞いにマーレンの不満が蓄積する。"
  act2_conflict:
    build_up: "不意に魔物の気配を察知した際、マーレンが気付く前にノルクが適当な理由をつけて最適な回避位置に移動する。"
  act3_climax:
    turn: "戦闘の直前、マーレンが彼から一瞬だけ異質なプレッシャーを感じ取る。"
    cliffhanger: "背筋が凍るような「死地の気配」を察知し、ただの無能ではないかもしれないと彼女の認識が揺らぐところで引く。"

scenes:
  - scene_01: "街道での移動と不和"
  - scene_02: "ノルクから漏れ出た異質な気配"

validation_hook:
  is_linked_to_arc: true
  has_clear_stimulus: true
```

## 第5話（Chapter 5）
```yaml
chapter_id: "CH_05"
arc_linkage: "第1アーク / 展開（承）"

chapter_stimulus:
  peak_variable: "危機" # 定型対応が通じないピンチ

chapter_acts:
  act1_intro:
    hook: "薬物強化された異常な魔物との遭遇。"
  act2_conflict:
    build_up: "マーレンがマニュアル通りの完璧な対応を見せるが、強化された魔物には致命傷とならない。"
  act3_climax:
    turn: "マーレンの防衛線が突破され、彼女自身の安全が脅かされる。"
    cliffhanger: "マニュアルが通用しない絶体絶命の危機に陥る。"

scenes:
  - scene_01: "異常な魔物との遭遇"
  - scene_02: "定型対応の崩壊と防衛突破"

validation_hook:
  is_linked_to_arc: true
  has_clear_stimulus: true
```

## 第6話（Chapter 6）
```yaml
chapter_id: "CH_06"
arc_linkage: "第1アーク / 展開（承）"

chapter_stimulus:
  peak_variable: "驚き" # 適当な男の異常な実力と実利

chapter_acts:
  act1_intro:
    hook: "魔物の一撃がマーレンに迫る瞬間。"
  act2_conflict:
    build_up: "ノルクが「死体にすると素材の価値が下がる」とため息をつき、最小限の動きで魔物の攻撃をいなす。"
  act3_climax:
    turn: "極めて実務的な非殺制圧（手抜き）であっさりと無傷のまま魔物を排除する。【無形報酬3: マーレンの戦慄と再評価】"
    cliffhanger: "マーレンが畏怖する中、ノルクが「これでボーナス確定だな」と生け捕り報酬に喜ぶギャップで引く。"

scenes:
  - scene_01: "ノルクの介入と手抜き処理"
  - scene_02: "マーレンの戦慄と再評価"

validation_hook:
  is_linked_to_arc: true
  has_clear_stimulus: true
```

## 第7話（Chapter 7）
```yaml
chapter_id: "CH_07"
arc_linkage: "第1アーク / 展開（承）"

chapter_stimulus:
  peak_variable: "危機" # 社会的・組織的な行き詰まり

chapter_acts:
  act1_intro:
    hook: "街に帰還。無傷の魔物は高額で買い取られ、ノルクは多額の特別ボーナスを獲得。【有形報酬3: 特別ボーナスと決定的な証拠】"
  act2_conflict:
    build_up: "魔物から検出された薬物の痕跡（証拠）をもとに、マーレンが上層部に密造網の捜査権を申請するが、謎の圧力によって握り潰される。"
  act3_climax:
    turn: "決定的な証拠があるのに、正論とマニュアルが組織の根回しに敗北する。"
    cliffhanger: "自分が信じる「教条」が機能せず、完全に手詰まりとなる絶望感で引く。"

scenes:
  - scene_01: "ボーナスの獲得と証拠の発見"
  - scene_02: "ギルド上層部による捜査の妨害"

validation_hook:
  is_linked_to_arc: true
  has_clear_stimulus: true
```

## 第8話（Chapter 8）
```yaml
chapter_id: "CH_08"
arc_linkage: "第1アーク / 展開（承）の底"

chapter_stimulus:
  peak_variable: "共感" # マーレンの挫折への同情

chapter_acts:
  act1_intro:
    hook: "それでも教条に従い、孤立しながら奔走するマーレン。"
  act2_conflict:
    build_up: "正攻法で壁を突破しようとするが、どこに行っても門前払いを食らい、彼女の心が摩耗していく。"
  act3_climax:
    turn: "路地裏で崩れ落ち、自身の無力さとマニュアルの限界に直面する。"
    cliffhanger: "その横でノルクが「じゃあ裏から行くか」と面倒くさそうに宣言する。"

scenes:
  - scene_01: "マーレンの孤独な奔走"
  - scene_02: "挫折とノルクの提案"

validation_hook:
  is_linked_to_arc: true
  has_clear_stimulus: true
```

## 第9話（Chapter 9）
```yaml
chapter_id: "CH_09"
arc_linkage: "第1アーク / 展開（承）の反転"

chapter_stimulus:
  peak_variable: "驚き" # 教条外のアプローチによる解決

chapter_acts:
  act1_intro:
    hook: "ノルクがスィグナの組織（第1〜2話で得た裏ルート）を活用し、情報収集をスタートする。"
  act2_conflict:
    build_up: "マーレンの常識を覆すような、物理的・心理的圧力を伴う効率的な脅迫や交渉で、次々と情報が引き出されていく。"
  act3_climax:
    turn: "あっという間に密造網のアジトを特定するノルク。"
    cliffhanger: "結果を出す彼に対し、マーレンの中に「自分にはない力への依存の萌芽」が生まれる。"

scenes:
  - scene_01: "ノルクによる裏の情報収集"
  - scene_02: "アジトの特定とマーレンの心境変化"

validation_hook:
  is_linked_to_arc: true
  has_clear_stimulus: true
```

## 第10話（Chapter 10）
```yaml
chapter_id: "CH_10"
arc_linkage: "第1アーク / 転（ミッドポイント直前）"

chapter_stimulus:
  peak_variable: "危機" # ボスの正体の判明

chapter_acts:
  act1_intro:
    hook: "特定したアジト周辺の状況確認。"
  act2_conflict:
    build_up: "内部の様子を探る中で、裏のボスが「システム加護を悪用する汚職エリート」である事実が判明する。"
  act3_climax:
    turn: "そのエリートが持つ権限とバフの凶悪さが浮き彫りになる。"
    cliffhanger: "現状の戦力では到底太刀打ちできない絶望的な戦力差に直面して引く。"

scenes:
  - scene_01: "アジトへの潜入準備"
  - scene_02: "ボスの正体とシステムの理不尽の判明"

validation_hook:
  is_linked_to_arc: true
  has_clear_stimulus: true
```

## 第11話（Chapter 11）
```yaml
chapter_id: "CH_11"
arc_linkage: "第1アーク / 転（突入）"

chapter_stimulus:
  peak_variable: "驚き" # マーレンの決意と強行突破

chapter_acts:
  act1_intro:
    hook: "戦力差を理解しつつも、マーレンは自身の正義を貫くため密造工房への強襲を決行する。"
  act2_conflict:
    build_up: "ノルクのサポートを受けつつ、雑魚を的確に掃討して深部へと進む。"
  act3_climax:
    turn: "順調に見えた進撃だが、最奥の扉を開けた瞬間、空気が変わる。"
    cliffhanger: "汚職エリートのボスが立ちはだかり、圧倒的なプレッシャーを放つ。"

scenes:
  - scene_01: "アジト突入と雑魚戦"
  - scene_02: "最奥でのボスとの対峙"

validation_hook:
  is_linked_to_arc: true
  has_clear_stimulus: true
```

## 第12話（Chapter 12）
```yaml
chapter_id: "CH_12"
arc_linkage: "第1アーク / 転（ボス戦開始）"

chapter_stimulus:
  peak_variable: "危機" # 正規手段の完全な敗北

chapter_acts:
  act1_intro:
    hook: "ボスとの交戦開始。マーレンが果敢に切り込む。"
  act2_conflict:
    build_up: "彼女の正規の剣術（マニュアルに則った攻撃）が、ボスのシステム加護の前に傷一つつけられない。"
  act3_climax:
    turn: "マニュアルの完全な限界を悟ったマーレンが、ついに大きな決断を下す。"
    cliffhanger: "彼女が自身の「縛り」を解き、封印していた本来の戦い方（巨大な武器）を解き放つ。"

scenes:
  - scene_01: "ボス戦（マニュアル剣術）"
  - scene_02: "マニュアルの限界と封印解除の決意"

validation_hook:
  is_linked_to_arc: true
  has_clear_stimulus: true
```

## 第13話（Chapter 13）
```yaml
chapter_id: "CH_13"
arc_linkage: "第1アーク / 転（偽りのカタルシス）"

chapter_stimulus:
  peak_variable: "驚き" # マーレンの真の姿

chapter_acts:
  act1_intro:
    hook: "封印を解かれたマーレンのいびつな全力が牙を剥く。"
  act2_conflict:
    build_up: "システムから逸脱した規格外の狂戦士のような攻撃で、ボスを圧倒していく。"
  act3_climax:
    turn: "現時点での彼女の最強にして最凶の一撃がボスに迫る。"
    cliffhanger: "読者も「これで勝てる」と思うほどの渾身の攻撃が放たれる瞬間で引く。"

scenes:
  - scene_01: "封印解除後の猛攻"
  - scene_02: "渾身の一撃の投下"

validation_hook:
  is_linked_to_arc: true
  has_clear_stimulus: true
```

## 第14話（Chapter 14）
```yaml
chapter_id: "CH_14"
arc_linkage: "第1アーク / 転（真の絶望）"

chapter_stimulus:
  peak_variable: "危機" # 心の完全な折れ

chapter_acts:
  act1_intro:
    hook: "マーレンの最強の一撃がボスに直撃する。"
  act2_conflict:
    build_up: "しかし、ボスの「理不尽な無敵バフ」が発動し、全量のエレメントが完全に弾き返される。"
  act3_climax:
    turn: "個人のどれほどの足掻きもシステムの理不尽には勝てないという絶対的現実。"
    cliffhanger: "武器が砕け、マーレンの心が完全に折れ、死を待つだけの状態になる。"

scenes:
  - scene_01: "無敵バフによる攻撃の無効化"
  - scene_02: "マーレンの完全なる敗北と絶望"

validation_hook:
  is_linked_to_arc: true
  has_clear_stimulus: true
```

## 第15話（Chapter 15）
```yaml
chapter_id: "CH_15"
arc_linkage: "第1アーク / 結（クライマックスの入り口）"

chapter_stimulus:
  peak_variable: "探求" # 逆転の予兆

chapter_acts:
  act1_intro:
    hook: "ボスのトドメの一撃がマーレンに振り下ろされる。"
  act2_conflict:
    build_up: "死を覚悟したマーレンの前に、影が割り込む。ノルクが「ここで死なれるとギルド評価が下がる」と面倒くさそうに立ち塞がる。"
  act3_climax:
    turn: "極めて低いテンションでの介入。"
    cliffhanger: "無敵のボスに対し、手ぶらのノルクがどう立ち向かうのかという期待で引く。"

scenes:
  - scene_01: "迫る死とノルクの介入"
  - scene_02: "ボスとノルクの対峙"

validation_hook:
  is_linked_to_arc: true
  has_clear_stimulus: true
```

## 第16話（Chapter 16）
```yaml
chapter_id: "CH_16"
arc_linkage: "第1アーク / 結（クライマックス前編）"

chapter_stimulus:
  peak_variable: "驚き" # 神のシステムのハッキング

chapter_acts:
  act1_intro:
    hook: "余裕を見せるボスに対し、ノルクがAI精霊セリファを起動する。"
  act2_conflict:
    build_up: "ボスの周囲の空間（システム）に論理エラーが走り始め、絶対的だったバフが強制的に剥奪されていく。"
  act3_climax:
    turn: "神の加護と信じて疑わなかった無敵の盾が、ただの演算処理によって無効化される。"
    cliffhanger: "力を失ったボスが初めて恐怖に顔を歪める瞬間で引く。"

scenes:
  - scene_01: "セリファによる演算開始"
  - scene_02: "システムバフの強制剥奪"

validation_hook:
  is_linked_to_arc: true
  has_clear_stimulus: true
```

## 第17話（Chapter 17）
```yaml
chapter_id: "CH_17"
arc_linkage: "第1アーク / 結（クライマックス後編）"

chapter_stimulus:
  peak_variable: "報酬" # 理不尽への圧倒的蹂躙

chapter_acts:
  act1_intro:
    hook: "丸裸になったボスへの反撃。"
  act2_conflict:
    build_up: "ノルクが頭痛の代償を堪えながら、最適化された超火力を「雑に」放ち、ボスを粉砕・蹂躙する。"
  act3_climax:
    turn: "圧倒的な力による決着。さらにボスの不正蓄財（レアアイテムや裏金）の隠し金庫が吹き飛び、ノルクがちゃっかりそれを回収する。【有形報酬4: ボスの遺産】"
    cliffhanger: "その光景を見たマーレンの感情が、絶望から「救世主への狂信（執着）」へと完全に切り替わる。【無形報酬4: マーレンの心酔】"

scenes:
  - scene_01: "ノルクの最適化された超火力"
  - scene_02: "ボスの排除と莫大な報酬の獲得"

validation_hook:
  is_linked_to_arc: true
  has_clear_stimulus: true
```

## 第18話（Chapter 18）
```yaml
chapter_id: "CH_18"
arc_linkage: "第1アーク / エピローグ前編"

chapter_stimulus:
  peak_variable: "報酬" # 優越感の獲得とインフラ完成

chapter_acts:
  act1_intro:
    hook: "戦闘後の事後処理。ギルドは事件をボスの自滅として処理する。"
  act2_conflict:
    build_up: "真実が隠蔽される中、スィグナがボスの利権を乗っ取り裏社会を掌握。ノルクに「快適な不労所得のインフラ」という最大の報酬をもたらす。【有形報酬5: 平穏な生活インフラ】"
  act3_climax:
    turn: "一方、マーレンの態度はかつての嫌悪から完全な崇拝へと激変している。"
    cliffhanger: "彼女の重すぎる執着の目がノルクに向けられている描写で引く。"

scenes:
  - scene_01: "ギルドによる隠蔽と事後処理"
  - scene_02: "スィグナの利権掌握と、マーレンの態度の変化"

validation_hook:
  is_linked_to_arc: true
  has_clear_stimulus: true
```

## 第19話（Chapter 19）
```yaml
chapter_id: "CH_19"
arc_linkage: "第1アーク / エピローグ後編"

chapter_stimulus:
  peak_variable: "共感" # ノルクの不憫さ

chapter_acts:
  act1_intro:
    hook: "事件後、豊富な資金と環境で元の適当な平穏を満喫しようとするノルク。"
  act2_conflict:
    build_up: "しかし、マーレンが「私の救世主」として勝手に付き纏い始め、さらにはスィグナも神輿である彼を逃がさない。"
  act3_climax:
    turn: "多段的な有形無形の報酬を得た結果、皮肉にも一番厄介な人間関係の中心に据えられてしまう。"
    cliffhanger: "望んでいた平穏が完全に遠ざかり、ノルクが頭を抱えて第1アークが終了する。"

scenes:
  - scene_01: "マーレンの付き纏いとスィグナの暗躍"
  - scene_02: "ノルクの苦悩とアークの締めくくり"

validation_hook:
  is_linked_to_arc: true
  has_clear_stimulus: true
```
