#For Q2

PlayerStat = (input("Enter player's reputation and item price:"))
PlayerStat = PlayerStat.split(";")
PlayerRep = int(PlayerStat[0])
PriceItem = float(PlayerStat[-1])

if PlayerRep >= 20:
    PriceItem = (PriceItem*(0.9))
elif (PlayerRep < 20) and (PriceItem >= 200):
    PriceItem = (PriceItem*(0.95))
else:
    PriceItem

print(f'{"Price to pay: "}{"$"}{PriceItem:.2f}')