#!/usr/div/env python3
from classes.human import Human


class Citizen(Human):
    def __init__(self, first_name: str, last_name: str, personal_id: int, gender=None):
        super().__init__(first_name, last_name, gender)
        self._personal_id = self.set_personal_id(personal_id)

    def set_personal_id(self, personal_id: int):
        if str(personal_id).isnumeric():
            if len(str(personal_id)) != 9:
                raise TypeError("ERROR: personal id must contain 9 digits: {}".format(personal_id))
            else:
                # personal_id = int(personal_id)
                return personal_id
        else:
            raise TypeError("ERROR: personal id must contain digits only: {}".format(personal_id))

    def get_personal_id(self):
        return self._personal_id

    def get_keys(self):
        # DEBUG:
        # print(self.__dict__)
        return self.__dict__.keys()

    def get_values(self):
        return self.__dict__.values()

    def get_items(self):
        return self.__dict__.items()

    def get_param(self, key):
        return self.__dict__.get(key)

    def set_param(self, key, value):
        if value is not None:
            self.__dict__.__setitem__(key, value)
        else:
            raise TypeError("Value can not be None: {}".format(key))

    def set_params(self, **kwargs):
        for key in kwargs:
            if kwargs.get(key) is not None:
                self.__dict__.__setitem__(key, kwargs.get(key))
            else:
                raise TypeError("Value can not be None: {}".format(key))
