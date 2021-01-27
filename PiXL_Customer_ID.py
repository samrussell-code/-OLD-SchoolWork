
validInput=False
quit=False

while validInput==False and quit==False:
    try:
        validInput=True
        userForename=input("Enter your first name:\n").title()
        if userForename=="quit":
            break
    except:
        print("Incorrect data format entered.\n")
        validInput=False


validInput=False
while validInput==False and quit==False:
    try:

        validInput=True
        userSurname=input("Enter your last name:\n").title()
        if userSurname=="quit":
            break
    except:
        print("Incorrect data format entered.\n")
        validInput=False

validInput=False
while validInput==False and quit==False:
    try:
        validInput=True
        userDate=int(input("Enter a date format DDMMYYYY:\n"))
        if userDate=="quit":
            break
    except:
        print("Incorrect data format entered.\n")
        validInput=False

if quit==False:
    ID=(str(userDate)+str(userSurname[0])+str(userSurname[1])+str(userSurname[2])+str(userForename[0])+str(len(userForename)))
    print(ID)