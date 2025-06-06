#For the Sleepy Librarian
total = 0
finelist = []
booklist = []
position = 0
intduelist = []
floatfinelist = []

path = "C:\\Users\\Zhe Kai\\PRG_01v2\\MiniTask02\\"
fulllist = open(path+"overduebooks.txt", 'r')
mainlist = fulllist.read()
mainlist = mainlist.split("\n")
list1, list2, list3 = mainlist[0:3]
fulllist.close()

book1, due1 = list1.split(";")
book2, due2 = list2.split(";")
book3, due3 = list3.split(";")
booklist = [book1, book2, book3]
duelist = [due1, due2, due3]


while True:
    booktitle = str(input("Enter book title (or type 'stop' to finish): "))
    booklist.append(booktitle)
    if booktitle == "stop":
        booklist.pop(-1)
        break
    else:
        daysoverdue = str(input("Enter days overdue: "))
        duelist.append(daysoverdue)


intduelist = []
i = 0
while i < len(duelist):
    intdue = int(duelist[i])
    intduelist.append(intdue)
    i += 1

while position < len(duelist):
    if float(duelist[position]) < 5:
        fines = (float(intduelist[position])*0.50)
        finelist.append(fines)
        position += 1
    elif float(duelist[position]) < 10:
        fines = (float(intduelist[position])*1)
        finelist.append(fines)
        position += 1
    elif float(duelist[position]) > 10:
        fines = (float(intduelist[position])*1.5)
        finelist.append(fines)
        position += 1

floatfinelist = []
x = 0
while x < len(finelist):
    floatfine = float(finelist[x])
    floatfinelist.append(floatfine)
    x += 1


total = sum(floatfinelist)

print("Total books processed: {}\nOverall total fine amount: ${:.2f}".format((len(booklist)), total))

finesreport = open(path+'fines_report.txt', 'w')

position = 0
while position < len(booklist):
    if intduelist[position] > 10:
       glare = "-.-"
    else:
        glare = ""
    finesreport.write("{} {} - ${:.2f} {}\n".format(booklist[position],intduelist[position],floatfinelist[position], glare))
    position += 1
finesreport.close()



