import os
import glob
import time
import requests
import json
 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

email = input("Please insert the patient's email: ")
password = input("Please insert the patient's password: ")

data = "{email:" + email + ", password": + password + "}"
headers = {'Content-Type':'application/json'}

response = requests.request("POST", "https://www.akal.app", data=data, headers=headers)

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c

def send_temp(temp):
    response = requests.get("https://www.akal.app/alert/" + temp)

while True:
	send_temp(read_temp())	
	time.sleep(900)
	