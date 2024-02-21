import numpy as np
def solution(board):
    mx,my=len(board),len(board)
    for i in range(mx):
        for j in range(my):
            try :
                if i!=0 and j!=0 and board[i-1][j-1] ==1:
                    if board[i][j]==1:
                        pass
                    else:
                        board[i][j]=-1
            except:
                pass
            try :
                if i!=0 and board[i-1][j] ==1:
                    if board[i][j]==1:
                        pass
                    else:
                        board[i][j]=-1
            except:
                pass
            try :
                if i!=0 and board[i-1][j+1] ==1:
                    if board[i][j]==1:
                        pass
                    else:
                        board[i][j]=-1
            except:
                pass
            try :
                if j!=0 and board[i][j-1] ==1:
                    if board[i][j]==1:
                        pass
                    else:
                        board[i][j]=-1
            except:
                pass
            try :
                if board[i][j+1] ==1:
                    if board[i][j]==1:
                        pass
                    else:
                        board[i][j]=-1
            except:
                pass
            try :
                if j!=0 and board[i+1][j-1] ==1:
                    if board[i][j]==1:
                        pass
                    else:
                        board[i][j]=-1
            except:
                pass
            try :
                if board[i+1][j] ==1:
                    if board[i][j]==1:
                        pass
                    else:
                        board[i][j]=-1
            except:
                pass
            try :
                if board[i+1][j+1] ==1:
                    if board[i][j]==1:
                        pass
                    else:
                        board[i][j]=-1
            except:
                pass
    r=0    
    for i in board:
        for j in i:
            if j ==0:
                r+=1
    return r
