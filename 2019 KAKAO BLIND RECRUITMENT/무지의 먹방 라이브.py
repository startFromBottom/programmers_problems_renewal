"""

problem link : https://programmers.co.kr/learn/courses/30/lessons/42891

"""

def solution(food_times, k):
    ans = -1

    food_times = [(f, i) for i, f in enumerate(food_times)]
    food_times.sort(key=lambda x: x[0])

    i = 0
    l = len(food_times)
    before = 0

    while i < l:
        time = food_times[i][0]
        start = i
        while i + 1 < l and food_times[i + 1][0] == time:
            i += 1
        cnt = l - start

        if k < (time - before) * cnt:
            food_times[start:] = sorted(food_times[start:], key=lambda x: x[1])
            ans = food_times[start + (k % cnt)][1] + 1
            break

        k -= (time - before) * cnt
        before = time
        i += 1

    return ans