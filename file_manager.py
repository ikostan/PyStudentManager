#!/usr/div/env python3
from student import Student


class FileManager:
    @staticmethod
    def write_file(f_name, student):
        f = None
        try:
            f = open(f_name, 'a+')
            f.write('\n' + student.__str__())
        except Exception as e:
            print(e)
        finally:
            if f is not None:
                f.close()

    @staticmethod
    def read_file(f_name):
        students = []
        f = None
        try:
            f = open(f_name, 'r')
            for line in f.readlines():
                std_data = {}
                items = line.split('; ')
                for item in items:
                    params = item.split(': ')
                    std_data[params[0]] = params[1].strip()

                try:
                    students.append(Student(std_data))
                except Exception as e:
                    print(e)  # print error
                    # Debug:
                    print(type(std_data))
                    for d in std_data.items():
                        print(d)
                    print()

        except Exception as e:
            print(e)
        finally:
            if f is not None:
                f.close()
            return students
