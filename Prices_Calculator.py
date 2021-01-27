import time
itemNameList=[]
itemCostList=[]
itemNumber=len(itemNameList)
itemNameList.append(input("Enter product name, or 'none' to stop adding:\n").title())
while "None" not in itemNameList:

    validInput=False
    while validInput==False:
        validInput=True
        try:
            itemCostList.append(float(input("Enter cost of "+str(itemNameList[itemNumber])+" in £:\n")))
        except:
            validInput=True
            print("Enter a valid price")
    itemNumber=len(itemNameList)
    itemNameList.append(input("Enter product name:\n").title())



itemNameList.remove("None")

mostExpensiveItemPos=itemCostList.index(max(itemCostList))
leastExpensiveItemPos=itemCostList.index(min(itemCostList))

newItemList=[]
for item in itemCostList:
    if item>50:
        item=item*0.95
    item=item*1.2
    item=round(item, 2)
    stringItem=str(item)
    if "." == stringItem[-2]:
            item=str(item)+"0"
    else:
            item=str(item)
    newItemList.append(item)
itemCostList=newItemList

calculationList=[]
for i in range(len(itemCostList)):
    calculationList.append(float(itemCostList[i]))


print("Final costs of items is:  "+str(itemCostList))
print("Total costs of items is:  £"+str(sum(calculationList)))
priceyItem=str((itemCostList[mostExpensiveItemPos]))
cheapyItem=str((itemCostList[leastExpensiveItemPos]))
if "." == priceyItem[-2]:
    print("Most expensive:  "+itemNameList[mostExpensiveItemPos],"£"+str(itemCostList[mostExpensiveItemPos])+"0")
if "." == cheapyItem[-2]:
    print("Least expensive:  "+itemNameList[leastExpensiveItemPos],"£"+str(itemCostList[leastExpensiveItemPos])+"0")
if "." != priceyItem[-2]:
    print("Most expensive:  "+itemNameList[mostExpensiveItemPos],"£"+str(itemCostList[mostExpensiveItemPos]))
if "." != cheapyItem[-2]:
    print("Least expensive:  "+itemNameList[leastExpensiveItemPos],"£"+str(itemCostList[leastExpensiveItemPos]))

averageCost=round((sum(calculationList))/(itemNumber), 2)
print("Average Cost:   £"+str(averageCost))
while True:
    time.sleep(120)
