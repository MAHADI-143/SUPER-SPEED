import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')
 
 
 
import requests
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from MAHADI import main
 
        mahadi()
 
 
 
elif bit == "32bit":
 
        from RANDOM import main
 
 
        mahadi()
 
