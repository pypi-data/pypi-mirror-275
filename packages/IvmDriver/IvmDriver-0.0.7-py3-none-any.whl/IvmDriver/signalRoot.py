import json 
from ast import literal_eval
from typing import List 
import json 
import warnings
import sys
# from logs.logger import log 
from logger import log 

class SignalRoot:
    
    def __init__(self, ) -> None:
        pass
        
    
    def signalPathMapping(self,signalConfig_path='driver\signals\SignalConfig.json', signalMapfile_path='driver/signals/signalroot_matrix.json'):
        with open(signalConfig_path, 'r') as file :
            data = json.load(file)
            log.info(f'SignalMapping configurations loaded from {signalMapfile_path} file')
        signalMatrix = {}
        base_addr = 0x20
        for matrix, signalMap in data.items() :
            signalroot = {}
            for row, Signal in enumerate(signalMap.get('rowsHigh')):
                row = row + 1
                for col, instrument in enumerate(signalMap.get('colsHigh')) :
                    col = col + 1
                    if  1 <= row  < 3:
                        device_addr = base_addr + int(matrix) * 4
                    elif 3 <= row  < 5:
                        device_addr = base_addr + int(matrix) * 4 + 1
                    elif 5 <= row  < 7:
                        device_addr = base_addr + int(matrix) * 4 + 2
                    elif 7 <= row  < 9:
                        device_addr = base_addr + int(matrix) * 4 + 3
                    signalroot.update(
                        {
                            str({"Source":{"High":Signal,"Low":signalMap.get('rowsLow')[row-1] }, "Destination" : {"High":instrument,"Low":signalMap.get('colsLow')[col-1] }}) : {
                            "deviceAddr" : hex(device_addr),
                            "relay":{
                                "row" : row ,
                                "col":col                    
                                }
                            }
                        }
                    )
            signalMatrix.update({
                matrix : signalroot
            })
        with open(signalMapfile_path,'w') as file :
            json.dump(signalMatrix ,file,)
            log.info(f'Signal Mapping Dumped into {signalMapfile_path}')

    def signalConfig(self,Source={'High': 'BCLK', 'Low': 'SDI'}, Destination={'High': 'FSYN AP', 'Low': 'GND'}, Signalroot_file='driver/signals/signalroot_matrix.json'): 
        signal_root ={}
        with open(Signalroot_file,'r') as file :
            signals = json.load(file,)
        for  matrix, path_data in signals.items():
            for signal, data in path_data.items():
                signal = literal_eval(signal)
                if signal.get('Source').get('High') == Source.get('High') and \
                    signal.get('Source').get('Low') == Source.get('Low') :
                    if signal.get('Destination').get('High') == Destination.get('High') and \
                        signal.get('Destination').get('Low') == Destination.get('Low') :
                            signal_root = data
                            
                #     else:
                #         log.error(f'Signal Destination not matched {Destination}')
                # #         warnings.warn('Destination Path is Wrong .......!')
                # else:
                #         log.error(f'Signal Source not matched {Destination}')
                #     warnings.warn('Source Path is Wrong .......!')
                
        # return data {'deviceAddr': '0x24', 'relay': {'row': 1, 'col': 1}}
        if not signal_root:
            log.error(f'Signal Path did not match Source: {Source} Destination: {Destination}')
            
        return signal_root
    
if __name__ == '__main__':
    signalRoot = SignalRoot()
    signalRoot.signalPathMapping()
    print(signalRoot.signalConfig(Source={'High': 'BCLK', 'Low': 'SDI'}, Destination={'High': 'FSYN AP', 'Low': 'GND'}, Signalroot_file='driver/signals/signalroot_matrix.json'))