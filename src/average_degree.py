#!/usr/bin/python
# -*- coding: utf-8 -*-
# example of program that calculates the average degree of hashtags

import os
import json
import re
import itertools
from collections import defaultdict

'''tweets["entities"]["hashtags"] does not work since the txt file doesnt have
the hashtags in there even though there are hashtags in the text. However it 
has been implemented nevertheless but there is a regex method included as a 
comment as well 
Hashtags have been encoded to ascii just in case unicode contains any non-
ascii chars.
Asked ronak if i could use timestamp_ms for ease in calculations'''


def updateList(lists,timestamp):
    newList = []
    for rows in lists:
        if rows[1] > (timestamp - 60000):
            newList.append(rows)
    return newList
    
def makeEdges(lists):
    edges = []
    for rows in lists:
        for pair in itertools.permutations(rows,2):
            edges.append(pair)
    return edges


def tweetAvgDegree(ospath,filename,outputFname):
    listing = []
    #reading one line at a time from the input file tweets.txt
    for line in open(os.path.join(ospath,filename)):    
        tweets = json.loads(line)  #output is of type dict
        
        '''If the current tweet has errors (not all the variables have been passed)
        then skip the current tweet and label the avg degree as zero'''    
        if len(tweets) < 25:
            avgDegree = 0
            with open(os.path.join(ospath,outputFname),'a') as opWrite:
                opWrite.write("{0:0.2f}".format(avgDegree) + "\n")
            opWrite.close()
            continue
        
        #cleaning the tweets
        twCreation = tweets["created_at"].encode('ascii','ignore')
        twTimestamp = int(tweets["timestamp_ms"].encode('ascii','ignore'))
        twText = tweets["text"].encode('ascii','ignore')
         
        #twTextHash = re.findall('#(\w+)',twText)  
        #Regex method for getting hashtags from the tweets["text"]
         
        #Getting Hashtags from the tweets
        twTextHash = [hashtag["text"] for hashtag in tweets["entities"]["hashtags"]]
        twTextHash = [lists.encode('ascii','ignore') for lists in twTextHash]
        
        #updating the list with all the tweets within 60 seconds
        listing.append([twCreation,twTimestamp,twTextHash])
        newList = updateList(listing,twTimestamp)
        
        #updated hashtags from the new List    
        hashtags = [row[2] for row in newList if row[2]!=[]]
        
        #Using Edges from makeEdges, convert them into dictionary and count them
        graphEdges = makeEdges(hashtags)
        dictHashtags = defaultdict(list)
        for key,value in graphEdges:
            dictHashtags[key].append(value)
        
        #Although this could have been done with dictHashtags, I preferred it 
        #to be more clear 
        lenHashtags = {}
        for keys,values in dictHashtags.items():
            lenHashtags[keys] = len(values)
            
        #Calculate the average degree 
        avgDegree = 0
        sumHashtags = sum(lenHashtags.values())
        sumHashtags = "{0:0.2f}".format(sumHashtags)
        if len(lenHashtags)>0:
            avgDegree = float(sumHashtags)/len(lenHashtags)
        listing = newList
        
        #write the avg. degree into the output file with 2 decimal places
        with open(os.path.join(ospath,outputFname),'a') as opWrite:
            opWrite.write("{0:0.2f}".format(avgDegree) + "\n")
            
if __name__ == "__main__":
    #Input and output file names 
    filename = "tweet_input/tweets.txt"
    outputFname = 'tweet_output/ft2.txt'
    ospath = os.getcwd() 

    #function for calculating avg degree in a graph
    tweetAvgDegree(ospath,filename,outputFname)
    
    



			
