import math
print 'For tutorial, please see video: https://www.youtube.com/watch?v=09UgmwtL12c.'
firstLocked = int(raw_input('First locked position: '))
secondLocked = int(raw_input('Second locked position: '))

if(firstLocked > 11 or secondLocked > 11):
	print 'Error, position value(s) should not be over 11!'
	exit()

res = float(raw_input('Resistant location: '))
firstVal = (math.ceil(res) + 5) % 40
mod = firstVal % 4
third = []
second = []
for x in range(0, 3):
	if (((10 * x) + firstLocked) % 4 == mod):
		third.append((10 * x) + firstLocked)	
	if (((10 * x) + secondLocked) % 4 == mod):
		third.append((10 * x) + secondLocked)		
print 'Possible third digits: ' 
print third
thirdVal = int(raw_input('Which is the third digit? '))
for x in range(0, 9):
	temp = ((mod + 2) % 4) + (4 * x)
	if((thirdVal + 2) % 40 != temp and (thirdVal - 2) % 40 != temp):
		second.append(temp)
print firstVal
print str(second)[1:-1]
print second
print thirdVal
