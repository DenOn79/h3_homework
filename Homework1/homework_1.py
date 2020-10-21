

def catalog_finder(url_list):
    """
    Дописать функцию, которая принимает список URL, а возвращает
    список только тех URL, в которых есть /catalog/
    """
    # your code here
    word = 'catalog'
    if word in url_list.split('/'):
        result_list = url_list
    else:
        result_list = None
    return result_list


def get_str_center(input_str):
    """
    Дописать функцию, которая вернет Х символов из середины строки
    (2 для четного кол-ва символов, 3 - для нечетного).
    """
    # your code here
    length = len(input_str)
    if length % 2:
        output_str = input_str[(length//2)-1:(length//2)+2]
    else:
        output_str = input_str[(length//2)-1:(length//2)+1]
    return output_str


def count_symbols(input_str):
    """
    Дописать функцию, которая считает сколько раз каждая из букв
    встречается в строке, разложить буквы в словарь парами
    {буква:количество упоминаний в строке}
    """
    # your code here
    output_dict = dict()
    for letter in input_str:
        letter_number = input_str.count(letter)
        output_dict.update({letter: letter_number})
    return output_dict


def mix_strings(str1, str2):
    """
    Дописать функцию, которая будет принимать 2 строки и вставлять вторую
    в середину первой
    """
    length = len(str1)
    half1_str1 = str1[:length//2]
    half2_str1 = str1[length//2:length+1]
    result_str = f"{half1_str1}{str2}{half2_str1}"
    return result_str


def even_int_generator():
    """
    Сгенерировать список из диапазона чисел от 0 до 100 и записать
    в результирующий список только четные числа.
    """
    # your code here
    even_int_list = [i for i in range(0, 101) if not i % 2]
    return even_int_list
