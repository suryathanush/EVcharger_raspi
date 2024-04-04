import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from PIL import Image, ImageTk
import time

from pathlib import Path

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/home/surya/evcharger/assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

root = tk.Tk()
root.attributes('-fullscreen',True)
root.geometry("800x480")  # Open the window in full screen mode
root.configure(bg="black")

#----------------setup frame content -----------------------------------------------------------------#
setup_frame = tk.Frame(root)
setup_frame.configure(bg="black")

# Load and resize the logo
logo_image = Image.open("logo.png")  # Replace "logo.png" with your image file path
target_resolution = (400, 300)  # Desired resolution
logo_image.thumbnail(target_resolution)
logo_photo = ImageTk.PhotoImage(logo_image)

logo_label = tk.Label(setup_frame, image=logo_photo, bg="black")
logo_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
logo_label.pack(pady=30)

# Display text below the logo
text_label = tk.Label(setup_frame, text="Pay and Use", font=("Helvetica", 26, 'bold'), fg="white", bg="black")
#text_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
text_label.pack()

# setup screen
def setup_screen(msg):
    qr_frame.place_forget()
    usage_frame.place_forget()
    text_label.configure(text=msg)
    if(not setup_frame.winfo_manager()):
        setup_frame.pack()
        setup_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    else:
        setup_frame.tkraise()
  
#-------------------------------------------------------------------------------------------------------#

#-----------QR frame Content------------------------------------------------------------------------------#
qr_frame = tk.Frame(root)
qr_frame.configure(bg="black")

    # Load and resize the logo
qr_image = Image.open("qr.png")  # Replace "logo.png" with your image file path
target_resolution = (400, 300)  # Desired resolution
qr_image.thumbnail(target_resolution)
qr_photo = ImageTk.PhotoImage(qr_image)

qr_label = tk.Label(qr_frame, image=qr_photo, bg="black")
qr_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
qr_label.pack(pady=50)

# Display text below the logo
qr_text_label = tk.Label(qr_frame, text="Scan and Pay to Use", font=("Helvetica", 26, 'bold'), fg="white", bg="black")
#qr_text_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
qr_text_label.pack()

def qr_screen(msg):
    setup_frame.place_forget()
    usage_frame.place_forget()
    qr_text_label.configure(text=msg)
    if(not qr_frame.winfo_manager()):
        qr_frame.pack()
        qr_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER) 

#-----------------------------------------------------------------------------------------------------#
  
  
#---------------Usage content----------------------------------------------------------------------------#
usage_frame = tk.Frame(root)

canvas = tk.Canvas(
    usage_frame,
    bg = "#000000",
    height = 480,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("value_box.png"))
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
    file=relative_to_assets("value_box.png"))
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
    file=relative_to_assets("value_box.png"))
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
    file=relative_to_assets("value_box.png"))
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
    file=relative_to_assets("value_box.png"))
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
    text="00.0 KWh",
    fill="#000000",
    font=("Inter Bold", 24 * -1)
)

orange_img = PhotoImage(file=relative_to_assets("orange.png"))
green_img = PhotoImage(file=relative_to_assets("green.png"))
state_img_label = canvas.create_image(
    557.0,
    55.0,
    image=green_img
)

state_label = canvas.create_text(
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

canvas.pack()

def usage_screen(colour,time_elapsed, voltage, current, power, units):
    setup_frame.place_forget()
    qr_frame.place_forget()
    if(colour=="ORANGE"):
        canvas.itemconfig(state_img_label,image=orange_img)
        canvas.itemconfig(state_label, text="INACTIVE")
    elif(colour=="GREEN"):
        canvas.itemconfig(state_img_label,image=green_img)
        canvas.itemconfig(state_label, text="ACTIVE")
    canvas.itemconfig(time_elapsed_label,text=time_elapsed)
    canvas.itemconfig(voltage_label,text=voltage)
    canvas.itemconfig(current_label,text=current)
    canvas.itemconfig(power_label,text=power)
    canvas.itemconfig(units_label,text=units)
    if(not usage_frame.winfo_manager()):
        usage_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER) 


# def main():

#     # Function to exit full screen mode on pressing Escape
#     def exit_fullscreen(event):
#         root.attributes("-fullscreen", False)
#     root.bind("<Escape>", exit_fullscreen)
    
#     # B1 = tk.Button(root, text ="setup", command = lambda: setup_screen("hello"))
#     # B2 = tk.Button(root, text ="qr", command = lambda: qr_screen("hello again"))
#     # B1.place(x=50,y=50)
#     # B2.place(x=50,y=100)
    
#     #setup_screen("Please Wait.. Loading")
#     #qr_screen("Scan, Pay, Use")
#     #usage_screen("ORANGE", "02:34:12", "100 V", "20 A", "33 W", "300 KWH")

#     root.mainloop()

# if __name__ == "__main__":    
#     main()