from typing import Any


class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if self == contract.author]
    
    def books(self):
        return [contract.book for contract in Contract.all if self == contract.author]
    
    def sign_contract(self, book, date, royalties):
        new_contract = Contract(self, book, date, royalties)
        return new_contract
    
    def total_royalties(self):
        return sum([contract.royalties for contract in Contract.all if self == contract.author])


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if self == contract.book]
    
    def authors(self):
        return [contract.author for contract in Contract.all if self == contract.book]
    



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

    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of Author class.")
        else:
            self._author = author

    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, book):
        if isinstance(book, Book):
            self._book = book
        else:
            raise Exception("Book must be an instance of Book class.")
        
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        if isinstance(date, str):
            self._date = date
        else:
            raise Exception("Date must be a string.")
        
    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, royalties):
        if isinstance(royalties, int):
            self._royalties = royalties
        else:
            raise Exception("Royalties must be an integer.")
    
    def contracts_by_date(date):
        return [contract for contract in Contract.all if date == contract.date]