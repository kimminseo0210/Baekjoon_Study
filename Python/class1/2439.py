n = int(input())

for i in range(1, 1+n):     # 층
    for k in range(n-i):    # 빈칸
        # n=5 i=1 빈칸 4 ...
        print(" ", end="")
    for k in range(i):      # 별
        # i=1 별 1
        print("*",end="")
    print()