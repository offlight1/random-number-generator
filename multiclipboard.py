#random number generator

import random

print("Use this generator to your liking, it includes a range of numbers from 0 to 10000. it also has a decimal generator with an unlimited range!")

#here it generates a random integer and prints it
number = random.randint(0,1000000000)
print(number)

#now we will repeat this but with float values
number_decimals = random.random()
print(number_decimals)
