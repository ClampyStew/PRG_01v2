CommSales = int(input("Enter monthly sales of sales agent:"))

if CommSales < 10000:
    CommRate = (5)
else:
    CommRate = (10)

if CommRate == 5:
    CommPay = (CommSales*(5/100))
else:
    CommPay = (CommSales*(10/100))

print(f'{"The Commission Rate is :"}{CommRate}{"%"}{"\nThe Commission paid is :"}{"$"}{CommPay:.2f}')