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

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(15, GPIO.OUT,initial=GPIO.LOW)

GPIO.output(15, GPIO.HIGH)
time.sleep(5000)
GPIO.output(15, GPIO.LOW)
GPIO.cleanup()


