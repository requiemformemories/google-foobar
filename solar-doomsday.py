def solution(area):
    i = 1
    arr = []
    while area > 0:
        if area < i*i:
            square = (i-1)*(i-1)
            arr.append(square)
            area -= square
            i = 1
        else:
           i+=1
    return arr
