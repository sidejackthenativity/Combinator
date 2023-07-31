def generate_combinations_2d(arr_2d):
    if not arr_2d or not all(arr_2d):
        return []

    rows = len(arr_2d) #3
    cols = max(len(row) for row in arr_2d) #3


    combinations = []

    for a in arr_2d[0]: #grab a value
        for b in range(1, rows): 
            for c in range(len(arr_2d[b])):
                next_element = arr_2d[b][c]
                combinations.append((f"{a}{a}{next_element}")*5)


    return combinations


# Example usage:
two_d_array = [['a1', 'a2', 'a3'], ['b1', 'b2', 'b3'], ['c1', 'c2']]
result = generate_combinations_2d(two_d_array)
print(result)
