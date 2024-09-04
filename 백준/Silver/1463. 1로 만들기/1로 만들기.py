#https://www.acmicpc.net/problem/1463
import sys

#input = sys.stdin.readline
x=int(input())
c=0
dp=[0]*(x+1)


for i in range(2,x+1):
    #print(i)
    dp[i] = dp[i-1]+1
    #일단 이전의 수를 만드는 횟수에서 +1 하는게 기본값으로 설정(1을증가시킴)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
        #얘가 3으로 나누어떨어지면 3으로 나누어진 dp의 횟수에서 +1 >>그 이후 dp[i-1] +1 과 비교함
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
        #얘가 2으로 나누어떨어지면 2으로 나누어진 dp의 횟수에서 +1 >>그 이후 dp[i-1] +1 과 비교함
print(dp[x])
#print(dp)