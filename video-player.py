import os
import time
import RPi.GPIO as GPIO

# Constants
sensorPin = ??
clipDuration = ??

# Variables
lastPlay = 0
i = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensorPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
	if GPIO.input(sensorPin) == False:
		i = i + 1
		print "Motion %d detected" % i
		if (time.time() - lastPlay) > clipDuration:
			os.system('omxplayer -o local 3YearsInHastingsPark.mp4')
			lastPlay = time.time()