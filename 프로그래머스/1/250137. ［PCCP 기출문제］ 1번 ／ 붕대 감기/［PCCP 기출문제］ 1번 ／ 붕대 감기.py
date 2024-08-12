
def solution(bandage, health, attacks):
    t=0
    s=0
    a=0
    h=health
    while True:
        t+=1
        s+=1
        if health>h:
            health=h
        if t==attacks[a][0]:
            health-=attacks[a][1]
            a+=1
            s=0
            if health <=0:
                answer=-1
                False
                break                            
        else:
            health += bandage[1]
        if s==bandage[0]:
            health+=bandage[2]
            s=0
        answer = health
        if t==attacks[-1][0]:
            break


    return answer