__author__ = 'Maxime'


from libs.bottle import run, Bottle, static_file
from app import *
import os


App = Bottle()



@App.route('/')
def index():
    return "Page d'accueil"

@App.route('/picamera/photo/<name>/<x:int>/<y:int>')
def picamera_takeshot(name = 0, x = 2592, y = 2592):
    if name != 0:
        photoname = application.capture(name, x, y)
        return static_file(photoname + '.jpg', root='img/', mimetype='image/png')
    else:
        return "Le nom doit etre specifie"

@App.route('/picamera/photos/<name>/<nb:int>/<delay:int>/<x:int>/<y:int>')
def picamera_takeshot(name = 0, nb=5, delay=2, x = 2592, y = 2592):
    photos = application.capture_while(delay, nb, name, x, y)

    return photos

@App.route('/img/<name>')
def img(name = ''):
    if name != '':
        return static_file(name, root='img/', mimetype='image/png')

@App.route('/imglist')
def imglist():
    list = {'data':os.listdir('img/')}

    return list


def run_handler():
    run(App, host='0.0.0.0', port=8080)