first = int(input("Введите первый элемент: "))
step = int(input("Введите шаг: "))
len = int(input("Введите длину: "))

def res(x,y,z):
    result = []
    for i in range(0,z):
        result.append(x)
        x = x + y
    return result

print(res(first,step,len))
print(first)