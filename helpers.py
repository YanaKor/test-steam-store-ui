def convert_to_numbers(price_list):
    result = []
    for price_str in price_list:
        price_str = price_str.replace(',', '.')
        print(price_str)
        price = price_str[:-1]
        print(price)
        result.append(price)
    return result


def is_sorted_descending(lst):
    for i in range(len(convert_to_numbers(lst)) - 1):
        if lst[i] < lst[i + 1]:
            return False
    return True
