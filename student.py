#!/usr/div/env python3
from citizen import Citizen


class Student(Citizen):

    def __init__(self, kwargs):
        # print('Student constructor #1 called')
        # first_name: str, last_name: str, gender: str, id: int
        super().__init__(kwargs.get('_first_name'),
                         kwargs.get('_last_name'),
                         kwargs.get('_gender'),
                         kwargs.get('personal_id'))
        for key in kwargs.keys():
            if key != '_first_name' and key != '_last_name' and key != '_id' and key != '_gender':
                if kwargs.get(key) is not None:
                    # DEBUG:
                    # print('Student constructor: {} > {}'.format(key, kwargs.get(key)))
                    self.__dict__.__setitem__(key, kwargs.get(key))
                else:
                    raise TypeError("Value can not be None: {}".format(key))

    '''
    def __init__(self, first_name: str, last_name: str, student_id: int):
        print('Student constructor #2 called')
        self.set_initial_data(first_name, last_name, student_id)       
        
    def __init__(self, first_name: str, last_name: str, student_id: int, **kwargs):
        print('Student constructor #3 called')
        self.set_initial_data(first_name, last_name, student_id)
        for key in kwargs:
            if kwargs.get(key) is not None:
                self.__dict__.__setitem__(key, kwargs.get(key))
            else:
                raise TypeError("Value can not be None: {}".format(key))
    '''

    def __str__(self):
        data = None
        for k in self.__dict__:
            if data is None:
                data = '{}: {}'.format(k, str(self.__dict__.get(k)))
            else:
                data = '{}; {}: {}'.format(data, k, str(self.__dict__.get(k)))
        return data

    def set_student_id(self, student_id: int):
        if len(str(student_id)) != 9:
            raise TypeError("ERROR: student id must contain 9 digits: {}".format(student_id))
        else:
            student_id = int(student_id)
            return student_id
    '''
        def set_initial_data(self, first_name: str, last_name: str, student_id: int):
        if first_name is not None and last_name is not None and student_id is not None:
            self.set_param('_first_name', self.set_name(first_name.strip()))
            self.set_param('_last_name', self.set_name(last_name.strip()))
            self.set_param('_student_id', self.set_student_id(student_id))
        else:
            raise TypeError("Value can not be None")
    '''

