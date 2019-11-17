def checker(V):
    for i in range(1, len(V)):
        if V[i - 1] > V[i]:
            print("сортировка говно")
            return


def checker_r(V, ascending=False):
    for i in range(1, len(V)):
        if ascending ^ (V[i - 1] > V[i]):
            print("сортировка говно")
            return
