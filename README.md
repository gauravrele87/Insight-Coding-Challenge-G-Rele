Insight Data Engineering - Coding Challenge - Gaurav Rele
===========================================================

## Details of Implementation

run.sh has been updated to run both the files. The original program was run on 64-bit windows using spyder anaconda IDE with python 2.7. The os.path for windows is different which is commented out of both files. It uses the new os.getcwd() which was run on centos 6 linux OS. 
I have tried to explain the code with comments for every section.

# tweets_cleaned.py

tweets_cleaned.py will clean the tweets that are imported from the text file and outputs the text and timestamp to the file ft1.txt

- Dependencies: 
os
json



# average_degree.py

average_degree.py will use hashtags from the tweets that are imported from the text file and outputs the avg degree to the file ft2.txt

- Dependencies: 
os
json
re (unused since the line is commented out yet useful)
itertools
collections import defaultdict
