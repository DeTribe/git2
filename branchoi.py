num = int(input("Please enter a Number: "))

if num > 5:
   print("Number is greater than 5")
elif num < 5:
   print("Number is less than 5")
else:
   print("Number is 5")

# Now test the variable again using two expressions
# and display a response only on success

if num > 7 and num < 9:
   print("Number is 8")
if num == 1 or num == 3:
   print("Number is 1 or 3")
