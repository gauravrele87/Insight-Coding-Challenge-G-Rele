# example of program that calculates the number of tweets cleaned
#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import json
    

def escapeChar(tweetText):
    tweetText = tweetText.replace("\r","").replace("\n","")
    tweetText = tweetText.replace("\/","/").replace("\t","")
    tweetText = tweetText.replace('\"','"').replace("\'","'")
    return tweetText


def tweetClean(ospath,filename,outputFname):
    count = 0
    
    #reading one line at a time from the input file tweets.txt
    for line in open(os.path.join(ospath,filename)):    
        tweets = json.loads(line)
        
        #If the current tweet has errors (not all the variables have been passed)
        #then skip the current tweet'''
        if len(tweets) < 25:
            continue
        
        #cleaning the tweets
        tweets["text"] = escapeChar(tweets["text"])
        textTweet = tweets["text"]
        creationTweet = tweets["created_at"]
        
        #tweets are in unicode so converting the tweets to ascii
        if textTweet.encode('ascii','ignore').decode('ascii') != textTweet:
            count = count+1   
        textTwConv = ''.join([x for x in textTweet if ord(x) < 128])
        creationTwConv = ''.join([x for x in creationTweet if ord(x) < 128])
        textTwConv = textTwConv.encode('ascii','ignore')
        creationTwConv = creationTwConv.encode('ascii','ignore')
        
        
        with open(os.path.join(ospath,outputFname),'a') as opWrite:
            opWrite.write(textTwConv + " (timestamp: "+ creationTwConv + ")\n")
            
    #Writing the number of lines with unicode        
    if count == 1:
        textUnicode = " tweet contained unicode.\n"
    else:
        textUnicode = " tweets contained unicode.\n"        
    with open(os.path.join(ospath,outputFname),'a') as opWrite:
        opWrite.write("\n" + str(count) + textUnicode)   
    


if __name__ == "__main__":
    #Input and output file names 
    filename = "tweet_input/tweets.txt"
    outputFname = 'tweet_output/ft1.txt'
    ospath = os.getcwd() 

    #function for calculating avg degree in a graph
    tweetClean(ospath,filename,outputFname)
       
