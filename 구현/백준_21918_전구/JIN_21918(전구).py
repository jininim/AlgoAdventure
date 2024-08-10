N, M = map(int, input().split())  # N = 전구의 개수 , M = 명령어 개수
statusList = list(map(int, input().split()))  # 전구의 상태 0 = off

for i in range(M):  # M 만큼 반복
    a, b, c = map(int, input().split())
    if a == 1:
        statusList[b - 1] = c
    elif a == 2:
        for index in range(b - 1, c):
            if statusList[index]:
                statusList[index] = 0
            else:
                statusList[index] = 1
    elif a == 3:
        for index in range(b - 1, c):
            statusList[index] = 0
    elif a == 4:
        for index in range(b - 1, c):
            statusList[index] = 1
result = " ".join(str(value) for value in statusList)
print(result)
