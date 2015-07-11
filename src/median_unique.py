#median_unique.py
#Calculate the median number of unique words per tweet, 
#and update this median as tweets come in.

# author Sergey Kostenko


import numpy

#paths to files
read_path = '../tweet_input/tweets.txt'
write_path = "../tweet_output/ft2.txt"

try:
    with open(read_path) as inf, open(write_path, 'a') as outf:
        array = []
        #for every line (tweet) in the file
        for line in inf:
            #append amount of unique words to the array
            array.append(len(set(line.split())))
            #write current median of the array to the file
            result = "{:.2f}\n".format(numpy.median(array))
            outf.write(result)
except IOError as e:
    print 'Operation failed: %s' % e.strerror
