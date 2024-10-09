def solution(diffs, times, limit):
    ls= times
    lf = [times[0]]
    for i in range(1,len(times)):
        lf.append(ls[i]+ls[i-1])
    #print(lf)
    total1 = sum(times)
    result =0
    
    def play(level):

        total2 = 0
        for i in range(len(diffs)):
            if diffs[i]-level >0:
                total2 += lf[i] *(diffs[i]-level)
        if total1+ total2 <=limit:
            return 0
        else:
            return 1
        #return total1+ total2
    top = max(diffs)
    bot =1
    while True:
        now = (bot+top)//2
        if top == bot:
            return now
        r= play(now) + play(now+1)
        if  r==1:
            return now+1
            break
        elif r == 2:
            bot = now
        else:
            top = now





