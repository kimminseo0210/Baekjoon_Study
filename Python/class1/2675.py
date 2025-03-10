n = int(input())

for _ in range(n):
    repeat, word = input().split()
    for j in word:
        print(j * int(repeat),end="")
    print()