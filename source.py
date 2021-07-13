import pickle
import pyperclip

user_id=input('Enter Your User ID (press-1 to create a new id) : ')

dictionary = {}

if(user_id == '1'):

	new_user = input ('Create Your User ID : ')

	with open ("C:\\Users\\AnkitKumar\\Documents\\python\\password_manager\\new_id.txt", "w") as a:
		a.write(new_user)

	id_pass = input ('Create Your Password : ')

	with open("C:\\Users\\AnkitKumar\\Documents\\python\\password_manager\\id_pass.txt", "w" ) as b:
		b.write(id_pass)

	print("REGISTERATION SUCCESS")

with open("C:\\Users\\AnkitKumar\\Documents\\python\\password_manager\\new_id.txt", "r") as c:
	store_user=c.read()

if user_id == store_user:
	user_pass = input("Enter Your Password : ")

	with open("C:\\Users\\AnkitKumar\\Documents\\python\\password_manager\\id_pass.txt", "r" ) as d:
		store_pass=d.read()

	if user_pass != store_pass:
		print("WRONG PASSWORD")
	else:
		while (1):
				further = input("To know your saved password press '1' , To save a new password press '2' , To quit press 'q'  : ")

				if further == '2':
					account = input("Enter Your Account Name : ")
					acc_pass = input("Enter Your Account Password : ")

					confirmation = input("Would You Like To Save The Above Details (y/n) : ")

					if confirmation == 'y':
						dictionary[account] = acc_pass

						with open("C:\\Users\\AnkitKumar\\Documents\\python\\password_manager\\pass_man.txt", "bw") as readfile:
							dictionary = pickle.dump(dictionary,readfile, protocol=2)
						print ("ACCOUNT ADDED")
					else:
						print ("YOUR ACCOUNT WAS NOT ADDED!!")

				elif '1' == further:
					get_account = input("Which Account Password You want to know? : ")

					with open("C:\\Users\\AnkitKumar\\Documents\\python\\password_manager\\pass_man.txt", 'br') as fileread:
						dictionary = pickle.load(fileread)

					if get_account in dictionary:
						print(f"Your {get_account}'s password is {dictionary[get_account]} : ")
						pyperclip.copy(dictionary[get_account])
						print(f"{get_account}'s password copied to clipboard..")
					else:
						print("This account not saved")

				elif 'q' == further:
					print('TURNING OFF....')
					break
				else:
					print('WRONG INPUT PLEASE TRY AGAIN')
else:
	print(f'user named {user_id} was not found' )
			