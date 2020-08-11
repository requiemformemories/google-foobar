def solution(total_lambs):
    return be_stingy(total_lambs) - be_generous(total_lambs)

def be_generous(total_lambs):
    number_of_henchmen = 0
    paid = 1
    while True:
        if total_lambs < paid:
            return number_of_henchmen
        total_lambs -= paid
        paid *= 2
        number_of_henchmen += 1

def be_stingy(total_lambs):
    number_of_henchmen = 0
    paid = [1]
    while True:
        if total_lambs < paid[len(paid) - 1]:
            return number_of_henchmen
        total_lambs -= paid[len(paid) - 1]
        if len(paid) == 1:
            paid.append(1)
        else:
            paid.append(paid[len(paid) - 1] + paid[len(paid) - 2])
        number_of_henchmen += 1
