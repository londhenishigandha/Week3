import json

from Week3.InventoryInfo import stock_dateTime_Transaction


class Date_Time_Transaction:
    try:
        with open("dateTime.json","r") as content:
            new_file = content.read()
            content.close()
            item = json.loads(new_file)
            d1 = stock_dateTime_Transaction(item)
            print()
            d1.date_and_Time()
    except Exception as e:
        print(e)