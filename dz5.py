# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# first = int(input("Введите первый элемент: "))
# step = int(input("Введите шаг: "))
# len = int(input("Введите длину: "))

# def res(x,y,z):
#     result = []
#     for i in range(0,z):
#         result.append(x)
#         x = x + y
#     return result

# print(res(first,step,len))


# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

def do_deap(x,y):
    res = []
    if y <= x:
        for i in range(y,x+1):
            res.append(i)
    else:        
        for i in range(x,y+1):
            res.append(i)
    return res

data = [int(i) for i in input("Введите числа:").split() ]

start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона диапазона: "))

result = []

diap = do_deap(start,end)
    
    

for i in range(0,len(data)):
    if data[i] in diap:
        result.append(i)


print(result)







