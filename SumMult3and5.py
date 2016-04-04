
maxValue = 1000
storeValueThree = set()
storeValueFive = set()
storeValue = set()
sum = 0

for x in range(3,maxValue,3):
        storeValueThree.add(x)

for y in range(5,maxValue,5):
        storeValueFive.add(y)

storeValue = list(storeValueThree.union(storeValueFive))

for i in range(0,len(storeValue)):
    sum = sum + storeValue[i]

print(storeValueFive)
print(storeValueThree)
print(sum)
