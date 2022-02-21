# 평균 1546

# N = int(input())

# A = list(map(int, input().split()))

# B = max(A)
# C = []

# for i in A:
#     C.append(i/B*100)
    
# print(sum(C) / len(C))

# n=int(input())
# a=list(map(int, input().split()))
# print(sum(a)/max(a)*100/n)

# N = int(input())

# score = list(map(int, input().split()))

# maxscore = max(score)
# addAllscore = 0

# for i in range(len(score)): 
#     score[i] = score[i]/maxscore*100

# for i in score:
#     addAllscore += i

# addAllscore /= len(score)

# print(addAllscore)

# OX퀴즈 8958

# > string을 for문에 넣어서 한글자씩 검사한다 >
# >> 점수는 if else로 추가하고 else가 되면 점수가 초기화 되게 함 >>

# N = int(input())
# A = []

# for i in range(N):
#     A.append(str(input()))

# for i in A:
#     answer = 0
#     score = 1
#     for x in i:
#         if x == "O":
#             answer += score
#             score += 1
#         else:
#             score = 1
#     print(answer)

# 평균은 넘겠지 4344

# B에서 순서(첫번째)를 제외한 것들의 평균보다 높은건 변수에 저장하고 변수 / len(listName)으로 
# 평균보다 높은 학생을 구한다

# A = int(input())

# for i in range(A):
#     top = 0
#     B = list(map(int, input().split()))
#     del B[0] # 1번째는 순서라 삭제
#     for i in B:
#         if i > sum(B) / len(B):
#             top += 1
#     print("{0}%".format(format(round(top / len(B) * 100, 3), '.3f')))
            


# C = int(input())

# std = []
# mean = 0
# percent = 0

# for i in range(0, C):
#     std.append(int(input()))

# mean = sum(std) / len(std)

# for i in std:
#     if i > mean:
#         percent += (1 / len(std)) * 100

# print("{0}%".format(percent))

# 셀프 넘버 4673 아직 못풀겠음 22.1.12
# 1. 1부터 10000까지 있는 리스트에서 생성자가 있는 수는 삭제한다
# 2. 셀프넘버의 특징을 찾아 1부터 10000까지 재귀함수를 돈다
# nums = list(range(1, 10001))
# noSelfnums = []
# def Self_Num(A):
#     for i in range(1, 10001):
#         B = i 
#         C = i
#         while True:
#             if C % 10 == 0:
#                 break
#             else:
#                 B += C % 10
#                 C //= 10
#         noSelfnums.append(B)



# Self_Num(1)

# print("\n\n\n\naaaaaaaaaaaaaaaaaaaaaaaaaaaaa",noSelfnums,"\n\n\n\naaaaaaaaaaaaaaaaaaaaaas")

# complement = list(set(nums) - set(noSelfnums))

# print(sorted(list(complement)))
# 1.숫자 > 문자열 변환 > 리스트 변환 sum으로 전부 합 **
# 2.나누기로 for문 돌기

# 알파벳 찾기 10809
# 1. 알파벳 리스트를 만들어서 나오는 알파벳은 숫자를 바꾼다 > for문으로 검사
# 2. 

# alphabet = [-1] * 26 # -1이 들어있는 26길인=의 리스트
# cnt = 0
# A = input()

# for i in A:
#     if (alphabet[ord(i) - 97] == -1): # 이미 배뀌어있다면 값을 바꾸지 않음
#         alphabet[ord(i) - 97] = cnt
#     cnt += 1
# # 만약 i = b라면, 첫번째라면 리스트의 2번째에 값을 0으로 바꿔야함
# print(*alphabet) # *은 리스트에 대괄호, 콤마를 없애줌

# 문자열 반복  2675
# 1. 첫번째 변수를 받고 그 숫자만큼 for문을 돌게 함 거기서 for문을 또 돌아서 문자열을 입력받고 
# 반복 횟수만큼 print()로 출력하는데 end=""으로 줄바꿈 X
# 2. print()를 리스트로 바꿔봄

# loop = int(input())

# for i in range(loop):
#     R, S = input().split(' ')
#     for x in S:
#         #if x in alphanumeric:
#         print(x*int(R), end='')
#     print('')

# a=int(input())

# for i in range(a):
#     c=[] # 돌때마다 초기화
#     b,d=input().split()
#     for j in d: # 문자열 > 문자
#         c.append(j) # 문자를 리스트에 넣음
#     for k in range(len(c)):  # 리스트의 값 역할
#         for l in range(int(b)): # R만큼 반복해서 출력
#             print(c[k],end='')
#     print('')

# 단어 공부 1157
# 조건. 대문자와 소문자를 구분하지 않는다, 
#       가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
# 대문자 A = 65, 소문자 a = 97
# 1. upper 로 전부 대문자로 만들면 됌 > 

# N = int(input())
# cnt = 1 # 자기 방도 포함
# i = 0
# while True:
#     if N <= 1: # 도착했는지 확인
#         break
#     else:
#         cnt += 1
#         i += 6 # 외각으로 갈수록 값이 커짐
#         N -= i # 한칸 전진
# print(cnt)

#6,12,18,24...
# (육각형 한 변 길이) - 1 * 6 = (그 육각형의 방 총갯수)
# ***값에 1을 빼고 6을 버림 나누기 하면 1.2.3.4... 이렇게 나옴. 즉 이걸로 할수***

# ??! 10926
# answer1 = 층, answer2 = 호수
# print(int(input())-543)


# ACM 호텔 10250

# import math
# N = int(input())

# for i in range(N):
#     H, W, N = map(int, input().split())
#     호 = math.ceil(N / H) # 왜 이 식이 나왔는가
#     층 = N % H
#     if 층 == 0:
#         층 = H
#     호 = '{0:02d}'.format(호)
  
#     print('%s%s' % (층,호))
# def find_index(rcnt, answer, char):
#     answer.replace(' ', '')
#     cnt = 0
#     for i in answer:
#         if i == char and rcnt != 1:
#             rcnt -= 1
#         elif i == char and rcnt == 1:
#             return cnt
#         cnt += 1

# answer = input()

# if answer.find('(') != -1:
#     print(answer[answer.find('(')+1:find_index(answer.count(')'), answer, ')')])


# y지점에 도착하기 바로 직전의 이동거리는 반드시 1광년으로 하려 한다.
# 1광년 이동한 후에 2광년, 또 후엔 3광년을 움직일 수 있다 

# return 을 이상하게 하고있음, 그걸 다 모아야함 @37218 저장이 되지 않고 있다 @#!# 고친거 같다
# def find_sequence(ableToGo, total=0):
#     a = 0
#     if ableToGo % 2 == 1: # 홀수면 중간수를 구함 \\ 짝수는 중간수가 없다
#         a = ableToGo // 2 + 1 # 중간수
#     b = ableToGo // 2 # 곱하는 횟수
#     c = ableToGo + 1 # 곱해지는 수
    
#     total = (b * c) + a

#     return total    

# N = int(input())

# for i in range(N):
#     cnt = 0
#     ableToGo = 0 # 갈수 있는 거리 // 중간 ex). 0, 1, 2 를 갈수 있다면 1
#     x, y = map(int, input().split())
#     distance = y - x # 도착까지 남은 거리
#     while distance != 0:
#         # 최대로 갈수 있는 거리에서 차례대로 내려오면 나오는 수
#         sq = find_sequence(ableToGo+1, 0) # EX). 3 => 3+2+1 = 6 || 5 => 5+4+3+2+1 = 15
#         if distance >= sq: # 쭉 내려와도 남은 거리보다 적다면 UP
#             ableToGo += 1
#             distance -= ableToGo

#         elif distance < sq:
#             # 최대 거리로 갈 수 없는 상태. 이동거리 유지나 낮추는게 필요함
#             if sq - (ableToGo+1) <= distance: # 그냥 올리지 않고 가는게 distance보다 많냐
#                 distance -= ableToGo       # 많지 않으면 동결
#             else:
#                 ableToGo -= 1              # 이것도 많으면 하나 내려서 계산
#                 distance -= ableToGo
#         cnt += 1
#     print(cnt)

# t = int(input())

# for _ in range(t):
#     x, y = map(int,input().split())
#     distance = y - x
#     count = 0  # 이동 횟수
#     move = 1  # count별 이동 가능한 거리
#     move_plus = 0  # 이동한 거리의 합
#     while move_plus < distance :
#         count += 1
#         move_plus += move  # count 수에 해당하는 move를 더함
#         if count % 2 == 0 :  # count가 2의 배수일 때, 
#             move += 1  
#     print(count)

# answer = list(input('N:'))
# lenght = len(answer)
# for i in range(lenght-1):
#     answer.insert(0,' ')
# print(answer)

# os.system('cls')
# while True:
#     print(''.join(answer)[:lenght])
#     answer.append(answer[0])
#     del answer[0]
#     sleep(0.5)
#     os.system('cls')
    
# 나중에 풀기 모르겠음
# import os
# from time import sleep

# string = input('S:') # hel
# lenght = len(string)

# string = lenght * ' ' + string + (lenght - 1) * ' '
# print('lenght = %s' % (len(string)))
# start = 0
# while True:
#     print(string[start:(start + lenght)]) # 0:3 1:4 2:5 3:6 4:7 5:8 6:9 7:10 0:3 8:3 1:4 2:5
#     print('start : %d, start + lenght : %d' % (start, start + lenght))
#     sleep(0.5)             # 8
#     start = (start + 1) % (lenght * 3 - 1) # 1 2 3 4 5 6 7 0 1 2 3 4 5 6 7 0 1 2 3 4 5 6 7 0






