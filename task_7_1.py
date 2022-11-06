from random import randint
from timeit import timeit
list_obj = [randint(-100, 100) for _ in range(100)]

def bubble_sort(lst_obj):
    for i in range(len(list_obj)):
        for j in range(len(lst_obj) - 1):
            if lst_obj[j] < lst_obj[j + 1]:
                lst_obj[j], lst_obj[j + 1] = lst_obj[j + 1], lst_obj[i]
    return lst_obj

# доработанная функция
def bubble_update_sort(lst_obj):
    flag = True
    while flag:
        flag = False
        for i in range(len(lst_obj) - 1):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                flag = True
    return lst_obj

list_obj_sort = bubble_sort(list_obj[:])
print(list_obj)
print(list_obj_sort)
print(bubble_update_sort(list_obj[:]))

print(timeit("bubble_sort(list_obj[:])", globals=globals(), number=1000))               # 2.7985600000001796
print(timeit("bubble_update_sort(list_obj[:])", globals=globals(), number=1000))        # 2.960869100000309
print(timeit("bubble_update_sort(list_obj_sort[:])", globals=globals(), number=1000))   # 0.03372280000075989

"""
Замеры показали, что оптимизированная функция работает немного дольше функции до оптимизации. Но, если на вход 
оптимизированная функция получит упорядоченный список, тогда она отработает намного эффективнее. На основании 
вышеизложенного можно сделать вывод, что использовать оптимизированную функцию не имеет смысла, т.к. вероятность 
получить упорядоченный список с длиной массива 100 элементов минимальна. 
"""