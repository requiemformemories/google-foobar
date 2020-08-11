def solution(n):
    count = 0
    max_num = max_number(n)
    table = [[[] for j in range(n + 1)] for i in range(max_num + 1)]
    for num in range(2,max_num + 1):
        for current_n in range(get_accu(num),n + 1):
            if num == 2:
                table[num][current_n] = table[num][current_n - 1][:]
                if (current_n - 3) % 2 == 0:
                    table[num][current_n].append(1)
            else:
                i = 1
                while get_accu(num, i) <= current_n:
                    table[num][current_n].append(sum(table[num-1][current_n-i][i:]))
                    i += 1
    for i in range(2, max_num + 1):
        count += sum(table[i][n])
    return count

def max_number(n):
    i = 1
    accu = 1
    while True:
        if accu > n:
            return i
        i +=1
        accu += i

def get_accu(number, start = 1):
    accu = 0
    for i in range(start, number + start):
        accu += i
    return accu
