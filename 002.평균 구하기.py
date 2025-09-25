N = input() # 1000보다 작음
M = input()
scores = list(map(int, M.split()))

# 총합 / 개수 * 100 = 평균
# 새로운 총합 / 최고점 / 개수 * 100

max = max(scores)
sum = sum(scores)

print(sum / int(N) / max * 100)

