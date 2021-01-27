
import random
import time
print("## Welcome to Make 15! ##\n## Your goal is to reach 15 using the 9 cards on the deck. ##\n## If you go over or the CPU beats you there, you lose ##\n")
time.sleep(2)
while True:
    print("--------## GAME START ##--------")
    deck=[1,2,3,4,5,6,7,8,9]; print(deck)
    userDeck=[]
    cpuDeck=[]
    userTotal=0
    cpuTotal=0
    safePickupCard=999
    deckSize=len(deck)

    while (cpuTotal<15 and userTotal<15):

        validUserPickup=False
        while validUserPickup==False:
            validUserPickup=True
            try:
                userPickup=int(input("Pick a remaining card on table:\n"))
                deck.remove(userPickup);    userDeck.append(userPickup);    userTotal=sum(userDeck);                    
            except:
                print("Enter one of the numbers on the table.")
                validUserPickup=False

                
        deckSize=len(deck)
        if userTotal<15:
            if 15-cpuTotal in deck:
                print("CPU Chooses ",(15-cpuTotal))
                deck.remove(15-cpuTotal)
                cpuDeck.append(15-cpuTotal)
            elif ((15-userTotal) in deck) and (15-userTotal)+cpuTotal<=15:
                print("CPU Chooses ",(15-userTotal))
                deck.remove(15-userTotal)
                cpuDeck.append(15-userTotal)
            else:

                
                cpuPickup=deck[random.randint(1,deckSize-1)]
                if cpuTotal+cpuPickup>15:
                    for x in range (0,deckSize-1):
                        cpuPickup=deck[x]
                        if cpuTotal+cpuPickup<16:
                            safePickupCard=cpuPickup
                    if safePickupCard+cpuTotal<16:
                        cpuPickup=safePickupCard
                    else:
                        cpuPickup=deck[random.randint(1,deckSize-1)]
                        

                
                print("CPU Chooses ",cpuPickup,"\n\n");   deck.remove(cpuPickup);   cpuDeck.append(cpuPickup)
            cpuTotal=sum(cpuDeck);  safePickupCard=999
            
        print("CPU Deck: "+str(cpuDeck)+"                     USER Deck: "+str(userDeck)+"\n\nCPU Total: "+str(cpuTotal)+"                          USER Total: "+str(userTotal)+"\n\nTable Deck: "+str(deck))
        
    if userTotal==15:
        print("PLAYER WON!")
    elif cpuTotal==15:
        print("CPU WON!")
    else:
        if userTotal>15:
            print("CPU WON (By player going over 15)...")
        else:
            print("PLAYER WON (By CPU going over15)...")

