#!/usr/bin/python3



#////////////////////////////////////////////////////////////////////////////////
# AUTHOR:   Robert Morouney
# EMAIL:    robert@morouney.com
# FILE:     make data.py
# CREATED:  2016-11-28 17:35:16
# MODIFIED: 2016-11-30 16:53:33
#////////////////////////////////////////////////////////////////////////////////
MAX_CHAR = 255
MIN_CHAR = 0

MIN_TIME = 10
MAX_TIME = 5000

import math

def gaus_norm(x, MIN, MAX):
    return (float(x - MIN)/float(MAX-MIN))

with open("./robert_stroke.log", 'r') as fin:
    write_str = ''
    print('CHAR\t-->\tTIME\t-->\tCHAR')
    for i, line in enumerate(fin):

        time, char = line.split(',')
        time, char = int(time), int(char)
        if i == 0 :
            last_char = char
            continue
        if time > MAX_TIME or time < MIN_TIME:
            print('time error value found, skipping')
            continue
        else:
            with open('./normal_strokesPOS.log', 'a') as fout:
                new_time = gaus_norm(time, MIN_TIME, MAX_TIME)
                new_char = gaus_norm(char, MIN_CHAR, MAX_CHAR)
                new_last_char = gaus_norm(last_char, MIN_CHAR, MAX_CHAR)
                print("{},{},{}".format(new_last_char, new_time, new_char), file=fout)
                print("{}\t-->\t{}\t-->\t{}".format(last_char, time, char))
                print("{}\t-->\t{}\t-->\t{}".format(new_last_char, new_time, new_char))
                last_char = char
