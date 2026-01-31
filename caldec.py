from decimal import*

item1=Decimal(.70)
rate1=Decimal(1.05)
tax1=item1*rate1
total1= item1 + tax1
item = .70
rate = 1.05
tax = item * rate
total = item + tax 
print("item and item1:\t", "%.20f" % item, item1)
print("tax and tax1:\t", "%.20f" % tax, tax1)
print("total and total 1:\t", "%.20f" % total, total1)

