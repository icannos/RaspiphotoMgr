__author__ = 'Maxime'


from RequestHandler import *
import socket
import time
import threading

import Image



def main():

    a = threading.Thread(None, application.streaming, None, (), {'port': 7000})
    c = threading.Thread(None, run_handler, None)
    a.start()
    c.start()

    while application.on:
        data = raw_input(">> ")

        if data == 'stop':
            application.on = 0
            App.close()

        spliteddata = data.split(' ')

        if spliteddata[0] == "capture_while":
            application.capture_while(int(spliteddata[1]), int(spliteddata[2]), str(spliteddata[3]))



if __name__ == '__main__':
    main()