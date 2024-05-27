import pyperclip
import time
from collections import deque
import os

class ClipboardHist:
    def __init__(self, max_size=100):
        self.history = deque(maxlen=max_size)
        self.current_clipboard = ""

    def watch_clipboard(self, interval=1):
        try:
            while True:
                current_content = pyperclip.paste()
                if current_content != self.current_clipboard:
                    self.current_clipboard = current_content
                    self.history.appendleft(current_content)
                    print(f"New entry added to history: {current_content}")
                time.sleep(interval)
        except KeyboardInterrupt:
            print("Clipboard monitoring stopped.")

    def show_history(self):
        print("Clipboard History:")
        for idx, item in enumerate(self.history):
            print(f"{idx + 1}: {item}")

    def get_from_history(self, index):
        try:
            return self.history[index - 1]
        except IndexError:
            print("Invalid index.")
            return None

    def search_history(self, query):
        results = [item for item in self.history if query in item]
        print(f"Search results for '{query}':")
        for result in results:
            print(result)

    def copy_to_clipboard(self, index):
        item = self.get_from_history(index)
        if item:
            pyperclip.copy(item)
            print(f"Copied to clipboard: {item}")

    def clear_history(self):
        self.history.clear()
        print("Clipboard history cleared.")

# Example usage
if __name__ == "__main__":
    clipboard_hist = ClipboardHist(max_size=50)
    
    # Run this in a separate thread or process if you want continuous monitoring
    # clipboard_hist.watch_clipboard()

    # Manual interactions
    clipboard_hist.watch_clipboard()  # This will start monitoring until you interrupt with Ctrl+C
    
    clipboard_hist.show_history()
    clipboard_hist.search_history("example")
    clipboard_hist.copy_to_clipboard(1)
    clipboard_hist.clear_history()
