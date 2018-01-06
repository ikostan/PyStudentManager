#!/usr/div/env python3
from utils.main_menu import Menu
from utils.file_manager import FileManager


def main():
    print("Testing program: Student registration\n")

    students = FileManager.read_file(r'files\students.txt')
    menu = Menu(students)
    menu.main_menu()


if __name__ == '__main__':
    main()
