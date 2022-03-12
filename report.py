# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 2022

@author: migram
"""

import json

class Person():

    def __init__(self, entity) -> None:
        self.firstname = entity['firstname']
        self.lastname  = entity['lastname']
        self.address   = entity['address']
        self.friend    = entity['friend']

    def list_friends(self):
        for friend in self.friend:
            Friend(friend)

    def set_address(self):
        for address in self.address:
            Address(address)

    def list_adress(self):
        return self.set_address().__str__()
  
    def get_fullname(self):
        return f"{self.firstname} {self.lastname}"

    def list_all_json(self):
        return json.dumps(self.__dict__)

    def list_all(self):
        self.get_fullname()
        self.list_friends()
        self.list_adress() 

    def __str__(self) -> str:
        return f"{self.firstname}, {self.lastname}, {self.address}, {self.friend}"  


class Friend():
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname  = lastname

    def get_fullname(self):
        return f"{self.firstname} {self.lastname}"

    def __str__(self) -> str:
        return f"{self.firstname}, {self.lastname}"


class Address():
    def __init__(self, street, zip, city):
        self.street = street
        self.zip   = zip
        self.city  = city

    def __str__(self) -> str:
        return f"{self.street}, {self.zip}, {self.city}"


def readReport():
    with open('./persons.json', 'r') as f:
        data = json.load(f)
        for entry in data:
            person = Person(entry)
            print(person)


def writeReport():
    input_firstname = input("Please Enter the firstname ")
    input_lastname  = input("Please Enter the lastname ")
    input_address   = input("Please Enter the address ")
    input_friends   = input("Please Enter a friend or list of friends ")
    
    new_entry = {'firstname': input_firstname, 'lastname': input_lastname, 'address': [ input_address ], 'friend': [input_friends]}

    with open("./persons.json", "r+") as file:
        data = json.load(file)
        data.append(new_entry)
    
    with open("./persons.json", "w") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    

def main():
    user_select = input("Please select an option: \n 1. Read Report \n 2. Write Report \n 3. Exit \n")
    if user_select == "1":
        readReport()
    if user_select == "2":
        writeReport()
    else:
        print("Goodbye")


if __name__ == '__main__':
    main()