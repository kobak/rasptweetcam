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
import random

messages = [
      "Hello world #Picademy",
      "Team RaspTweetCam are the best! #Picademy",
      "We love Rapsberry Pi! #Picademy",
  ]
  
message = random.choice(messages)
twitter.update_status(status=message)
print("Tweeted: %s" % message)




