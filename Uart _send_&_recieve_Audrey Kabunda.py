#importing the needed module and files form the module
from machine import UART
from machine import Pin
import time

#a UART object with 8 data bits, no parity, and 1 stop bit
uart = UART(1, baudrate=9600, tx=Pin(8), rx=Pin(9))
uart.init(bits=8, parity=None, stop=1)

#i want the receiver to see this message
#i will achieve this through assigning a variable to my message
send_mess = "If the world was ending"
uart.write(send_mess)

#this wait for an appointed amount of time before displaying the receive message
time.sleep(1.5)

#reading the messages from the other Pico and giving it a valuable variable name
rec_mess = uart.read()

#a while True statement in this case will keep the 
while True: 
    #if my pico receives a message, decode and print the message,
    #if not, print didn't receive message
    #handling error cases: try that ↑, if there is no message to begin with, print there is no message 
    try:
        #giving the attribute of decoding messages to a variable name
        recdeco = rec_mess.decode() #this takes the message from the other Pico and presents it in a way that is legible to the receiver 
        send_mess = True
        time.sleep(1.5)

        if uart.any():
            print ("-->", recdeco)
        else:
            print ("didn't receive messages")
    except:
        print("there is no message to decode") #there aren't any received messages from the other Pico