import requests
import time
from notify_run import Notify 
headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}





import os

def initScreen():
    width = os.get_terminal_size().columns
    print("-"*width)
    print("\n")
    print("WORKHORSE - By adikeshri(https://github.com/adikeshri)\n".center(width))

    print("This script will notify you on the availability of vaccine in your district/pincode. Please fill out the details correctly. \nIf you want to stop the script execution at any point of time, simply press Ctrl+C to exit.\n")
    print("-"*width)



def horizontalLine():
    width = os.get_terminal_size().columns
    print("-"*width)




def stopExecution():


    horizontalLine()
    print("Wrong selection, exiting ...")
    exit()


    

initScreen()
print("\n1.Check by Pincode \n2.Check by District")
checkerType=int(input("Enter either 1 for pincode or 2 for district:" ))

if checkerType!=1:
    stopExecution()

shouldGetPushNotifications=input("Do you also want to be notified on your phone via push notifications?(y/n)": )


if(shouldGetPushNotifications.lower()!="y" or shouldGetPushNotifications.lower()!="n"):
    stopExecution()

print("\n1.18+ \n2.45+ \n3.Both")
ageGroup=int(input("Enter either 1 for 18+ slots or 2 for 45+ slots or 3 for any:" ))

if ageGroup!=1 or ageGroup!=2 or ageGroup!=3:
    stopExecution()






print("\n1.Dose 1 \n2.Dose 2")
doseType=int(input("Enter 1 for dose 1 or 2 for dose 2: "))

if doseType!=1 or doseType!=2:


    stopExecution()
if checkerType==1:
    controller.findByPincode(shouldGetPushNotifications.lower(),ageGroup,doseType)
else:
    controller.findByDistrict(
        shouldGetPushNotifications.lower(),ageGroup,doseType
    )
    # print("-"*50)
    # print("Calling cowin api")
    # response=requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=97&date=10-05-2021",headers=headers)
    # if response.status_code!=200:
    #     print("API call failed")
    #     time.sleep(5)
    #     continue
    # jsonResp=response.json()
    # sessions=jsonResp["sessions"]
    # availSessionsFor18 = []
    # for session in sessions:
    #     if session["min_age_limit"]!=45:
    #         availSessionsFor18.append(session)
    # if availSessionsFor18 !=[]:
    #     print("Slots available")
    #     print(availSessionsFor18)
    #     for availSessions in availSessionsFor18:
    #         notify = Notify()
    #         print(availSessions["vaccine"] + " available at " + availSessions["name"] + " on " + availSessions["date"])
    #         notify.send(availSessions["vaccine"] + " available at " + availSessions["name"] + " on " + availSessions["date"])
    # else:
    #     print("No slot available right now!")
    # time.sleep(5)
