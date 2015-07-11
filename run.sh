#!/bin/bash
# Author: Sergey Kostenko
# File for Insight Data Engineering
# Running WordCount and RunningMedian

# Set permission for the directory
chmod 777 src

# Changing directory to src
cd ./src

# Set proper permissions
echo "Setting proper permissions..."
chmod 777 words_tweeted.py
chmod 777 median_unique.py

#installing Tweepy
#pip install Tweepy

# Compile and run Word Count
echo "Run Words Tweeted..."
python words_tweeted.py

# Compile and run Running Median
echo "Run Running Median..."
python median_unique.py

echo "Done!"
