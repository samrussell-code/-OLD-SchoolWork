#A corridor has 17 rooms 1-17, princess sleeps in a different room each night.
#on the first night of 365 days she sleeps in a random room, always moves one room up or down per night.
import random;

def PRINCESS_START_ROOM():
    randomRoom=random.randint(1,17)
    return randomRoom

guess=False; daycount=1; princessRoom=PRINCESS_START_ROOM()

while guess==False:

    if daycount==365:
        daycount=1; princessRoom=PRINCESS_START_ROOM()

    print("Day "+str(daycount));    userRoomGuess=int(input("Guess the princess' new room:\n"))

    if userRoomGuess==princessRoom:
        print("Your guess (Room "+str(userRoomGuess)+") was correct!\nYou took "+str(daycount)+" day(s) to find her."); guess=True
    else:
        print("Your guess (Room "+str(userRoomGuess)+") was incorrect!"); daycount=daycount+1
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