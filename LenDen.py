print("\n\t** Welcome to LenDen **")

admin_info = {}
user_info = {}

class LenDen:
    def __init__(self):
        self.admin_info = admin_info
        self.user_info = user_info

    def home(self):
        while True:
            print("\n\n***LenDen Home***\n")
            print("Admin        >> Press 1: ")
            print("LenDen User  >> Press 2: ")
            print("Exit         >> Press 0: ")

            try:
                option = int(input("Choose option : "))
                break
            except:
                print("invalid option chosen !")
                continue
        return option


    def admin_create_account(self, id , password):
        self.admin_id = id
        self.admin_pass = password
        self.admin_login_ = False

        self.admin_info[id] = [password, id, self.admin_login]


    def admin_login(self):
        print("\n***Admin Login Panel***\n")
        count = 0
        for i in range(3):
            try:
                admin_id = int(input("\nEnter ID No. : "))
            except:
                print("Wrong input !")
                
            admin_id_list  = list(object_.admin_info.keys())
            if admin_id in admin_id_list:
                break
            if count == 2:
                print("Try after some times")
                break
            print("ID not exist")
        for admin_id_ , info in admin_info.items():
            if admin_id == admin_id_:
                for i in range(3):
                    admin_pass = input("Enter password : ")
                    if admin_pass == info[0]:
                        print("\nAdmin Login Successfull")
                        info[2] = True

                        while True:
                            print("\n\n***Admin panel***\n")
                            print("Search an User   >>press 1: ")
                            print("All user List    >>press 2: ")
                            print("Exit             >>press 0: ")

                            try:
                                option = int(input("Choose option : "))
                            except:
                                print("Invalid option chosen !")
                            
                            if option == 1:
                                try:
                                    user_phone_no = int(input("\nEnter User phone number : "))
                                except:
                                    print("\nInvalid input.")
                                object_.search_an_user(user_phone_no)

                            elif option == 2:
                                print("\n___User info___\n")
                                for info in user_info.values():
                                    print(f"Name        :  {info[2]}")
                                    print(f"Gender      :  {info[3]}")
                                    print(f"Phone No    :  {info[5]}")
                                    print(f"Password    :  {info[0]}")
                                    print(f"Balance     :  {info[4]}")
                                    print("\n\n")
                            
                            elif option == 0:
                                break

                            else:
                                print("Invalid option chosen !")
                            
                        break
                    else:
                        print("\nWrong password given")

                    if i == 3:    
                        print("Try after some times")
    

    def search_an_user(self, user_phone_no):
        self.user_phone_no = user_phone_no
        phone_no_list = list(object_.user_info.keys())
        if user_phone_no in phone_no_list:
            for ph_no , info in user_info.items():
                if user_phone_no == ph_no:
                    print("\n___User info___\n")
                    print(f"Name        :  {info[2]}")
                    print(f"Gender      :  {info[3]}")
                    print(f"Phone No    :  {info[5]}")
                    print(f"Password    :  {info[0]}")
                    print(f"Balance     :  {info[4]}")
        else:
            print("This number not registered. ")


    def user_home(self):
        while True:
            print("\n\n***User Panel***\n")
            print("Create an account : Press 1: ")
            print("Login account     : Press 2: ")
            print("Exit              : Press 0: ")

            try:
                option = int(input("Choose option : "))
            except:
                print("invalid option chosen !")
                continue
            
            if option == 1:
                object_.user_create_account()

            elif option == 2:
                object_.user_login()

            elif option == 0:
                break

            else:
                print("Invalid option chosen")


    def default_user_account(self, name, phone_no, password, gender, balance = 50):
        self.name = name
        self.phone_no = int(phone_no)
        self.password = password
        self.gender = gender.lower()
        self.balance = balance
        self.login = False

        self.user_info[self.phone_no] = [self.password, self.login, self.name, self.gender, self.balance, self.phone_no]          
    

    def user_create_account(self):
        # self.count = count
        # track = count
        # print(track)
        print("\n***Create account panel***\n")

        self.name = input("Enter you name : ")
        while True:
            try:
                self.phone_no = int(input("Enter phone number : "))
                break
            except:
                print("Enter valid number")
        self.password = input("Enter password : ")
        self.gender = input("Enter gender : ").lower()
        self.balance = 50
        self.login_ = False

        self.user_info[self.phone_no] = [self.password, self.login_,self.name,self.gender,self.balance,self.phone_no] 
        print("\nAccount created successfuly",end="")


    def user_login(self):
        print("\n***Login panel***\n")

        for i in range(3):
            try:
                phone_no = int(input("Enter phone number : "))
            except:
                print("Invalid input")
            phone_no_list = list(object_.user_info.keys())
            if phone_no in phone_no_list:
                break
            else:
                print("\nUnregistered number\n")
            if i == 2:
                object_.home()
        for ph_no , info in user_info.items():
            if phone_no == ph_no:
                for i in range(3):
                    password = input("Enter password : ")
                    if password == info[0]:
                        print("\nLogin Successfull.",end=" ")
                        if info[3] == 'male':
                            print(f"Mr. {info[2]}.")
                        else:
                            print(f"Miss. {info[2]}.")
                        info[1] = True

                        while True:
                            print("\n ***Lenden account***\n")
                            print("Check Balance   >> Press 1 :")
                            print("Send money      >> Press 2 :")
                            print("Cash Out        >> Press 3 :")
                            print("Cash In         >> Press 4 :")
                            print("Profile         >> Press 5 :")
                            print("Log Out         >> Press 6 :")

                            try:
                                option = int(input("Choose Option : "))
                            except:
                                print("\nInvalid Option")
                            
                            if option == 1:
                                print(f"\nYour current balance {info[4]}tk.")
                            
                            if option == 2:
                                print("\n__Send money__\n")
                                try:
                                    receiver_phn_no = int(input("Enter receiver phone number : "))
                                except:
                                    print("\nGiven input not valid\n")
                                    continue
                                phone_no_list = list(object_.user_info.keys())
                                if receiver_phn_no in phone_no_list:
                                    while True:
                                        try:
                                            amount = int(input("\nEnter send amount : "))
                                        except:
                                            print("\nInvalid input")
                                            print("Try again\n")
                                        if info[4] - amount >= 5:
                                            info[4] -= amount + 5
                                            self.send_money(receiver_phn_no,amount)
                                            break
                                        else:
                                            print("\nYou have no sufficient amount\n")
                                else:
                                    print("\nThe number is not registered\n")
                            
                            if option == 3:
                                print("\n__Cash Out__\n")
                                while True:
                                    try:
                                        amount = int(input("Enter amount : "))
                                    except:
                                        print("\nType Error")
                                        print("Try again")
                                    tax_amount = amount / 1000
                                    tax_amount *= 20
                                    totall_amount = amount + tax_amount
                                    if info[4] - totall_amount >= 0:
                                        info[4] -= totall_amount
                                        break
                                    else:
                                        print("You have no sufficient amount")
                                print("\nCash out successfull\n")
                            
                            if option == 4:
                                print("\n__Cash In__\n")
                                while True:
                                    try:
                                        amount = int(input("Enter amount : "))
                                    except:
                                        print("\nType Error")
                                        print("Try again")
                                    info[4] += amount
                                    break
                                print("\nCash In successfull\n")

                            if option == 5:
                                print("\n__Profile__\n")
                                print(f"Name     : {info[2]}")
                                print(f"Phone no : {info[5]}")
                                print(f"Password : {info[0]}")
                                print(f"Gender   : {info[3]}")
                                print(f"Balance  : {info[4]}")
                                print(f"Log in   : {info[1]}")

                            if option == 6:
                                info[1] == False
                                print(f"Log out done.", end=" ")
                                if info[3] == 'male':
                                    print(f"Mr. {info[2]}.")
                                    break
                                else:
                                    print(f"Miss. {info[2]}.")
                                    break    
                        break                    
                        
                    else:
                        print("\nPassword Incorrect")

                    if i == 2:
                        print("Try again latter")
                


    def send_money(self, receiver_phn_no, amount):
        self.receiver_phn_no = receiver_phn_no
        self.amount = amount
        for ph_no , info in user_info.items():
            if receiver_phn_no == ph_no:
                info[4] += amount
                print("\nMoney send successfully\n")

        
counter = 0
while True:
    object_ = LenDen()
    counter += 1
    if counter == 1:
        object_.admin_create_account(1271, 'aayan17')
        object_.default_user_account('Ayan', '01515', '12345', 'male', 50)
        object_.default_user_account('Tom H', '01517', '12345', 'male', 100)
        object_.default_user_account('Mitu', '01518', '12345', 'female', 50)
        object_.default_user_account('Shanto', '01519', '12345', 'male', 200)
        object_.default_user_account('Julie', '01520', '12345', 'female', 500)

    option = object_.home()

    if option == 1:
        object_.admin_login()
    elif option == 2:
        object_.user_home()
    elif option == 0:
        print("Thanks for using")
        break
    else:
        print("Invalid option chpsen !")



# ************** Happy Coding Life ***************