# 운동복 문제

# def solution(n, lost, reserve):
#     getHelps = [] # 갱생 가능한 사람
#     cnt = n-len(lost) # 입을 수 있는 학생 수 (빌려주지 않을 경우)
#     lost.sort(reverse=True) # 역정렬
#     reserve.sort(reverse=True) # 역정렬
#     for i in lost: 
#         if i in reserve: # reserve 와 lost가 같다면
#             reserve.remove(i) 
#             getHelps.append(i)
#             cnt += 1
#     # 왜 리스트로 담아서 나중에 삭제하나?
#     # 삭제하면 의도치 않은 버그가 난다
#     lost = [x for x in lost if x not in getHelps] # 겹치는 거 lost에서 전부 삭제
#     # 제외하고 다시 만드는 거
#     # for x in lost:
#     #     if (x in getHelps):
#     #         lost.remove(x)
        
#     for i in lost:
#         if i+1 in reserve: # lost +1 이 reserve 안에 있나?
#             cnt += 1 
#             reserve.remove(i+1) 
#         elif i-1 in reserve: # lost -1 이 reserve 안에 있나?
#             cnt += 1 
#             reserve.remove(i-1) 
#     return cnt


# def solution(n, lost, reserve):
#     _reserve = [r for r in reserve if r not in lost] # 같은 값에 있는건 미리 제외
#     _lost = [l for l in lost if l not in reserve] # 같은 값에 있는건 미리 제외
    
#     # 정렬 하지 않으면 줄 수 있지만 못받는 경우가 생김
#     _reserve = sorted(_reserve) # 정렬해서 준서에 맞게 주기
    
#     for r in _reserve:
#         f = r - 1
#         b = r + 1
#         if f in _lost:
#             _lost.remove(f)
#         elif b in _lost:
#             _lost.remove(b)
#     return n - len(_lost)

# 두개 뽑아서 더하기

# 52
# def solution(numbers):
#     answer = []
#     for i in range(len(numbers)):
#         for j in range(i+1, len(numbers)):
#             answer.append(numbers[i] + numbers[j])
#     return sorted(list(set(answer)))

# # 내 풀이
# def solution(numbers):
#     answer = []
#     numbers.sort()
#     for i in range(len(numbers)-1): # 0 ~ 3
#         for x in range(i+1, len(numbers)):
#             answer.append(numbers[i]+numbers[x])
#     return sorted(list(set(answer)))

# 숫자는 인형의 모양

# 수박수박수박수?

# def strToInt(str):
#     result = 0
#     for idx, number in enumerate(str[::-1]):
#         if number == '-':
#             result *= -1
#         else:
#             result += int(number) * (10 ** idx) # 0 제곱은 1이다
#     return result

# # 아래는 테스트로 출력해 보기 위한 코드입니다.
# print(strToInt("-1234"))

# 모의고사

# from math import ceil
# import operator

# def foo(answers, lst):
#     lstLen = len(lst)
#     person = (lst * (ceil(len(answers) / lstLen)))[:len(answers)]

#     cnt = 0
#     for i in range(len(answers)):
#         if person[i] == answers[i]:
#             cnt += 1
#     return cnt

# def solution(answers):
#     corrects = {}

#     corrects[1] = foo(answers, [1,2,3,4,5]) # 길이에 맞게 제조
#     corrects[2] = foo(answers, [2,1,2,3,2,4,2,5]) # 길이에 맞게 제조
#     corrects[3] = foo(answers, [3,3,1,1,2,2,4,4,5,5]) # 길이에 맞게 제조

#     corrects = sorted(corrects.items(), key=operator.itemgetter(1), reverse=True) # 점수에 따라 정렬
#     answer = [] 

#     maxScore = corrects[0][1] # 가장 큰 점수
#     for i in corrects:
#         if i[1] == maxScore: # 점수가 같으면 추가 
#             answer.append(i[0])

#     return list(answer)

# print(solution([1,3,2,4,2]))


# from itertools import cycle

# def solution(answers):
#     giveups = [ # cycle 로 무한히 리스트 만듬
#         cycle([1,2,3,4,5]),
#         cycle([2,1,2,3,2,4,2,5]),
#         cycle([3,3,1,1,2,2,4,4,5,5]),
#     ]
#     scores = [0, 0, 0] 
#     for num in answers:
#         for i in range(3): # 각 세 학생의 답과 비교
#             if next(giveups[i]) == num: # next로 index가 한칸씩 앞으로 감
#                 scores[i] += 1
#     highest = max(scores)

#     answer = []

#     for i, v in enumerate(scores):
#         if v == highest:
#             answer.append(i + 1)

#     return answer

# 나중에 해야함 해석

# def solution(answers):
#     p = [[1, 2, 3, 4, 5],
#          [2, 1, 2, 3, 2, 4, 2, 5],
#          [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
#     s = [0, 0, 0]

#     for index1, answer in enumerate(answers): # 답
#         for index2, solve in enumerate(p): # 학생 답
#             if answer == solve[index1 % len(solve)]: # 답과 학생 답이 같나 // % 로 길이 제한 둠  
#                 s[index2] += 1
#     return [index2 + 1 for index2, v in enumerate(s) if v == max(s)]


# def solution(id_list, report, k):
#     answer = [0] * len(id_list)
#     reports_info = {x : [] for x in id_list}

#     for r in set(report): # 
#         reports_info[r.split()[1]].append((r.split())[0])

#     for v in reports_info.values():
#         if len(v) >= k:
#             for i in v:
#                 answer[id_list.index(i)] += 1
#     return answer

# 이 코드는 신고한 사람을 저장 하지 않고 report를 다시 해석해서 

# def solution(id_list, report, k):
#     answer = [0] * len(id_list)  
#     reports = {x : 0 for x in id_list}

#     for r in set(report): # 신고 받은 사람 += 1
#         reports[r.split()[1]] += 1

#     for r in set(report): # r[0] : 신고한 사람
#         if reports[r.split()[1]] >= k: # 신고를 k번 이상 받았다면
#             answer[id_list.index(r.split()[0])] += 1 # 신고한 사람에게 += 1

#     return answer

# def solution(lottos, win_nums):
#     rank = [6,6,5,4,3,2,1]
#     same = 0

#     for l in range(6):
#         if lottos[l] in win_nums:
#             same += 1

#     return rank[same + lottos.count(0)], rank[same]
	
# print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))

# 로또 최고 최저

# def solution(lottos, win_nums):
#     rank=[6,6,5,4,3,2,1]

#     cnt_0 = lottos.count(0)
#     ans = 0
#     for x in win_nums:
#         if x in lottos:
#             ans += 1
#     return rank[cnt_0 + ans],rank[ans]

# def solution(arr1, arr2):
#     answer = [] 

#     for i in range(len(arr1)):
#         answer.append([])

#     for i in range(len(arr1)):
#         for z in range(len(arr1[0])):
#             answer[i].append(arr1[i][z] + arr2[i][z])

#     return answer

    	
# print(solution([[1], [2]], [[3], [4]]))

#	[[1, 2], [2, 3]], [[3, 4], [5, 6]]

# 코딩 테스트 1

# def solution(arr1, arr2):
#     answer = [] 

#     for i in range(len(arr1)):
#         answer.append([])

#     for i in range(len(arr1)):
#         for z in range(len(arr1[0])):
#             answer[i].append(arr1[i][z] * arr2[i][z])

#     return answer

# 코딩 테스트 2

# def solution(priorities, location):
#     priorities_dict = priorities
#     cnt = 1
#     sample = priorities[:priorities.index(max(priorities))]
#     sample = list(sample)
#     priorities = priorities[priorities.index(max(priorities)):]
#     print(sample)
#     print(type(sample))
#     print(priorities)
#     print(type(priorities))
#     priorities = priorities + list(reversed(sample))

#     while True:
#         print(priorities_dict.index(max(priorities)))
#         if priorities_dict.index(max(priorities)) == location:
#             return cnt
#         priorities[priorities.index(max(priorities))] = 0
#         cnt += 1

# 코딩테스트 2

# def solution(priorities, location):
#     cnt = 1
#     priorities_dict = {} # temp는 무슨역할?

#     for index, p in enumerate(priorities): # 인덱스를 지정해주는 거
#         priorities_dict[index] = p 
#     # key : 인덱스 , value : 값, priorities : 값
#     sMaxIndex = location # 나보다 큰 수중 가장 작은 값 index
#     # 값만 추출한 리스트
    
#     for i, p in enumerate(priorities): # p의 우선순위가 location의 값보다 높으면 cnt += 1
#         if p > priorities_dict[location]:
#             cnt += 1
#             sMaxIndex = min(p, sMaxIndex) # 이걸로 
#     if location < sMaxIndex:
#         location_temp = location + len(priorities)
#     else:
#         location_temp = location

#     for i in range(1, location_temp - sMaxIndex):
#         if priorities[location] == priorities[(sMaxIndex+i) % len(priorities)]:
#             if sMaxIndex + i < location:
#                 cnt += 1 
#     return cnt

#     while True:
#         # 첫번째가 priorities_dict 중 우선도가 가장 높나?
#         if next(iter(priorities_dict.values())) == max(priorities_dict.values()): 
#             # 나의 인덱스와 구하고자 하는 index가 같나
#             if next(iter(priorities_dict.keys())) == location:
#                 return cnt
#             # 다르면 삭제
#             del priorities_dict[next(iter(priorities_dict.keys()))] 
#             cnt += 1 
#         else: # 해석 : 맨앞에껄 맨뒤로 옮기는 것
#             # key와 value를 저장하고 마지막에 index에 append
#             temp_key = next(iter(priorities_dict)) # 삭제하는 key 저장
#             temp_value = priorities_dict[next(iter(priorities_dict))] # 삭제하는 value 저장
#             del priorities_dict[next(iter(priorities_dict.keys()))] # 첫번째 순서 삭제
#             # 첫번쨰 값 append
#             priorities_dict[temp_key] = temp_value


# print(solution([1, 1, 9, 1, 1, 1], 0))

# def solution(priorities, location):
#     answer = 0
#     while True:
#         max_num = max(priorities) # 리스트에서 가장 큰수를 구한다.
#         for i in range(len(priorities)): # 리스트를 처음부터 확인한다 
#             if max_num == priorities[i]: # 만약 가장 큰 수와 리스트의 요소와 일치하면
#                 answer += 1 # 프린트한 것으로 간주하고 answer에 1 추가 
#                 priorities[i] = 0 # 프린트한 요소는 0으로 표시 
#                 max_num = max(priorities) # 가장 큰 수를 다시 구한다.
#                 if i == location: # 만약 location과 i가 일치하면 answer을 반환한다. 
#                     return answer



# 코딩 테스트 2

# def solution(prices):
#     answer = []
#     for i in range(len(prices)-1):
#         if prices[i] > min(prices[i+1:]):
#             answer.append((prices[i+1:].index(min(prices[i+1:]))) - i + i + 1)

#         elif prices[i] <= min(prices[i+1:]):
#             answer.append(len(prices)-i-1)
#     answer.append(0)
#     return answer

# print(solution([1, 2, 3, 2, 3]))

# 기능개발

# from math import ceil

# def solution(progresses, speeds):
#     def minusOne(x): # 앞의 index 가 0이 될때까지 반복하는걸 한번에 함 // 0 이하 안나오게 함
#         if x - progresses_cnt[0] <= 0:
#             return 0
#         else:
#             return x - progresses_cnt[0]

#     answer = []
#     progresses_cnt = []

#     for i in range(len(progresses)):
#         progresses_cnt.append(ceil((100 - progresses[i]) / speeds[i]))

#     while True: 
#         progresses_cnt = list(map(minusOne, progresses_cnt)) # 앞 index를 0으로 만들고 뺀 만큼 다른 index에도 빼줌
#         cnt = 0
        
#         # {1}
#         if sum(progresses_cnt) == 0: # 모든 값이 0 이라면
#             cnt += len(progresses_cnt) # cnt += p_cnt 길이 
#             break
#         while (progresses_cnt[0] == 0): # progresses의 첫번째가 100이상이면
#             del progresses_cnt[0] # 값 삭제
#             cnt += 1   # 이렇게 하면 연속된 값은 같이 append 할 수 있음
            
#         if not (cnt == 0): # cnt가 1이상이면 append
#             answer.append(cnt) 
#     answer.append(cnt) # {1} 에서 더한 cnt를 여기서 append
#     return answer                   

# print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))


# def solution(progresses, speeds):
#     answer = []
#     time = 0
#     count = 0
    
#     while len(progresses) > 0:
#         if (progresses[0] + time*speeds[0]) >= 100: 
#             del progresses[0]
#             del speeds[0]
#             count += 1
            
#         else:
#             if count > 0:
#                 answer.append(count)
#                 count = 0
#             time += 1 # append 할게 없다면 하루가 흐름
#     answer.append(count) # 마지막엔 0이 되서 여기서 append
#     return answer

# import math


# def solution(progresses, speeds):
#     progresses = [math.ceil((100 - a) / b) for a, b in zip(progresses, speeds)]
#     answer = []
#     front = 0, 0

#     for idx in range(len(progresses)):
#         if progresses[idx] > progresses[front]:  
#             answer.append(idx - front)
#             front = idx 
#     answer.append(len(progresses) - front)  

#     return answer

# def solution(phone_book):
#     phone_book = list(map(str, phone_book))
#     phone_book.sort() # 숫자순으로 정렬 1,2,3 ... 8,9
#     for i in range(len(phone_book)-1):
#         if phone_book[i] in phone_book[i+1]:
#             return False 
#     return True        
# print(solution(["12", "3465346", "13", "123"]))

# 이게 내꺼임 전화번호

# def solution(phone_book):
#     phone_book = list(map(str, phone_book)) # str 로 정렬해서 123이 13보다 우선되게 함
#     phone_book.sort() # 정렬
#     for index in range(len(phone_book[:-1])): # 마지막 제외
#         if phone_book[index] == phone_book[index+1][:len(phone_book[index])]:
#             return False
#     return True

# 내가 푼거랑 거의 비슷함 // 똑같다 봐도 무방

# def solution(phone_book):
#     answer = True
#     phone_book.sort()
#     for i in range(len(phone_book)-1):
#         if len(phone_book[i]) < len(phone_book[i+1]): # 비교 할게 더 크냐 (작으면 접미사가 안됌)
#             if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]: # 
#                 answer = False
#                 break
#     return answer

# def solution(phoneBook):
#     phoneBook = sorted(phoneBook)

#     for p1, p2 in zip(phoneBook, phoneBook[1:]):
#         if p2.startswith(p1):
#             return False
#     return True

# 나중에 풀기

# def solution(phone_book):
#     hash_map = {}
#     for phone_number in phone_book: 
#         hash_map[phone_number] = 1 # phoneNumber마다 1을 부여
#         # 1을 왜 부여할까
#     for phone_number in phone_book:
#         temp = ""

#         for number in phone_number:
#             temp += number # temp에 number 추가
#             # hash_map 이 temp에 포함되어 있나 
#             if temp in hash_map and temp != phone_number: # temp와 phone_number가 다른가
#                 return False

#     return True

# def solution(numbers):
#     numbers = list(map(str, numbers))
#     numbers.sort(reverse=True)

#     answer = ''.join(numbers)
#     return answer



# def solution(left, right):
#     cnt_lst = [1] * (right - left + 1)
#     lst = list(range(left, right+1))
#     answer = 0

#     for i in lst:
#         for x in range(2, i+1):
#             if i % x == 0:
#                 cnt_lst[lst.index(i)] += 1

#     for i in range(len(cnt_lst)):
#         if cnt_lst[i] % 2 == 0:
#             answer += lst[i]
#         else:    
#             answer -= lst[i]
#     return answer

# print(solution(13, 17))

# def solution(left, right):
#     answer = 0
#     for i in range(left,right+1):
#         if int(i**0.5)==i**0.5:
#             answer -= i
#         else:
#             answer += i
#     return answer

# def solution(numbers):
#     numbers = list(map(str, numbers))
#     numbers.sort(reverse=True)

#     answer = ''.join(numbers)
#     return answer

# def solution(progresses, speeds):
#     Q=[]
#     answer = []
#     for p, s in zip(progresses, speeds):
#         if len(Q)==0 or Q[-1][0] > ((p-100)//s):
#             Q.append([-((p-100)//s),1])
#         else:
#             Q[-1][1]+=1

#     for q in Q:
#         answer.append(q[1])
#     return answer

# print(solution(	[95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))


