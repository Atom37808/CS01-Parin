Num = int(input('Enter loop count'))
NumTotal = []
for i in range(Num):
    data = int(input('Enter number'))
    NumTotal += [data]
print(NumTotal[0])
print(NumTotal[-1])