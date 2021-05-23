from datetime import date
class Common:

    def getCurrentDate():
        today = date.today()
        # dd-mm-YY
        return today.strftime("%d-%m-%Y")