"""

problem link : https://programmers.co.kr/learn/courses/30/lessons/17678?language=python3

파이썬 알고리즘 인터뷰 - 박상길 지음, 정진호 일러스트
책의 코드입니다

"""


def solution(n, t, m, timetable):
    # 입력값 초 단위 전처리
    timetable = [
        int(time[:2]) * 60 + int(time[3:])
        for time in timetable
    ]
    timetable.sort()

    current = 540  # 09:00, 첫 버스 도착 시간
    for _ in range(n):
        for _ in range(m):
            # 대기가 있는 경우, 1초 전 도착
            if timetable and timetable[0] <= current:
                candidate = timetable.pop(0) - 1
            else:  # 대기가 없는 경우, 정시 도착
                candidate = current

        current += t
    # 분, 초로 변경
    h, m = divmod(candidate, 60)
    return str(h).zfill(2) + ":" + str(m).zfill(2)
