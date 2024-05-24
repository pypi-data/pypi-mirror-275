from enum import Enum
from PyMCP2221A import PyMCP2221A
from time import sleep

class PCF8547Constants(Enum):
    # Invert all of the values becuase the relay board is actuvatedfor the active low
    Reset = 0xFF
    P0 = 0x01
    P1 = 0x02
    P2 = 0x04
    P3 = 0x08
    P4 = 0x10
    P5 = 0x20
    P6 = 0x40
    P7 = 0x80
    SetAll = 0x00

class PCF8547:
    
    def __init__(self,slaveAddress,mcp) -> None:
        self.mcp2221A = mcp
        self.slaveAddress = slaveAddress
        self.reset()

    def setport(self,port):
        # print(port,'..........',self.slaveAddress)
        port = (~port &  self.mcp2221A.I2C_Read(self.slaveAddress, 1)[0])
        self.mcp2221A.I2C_Write(self.slaveAddress,[port])
      
    def resetport(self,port):  
        port = (port |  self.mcp2221A.I2C_Read(self.slaveAddress, 1)[0])
        print(port)
        self.mcp2221A.I2C_Write(self.slaveAddress,[port])
    
    def enable_P0(self,port=0x01):
        self.setport(port)
    def disable_P0(self,port=0x02):
        self.resetport(port)
    def enable_P1(self,port=0x02):
        self.setport(port)
    def disable_P1(self,port=0x02):
        self.resetport(port)
    def enable_P2(self,port=0x04):
        self.setport(port)
    def disable_P2(self,port=0x04):
        self.resetport(port)
    def enable_P3(self,port=0x08):
        self.setport(port)
    def disable_P3(self,port=0x08):
        self.resetport(port)
    def enable_P4(self,port=0x10):
        self.setport(port)
    def disable_P4(self,port=0x10):
        self.resetport(port)
    def enable_P5(self,port=0x20):
        self.setport(port)
    def disable_P5(self,port=0x20):
        self.resetport(port)
    def enable_P6(self,port=0x40):
        self.setport(port)
    def disable_P6(self,port=0x40):
        self.resetport(port)
    def enable_P7(self,port=0x80):
        self.setport(port)
    def disable_P7(self,port=0x80):
        self.resetport(port)

    def reset(self):
        port = 0xFF
        self.mcp2221A.I2C_Write(self.slaveAddress,[port])

if __name__ == '__main__':

    pcf8547 = PCF8547()

    pcf8547.setport(PCF8547Constants.P0.value)
    sleep(0.5)
    pcf8547.setport(PCF8547Constants.P1.value)
    sleep(0.5)
    pcf8547.resetport(PCF8547Constants.P0.value)