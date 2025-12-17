from abc import abstractmethod


class Book:
    page_material = 'бумага'
    have_text = True

    def __init__(self, name, author, page_count, isbn, reserved):
        self.name = name
        self.author = author
        self.page_count = page_count
        self.isbn = isbn
        self.reserved = reserved

    @abstractmethod
    def print_book_info(self):
        if self.reserved is True:
            print(f'Название: {self.name}, Автор: {self.author}, страниц: {self.page_count}, \
материал: {self.page_material}, зарезервирована')
        else:
            print(f'Название: {self.name}, Автор: {self.author}, страниц: {self.page_count}, \
материал: {self.page_material}')


first_book = Book('Идиот', 'Достоевский', 500, 1, True)
second_book = Book('Братья Карамазовы', 'Достоевский', 890, 2, False)
third_book = Book('Игрок', 'Достоевский', 321, 3, False)
fourth_book = Book('Преступление и наказание', 'Достоевский', 700, 4, False)
fifth_book = Book('Бесы', 'Достоевский', 650, 5, False)

first_book.print_book_info()
second_book.print_book_info()
third_book.print_book_info()
fourth_book.print_book_info()
fifth_book.print_book_info()


class SchoolBook(Book):
    def __init__(self, name, author, page_count, isbn, reserved, subject, grade_level, have_tasks):
        super().__init__(name, author, page_count, isbn, reserved)
        self.subject = subject
        self.grade_level = grade_level
        self.have_tasks = have_tasks

    def print_book_info(self):
        if self.reserved is True:
            print(f'Название: {self.name}, Автор: {self.author}, страниц: {self.page_count}, \
предмет: {self.subject}, класс: {self.grade_level}, зарезервирована')
        else:
            print(f'Название: {self.name}, Автор: {self.author}, страниц: {self.page_count}, \
предмет: {self.subject}, класс: {self.grade_level}')


first_school_book = SchoolBook('Алгебра', 'Иванов', 200, 6, True, 'Математика', '9', True)
second_school_book = SchoolBook('История российского государства', 'Акунин', 545, 7, False, 'История', '6', False)
third_school_book = SchoolBook('Внеклассное чтение', 'Паустовский', 189, 8, False, 'Литература', '2', False)
fourth_school_book = SchoolBook('Экономика. Базовый курс', 'Липсиц', 306, 9, False, 'Экономика', '11', True)
fifth_school_book = SchoolBook('English 3', 'Верещагина', 265, 10, False, 'Английский', '3', True)

first_school_book.print_book_info()
second_school_book.print_book_info()
third_school_book.print_book_info()
fourth_school_book.print_book_info()
fifth_school_book.print_book_info()
