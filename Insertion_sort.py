import random

def insertion_sort(list):
    
    for i in range(1, len(list)):
        actual_value = list[i]
        actual_position = i

        while actual_position > 0 and list[actual_position -1] > actual_value:

            list[actual_position] = list[actual_position - 1]
            actual_position -= 1

        list[actual_position] = actual_value
    
    return (list)

def run():  

    list_size = int(input('Set the list size: '))

    list = [random.randint(0,100) for i in range(list_size)]

    print(list)

    ordered_list = insertion_sort(list)

    print(ordered_list)

if __name__ == '__main__':
    run()