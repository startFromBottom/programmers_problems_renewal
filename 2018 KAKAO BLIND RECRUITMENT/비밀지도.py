"""

problem link : https://programmers.co.kr/learn/courses/30/lessons/17681

"""


def solution(n, arr1, arr2):
    decodes = [str(bin(num1 | num2))[2:] for num1, num2 in zip(arr1, arr2)]
    decodes = [d.replace("1", "#").replace("0", " ") for d in decodes]
    return [" " * (n - len(d)) + d for d in decodes]
