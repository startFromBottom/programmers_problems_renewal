"""

problem link : https://programmers.co.kr/learn/courses/30/lessons/49191#qna

"""
from collections import defaultdict


def divide(player, records):
    win, lose = [], []
    for i, v in enumerate(records[player]):
        if v == 1:
            win.append(i)
        elif v == -1:
            lose.append(i)
    return win, lose


def solution(n, results):
    # 1 : 승리, -1 : 패배, 0: 정보 없음
    records = [[0 for _ in range(n)] for _ in range(n)]
    # key : 선수 번호, value : 경기 횟수
    cnt_dict = defaultdict(int)

    # 선수별 승, 패 정보 반영
    for r in results:
        # winner, loser
        w, l = r[0] - 1, r[1] - 1
        records[w][l] = 1
        records[l][w] = -1

        cnt_dict[w] += 1
        cnt_dict[l] += 1

    # 선수의 대결 횟수 별로 내림차순
    cnt = sorted(cnt_dict.items(), key=lambda x: x[1],
                 reverse=True)

    # 선수별 승, 패 정보 갱신
    for player, _ in cnt:
        win, lose = divide(player, records)
        # i번째 player가 이긴 사람(win)은, i번째 player를 이긴 사람(lose)에게 지는 점을 반영.
        for w in win:
            for l in lose:
                records[w][l] = -1
                records[l][w] = 1

    # 정확하게 순위를 매길 수 있는 선수(각 행에서 0이 딱 1개인)의 수를 세기
    answer = 0
    for record in records:
        num_zero = len([i for i in record if i == 0])
        if num_zero == 1:
            answer += 1

    return answer
