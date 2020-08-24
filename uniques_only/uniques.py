def uniques_only(input_list):
    unique_list = list()
    for val in input_list:
        if val not in unique_list:
            unique_list.append(val)
    return unique_list