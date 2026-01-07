title="Coding for beginners in easy steps"
 
try:
   print(titel)

except NameError as msg:
   print(msg)

day = 32

try:
   if day > 31:
            raise ValueError(" invalid day number.")
   # More statements to execute get added here
   
except ValueError as msg:
   print("The program found an", msg)

finally:
   print("..but today is a good day anyway")
