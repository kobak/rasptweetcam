#camera test by Ian
# v001
from picamera import PiCamera

def TakePicture(name, delay=1):
    camera = PiCamera()
    camera.start_preview(alpha=192)
    camera.capture("/home/pi/{}.jpg".format(name))
    #applyEffect()
    camera.image_effect = 'colorswap'
    camera.stop_preview()



TakePicture("test")
