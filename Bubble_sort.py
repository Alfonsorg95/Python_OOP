import random

def bubble_sort(list):
    
    for i in range(len(list)):
        for j in range(0,len(list) - i - 1):

            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    
    return (list)

def run():  

    list_size = int(input('Set the list size: '))

    list = [random.randint(0,100) for i in range(list_size)]

    print(list)

    ordered_list = bubble_sort(list)

    print(ordered_list)

if __name__ == '__main__':
    run()