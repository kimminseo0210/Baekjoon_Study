num = input().split()
# 다른 방법
# num = map(int, input().split())

result = 0

for i in num:
    double = int(i)**2
    result += double
    # result += i**2
    
print(result%10)