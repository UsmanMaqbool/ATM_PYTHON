class B_account:

    # Construct an bank account object
    def __init__(self, id, balance = 0):
        self.id = id
        self.c_balance = balance
        self.s_balance = balance
 
    def getId(self):
        return self.id
 
    def SgetBalance(self):
        return self.s_balance
 
    def Swithdraw(self, amount):
        self.s_balance -= amount
 
    def Sdeposit(self, amount):
        self.s_balance += amount

    def CgetBalance(self):
        return self.c_balance
 
    def Cwithdraw(self, amount):
        self.c_balance -= amount
 
    def Cdeposit(self, amount):
        self.c_balance += amount
 	
def atm():
   
   # For creating accounts
   accounts = []
   
   for i in range(1000, 9999):
       account = B_account(i, 0)
       accounts.append(account)
        # ATM Processes
   while True:
 
       # After inserting the card and ask user for pin
       pin = int(input("\n Enter 4 digit account pin: "))
 
       # For the valid i/P
       while pin < 1000 or pin > 9999:
           pin = int(input("\n1 Invalid Account Pin, Please re-enter: "))
 
       
       # Iterating over account session
       while True:
 
           print("\n1 - Current Account \t 2 - Saving Account")
           # Reading account_type
           account_type = int(input("\nSelect Account Type: "))

           # For the valid i/P 
           while account_type < 1 or account_type > 2:
            account_type = int(input("\n1 Invalid Account Type:, Please re-enter: "))

           # Printing menu
           print("\n1 - View Balance \t 2 - Withdraw \t 3 - Deposit \t 4 - Cancel")
 
           # Reading selection
           selection = int(input("\nEnter your selection: "))
 
           # Getting account object
           for acc in accounts:
               # Comparing account id
               if acc.getId() == pin:
                   objAcc = acc
                   break
 
           # View Balance
           if selection == 1:
               # Printing balance
               if account_type == 1:
                   print("\nAccount Balance: " + str(objAcc.CgetBalance()) + " \n")
               else:
                   print("\nAccount Balance: " + str(objAcc.SgetBalance()) + " \n")
 
           # Withdraw
           elif selection == 2:
               # Reading amount
               total = int(input("\nEnter amount to withdraw: "))
               ver_withdraw = input("Please confirm the correct amount, Yes or No ? " + str(total) + " ")
 
               if ver_withdraw == "Yes":
                   print("Confirmed withdraw")
               else:
                   break
               if account_type == 1:
                   if total < objAcc.CgetBalance():
                        # Calling withdraw method
                        objAcc.Cwithdraw(total)
                        # Printing updated balance
                        print("\nTransaction is now complete.")
                        print("\nUpdated Balance: " + str(objAcc.CgetBalance()) + " \n")
                   else:
                        print("\nYour balance is less than withdrawl amount: " + str(objAcc.CgetBalance()) + " \n")
                        print("\nPlease make a deposit.");
               else:
                   if total < objAcc.SgetBalance():
                        # Calling withdraw method
                        objAcc.Swithdraw(total)
                        # Printing updated balance
                        print("\nTransaction is now complete.")
                        print("\nUpdated Balance: " + str(objAcc.SgetBalance()) + " \n")
                   else:
                        print("\nYour balance is less than withdrawl amount: " + str(objAcc.SgetBalance()) + " \n")
                        print("\nPlease make a deposit.");

           # Deposit
           elif selection == 3:
               # Reading amount
               total = int(input("\nEnter amount to deposit: "))
               ver_deposit = input("Please confirm the correct amount, Yes, or No ? " + str(total) + " ")
 
               if ver_deposit == "Yes":
                  # Calling deposit method

                  if account_type == 1:
                    objAcc.Cdeposit(total);
                    # Printing updated balance
                    print("\nTransaction is now complete.")
                    print("\nUpdated Balance: " + str(objAcc.CgetBalance()) + " \n")
                  else:
                    objAcc.Sdeposit(total);
                    # Printing updated balance
                    print("\nTransaction is now complete.")
                    print("\nUpdated Balance: " + str(objAcc.SgetBalance()) + " \n")  
               else:
                   break
 
           elif selection == 4:
               print("Thanks for choosing our bank")
               exit()
 
           # Any other choice
           else:
               print("\nThat's an invalid choice.")

# Main function
atm()