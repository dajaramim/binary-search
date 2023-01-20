# una función que toma una lista y busca un parámetro
# multiples variables : middle, start, end, steps
# recursion or while loop
# incrementar los steps cada vez que se realice una division
# condiciones para encontrar ella posición del valor buscado

def binary_search(list, start,end, element, steps = 0):
    if end >= start:
        steps += 1
        print("Step: {}, {}".format(str(steps),str(my_list[start:end + 1]))) #se suma porque en la sintaxis de : el último valor no se cuenta
        middle = (end + start) // 2
        if list[middle] == element:
            return middle
        elif list[middle] > element:
            return binary_search(list, start, middle - 1, element, steps)
        else:
            return binary_search(list, middle + 1, end, element, steps)
    else:
        return - 1 # significa que elemento no está en el array


my_list = [1,2,3,4,5,6,7,8,9,10,11,12]
target = 5
print(binary_search(my_list, 0, len(my_list) - 1, target))