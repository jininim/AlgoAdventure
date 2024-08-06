"""
입력 A, B, C, M
A = 1시간 피로도
B = 일 처리량
C = 1시간 피로도 감소량
M = 최대 피로도
조건 : 하루 24시 M 을 넘기지 않게 일을 할 수 있는 일 처리량
"""
A, B, C, M = map(int, input().split())
if A > M:
    print(0)
else:
    result = 0  # 최대 일 처리량
    N = 0  # 근무 시간
    current_M = 0  # 현재 피로도
    while N < 24:
        if current_M + A <= M:  # 현재피로도 + 1시간 피로도가 최대 피로도 보다 낮은경우에 일을함.
            N += 1  # 1시간 근무
            result += B  # 일 처리량
            current_M += A  # 1시간 피로도 만큼 현재 피로도 증가
        else:
            N += 1
            current_M -= C
            if current_M < 0:  # 현재 피로도가 음수인 경우
                current_M = 0

    print(result)
