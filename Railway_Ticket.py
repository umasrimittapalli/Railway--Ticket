
import random
# AVAIABLE TRAIN LIST 
class Railwaysticket:
    def __init__(self):
     
      self.Trains_details = {
                     "warangal":[12342,"Hyderbad","kakatiya express",300, 40],
                     "Visakhapatnam":[23859,"Triupathi","Simhapuri Express", 400 ,45],
                    "vijawada":[17016,"Secunderabad","Vande Bharat Express" , 1500, 20]
                }
      self.Passengers=[]
    
    def Show_trains(self):  
      print(format("from","<30"),format("to","<30"),format("Trains Number","<30"),format("Trains Name","<30") ,format("price","<10"),format("seats left","<10"))
      for i,j in self.Trains_details.items():
        print(format(i,'<30'),format(j[1],"<30"),format(j[0],"<30"),format(j[2],"<30"),format(j[3],"<11"),format(j[4],"<10"))
        
      
# ticket booking 
    def book_ticket(self):
      self.Show_trains()
      Train_number = None
      Matched_train = None
      from_station = None
      while True:
        try:
            Train_number= int(input("\nEnter the Train number:"))
            Num_tickets = int(input("Enter NUmber of Tickets:"))
            for station,details in self.Trains_details.items():
              if details[0] == Train_number :
                Matched_train =details
                from_station =station
                break
            if Matched_train is None:
                print("Inavlid Train number , Please try again")
                continue
            

                
######### Passengers Details #############
            if Num_tickets > Matched_train[4]:
                    print(" Not enough seats available.")
                    return
            pnr_list =[]
            self.Passengers.clear()
       
            for tickets in range(Num_tickets):
                    print(f"\nEnter details for Passenger {tickets + 1}:")
                    Name=input("Enter your Name:")
                    if not Name:
                        raise ValueError("Nmae cannot be Empty")
                    Age = int(input("Enter your Age"))
                    if Age <= 0 or  Age >120:
                        raise ValueError("Invalid Age")
                    Gender = input("Enter your Gender: M / F :")
                    if Gender not in ["M","F"]:
                        raise ValueError("Please select Valide Gender")
                    Mobile = input("Enter your Phone number:")
                    if not Mobile or len(Mobile) != 10 or not Mobile.isdigit():
                        raise ValueError("Invalid Mobile NUmber")
                    PNR = random.randint(100000, 999999)
                    pnr_list.append(PNR)
                    self.Passengers.append({
                        "Name": Name,
                        "Age": Age,
                        "Gender": Gender,
                        "Phone": Mobile,
                        "PNR": PNR
                    })
                     
            print("\n--- Passenger Details ---")
            for passenger in self.Passengers:
                print(f"Name: {passenger['Name']}, Age: {passenger['Age']}, Gender: {passenger['Gender']}, Phone: {passenger['Phone']}")
            amount = Matched_train[3]* Num_tickets
            print("\n--- Ticket Info ---")
            print(f"Train Number : {Matched_train[0]}")
            print(f"\nBooking for: {Matched_train[2]} from {from_station} to {Matched_train[1]}")                        
            print(f"Total Tickets: {Num_tickets}")
            print(f"Total Amount : ₹{amount}")
            
            
            confirm = input("\nDo you want to book the tickets? (Yes/No): ").strip().lower()
            if confirm != "yes":
                print("Booking cancelled.")
                return

            print("\n*** Tickets Booked Successfully! ***")
            print("-------- THANK YOU 😊 --------")
            print("------- SAFE JOURNEY 🚆--------")

     #ticket details
            for passenger in self.Passengers:
                        print("\nYour Ticket Details:")
                        print(f"Train Number: {Matched_train[0]}")
                        print(f"PNR: {passenger['PNR']}")
                        print(f"Name: {passenger['Name']}")
                        print(f"Age: {passenger['Age']}")
                        print(f"Gender: {passenger['Gender']}")
                        print(f"Phone Number: {passenger['Phone']}")
            print(f"Amount  Paid :{amount}")
            
                
            print("***"*5,"Happy Journey (❁´◡`❁)","***"*5)  
            Matched_train[3] -= Num_tickets 
            exit_input = input("\nType 'exit' to leave booking or press Enter to continue: ").strip().lower()
            if exit_input == "exit":
                print("Exiting booking... Please visit again!")
                return
                    
        except ValueError as e:
            print(f"Invalid Input: {e}") 
                   
       
# Account login details

class Account():
    def __init__(self ,username ,password):
        self.username = username
        self.password = password

Account_details= []

logged_account = None
while True:
    print("\n1.Create an Account\n2. login into Account\n")
    option = int(input("Enter your option :"))
    if option == 1:
       while True:
        Username =input("Enter  Username :")
        if Username.isalpha():
            break
        else:
            print("username must be Aplhabets only.")
       Password =input("Enter  Password :")
       New_account=Account(Username , Password)
       Account_details.append(New_account)
       print("Account Created Successfully !! Press 2 for Login")
    elif option == 2:
       Username =input("Enter your Username:")
       Password =input("Enter your Password :")
       for account in Account_details:
          if account.username == Username and account.password == Password:
            logged_account = account
            break
       if logged_account is None:
        print("Invalid username or password.")
       else:
          print("--"*10," Availabe Train Details" ,"--"*10)
          obj=Railwaysticket()
          obj.book_ticket()
          break
          
    else:
       print("Inavalid Option. Please enter 1 or 2")
      





















































































































































































































































































