# 투포인터 알고리즘 이용하기
# 완전탐색이 아닌 투포인터를 이용해야 시간복잡도 O(N)으로 해결 가능
# 투포인터: start_index, end_index 2개의 포인터를 이동시키면서 연속된 수열의 합을 수를 구하는 알고리즘

N = int(input())
num_list = []

for i in range(1, N+1):
    num_list.append(i)

print(num_list)

start_index = 1
end_index = 1
count = 1
sum = 1

while end_index != N: # end_index가 주어진 자연수 N과 같지 않을 때 반복

    if sum == N:            # 1) 합과 주어진 자연수 N이 같을 때
        count += 1          # 연속된 수열을 찾았으므로 count + 1
        end_index += 1      # end_index 1 증가
        sum += end_index    # 합에도 end_index 추가
    elif sum < N:           # 2) 합이 주어진 자연수보다 작을 때
        end_index += 1      # end_index 1 증가
        sum += end_index    # 합에도 end_index 추가, 합이 자연수와 일치하지 않으므로 count는 무시
    else:                   # 3) 합이 주어진 자연수보다 클 때
        start_index += 1    # start_index 1 증가
        sum -= start_index  # 합에서 start_index 1 감소

print(count)