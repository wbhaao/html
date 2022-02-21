import random
from os import system
from time import sleep

mid = []
bottom = [0, 0, 0, 0, 0, 0, 0, 1, 2, 4, 7, 8, 16, 17, 19, 21, 22, 23, 24, 25, 26, 27]

def getName():
    
    #               초성                    중성                   종성        
    return chr(((random.randint(0,15) * 588) + (random.randint(0,20) * 28) + random.choice(bottom)) + 44032)\
         + chr(((random.randint(0,15) * 588) + (random.randint(0,20) * 28) + random.choice(bottom)) + 44032)

system('cls')

print('2글자 이름 생성기')
yN = input('y/n:')
if yN == 'y':
    system('cls')
    print(getName())
    while True:
        print('이름이 마음에 안든다면 다시 뽑을 수 있습니다')
        yN = input('y/n:')
        if yN == 'y':
            system('cls')
            print(getName())
        else:
            print('ㅃㅇ')
            sleep(1)
            exit()

else:
    print('?')
    sleep(1)
    exit()

