import random

def binary_search(list, beginning, end, objective):
    if beginning > end:
        return False

    mid = (beginning + end) // 2

    if list[mid] == objective:
        return True
    elif list[mid] < objective:
        return binary_search(list, mid +1, end, objective)
    else:
        return binary_search(list, beginning, mid - 1, objective)



if __name__ == '__main__':
    list_size = int(input('Set the list size: '))
    objective = int(input("Which number you want to find? "))

    list = sorted([random.randint(0,100) for i in range(list_size)])

    match = binary_search(list, 0, len(list), objective)

    print(list)
    print(f'The element {objective} {"is" if match else "is not"} in the list')