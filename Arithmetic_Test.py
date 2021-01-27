import random, time, os, glob #random to generate questions, time to get the date/time for writing, os to get the current directory, glob to filter for txt files in the directory

def GetAnswer(num1,num2): #subroutine that generates both the operator to use for the question (using 2 random numbers generated earlier), and the answer for that question.
    operatorNum=random.randint(1,4)
    if operatorNum==1:
        print(num1,"+",num2,"=\n")
        answer=num1+num2
    elif operatorNum==2:
        print(num1,"-",num2,"=\n")
        answer=num1-num2
    elif operatorNum==3:
        print(num1,"*",num2,"=\n")
        answer=num1*num2
    else:
        badGen=True
        while badGen==True:
            try:
                badGen=False
                answer=round((num1/num2), 2)              
                if num1%num2!=0: #extra stuff to make sure division questions are simple - the only way to break the generator cycle is to get an answer with no remainder.
                    loopbreaker=42069/0
                print(num1,"/",num2,"=  \n")
            except:
                num1=GetRandInt()
                num2=GetRandInt()
                badGen=True
    return answer

def GetRandInt(): #generates the two random numbers
    return random.randint(-12,12)

######### Program output begins here
username=str(input("Enter your name:\n").title())
totalCorrect=0 #score counter for questions answered correctly, used later on to show the user and store

for x in range(0,10):
    num1=GetRandInt();num2=GetRandInt()
    correctAnswer=GetAnswer(num1,num2)
    
    ######################################## -PROOFING
    validInput=False
    while validInput==False:
        try:
            validInput=True
            userGuess=float(input(""))
        except:
            validInput=False
            print("Make sure to enter a number!")
      ########################################

    if userGuess==correctAnswer:
        print("Correct answer.")
        totalCorrect+=1
    else:
        print("Incorrect. The answer was",correctAnswer)
print("\n"+username+", you got",totalCorrect,"out of 10 correct!\n")

#adding the new information to a text file, to then be sorted later on.
usernameFile=str(username)+".txt"
fileManager=open(usernameFile,"a")
getTime=time.ctime()
sentence=str(totalCorrect)+" out of 10 achieved by "+str(username)+" on - "+str(getTime)+"\n"
fileManager.write(sentence)
fileManager.close()

#collecting this information back into variables in the program for sorting
def GetLineScore(line):
    if line[0]=="1" and line[1]=="0":
        score=10
    else:
        score=line[0]
    return score

fileReader=open(usernameFile,"r")
numberOfLines = len(fileReader.readlines())
fileReader.seek(0)#resets file pointer back to start of file

scoreList=[]
previousData=False
previousData2=False
for x in range(0,numberOfLines):#stores each lines string data, score data, original position in list, and new position in list.
    if x==0:
        line1=fileReader.readline()
        score1=GetLineScore(line1)
        scoreList.append(score1)
        scoreList[0]=int(scoreList[0])
    elif x==1:
        previousData=True
        line2=fileReader.readline()
        score2=GetLineScore(line2)
        scoreList.append(score2)
        scoreList[1]=int(scoreList[1])
    elif x==2:
        previousData2=True
        line3=fileReader.readline()
        score3=GetLineScore(line3)
        scoreList.append(score3)
        scoreList[2]=int(scoreList[2])
    elif x==3:
        line4=fileReader.readline()
        score4=GetLineScore(line4)
        scoreList.append(score4)
        scoreList[3]=int(scoreList[3])
fileReader.close()

#time to use those extracted scores to order the lines on write.

sortedScoreList=sorted(scoreList)
listLen=len(scoreList)


firstLine=scoreList.index(sortedScoreList[listLen-1])
secondLine=scoreList.index(sortedScoreList[listLen-2])
################################################# -Making sure script doesn't break if the user hasn't entered 3 sets of data yet.
try:
    thirdLine=scoreList.index(sortedScoreList[listLen-3])
except:
    print("")
if previousData==True:
    if previousData2==True:
        try:
            lineDataList=[line1,line2,line3,line4]
        except:
            lineDataList=[line1,line2,line3]
    else:
            lineDataList=[line1,line2]
else:
    lineDataList=[line1]
##################################################

#rewrite the file with the new data

fileManager=open(usernameFile,"w")
fileManager.write(lineDataList[firstLine])
if previousData==True:
    fileManager.write(lineDataList[secondLine])
if previousData2==True:
    try:
        fileManager.write(lineDataList[thirdLine])
    except:
        print("\nKeep trying again and entering data until your top 3 attempts can be stored!\n")
fileManager.close()

###

userList=[];path = os.path.dirname(os.path.realpath(__file__));os.chdir(path) #creates a variable called path that is set to the name of the 'real' path to the script, then changes the directory to that variable
for file in glob.glob("*.txt"): #use glob to only include files ending in .txt
    userList.append(file)
userList.sort

for x in userList:
    userPrintout=open(x,"r")
    print("#############-- "+str(x)+ " --#############\n")
    for line in x:
        tempLine=userPrintout.readline()
        print(tempLine)
#sleep so results can be viewed
time.sleep(30)