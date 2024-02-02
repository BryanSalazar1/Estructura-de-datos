mi_lista = [2,1,3,4,5,3,9]

n = len(mi_lista)
for i in range(n - 1):
    min_index = i
    for j in range(i + 1, n):
        if mi_lista[j] < mi_lista[min_index]:
            min_index = j
    mi_lista[i], mi_lista[min_index] = mi_lista[min_index], mi_lista[i]

print( mi_lista)