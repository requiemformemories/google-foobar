def solution(l):
    mod_1 = []
    mod_2 = []
    selected = []
    for num in l:
        if num % 3 == 1:
            mod_1.append(num)
        elif num % 3 == 2:
            mod_2.append(num)
        else:
            selected.append(num)
    mod_1.sort(reverse=True)
    mod_2.sort(reverse=True)
    selected += mod_1[:int(int(len(mod_1) /3) * 3)]
    selected += mod_2[:int(int(len(mod_2) /3) * 3)]
    mod_1 = mod_1[int(int(len(mod_1) /3) * 3):]
    mod_2 = mod_2[int(int(len(mod_2) /3) * 3):]
    shared = min(len(mod_1), len(mod_2))
    selected += mod_1[:shared]
    selected += mod_2[:shared]
    selected.sort(reverse=True)
    if len(selected) == 0:
        return 0
    return ''.join(str(x) for x in selected)
