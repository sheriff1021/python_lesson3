import json
class config_reader():
    def __init__(self):
        with open('cpu.conf', 'r') as fp:
            data = fp.read()

        json_data=json.loads(str(data))
        
        self.format=json_data['format']
        self.time=int(json_data['time'])
