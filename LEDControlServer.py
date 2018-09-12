# File: LEDControlServer.py
# Author: BehindTheSciences.com
# Description: A simple BT server that accepts connection from a phone and controls LEDs
#


from bluetooth import *
import RPi.GPIO as GPIO

server_sock=BluetoothSocket( RFCOMM )
server_sock.bind(("",PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]

uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.output(18,GPIO.LOW)
GPIO.setup(17,GPIO.OUT)
GPIO.output(17,GPIO.LOW)

advertise_service( server_sock, "BTS",
                   service_id = uuid,
                   service_classes = [ uuid, SERIAL_PORT_CLASS ],
                   profiles = [ SERIAL_PORT_PROFILE ], 
                    )
                   
print("Waiting for connection on RFCOMM channel %d" % port)

client_sock, client_info = server_sock.accept()
print("Accepted connection from ", client_info)

try:
    while True:
        data = client_sock.recv(1024)
        if len(data) == 0: break
        print("received [%s]" % data.decode("utf-8"))
        if data == "GreenOn":
            GPIO.output(18,GPIO.HIGH)
        if data == "GreenOff":
            GPIO.output(18,GPIO.LOW)
        if data == "RedOn":
            GPIO.output(17,GPIO.HIGH)
        if data == "RedOff":
            GPIO.output(17,GPIO.LOW)
        
except IOError:
    pass

print("Disconnected")

client_sock.close()
server_sock.close()
print("All Closed")
