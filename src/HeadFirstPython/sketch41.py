#!/user/bin/env python
#encoding:utf-8

#import os
#os.chdir('/Users/king/Documents/nester/HeadFirstPython/chapter3')
import nester

man = []
other = []
try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role,line_spoken) = each_line.split(':',1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('the date file is missing!')
try:
    man_file = open('man_data.txt','w')
    other_file = open('other_data.txt','w')
    print(man,file=man_file)
    print(other,file=other_file)
except IOError:
    print('file error')
finally:
    if 'man_file' in locals():
        man_file.close()
    if 'other_file' in locals():
        other_file.close()
try:
    with open('man_data.txt','w') as man_file:
        nester.print_lol(man,fh=man_file)
    with open('other_data.txt','w') as other_file:
        nester.print_lol(other,fh=other_file)
except IOError as err:
    print('file error:' + str(err))
