#!/usr/div/env python3


class Person:
    def __init__(self, first_name: str, last_name: str, gender: str, id: int):
        self._first_name = self.set_name(first_name)
        self._last_name = self.set_name(last_name)
        self._gender = self.set_gender(gender)
        self._id = self.set_id(id)

    def set_id(self, id: int):
        if id.isnumeric():
            if len(str(id)) == 9:
                return int(id)
            else:
                raise TypeError("ERROR: id must contain 9 digits: {}".format(id))
        else:
            raise TypeError("ERROR: id must contain 9 digits: {}".format(id))

    def get_id(self):
        return self._id

    def set_gender(self, gender: str):
        if gender == 'Male' or gender == 'male':
            self._gender = 'male'
        elif gender == 'Female' or gender == 'female':
            self._gender = 'female'
        else:
            self._gender = 'unknown'
        return self._gender

    def get_gender(self):
        return self._gender

    def set_name(self, name: str):
        if len(name) < 2 or name is None:
            raise TypeError("ERROR: name must be at least 2 chars long: {}".format(name))
        else:
            if not name.isalpha():
                raise TypeError("ERROR: name must contain alphabetic chars only: {}".format(name))
            else:
                new_name = name.strip().capitalize()
                # print('Debug >>> set_name: {}'.format(new_name))
                return new_name

    def get_last_name(self):
        return self._last_name

    def get_first_name(self):
        return self._first_name
