from datetime import datetime
from datetime import date


def correct_empty(data):
    if data:
        today = date.today()
        if not data["time"]:
            now = datetime.now()
            data["time"] = now.strftime("%H:%M")
            print("Nice")
        if not data["email"]:
            data["email"] = "noname@noname.com"
        if not data["date"]:
            data["date"] = today.strftime("%d.%m.%Y")
        if not data["year"]:
            data["year"] = today.strftime("%Y")
        if not data["firstname"]:
            data["firstname"] = "Николай"
        if not data["surname"]:
            data["surname"] = "Яшин"
    return data
