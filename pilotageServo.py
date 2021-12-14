import sys
import smbus2 as smbus
import time

I2C_SLAVE_ADDRESS = 11


def ConvertStringToByte(src):
    converted=[]
    for b in src:
        converted.append(ord(b))
    return converted

def main(args):
    I2Cbus = smbus.SMBus(1)
    slaveAddress = I2C_SLAVE_ADDRESS
    ByteToSend = ConvertStringToByte("servo1")
    I2Cbus.write_i2c_block_data(slaveAddress, 0x00, ByteToSend)
    time.sleep(0.5)
       
    return 0

if __name__ == '__main__':
    try:
        main(sys.argv)
    except KeyboardInterrupt:
        print("program stopped")
    
