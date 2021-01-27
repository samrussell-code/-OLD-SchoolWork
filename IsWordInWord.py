w1=input("Enter first word:\n").upper();word1Length=len(w1);w2=input("Enter second word:\n").upper();matchingLength=0
for x in w2:
    if x in w1:
            matchingLength+=1
if matchingLength==word1Length:
    print(w1,"can be made from",w2+"!\n")
else:
    print(w1,"cannot be made from",w2+"!\n")