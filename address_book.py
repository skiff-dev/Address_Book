from collections import UserDict


class AddressBook(UserDict):
    """Class for creating user's addressbooks"""

    def add_record(self, record):
        self.data[record.name] = record.show_contact()

    def remove_record(self, record):
        self.data.pop(record.name, None)

    def show_records(self):
        return self.data


class Record:
    """Creating user's contacts"""

    def __init__(self, name, phone=None):
        self.name = name
        if phone is None:
            self.phone = []

    def add_phone(self, phone):
        self.phone.append(phone)

    def change_phone(self, phone):
        self.phones = phone

    def delete_phone(self):
        self.phones = []

    def show_contact(self):
        return {"name": self.name, "phone": self.phone}


class Field:
    pass


class Name(Field):
    pass


class Phone(Field):
    pass


if __name__ == "__main__":
    name = Name("Bill")
    phone = Phone("12345")
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)
    assert isinstance(ab["Bill"], Record)
