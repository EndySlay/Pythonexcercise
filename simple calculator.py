num_1 = int(input("Input your number"))
num_2 = int(input("Enter your second number"))

op = str(input("Enter what you wanna do * / - or +"))

if(op == "*"):
	print(num_1 * num_2)
elif(op == "-" ):
	print (num_1 - num_2)
elif (op == "/"):
	print(num_1 / num_2)
elif (op == "+"):
	print(num_1 + num_2)
else:
	print("Error")
