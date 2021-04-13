from random import randint
from time import sleep

rnd2 = randint(1, 30)


def gentree():
    print('\033c')
    for x in range(1, 23):
        rnd1 = randint(1, rnd2)
        if x == 1:
            ch = "$"
        elif rnd1 % 4 == 0:
            ch = "o"
        elif rnd1 % 3 == 0:
            ch = "i"
        else:
            ch = "*"
        print("{:^33}".format(ch * x))
    sleep(75)


while True:
    gentree()
