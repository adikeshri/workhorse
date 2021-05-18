import requests
import time
from notify_run import Notify 

headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

while True:
    print("-"*50)
    print("Calling cowin api")
    response=requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id=97&date=10-05-2021",headers=headers)
    if response.status_code!=200:
        print("API call failed")
        time.sleep(5)
        continue

    jsonResp=response.json()


    sessions=jsonResp["sessions"]


    availSessionsFor18 = []

    for session in sessions:
        if session["min_age_limit"]!=45:
            availSessionsFor18.append(session)

    if availSessionsFor18 !=[]:
        print("Slots available")
        print(availSessionsFor18)
        for availSessions in availSessionsFor18:
            notify = Notify()
            print(availSessions["vaccine"] + " available at " + availSessions["name"] + " on " + availSessions["date"])
            notify.send(availSessions["vaccine"] + " available at " + availSessions["name"] + " on " + availSessions["date"])
    else:
        print("No slot available right now!")
    time.sleep(5)
