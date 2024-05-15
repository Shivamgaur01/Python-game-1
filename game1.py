print(" Welcome to the number guessing game ")
import math
import random

lower = int(input(" Enter lower bound:- "))
Upper = int(input(" Enter Upper bound:- "))

Random_number = random.randint(lower, Upper)

chance = round(math.log(Upper - lower + 1, 2))

a = "You have only"
print(a, chance, "chances to guess the number!!")

if (chance == 0):
  print("You have no chance to guess the number")

elif(chance > 0):
  count = 0
  while (count<chance):
    count = count + 1
    guess = int(input("Guess a number: "))
    if(guess == Random_number):
      print("Congratulations you did it in ", count, " try")
      
    elif(guess > Random_number):
      print("You guess too large number!! ")
      
    else:
      print("You guess too small number!! ") 

else:
  print("You have no chance to guess the number")
      
    
  
