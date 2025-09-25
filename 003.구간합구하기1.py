import sys

input = sys.stdin.readline
n, m = list(map(int, input().split())) # n = 개수, m = 합을 구해야 하는 수 
num_list = list(map(int, input().split())) # n개의 수
sum_list = [0]
temp = 0

# 합 배열 구하기
for num in num_list:
    temp += num
    sum_list.append(temp)

for _ in range(m):
    i, j = list(map(int, input().split())) # 합을 구해야 하는 구간 - i ~ j
    print(sum_list[j] - sum_list[i - 1])
