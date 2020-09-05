"""

problem link : https://programmers.co.kr/learn/courses/30/lessons/42888?language=python3

"""


def solution(record):
    infos = {}  # key : uid, value : name
    res = []

    for _, r in enumerate(record):
        r = r.split(" ")
        if r[0] in {"Enter", "Change"}:
            command, uid, name = r
            infos[uid] = name
            if command == "Enter":
                res.append((True, uid))
        else:
            command, uid = r
            res.append((False, uid))

    answer = []

    for enter, uid in res:
        if enter:
            answer.append("{}님이 들어왔습니다.".format(infos[uid]))
        else:
            answer.append("{}님이 나갔습니다.".format(infos[uid]))

    return answer
