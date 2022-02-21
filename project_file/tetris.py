# block_library = [\
#     [
#         [1, 0, 0],
#         [1, 0, 0],
#         [1, 1, 1]
#     ],\
#     [
#         [0, 0, 0],
#         [0, 1, 0],
#         [1, 1, 1],
#     ],\
#     [
#         [0, 1, 0],
#         [0, 1, 0],
#         [1, 1, 0],
#     ]]

# # 0:null. 1~7:block. -1:floor // 콘솔에 표시될 거 
# block_info = [ 
#     [0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0],
#     [-1, -1, -1, -1, -1, -1, -1]]

# def setting_block():
#     for b in block_info:
#         for i in b:
#             if i == -1:
#                 print('⬛', end='')
#             elif i == 1:
#                 print('🟥', end='')
#             elif i == 2:
#                 print('🟩', end='')
#             elif i == 3:
#                 print('🟦', end='')
#             elif i == 4:
#                 print('🟧', end='')
#             elif i == 5:
#                 print('🟪', end='')
#             elif i == 6:
#                 print('🟨', end='')
#             elif i == 7:
#                 print('🟫', end='')
#             else:
#                 print('⬜', end='')
#         print()

# # i : 가로, x : 세로
# setting_block()
# for i in range(7): # 가로 // 내려가는 역할
#     for x in range(3): # 세로 //  블록의 세로
#         for z in range(3): # 블록의 가로
#             block_info[i][x] = block_library[0][x][z]
# setting_block()
