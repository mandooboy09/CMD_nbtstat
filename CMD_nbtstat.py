
# NBTSTAT TOOL
restart = 0
import os

while restart == 0:
    ipaddress = input("NBSTAT this address: 61.250.183.")
    command = "nbtstat -a 61.250.183." + ipaddress
    os.system(command)
    input()
    os.system("CLS")


