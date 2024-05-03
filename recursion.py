def euclid_algorithm(length, breadth):
    if length == 2 * breadth:
        return breadth
    else:
        temp = breadth
        breadth = length % breadth
        length = temp

        return euclid_algorithm(length, breadth)


print(euclid_algorithm(1680, 640))
