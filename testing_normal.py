import full_lists
import time_parse

def turningToList(list_):
    newlist = []
    for i in list_:
        item = i.split('  ')
        length_ = len(item)
        for char_index in range(length_):
            reverse_index = length_ - char_index - 1
            if item[reverse_index] == '':
                item.remove(item[reverse_index])
        for j in item:
            indeks = item.index(j)
            h = list(j)
            if h[0] == ' ':
                h.remove(h[0])
                m = ''
                for k in h:
                    m += k
                item[indeks] = m
        newlist.append(item)
    return newlist

def fixingTimes(list_): #use this one after turningToList MAKE SURE TO CHECK WHICH LAYER OF NESTED LIST
    newlist = []
    for i in list_:
        if len(str(i[1])) > 5:
            indeks = list_.index(i)
            l = ''
            j = list(i[1])
            for k in range(5):
                l += j[k]
            i[1] = l
            list_[indeks] = i
    return list_

'''
order of indecies in each item (remember to do -1 when looking)
1. position on document
2. time
3. name
4. nationality
5. birthday
6. pos (for 1rA 1q1 1h2 etc --> first number)
7. venue
8. date
'''

def getPosTimes(list_, position):
    poslist = []
    timelist = []
    for i in list_:
        pos = list(i[5])
        if pos[0] == str(position):
            poslist.append(i)
    for i in poslist:
        timelist.append(i[1])
    return timelist

first400m1 = getPosTimes(fixingTimes(turningToList(full_lists.list400m)),1)
first400m2 = getPosTimes(turningToList(full_lists.list400m),1)
m400freqdict1 = time_parse.getFreqDict(first400m1)
m400freqdict2 = time_parse.getFreqDict(first400m2)

for key in m400freqdict1:
    print(key, m400freqdict1[key])
