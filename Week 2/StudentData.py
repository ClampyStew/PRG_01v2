path = 'C:\\Users\\Clampy\\PRG1v2\\PRG_01v2\\Week 2\\'
sourcefile = open(path+'StudentData.txt','r')
info1 = sourcefile.readlines(1)
info3 = sourcefile.readlines(3)
info5 = sourcefile.readlines(5)
total = (info1, info3, info5)
strings = ' '.join([' '.join(inner) for inner in total]) 
#I hate you python, thanks stackabuse, article is here:https://stackabuse.com/bytes/error-sequence-item-0-expected-str-instance-x-found-in-python/
cleanstrings = strings.rstrip()
print(cleanstrings)


