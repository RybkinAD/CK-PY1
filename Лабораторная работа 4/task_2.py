def get_count_char(str_):
    """
    Creates a dictionary from a string.
    :param str_: Initial string.
    :return: Dictionary: key - letter;
                         value - number of letters in the string.
    """
    list_ = str_.lower().split()
    str_ = ''.join(list_)
    dict_ = {}
    for i in range(len(str_)):
        if str_[i].isalpha():
            if str_[i] in dict_:
                dict_[str_[i]] += 1
            else:
                dict_.update({str_[i]: 1})
    return dict_


def percent_letter(dictionary):
    """
    Creates a dictionary from a dictionary.
    :param dictionary: Initial dictionary.
    :return: Dictionary: key - letter;
                         value - percent of letters in the string.
    """
    sum_ = sum(list(dictionary.values()))
    list_ = list(dictionary)
    for i in range(len(dictionary)):
        dictionary[list_[i]] = round(dictionary[list_[i]] / sum_ * 100, 1)
    return dictionary


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print(get_count_char(main_str))
#print(percent_letter(get_count_char(main_str)))
#print('Проверка: ' + (str(round(sum(list(percent_letter(get_count_char(main_str)).values()))))))
