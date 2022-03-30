import os


def thisIsTheWay() -> object:
    """
    function to read the file path and create a list of the files that start with deep
    and prints them.
    :return: none
    """
    folder_path = input("Insert the path of the wanted folder")
    files_list = os.listdir(folder_path)
    starts_with_deep = [file_path for file_path in files_list if file_path.startswith("deep")]
    print(starts_with_deep)


if __name__ == '__main__':
    thisIsTheWay()


