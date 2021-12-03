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
    with smbus.SMBus(1) as I2Cbus :
        slaveAddress = I2C_SLAVE_ADDRESS
        servoSelect = input("Which Servo (1-2) :")
        
        ByteToSend = servoSelect
        I2Cbus.write_i2c_block_data(slaveAddress, 0x00, ByteToSend)
        time.sleep(0.5)
        while True:
            try :
                data= I2Cbus.read_i2c_block_data(slaveAddress,0x00,16)
                print("recieve from slave:")
                print(data)
            except:
                print("remote i/o error")
                time.sleep(0.5)
    return 0

if __name__ == '__main__':
    try:
        main(sys.argv)
    except KeyboardInterrupt:
        print("program stopped")
    input()
