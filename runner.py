import tkinter as tk
from tkinter import scrolledtext
import subprocess
import threading

class BotRunner:
    def __init__(self, root):
        self.root = root
        self.root.title("Bot Runner")

        self.log_label = tk.Label(root, text="Logs:")
        self.log_label.pack()

        self.log_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20)
        self.log_text.pack()

        self.run_button = tk.Button(root, text="Run bot!", command=self.run_custom_py_file)
        self.run_button.pack()

    def run_custom_py_file(self):
        self.log_text.delete(1.0, tk.END)  # Clear previous logs
        self.log_text.insert(tk.END, "Bot started...\n")

        self.run_button.config(state=tk.DISABLED)  # Disable the run button during execution

        self.execute_custom_file()

    def execute_custom_file(self):
        def execute_and_update_logs():
            try:
                result = subprocess.run(["python", "bot.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                stdout = result.stdout
                stderr = result.stderr

                self.log_text.insert(tk.END, stdout)
                self.log_text.insert(tk.END, stderr)

                self.run_button.config(state=tk.NORMAL)  # Enable the run button after execution
            except Exception as e:
                self.log_text.insert(tk.END, f"Error: {e}\n")

        threading.Thread(target=execute_and_update_logs).start()

if __name__ == "__main__":
    root = tk.Tk()
    app = BotRunner(root)
    root.mainloop()