# -*- coding: utf-8 -*-
#!/usr/bin/env python
import json
import requests
import os.path
import io
import os
import datetime
import time
import os
import subprocess
from wifi import Cell, Scheme 
from socketIO_client import SocketIO, LoggingNamespace
import logging, threading, functools
from apscheduler.schedulers.background import BackgroundScheduler



nodeID = "SACSYCHY778483477873YHSH"
node_type = "1"

DEBUG = True

config_direct = "/home/pi/config/"
DataLog_direct = "/home/pi/log/log.txt"
Data_offline = "/home/pi/log/offline.json"
host_addr = "http://demo.ilyra.vn"
url_regist ="http://demo.ilyra.vn/api/device/register"
url_Config_File = 'http://demo.ilyra.vn/api/device/loadconfig'
url_Post = "http://demo.ilyra.vn/node/sensordata"

query = {
    "__sails_io_sdk_version": "0.13.8",
    "__sails_io_sdk_platform": "browser",
    "__sails_io_sdk_language": "javascript"
}

emit_data = {"url": "/actuator/34/communicate"}

Conf_File = "config.json"
isConnected = False 
Active_Flag = False
regist_flag = False
Pause_Flag  = False
#/* ------ Config ------------------- */
#****Type Node ****

#		GPIO 22 : HIGH | LOW
#		GPIO 23 : HIGH | LOW
#		GPIO 24 : HIGH | LOW
#		GPIO 25 : HIGH | LOW
#		GPIO 26 : HIGH | LOW
#		GPIO 27 : HIGH | LOW
#
#

## ------------------------ Function ----------------------------
def on_connect():
    // active run flag
    // write log time active
    // listen command channel
    
def on_disconnect():
    // disable run flag 
    // alarm by LED error disconnect with server
    // write log time when disconnect
    // try create new connect

def on_reconnect():
    // emit message  aim to connect server
    socketIO.emit("get",emit_data)



def log(message):
    if DEBUG:
	print str(message)
def timeout():
    print " -----  Rewaiting --------"
    socketIO.wait(30)

def GPIO_22(message,interval):
    print "--------  GPIO_22 -----------"
    log(datetime.datetime.now())
    command = 'python /home/pi/actuator/GPIO_22.py'+' '+message+' '+str(interval)
    procs = subprocess.Popen(command,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,)
    stdout,stderrs = procs.communicate('through stdin to stdout\n')
    procs.wait()
    log(stdout)
def GPIO_23(message,interval):
    print "--------  GPIO_23 -----------"
    log(datetime.datetime.now())
    command = 'python /home/pi/actuator/GPIO_23.py'+' '+message+' '+str(interval)
    procs = subprocess.Popen(command,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,)
    stdout,stderrs = procs.communicate('through stdin to stdout\n')
    procs.wait()
    log(stdout)
def GPIO_24(message,interval):
    print "--------  GPIO_24 -----------"
    log(datetime.datetime.now())
    command = 'python /home/pi/actuator/GPIO_24.py'+' '+message+' '+str(interval)
    procs = subprocess.Popen(command,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,)
    stdout,stderrs = procs.communicate('through stdin to stdout\n')
    procs.wait()
    log(stdout)
def GPIO_25(message,interval):
    print "--------  GPIO_25 -----------"
    log(datetime.datetime.now())
    command = 'python /home/pi/actuator/GPIO_25.py'+' '+message+' '+str(interval)
    procs = subprocess.Popen(command,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,)
    stdout,stderrs = procs.communicate('through stdin to stdout\n')
    procs.wait()
    log(stdout)
def GPIO_26(message,interval):
    print "--------  GPIO_26 -----------"
    log(datetime.datetime.now())
    command = 'python /home/pi/actuator/GPIO_26.py'+' '+message+' '+str(interval)
    procs = subprocess.Popen(command,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,)
    stdout,stderrs = procs.communicate('through stdin to stdout\n')
    procs.wait()
    log(stdout)
def GPIO_27(message,interval):
    print "--------  GPIO_27 -----------"
    log(datetime.datetime.now())
    command = 'python /home/pi/actuator/GPIO_27.py'+' '+message+' '+str(interval)
    procs = subprocess.Popen(command,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,)
    stdout,stderrs = procs.communicate('through stdin to stdout\n')
    procs.wait()
    log(stdout)

def check_config_exist():
    file = config_direct+Conf_File
    if os.path.isfile(file):
        return True
	pass
    else:
        return False
def upload_offline_log():
    with io.open(Data_offline) as ourfile:
        dataLoad = json.load(ourfile)
    try:
        resp = requests.post(url_Config_File,data=dataLoad)
        if resp.status_code == 200:
	    return True
	else:
	    return Falses
    except Exception as e:
	raise
	return False
def check_Internet_connect(hostname):
    ret_code = subprocess.call(['ping', '-c', '5', '-W', '3', hostname],stdout=open(os.devnull, 'w'),stderr=open(os.devnull, 'w'))
    for i in range(1,5):
	time.sleep(0.5)
    if ret_code == 0 :
    	return True
    	pass
    else: 
    	return False
def down_Config():
    data = {'imel':node_Imel}
    if check_config_exist():
        os.remove(config_direct+Conf_File)
    try:
	resp = requests.get(url_Config_File,data)
	#log(resp.json())
	with io.open( config_direct+Conf_File,'w+', encoding='utf8') as ourfile:
	    #json.dump(resp.json(),ourfile)
	    #ourfile.write(str_)
            ourfile.write(unicode(json.dumps(resp.json(), ensure_ascii=False)))
	    ourfile.close()
	    return True
	    pass
    except Exception as e:
	raise
	return False
def read_config_file():
    with io.open( config_direct+ Conf_File) as ourfile:
        dataLoad = json.load(ourfile)
        ourfile.close()
	return dataLoad

def write_offline(a):
    try:
        with open(Data_offline,'w+') as data:
	    data_loaded = json.load(data_file)
    except Exception as e:
	log("Error")
    log = data_loaded[log]
    log =+ str(a)+"|"
    data_loaded[log] = log
    with open(Data_offline,'w') as data:
	data.write(json.dumps(data_loaded))
def check_Wifi_connected():
    wifi = Cell.all('wlan0')[0]
    if wifi.ssid != "":
	return True
    else:
	return False
def config_wifi(ssid,passw):
    try:
        procs = subprocess.Popen('sudo /home/pi/raspi-wifi/config.sh '+ssid+' '+passw,shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,)
	res,errs = procs.communicate('through stdin to stdout\n')
	log(res)
    except Exception as e:
	raise e
    else:
         os.system('sudo reboot')
def controller(*args):
    # check command
    if args[command] == "reconfig":
	resp = down_Config()
	if resp:
	    os.system('sudo reboot')
def regist_device():
    data = {'imel':node_Imel,'type':node_type}
    try:
        resp = requests.post(url_regist,data)
        for x in xrange(1,5):
	    time.sleep(0.5)
        log("regist fucntion")
        log(resp.status_code)
	return resp.status_code
    except Exception as e:
    	return 400
    	log("error")
def parse_command():
    resp = requests.get("link check command")
    for x in xrange(1,5):
	time.sleep(0.5)
    data = resp.json()
	
def _init_():
    
    log("---- Init () ____")
    log(Active_Flag)
    readed = False
    if check_config_exist():
	log("----- regist_flag == True -----")
        regist_flag = True     

    if regist_flag == False:
	log("----- regist_flag == False -----")
        regist_resp = regist_device()
        if regist_resp == 200:
             log("right")
             regist_flag = True    
    if Active_Flag == False and regist_flag == True :
        log("---- state 1 ____")
        if check_config_exist():
	    log(" --- read config ---- ")
	    try:
	        config = read_config_file()
		readed = True
	    except IOError:
	        log(" Read file error")
	else:
            log("down load config")
	    out = down_Config()
	    if out:
	    	log(" success download confg")
	    	config = read_config_file()
		readed = True
	    else:
	    	log("error download")
	if check_Wifi_connected() == False:
            if ('wifi' in config):
		ssid = config["wifi"]["ssid"]
		passw = config["wifi"]["password"]
		try:
		    config_wifi(ssid,passw)
		except Exception as e:
		    raise e
	    else:
		log(" Missing Wifi config")
	else:
	    isConnected = True
	    log(" Already connect wlan")
	        # Parse Config Device   
	    Active_Flag = True
	    log("----- Active_Flag:%s ---" %Active_Flag)

#    else:
#        log(" System Actived")   
def writeLog(Message):
    log_file = open(DataLog_direct,"ab")
    log_file.write(Message+str(datetime.datetime.now())+'\n')
    log_file.close()
def on_aaa_response(*args):
    print('on_aaa_response', args)
    print datetime.datetime.now()
    // parse command for server with 3 value
    // message_id | port_number | interval
    // write log receive command 
    switch case : port : 
    // pass argument message_ID and interval to do task 
    // message_id use to report done when finish task


def pushData(type,Message):
    headers = {'Content-type': 'application/json'}
    payload = {
               "name":"SS_DATA",
                "nodeId":nodeID,
                "data":str(type)+":"+str(Message),
                "time":str(datetime.datetime.utcnow().isoformat())
               }
    print json.dumps(payload)
    rsp = requests.post(url_Post, json=payload, headers=headers)
    for i in range (1,10):
    	time.sleep(0.2)
    if rsp.status_code == 200:
	log("Succes")
      	return True
    else:
        log("False")
	return False
def main():
    log("----- main ()-----")
    ##global Active_Flag
    #// check active flag
    #creat scheduler to check socketwhen  
    scheduler = BackgroundScheduler()
    scheduler.add_job(timeout, 'interval', seconds=30)
    scheduler.start()

    try:
        while True:
            time.sleep(0.1)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
            #os.system('sudo reboot')

if __name__ == '__main__':
    main()

