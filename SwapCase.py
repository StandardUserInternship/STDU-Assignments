def swap_case_string(str1):
    result_str = " "
    for item in str1:
        if item.isupper():
            result_str += item.lower()
        else:
            result_str += item.upper()
    return result_str
print(swap_case_string("Swap Case Lab Exercise"))
print(swap_case_string("Corbyn Yip"))