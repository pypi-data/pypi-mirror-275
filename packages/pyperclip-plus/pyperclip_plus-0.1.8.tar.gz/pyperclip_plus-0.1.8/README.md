以下は、`pyperclip_plus` パッケージの README を日本語で書いたものです：

---

# pyperclip_plus

`pyperclip_plus` は、クリップボードの管理をより簡単かつ効率的に行うための強力なツールです。このパッケージは、複数のクリップボードの管理やクリップボード履歴の検索など、基本的な機能を拡張します。

## 機能

- メインクリップボードとセカンダリクリップボードの切り替え
- クリップボードにコピーした内容の履歴を保持
- キーワードに基づく履歴検索
- コピーと貼り付けのスケジュール設定

## インストール

`pyperclip_plus` をインストールするには、以下のコマンドを使用します：

```bash
pip install pyperclip_plus
```

## 使用方法

以下は、`pyperclip_plus` の基本的な使用例です：

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

# 履歴から特定のキーワードを含むアイテムを検索
history_items = manager.search_history("World")
print("履歴検索結果:")
for item in history_items:
    print(item)
```

## ライセンス

このプロジェクトは [MIT License](https://opensource.org/licenses/MIT) の下でライセンスされています。

## 作者

- 名前: Your Name
- メール: your.email@example.com
