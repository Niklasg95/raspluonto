# ky_026_flame.py - report presence of IR light from flame to serial
# (c) BotBook.com - Karvinen, Karvinen, Valtokari
# modified 6 Oct 2017

#-*- coding: utf-8 -*-

import time
import botbook_gpio as gpio
import paho.mqtt.client as mqtt

learningPeriod = 30

def main():

	broker_address="10.0.0.5"
	client = mqtt.Client("P1")	
	client.connect(broker_address)

	flamePin = 8
	gpio.mode(flamePin, "in")

	#Learning period
	print ("learning... " + str(learningPeriod) + " seconds")
	time.sleep(learningPeriod)
	
	while(True):
		flame = gpio.read(flamePin)
		if(flame == gpio.HIGH):
			client.publish("nuotiovahti","Flame detected" + time.ctime())
			print ("Flame detected " + time.ctime())
		else:
			client.publish("nuotiovahti","NO flame detected" + time.ctime())
			print ("NO flame detected " + time.ctime())
		time.sleep(2)

if __name__ == "__main__":
	main()


