def join(*lists, sep='-'):
    # function that receives unlimited lists and if gets also seperator parameter
    # combines them with seperator between each list.
    # the function get Unlimited lists and Seperator - separate between each list
    # function returns the list with seperator in the end (without the last character)
    new_list = [lst for curr_list in lists for lst in curr_list + [sep]][:-1]
    if new_list == []:
        return 'none'
    return new_list


if __name__ == '__main__':
    print(join([1, 2], [8], [9, 5, 6], sep='^'))
