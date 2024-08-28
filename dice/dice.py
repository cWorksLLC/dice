import random

max = int(input("The dice is going to be a d"))
num = int(input("How many dice do you want?"))
i = 1
#its the variables buddy

for i in range(num):
    int = random.randint(0, max)
    print(int)
#end