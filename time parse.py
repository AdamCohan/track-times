import times
import names
import math
import random

'''
TO DO
* figure out why meanpercenterror is always about -1.45%
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

meanlist = [] #where all the averages are appended to
sampleacc = 0 #accumulates all the random times
meanval = 0 #a mean time that gets added to meanlist
samplesize = 100 #size of a sample (n)
numsamples = 100 #number of samples

#do this bit (working out sample size and number of samples for mean distribution)
#append each one to meanlist
for i in range(numsamples):
    for i in range(samplesize):
        x = random.randint(0,len(times.m200)-1)
        sampleacc += int(times.m200[x])
    meanval = sampleacc / samplesize
    meanlist.append(meanval)
    sampleacc = 0

meanlistcum = 0
meanlistavg = 0
for i in range(len(meanlist)):
    meanlistcum += meanlist[i]
    meanlistavg = meanlistcum / len(meanlist)

meanpercenterror = (meanlistavg - mean) / mean
#all the garbage I print
print(meanlist) #the list that will have the items for the sample mean distribution (normal)
print('actual mean: ' + str(mean)) #the mean --> round to 2 decimals
print('sample mean: ' + str(meanlistavg)) #the mean of the sample mean distribution
print('percent error: ' + str(meanpercenterror * 100) + '%')
