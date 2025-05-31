prices = [ ["kopi", 0.4], 
           ["teh", 0.4], 
           ["milo", 0.5], 
           ["soft drinks", 1.20] ]
path = "C:\\Users\\Zhe Kai\\PRG_01v2\\Week 5\\DrinkPrice\\"
pricelist = open(path + "PriceList.txt",'w')
price1, price2, price3, price4 = prices[0:]
price1 = str(price1)
price2 = str(price2)
price3 = str(price3)
price4 = str(price4)
print(price1, price2, price3, price4)
fprice1 = price1.replace("['kopi', 0.4]", "kopi: $0.40")
fprice2 = price2.replace("['teh', 0.4]", "teh: $0.40")
fprice3 = price3.replace("['milo', 0.5]", "milo: $0.50")
fprice4 = price4.replace("['soft drinks', 1.2]", "soft drinks: $1.20")
pricelist.write(f"{fprice1}{"\n"}{fprice2}{"\n"}{fprice3}{"\n"}{fprice4}")
pricelist.close()