# 2020-05-15 FRI
# Author by toto
from random import randint
magic_num = randint(1, 5)
input_times = 0
bingo=False
while bingo == False:
    input_times += 1
    input_num = input("Enter your lucky number (1...5):")
    if input_num.isdigit():
        if int(input_num) < magic_num:
            print("Too small,please try again")
        elif int(input_num) > magic_num:
            print("Too big,please try again")
        else:
            print("bingo,count input_times %s"%input_times)
            bingo = True
    else:
        print("User input need to be a number,please try again")
