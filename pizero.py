
import tkinter as tk
import random

import serial
import struct
import threading
import math
import queue

offsetVoltage = 1650
sensitivity = 39.4
VoltageScale = 72.0/3.3
VoltageGain = 100

# Define the serial port and baud rate
serial_port = '/dev/ttyAMA0'  # Replace with the actual device name (e.g., '/dev/ttyS0')
baud_rate = 115200

# Create queues for storing data and output
data_list = [0,0,0,0,0,0,0,0,0,0]
output_list = [0,0,0,0,0,0,0,0,0,0]

# Function to update the data
def update_tkinter_window():
    # Update the labels with new data and color
    for i in range(3):
        phase_current_labels[i].config(
            text=f"Phase {i + 1} Current:",
            fg="black",
        )
        phase_current_values[i].config(
            text=f"{output_list[2+i]:.2f} A",
            fg="green",
        )
        phase_voltage_labels[i].config(
            text=f"Phase {i + 1} Voltage:",
            fg="black",
        )
        phase_voltage_values[i].config(
            text=f"{output_list[5+i]:.2f} V",
            fg="red",
        )
    
    dc_current_label.config(
        text="DC Current:",
        fg="black",
    )
    dc_current_value.config(
        text=f"{output_list[0]:.2f} A",
        fg="green",
    )
    dc_voltage_label.config(
        text="DC Voltage:",
        fg="black",
    )
    dc_voltage_value.config(
        text=f"{output_list[1]:.2f} V",
        fg="red",
    )
    torque_signal_label.config(
        text="Torque Signal:",
        fg="black",
    )
    torque_signal_value.config(
        text=f"{output_list[8]:.2f}",
        fg="blue",
    )
    frequency_label.config(
        text="Frequency:",
        fg="black",
    )
    frequency_value.config(
        text=f"{output_list[9]:.2f} Hz",
        fg="blue",
    )
    
    root.after(10, update_tkinter_window)


def tkinter_window():
    global root, phase_current_labels, phase_current_values, phase_voltage_labels, phase_voltage_values, dc_current_label, dc_current_value,dc_voltage_label, dc_voltage_value, torque_signal_label, torque_signal_value, frequency_label, frequency_value
    # Create the main window
    root = tk.Tk()
    root.title("Data Display")

    # Get the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Set the window size to cover the entire screen without a border
    root.geometry(f"{screen_width}x{screen_height}+0+0")

    # Create a custom font for the labels
    custom_font = ('Helvetica', 20, 'bold')

    # Create labels for three phase currents
    phase_current_labels = []
    phase_current_values = []
    for i in range(3):
        label = tk.Label(root, font=custom_font, fg="black")
        label.grid(row=i, column=0, padx=10, pady=10)
        phase_current_labels.append(label)

        value_label = tk.Label(root, font=custom_font, fg="green")
        value_label.grid(row=i, column=1, pady=10)
        phase_current_values.append(value_label)

    # Create labels for three phase voltages
    phase_voltage_labels = []
    phase_voltage_values = []
    for i in range(3):
        label = tk.Label(root, font=custom_font, fg="black")
        label.grid(row=i, column=2, padx=10, pady=10)
        phase_voltage_labels.append(label)

        value_label = tk.Label(root, font=custom_font, fg="red")
        value_label.grid(row=i, column=3, pady=10)
        phase_voltage_values.append(value_label)

    # Create labels for DC current and voltage
    dc_current_label = tk.Label(root, font=custom_font, fg="black")
    dc_current_label.grid(row=3, column=0, padx=10, pady=10)

    dc_current_value = tk.Label(root, font=custom_font, fg="green")
    dc_current_value.grid(row=3, column=1, pady=10)

    dc_voltage_label = tk.Label(root, font=custom_font, fg="black")
    dc_voltage_label.grid(row=3, column=2, padx=10, pady=10)

    dc_voltage_value = tk.Label(root, font=custom_font, fg="red")
    dc_voltage_value.grid(row=3, column=3, pady=10)

    # Create labels for torque signal and frequency
    torque_signal_label = tk.Label(root, font=custom_font, fg="black")
    torque_signal_label.grid(row=4, column=0, padx=10, pady=10)

    torque_signal_value = tk.Label(root, font=custom_font, fg="blue")
    torque_signal_value.grid(row=4, column=1, pady=10)

    frequency_label = tk.Label(root, font=custom_font, fg="black")
    frequency_label.grid(row=4, column=2, padx=10, pady=10)

    frequency_value = tk.Label(root, font=custom_font, fg="blue")
    frequency_value.grid(row=4, column=3, pady=10)
    
    # Start the periodic update
    update_tkinter_window()

    root.mainloop()


# Function to calculate RMS
def calculate_rms(channel):
    global output_list
    rms_buffer = []
    current_value = None  # Initialize current value to None
    while True:
        data = data_list[channel]

        if data != current_value:
            current_value = data
            if(channel==2 or channel==3 or channel==4):   #BLDC current channels
                data_mv = (data/4096.0)*3300
                data_i = (data_mv-offsetVoltage)/sensitivity
                rms_buffer.append(data_i)
                
            elif(channel==5 or channel==6 or channel==7):  #BLDC voltage channels
                data_v = ((data/4096.0)*3.3)*VoltageScale
                rms_buffer.append(data_v)

        if len(rms_buffer) >= 128:
            rms = math.sqrt(sum(x ** 2 for x in rms_buffer) / len(rms_buffer))
            output_list[channel] = rms
            print(f"RMS for ADC{channel}: {rms:.2f}")
            rms_buffer.clear()

def DC_calculate(channel):
    current_value = None
    while True:
        data = data_list[channel]
        
        if data != current_value:
            current_value = data
            if(channel == 0):                   #DC current channel
                data_mv = (data/4096.0)*3300
                data_i = (data_mv-offsetVoltage)/sensitivity
                output_list[channel] = data_i
        
            elif(channel == 1):                 #DC voltage channel
                data_v = ((data/4096.0)*3.3)*VoltageScale
                output_list[channel] = data_v

def sensor_data(channel):
    current_value = None
    while True:
        data = data_list[channel].get()
        
        if(channel == 8):                 #Torque channel
            data_v = ((data/4096.0)*3.3)*VoltageScale
            data_mv = data_v/VoltageGain
            output_list[channel] = data_v
        
        elif(channel == 9):               #frequency channel
            output_list[channel] = data
            
            
# Threaded RMS calculation for each ADC channel
threads = []
for channel in range(10):
    if(channel<2):
        t = threading.Thread(target=DC_calculate, args=(channel,))
    elif(channel in range(2,8)):
        t = threading.Thread(target=calculate_rms, args=(channel,))
    elif(channel>7):
        t = threading.Thread(target=sensor_data, args=(channel,))    
    threads.append(t)
    t.start()

# Create a separate thread for the tkinter window
tkinter_thread = threading.Thread(target=tkinter_window)
# Start the tkinter thread
tkinter_thread.start()

# Serial communication and data decoding
ser = serial.Serial(serial_port, baud_rate)
while True:
    data = ser.read(40)  # Read 40 bytes (adjust according to your data size)

    if len(data) == 40:
        # Unpack ADC values (9 x 4 bytes each) and the float value (4 bytes)
        adc_values = struct.unpack('!IIIIIIIII', data[:36])

        # Put ADC values into the respective queues
        for channel, value in enumerate(adc_values):
            data_list[channel] = value

        # Extract and print the float value (if needed)
        float_value = struct.unpack('!f', data[36:])[0]
        data_list[9] = float_value

    else:
        print("Incomplete data received or data size mismatch")
    
    print("hannels :", end=" ")
    for i in range(10):
        # print(adc_values[i], end=" , ")
        try:
            print(data_list[i], end=" , ")
        except queue.Empty:
            print("0", end=" , ")
    print("")

# Close the serial port (unreachable in this example)
ser.close()
