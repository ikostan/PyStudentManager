#!/usr/div/env python3
from human import Human


class Citizen(Human):
    def __init__(self, first_name: str, last_name: str, gender: str, personal_id: int):
        super().__init__(first_name, last_name, gender)
        self._personal_id = self.set_id(personal_id)

    def set_id(self, personal_id: int):
        if personal_id.isnumeric():
            if len(str(personal_id)) == 9:
                return int(personal_id)
            else:
                raise TypeError("ERROR: id must contain 9 digits: {}".format(personal_id))
        else:
            raise TypeError("ERROR: id must contain 9 digits: {}".format(personal_id))

    def get_id(self):
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
