#module writter_res
import os.path
from config_reader import config_reader
from psutil_reader import system_data_reader
import json

class conf_analyze():
    def analyze(self, data):
        ins=config_reader()
        if ins.format=="txt":
           wr=writter(data)
           wr.write_data_txt()
        else:
           wr=writter(data)
           wr.write_data_json()
class writter():
    def __init__(self,data):
        self.data=data
    def write_data_txt(self):
        if os.path.isfile('/home/centos/Documents/lesson3/result.txt'):
            with open('result.txt', 'a') as fp:
                fp.write('\n'+ str(self.data))        
        else:
            with open('result.txt', 'w') as fp:
                fp.write(self.data)
    def write_data_json(self):
        data=system_data_reader()
        with open('result.json', 'w') as fp:
            json.dump(self.data,fp,indent=3)       
                
    
