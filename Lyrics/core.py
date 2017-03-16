import requests, os, threading, time, sys
'''
takes artist name and swear word as arguements and returns occurence in the lyrics
'''
# transf takes the artist name and returns the URL on which song list will be found
# trhelp is a helper function

global curse 
curse = sys.argv[len(sys.argv) - 1].lower()
artist = sys.argv[len(sys.argv) - 2]
global occur 
occur = 0
#global calls # needed to signal other threads to stop
#calls = 0


def trhelp (Nam):
    tempPlace = Nam.find(" ")
    if (tempPlace > 0):
        return Nam[:tempPlace] + trhelp(Nam[tempPlace + 1:])
    else:
        return Nam

def transf (Nam) :
    return 'http://www.azlyrics.com/' + Nam[:1].lower() + '/' + trhelp(Nam[:].lower()) + '.html'


def retrieve (URL) :
    a = requests.Session()
    # changing the header User-Agent for my requests with that of google chrome to fake a browser
    # apparently azlyrics is not BOT-Friendly
    a.headers.update({'Accept' : 'text/html'})
    a.headers.update({'Accept-Encoding' : 'gzip'})
    a.headers.update({'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'})
    tp = a.get(URL)
    if tp.status_code == 200 :                              ########
        return tp                   # often returns 205, Guess what also prevents too many requests
    print "Error"                   #debug  
    del a
    return tp          
  
    

def SortArtist (Nam) :

    #Get the song list
    Nam = transf(Nam)
    temp = retrieve(Nam).text #takes a lot of time (cant help it)
    temp = temp [temp.find("<!-- start of song list -->") + 27 : temp.find("<!-- end of song list -->")]

    # iterate over the song list
    placeSt = temp.find('<a href="..') + 11
    temp = temp[placeSt:]
    
    while(placeSt > 10) :
        placeEnd = placeSt = temp.find('"')
        songURL =  'http://www.azlyrics.com' + temp[:placeEnd]
        
        #global calls                                   ################
        #if(calls >= 90):                               # manage the calls made no mare than few threads a time
        #    calls = 0
        #    time.sleep(1)                              # to fool the server into thinking that the data is being requested by human
        #    while(threading.activeCount() > 1):
        #        pass
       
        #calls += 1

        threading.Thread(target=process, args = (songURL,)).start()
        placeSt = temp.find('<a href="..') + 11
        temp = temp[placeSt:]
    #temporary
    while(threading.activeCount() > 1):
        pass
    #check that threads have ended before return
    return occur

def process(songURL):
    t = retrieve(songURL).text
    t = t [t.find("licensing agreement. Sorry about that. -->") + 42 : t.find("<!-- MxM banner -->")]
    tempCount = t.count(curse)
    global occur
    occur += tempCount
    print tempCount   #debug
    print songURL

#make sure you have a VPN running
# Inside Insti Things
# or run this
# "handleErr.bat" will do the work for you (Windows)
print artist 
print curse
print SortArtist(artist)
