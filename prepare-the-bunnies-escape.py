def solution(map):
    visited = [[[-2 for j in range(0, len(map[0]))] for i in range(0, len(map))] for h in range(2)]
    visited = bfs([0, 0], 0, 0, map, visited)
    if visited[1][-1][-1] == -2:
        return visited[0][-1][-1]
    elif visited[0][-1][-1] == -2:
        return visited[1][-1][-1]
    else:
        return visited[0][-1][-1] if visited[0][-1][-1] < visited[1][-1][-1] else visited[1][-1][-1]



def bfs(coordinate, layer, previous_count, map, visited):
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    if coordinate[0] < 0:
        return
    if coordinate[1] < 0:
        return
    if coordinate[0] >= len(map):
        return
    if coordinate[1] >= len(map[0]):
        return

    if visited[layer][coordinate[0]][coordinate[1]] > -2 and visited[layer][coordinate[0]][coordinate[1]] <= (previous_count + 1):
        return

    if map[coordinate[0]][coordinate[1]] == 1 and layer == 1:
        return
    elif map[coordinate[0]][coordinate[1]] == 1:
        layer+=1

    if visited[layer][coordinate[0]][coordinate[1]] == -2:
        visited[layer][coordinate[0]][coordinate[1]] = previous_count + 1
    if visited[layer][coordinate[0]][coordinate[1]] > 0 and visited[layer][coordinate[0]][coordinate[1]] > (previous_count + 1):
        visited[layer][coordinate[0]][coordinate[1]] = previous_count + 1

    if coordinate[0] == len(map) - 1 and coordinate[1] == len(map[0]) - 1:
        return visited

    for direction in directions:
        new_coordinate = [coordinate[0] + direction[0], coordinate[1] + direction[1]]
        new_visited = bfs(new_coordinate, layer, previous_count + 1, map, visited)
        if (new_visited is not None) and (new_visited[0][-1][-1] > -2 and new_visited[1][-1][-1] > -2):
            return new_visited
    return visited
