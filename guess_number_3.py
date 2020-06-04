# -*- coding: UTF-8 -*-
# 2020-05-29 Fri
# Author by toto
from random import randint
your_name = input("Enter your name (such ad David):")
total_game_times = 0
bingo_times = []
total_guess_times = 0
while True:
    magic_num = randint(1, 100)
    input_times = 0
    total_game_times += 1
    bingo = False
    while bingo == False:
        input_times += 1
        input_num = input("Enter your lucky number (1...100):")
        if input_num.isdigit():
            if int(input_num) < magic_num:
                print("Too small,please try again")
            elif int(input_num) > magic_num:
                print("Too big,please try again")
            else:
                print("bingo,count input_times %s" % input_times)
                total_guess_times = total_guess_times + input_times
                bingo_times.append(input_times)
                bingo = True
        else:
            print("User input need to be a number,please try again")

    input_switch = input("Input Y to continue:")
    if input_switch != "Y":
        avg_bingo_times = total_guess_times / total_game_times
        print(bingo_times)
        res = "%s你好，你已经玩了%s次，一共%s轮，最快%s轮猜出答案，平均%.2f轮猜出答案，good night , my LORD" % (your_name,total_game_times,total_guess_times,min(bingo_times),avg_bingo_times)
        print(res)
        break

out = open('game_one_user.txt', 'w')
out.write(res)
out.close()
