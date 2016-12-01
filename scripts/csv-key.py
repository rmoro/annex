#////////////////////////////////////////////////////////////////////////////////
# AUTHOR:   Robert Morouney
# EMAIL:    robert@morouney.com 
# FILE:     csv-key.py
# CREATED:  2016-11-27 17:44:33
# MODIFIED: 2016-11-28 01:34:53
#////////////////////////////////////////////////////////////////////////////////

password = [47,17,34,14,23,56,15,31,0,45,36]

with open('dsl.csv', 'r') as fin:
    for line in fin: 
        vals = line.split(',')
        with open('./logs/'+vals[0], 'a') as fout:
            for i,c in enumerate(password):
                idx = 3 * (i+1)
                dwell = float(vals[idx])
                flight = float(vals[idx+1])
                dt = int( (dwell + flight)*1000 )
                print("{},{}".format(dt, c), file=fout)
