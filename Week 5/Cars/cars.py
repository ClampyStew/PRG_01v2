path = "C:\\Users\\Zhe Kai\\PRG_01v2\\Week 5\\Cars\\"
carsdoc = open(path+"cars.txt", 'r')
mainlist = carsdoc.read()
subs = mainlist.replace("Fesla Corp\n***Price List***", '')
subs = subs.split("\n")
car1, car2, car3, car4 = subs[1:5]
print(f'{"1: "}{car1}{"\n"}{"2: "}{car2}{"\n"}{"3: "}{car3}{"\n"}{"4: "}{car4}')

car1, carprice1 = car1.split(" : ")
car2, carprice2 = car2.split(" : ")
car3, carprice3 = car3.split(" : ")
car4, carprice4 = car4.split(" : ")

#adding to list for both the cars and their prices
carlist = car1, car2, car3, car4
pricelist = carprice1, carprice2, carprice3, carprice4
ordernumber = input("Enter the order number: ")

#Customer Info
custname = input("Customer Name: ")
carchoice = int(input("Enter car choice: "))
carlistchoice = carchoice - 1
carchosen = carlist[carlistchoice]
caractprice = pricelist[carlistchoice]

receipt = open(path+"{}.txt".format(ordernumber), 'w')
receipt.write("{} ordered the {} at the price of {}.".format(custname, carchosen, caractprice))
print("Car has been successfully ordered.")