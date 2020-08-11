def solution(x, y):
    arr = [int(x), int(y)]
    arr.sort()

    generation = 0
    while True:
        if arr[0] == 1:
            return str(arr[1] + generation - 1)
        elif arr[0] == 0:
            return 'impossible'
        generation += int(arr[1] / arr[0])
        arr[1] %= arr[0]
        arr.sort()
