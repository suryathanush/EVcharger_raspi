import MODBUS_CRC16
import struct
import serial, time

#============================================================
# Register address
#
#============================================================
EM2M_DEFAULT_SLAVE_ADDRESS = 0x01
FUNCTION_CODE = 0x04

TOTAL_ACTIVE_ENERGY_REG = 0x01
IMPORT_ACTIVE_ENERGY_REG = 0x03
EXPORT_ACTIVE_ENERGY_REG = 0x05
TOTAL_REACTIVE_ENERGY_REG = 0x07
IMPORT_REACTIVE_ENERGY_REG = 0x09
EXPORT_REACTIVE_ENERGY_REG = 0x0B
APPARENT_ENERGY_REG = 0x0D
ACTIVE_POWER_REG = 0x0F
REACTIVE_POWER_REG = 0x11
APPARENT_POWER_REG = 0x12
VOLTAGE_REG = 0x15
CURRENT_REG = 0x17
POWER_FACTOR_REG = 0x19 
FREQUENCY_REG = 0x1B
MAX_DEMAND_ACTIVE_POWER_REG = 0x1D
MAX_DEMAND_REACTIVE_POWER_REG = 0x1F
MAX_DEMAND_APPARENT_POWER_REG = 0x21

TOTAL_KWH_REG = 0X95
IMPORT_KWH_REG = 0X96
EXPORT_KWH_REG = 0x97
TOTAL_KVARH_REG = 0X98
IMPORT_KVARH_REG = 0X99
EXPORT_KVARH_REG = 0X9A
KVAH_REG = 0X9B

#============================================================
#
#
#============================================================
COM_PORT_NAME = '/dev/ttyUSB0'
#============================================================
#
#
#============================================================

voltage = 0.0
current = 0.0
power = 0.0
units = 0.0

#============================================================
def readparam(REG):
    ser = serial.Serial(COM_PORT_NAME, 9600, 8, 'N', 1, timeout=3, writeTimeout=4, interCharTimeout=3)
    if(True == ser.is_open):
        try:
            #print("Serial port Opened Successfully")
            str = [EM2M_DEFAULT_SLAVE_ADDRESS, 4, 0, REG, 0, 2]
            len_str = len(str)
            crc_list = MODBUS_CRC16.calcCRC(str, len_str)
            str.append(crc_list[0])
            str.append(crc_list[1])
            ser.write(str)
            response = ser.read(9)
            voltageByte = response[3:7]
            voltageFloatTuple = struct.unpack('>f', voltageByte)   #big endian
            voltage = voltageFloatTuple[0]
            ser.close()
            print("value :", voltage)      
            return "SUCCESS", voltage
        except Exception as e:
            print(e)
            return "FAILURE", 0.00
    else:
        print("Serial port failed to open")
        return "FAILURE", 0.00
#============================================================

def get_data():
    global voltage, current, power, units
    status, voltage = readparam(VOLTAGE_REG)
    time.sleep(0.2)
    status, current = readparam(CURRENT_REG)
    time.sleep(0.2)
    status, power = readparam(APPARENT_POWER_REG)
    time.sleep(0.2)
    status, units = readparam(TOTAL_KWH_REG)
