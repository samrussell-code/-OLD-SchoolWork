value=int(input("Enter integer (0-99):\n"))
operation=str(input("Calculate additive or multiplicative persistence (a or m)?\n"));count=0
while value>9:
    if operation=="a":
        value=(value/10)+(value%10)
    else:
        value=(value/10)*(value%10)
    count+=1
print("The persistence is:",count)