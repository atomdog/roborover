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
        if(data=='0'):
            GPIO.cleanup()
            exit()
        datalist = [int(data[0:2]), int(data[2:4]),int(data[4:6]), int(data[6:8]), int(data[8]), int(data[9]), int(data[10]), int(data[11])]
        for x in range(5, 9):
            if(datalist[x]==0):
                GPIO.output(datalist[x-4], GPIO.LOW)
        for x in range(5, 9):
            elif(datalist[x]==1):
                GPIO.output(datalist[x-4], GPIO.HIGH)
