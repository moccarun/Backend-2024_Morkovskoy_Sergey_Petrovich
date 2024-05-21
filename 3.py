def max_sum_of_two(numbers):
    sorted_numbers = sorted(numbers)
    return sorted_numbers[-1] + sorted_numbers[-2]

example_list = [2, 7, 4, 1, 8]
result = max_sum_of_two(example_list)
print(result)  
