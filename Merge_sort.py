import random

def merge_sort(list):

    if len(list) > 1:
        mid = len(list) // 2
        left_list = list[:mid]
        right_list= list[mid:]

        merge_sort(left_list)
        merge_sort(right_list)

        left_iterator = 0
        right_iterator = 0
        main_iterator = 0

        while left_iterator < len(left_list) and right_iterator < len(right_list):
            if left_list[left_iterator] < right_list[right_iterator]:
                list[main_iterator] = left_list[left_iterator]
                left_iterator += 1
            else:
                list[main_iterator] = right_list[right_iterator]
                right_iterator += 1

            main_iterator += 1

        while left_iterator < len(left_list):
            list[main_iterator] = left_list[left_iterator]
            left_iterator += 1
            main_iterator += 1

        while right_iterator < len(right_list):
            list[main_iterator] = right_list[right_iterator]
            right_iterator += 1
            main_iterator += 1
    
    return (list)

def run():  

    list_size = int(input('Set the list size: '))

    list = [random.randint(0,100) for i in range(list_size)]

    print(list)

    ordered_list = merge_sort(list)

    print(ordered_list)

if __name__ == '__main__':
    run()