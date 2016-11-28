#////////////////////////////////////////////////////////////////////////////////
# AUTHOR:   Robert Morouney
# EMAIL:    robert@morouney.com 
# FILE:     csv-key.py
# CREATED:  2016-11-27 17:44:33
# MODIFIED: 2016-11-27 17:57:41
#////////////////////////////////////////////////////////////////////////////////


with open('dsl.csv', 'r') as fin:
    for line in fin: 
        vals = line.split(',')
        with open('./logs/'+vals[0], 'a') as fout:
            for i,c in enumerate(".tie5Roanl"):
                print("{},{}".format(ord(c),int((float(vals[3+(i*3)])+float(vals[4+(i*3)]))*1000)), file=fout)
