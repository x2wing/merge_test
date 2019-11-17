def BubleSort(V):
    counter = 0
    for i in range(V.__len__()):
        # print(len(V))
        F = 0
        for j in range(1, V.__len__() - i):
            counter += 1
            if V[j - 1] > V[j]:
                V[j - 1], V[j] = V[j], V[j - 1]  # обмен
                F = 1

        if F == 0:
            print("counter=", counter)
            return
    print("counter=", counter)


def InsertionSort(V):
    counter = 0
    for i in range(1, V.__len__()):
        j = i

        while j > 0 and V[j] < V[j - 1]:
            counter += 1
            V[j - 1], V[j] = V[j], V[j - 1]
            j -= 1

    print("counter=", counter)