import os

DEEP = "deep"
FILE_MSG = "insert the path of the wanted folder"


def thisIsTheWay() -> object:
    # function to read the path and create a list of the files that start with deep
    # and prints them
    folder_path = input("insert the path of the wanted folder")
    dir_list = os.listdir(folder_path)
    starts_with_deep = [f for f in dir_list if f.startswith(DEEP)]
    print(starts_with_deep)


if __name__ == '__main__':
    thisIsTheWay()
