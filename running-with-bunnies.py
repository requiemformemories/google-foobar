import time
def solution(times, times_limit):
    shortest_path_map = [[float('inf') for j in range(len(times))] for i in range(len(times))]
    for src in range(len(times)):
        shortest_path_map[src][src] = 0
        for relax in range(len(times)):
            for i in range(len(times)):
                for j in range(len(times)):
                    if shortest_path_map[src][i] + times[i][j] < shortest_path_map[src][j]:
                        if relax == len(times) - 1:
                            return list(range(0, len(times) - 2))
                        shortest_path_map[src][j] = shortest_path_map[src][i] + times[i][j]
    path_to_walk = [[0, times_limit, [], [0]]]
    max_bunnies = []
    while len(path_to_walk) > 0:
        current = path_to_walk.pop()
        src = current[0]
        remainingTime = current[1]
        bunnies = current[2]
        path = current[3]

        if(src > 0 and (src < len(times) - 1) and (src not in bunnies)):
            bunnies.append(src)
            bunnies.sort()

        if (src == len(times) - 1) and (len(bunnies) > len(max_bunnies)):
            max_bunnies = bunnies
            if len(max_bunnies) == len(times) - 2:
                return list(range(0, len(times) - 2))
        if len(bunnies) == len(max_bunnies) and sum(bunnies) < sum(max_bunnies):
            max_bunnies = bunnies

        for i in range(0, len(times)):
            if i == src:
                continue
            if remainingTime - shortest_path_map[src][i] - shortest_path_map[i][len(times) - 1] < 0:
                continue
            if shortest_path_map[i][src] + shortest_path_map[src][i] == 0 and (i in path):
                continue
            new_path = path[:]
            new_path.append(i)
            path_to_walk.append([i, remainingTime - shortest_path_map[src][i], bunnies[:], new_path])
    return  [b - 1 for b in max_bunnies]
