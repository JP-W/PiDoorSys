import RPi.GPIO as GPIO
import time
import cpi6x
board1=cpi6x.add1
cpi6x.setasoutput(board1)
cpi6x.setbit(board1, cpi6x.ONrelay2)
time.sleep(5)
cpi6x.clrbit(board1, cpi6x.OFFrelay2)

 
