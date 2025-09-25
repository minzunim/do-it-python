import sys

# 1000보다 작은 자연수 10,000,000개를 1초 안에 정렬

# 빈 배열 초기화 - 1~1000
# 배열을 순회하면서 등장할 때마다 인덱스에 값을 +1
# 해당 배열에서 하나씩 꺼냄

count = [0] * 1001
numbers = [1,1,2,3,4,5,2,4,5,6,2,3,6,7,8,9]

for num in numbers:
    count[num] += 1

print(count)

for i in range(len(count)):
    for j in range(count[i]):
        print(i, sep='')
