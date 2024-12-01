from collections import Counter
from heapq import heappush, heappop 


def problem1(data: str) -> str:
    heap1, heap2 = [], []

    for line in data.splitlines():
        x1, x2 = map(int, line.split())
        heappush(heap1, x1)
        heappush(heap2, x2)

    dist = 0
    while heap1:
        dist += abs(heappop(heap1) - heappop(heap2))
    
    return str(dist)


def problem2(data: str) -> str:
    counter1, counter2 = Counter(), Counter()

    for line in data.splitlines():
        x1, x2 = map(int, line.split())
        counter1[x1] += 1
        counter2[x2] += 1

    sim = 0
    shared_keys = set(counter1.keys()) & set(counter2.keys())
    for key in shared_keys:
        sim += key * counter1[key] * counter2[key]

    return str(sim)

    
