def HDL_driver():
        # get input
	user_HDL = get_HDL()
        # check if HDL is normal
	output = check_HDL(user_HDL)
        # Output
	return output

def get_HDL():
	HDL = input("Enter your HDL: ")
	return int(HDL)

def check_HDL(HDL):
	if HDL >= 60:
		return("Your HDL is Normal")
	elif 40 <= HDL <  60:
		return("Your HDL is Blorderline Low")
	else:
		return("Your HDL is Low")

def interface():
    print("My Program")
    while true:
   	 print("Options:")
	 print("1 - HDL")
   	 print("9 - Quit")
   	 choice = input("Enter your choice: ")
   	 if choice=='9':
       		 return
	 elif coice == '1':
		HDL_driver()
   
interface()
