listA = []
listB = []

with open('input.txt', 'r') as file:
    for line in file:
        itemA, itemB = line.split()
        listA.append(int(itemA))
        listB.append(int(itemB))

listA.sort()
listB.sort()

answerOne = 0
for itemA, itemB in zip(listA, listB):
    answerOne += abs(itemA-itemB)

answerTwo = 0
for itemA in listA:
    instances = listB.count(itemA)
    answerTwo += (itemA * instances)

print(f"Answer one: {answerOne}")
print(f"Answer two: {answerTwo}")