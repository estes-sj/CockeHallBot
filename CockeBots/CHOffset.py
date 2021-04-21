#Offset value to fix bot
import sys

from datetime import datetime

print("----------------------------")
now = datetime.now()
print("starting at..." + now.strftime("%Y-%m-%d %H:%M:%S"))

# Open function to open the file "MyFile1.txt"
# (same directory) in append mode and
offset_file = open("/home/pi/Documents/CockeBots/offsetcounter.txt", "r+")

print("Increasing Offset Counter...")

value = offset_file.read()
value = int(float(value))
offset_file.close()
print("Current Offset = " + str(value))

offset_file = open("/home/pi/Documents/CockeBots/offsetcounter.txt", "w")
offset_file.truncate(0)

value += 1
offset_file.write(str(value))
offset_file.close()
print("New offset = " + str(value)) 

now = datetime.now()
print("ending task..." + now.strftime("%Y-%m-%d %H:%M:%S"))
