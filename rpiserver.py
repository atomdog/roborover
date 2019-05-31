#new rpi rover server
import RPi.GPIO as GPIO
import socket
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(15, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)


def locatehost(hostname):
    hostnotfound = True
    iterations = 0
    while(hostnotfound):
        try:
            return(socket.gethostbyname(hostname))
        except:
            iterations=iterations+1
            print("Base station not found in " + str(iterations) + " iterations.")
            print("Attempting to locate base station again in 5 seconds.")
            time.sleep(5)

bip = ""
opport = 5005
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
connectionsucc=False
try:
    sock.bind((bip, opport))
    connectionsucc=True
    print("Port opened. Enabling reception.")
except:
    print("Socket binding failed")

if(connectionsucc==True):
    while(True):
        data, addr = sock.recvfrom(1024)
        print("received message:", data)
        if(data=='w'):
            GPIO.output(15, GPIO.HIGH)
            GPIO.output(23, GPIO.HIGH)
            GPIO.output(18, GPIO.LOW)
            GPIO.output(24, GPIO.LOW)
        if(data=="s"):
            GPIO.output(18, GPIO.HIGH)
            GPIO.output(24, GPIO.HIGH)
            GPIO.output(15, GPIO.LOW)
            GPIO.output(23, GPIO.LOW)
        if(data="a"):
            GPIO.output(18, GPIO.HIGH)
            GPIO.output(23, GPIO.HIGH)
            GPIO.output(15, GPIO.LOW)
            GPIO.output(24, GPIO.LOW)
        if(data="s"):
            GPIO.output(15, GPIO.HIGH)
            GPIO.output(23, GPIO.HIGH)
            GPIO.output(18, GPIO.LOW)
            GPIO.output(24, GPIO.LOW)
        if(data=='0'):
            GPIO.cleanup()
            exit()
