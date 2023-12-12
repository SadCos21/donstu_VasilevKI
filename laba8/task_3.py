def numbers(temp: list): # фунция ввода последовательности
    n = int(input())
    if n == 0:
        return temp
    temp.append(n)
    return numbers(temp)

def invert(array): # функция ввывода последовательности в обратном порядке
    i = -1
    while i >= (-1)*len(array):
        print(array[i])
        i -= 1

arr = []
numbers(arr)
invert(arr)
# коммент ради коммента на гите