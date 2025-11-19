
position = 0
cmsg = []
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
'o','p','q','r','s','t','u','v','w','x','y','z',' ']

spy_code = ['alpha','bravo','cipher','delta','echo','falcon','ghost','hawk','intel',
'joker','knight','link','matrix','nova','omega','phantom','quake','raven','shadow',
'tango','ultra','viper','wolf','xray','yankee','zealot','space']

f = "'[PATH]'"
document = open(f+"SpyMessage.txt", 'r')
message = document.read()
message = message.lower()
document.close()

while len(cmsg) < len(message):
    index = message[position]
    letterpos = letters.index(index)
    codeword = spy_code[letterpos]
    cmsg.append(codeword)
    position += 1
if len(cmsg) == len(message):
    i = 0
    while i < len(cmsg):
        print(cmsg[i])
        i += 1
        
