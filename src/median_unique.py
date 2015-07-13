#median_unique.py

# author Sergey Kostenko

#Calculate the median number of unique words per tweet, 
#and update this median as tweets come in.

import bisect

#paths to files
read_path = '../tweet_input/tweets.txt'
write_path = "../tweet_output/ft2.txt"
    

#This function calculates median for the file. The reason I wrote my own function
#vs using numpy.median() is that numpy.median() sorts array even in case if it is
#already sorted. And it take a lot of time.
def median(array):
    if len(array)%2 !=0:
        return array[len(array)/2]
    return (array[len(array)/2-1] + array[len(array)/2])/2.0
            
try:
    with open(read_path) as inf, open(write_path, 'a') as outf:
        array = []
        #for every line (tweet) in the file
        for line in inf:
            #find amount of unique words in the tweet
            k = len(set(line.split()))
            #insert amount of unique words into the array in the sorted fashion
            bisect.insort_left(array, k)
            #write current median of the array into the file
            result = "{:.2f}\n".format(median(array))
            outf.write(result)
except IOError as e:
    print 'Operation failed: %s' % e.strerror
