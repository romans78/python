def transform_list(orig_list):
    return [orig_list[n] for n in range(1, len(orig_list)) if orig_list[n] > orig_list[n - 1]]


orig_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

print(f"Изменённый список: {transform_list(orig_list)}")
