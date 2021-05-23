class Controller:
    def findByPincode(shouldGetPushNotifications,ageGroup,doseType):
        print("Enter your pincode, you can enter upto 5 pin codes seperated by commas, eg: 800026,562157:", end="")
        pincodes = list(map(int, input().split(",")))
        repository.findByPincode(pincodes, shouldGetPushNotifications,ageGroup,doseType)

    def findByDistrict(shouldGetPushNotifications,ageGroup,doseType):
        repository.findByDistrict(shouldGetPushNotifications)