class cowinApis:
    def __init__(self):
        self.headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    def findNextSevenDaysByDistrict(districtId,date):
        apiUrl="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=" +str(districtId) + "&date=" + str(date)
        response=requests.get(apiUrl, headers=self.headers)
        return response

    def getStates():
        response=request.get("https://cdn-api.co-vin.in/api/v2/admin/location/states",headers=self.headers)
        return response

    def getDistricts(stateId):
        apiUrl="https://cdn-api.co-vin.in/api/v2/admin/location/districts/" + str(stateId)
        response=requests.get(apiUrl,headers=self.headers)
        return response



    def findNextSevenDaysByPinCode(pinCode,date):
        apiUrl="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=" +str( pindCode  ) + "&date=" + str(date)
        response=requests.get(apiUrl, headers=self.headers)
        return response