#!/usr/bin/env python
#All code found here was created by James P. Whybrow (epptjames@gmail.com.)
#Please give credit if you modify. (C)

import binascii
from datetime import datetime
import mmap
import sys
import logging
import time
import Adafruit_PN532 as PN532
import cpi6x
import RPi.GPIO as GPIO
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
dt = datetime.now().strftime('%H:%M:%S on the %d/%m/%Y')

logging.basicConfig(filename='Door.log', level=logging.INFO)

CS   = 18
MOSI = 23
MISO = 24
SCLK = 25

pn532 = PN532.PN532(cs=CS, sclk=SCLK, mosi=MOSI, miso=MISO)
pn532.begin()

ic, ver, rev, support = pn532.get_firmware_version()
print 'Found PN532 with firmware version: {0}.{1}'.format(ver, rev)

pn532.SAM_configuration()

#GPIO.setmode(GPIO.BOARD)
board1 = cpi6x.add1
cpi6x.setasoutput(board1)

def relay(opentime):
    cpi6x.setbit(board1, cpi6x.ONrelay2)
    time.sleep(opentime)
    cpi6x.clrbit(board1, cpi6x.OFFrelay2)

print 'Waiting for card...'
while True:
    uid = pn532.read_passive_target()
    f = open('Tags.txt')
    s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    uidstr = str(uid)
    if uid is None:
	continue
    elif s.find(binascii.hexlify(uid)) != -1: #Basically a long way of saying 'if uid in tags.txt'
        logging.info(binascii.hexlify(uid)+':'+'Granted Access'+':'+dt)
        print('Found Tag with UID:'+binascii.hexlify(uid)+'. Logged and granted.')
        relay(3)
    elif binascii.hexlify(uid).startswith('08'):
	logging.info('Apple Pay Entry'+':'+'Granted Access'+':'+dt)
	print('Found Apple Pay Entry. Allowing Access')
	#ADD RELAY SCRIPT HERE REMEMBER TO REM TIME.sleep
        relay(3)
    else:
        logging.info(binascii.hexlify(uid)+':'+'Denied Access'+':'+dt)
	print('Found Tag with UID:'+binascii.hexlify(uid)+'. Logged and denied.')
        time.sleep(2)
        
    

