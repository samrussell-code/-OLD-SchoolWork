
import os, shutil,time,datetime;currentDir=os.getcwd();print("**Place this script in the root folder of your server**\n")

worldName=str(input("Enter world folder name: \n"));backupInterval=int(input("Enter backup interval in minutes: \n"))
backupTimeList=[];deletionInterval=int(input("Enter deletion interval in hours:\n"))

def CreateBackup(worldName,backupTimeList):
    now=datetime.datetime.now().time()
    currentTime=now.strftime("%H.%M.%S")
    backupName=worldName+"_"+str(currentTime)
    print("Backing up now to",backupName,"...")
    shutil.make_archive(backupName, 'zip', worldName)
    print("Backup Complete!\n")

    backupTimeList.append(currentTime)
    global currentHour
    currentHour=currentTime[0:2]


def DeleteBackup(backupName,backupTimeList,listItem):
    backupPath=str(backupName)+".zip";os.remove(backupPath)
    backupTimeList.remove(listItem);print("Deleted old backup - ",backupName)
    

while True:
    time.sleep(60*backupInterval);    CreateBackup(worldName,backupTimeList)
    
    for x in backupTimeList:
        saveHour=x[0:2]
        if int(currentHour)!=int(saveHour) and int(currentHour)%deletionInterval==0:
            backupName=worldName+"_"+x
            DeleteBackup(backupName,backupTimeList,x)
        