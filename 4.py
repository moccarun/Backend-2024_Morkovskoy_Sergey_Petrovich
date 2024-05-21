def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return mid
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1

    return 'не найден'

sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target_element = 11
result_index = binary_search(sorted_list, target_element)
print(result_index)
