path = "C:\\Users\\Zhe Kai\\PRG_01v2\\Week 5\\ToDO\\"
todolist = open(path+'todolist.txt', 'r')
todolist = todolist.readlines()
title, task1, task2 = todolist[0:3] 
title = title.strip()
task1 = task1.strip()
task2 = task2.strip()
print(f'{title}{'\n'}{task1}{'\n'}{task2}')