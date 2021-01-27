#A corridor has 17 rooms 1-17, princess sleeps in a different room each night.
#on the first night of 365 days she sleeps in a random room, always moves one room up or down per night.
import random 
cycles=1
cycleCount=int(input("Enter the number of cycles you want the program to do (normally produces ~750 cycles/second:\n"))
daycountList=[]
while cycles<=cycleCount:
    cycles=cycles+1
    def PRINCESS_START_ROOM():
        randomRoom=random.randint(1,17)
        return randomRoom

    guess=False; daycount=1; princessRoom=PRINCESS_START_ROOM(); userRoomGuess=1; prevRoomGuess=0

    while guess==False:

    
        if userRoomGuess==princessRoom:
            print("Your guess (Room "+str(userRoomGuess)+") was correct!\nYou took "+str(daycount)+" day(s) to find her."); guess=True
            daycountList.append(daycount)
            resultsFile=open("results.txt","a")
            resultsFile.write("Guessed "+str(userRoomGuess)+" in "+str(daycount)+" days.\n")
            resultsFile.close()

        else:
            daycount=daycount+1
            if princessRoom==1:
                princessRoom=2
            elif princessRoom==17:
                princessRoom=16
            else:
                UpOrDown=random.randint(0,1) #0 for down, 1 for up
                if UpOrDown==1:
                    princessRoom=princessRoom+1
                else:
                    princessRoom=princessRoom-1
            if userRoomGuess==17:
                if prevRoomGuess==9999:
                    userRoomGuess=16
                    prevRoomGuess=17
                else:
                    prevRoomGuess=9999
                    userRoomGuess=17
            elif userRoomGuess==1:
                prevRoomGuess=1
                userRoomGuess=2
            elif prevRoomGuess>userRoomGuess:
                prevRoomGuess=userRoomGuess
                userRoomGuess=userRoomGuess-1
            elif prevRoomGuess<userRoomGuess:
                userRoomGuess=userRoomGuess+1
totalSum=sum(daycountList)
mean=totalSum/cycleCount
meanSentence=("The average number of guesses was "+str(mean))
maxSentence=("The highest number of guesses was "+str(max(daycountList)))
resultsFile=open("results.txt","a")
resultsFile.write(meanSentence+"\n"+maxSentence)
resultsFile.close()
print(meanSentence+"\n"+maxSentence)