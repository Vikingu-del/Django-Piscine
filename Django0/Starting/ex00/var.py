def my_var():
    type_int = 42
    type_str = "42"
    type_str_2 = "quarante-deux"
    type_str_2 = type_str_2.replace('a', 'b', 2)
    type_float = 42.0
    type_bool = True
    type_list = [42]
    type_dict = {42: 42}
    type_tuple = (42,)
    type_set = set()
    to_print = [type_int, type_str, type_str_2, type_float, type_bool, type_list, type_dict, type_tuple, type_set]
    for v in to_print:
        print(f"{v} has a type {type(v)}")

if __name__ == "__main__":
    my_var()

