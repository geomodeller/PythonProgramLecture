# fine duplicate
def find_duplicate(lst: list) -> list:
    """function to find duplicated elements

    Args:
        lst (list): input list

    Returns:
        list: list of elements that are duplciated 
    """
    lst_new = []
    lst_duplicated = []
    for element in lst:
        if element in lst_new:
            if not element in lst_duplicated:
                lst_duplicated.append(element)
        else:
            lst_new.append(element)
    return lst_duplicated

my_lst = [1, 2, 3, 1, 1, 1, 4, 2]
my_duplicated_lst = find_duplicate(my_lst)
print(my_duplicated_lst)