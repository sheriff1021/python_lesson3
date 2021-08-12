import psutil
import datetime
import time

class system_data_reader():
    def __init__(self):
        self.time={'time': self.get_time()}
        self.cpu={'CPU':self.cpu_overload()}
        self.memory=self.memory_total()
        self.disk=self.space()
        self.net=self.net()
        self.result=[ self.time, self.cpu, {'memory':self.memory}, {'disk': self.disk},{'net': self.net} ]
    def cpu_overload(self):
        cpu_overload=str(psutil.cpu_percent(interval=1))
        return cpu_overload
    def memory_total(self):
        mem=psutil.virtual_memory()
        memory={'total':mem.total, 'available': mem.available, 'percent': mem.percent, 'used': mem.used, 'free':mem.free}
        return memory
    def space(self):
        varka=psutil.disk_usage('/')
        disk={'total':varka.total, 'used':varka.used, 'free':varka.free, 'percent':varka.percent}
        return disk
    def net(self):
        netk=psutil.net_io_counters()
        net={'bytes_sent':netk.bytes_sent, 'bytes_recv': netk.bytes_recv, 'packets_sent': netk.packets_sent}
        return net
    def get_time(self):
        ts=time.time()
        st=datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        return str(st)