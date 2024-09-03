#https://www.acmicpc.net/problem/22864
a, b, c ,m = map(int,input().split())
if a>m:
    print(0)
else:
    work = 0
    hard = 0
    for h in range(0,24):
        if hard+a <=m:
            hard+=a
            work +=b
        else:
            hard-=c
            if hard<0:
                hard=0
        #print("h",hard,"work",work)
    print(work)
#이게 내코드 근데 문제가 피로도가 음수로 내려갈 수가 없는 부분
#25의 피로도가 있을때 30만큼 감소시킬 수 없음 > 여기서 오류가 발생함 일괄적으로 계산하면