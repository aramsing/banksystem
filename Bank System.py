from random import randint
import os

def main():
	cust_or_staff = Customer_or_Staff()
	if cust_or_staff == "user":
		acct_type_menu_user()

	if cust_or_staff == "staff":
		print('\nHello employee of Python Bank!')
		print('Please enter your username and password.')
		acct_type_menu_staff()
			
def Customer_or_Staff():
	print('Welcome to Python Bank')
	userinput = input('If you are a customer - [Press 1]. If staff - [Press 2]. To close system - [Press 3]: ')
	if userinput == '1':
		return "user"         
	elif userinput == '2':
		return "staff"
	elif userinput == '3':
		return
	else:
		print('Please select only from the options provided!')

def acct_type_menu_user():
	print('\nPlease select an account type or \"Funds Transfer\"\n')
	print('1: Checkings account')
	print('2: Savings account')
	print('3: Funds Transfer') 
	print('4: Close system')
	user_input = input('Please make a selection: ')
	if user_input == '1':
		return acciso_user("checking.txt")
	elif user_input == '2':
		return acciso_user("savings.txt")
	elif user_input == '3':
		return acciso_user("checking.txt", "savings.txt") 
	elif user_input == '4':
		return
	else:
		print('Invalid selection. Please try again')
		return acct_type_menu_user()

def staff_verification():
	USERNAME = 'monty_python'
	PASSWORD = 'whatever'
	verification = False
	attempts = 0
	while verification == False and attempts < 3:
		u_n = input('Enter username: ')
		p_c = input('Enter password: ')
		if u_n == USERNAME and p_c == PASSWORD:
			verification = True
		else:
			print('Please enter the correct username and password to gain access.')
			return staff_verification()
	if attempts >= 3:
		print("Session terminated")
		return
		
	return verification

def acct_type_menu_staff():
	print('\nPlease select an account type from the menu\n')
	print('1: Checkings account')
	print('2: Savings account')
	print('3: Open account')
	print('4: Close system') 
	user_input = input('Please make a selection: ')
	
	if user_input == '1':
		return acciso_staff('checking.txt')
	elif user_input == '2':
		return acciso_staff('savings.txt')
	elif user_input == '3':
		return openacc()
	elif user_input == '4':
		return
	else:
		print('Invalid selection. Please try again')
		return acct_type_menu_staff()


def acciso_user(filename1, filename2=None):
	validation = False
	attempts = 0
	while validation == False and attempts < 3:
		acct_num1 = input("\nEnter account number: ")
		if filename2 != None:
			acct_num2 = input("Enter second account number: ")
		pin_num = input("Enter PIN number: ")
		
		if filename1 == "checking.txt" and filename2 == None: 
			iso_file = open("doc_iso.txt","w")
			file1 = open(filename1, "r")
			for line in file1:
				line_data = line.split("; ")
				if acct_num1 == line_data[0] and pin_num == line_data[1]:
					iso_file.write(line)
					validation = True
				else:
					continue
			iso_file.close()
			file1.close()
		
		if filename1 == "savings.txt" and filename2 == None:
			iso_file = open("doc_iso.txt","w")
			file1 = open(filename1,"r")
			for line in file1:
				line_data = line.split("; ")
				if acct_num1 == line_data[0] and pin_num == line_data[1]:	
					iso_file.write(line)
					validation = True
				else:
					continue
			iso_file.close()
			file1.close()
			
		if filename1 == "checking.txt" and filename2 == "savings.txt":
			checked = []
			file1 = open(filename1, "r")
			file2 = open(filename2, "r")
			iso_file = open("doc_iso.txt","w")
			for line in file1:
				line_data = line.split("; ")
				if acct_num1 == line_data[0] and pin_num == line_data[1]:
					iso_file.write(line)
					checked.append(1)	
			iso_file.close()
			
			iso_file = open("doc_iso.txt","a")
			
			for line in file2:
				line_data = line.split("; ")
				if acct_num2 == line_data[0] and pin_num == line_data[1]:
					iso_file.write(line) 
					checked.append(1)
			iso_file.close()
			file1.close()
			file2.close()
			
			if len(checked) == 2:
				validation = True
		attempts += 1
	if attempts >= 3:
		print("Session terminated")
		return	
	
	if validation == True and filename2 == None:
		return Transaction_Menu()           
	if validation == True and filename2 != None:
		return transfer_funds()


def Transaction_Menu():
	
	print('\nCustomer Transaction Menu:\n')
	
	print('1: Deposit Funds')
	print('2: Withdraw Funds')
	print('3: Query Balance')
	print('4: Transfer Funds')
	print('5: View Last Deposit Amount')
	print('6: Cancel')
	print('7: Return to Account Type Selection Menu')
	print('8: Close system')
	input_option = input('Enter your selection here: ')
	
	if input_option == '1':
		return deposit_funds()
	elif input_option == '2':
		return withdraw_funds()
	elif input_option == '3':
		return Query_Balance()
	elif input_option == '4':
		print("In order to make a funds transfer, please select \"Funds Transfer\" on the Account Selection Menu.\n")
		return acct_type_menu_user()  
	elif input_option == '5':
		return view_last_deposit()
	elif input_option == '6':
		return cancel()
	elif input_option == '7':
		return acct_type_menu_user()
	elif input_option == '8':
		return
	else :
		print('Invalid selection. Please try again.')
		return Transaction_Menu()
   


def deposit_funds():
	acct_file = open("doc_iso.txt", "r")
	contents = acct_file.read().split("; ")
	acct_file.close()
	
	deposit_amt = float(input("\nEnter the amount that you would like to deposit: "))
	acct_bal = float(contents[3]) + deposit_amt
	try:  
		contents[3] = str(acct_bal)
		contents[4] = str(deposit_amt)
	except IndexError:
		contents[3] = str(acct_bal)
	
	acct_file = open("doc_iso.txt", "w")
	write_contents = "; ".join(contents)
	acct_file.write(write_contents)
	acct_file.close()
		
	print("\n", "Account balance: $", format(acct_bal, ",.2f"),"\n", "Deposit amount: $", format(deposit_amt, ",.2f"), sep="")
	
	update_file()
	
	print("\nIf you would like to return to the transcation menu, select \"T\". If you would like to return to the Account Type Selection Menu, enter \"A\".",
	"To close the system, enter \"C\".")
	user_input = input("Selection: ").upper()
	if user_input == "T":
		return Transaction_Menu()
	elif user_input == "A":
		return acct_type_menu_user()
	elif user_input == "C":
		return
	else:
		print("Invalid selection. You are being routed to the Transaction Menu.")
		return Transaction_Menu()


def withdraw_funds(): # define function
	infile = open('doc_iso.txt', 'r') # read  the checking file
	contents = infile.read().split('; ') # read the file and make a list
	infile.close()
	withdraw = float(input('\nHow much cash do you want to withdraw?: ')) # enter the amount of cash that you want to withdraw
	allowance = float(contents[3]) # convert the 4th item in the list into a float
	if withdraw <= allowance: # create the condition
		new_bal = allowance - withdraw # subtract the variable withdraw from allowance
		outfile = open('doc_iso.txt', 'w') # overwrite checking.txt
		contents[3] = str(new_bal) # remove the first allowance making the previous line the 4th item
		contents = "; ".join(contents)
		outfile.write(contents) # write the string to the file
		outfile.close() # close the file
	else:
		print('There is not enough money in your account to withdraw the requested amount. Please try again with a withdraw amount less than %f' %allowance) # if the number entered in withdraw is not enough print this statement
		return withdraw_funds()
	
	update_file()
		
	print("\nWithdrawal complete.\nCurrent account balance: ${acct}".format(acct=format(new_bal, ",.2f")))
	print("\nIf you would like to return to the transcation menu, select \"T\". If you would like to return to the Account Type Selection Menu, enter \"A\".",
	"To close the system, enter \"C\".")
	user_input = input("Selection: ").upper()
	if user_input == "T":
		return Transaction_Menu()
	elif user_input == "A":
		return acct_type_menu_user()
	elif user_input == "C":
		return
	else:
		print("Invalid selection. You are being routed to the Transaction Menu.")
		return Transaction_Menu()
		
		
def Query_Balance():
	infile = open('doc_iso.txt', 'r')
	contents = infile.read().split('; ')
	infile.close()
	balance = contents[3]
	print("\nAccount balance: %s" %balance)
	print("\nIf you would like to return to the transcation menu, select \"T\". If you would like to return to the Account Type Selection Menu, enter \"A\".",
	"To close the system, enter \"C\".")
	user_input = input("Selection: ").upper()
	if user_input == "T":
		return Transaction_Menu()
	elif user_input == "A":
		return acct_type_menu_user()
	elif user_input == "C":
		return
	else:
		print("Invalid selection. You are being routed to the Transaction Menu.")
		return Transaction_Menu()
 
def transfer_funds():
	read_doc_iso = open("doc_iso.txt", "r")
	file_data = []
	file_data.append(read_doc_iso.readline())
	file_data.append(read_doc_iso.readline())
	read_doc_iso.close()
	checking_data = file_data[0].split("; ")
	savings_data = file_data[1].split("; ")
	print("\nTo transfer funds from your checking account to your savings account, enter \"1\" below. To transfer funds",
	"from your savings account to your checking account, enter \"2\" below.")
	selection = input("Selection: ")
	transfer_amt = float(input("\nEnter the amount you would like to transfer: "))
	if selection == "1":
		if transfer_amt <= float(checking_data[3]):
			new_check_bal = float(checking_data[3]) - transfer_amt
			new_save_bal = float(savings_data[3]) + transfer_amt
			checking_data[3] = str(new_check_bal)
			savings_data[3] = str(new_save_bal)
		else:
			print("\nI'm sorry, but you have insufficient funds in your checking account to make this transfer. Please try again.")
			return transfer_funds()
	elif selection == "2":
		if transfer_amt <= float(savings_data[3]):
			new_check_bal = float(checking_data[3]) + transfer_amt
			new_save_bal = float(savings_data[3]) - transfer_amt
			checking_data[3] = str(new_check_bal)
			checking_data[4] = str(transfer_amt)
			savings_data[3] = str(new_save_bal)
		else:
			print("\nI'm sorry, but you have insufficient funds in your savings account to make this transfer. Please try again.")
			return transfer_funds()	
	else:
		print("Invalid selection. Please try again.")
		return transfer_funds()
	write_doc_iso = open("doc_iso.txt", "w")
	write_check_data = "; ".join(checking_data)
	write_save_data = "; ".join(savings_data)
	write_doc_iso.write(write_check_data)
	write_doc_iso.write(write_save_data)
	write_doc_iso.close()
	
	update_file()
	
	print("\nTransfer complete.\nCurrent checking account balance: ${checking}\nCurrent savings account balance: ${savings}".format(checking\
	=format(new_check_bal, ".2f"), savings=format(new_save_bal, ".2f")))
	print("\nIf you would like to return to the Account Type Selection Menu, enter \"A\" below.",
	 "To close the system, enter \"C\" below.")
	user_input = input("Selection: ").upper()
	if user_input == "A":
		return acct_type_menu_user()
	elif user_input == "C":
		return
	else:
		print("Invalid selection. You are being routed to the Account Type Selection Menu.")
		return acct_type_menu_user()
	

def view_last_deposit():
	try:
		acct_file = open("doc_iso.txt", "r")
		contents = acct_file.read().split("; ")
		acct_file.close()
		acct_num = contents[0]
		last_deposit = float(contents[4])
		print("\nThe last deposit made into account number ", acct_num, " was $", format(last_deposit, ",.2f"), sep="")
	except IndexError:
		print("\nThis operation can only be done on checking accounts. To return to the Transaction Menu, enter \"T\" below. To select a different account",
		"type, enter \"A\" below. To exit the program, enter \"R\" below.")
		decision = input("User selection: ").upper()
		if decision == "T":
			return Transaction_Menu()
		elif decision == "A":
			return acct_type_menu_user()
		else:
			return
	print("\nIf you would like to return to the transcation menu, select \"T\". If you would like to return to the Account Type Selection Menu, enter \"A\".",
	"To close the system, enter \"C\".")
	user_input = input("Selection: ").upper()
	if user_input == "T":
		return Transaction_Menu()
	elif user_input == "A":
		return acct_type_menu_user()
	elif user_input == "C":
		return
	else:
		print("Invalid selection. You are being routed to the Transaction Menu.")
		return Transaction_Menu()

def cancel(): # name the function
	terminate = input('\nDo you want to cancel the transaction? Enter \"y\" if yes, \"n\" if no: ').lower() # ask the user if they want to cancel the transaction
	if terminate == 'y': # create the condition
		return main() # call the transaction menu
	elif terminate == 'n':
		return Transaction_Menu()
	else:
		print('You can only select options from the menu.') # if statement is not true
		return cancel()

def acciso_staff(filename1):
	found = False
	acct_num = input("\nEnter account number: ")
	if filename1 == "checking.txt": 
		iso_file = open("doc_iso.txt","w")
		file1 = open(filename1, "r")
		for line in file1:
			line_data = line.split("; ")
			if acct_num == line_data[0]:
				iso_file.write(line)
				found = True
		iso_file.close()
		file1.close()
	
	if filename1 == "savings.txt":
		iso_file = open("doc_iso.txt","w")
		file1 = open(filename1,"r")
		for line in file1:
			line_data = line.split("; ")
			if acct_num == line_data[0]:	
				iso_file.write(line)
				found = True

		iso_file.close()
		file1.close()
	
	if found == True:
		return Staff_Menu() 
	else:
		print("I'm sorry, the account number you entered could not be found. Please try again.")
		return acct_type_menu_staff()          


def Staff_Menu():  
	print('\nStaff Menu:')
	print('Please select one of the following:\n')
	print('1: Open Account')
	print('2: Close Account')
	print('3: Add Interest')
	print('4: Return to Account Type Selection Menu')
	print('5: Close system')
	input_option = input('\nEnter the option number you want choose: ')
		
	if input_option == '1':
		return openacc()
	elif input_option == '2':
		return close_acct()
	elif input_option == '3':
		return add_interest()
	elif input_option == '4':
		return acct_type_menu_staff()
	elif input_option == '5':
		return
	else :
		print('Please enter only from the options provided!')
		return Staff_Menu()

def openacc():
	print("\nPlease enter the type of account that you will be opening below. Enter \"check\" for a Checking Account and \"save\" for a Savings Account")
	acct_type = input("Account type: ").lower() 
	userpin = input("Please enter in a PIN number (4 numbers) for the new account: ")
	userssn = input("Please enter in your SSN (NO SPACES PLEASE): ")
  
	if len(userpin) == 4 and len(userssn) == 9:
		print("\nOpening account...")
	
		BAL = "0"
		LAST_DEPOSIT = "0"

		accnum = str(randint(10000,99999))
		if acct_type == "check":
			user_info = [accnum, userpin, userssn, BAL, LAST_DEPOSIT]
			user_info = "; ".join(user_info)
			check_file = open("checking.txt","a")
			check_file.write("\n")
			check_file.seek(0, 2)
			check_file.write(user_info)
			check_file.close()
		elif acct_type == "save":
			user_info = [accnum, userpin, userssn, BAL]
			user_info = "; ".join(user_info)
			save_file = open("savings.txt","a")
			save_file.write("\n")
			save_file.write(user_info)
			save_file.close()
		else:
			print("Invalid account type input. Please try again.")
			return openacc()
		print('\nAccount has been opened. To return to the Account Type Selection Menu',
		'enter \"A\" below. To close the system, enter \"C\" below.')
		return_to_menu = input('Return to menu? ').upper()
		if return_to_menu == 'A':
			return acct_type_menu_staff()
		elif return_to_menu == 'C':
			return
		else:
			print("Invalid input. Routing you to the Account Type Selection Menu")
			return openacc()
	else:
		print("Invalid PIN or SSN input. Routing you to the Staff Menu.")
		return Staff_Menu()
	
			
def add_interest():
	INT_RATE = 0.00217 # Monthly interest rate when annual rate is 2.6%
	TIME = 6           # Assumes monthly compounding and is expressed in months
	acct_file = open("doc_iso.txt", "r") # Remember that bank staff functions will utilize a different isolated file
	contents = acct_file.read().split("; ")
	acct_num = contents[0]
	acct_bal = float(contents[3])
	int_amt = acct_bal * INT_RATE * TIME # Simple interest rate formula
	new_bal = acct_bal + int_amt
	try:	
		contents[3] = str(new_bal)
		contents[4] = str(int_amt)
	except IndexError:
		contents[3] = str(new_bal)
	acct_file = open("doc_iso.txt", "w")
	write_contents = "; ".join(contents)
	acct_file.write(write_contents)
	print("\nInterest of $", format(int_amt, ",.2f"), " was added to account number ", acct_num, ". New account balance is $",
	format(new_bal, ",.2f"), sep="")
	acct_file.close()
	
	update_file()
	
	print('\nIf you would like to return to the Staff Menu, enter \"S\" below. To return to the Account Type Selection Menu',
	'enter \"A\" below. To close the system, enter \"C\" below.')
	return_to_menu = input('Return to menu? ').upper()
	if return_to_menu == 'S':
		return Staff_Menu()
	elif return_to_menu == 'A':
		return acct_type_menu_staff()
	elif return_to_menu == 'C':
		return
	else:
		print("Invalid input. Routing you to the Staff Menu.")
		return Staff_Menu()
	
def close_acct():
	infile = open('doc_iso.txt', 'r')
	acct_data = infile.read().split("; ")
	infile.close()
        
	acct_num = acct_data[0]
	print('\nAre you sure that you would like to close Account Number %s? If yes, enter \"y\" below. If no, enter \"n\" to return to the staff menu.' %acct_num)
	confirm_close = input('Close Account Number %s? ' %acct_num).lower()
	if confirm_close == 'y':
		if len(acct_data) == 5:
			check_file = open("checking.txt", "r")
			temp_check = open("temp_checking.txt", "w")
			for line in check_file:
				line_data = line.split("; ")
				if line_data[0] != acct_data[0]:
					temp_check.write(line)
			check_file.close()
			temp_check.close()
			
			os.remove("checking.txt")
			os.replace("temp_checking.txt", "checking.txt")
		if len(acct_data) == 4:
			save_file = open("savings.txt", "r")
			temp_save = open("temp_savings.txt", "w")
			for line in save_file:
				line_data = line.split("; ")
				if line_data[0] != acct_data[0]:
					temp_save.write(line)
			save_file.close()
			temp_save.close()
			
			os.remove("savings.txt")
			os.replace("temp_savings.txt", "savings.txt")
		
		print('\nAccount has been closed. To return to the Account Type Selection Menu',
		'enter \"A\" below. To close the system, enter \"C\" below.')
		return_to_menu = input('Return to menu? ').upper()
		if return_to_menu == 'A':
			return acct_type_menu_staff()
		elif return_to_menu == 'C':
			return
		else:
			print("Invalid input. Routing you to Staff Menu.")
			return Staff_Menu()
	else:
		return Staff_Menu()

def update_file():
	doc_iso = open('doc_iso.txt', 'r')
	iso_file_data = []
	iso_file_data.append(doc_iso.readline())
	second_line = doc_iso.readline()
	if second_line != "":
		iso_file_data.append(second_line)
	doc_iso.close()
	
	if len(iso_file_data) == 1:
		acct_data = iso_file_data[0].split('; ')
		if len(acct_data) == 5:
			check_file = open('checking.txt', 'r')
			temp_check = open('temp_checking.txt', 'w')
			temp_check.write(iso_file_data[0])
			temp_check.write("\n")
			for line in check_file:
				line_data = line.split("; ")
				if line_data[0] != acct_data[0]:
					temp_check.write(line)
			temp_check.close()
			check_file.close()
			
			os.remove('checking.txt')
			os.rename('temp_checking.txt', 'checking.txt')
			
		if len(acct_data) == 4:
			save_file = open('savings.txt', 'r')
			temp_save = open('temp_savings.txt', 'w')
			temp_save.write(iso_file_data[0])
			temp_save.write("\n")
			for line in save_file:
				line_data = line.split("; ")
				if line_data[0] != acct_data[0]:
					temp_save.write(line)
			temp_save.close()
			save_file.close()
			
			os.remove('savings.txt')
			os.rename('temp_savings.txt', 'savings.txt')
	
	if len(iso_file_data) == 2:
		checking_data = iso_file_data[0].split('; ')
		savings_data = iso_file_data[1].split('; ')
		check_file = open('checking.txt', 'r')
		temp_check = open('temp_check.txt', 'w')
		temp_check.write(iso_file_data[0])
		temp_check.write("\n")
		for line in check_file:
			line_data = line.split("; ")
			if line_data[0] != checking_data[0]:
				temp_check.write(line)

		check_file.close()
		temp_check.close()
			
		save_file = open('savings.txt', 'r')
		temp_save = open('temp_save.txt', 'w')
		temp_save.write(iso_file_data[1])
		temp_save.write("\n")
		for line in save_file:
			line_data = line.split("; ")
			if line_data[0] != savings_data[0]:
				temp_save.write(line)

		save_file.close()
		temp_save.close()

		os.remove('checking.txt')
		os.remove('savings.txt')
		os.replace('temp_check.txt', 'checking.txt')
		os.replace('temp_save.txt', 'savings.txt')

main()
