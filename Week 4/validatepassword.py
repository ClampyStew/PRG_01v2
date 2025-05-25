import re

userpwd = (input("Enter password: "))
digitcheck = bool(re.findall("[0-9]",userpwd))
UCcheck = bool(re.findall("[A-Z]", userpwd))
lencheck = len(userpwd)
if lencheck < 8:
    print("Password must be at least 8 characters long.")
elif digitcheck == False:
    print("Password must contain at least one digit")
elif UCcheck == False:
    print("Password must contain at least one uppercase letter.")
else:
    print("Password is valid.")