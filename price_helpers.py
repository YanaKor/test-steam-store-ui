def convert_to_numbers(price_list):
    result = []
    for price_str in price_list:
        if 'Цена для вас:' in price_str:
            price_str = price_str.replace("Цена для вас:\n", '').replace(',', '.').replace(' ', '')
        else:
            price_str = price_str.replace("Your Price:\n", '').replace(',', '.').replace(' ', '')
        price = price_str[:-1]
        new_price = float(price)
        result.append(new_price)
    return result


def is_sorted_descending(lst):
    new_lst = convert_to_numbers(lst)
    print(new_lst)
    for i in range(len(new_lst) - 1):
        print(new_lst[i])
        if new_lst[i] < new_lst[i + 1]:
            return False
    return True
