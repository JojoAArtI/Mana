import requests
import tkinter as tk
from tkinter import messagebox

def get_quote():
    try:
        res = requests.get("https://zenquotes.io/api/random", timeout=10)
        if res.status_code == 200:
            data = res.json()[0]
            quote_label.config(text=f'"{data["q"]}"\n\n– {data["a"]}')
        else:
            quote_label.config(text="Couldn't fetch quote. Try again.")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")



app = tk.Tk()
app.title("Quote Generator")
app.geometry("600x400")
app.configure(bg="#ffffff")
app.resizable(False, False)

frame = tk.Frame(app, bg="#ffffff", padx=40, pady=40)
frame.pack(expand=True, fill="both")

quote_label = tk.Label(
    frame,
    text="Click the button to get a quote!",
    wraplength=500,
    justify="center",
    font=("Segoe UI", 14),
    bg="#ffffff",
    fg="#333333",
    padx=20,
    pady=20
)
quote_label.pack(expand=True)

btn = tk.Button(
    app,
    text="Get Quote",
    command=get_quote,
    font=("Segoe UI", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    activebackground="#45A049",
    activeforeground="white",
    padx=20,
    pady=10,
    relief="flat",
    bd=0
)
btn.pack(pady=20)

get_quote()
app.mainloop()
