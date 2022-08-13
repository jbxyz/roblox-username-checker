# ROBLOX USERNAME CHECKER by Jb & 3zg!  
# © 2022-2030 Jb & 3zg

import requests, colorama, random, time, threading, pyfiglet, sys

ascii_banner = pyfiglet.figlet_format("jbxyz")
print(colorama.Fore.WHITE + f"{ascii_banner}")
print(colorama.Fore.BLUE + "Roblox Username Checker")
print(colorama.Fore.CYAN + "https://github.com/jbxyz & https://github.com/3zg")
print("\n")


def fiveletters():
	choices = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
	while True:
		try:
			code = random.choices(choices, k=5)
			user = "".join(code)
			r = requests.get(f"https://api.roblox.com/users/get-by-username?username={user}").text
			r = str(r)
			if "User not found" in r:
				print(colorama.Fore.GREEN + f"Generated valid/banned username: {user}")
				if save == "y":
					file = open("valid_or_banned_roblox_names.txt", "a")
					file.write(f"{user}\n")
					file.close()
			else:
				print(colorama.Fore.RED + f"Generated invalid username: {user}")
		except Exception:
			print(colorama.Fore.RED + "Unkown ERROR")
		time.sleep(float(delay))

def fourletters():
	choices = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
	while True:
		try:
			code = random.choices(choices, k=4)
			user = "".join(code)
			r = requests.get(f"https://api.roblox.com/users/get-by-username?username={user}").text
			r = str(r)
			if "User not found" in r:
				print(colorama.Fore.GREEN + f"Generated valid/banned username: {user}")
				if save == "y":
					file = open("valid_or_banned_roblox_names.txt", "a")
					file.write(f"{user}\n")
					file.close()
			else:
				print(colorama.Fore.RED + f"Generated invalid username: {user}")
		except Exception:
			print(colorama.Fore.RED + "Unkown ERROR")
		time.sleep(float(delay))

def threeletters():
	choices = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
	while True:
		try:
			code = random.choices(choices, k=3)
			user = "".join(code)
			r = requests.get(f"https://api.roblox.com/users/get-by-username?username={user}").text
			r = str(r)
			if "User not found" in r:
				print(colorama.Fore.GREEN + f"Generated valid/banned username: {user}")
				if save == "y":
					file = open("valid_or_banned_roblox_names.txt", "a")
					file.write(f"{user}\n")
					file.close()
			else:
				print(colorama.Fore.RED + f"Generated invalid username, {user}")
		except Exception:
			print(colorama.Fore.RED + "Unkown ERROR")
		time.sleep(float(delay))

while True:
	try: 
		letter = input(f"""{colorama.Fore.BLUE}Pick one number (1-5): {colorama.Fore.RESET}
{colorama.Fore.GREEN}[1]{colorama.Fore.RESET} Check usernames manually
{colorama.Fore.GREEN}[2]{colorama.Fore.RESET} Check usernames in usernames_to_check.txt
{colorama.Fore.GREEN}[3]{colorama.Fore.RESET} Find 3 letter usernames
{colorama.Fore.GREEN}[4]{colorama.Fore.RESET} Find 4 letter usernames
{colorama.Fore.GREEN}[5]{colorama.Fore.RESET} Find 5 letter usernames
> """) 
		if letter == "1" or letter == "2" or letter == "3" or letter == "4" or letter == "5":
			break
		else:
			print(colorama.Fore.RED + "Enter a valid choice (1-5) " + colorama.Fore.RESET)
	except KeyboardInterrupt:
		print(colorama.Fore.RED + "Keyboard Interupt, Exiting.." + colorama.Fore.RESET)
		time.sleep(0.3)
		sys.exit()

if letter == "1":
	try: 
		print("INFO: If the usernames does not follow roblox username rules it will still count as valid")
		while True:
				username = input("Enter Username: ")
				r = requests.get(f"https://api.roblox.com/users/get-by-username?username={str(username)}").text
				r = str(r)
				if "User not found" in r:
					print(colorama.Fore.GREEN + "Username Not Taken/Banned!" + colorama.Fore.RESET)
				else:
					print(colorama.Fore.RED + "Username Taken!" + colorama.Fore.RESET)
	except KeyboardInterrupt:
			print(colorama.Fore.RED + "\n> Keyboard Interupt, Exiting.." + colorama.Fore.RESET)
			time.sleep(0.3)
			sys.exit()


if letter == "2":
	try:
		print("This Will Check All Usernames In usernames_to_check.txt")
		print("INFO: If The Usernames Does Not Follow Roblox Username Rules It Will Count As Valid")
		while True:
			try:
				try:
					delay = input("Enter delay (0 = None): ")
					delay = float(delay)
					break
				except:
					print("Enter a valid choice")
			except KeyboardInterrupt:
				print(colorama.Fore.RED + "Keyboard Interupt, Exiting.." + colorama.Fore.RESET)
				time.sleep(0.3)
				sys.exit()
		while True:
				save = input("Auto save names (y/n): ")
				if save == "y" or save == "n":
					break
				else:
					print("Enter a valid choice")
				input("Press enter to start: ")
				try:
					file = open("usernames_to_check.txt", "r")
					lines = file.readlines()
					file.close()
				except:
					print("File usernames_to_check.txt was not found. Please create one and enter usernames in it")
				list = []
				donelist = 0
				for name in lines:
					if "\n" in name:
						list.append(name[:-1])
						donelist = int(donelist) + 1
					else:
						list.append(name)
						donelist = int(donelist) + 1
					print(f"[{str(donelist)}] Loaded name")
				print("Done with loading names. Press enter to start checker")
				input("")
				donee = 0
				for user in list:
					donee = int(donee) + 1
					e = len(user)
					e = str(e)
					if int(e) >= 3 or int(e) <= 20:
						r = requests.get(f"https://api.roblox.com/users/get-by-username?username={str(user)}").text
						r = str(r)
						if "User not found" in r:
							print(colorama.Fore.GREEN + f"[{str(donee)}] Valid username: " + str(user))
							if save == "y":
								file = open("valid_usernames_(usernames_to_check).txt", "a")
								file.write(user+"\n")
								file.close()
						else:
							print(colorama.Fore.RED + f"[{str(donee)}] Invalid username: " + str(user))
							if save == "y":
								file2 = open("invalid_usernames_(usernames_to_check).txt", "a")
								file2.write(user+"\n")
								file2.close()
					else:
						print(colorama.Fore.RED + f"[{str(donee)}] Invalid username: " + str(user))
						if save == "y":
							file3 = open("invalid_usernames_(usernames_to_check).txt", "a")
							file3.write(user+"\n")
							file3.close()
					time.sleep(float(delay))
				print(colorama.Fore.RESET + "Done")
				input("")
				exit()
	except KeyboardInterrupt:
		print(colorama.Fore.RED + "Keyboard Interupt, Exiting.." + colorama.Fore.RESET)
		time.sleep(0.3)
		sys.exit()


if letter == "3":
	try: 
		while True:
			try:
				threads = input("Enter how many threads (5-10 recomended): ")
				threads = int(threads)
				break
			except Exception:
				print("Enter a valid choice")
		while True:
			try:
				delay = input("Enter delay for each thread (0 = None): ")
				delay = float(delay)
				delay = str(delay)
				break
			except Exception:
				print("Enter a valid choice")
		while True:
			save = input("Want to save all 3 letter usernames in a .txt file (y/n): ")
			if save == "y" or save == "n":
				break
			else:
				print("Enter a valid choice")
		input("Press enter to start: ")
		for _ in range(int(threads)):
			t1 = threading.Thread(target=threeletters)
			t1.start()
	except KeyboardInterrupt:
			print(colorama.Fore.RED + "\n> Keyboard Interupt, Exiting.." + colorama.Fore.RESET)
			time.sleep(0.3)
			sys.exit()


if letter == "4":
	try: 
		while True:
			try:
				threads = input("Enter how many threads (5-10 recomended): ")
				threads = int(threads)
				break
			except Exception:
				print("Enter a valid choice")
		while True:
			try:
				delay = input("Enter delay for each thread (0 = None): ")
				delay = float(delay)
				delay = str(delay)
				break
			except Exception:
				print("Enter a valid choice")
		while True:
			save = input("Want to save all 4 letter usernames in a .txt file (y/n): ")
			if save == "y" or save == "n":
				break
			else:
				print("Enter a valid choice")
		input("Press enter to start: ")
		for _ in range(int(threads)):
			t1 = threading.Thread(target=fourletters)
			t1.start()
	except KeyboardInterrupt:
			print(colorama.Fore.RED + "\n> Keyboard Interupt, Exiting.." + colorama.Fore.RESET)
			time.sleep(0.3)
			sys.exit()


if letter == "5":
	try: 
		while True:
			try:
				threads = input("Enter how many threads (5-10 recomended): ")
				threads = int(threads)
				break
			except Exception:
				print("Enter a valid choice")
		while True:
			try:
				delay = input("Enter delay for each thread (0 = None): ")
				delay = float(delay)
				delay = str(delay)
				break
			except Exception:
				print("Enter a valid choice")
		while True:
			save = input("Want to save all 5 letter usernames in a .txt file (y/n): ")
			if save == "y" or save == "n":
				break
			else:
				print("Enter a valid choice")
		input("Press enter to start: ")
		for _ in range(int(threads)):
			t1 = threading.Thread(target=fiveletters)
			t1.start()
	except KeyboardInterrupt:
			print(colorama.Fore.RED + "\n> Keyboard Interupt, Exiting.." + colorama.Fore.RESET)
			time.sleep(0.3)
			sys.exit()