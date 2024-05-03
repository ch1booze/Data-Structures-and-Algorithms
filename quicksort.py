def qsort(array):
    if len(array) < 2:
        return array
    else:
        pivot_index = len(array) // 2
        pivot = array[pivot_index]
        lt_array = list()
        gt_array = list()

        for index in range(len(array)):
            if index != pivot_index:
                if array[index] < pivot:
                    lt_array.append(array[index])
                else:
                    gt_array.append(array[index])

        return qsort(lt_array) + [pivot] + qsort(gt_array)
    

print(qsort([2, 7, 1, 4, 0, 5, 9, 3, 8, 6]))


        
