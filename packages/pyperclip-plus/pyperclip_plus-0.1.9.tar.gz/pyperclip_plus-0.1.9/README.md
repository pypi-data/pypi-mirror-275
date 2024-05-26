# pyperclip_plus

`pyperclip_plus` は、クリップボードの管理をより簡単かつ効率的に行うための強力なツールです。このパッケージは、複数のクリップボードの管理やクリップボード履歴の検索など、基本的な機能を拡張します。

## 機能

- メインクリップボードとセカンダリクリップボードの切り替え
- クリップボードにコピーした内容の履歴を保持
- キーワードに基づく履歴検索
- コピーと貼り付けのスケジュール設定
- 手動コピー（command+c）内容の取得

## インストール

`pyperclip_plus` をインストールするには、以下のコマンドを使用します：

```bash
pip install pyperclip_plus
```

## 使用方法

以下は、`pyperclip_plus` の基本的な使用例です：

### 基本的なクリップボード操作

```python
import pyperclip_plus as pp

# クリップボードマネージャのインスタンスを作成
manager = pp.ClipboardManager()

# メインクリップボードに切り替え
manager.switch_to_main()

# テキストをコピー
manager.copy("Hello, World!")

# クリップボードからテキストを貼り付け
print(manager.paste())  # 出力: Hello, World!
```

### クリップボード履歴の検索

```python
import pyperclip_plus as pp

# クリップボードマネージャのインスタンスを作成
manager = pp.ClipboardManager()

# メインクリップボードに切り替え
manager.switch_to_main()

# 複数のテキストをコピー
manager.copy("Python is great")
manager.copy("Machine Learning is fascinating")
manager.copy("Hello, World!")

# 履歴から特定のキーワードを含むアイテムを検索
history_items = manager.search_history("Python")
print("履歴検索結果:")
for item in history_items:
    print(item)
```

### クリップボード操作のスケジュール設定

```python
import pyperclip_plus as pp
import time

# クリップボードマネージャのインスタンスを作成
manager = pp.ClipboardManager()

# メインクリップボードに切り替え
manager.switch_to_main()

# 5秒後にテキストをコピー
manager.schedule_copy("Scheduled copy", 5)

# 10秒後にクリップボードからテキストを貼り付け
time.sleep(10)
print(manager.paste())  # 出力: Scheduled copy
```

### セカンダリクリップボードの使用

```python
import pyperclip_plus as pp

# クリップボードマネージャのインスタンスを作成
manager = pp.ClipboardManager()

# セカンダリクリップボードに切り替え
manager.switch_to_secondary()

# セカンダリクリップボードにコピーを試みる
manager.copy("This will not be copied")

# メインクリップボードに戻してコピー
manager.switch_to_main()
manager.copy("This will be copied")

# メインクリップボードから貼り付け
print(manager.paste())  # 出力: This will be copied
```

### 手動コピー内容の取得

```python
import pyperclip
import pyperclip_plus as pp
import time

# クリップボードマネージャのインスタンスを作成
manager = pp.ClipboardManager()

# メインクリップボードに切り替え
manager.switch_to_main()
manager.copy("Hello, World!")  # プログラムでのコピー
print(manager.paste())  # 出力: Hello, World!

# 手動でテキストをコピー (command+c) を行い、以下で貼り付ける
time.sleep(10)  # 手動コピーの時間を確保
manual_copied_text = pyperclip.paste()
print(manual_copied_text)  # 出力: Manual copy text (手動でコピーしたテキストが表示されます)
```


## ライセンス

このプロジェクトは [MIT License](https://opensource.org/licenses/MIT) の下でライセンスされています。


## プロジェクトURL

[GitHub リポジトリ](https://github.com/AkitaShohei/ds_packege.git)

