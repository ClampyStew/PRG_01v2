#For Decisions... Decisions... Decisions...

import random

temp = float(input("Enter the current temperature: "))
botmood = ["bored", "sad", "happy", "excited", "angry"]

if temp > 30:
    action = "go to the beach to enjoy the sun"
elif temp < 0:
    action = "go to the moon to escape the cold"
else: 
    action = "stay home and relax with a cup of coffee"

moodnow = botmood[random.randint(0,4)]

print("The temperature for today is {} degree Celcius so I will {}. I am feeling very {} now".format(temp, action, moodnow))