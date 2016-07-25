#!/usr/bin/python3.4
import fileinput

nation = -1 #init var with the first iteration value
sumTotal = 0


for line in fileinput.input():

	data = line.replace("\n","").split('\t')
	newNation = data[0]
	total = int(data[1])

	#set value in the first iteration
	if (nation == -1):
		nation = newNation
	#increment value if the key is the same
	if (newNation == nation):
		sumTotal += total
	#if the key is different print previos values and restart with the key
	else:
		print(('{0}\t{1}'.format(nation, sumTotal)))
		nation = newNation
		sumTotal = total

#print last value
print(('{0}\t{1}'.format(newNation, sumTotal)))