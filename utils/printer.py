#!/usr/div/env python3


class Printer:
    def __init__(self, users):
        self._list = users

    def show_printer_menu(self):
        print('Please enter one of the following options:\n')
        print('F -> sort by first name')
        print('L -> sort by last name')
        print('I -> sort by personal id')
        print('S -> sort by student id')
        print('E -> exit')

    def get_user_input(self):
        user_input = input()
        return user_input

    def show_sub_menu(self):
        print('Would you like to sort the list in reverse:\n')
        print('Y -> yes')
        print('N -> no')

    def print_sorted_list(self, user_input):
        self.show_sub_menu()
        sub_input = self.get_user_input()
        is_reverse = False
        if sub_input == 'Y' or sub_input == 'y':
            is_reverse = True

        if user_input == 'F' or user_input == 'f':
            self._list.sort(key=lambda x: x.get_first_name(), reverse=is_reverse)
            for s in self._list:
                print(s)
        elif user_input == 'L' or user_input == 'l':
            self._list.sort(key=lambda x: x.get_last_name(), reverse=is_reverse)
            for s in self._list:
                print(s)
        elif user_input == 'I' or user_input == 'i':
            self._list.sort(key=lambda x: x.get_personal_id(), reverse=is_reverse)
            for s in self._list:
                print(s)
        elif user_input == 'S' or user_input == 's':
            self._list.sort(key=lambda x: x.get_student_id(), reverse=is_reverse)
            for s in self._list:
                print(s)
        else:
            return

