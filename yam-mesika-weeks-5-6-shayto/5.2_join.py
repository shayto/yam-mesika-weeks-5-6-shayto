def join(*lists, sep='-'):
    """
    function that receives unlimited lists and if gets also seperator parameter
    combines them with seperator between each list.
    :param lists: unlimited lists
    :param sep: seperator parameter (optional, default- ('-').
    :return: list with seperator in the end (without the last character)
    """

    new_list_with_seperator = [lst for curr_list in lists for lst in curr_list + [sep]][:-1]
    if not new_list_with_seperator:
        return 'none'
    return new_list_with_seperator


if __name__ == '__main__':
    print(join([1, 2], [8], [9, 5, 6], sep='^'))

