class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [contract.book for contract in self.contracts()]
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])




class Book:
    all = []
    
    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in self.contracts()]


class Contract:
    all = []
    
    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author
    # in all cases, i believe that value can be replaced with the setter method name.
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception
        self._author = value

    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception
        self._book = value

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        if not isinstance(date, str):
            raise Exception
        self._date = date

    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, royalties):
        if not isinstance(royalties, int):
            raise Exception
        self._royalties = royalties
    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date==date]

# SOMETHING ELSE FROM YOUTUBE... UNRELATED TO LAB

# class Employee:

#     raise_amt = 1.04

#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.email = first + '.' + last + '@email.com'
#         self.pay = pay

#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)

#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amt)


# class Developer(Employee):
#     raise_amt = 1.10

#     def __init__(self, first, last, pay, prog_lang):
#         super().__init__(first, last, pay)
#         self.prog_lang = prog_lang


# class Manager(Employee):

#     def __init__(self, first, last, pay, employees=None):
#         super().__init__(first, last, pay)
#         if employees is None:
#             self.employees = []
#         else:
#             self.employees = employees

#     def add_emp(self, emp):
#         if emp not in self.employees:
#             self.employees.append(emp)

#     def remove_emp(self, emp):
#         if emp in self.employees:
#             self.employees.remove(emp)

#     def print_emps(self):
#         for emp in self.employees:
#             print('-->', emp.fullname())


# dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
# dev_2 = Developer('Test', 'Employee', 60000, 'Java')

# mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1, dev_2])

# print(mgr_1.email)

# # mgr_1.add_emp(dev_2)
# # mgr_1.remove_emp(dev_2)

# mgr_1.print_emps()