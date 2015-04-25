__author__ = 'Maxime'

import libs.bottle
import picamera
import time
import socket


global application


class appli:

    on = 1
    camera = None

    resolutions = [ (2592, 1944) , (1920, 1080), (1296, 972), (1296, 730), (640, 480) ]

    def __init__(self):
        print ">> Lancement"
        print ">> Initialisatoin de la camera"
        self.camera = self.initcam()
		

        print ">> Lancement du streaming"


    def initcam(self):
        camera = picamera.PiCamera()
        camera.resolution = self.resolutions[4]
        camera.framerate = 24

        return camera

    def capture(self, name = 0, x = 2592, y = 1944):
        if name == 'Default':
            photoname = str(time.time())
        else:
            photoname = name

        resolution = (x,y)
        self.camera.capture('img/' + name + '.jpg', use_video_port=True, resize = resolution)

        return photoname

    def capture_while(self, delay, nb, nametemplate, x = 2592, y = 1944):
        for i in range(nb):
            self.camera.capture('img/' + str(nametemplate) + '-' + str(i) +  '.jpg', use_video_port=True, resize = (x, y))
            time.sleep(delay)

        return {'nametemplate' : nametemplate, 'from': 0, 'to': nb-1}

    def streaming(self, port):
        server_socket = socket.socket()
        server_socket.bind(('0.0.0.0', port))
        server_socket.listen(0)

        print "Streaming"
        # Accept a single connection and make a file-like object out of it
        connection = server_socket.accept()[0].makefile('wb')
        self.camera.start_recording(connection, format='h264', splitter_port=2)

        while self.on:
            time.sleep(1)

        print "Arret Streaming"
        self.camera.stop_recording(splitter_port=2)
        print "Fermeture connexion"
        connection.close()
        print "Arret Serveur"
        server_socket.close()
        print "Arret complet"


application = appli()