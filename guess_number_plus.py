# 2020-05-16 Saturday
# Author by toto
from random import randint

while True:
    magic_num = randint(1, 100)
    input_times = 0
    bingo=False
    while bingo == False:
        input_times += 1
        input_num = input("Enter your lucky number (1...100):")
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

    input_switch = input("Input Y to continue:")
    if input_switch != "Y":
        print("good night , my LORD")
        break
