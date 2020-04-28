# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 19:14:43 2019

@author: lynst
"""

# First we must import the time package

import time

# Initialize a variable named 'stopwatch'
stopwatch = input('How many seconds will you need: ')

# Convert to an integer
time_int = int(stopwatch)

# Create a message
print('Start the timer now')
time.sleep(time_int)
print('Stop the timer now')

