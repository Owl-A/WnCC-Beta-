import sys, time, os
from parse import *

'''
the idea of the algorithm is recursively processing the list of overlapping subtitles to 
give a sort of flat list in which the subtitles are not overlapping.
say, we have flattened a list already then adding another element is simply a matter a figuring out 
which keys (inner lists) are affected, segregating them, and creating a list with new keys 
'''
def segment(format):
    
    # uses <insertion> sort like algorithm
    if (format == []):
        return []
    else:
        return overlay(format[0],segment(format[1:])) # recursion

def overlay (newLine, sortedTxt):
    # takes a new line and ditermines its appropriate position and formatting in the final list
    if sortedTxt == []:
        return [newLine]
    else:

        acc = []
        overlap = []
        lft = []
        rgt = []
        for sortedLine in sortedTxt:
            if (sortedLine[1] <= newLine[0]) : 
                lft = lft + [sortedLine]
            elif (newLine[1] <= sortedLine[0]):
                rgt = rgt + [sortedLine]
            else:
               overlap = overlap + [sortedLine]

        for sortedLine in overlap:
            
            if(sortedLine[0] < newLine[0]):
                acc += [[sortedLine[0], newLine[0], sortedLine[2]]]
                curr = newLine[0]
            elif (sortedLine[0] > newLine[0]):
                acc += [[ newLine[0], sortedLine[0], newLine[2]]]
                curr = sortedLine[0]
            else:
                curr = newLine[0]

            currT =  min(sortedLine[1],newLine[1])
            acc += [[ curr,currT , newLine[2] + sortedLine[2]]]
            curr = currT
            newLine = [curr, newLine[1], newLine[2]]

            if(newLine[1] < sortedLine[1]):
                 acc += [[ newLine[1],sortedLine[1],sortedLine[2]]]
        
        if(newLine[1] != newLine[0]):
            acc += [newLine]

        return lft + acc + rgt

def scheduler(lineKeys):
    # this gentleman handles the metronome
    os.system('cls' if os.name == 'nt' else 'clear')
    print '<start>'
    time.clock()
    for key in lineKeys:
        while (key[0] > time.clock()):
            pass
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print key[2]

        while (key[1] > time.clock()):
            pass
        os.system('cls' if os.name == 'nt' else 'clear')
    print '<end>'

try:
    file = open(sys.argv[len(sys.argv) - 1], 'r')
    formatted = segment(parse(file.readlines(),1))
    scheduler(formatted)
    file.close()
except:
    print ("an unknown error occured")