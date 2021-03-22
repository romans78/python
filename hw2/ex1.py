data_list = [1, True, 1.0, "string", None, (2, 3), {4, 5}, [0, "p"], 1 + 1j, {1: "1", 2: "2"}, b"bytes"]
for data in data_list:
    print(data, ": type -", type(data))
