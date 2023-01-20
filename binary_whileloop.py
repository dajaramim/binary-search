# una función que toma una lista y busca un parámetro
# multiples variables : middle, start, end, steps
# recursion or while loop
# incrementar los steps cada vez que se realice una division
# condiciones para encontrar ella posición del valor buscado

def binary_search(list, element):
    middle = 0
    start = 0
    end = len(list)
    steps = 0

    while(start <= end): #mientras que el comienzo de la lista (que va siendo actualizada) sea menor a el largo de la lista.
        print("Step", steps, ":", str(list[start:end + 1]))
        steps = steps + 1
        middle = (start + end) // 2
        if element == list[middle]:
            return middle
        if element < list[middle]:
            end = middle - 1 # se resta porque si no es el elemento de al medio y es menor, va a buscar en una lista con un número menor al de middle
        else:
            start = middle + 1 
    return -1

my_list = [1,2,3,4,5,6,7,8,9,10,11,12]
target = 12

binary_search(my_list, target)

