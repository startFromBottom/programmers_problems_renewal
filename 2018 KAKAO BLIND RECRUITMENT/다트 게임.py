"""

problem link : https://programmers.co.kr/learn/courses/30/lessons/17682?language=python3

"""


def tokenize_result(dartResult):
    """
    ex)
    "1D2S#10S" -> ["1D", "2S#", "KS"]
    10은 임시로 K로 변환, count_score 함수에서 다시 K -> 10으로 변환

    """
    darts = []
    each = ""
    dartResult = dartResult.replace("10", "K")
    for i, d in enumerate(dartResult):
        if i == len(dartResult) - 1:
            darts.append(each + d)
        elif (len(each) == 2 and d not in {'*', "#"}) or len(each) == 3:
            darts.append(each)
            each = d
        else:
            each += d
    return darts


def calculate_score(darts):
    scores = []
    bonus_d = {"S": 1, "D": 2, "T": 3}

    for i, dart in enumerate(darts):
        n, b = dart[0], bonus_d[dart[1]]
        if n == "K":
            n = 10
        s = int(n) ** b
        scores.append(s)
        if len(dart) == 3:
            o = dart[2]
            if o == "*":
                scores[i] *= 2
                if i > 0:
                    scores[i - 1] *= 2
            elif o == "#":
                scores[-1] *= -1

    return sum(scores)


def solution(dartResult):
    darts = tokenize_result(dartResult)

    return calculate_score(darts)
