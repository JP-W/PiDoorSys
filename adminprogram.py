#All code found here was created by James Peter Whybrow (epptjames@gmail.com.)
#Please give credit if you modify. (C)

#Import Section

import logging
import time
from datetime import datetime
import binascii
import sys
import Adafruit_PN532 as PN532
dt = datetime.now().strftime('%d-%m-%Y on the %H:%M:%S')

#RFID Config Section

CS   = 18
MOSI = 23
MISO = 24
SCLK = 25

pn532 = PN532.PN532(cs=CS, sclk=SCLK, mosi=MOSI, miso=MISO)
pn532.begin()

ic, ver, rev, support = pn532.get_firmware_version()

pn532.SAM_configuration()

#Logging Section

logging.basicConfig(filename='Tags.txt',level=logging.INFO)

#Everything Else

print "Welcome to James's Door Security Program."
while True:
    INPUT1 = raw_input('Enter Option (1: Adder or 2: Searcher):')
    if INPUT1 == '1':
        print ('Tag Adder.')
        while True:
	    uid = pn532.read_passive_target()
            print 'Waiting for card...'
            if uid is None:
                continue
            else:
                print('Found Tag with UID:'+binascii.hexlify(uid))
                print('You may hit Ctrl + C if you have got the incorrect tag.')
		print('Also, When done, hit Ctrl + C.')
                hexuid = binascii.hexlify(uid)
                recip = raw_input('Now enter name of recipient:')
                print('Accepted.')
                logging.info(hexuid+':'+recip+':'+'Added at '+dt)
    elif INPUT1 == '2':
        print('Log Searcher')
        UIDINPUTLOGSEARCH = raw_input('Please Enter Name or UID to find:')
        with open("Door.log") as f:
            for line in f:
                if UIDINPUTLOGSEARCH in line:
                    print line
                elif UIDINPUTLOGSEARCH not in line:
                    print 'Ended, or not in file.'
                    break
                else:
                    time.sleep(0.1)
        
    else:
        print('Wrong input.')
