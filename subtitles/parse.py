import sys, time, os

'''
functions for parsing raw file data
'''

def process(lines):
    #takes raw lines from the file and changes them to list of lists of format [startTime, EndTime, content]
    
    acc = []
    for line in lines:
        if line != '\n':
            acc.append(line)
    
    cont = ""
    for ctr in range(2,len(acc)):
        cont += acc[ctr]

    lnew = acc[1].split(" --> ")
    t0 = convert(lnew[0])
    t1 = convert(lnew[1][:len(lnew[1])])
    
    return [[t0, t1, cont]]
    
    
def convert(time):
    # converts time from format HH:MM:SS,mS to decimal Seconds 
    inList = time.split(':')
    return int(inList[0])*3600 + int(inList[1])*60 + int(inList[2][:2]) + int(inList[2][3:])/1000.00


def parse (raw, ctr = 1):
    # acts as a wrapper for process and an interface for parse library
    if (len(raw) == 0):
        return raw

    ctr1 = ctr + 1
    en = len(raw)
    for i in range(0, len(raw)):
        if ( raw[i] == str(ctr1)+'\n' ) :
            en = i
    return process(raw[:en]) + parse(raw[en:], ctr + 1) 
