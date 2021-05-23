

from notify_run import Notify 
class Repository:




    def __init__(self):
        self.api=cowinApis()
        self.common=Common()

    def findByPincode(pincodes, shouldGetPushNotifications,ageGroup,doseType):




        if shouldGetPushNotifications:
            try:
                notify = Notify()
                notify.send("Test run")
            except:
                os.popen(
                    "notify-run register"
                )
                print("Scan the above QR code with your mobile, go to the url an click on subscribe button. Then allow it to send ush notifications")



           
        while True:
            date=self.common.getCurrentDate()
            for pincode in pincodes:
                resp=apis.findNextSevenDaysByPinCode(pincode, date)



                if resp.status_code!=200:
                    print("An error occured whn trying to reach cowin servers, don't worry, trying again...")
                    continue
                response=resp.json()
                centers=response["centers"]


                for center in centers:
                    for session in center["sessions"]:
                        if ageGroup==1:
                            session["available_capacity_dose1"]>0:
                            print()