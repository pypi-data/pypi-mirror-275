from PyMCP2221A import PyMCP2221A
from time import sleep

class MCP2221:

    def __init__(self) :
        # self.mcp = PyMCP2221A.PyMCP2221A()
        # self.mcp.Reset()
        self.mcp2221 = PyMCP2221A.PyMCP2221A()
        self.mcp2221.I2C_Init()
    
    def Reset(self):
        self.mcp2221.Reset()
        sleep(0.1)
        self.mcp2221.I2C_Init()
    def mcpWrite(self,SlaveAddress,data:list):
        # slaveAdddress = data.pop(0)
        # senddata = data
        # senddata = []
        # for i in range(0,len(data)):
        #     senddata.append(data[i])
        # print(senddata)
        self.mcp2221.I2C_Write(SlaveAddress,data)


    def mcpRead(self,SlaveAddress,data:list,Nobytes=1):
        # slaveAddress = data[0]
        self.mcpWrite(SlaveAddress=SlaveAddress,data=data)
        data = self.mcp2221.I2C_Read(SlaveAddress, Nobytes)
        return data

if __name__ == '__main__':

    mcp=MCP2221()
    mcp.mcpWrite(SlaveAddress=0x20,data=[00,0x01])
    print(mcp.mcpRead(SlaveAddress=0x20,data=[00],Nobytes=1))