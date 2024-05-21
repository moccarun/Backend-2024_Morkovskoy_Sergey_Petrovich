def custom_sort(A, B):
    index_map = {value: index for index, value in enumerate(B)}

    present_in_B = []
    not_in_B = []

    for num in A:
        if num in index_map:
            present_in_B.append(num)
        else:
            not_in_B.append(num)

    present_in_B.sort(key=lambda x: index_map[x])

    not_in_B.sort(reverse=True)

    return present_in_B + not_in_B

A = [2, 4, 1, 3, 2, 4, 6, 7, 9, 2, 19]
B = [2, 1, 4, 3, 6, 9]

sorted_A = custom_sort(A, B)
print(sorted_A)
