from util import *
fname = "input1"
#fname = "1example"

lines = readlines(fname)
ints = readlinesints(fname)
#ints = ints(words(read(fname)))
#

ints = []
for x in lines:
    n=0
    for c in x:
       if c in "0123456789":
           n+=10*int(c)
           break
    for c in x[::-1]:
       if c in "0123456789":
           n+=int(c)
           break
    ints += [n]
print(sum(ints))

# part 2
digits=["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]+["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
m = [1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9]
ints = []
for l in lines:
    #print(l)
    tens=0
    units=0
    min_pos = len(l)
    for i,d in enumerate(digits):
        pos = l.find(d)
        if pos < 0: continue
        if pos < min_pos:
            min_pos=pos
            tens = m[i]
    max_pos =-1
    for i,d in enumerate(digits):
        pos = l.rfind(d)
        if pos < 0: continue
        if pos > max_pos:
            max_pos=pos
            #print(i, d)
            units = m[i]
    ints += [tens*10+units]

print(sum(ints))
