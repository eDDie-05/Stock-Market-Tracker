import tkinter as tk

root = tk.Tk()
root.title("Dark Mode")
root.geometry("500x300")
root.configure(bg="#1e1e1e")

label = tk.Label(
    root,
    text="Dark mode window is running",
    bg="#1e1e1e",
    fg="#ffffff",
    font=("Arial", 14),
)
label.pack(pady=40)

root.mainloop()
