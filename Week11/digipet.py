menu = ['Feed','Play','Rest','Status']
status = [3,3,3]
title = ['hungry','happiness','energy']
msg = ['Nom nom nom','XD','Zzzzz']

print('Digipet')
while True:
    for i in range(len(menu)):
        print('{{}} {}'.format(i+i, menu(i)))
    selection = int(input('Please select an option: '))

    if selection == 4:
        for i in range(len(status)):
            state = ''
            for s in range(status[i]):
                state = state + 