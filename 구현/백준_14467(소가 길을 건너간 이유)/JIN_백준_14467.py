# 입력
N = int(input())  # 관찰 횟수
observe_list = []  # 관찰 결과 리스트
result = 0
for i in range(N):
    observe_list.append(2)  # 0,1이 아닌 값을 가진 리스트 생성

for i in range(N):
    cowNum, cowLocation = map(int, input().split())  # 소의 번호, 위치 입력
    index = cowNum - 1

    if observe_list[index] == 2: # 초기값 세팅
        observe_list[index] = cowLocation
    else:
        if observe_list[index] != cowLocation: #소가 이동 할 경우
            result += 1 # 횟수 증가
            observe_list[index] = cowLocation

# 출력 : 소가 길을 건너간 최소 횟수를 출력 한다.
print(result)
