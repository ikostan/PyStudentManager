#!/usr/div/env python3
from utils.main_menu import Menu
from utils.file_manager import FileManager


def main():
    print("Testing program: Student registration\n")

    students = FileManager.read_file('students.txt')

    '''
    # DEBUG:
    for std in students:
        print(std)
    '''

    menu = Menu(students)
    menu.main_menu()


if __name__ == '__main__':
    main()
