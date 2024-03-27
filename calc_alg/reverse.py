def reverse(list, start, end = None):
    start_index = start
    end_index = end

    if end is None:
        end_index = len(list) - 1

    middle_index = (start_index + end_index) // 2

    for i in range(start_index, middle_index):
        j = start_index + end_index - i
        list[i], list[j] = list[j], list[i]

    return list

print(reverse([1,2,3,4,5], 0, 3))
