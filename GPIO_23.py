#!/usr/bin/env python

import sys
import RPi.GPIO as GPIO
import io  # used to create file streams
import fcntl  # used to access I2C parameters like addresses
import time  # used for sleep delay and timestamps
import string  # helps parse strings
import json
import datetime
import requests
import logging, threading, functools

nodeID     = "SACSYCHY778483477873YHSH"
node_type  = "2"

DEBUG = True
url_Post = "http://demo.ilyra.vn/node/sensordata"
config_direct = "/home/pi/config/"
DataLog_direct = "/home/pi/log/log.txt"
Data_offline = "/home/pi/log/offline.json"
host_addr = "http://demo.ilyra.vn"
url_regist ="http://demo.ilyra.vn/api/device/register"
url_Config_File = 'http://demo.ilyra.vn/api/device/loadconfig'



def delay(numTimes,speed):
    for i in range(0,numTimes):## Run loop numTimes
        print "Iteration " + str(i+1)## Print current loop
        time.sleep(speed)## Wait
def log(message):
    if DEBUG:
	print str(message)
def pushData(type,Message):
    print Message
    headers = {'Content-type': 'application/json'}
    payload = {
               "name":"SS_DATA",
                "nodeId":nodeID,
                "data":str(type)+":"+str(Message),
                "time":str(datetime.datetime.utcnow().isoformat())
               }

    rsp = requests.post(url_Post, json=payload, headers=headers)
    for i in range (1,10):
    	time.sleep(0.2)
    if rsp.status_code == 200:
	log("Succes")
      	return True
    else:
        log("False")
	return False
def writeLog(Message):
    log_file = open(DataLog_direct,"ab")
    log_file.write(Message+str(datetime.datetime.now())+'\n')
    log_file.close()
def check_Internet_connect(hostname):
    ret_code = subprocess.call(['ping', '-c', '5', '-W', '3', hostname],stdout=open(os.devnull, 'w'),stderr=open(os.devnull, 'w'))
    for i in range(1,5):
	time.sleep(0.5)
    if ret_code == 0 :
    	return True
    	pass
    else: 
    	return False
     

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT,initial=GPIO.LOW)

data = sys.argv[1:]
delay_time = data[1]
print(data[1])
GPIO.output(23, GPIO.HIGH)
delay(delay_time,1)
GPIO.output(23, GPIO.LOW)
GPIO.cleanup()
message = data[0]+"Done"
if check_Internet_connect(host_addr):
    pushData(node_type,message)
else:
    writeLog(message)