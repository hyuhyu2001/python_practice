#!/user/bin/env python
#encoding:utf-8

import os
os.chdir('/Users/king/Documents/nester/HeadFirstPython/chapter3')
try:
    data = open('sketch.txt')
    for each_line in data:
        #if not each_line.find(':')==-1:
        try:
            (role,line_spoken) = each_line.split(':',1)
            print(role,end='')
            print(' said:',end='')
            print(line_spoken,end='')
        except ValueError:
            pass
    data.close()
except IOError:
    print('the date file is missing!')

