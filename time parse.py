import times
import names
import math
import random

'''
TO DO
* finish coding for making meanlist
* mess around and figure out right numbers for samplesize and numsamples
* round the mean
'''

#testlist = [0,1,2,3,4,5,6,7,8,9]
#testlist was used for testing formulas bc it was easy to check

#timefreqdict is a dictionary with all the times and their counts
timefreqdict = {}
for i in range(len(times.m200)):
    try:
        a = timefreqdict[str(times.m200[i])]
        a += 1
        timefreqdict[str(times.m200[i])] = a
    except KeyError:
        timefreqdict[str(times.m200[i])] = 1

#this bit gets the mean of the times
acc = 0
for x in range(len(times.m200)):
    acc += times.m200[x]
mean = acc / (len(times.m200) + 1)

#this is the list where all the different averages will be appended to
#once this is done and samplesize and numsamples are decided it gets copied to sheets and graphed
meanlist = []

#these are here and isolated so they can be modified pretty easily
samplesize = 10
numsamples = 100

#do this bit (working out sample size and number of samples for mean distribution)
#append each one to meanlist
for i in range(numsamples):
    for i in range(samplesize):
        break
    break

#all the garbage I print
print(meanlist) #the list that will have the items for the sample mean distribution (normal)
print('mean: ' + str(mean)) #the mean --> round to 2 decimals
for i in range(len(times.m200)): #prints all the times
    print(times.m200[i])
print(timefreqdict) #all the frequencies of the different times
