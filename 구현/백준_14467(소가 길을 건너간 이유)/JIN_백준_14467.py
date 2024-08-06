# 입력
N = int(input())  # 관찰 횟수
observe_dict = {}  # 관찰 결과 딕셔너리
result = 0

for i in range(N):
    cowNum, cowLocation = map(int, input().split())  # 소의 번호, 위치 입력

    if cowNum not in observe_dict:  # 초기값 세팅
        observe_dict[cowNum] = cowLocation
    else:
        if observe_dict[cowNum] != cowLocation:  # 소가 이동 할 경우
            result += 1  # 횟수 증가
            observe_dict[cowNum] = cowLocation

# 출력 : 소가 길을 건너간 최소 횟수를 출력 한다.
print(result)
