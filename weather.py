import math
import random

def weatherMessage(temp,low,med):
	# old code - temp = 40 * math.sin(2.5)
	if temp < low:
		print("wear wool trousers")
	elif temp < med:
		print("wear trousers")
	else:
		print("wear shorts")

def predictTomorrowsTemp(todaysTemp):
	
	if todaysTemp <= - 3:
		newTemp = -3
	elif todaysTemp >= 24:
		newTemp = 24
	else:		
		change = random.choice(range(-1,2))
		newTemp = todaysTemp + change
	return newTemp

#for i in range(0,101):
#	print("The temperature is: " + str(i))
#	weatherMessage(i,5,20)

#today = 10
#tomorrow = predictTomorrowsTemp(today)
#nextday = predictTomorrowsTemp(tomorrow)
#print(today)
#print(tomorrow)
#print(nextday)


temp = 50
for day in range(1,8):
	temp = predictTomorrowsTemp(temp)
	print("Day " + str(day))
	print("Tomorrow will be:" + str(temp))

