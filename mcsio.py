#!/usr/bin/env python
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_up)



while True:

	SwitchStatus = GPIO.input(24)
	if( SwitchStatus ==0):
		print('Button pressed')
	else:
		print('Button released')
	payload = {"datapoints":["dataChnId":"Hum","values":{"value":humidity}},
		{"dataChnId":"Temp","values":{"value":temperature}},
		{"dataChnId":"SwitchStatus","values":{"value":SwitchStatus}}]}

