"""

problem link : https://programmers.co.kr/learn/courses/30/lessons/42583?language=python3

"""

from collections import deque


class Bridge:

    def __init__(self, bridge_length: int, max_weight: int):
        self._q = deque([0] * bridge_length)
        # weight attributes
        self.cur_w = 0
        self.max_w = max_weight

    def forward(self, truck: int) -> (bool, int):
        """
        :param truck: Truck trying to enter the bridge
        :return: (can_enter, popped from bridge)
        """
        out = self._q.popleft()
        self.cur_w -= out
        if self.cur_w + truck <= self.max_w:
            self._q.append(truck)
            self.cur_w += truck
            return True, out
        else:
            self._q.append(0)
            return False, out


def solution(bridge_length, weight, truck_weights):
    t = 0
    completed_sum = 0
    total = sum(truck_weights)

    truck_weights.reverse()
    bridge = Bridge(bridge_length, weight)

    while completed_sum < total:

        t += 1
        if truck_weights:
            can_enter, out = bridge.forward(truck_weights[-1])
            completed_sum += out
            if can_enter:
                truck_weights.pop()
        else:
            _, out = bridge.forward(0)
            completed_sum += out

    return t
