__author__ = 'Maxime'


from RequestHandler import *
import socket
import time
import threading
import sys



def main():
    a = threading.Thread(None, application.streaming, None, (), {'port': 7000})
    c = threading.Thread(None, run_handler, None)

    a.start()
    c.start()

    print str(application.on)

    while application.on == 1:
        data = raw_input(">> ")

        if data == 'stop':
            application.on = 0
            App.close()


        spliteddata = data.split(' ')

        if spliteddata[0] == "capture_while":
            application.capture_while(int(spliteddata[1]), int(spliteddata[2]), str(spliteddata[3]))
        if spliteddata[0] == "lum":
            application.camera.brightness = int(spliteddata[1])
        if spliteddata[0] == "con":
            application.camera.contrast = int(spliteddata[1])
        if spliteddata[0] == "iso":
            application.camera.iso = int(spliteddata[1])
        if spliteddata[0] == "expo":
            application.camera.exposure_compensation = int(spliteddata[1])
        if spliteddata[0] == "mode":
            application.camera.exposure_mode = int(spliteddata[1])
        if spliteddata[0] == "modes":
            print application.camera.EXPOSURE_MODES


if __name__ == '__main__':
    main()
    sys.exit()