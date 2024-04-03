string = '0123456789'
#
# matrix = []
#
# for row in matrix:
#     print(row)

matrix = []
print(matrix)

# for i in range(10):
#     print('first loop', i +1)
#
#     nested_list = []
#     for j in string:
#         q = int(j) * 10
#         print("inside nested loop", i, q)
#         nested_list.append(q)
#
#     matrix.append(nested_list)
#     print(matrix)
#
# print('end')
# print(matrix)

# matrix = [[j for j in string] for i in range(10)]
# print(matrix)
matrix = [[int(j) * 10 for j in string] for i in range(10)]
print(matrix)