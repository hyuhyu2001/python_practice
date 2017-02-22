#!/user/bin/env python
#encoding:utf-8

import pickle
import nester
man=[]
other=[]
new_man = []
new_other = []
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
    with open('man_data.txt','rb') as man_file:
        new_man = pickle.load(man_file)
    with open('other_data.txt','rb') as other_file:
        new_other = pickle.load(other_file)
except IOError as err:
    print('file error:' + str(err))
except pickle.PickleError as perr:
    print('Pickle eror:' + str(perr))

nester.print_lol(new_man)
nester.print_lol(new_other)
