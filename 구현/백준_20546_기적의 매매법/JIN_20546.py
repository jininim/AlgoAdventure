# 기적의 매매법
# 입력 :
# 1. 첫 번째 줄에 준현이와 성민이에게 주어진 현금이 주어진다.
# 2. 두 번째 줄에 2021년 1월 1일부터 2021년 1월 14일까지의 MachineDuck 주가가 공백을 두고 차례대로 주어진다. 모든 입력은 1000 이하의 양의 정수이다.

# 출력 :
# 1월 14일 기준 준현이의 자산이 더 크다면 "BNP"를, 성민이의 자산이 더 크다면 "TIMING"을 출력한다.
# 둘의 자산이 같다면 "SAMESAME"을 출력한다. 모든 결과 따옴표를 제외하고 출력한다.

# 입력 1
money = int(input())
# 입력 2
machineDuckPriceList = list(map(int, input().split()))

currentMoney_J = money  # 준현이 현금
stockCount_J = 0  # 준현이 주식 보유 수
money_J = 0  # 준현이 총 보유 자산
currentMoney_S = money  # 성민이 현금
stockCount_S = 0  # 성민이 주식 보유 수
money_S = 0  # 성민이 총 보유 자산

for i in range(len(machineDuckPriceList)):
    currentStockPrice = machineDuckPriceList[i]  # 오늘 주가
    if currentMoney_J >= currentStockPrice:
        a, b = divmod(currentMoney_J, currentStockPrice)  # a = 주식 보유 수 , b = 남은 현금
        currentMoney_J -= a * currentStockPrice
        stockCount_J += a
money_J = stockCount_J * machineDuckPriceList[-1] + currentMoney_J  # 준현이 총 보유 자산

stockChangeCount = 0  # 주가 변동 카운트
for i in range(len(machineDuckPriceList)):
    if i != 0:
        currentStockPrice = machineDuckPriceList[i]  # 오늘 주가
        beforeStockPrice = machineDuckPriceList[i - 1]  # 전일 주가
        # 오늘 주가가 전일 주가보다 크다면
        if currentStockPrice > beforeStockPrice:
            if stockChangeCount < 0:
                stockChangeCount = 0
            stockChangeCount += 1
        else:
            if stockChangeCount > 0:
                stockChangeCount = 0
            stockChangeCount -= 1
        # 주가가 3일 이상 하락 했다면,
        if stockChangeCount == -3:
            if currentMoney_S >= currentStockPrice:
                a, b = divmod(currentMoney_S, currentStockPrice)  # a = 주식 보유 수 , b = 남은 현금
                currentMoney_S -= a * currentStockPrice
                stockCount_S += a
                stockChangeCount = 0  # 변동 카운트 초기화
        elif stockChangeCount == 3:
            # 보유 주식을 전부 판매
            currentMoney_S += stockCount_S * currentStockPrice
            stockCount_S = 0
            stockChangeCount = 0  # 변동 카운트 초기화
money_S = stockCount_S * machineDuckPriceList[-1] + currentMoney_S

if money_J > money_S:
    print("BNP")
elif money_S == money_J:
    print("SAMESAME")
else:
    print("TIMING")
