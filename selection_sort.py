def selection_sort(array: list):
    def find_biggest(sub_array: list):
        biggest = sub_array[0]
        for i in range(1, len(sub_array)):
            if sub_array[i] > biggest:
                biggest = sub_array[i]
        return biggest

    ordered_array = list()
    array_length = len(array)
    for _ in range(array_length - 1):
        ordered_array.append(find_biggest(array))
        array.remove(ordered_array[-1])

    ordered_array += array
    return ordered_array


print(selection_sort([2, 1, 2, 5, 6, 2, 0]))
