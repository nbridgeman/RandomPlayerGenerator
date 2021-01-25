import tkinter as tk
import random

positions = ["Starting Pitcher", "Relief Pitcher", "First Baseman", "Second Baseman", "Third Baseman", "Shortstop", "Outfielder", "Outfielder", "Outfielder"]
position = random.choice(positions)

window = tk.Tk()
window.title("Random Player Gen")

textFrame = tk.Frame()
buttonFrame = tk.Frame()

randomPosition = tk.Label(
    master = textFrame,
    text = position,
    font = ("Calibri", 24),
    width = 16,
    height = 4
)

def press():
    randomPosition.config(
        text = random.choice(positions)
    )

reRollButton = tk.Button(
    master = buttonFrame,
    text = "Re-Roll",
    font = ("Calibri", 12),
    command = (press),
    width = 16,
)
reRollButton.pack()
randomPosition.pack()

textFrame.pack()
buttonFrame.pack()

window.mainloop()