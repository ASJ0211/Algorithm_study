def solution(players, callings):
    dic = {}
    for rank,name in enumerate(players):
        dic[name] = rank
    for i in callings:
        cur_rank = dic[i]
        players[cur_rank],players[cur_rank-1]=players[cur_rank-1],players[cur_rank]
        
        dic[players[cur_rank]] = cur_rank
        dic[players[cur_rank-1]] = cur_rank-1
    return players