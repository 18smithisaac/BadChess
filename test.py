import chess, random

def main():
    board = chess.Board()
    print(nPlyMoveSearch(board, 0, 4))
 


def makeRandomMove(board):
    l = []
    for moves in board.legal_moves:
        l.append(moves)
    randomNumber = random.randint(0, (len(l)-1))
    selectedMove = chess.Move.from_uci(str(l[randomNumber]))
    print(selectedMove)
    board.push(selectedMove)

def moveSearch(board, depth, n):
    totalPositions = 0
    if depth < n:
        for moves in board.legal_moves:
            board.push(moves)
            totalPositions += moveSearch(board, depth+1, n)
            board.pop()
        return totalPositions
    elif depth == n:
        return 1
    else:
        return 0

def nPlyMoveSearch(board, depth, n):
    l = []
    if n > 5:
        return 0 
    return moveSearch(board, depth, n)


    

main()