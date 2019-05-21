import json


from Week3.InventoryInfo import Test_Oops
t1 = Test_Oops()


class Inventory_Management:

    try:
        with open("Inventory_Data1.json", "r") as file:
            # print(json.loads(file.read())) # loads deserializes as string
            # print(json.load(file)          # load deserializes as fp (file pointer)
            jason_File = file.read()
            file.close()

            item = json.loads(jason_File)

            t1.inventory_information(item)
    except RuntimeError:
        print("oops something went wrong..\n")

"""

Rice information..... {'Basmati Rice': 50, 'Brown Rice': 55}
Total Rice Items...... 2
Sum of Rice Items....... Rs. 105

Wheat information..... {'Spelt': 66, 'Durum': 59}
Total Wheat Items...... 2
Sum of Wheat Items....... Rs. 125

Pulses information..... {'Mung bean': 69, 'Moth bean': 89}
Total Pulses Items...... 2
Sum of Pulses Items....... Rs. 158

Process finished with exit code 0
"""