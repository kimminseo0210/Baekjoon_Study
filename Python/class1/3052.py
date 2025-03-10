changeArr = []

for i in range(0,10):
    # 숫자 입력 (10개)
    n = int(input())
    # 받은 숫자를 42로 나눈 나머지가 changeArr에 없으면 추가
    if n % 42 not in changeArr:
        changeArr.append(n % 42)

# changeArr의 길이(서로다른 나머지의 개수) 출력
print(len(changeArr))