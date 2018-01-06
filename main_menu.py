#!/usr/div/env python3
from student import Student
import time
from file_manager import FileManager


class Menu:
    def __init__(self, students):
        self._students = students

    def main_menu(self):
        print("Main menu:")
        while True:
            print('Please select one of the following options:\n'
                  '(R -> register, E -> exit, P -> print, F -> find)')
            user_input = input()

            if user_input == 'r' or user_input == 'R':
                std = self.register_student()
                self._students.append(std)
                print("Register a new student...")
                FileManager.write_file('students.txt', std)
            elif user_input == 'f' or user_input == 'F':
                self.find_student()
            elif user_input == 'p' or user_input == 'P':
                self.print_all_students()
            else:
                print("Exiting program...")
                time.sleep(1)
                exit()

    def register_student(self):
        std_data = {}
        first_name = None
        last_name = None
        student_id = None

        while first_name is None:
            print('Please enter student first name:')
            first_name = input()
            if len(first_name) < 2:
                print("ERROR: first name must be at least 2 chars long. Please reenter.")
                first_name = None
            else:
                if not first_name.isalpha():
                    print("ERROR: first name must contain alphabetic chars only. Please reenter.")
                    first_name = None
                else:
                    std_data['_first_name'] = first_name

        while last_name is None:
            print('Please enter student last name:')
            last_name = input()
            if len(last_name) < 2:
                print("ERROR: last name must be at least 2 chars long. Please reenter.")
                last_name = None
            else:
                if not last_name.isalpha():
                    print("ERROR: last name must contain alphabetic chars only. Please reenter.")
                    last_name = None
                else:
                    std_data['_last_name'] = last_name

        while student_id is None:
            print('Please enter student id:')
            student_id = input()
            if len(student_id) != 9:
                print("ERROR: student id must contain 9 digits. Please reenter.")
                student_id = None
            else:
                if student_id.isalpha():
                    print("ERROR: student id must contain digits only. Please reenter.")
                    student_id = None
                else:
                    student_id = int(student_id)
                    is_doubled = False
                    for std in self._students:
                        # print(std)
                        # print("{} <> {}".format(std.get_param('_student_id'), student_id))
                        if int(std.get_param('_student_id')) == student_id:
                            print("ERROR: student id is already exists: {}. Please reenter.".format(student_id))
                            student_id = None
                            is_doubled = True

                    if is_doubled is False:
                        std_data['_student_id'] = student_id

        try:
            return Student(std_data)
        except Exception as e:
            print(e)

    def find_student(self):
        print('Please choose one of the following options:')
        print('1. F - search by first name')
        print('2. L - search by last name')
        print('3. I - search by ID')
        print('4. E - back to main menu')

        user_input = input()
        param = None

        if user_input == 'F' or user_input == 'f':
            param = self.get_param('first name', param)
            # print('param: {}'.format(param))
            self.find_students(param, 1)
        elif user_input == 'L' or user_input == 'l':
            param = self.get_param('last name', param)
            self.find_students(param, 2)
        elif user_input == 'I' or user_input == 'i':
            param = self.get_param('ID', param)
            self.find_students(param, 3)
        else:
            self.main_menu()

    def find_students(self, param, search_param):
        # first_name, last_name, student_id
        # print("Total number of students in the search list: {}".format(len(self._students)))

        std_list = []
        if search_param == 1:
            for std in self._students:
                print('Search by first_name: {} -> {}'.format(param, std.get_param('_first_name')))
                if std.get_param('_first_name') == param:
                    std_list.append(std)
        elif search_param == 2:
            for std in self._students:
                # print('Search by last_name')
                if std.get_param('_last_name') == param:
                    std_list.append(std)
        else:
            for std in self._students:
                # print('Search by student_id')
                if int(std.get_param('_student_id')) == int(param):
                    std_list.append(std)
        # return std_list
        if len(std_list) > 0:
            for s in std_list:
                print(s)
        else:
            print('Zero results found.')
        print()
        self.find_student()

    def get_param(self, param_name, param):
        while param is None or param == '':
            print('Please enter student {}:\n'.format(param_name))
            param = input()
        return param

    def print_all_students(self):
        num = 1
        for std in self._students:
            print('#', num, '-> ', std)
            num += 1
        print()
