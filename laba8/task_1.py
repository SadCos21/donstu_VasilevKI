from random import randint

def InvertDigits(K: int) -> int: # фунция перестановки цифр в обратном порядке в числе
    temp = 0
    flag = 1
    if K < 0: 
        flag = -1
        K *= -1
    while K !=0:
        temp = K % 10 + temp*10
        K = K // 10
    return temp*flag

def numbers() -> list: # фунция создания списка из 5-ти чисел
    arr = []
    for i in range(5):
        arr.append(randint(-1000,1000))
    return arr

def print_value(arr: list) -> list: # фунция вывода инвертированных чисел
    for i in range(len(arr)):
        arr[i] = InvertDigits(arr[i])
    print(arr)

arr = numbers()
print(arr)
print_value(arr)