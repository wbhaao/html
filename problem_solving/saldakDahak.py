# 무한히 입력받으니 while문 안에 입력 받아야함 > 입력받은 리스트의 길이에 따라 실행이 달라지게 할것 >
# ls 는 리스트 변수에 값을 저장. 딕셔너리 배열로. id로 하는건 index로 찾으면 됨.
# 글자 패딩은 나중에

# 첫번째 내가 짠 코드
# storage = {}

# while True:
#     A = input().split(' ')


#     if len(A) == 1:
#         print('[LIST]\n- [ID]         | [NAME]       | [Phone]      |')
#         for i in storage:
#             print('%-15s' % ('- {0}'.format(i)), end='')
#             print('%-15s' % ('| {0}'.format(storage[i][0])), end='')
#             print('%-15s' % ('| {0}'.format(storage[i][1])), end='')
#             print('|')

#     elif len(A) == 2:
#         S = len(storage)
#         for i in range(S):
#             try: 
#                 del storage[A[1]]
#             except: 
#                 pass

#     elif len(A) == 4:
#         storage[A[1]] = [A[2], A[3]]
#     else:
#         print('잘못된 값을 입력하였습니다')

# temp는 dict 키, _id_ 는 topWord, DictName[--]이렇게 들어가면 temp 로 넣기 

# from cgi import print_directory
# import operator

# _id_, _name_, _phone_ = "[GAME]", "[ID]", "[PASSWORD]"
# temp_id_, temp_name_, temp_phone_ = _id_, _name_, _phone_

# # 파일 내용 초기화
# def file_del(file_name):
#     f = open("%s.txt" % (file_name),'w')
#     f.close()
# # 리스트 윗줄 초기화 // 리턴으로 입력받아서 초기화
# # 여기에 버그 있음 # 고침
# def upDown_change(target, upArrow):
#     if int(upArrow) == -1: arrow = ''
#     if int(upArrow): arrow = '↑' 
#     else: arrow = '↓' 

#     lst = {temp_id_:temp_id_, temp_name_:temp_name_, temp_phone_:temp_phone_}
#     lst["%s" % (target.upper())] = "%s%s" % (arrow, target.upper())
#     return list(lst.values())

# # a는 ['id1 name1 phone1', 'id2 name2 phone2', 'id3 name3 phone3'] 형식으로 저장됌
# # for 로 나누고 split으로 딕셔너리 형태로 다시 만들기

# name_list = [] # list 초기화

# # 파일 저장 형식 : id1 name1 phone1 \n id2 name2 phone2 ... 
# try:
#     a = open('data_base.txt', 'r', encoding='utf8').readlines()

#     for i in a: # i 는 'id1 name1 phone1' 형식
#         z = i.split()
#         name_list.append({
#             temp_id_:z[0],
#             temp_name_:z[1],
#             temp_phone_:z[2]})
# except: pass

# while True:
#     A = input().split(' ')

#     if len(A) == 1 and A[0] == 'ls':
#         print('- [LIST]')
#         print('- %21s| %21s| %21s|' % (
#               _id_,_name_,_phone_))

#         for _storage in name_list:
#             print('- %21s| %21s| %21s|' % (
#                 _storage[temp_id_],
#                 _storage[temp_name_],
#                 _storage[temp_phone_]))

#     # for 문으로 id, name, phone 값을 모두 빼서 저장.
#     elif len(A) == 1 and A[0] == 'save':
#         file_del('data_base')
#         data_base = open("data_base.txt", "a", encoding="utf8")

#         for _storage in name_list: 
#             data_base.write(_storage[temp_id_] + " ")
#             data_base.write(_storage[temp_name_] + " ")
#             data_base.write(_storage[temp_phone_] + "\n")
#         data_base.close()

#     # _storage 는 딕셔너리임 
#     elif len(A) == 2:
#         upDown_change(temp_id_, -1)
#         if A[1] == 'ALL':
#             name_list = []
#         cnt = 0
#         for _storage in name_list:
#             if _storage[temp_id_] == A[1]: 
#                 try:
#                     del name_list[cnt] # del 은 오류를 불러와서 try에 묶음
#                     break
#                 except: 
#                     pass
#             cnt += 1

#     # 정렬하는 법 : 전부 lower 을 한다음에 아스키 코드 번호를 통해서 정렬
#     # A[0] : sort, A[1] : 정렬 종목(id, name, phone), A[2] : 정렬 = 1, 역정렬 = 0
#     # 정렬 종목을 가지고 정렬 역정렬로 위아래로 하기
#     elif len(A) == 3 and A[0] == 'sort':
#         cnt = 0
#         lst = {}
#         # key는 원래 인덱스
#         for _storage in name_list:
#             lst[cnt] = (ord(_storage[A[1]][0].lower()))
#             cnt += 1
#         # 해석 : 딕셔너리를 리스트의 형태로 바꿔주고 그걸로 인자값(key인지 value인지)을 통해 정령
#         if int(A[2]):
#             lst1 = sorted(lst.items(), key=operator.itemgetter(1))
#         else:
#             lst1 = sorted(lst.items(), key=operator.itemgetter(1), reverse=True)
#         # 여기에 _id_ 초기화됨
#         _id_, _name_, _phone_ = upDown_change(A[1] ,A[2])
        
#         temp_name_list = []
        
#         for i in lst1:
#             temp_name_list.append(name_list[i[0]])
        
#         name_list = temp_name_list

#     elif len(A) == 4 and A[0] == 'add':
#         upDown_change(temp_id_, -1)
#         name_list.append({
#             temp_id_:A[1],
#             temp_name_:A[2],
#             temp_phone_:A[3]})

#     elif len(A) == 4 and A[0] == 'rt': # retouch
#         upDown_change(temp_id_, -1)
#         for _storage in name_list:
#             cnt = 0
#             if _storage[temp_id_] == A[1]: 
#                 _storage[temp_name_] = A[2]
#                 _storage[temp_phone_] = A[3]
#             cnt += 1
    
#     elif len(A) == 4 and A[0] == 'login':
#         login = False
#         for _storage in name_list:
#             if _storage[temp_id_] == A[1] and _storage[temp_name_] == A[2] and _storage[temp_phone_] == A[3]:
#                 login = True
#         if login:
#             print('로그인 되었습니다')
#         else:
#             print('로그인이 실패되었습니다')

#     else:
#         print('잘못된 값을 입력하였습니다')

    
# 추가기능 : *수정, *파일 입출력을 통한 저장, *로그인, 순서 변경, 수시로 정렬
# 로그인 : 아이디, 이름, 전번를 입력하고 로그인


# 하노이 탑 문제 풀이
# 2차원 리스트로 원통을 저장.

# 알고리즘 : 자신이 있는 칸을 제외한 두칸에 
# num = int(input('N:'))

# column1 = list(range(num, 0, -1))
# column2 = []
# column3 = []

# def DrawDisk():
#     print(column1)
#     print(column2)
#     print(column3)
#     print()
    

# def MoveDisk(size, depart, arrival, other):
#     if( size == 1 ):
#         arrival.append(depart.pop())
#         DrawDisk()
#     else:
#         MoveDisk(size - 1, depart, other, arrival)
#         arrival.append(depart.pop())
#         DrawDisk()
#         MoveDisk(size - 1, other, arrival, depart)

# DrawDisk()
# MoveDisk(num, column1, column3, column2)


# raw_exp = input('E: ') + ' ' # 식

# operand_list = []  # 피연산자 목록 // 숫자
# present_num = 0    # 현재 숫자
# operator_list = [] # 연산자 목록 // 기호
# priority_layer = 0
# for letter in raw_exp:
#     if letter in '0123456789':
#         present_num = present_num * 10 + int(letter) # 숫자 입력
#     else:
#         if not (present_num == 0): # 현재 숫자가 0이 아니라면
#             operand_list.append(present_num) # 숫자를 추가하고
#             present_num = 0 # 초기화
#         if letter in '+-': # priority_layer, +-, */ 구분을 통하여 우선순위를 정함
#             operator_list.append((1 + priority_layer * 2, letter))
#         elif letter in '*xX/%':
#             operator_list.append((2 + priority_layer * 2, letter))
#         elif (letter == '('):
#             priority_layer += 1
#         elif (letter == ')'):
#             priority_layer -= 1

# print(operand_list) # 튜플 형식
# print(operator_list) # 튜플 형식

# while (len(operator_list) > 0):
#     max_index, max_point = 0, 0 # 가장 큰 수의 index 값
#     # index : for 문이 몇번 돌았는지, point : 우선순위, _ : 숫자 or 기호
#     # 우선순위가 가장 큰 기호 찾기
#     for index, (point, _) in enumerate(operator_list): # 튜플이라 3개까지 줄 수 있다
#         if point > max_point:
#             max_point = point
#             max_index = index

#     # 연산할 숫자 2개, 기호 1개 삭제
#     operand1 = operand_list.pop(max_index)
#     operand2 = operand_list.pop(max_index)
#     # 순서 안받아도 되지만 안받으면 에러나니까 쓸모없는거에 받는 거
#     _, operator = operator_list.pop(max_index)

#     # operator 에 따라 연산
#     if (operator == '+'):
#         result = operand1 + operand2
#     elif (operator == '-'):
#         result = operand1 - operand2
#     elif (operator in '*xX'):
#         result = operand1 * operand2
#     elif (operator in '/%'):
#         result = operand1 / operand2
    
#     # index 부분에 result 값 넣기
#     operand_list.insert(max_index, result)
#     print(operand_list)
#     print(operator_list)

# answer = operand_list[0]
# print('A = %.2f' % answer)

# H = int(input("H:"))
# M = int(input("M:"))

# print('D = %d' % (min(abs(H * 30 - M * 6), abs(M * 6 - H * 30))))
