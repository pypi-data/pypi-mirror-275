import pyperclip
import time

class ClipboardManager:
    def __init__(self):
        self.history = []
        self.current_clipboard = None

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
        self.paste()

if __name__ == "__main__":
    manager = ClipboardManager()
    manager.switch_to_main()
    manager.copy("Hello, World!")  # Correctly calling the copy method with the 'text' parameter
    print(manager.paste())  # Outputs: Hello, World!
    manager.search_history("World")  # Searches the history for the keyword "World"

