from picamera import PiCamera
from gpiozero import Button
from time import sleep

camera = PiCamera()
button = Button(14)


def TakePicture(name, delay=1):
    camera.start_preview(alpha=192)
    sleep (delay)
    camera.capture("/home/pi/{}.jpg".format(name))
    #applyEffect()
    camera.image_effect = 'colorswap'
    camera.stop_preview()

button.wait_for_press()

TakePicture("tweetpic",  3)

#twitter
from twython import Twython

from auth import (
      consumer_key,
      consumer_secret,
      access_token,
      access_token_secret
  )
twitter = Twython(
      consumer_key,
      consumer_secret,
      access_token,
      access_token_secret
  )

messages = "Hello world! Team @RaspTweetCam are the best! #Picademy"

with open('/home/pi/tweetpic.jpg', 'rb') as photo:
      twitter.update_status_with_media(status=messages, media=photo)
  
print("Tweeted: %s" % messages)




