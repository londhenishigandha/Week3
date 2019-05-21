import json

from Week3.InventoryInfo import Inventory_Stock_Management

# t1 = Inventory_Stock_Management()



class Inventory_Prog_4:
    try:
        with open("Inventorydata4.json", "r") as file:
            new_file = file.read()
            file.close()

            item = json.loads(new_file)
            t1 = Inventory_Stock_Management(item)
            print()
            t1.inventory_Stock_Data()

    except RuntimeError:
        print("=========")
