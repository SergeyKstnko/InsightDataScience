#words_tweeted.py
#Calculate the total number of times each word has been tweeted.

# author Sergey Kostenko

from collections import Counter

#paths to files
read_path = '../tweet_input/tweets.txt'
write_path = "../tweet_output/ft11.txt"

#count how many times each word is used
try:
    with open(read_path) as inf:
        wordsCount = Counter(word for line in inf for word in line.split())
except IOError as e:
    print 'Operation failed: %s' % e.strerror
    
with open(write_path, 'a') as outf:
    #iterate over sorted list of keys and write them in the file
    for word in sorted(wordsCount.iterkeys()):
        string = "{:<18}\t\t\t{}\n".format(word, wordsCount[word])
        outf.write(string)    
