import pyperclip
import time

class ClipboardManager:
    def __init__(self):
        self.history = []
        self.current_clipboard = "main"

    def copy(self, text):
        if self.current_clipboard == "main":
            pyperclip.copy(text)
            self.history.append(text)
        else:
            print("Switch to main clipboard to copy.")

    def paste(self):
        if self.current_clipboard == "main" and len(self.history) > 0:
            return pyperclip.paste()
        elif self.current_clipboard == "secondary":
            return "Secondary clipboard is empty."
        else:
            return "No clipboard selected."

    def switch_to_main(self):
        self.current_clipboard = "main"

    def switch_to_secondary(self):
        self.current_clipboard = "secondary"

    def search_history(self, keyword):
        return [item for item in self.history if keyword.lower() in item.lower()]

    def schedule_copy(self, text, delay):
        time.sleep(delay)
        self.copy(text)

    def schedule_paste(self, delay):
        time.sleep(delay)
        return self.paste()

if __name__ == "__main__":
    manager = ClipboardManager()
    manager.switch_to_main()
    manager.copy("Hello, World!")  # プログラムでのコピー
    print(manager.paste())  # 出力: Hello, World!

    # 手動でテキストをコピー (command+c) を行い、以下で貼り付ける
    time.sleep(10)  # 手動コピーの時間を確保
    manual_copied_text = pyperclip.paste()
    print(manual_copied_text)  # 出力: Manual copy text (手動でコピーしたテキストが表示されます)


