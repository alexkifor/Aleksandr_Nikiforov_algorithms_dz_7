from timeit import timeit
from random import randint
from statistics import median

m_1 = 5
m_2 = 50
m_3 = 500
# функция по созданию массива размером 2m + 1, где m - натуральное число
def add_list(num: int):
    return [randint(-100, 100) for _ in range(2 * num + 1)]

lst_10 = add_list(m_1)
lst_100 = add_list(m_2)
lst_1000 = add_list(m_3)

# нахождение медианны через сортировку Гномья

def gnome_sort(arr, m):
    i, j, size = 1, 2, len(arr)
    while i < size:
        if arr[i - 1] <= arr[i]:
            i, j = j, j + 1
        else:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            i -= 1
            if i == 0:
                i, j = j, j + 1
    return arr[m]


print(gnome_sort(lst_10[:], m_1))    # 7
print(gnome_sort(lst_100[:], m_2))   # -11
print(gnome_sort(lst_1000[:], m_3))  # -2
print(timeit("gnome_sort(lst_10[:], m_1)", globals=globals(), number=10))      # 0.00019999995129182935
print(timeit("gnome_sort(lst_100[:], m_2)", globals=globals(), number=10))    # 0.01752130000386387
print(timeit("gnome_sort(lst_1000[:], m_3)", globals=globals(), number=10))  # 1.9159484999836423

# нахождение медианы без сортировки

def find_median(lst, m):
    for i in range(m):
        lst.pop(lst.index(max(lst)))
    return max(lst)

print(find_median(lst_10[:], m_1))    # 7
print(find_median(lst_100[:], m_2))   # -11
print(find_median(lst_1000[:], m_3))  # 2
print(timeit("find_median(lst_10[:], m_1)", globals=globals(), number=10))   # 6.900000153109431e-05
print(timeit("find_median(lst_100[:], m_2)", globals=globals(), number=10))  # 0.00208910001674667
print(timeit("find_median(lst_1000[:], m_3)", globals=globals(), number=10)) # 0.18048179999459535

# нахождение медианы с помощью встроенной функции

print(median(lst_10[:]))     # 7
print(median(lst_100[:]))    # -11
print(median(lst_1000[:]))   # 2
print(timeit("median(lst_10[:])", globals=globals(), number=10))   # 1.969997538253665e-05
print(timeit("median(lst_10[:])", globals=globals(), number=10))   # 1.7900019884109497e-05
print(timeit("median(lst_10[:])", globals=globals(), number=10))   # 1.71000137925148e-05

"""
Самой быстрой оказалась встроенная функция median, что не удивительно, на то она и встроенная функция,
на втором месте нахождение медианы без сортировки и самая медденная(примерно в 10 раз медленне функции
без сортировки) функция с сортировкой.
"""
