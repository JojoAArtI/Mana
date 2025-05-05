import requests
import tkinter as tk
from tkinter import messagebox

def get_quote():
    try:
        res = requests.get("https://api.quotable.io/random", timeout=5)
        if res.status_code == 200:
            data = res.json()
            quote.config(text=f'"{data["content"]}"\n\n- {data["author"]}')
        else:
            quote.config(text="Couldn't fetch quote. Try again.")
    except:
        messagebox.showerror("Error", "Failed to connect to quote server.")

app = tk.Tk()
app.title("Random Quote Generator")
app.geometry("500x300")
app.resizable(False, False)
app.configure(bg="#f0f0f0")

quote = tk.Label(app, text="", wraplength=450, justify="center", font=("Helvetica", 12), bg="#f0f0f0", padx=20, pady=20)
quote.pack(expand=True)

btn = tk.Button(app, text="Get Quote", command=get_quote, font=("Helvetica", 12), bg="#4CAF50", fg="white", padx=10, pady=5)
btn.pack(pady=10)

get_quote()

app.mainloop()
