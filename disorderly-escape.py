from fractions import Fraction

def solution(w, h, s):
    result = 0
    for width_list in combinations(w):
        for height_list in combinations(h):
            sum = 0
            for width in width_list:
                for height in height_list:
                    sum += gcd(width, height)
            result += Fraction(s ** sum, redundant_divide(width_list) * redundant_divide(height_list))
    return result

def factoral(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result

def gcd(num1, num2):
    while num2 != 0:
        t = num2
        num2 = num1 % num2
        num1 = t
    return num1

def combinations(number):
    result= []
    stack = [[[], number, 1]]
    while len(stack) > 0:
        previous_array, current_num, upper_bound = stack.pop()
        result.append(previous_array + [current_num])
        for i in range(upper_bound, current_num//2 + 1):
            stack.append([previous_array + [i], current_num - i, i])
    return result

def element_count_list(number_list):
    return [[i, number_list.count(i)] for i in list(set(number_list))]

def redundant_divide(combination):
    result = 1
    for current_num, times in element_count_list(combination):
        result *= current_num ** times * factoral(times)
    return result
