"""
Author: Vigneswaran S
Last Update: 26.05.2024
License: MIT License

Description:

*NOTE:This module only for linux.*

The RadeonMaster is a Python package built on top of the `radeontop` utility to retrieve detailed information and usage statistics about AMD GPUs. It executes the `radeontop -d` command to generate a log file named 'amd_gpu_log.txt', which contains comprehensive GPU metrics. Additionally, it utilizes the `lm-sensors` package to obtain temperature readings for the GPU.

The gathered data is stored in a dictionary format, providing an accessible and structured way to query GPU information based on the bus ID.

Key Features:
- Executes `radeontop` to log detailed GPU usage statistics.
- Uses `lm-sensors` to monitor GPU temperature.
- Aggregates GPU information into a dictionary for easy access.
- Allows querying of GPU data by bus ID.

Use Cases:
This package is ideal for developers and system administrators who need to monitor and analyze the performance and thermal characteristics of AMD GPUs in their systems.
"""

import os
import sys
import json
import signal
import threading
import subprocess as s
from time import sleep

"""
k2w is a dictionary that have the key and full form for the radeontop output
"""
k2w = { "bus":"bus",
        "gpu":"GPU usage" , 
        "ee" :"Event Engine" , 
        "vgt" :"Vertex Grouper + Tesselator" , 
        "ta" : "Texture Addresser" , 
        "sh" : "Sequencer Instruction Cache" , 
        "sx" : "Shader Interpolator" , 
        "sc" : "scan converter" , 
        "pa" : "Primitive Assembly" , 
        "db" : "depth block" ,
        "cb" : "color block" , 
        "vram" : "VRAM" , 
        "gtt" : "GTT" , 
        "mclk" : "Memory Clock" , 
        "sclk" : "Shader Clock"
        }

"""
sc_ is the script used to log the output of the radeontop in the 'amd_gpu log-.txt' . It should exicuted in thread
"""

scr_ = """
log_file="/tmp/amd_gpu log-.txt"

touch "$log_file"

radeontop -d - -i 1 | while read -r line; do
    # Extract the bus number
    bus=$(echo "$line" | grep -o 'bus: [0-9]\\+')

    # Check if the line already exists in the file
    if grep -qF "$bus" "$log_file"; then
        echo "$line" > "$log_file"
    else
        # Append the line to the output file
        echo "$line" >> "$log_file"
    fi
done
"""
def _exi(_n):

    '''
    _exi used filter float in radeontop output
    
    '''

    return float("".join(filter(lambda x: x.isdigit() or x == ".",_n)))

def _exa(_a):

    '''
    _exa used filter alphabets in radeontop output to get the suffix (Eg : MB , G , GB , KB)
    
    '''

    return "".join(filter(str.isalpha,_a))

def get_available_gpus():
        
        av_g = []
        cpu_bus_p = s.check_output("lspci | grep -i 'host bridge' | awk '{print $1}'",shell=True).decode("utf-8")[:2]
        avg = s.check_output("lspci | grep -i vga",shell=True).decode("utf-8")
        
        for gpu in avg.splitlines():

            g_s = gpu.split()

            print()

            av_g.append({ "Bus address": g_s[0] , "Name" : " ".join(g_s[g_s.index("controller:")+1:]) , "Type" : ("Intergrated gpu" if cpu_bus_p == g_s[0][:2] else "Dedicated gpu")})

        return json.dumps(av_g,indent=2)
        
class GPU():

    def __init__(self):

        self.out = True 
        self.get_avai_gpu()

        ''' Start the thread and wait for 1 second to get radeontop . 
            This will stop being get wrong output'''

        threading.Thread(target=self.strl).start() 
        sleep(1)
    def check_dependencies():
        if not sys.platform.startswith('Linux'):
            raise RuntimeError("This module developed for Linux only!")
        if s.getoutput("command -v radeontop") == '':
            raise RuntimeError("`radeontop` not found!")
        elif s.getoutput("command -v sensors"):
            raise RuntimeError("`lm-sensors` not found!")
    def stop_logging(self):

        self.out = False
        
        pid = s.check_output("pgrep radeontop",shell=True).decode("utf-8")

        os.kill(int(pid),signal.SIGKILL)

    def strl(self):

        os.system(scr_)

    def get_temp(self,BusAdress):

        'this function used to get temparature using lm-sensors'

        output_dict = json.loads(s.getoutput("sensors -j"))

        bus = "".join(filter(str.isdigit,BusAdress))[:4]

        for sensor, data in output_dict.items():
            if bus in sensor:
                for category, values in data.items():
                    if 'temp' in category:
                        temperature_key = next(iter(values))
                        temperature_value = values[temperature_key]
                        return temperature_value

    def get_avai_gpu(self):
        
        self.av_g = {}
        self.cpu_bus_p = s.check_output("lspci | grep -i 'host bridge' | awk '{print $1}'",shell=True).decode("utf-8")[:2]
        self.avg = s.check_output("lspci | grep -i vga",shell=True).decode("utf-8")
        
        for gpu in self.avg.splitlines():

            g_s = gpu.split()

            self.av_g[g_s[0][:2]] = [ g_s[0] , ("Intergrated gpu" if self.cpu_bus_p == g_s[0][:2] else "Dedicated gpu")," ".join(g_s[g_s.index("controller:")+1:])]

    def get_output(self,bus_address=None):

        _ox = {}

        _f = open("/tmp/amd_gpu log-.txt","r")

        for _o in _f.readlines():

            _ot = {}

            _d = str(_o).split()

            for _i,_k in enumerate(k2w):

                if _k == "bus":

                    _kb = (_d[_d.index(_k)+1]).replace(",",'')
                    _ot["bus address"] = self.av_g[_kb][0]
                    _ot["GPU type"] = self.av_g[_kb][1]
                    _ot["GPU name"] = self.av_g[_kb][2]
                    _ot["GPU temp"] = self.get_temp(self.av_g[_kb][0])                      

                if _k in ["vram","gtt","mclk","sclk"]:

                    try :
                    
                        _ot[f"{k2w[_k]} PERCENTAGE"] = _vp = _d[_d.index(_k)+1] 
                        _ot[f"{k2w[_k]} Used"] = _vu = _d[_d.index(_k)+2] 
                        _ot[f"{k2w[_k]} Total"] = _vt = str(round(_exi(_vu)/ _exi(_vp) * 100 , 2 )) + _exa(_vu)
                        _ot[k2w[_k]] = f"{_vu} / {_vt} percentage : {_vp}"

                    except:

                        _ot[f"{k2w[_k]} PERCENT"] = _ot[f"{k2w[_k]} Used"] =  _ot[f"{k2w[_k]} Total"] =  _ot[k2w[_k]] = "Not found"

                else:
                    _ot[k2w[_k]] = _d[_d.index(_k)+1]
            
            _ox["".join(filter(str.isdigit,_ot["bus address"]))[:4]] = _ot

        if bus_address is None: 
            
            return list(_ox.values())

        elif isinstance(bus_address, str):

            return _ox.get(bus_address, _ox[next(iter(_ox))])  

        elif isinstance(bus_address, int) and bus_address < len(_ox):

            return list(_ox.values())[bus_address]   

    def continuos_output(self,bus_address = None,interval = 1 , out_range = 0):
        if out_range==0:
            while self.out:
                sleep(interval)
                yield self.get_output(bus_address)
        else:
            for i in range(out_range):
                sleep(interval)
                yield self.get_output(bus_address)
            self.stop_logging()


keywords = """
Event Engine ,
GPU name ,
GPU temp ,
GPU type ,
GPU usage ,
GTT ,
GTT PERCENTAGE ,
GTT Total ,
GTT Used ,
Memory Clock ,
Memory Clock PERCENT ,
Memory Clock PERCENTAGE ,
Memory Clock Total ,
Memory Clock Used ,
Primitive Assembly ,
Sequencer Instruction Cache ,
Shader Clock ,
Shader Clock PERCENTAGE ,
Shader Clock Total ,
Shader Clock Used ,
Shader Interpolator ,
Texture Addresser ,
VRAM ,
VRAM PERCENTAGE ,
VRAM Total ,
VRAM Used ,
Vertex Grouper + Tesselator ,
bus address ,
color block ,
depth block ,
scan converter ,
"""