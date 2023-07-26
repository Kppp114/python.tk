import tkinter as tk
root = tk.Tk()
root.title("Number Buttons")

button_colors = ["red", "green", "blue", "orange", "purple"]

for i in range(1, 6):
    button = tk.Button(root, text=f"Button {i}",bg=button_colors[i-1])
    button.pack(pady=5)

root.mainloop()