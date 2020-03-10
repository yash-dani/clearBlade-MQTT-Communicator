'''
author @yash
clearBlade MQTT Message Communicator
March 9th, 2020
'''
# IMPORTS
import psutil
from clearblade.ClearBladeCore import System, Query, Developer
import time

# Setup system using credentials
SystemKey = "8eedb6e60b8892f4e0e5d6fe8111"
SystemSecret = "8EEDB6E60BFCD5B4E8A6F5E7E264"

mySystem = System(SystemKey, SystemSecret)

# Setup User
yash = mySystem.User("yash.dani@uwaterloo.ca", "D00pamine!!")




#get the CPU Usage using:
'''
while True:
	print(psutil.cpu_percent())
	time.sleep(1)
'''