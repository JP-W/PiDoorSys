# PiDoorSys
A security system built around a Raspberry Pi 2 Model B, an Adafruit PN532 RFID/NFC module, and a Custard Pi 6 Relay Board.
Programs:
Adminprogram.py:
  Adminprogram.py is a python program (an extremely simple one) which simply checks the log or adds cards for you, without having to       manually type them into the Tags.txt file. It uses python's logging library.
Authprogram.py:
  Authprogram.py is also a python program that is very simple and this controls all I/O with the RFID/NFC and also the Tags.txt file.
  It also logs to Door.log, using the logging library, to show exact times of when events happened.
