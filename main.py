
import sys
import os


if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')


import QR
import threading, time, datetime
import mqtt
import ui
from getmac import get_mac_address
import power, config

LED_colour = "ORANGE"

config.relay_pin.value = True
config.deviceId = get_mac_address()
QR.generate_qr(f"{config.dashboard_url}/?deviceID={config.deviceId}")

def format_timedelta(delta):
    hours, remainder = divmod(delta, 3600)
    minutes, seconds = divmod(remainder, 60)
    return "{:02d}:{:02d}:{:02d}".format(int(hours), int(minutes), int(seconds))


def task_thread():
    global LED_colour
    while True:
        print("Device Started....")
        ui.setup_screen("Please Wait.. Starting")
        time.sleep(5)
        
        #check for sensor---
        
        #--------------------
        
        #wait for internet---------------
        ui.setup_screen("Connecting to Internet..")
        time.sleep(2)
        while not mqtt.check_internet():
            time.sleep(2)
        ui.setup_screen("Internet Connected !")
          
        #Connect to server---------------
        ui.setup_screen("Connecting to Server...")
        time.sleep(2)
        mqtt_client = mqtt.connect_mqtt()
        mqtt_client.on_disconnect = mqtt.on_disconnect
        mqtt.subscribe(mqtt_client)
        mqtt_client.loop_start()
        while not mqtt.connection_flag:
            pass
        ui.setup_screen("Connected to Server !")
        
        prev_connect_flag = False
        config.prev_idle_time = time.time()
    
        # print("showing qr screen")
        # ui.qr_screen("Scan, Pay, Use")
        
        while(1):
            connect_flag = mqtt.connection_flag

            if(connect_flag==True):
            
                if(mqtt.command=="start"):
                    print("started")
                    power.get_data()
                    if(power.current < config.cutoff_current):
                        LED_colour = "ORANGE"
                        print("elapse start : ", config.elapse_start_time)
                        print("prev_idle_time : ", config.prev_idle_time)
                        print("time.time : ", time.time())
                        print("datetime.datetime : ", datetime.datetime.now())
                        print("time.time diff : ", time.time()-config.prev_idle_time)
                        if((time.time()-config.prev_idle_time) > config.idle_time_in_sec):
                            mqtt.command = "stop"
                            ui.setup_screen(f"Charger Idle for\n{config.idle_time_in_sec} Seconds")
                            config.relay_pin.value = True
                            # config.red_LED.value = False
                            # config.green_LED.value = True
                            # config.orange_LED.value = False
                            time.sleep(2)
                            ui.qr_screen("Scan, Pay, Use")
                            continue
                            
                    else:
                        LED_colour = "GREEN"
                        config.prev_idle_time = time.time()

                    elapsed_time =  time.time() - config.elapse_start_time
                    ui.usage_screen(LED_colour, format_timedelta(elapsed_time), 
                                    str(round(power.voltage, 2))+" V",
                                    str(round(power.current, 2))+" A",
                                    str(round(power.voltage * power.current, 2))+" W", 
                                    str(round(power.units, 2))+" KWh")

                    if((time.time()-config.prev_upload_time) > config.upload_interval):
                        data = f'{{"deviceID": "{config.deviceId}", "Power": {power.units}}}'
                        print(data)
                        mqtt.publish(mqtt_client, data)
                        config.prev_upload_time = time.time()
                
                elif(prev_connect_flag==False or mqtt.command=="stop"):
                    ui.qr_screen("Scan, Pay, Use")

            elif(connect_flag==False):
                ui.setup_screen("Connecting to Server...")

            prev_connect_flag = connect_flag

        mqtt_client.loop_stop()
    
 
def tkinter_thread():
    # Function to exit full screen mode on pressing Escape
    def exit_fullscreen(event):
        ui.root.attributes("-fullscreen", False)
        
    ui.root.bind("<Escape>", exit_fullscreen)
    
    #setup_screen("Please Wait.. Loading")
    #ui.qr_screen("Scan, Pay, Use")
    ui.root.mainloop()

if __name__ == "__main__":
    task_thread = threading.Thread(target=task_thread)
    task_thread.daemon = True  # Set daemon to True to allow main thread to exit even if tkinter_thread is running
    task_thread.start()
    
    tkinter_thread()