import times
import names
import math
import random

'''
TO DO
* mess around and figure out right numbers for samplesize and numsamples
'''

#testlist = [0,1,2,3,4,5,6,7,8,9]
#testlist was used for testing formulas bc it was easy to check

#timefreqdict is a dictionary with all the times and their counts
#turned into a function that can be called for any list
def getFreqDict(list_):
    freqdict = {}
    for i in range(len(list_)):
        try:
            a = timefreqdict[str(list_[i])]
            a += 1
            timefreqdict[str(list_[i])] = a
        except KeyError:
            timefreqdict[str(list_[i])] = 1
    return freqdict

#takes a number of samples of n size, averages each sample, then appends to meanlist
#turned into a function (n = samplesize; sampcount = numsamples)
def getMeanlist(list_,n,sampcount):
    meanlist = []
    sampleacc = 0
    for i in range(sampcount):
        for i in range(n):
            x = random.randint(0, len(list_) - 1)
            sampleacc += list_[x]
        meanval = round((sampleacc / n), 2)
        meanlist.append(meanval)
        sampleacc = 0
    return meanlist

#combined both of the average bits of code into one function
def getMean(list_):
    acc = 0
    for i in range(len(list_)):
        acc += list_[i]
    avg = acc / len(list_)
    return avg

#standard deviation of a list
def getSD(list_):
    diffacc = 0
    mu = getMean(list_)
    for i in range(len(list_)):
        diffacc += (list_[i] - mu) ** 2
    sd = (diffacc / len(list_)) ** 0.5
    return sd

#the % error of the mean of the sample mean distribution compared to the actual mean
def getPercError(actual, expected):
    error = (actual - expected) / expected
    return error * 100

#test for 68-95-99.7 rule
#uses the meanlist for this because it is the one I will be graphing
def testNormal(list_):
    total = len(list_)
    mu = getMean(list_)
    sd = getSD(list_)
    sd1 = 0
    sd2 = 0
    sd3 = 0
    for i in range(len(list_)): #yes they aren't supposed to be elif
        if list_[i] <= mu + sd and list_[i] >= mu - sd: #number within 1 stdev
            sd1 += 1
        if list_[i] <= mu + 2 * sd and list_[i] >= mu - 2 * sd: #number within 2 stdev
            sd2 += 1
        if list_[i] <= mu + 3 * sd and list_[i] >= mu - 3 * sd: #number within 3 stdev
            sd3 += 1
    percsd1 = sd1 / total
    percsd2 = sd2 / total
    percsd3 = sd3 / total
    return percsd1, percsd2, percsd3

def checkSkew(list_):
    index_ = math.trunc(0.5 * len(list_)) + 1
    med = list_[index_]
    mean = getMean(list_)
    return 'the mean is ' + str(round(mean, 3)) + ' and the median is ' + str(med)

samplesize = 20 #size of a sample (n)
numsamples = 1000 #number of samples

m200mean = getMean(times.m200)
m200meanlist = getMeanlist(times.m200, samplesize, numsamples)
m200mlavg = getMean(m200meanlist)

'''
all the garbage I print
'''
#print(m200meanlist) #the list that will have the items for the sample mean distribution (normal)
#print('actual mean: ' + str(round(m200mean, 5))) #the mean
#print('sample mean: ' + str(round(m200mlavg, 5))) #the mean of the sample mean distribution
#print('percent error: ' + str(round((getPercError(m200mlavg, m200mean)), 5)) + '%') #the percent error of the mean
print(testNormal(times.m200))
print(checkSkew(times.m200))
print(testNormal(m200meanlist))
print(checkSkew(m200meanlist))
