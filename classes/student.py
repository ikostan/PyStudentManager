#!/usr/div/env python3
from classes.citizen import Citizen


class Student(Citizen):
    def __init__(self, kwargs):
        # print('Student constructor #1 called')
        # first_name: str, last_name: str, gender: str, personal_id: int
        super().__init__(kwargs.get('_first_name'),
                         kwargs.get('_last_name'),
                         kwargs.get('_personal_id'),
                         kwargs.get('_gender'))

        for key in kwargs.keys():
            if key == '_student_id':
                if kwargs.get(key) is not None:
                    # DEBUG:
                    # print('Student constructor: {} > {}'.format(key, kwargs.get(key)))
                    # self.__dict__.__setitem__(key, kwargs.get(key))
                    self._student_id = self.set_student_id(kwargs.get('_student_id'))
                else:
                    raise TypeError("Value can not be None: {}".format(key))
            elif key == '_major':
                if kwargs.get(key) is not None:
                    # DEBUG:
                    # print('Student constructor: {} > {}'.format(key, kwargs.get(key)))
                    # self.__dict__.__setitem__(key, kwargs.get(key))
                    self._major = self.set_major(kwargs.get('_major'))
                else:
                    raise TypeError("Value can not be None: {}".format(key))

    def set_student_id(self, student_id: int):
        if str(student_id).isnumeric():
            if len(str(student_id)) != 9:
                raise TypeError("ERROR: student id must contain 9 digits: {}".format(student_id))
            else:
                # student_id = int(student_id)
                return student_id
        else:
            raise TypeError("ERROR: student id must contain digits only: {}".format(student_id))

    def get_student_id(self):
        return self._student_id

    def set_major(self, major):
        if len(major) < 4:
            raise TypeError("ERROR: student id must contain 4 characters: {}".format(major))
        else:
            return major

    def get_major(self):
        return self._major


