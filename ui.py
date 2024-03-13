import tkinter as tk
from PIL import Image, ImageTk
import time

root = tk.Tk()
root.attributes('-fullscreen',True)
#root.geometry("800x480")  # Open the window in full screen mode
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
qr_image.show()
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
    qr_text_label.configure(text=msg)
    if(not qr_frame.winfo_manager()):
        qr_frame.pack()
        qr_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER) 

#-----------------------------------------------------------------------------------------------------#
  
  
#---------------Usage content----------------------------------------------------------------------------#
usage_frame = tk.Frame(root)
qr_frame.configure(bg="black")

# Create labels
time_label = tk.Label(usage_frame, text="Time:")
current_label = tk.Label(usage_frame, text="Current:")
voltage_label = tk.Label(usage_frame, text="Voltage:")
power_label = tk.Label(usage_frame, text="Power:")
units_label = tk.Label(usage_frame, text="Units Consumed:")

# Create value labels
time_value = tk.Label(usage_frame, text="00:00:00")
current_value = tk.Label(usage_frame, text="0.00 A")
voltage_value = tk.Label(usage_frame, text="0.00 V")
power_value = tk.Label(usage_frame, text="0.00 W")
units_value = tk.Label(usage_frame, text="0.00 kWh")

# Pack labels
time_label.grid(row=0, column=0, sticky="e")
time_value.grid(row=0, column=1, sticky="w")
current_label.grid(row=1, column=0, sticky="e")
current_value.grid(row=1, column=1, sticky="w")
voltage_label.grid(row=2, column=0, sticky="e")
voltage_value.grid(row=2, column=1, sticky="w")
power_label.grid(row=3, column=0, sticky="e")
power_value.grid(row=3, column=1, sticky="w")
units_label.grid(row=4, column=0, sticky="e")
units_value.grid(row=4, column=1, sticky="w")

def main():

    # Function to exit full screen mode on pressing Escape
    def exit_fullscreen(event):
        root.attributes("-fullscreen", False)
    root.bind("<Escape>", exit_fullscreen)
    
    # B1 = tk.Button(root, text ="setup", command = lambda: setup_screen("hello"))
    # B2 = tk.Button(root, text ="qr", command = lambda: qr_screen("hello again"))
    # B1.place(x=50,y=50)
    # B2.place(x=50,y=100)
    
    #setup_screen("Please Wait.. Loading")
    qr_screen("Scan, Pay, Use")

    root.mainloop()

if __name__ == "__main__":
    main()
