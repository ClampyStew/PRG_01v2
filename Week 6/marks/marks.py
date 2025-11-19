position = 0
listno = 1
name = ''
score = ''
namelist = []
scorelist = []
path = "'[PATH]'"
fulllist = open(path+"marks.txt", 'r')
mainlist = fulllist.read()
mainlist = mainlist.split("\n")

while position < len(mainlist):
    name[listno], score[listno] = mainlist[position]
    namelist.append(name[listno])
    scorelist.append(score[listno])
    position += 1
    listno += 1
