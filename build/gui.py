
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

import tkinter as tk

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/home/surya/evcharger2.0/build/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# window = Tk()

# window.geometry("800x480")
# window.configure(bg = "#000000")

root = tk.Tk()
root.geometry("800x480")  # Open the window in full screen mode
root.configure(bg="black")

window = tk.Frame(root)
window.configure(bg="black")
window.pack(fill="both", expand="true")


canvas = Canvas(
    window,
    bg = "#000000",
    height = 480,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    505.0,
    126.0,
    image=image_image_1
)

canvas.create_text(
    185.0,
    113.0,
    anchor="nw",
    text="Time Consumed :",
    fill="#FFFFFF",
    font=("Inter Bold", 24 * -1)
)

canvas.create_text(
    145.0,
    43.0,
    anchor="nw",
    text="Device :",
    fill="#FFFFFF",
    font=("Inter", 24 * -1)
)

device_id_label = canvas.create_text(
    245.0,
    43.0,
    anchor="nw",
    text="d8:3a:dd:27:e7:e4",
    fill="#FFFFFF",
    font=("Inter Bold", 24 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    505.0,
    192.0,
    image=image_image_2
)

canvas.create_text(
    195.0,
    180.0,
    anchor="nw",
    text="Socket Voltage :",
    fill="#FFFFFF",
    font=("Inter Bold", 24 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    505.0,
    258.0,
    image=image_image_3
)

canvas.create_text(
    195.0,
    246.0,
    anchor="nw",
    text="Current usage :",
    fill="#FFFFFF",
    font=("Inter Bold", 24 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    505.0,
    324.0,
    image=image_image_4
)

canvas.create_text(
    195.0,
    312.0,
    anchor="nw",
    text="Power Usage :",
    fill="#FFFFFF",
    font=("Inter Bold", 24 * -1)
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    505.0,
    390.0,
    image=image_image_5
)

canvas.create_text(
    195.0,
    378.0,
    anchor="nw",
    text="Units Used :",
    fill="#FFFFFF",
    font=("Inter Bold", 24 * -1)
)

time_elapsed_label = canvas.create_text(
    437.0,
    113.0,
    anchor="nw",
    text="12:00:00",
    fill="#000000",
    font=("Inter Bold", 24 * -1)
)

voltage_label = canvas.create_text(
    437.0,
    180.0,
    anchor="nw",
    text="220 V",
    fill="#000000",
    font=("Inter Bold", 24 * -1)
)

current_label = canvas.create_text(
    437.0,
    244.0,
    anchor="nw",
    text="10.5 A",
    fill="#000000",
    font=("Inter Bold", 24 * -1)
)

power_label = canvas.create_text(
    437.0,
    311.0,
    anchor="nw",
    text="2200 W",
    fill="#000000",
    font=("Inter Bold", 24 * -1)
)

units_label = canvas.create_text(
    437.0,
    378.0,
    anchor="nw",
    text="26.4 KWh",
    fill="#000000",
    font=("Inter Bold", 24 * -1)
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    557.0,
    55.0,
    image=image_image_6
)

canvas.create_text(
    579.0,
    41.0,
    anchor="nw",
    text="Active",
    fill="#FFFFFF",
    font=("Inter Bold", 24 * -1)
)

canvas.create_rectangle(
    -1.0,
    86.0,
    800.0006103515625,
    87.0,
    fill="#FFFFFF",
    outline="")
#window.resizable(False, False)
root.mainloop()
