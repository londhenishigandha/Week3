import datetime
import json

from Week2.UtilityStack import Test_LinkedList
from Week2.UtilityStack import Test_Stack

q1 = Test_Stack()
s1 = Test_Stack()
a1 = Test_LinkedList()


class Test_Oops:
    @staticmethod
    def inventory_information(item):
        # print(item)
        print("===========================================================\n")
        print("************Displaying Inventory Information**************\n")
        # print("**Rice_Name-------Rice_Weight-------Rice_price.....**")
        print("====================================================")

        update_Rice = {}
        update_Wheat = {}
        update_Pulses = {}

        for i, j, k in zip(item["Rice"], item["Wheat"], item["Pulses"]):  # zip() is used access element of lists
            r_name = i['name']                                            # rice name,price,update_rice
            r_price = i['price']
            update_Rice[r_name] = r_price

            w_name = j['name']                                             # rice name,price,update_rice
            w_price = j['price']
            update_Wheat[w_name] = w_price

            p_name = k['name']                                             # rice name,price,update_rice
            p_price = k['price']
            update_Pulses[p_name] = p_price

        print()                                                         # printing the information
        print("Rice information.....", update_Rice)
        print("Total Rice Items......", len(update_Rice))
        print("Sum of Rice Items.......", "Rs.", sum(update_Rice.values()))  # printing the sum of rice information
        print()
        print("Wheat information.....", update_Wheat)
        print("Total Wheat Items......", len(update_Wheat))
        print("Sum of Wheat Items.......", "Rs.", sum(update_Wheat.values()))  # printing the sum of wheat information
        print()
        print("Pulses information.....", update_Pulses)
        print("Total Pulses Items......", len(update_Pulses))
        print("Sum of Pulses Items.......", "Rs.", sum(update_Pulses.values())) # printing the sum of pulses information




"""===============Inventory_Management======================"""


class Inventory_Stock_Management:

    def __init__(self, data):
        self.data = data

    def inventory_Stock_Data(self):

        while True:
            try:
                count = 1
                while count > 0:
                    print()
                    print("Enter 1.Display 2.Add_item 3.exit..\n")
                    choice = int(input())
                    if choice == 1:
                        print("displaying inventory information...\n")
                        # t1.inventory_information(self.data)
                        print("***************Rice Details***************\n")
                        print("Name            weight       price")
                        print("=====================================")
                        for i in self.data['Rice']:
                            print(i['name'], end="          ")
                            print(i['weight'], end="          ")
                            print(i['price'], )
                        print()
                        print("***************Wheat Details***************\n")
                        print("Name           weight         price")
                        print("=====================================")
                        for j in self.data['Wheat']:
                            print(j['name'], end="          ")
                            print(j['weight'], end="          ")
                            print(j['price'], )
                        print()
                        print("***************Pulses Details***************\n")
                        print("Name           weight        price")
                        print("=====================================")
                        for k in self.data['Pulses']:
                            print(k['name'], end="          ")
                            print(k['weight'], end="          ")
                            print(k['price'], )
                        print()
                    elif choice == 2:
                        print("Enter Item Name(Rice,Wheat,Pulses)..\n")
                        item = input()
                        i = 0
                        """while i < len(self.data)
                            if self.data[i]["Rice"] == item.title():"""
                        while not item.isalpha():
                            print("enter valid item name(Characters Only)...\n")
                            print("Enter Item Name(Rice,Wheat,Pulses)..\n")
                            item = input()
                        print()

                        print("enter a name of given item:=> ", item)
                        name = input()
                        while not name.isalpha():  # name of a item
                            print("enter valid name for a item(Characters Only)...\n")
                            print("enter a name of given item:=> ", item)
                            name = input()
                        print()

                        print("enter a weight of given item:=> ", item, " item_name ", name)
                        weight = input()
                        while not weight.isdigit():  # weight of a item
                            print("enter weight for a item(Integer Only)...\n")
                            print("enter weight of given item:=> ", item, "item_name ", name)
                            weight = input()
                        print()

                        print("enter a price of a given item:=> ", item)
                        price = input()
                        while not price.isdigit():  # price of a item
                            print("enter price for a item(Integer Only)...\n")
                            print("enter a price of given item:=> ", item, " item_name ", name)
                            price = input()
                        print()

                        with open("Inventory_Data4.json", "w") as file:
                            self.data[item].append({
                                "name": name,
                                "weight": weight,
                                "price": price
                            })
                            file.write(json.dumps(self.data, indent=2))
                            file.close()

                    elif choice == 3:
                        exit()
                    else:
                        print(" sorry,invalid entry...\n")
            except Exception as e:
                print(e)

class Test_Stock_Report:
    def __init__(self):
        try:
            #self.data = None
            with open("Stockreport.json", "r") as file:
                json_file = file.read()
                data = json.loads(json_file)
        except FileNotFoundError:
            print("sorry,you are searching file is not found...\n")
        self.data = data

    def  stock_report(self):
        total_stock_flipkart = 0
        total_stock_amazon = 0

        print("=================Total shares of Two Companies==========")
        print()
        print("*****************Flipkart Shares************************")
        for g in self.data["Flipkart"]:
            print("total shares Flipkart:", g['name'], "is:", g['shares'] * g['price'])
            total_stock_flipkart += g['shares'] * g['price']
        print()
        print("*****************Amazon Shares************************")

        for a in self.data["Amazon"]:
            print("total shares Amazon :", a['name'], "is:", a['shares'] * a['price'])
            total_stock_amazon += a['shares'] * a['price']
        print()

        print("..............Stock information..............")
        print("Total Number of Flipkart Stocks...", total_stock_flipkart)

        print("Total Number of Amazon Stocks...", total_stock_amazon)

######################################################################################################
class stock_Linked_list:
    def __init__(self, data):
        self.data = data

    def add_companyShares(self):
        i = 0
        for i in range(len(self.data['Stock Report'])):
            a1.addNode(self.data['Stock Report'][i]["Number of Share"])
        print("**************displaying Company Shares*******")
        a1.PrintNode()
        print()
        print("**************size Of Company Shares *******")
        print(a1.getSize())
############################################################################################################
class stock_Account_Shares:
    try:
        def __init__(self):
            with open("Stock.json", "r") as stock_jf:
                stock_jf = json.load(stock_jf)  # load() convert file into python from json
                self.stock_jf = stock_jf
            with open("Customer.json", "r") as person_json_value:
                person_json_value = json.load(person_json_value)  # read customer json file
                self.person_json_value = person_json_value

        """===============view_Shares()======================"""

        def view_shares(self):
            """
                This method display the all shares record
                return: nothing
            """
            for i in range(len(self.stock_jf['Stock Report'])):
                print(i, "\t", self.stock_jf['Stock Report'][i])

        def check_validity(self):

            """
                This method provide user interface to customer as well as admin.
                It gives different options to sell and buy shares.
                :return: nothing
            """

            print("*********** Welcome **************")
            i = 0
            # print(self.person_json_value)
            name = input("Enter Username :")
            print(name)
            while i < len(self.person_json_value["Person"]):
                # title() method returns a copy of the string in which
                # first characters of all the words are capitalized.
                if self.person_json_value["Person"][i]["Name"] == name.title():
                    index = i
                    print(self.person_json_value["Person"][i])  # print all data of customer
                    print("....Login successful....")

                    # provide options
                    print("enter following choices to process further...\n")
                    c = int(input("1.Buy shares\n2.Sell shares\n3.Exit\n"))
                    if c == 1:
                        self.buy_share(index)  # for buying shares
                    elif c == 2:
                        self.sell_share(index)  # for selling shares
                    elif c == 3:
                        exit(0)
                    else:
                        # in case of user entered wrong input display following message
                        print("oops wrong input.....\n")

                i += 1

        def add_new_company(self):
            """
                This method used to add new company into stock it can only
                done by admin.
                :return: nothing
            """

            try:
                name = str(input("Enter company name: "))
                while not name.isalpha():
                    print("please enter company name should be (Character only)..\n")
                    print("Enter company name:..\n")
                    name = str(input())
                print()
                number = int(input("Enter Number of share: "))

                print()
                price = int(input("Enter Price per Share..\n"))

                new_stock_dict = {"Stock Name": name,  # add at new index in stock report
                                  "Number of Share": number,
                                  "Share Price": price}

                with open('Stock.json', 'w') as stock_jf:
                    self.stock_jf['Stock Report'].append(new_stock_dict)  # append updated data into stocks

                    stock_jf.write(json.dumps(self.stock_jf, indent=2))
            except ValueError:
                print("please enter valid input...\n")
            except FileNotFoundError:
                print("please enter correct file input...\n")

        def buy_share(self, index):
            """
                This method used to buy share from stocks its calculate the
                all stock price which is purchased by user.
            :param index:
            :return: nothing
            """
            try:
                for i in range(len(self.stock_jf['Stock Report'])):
                    print(i, self.stock_jf['Stock Report'][i])  # print stock data

                # taking input from user
                print('\nEnter Which Company Share you want to buy')
                choice = int(input("Enter company index number:-> "))
                """while not choice > len(self.stock_jf['Stock Report']) - 1:
                    print("invalid input(Only numbers)")
                    print("Enter the choice(0-", len(self.stock_jf['Stock Report']) - 1, ")to buy company share")
                    choice = int(input())"""
                buy_share = int(input("Enter Number of Share You want to buy:-> "))
                each_share_price = self.stock_jf['Stock Report'][choice]['Share Price']
                amount_pay = buy_share * each_share_price  # calculate total purchased share price

                # checks balance before purchase. if balance enough then proceed else terminate
                if self.person_json_value['Person'][index]["Total Balance"] > amount_pay:

                    print("Total amount you have to pay for ", buy_share, " stocks :", amount_pay)
                    updated_stock_share = self.stock_jf["Stock Report"][choice]["Number of Share"] - buy_share

                    # update stocks after purchasing
                    with open("Stock.json", "w") as jf:
                        self.stock_jf["Stock Report"][choice]["Number of Share"] = updated_stock_share
                        jf.write(json.dumps(self.stock_jf, indent=2))

                    person_updated_balance = self.person_json_value['Person'][index]["Total Balance"] - amount_pay
                    print('Now Your Updated Balance is ', person_updated_balance)
                    person_updated_share = self.person_json_value['Person'][index]['Number of Share'] + buy_share
                    print('Now Your Updated Number of share is ', person_updated_share)

                    # update customer data also
                    with open("Customers.json", "w") as jf:
                        self.person_json_value['Person'][index]['Total Balance'] = person_updated_balance
                        self.person_json_value['Person'][index]['Number of Share'] = person_updated_share
                        jf.write(json.dumps(self.person_json_value))
                else:

                    # if customer don't have enough balance then print following message
                    print("You Don't have enough money ")

            except ValueError:
                print("Enter valid input...\n")

        def sell_share(self, index):
            """
                This method used to sell share from customer stocks its calculate the
                    all stock price which is sold by user.
                :param index:
                :return:nothing
            """

            print('Enter choice to sell your share to particular company')
            for i in range(len(self.stock_jf['Stock Report'])):
                print(i, self.stock_jf['Stock Report'][i])  # print stock report

            choice = int(input("Enter choice (company index):-> \n"))

            print('Enter Number of share you want to sell to', self.stock_jf['Stock Report'][choice]['Stock Name'],
                  'company')
            sell_share = int(input("Number of shares to sell:-> "))
            updated_stock_share = self.stock_jf["Stock Report"][choice]["Number of Share"] + sell_share

            # update stock report data
            with open("Stock.json", "w") as jf:
                self.stock_jf["Stock Report"][choice]["Number of Share"] = updated_stock_share
                jf.write(json.dumps(self.stock_jf, indent=2))  # write updated data into stock report

            # calculate updated person shares
            updated_person_share = self.person_json_value['Person'][index]["Number of Share"] - sell_share

            person_share_price = int(input("price for per share you want from company"))
            person_updated_balance = self.person_json_value['Person'][index][
                                         "Total Balance"] + person_share_price * sell_share
            # print all transaction data
            print(' --> ', person_share_price * sell_share, '<--will be Added to your total balance')
            print('Now Your Updated Balance is ', person_updated_balance)

            print('Now Your Updated Number of share is ', updated_person_share)

            # update customer data also
            with open("Customers.json", "w") as jf:
                self.person_json_value['Person'][index]['Total Balance'] = person_updated_balance
                self.person_json_value['Person'][index]['Number of Share'] = updated_person_share
                jf.write(json.dumps(self.person_json_value, indent=2))

    except Exception as e:
        print(e)
        ###############################################################################################

class stock_dateTime_Transaction:
    def __init__(self, data):
        self.data = data

    def date_and_Time(self):
        my_list = []
        for i in range(len(self.data['datetime'])):
            str1 = self.data['datetime'][i]['result'] + "-" + self.data['datetime'][i]['Number of Share'] + " Transaction Date & Time..... " + self.data['datetime'][i]['date_time']
            my_list.append(str1)
            # print(my_list)
        for i in my_list:
            a1.addNode(i)
        print()
        print("---------  DateTime of the transactions ------\n")
        a1.PrintNode()
        print()

    print()

