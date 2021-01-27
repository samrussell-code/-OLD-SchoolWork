inputNum = int(input("Enter your full ISBN number"))
inputNum=str(inputNum)
multiplier=1;numTotal=0

for x in range(0,12):
    tempNum=int(inputNum[x])*multiplier

    numTotal=numTotal+tempNum
    if multiplier==1:
        multiplier=3
    else:
        multiplier=1

        remainder=numTotal%10;checkDigit=10-remainder;print(checkDigit)
