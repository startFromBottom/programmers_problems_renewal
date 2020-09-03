"""

problem link : https://programmers.co.kr/learn/courses/30/lessons/17679

"""

from collections import defaultdict


def one_cycle(m, n, board):
    cnt = 0

    # 1. 지울 수 있는 블록을 찾기 -> 지울 수 있는 블록 개수를 del_cnt에 추가
    delete_squares = []
    for i in range(m - 1):
        for j in range(n - 1):
            if board[i][j] == "#":
                continue
            can_delete = True
            start = board[i][j]
            square = [(i, j), (i + 1, j), (i, j + 1), (i + 1, j + 1)]
            for x, y in square:
                if (x, y) == (i, j):
                    continue
                if board[x][y] != start:
                    can_delete = False
            if can_delete:
                delete_squares.extend(square)

    delete_squares = list(set(delete_squares))
    cnt += len(delete_squares)

    # 2. 지워진 블록 -> # 표시
    for x, y in delete_squares:
        board[x][y] = "#"

    # 3. 블록 재배치
    for i in range(n):
        valids = []
        for j in range(m):
            if board[j][i] != "#":
                valids.append(board[j][i])
        valids.reverse()
        valids.extend(["#"] * (m - len(valids)))
        for j in range(m):
            board[m - 1 - j][i] = valids[j]

    return cnt


def solution(m, n, board):
    del_cnt = 0
    board = [list(row) for row in board]

    while del_cnt < m * n:
        one_cnt = one_cycle(m, n, board)
        del_cnt += one_cnt
        if one_cnt == 0:
            break

    return del_cnt
