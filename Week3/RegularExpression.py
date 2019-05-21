import re
import datetime

class RegEx:
    def RegularExp(self):
        string = "Hello <<user-name>>,we have your full name as <<full-name>> in our system."
        name = input("Enter name:")
        string_one = re.sub("<<user-name>>", name, string)
 # Check if the string has any characters from a to z lower case, and A to Z upper case:

        x = re.findall("[a-zA-Z]", name)

        if (x):
         """print(str1)"""
        else:
          print("Enter valid name")

        fullname = input("Enter your full name: ")

        first_name, last_name = fullname.split(" ")
        # Check if the string has any characters from a to z lower case, and A to Z upper case:

        x1 = re.findall("[a-zA-Z]", fullname)

        if (x1):
          string_two = re.sub("<<full-name>>", fullname, string_one)
        else:
              print("Enter valid name")

        mob_string = "Your contact number is 91-xxxxxxxxxx."
        mobile_number = input("Enter mobile number : ")

        if re.match(r'[789]\d{9}$', mobile_number):
         new_mobile_num = str(mobile_number)
         new_string = re.sub("xxxxxxxxxx", new_mobile_num, mob_string)
        else:
          print("Enter valid mob no")
          exit()

        date_string = "please, let us know in case of any clarification Thank you BridgeLabs,on <<Today>>-XX/XX/XXXX. "

        date = datetime.date.today()  # date.today is display the today date
        replace_date = str(date)
        day = date.strftime("%A")  # this method is used to display the day in full name .
        day1 = re.sub("<<Today>>", day, date_string)
        bridge_lab = re.sub("XX/XX/XXXX", replace_date, day1)
        # print(bridge_lab, "\n")

        print(string_two, new_string)
        print(bridge_lab)





if __name__ == '__main__':
    obj = RegEx()
   # string = "Hello <<name>>, \nWe have your full" + " name as <<full name>> in our system. Your contact number is 91­xxxxxxxxxx." + "\nPlease,let us know in case of any clarification. \nThank you \nBridgeLabz xx/xx/xxxx."
    obj.RegularExp()
