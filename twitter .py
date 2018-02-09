from picamera import PiCamera
from gpiozero import Button
from time import sleep
import time
import RPi.GPIO as GPIO
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
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 15
GPIO_ECHO = 8
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance




camera = PiCamera()
button = Button(14)


def TakePicture(name, delay=1):
    camera.start_preview(alpha=192)
    sleep (delay)
    camera.capture("/home/pi/{}.jpg".format(name))
    #applyEffect()
    camera.image_effect = 'colorswap'
    camera.stop_preview()

def useButton():
    button.wait_for_press()
    TakePicture("tweetpic",  3)
    

def useDistanceSensor():
    
    while distance() < 20:
        print("in useDistance: ", distance())
        TakePicture("tweetpic",  3)
        sleep (0.5)
        tweet()
        
def tweet():
    messages = "Hello world! Team @RaspTweetCam are the best! #Picademy"
    with open('/home/pi/tweetpic.jpg', 'rb') as photo:
        twitter.update_status_with_media(status=messages, media=photo)
  
    print("Tweeted: %s" % messages)

while True:
    
    useDistanceSensor()
    #useButton()


