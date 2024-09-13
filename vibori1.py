class Uchastok:
    def __init__(self):
        self.nHouse = 0
        self.summaGolosov = 0
        self.selected = False


def sum_from_left_while_negative(array1, left_side, first, last):
    for i in range(first, last):
        left_side.summaGolosov += array1[i]
        left_side.nHouse += 1
        if left_side.summaGolosov > 0:  # +???sum(+)
            left_side.selected = True
            break
    return left_side


def sum_from_right_while_negative(array1, right_side, first, last):
    for i in reversed(range(first, last)):  # ищем от конца
        right_side.summaGolosov += array1[i]
        right_side.nHouse += 1
        if right_side.summaGolosov > 0:
            right_side.selected = True
            break
    return right_side


def kill_negative_from_right(array1, left_side, len_right_side):
    len_array = len(array1) - len_right_side - 1  # 1 - N2.nHouse
    for i in range(left_side.nHouse, len_array):
        if array1[i] > 0:
            break
        left_side.summaGolosov += array1[i]
        left_side.nHouse += 1
        if left_side.summaGolosov <= 0:
            left_side.summaGolosov -= array1[i]
            left_side.nHouse -= 1
            break
    return left_side


def kill_negative_from_left(array1, right_side, len_left_side):
    len_array = len(array1) - right_side.nHouse
    for i in reversed(range(len_left_side + 1, len_array)):  # 1 - N2.nHouse
        if array1[i] > 0:
            break
        right_side.summaGolosov += array1[i]
        right_side.nHouse += 1
        if right_side.summaGolosov <= 0:
            right_side.summaGolosov -= array1[i]
            right_side.nHouse -= 1
            break
    return right_side


N1 = Uchastok()
N2 = Uchastok()
N3 = Uchastok()
"""
N = int(input())
for i in range(N):
    golos.append(int(input()))
"""
N = 7
golos = [2, -3, 1, -3, -1, -5, -4]
print(golos)

#  Холява
if golos[0] > 0:  # +??????
    N1.selected = True
N1.summaGolosov = golos[0]
N1.nHouse = 1
if golos[N - 1] > 0:  # ??????+
    N3.selected = True
N3.summaGolosov = golos[N - 1]
N3.nHouse = 1
if N1.selected and (golos[1] > 0):  # ++..................
    print("N1 =", 1, ", N2 =", 1, ", N3 =", N - 2)
    exit()
if N3.selected and (golos[N - 2] > 0):  # ..............++
    print("N1 =", N - 2, ", N2 =", 1, ", N3 =", 1)
    exit()
if N3.selected and N1.selected:  # +..................+
    print("N1 =", 1, ", N2 =", N - 2, ", N3 =", 1)
    exit()
#  Конец холявы
#  Холява с одного конца
if N1.selected:  # +-.................-
    N1 = kill_negative_from_right(golos, N1, N3.nHouse)
    if golos[N1.nHouse] > 0:  # sum(+)+...............-
        print("N1 =", N1.nHouse, ", N2 =", 1, ", N3 =", N - N1.nHouse - 1)
        exit()
    N3 = sum_from_right_while_negative(golos, N3, N1.nHouse + 1, N - 1)  # sum(+)-...............-
    if N3.selected:  # sum(+)-...sum(+)
        print("N1 =", N1.nHouse, ", N2 =", N - N1.nHouse - N3.nHouse, ", N3 =", N3.nHouse)
        exit()
    else:  # sum(+)-...sum(-)
        N2 = sum_from_left_while_negative(golos, N2, N1.nHouse, N - 1)
        if N2.selected:  # sum(+)sum(+)???-
            print("N1 =", N1.nHouse, ", N2 =", N2.nHouse, ", N3 =", N - N2.nHouse - N1.nHouse)
            exit()
        else:  # sum(+)sum(-)sum(-)
            print(0)
            exit()
elif N3.selected:  # -.................-+
    N3 = kill_negative_from_left(golos, N3, N1.nHouse)
    if golos[N - N3.nHouse - 1] > 0:  # -...............+sum(+)
        print("N1 =", N - N3.nHouse - 1, ", N2 =", 1, ", N3 =", N3.nHouse)
        exit()
    N1 = sum_from_left_while_negative(golos, N1, 1, N - N3.nHouse - 1)  # -...............-sum(+)
    if N1.selected:  # sum(+)-...sum(+)
        print("N1 =", N1.nHouse, ", N2 =", N - N1.nHouse - N3.nHouse, ", N3 =", N3.nHouse)
        exit()
    else:  # sum(-)-...sum(+)
        N2 = sum_from_right_while_negative(golos, N2, 1, N - N3.nHouse)
        if N2.selected:  # sum(+)sum(+)???-
            print("N1 =", N - N2.nHouse - N3.nHouse, ", N2 =", N2.nHouse, ", N3 =", N3.nHouse)
            exit()
        else:  # sum(+)sum(-)sum(-)
            print(0)
#  Конец холявы с одного конца
N1 = sum_from_left_while_negative(golos, N1, N1.nHouse, N - 2)
if N1.selected:
    N1 = kill_negative_from_right(golos, N1, 1)
    N3 = sum_from_right_while_negative(golos, N3, N1.nHouse + 1, N - N3.nHouse)
    if N3.selected:
        print("N1 =", N1.nHouse, ", N2 =", N - N1.nHouse - N3.nHouse, ", N3 =", N3.nHouse)
        exit()
    else:
        N2 = sum_from_left_while_negative(golos, N2, N1.nHouse, N - 1)
        if N2.selected:
            print("N1 =", N1.nHouse, ", N2 =", N2.nHouse, ", N3 =", N - N1.nHouse - N2.nHouse)
            exit()
        else:
            print(0)
else:
    N3 = sum_from_right_while_negative(golos, N3, 2, N - N3.nHouse)
    if N3.selected:
        N3 = kill_negative_from_left(golos, N3, N1.nHouse)
        N2 = sum_from_right_while_negative(golos, N2, 1, N - N3.nHouse)
        print("N1 =", N - N2.nHouse - N3.nHouse, ", N2 =", N2.nHouse, ", N3 =", N3.nHouse)
    else:
        print(0)












