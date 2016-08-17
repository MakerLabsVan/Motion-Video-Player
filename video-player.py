import os
import time
import RPi.GPIO as GPIO

# Constants
sensorPin = 14
clipDuration = 640
command = 'omxplayer -o local '
video = '3YearsInHastingsPark.mp4'

# Variables
i = 0
lastPlay = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensorPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
	if GPIO.input(sensorPin) == False:
		i = i + 1
		print "Motion %d detected" % i

		if (time.time() - lastPlay) > clipDuration:
			os.system(command + video)	
			lastPlay = time.time()
			i = 0