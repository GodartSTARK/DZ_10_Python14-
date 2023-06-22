from collections import UserDict


class Field():
    pass


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
    

class Record:
    def __init__(self, name):
        self.name = name
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(phone)

    def remove_phone(self, phone):
        self.phones.remove(phone)

    def edit_phone(self, new_phone):
        index = self.phones.index(self)
        self.phones[index] = new_phone


class Name(Field):
    def __init__(self, value):
        self.value = value


class Phone(Field):
    def __init__(self, value):
        self.value = value
