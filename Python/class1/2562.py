# numList = []
# for _ in range(9):
#     i = int(input())
#     numList.append(i)

# list comprehension 표현식
numList = [int(input()) for _ in range(9)]

print(max(numList))
print(numList.index(max(numList)) + 1)