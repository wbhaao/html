import sys
from winsound import Beep
from time import sleep
from os import system
from random import *
# import pygame


# pygame.init()
# pygame.mixer.init()
# pygame.mixer.music.load('cloud_nine.mp3')
# pygame.mixer.music.play(-1)

beat = 0.47

def getName():
    #               초성                    중성                   종성        
    return chr(((randint(0,15) * 588) + (randint(0,20) * 28) + randint(0,0)) + 44032)\
         + chr(((randint(0,15) * 588) + (randint(0,20) * 28) + randint(0,0)) + 44032)

delay = 80

playerNames = [getName(), getName(), 'ㅤㅤ']
dialog = ['hel', 'hel', 'hel']

def drawOneLine(index, talk):
    print('%-8s' % (playerNames[index]), end='')
    print('|', end='')
    dialog[index] = talk
    print('%16s' % (dialog[index]), end='')

def drawPlayerLine(index, talk):
    print('%-8s' % (playerNames[index]), end='')
    print('|', end='')
    dialog[index] = talk
    print('%14s' % (dialog[index]), end='')
    return input()
    
def playerFail():
    print('실패')
    exit()
    
    

for i in range(len(playerNames)):
    Beep(1000, int(beat*1000))
    
    Beep(1000,int(beat*1000))

    if not (i == 2):
        drawOneLine(i, '나는 %s' % (playerNames[i]))
    else:
        playerNames[2] = drawPlayerLine(i, '나는 ')

    print() # 줄바꿈
    sleep(beat*2)

system('cls')
for i in range(len(playerNames)):
    drawOneLine(i, '나는 %s' % (playerNames[i]))
    print()

sleep(2)

def random_char_num():
    a = randint(1, 4)
    if a == 1:
        return '하나'
    elif a == 2:
        return '둘'
    elif a == 3:
        return '셋'
    elif a == 4:
        return '넷'
    return False

def charToNum(chr):
    if chr == '하나':
        return 1
    elif chr == '둘':
        return 2
    elif chr == '셋':
        return 3
    elif chr == '넷':
        return 4
    return False

system('cls')
for i in range(3):
    drawOneLine(i,  talk='아이엠 그라운드 지금부터 시작')
    print()
print()
sleep(beat*4)
# attacker | deffencer num!
attacker = 0
deffencer = -1

lst = [0, 1, 2]
while True: # 중복 안되게
    deffencer = choice(lst)
    if attacker != deffencer:
        num = random_char_num() # '누구 몇' 에 몇을 고르는 거
        break
    

while True:
    dialog = ['','','']
    system('cls')
    # 공격
    if not (attacker == 2): # 공격하는게 Ai인가
        lst = [0, 1, 2]
        while True: # 중복 안되게
            deffencer = choice(lst)
            if attacker != deffencer:
                num = random_char_num() # '누구 몇' 에 몇을 고르는 거
                break
        drawOneLine(attacker, '%s %s!' % (playerNames[deffencer], num))
        for i in range(3):
            if i != attacker:
                print()
                drawOneLine(i, dialog[i])
        print()  
    else: # 공격하는게 플레이언가
        for i in range(3):
            if i != attacker:
                print()
                drawOneLine(i, dialog[i])
        print()  
        answer = drawPlayerLine(2, '')
        answer += ' a a'
        # 내 답이 이름중에 있나                      몇번 하는거에 에러가 나지 않았나 (하나, 둘, 셋, 넷 이외는 error)              
        if answer.split()[0] in playerNames[:2] and charToNum(answer.split()[1]): # 공격을 잘했나
            # 공격 성공함
            num = answer.split()[1]
            deffencer = playerNames.index(answer.split()[0])
            print()

        else: # 답 틀리면
            playerFail()

    sleep(beat*2)
    system('cls')  
    # 방어
    if not (deffencer == 2):
        sts = (playerNames[deffencer] + ' ') * charToNum(num)
        
        drawOneLine(deffencer, sts[:-1])
        for i in range(3):
            if i != deffencer:
                print()
                drawOneLine(i, dialog[i])
                
        attacker = deffencer
        print()

    else: # 공격 받은게 플레이어 인가
        for i in range(3):
            if i != deffencer:
                print()
                drawOneLine(i, dialog[i])
        
        print()        
        answer = drawPlayerLine(2, '')
        correct = (playerNames[2]+' ') * charToNum(num)
        if answer == (correct[:-1]): # 방어에 성공했는가
            attacker = 2
            print()
        else: # 방어 실패
            playerFail()
    sleep(beat*charToNum(num))
    print()