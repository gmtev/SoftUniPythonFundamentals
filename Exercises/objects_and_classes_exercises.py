# Storage
class Storage:
    storage = []

    def __init__(self, capacity):
        self.capacity = capacity

    def add_product(self, product):
        if self.capacity > 0:
            self.capacity -= 1
            Storage.storage.append(product)

    def get_products(self):
        return Storage.storage


# Weapon
class Weapon:
    def __init__(self, bullets):
        self.bullets = int(bullets)

    def shoot(self):
        if self.bullets > 0:
            self.bullets -= 1
            return "shooting..."
        else:
            return "no bullets left"

    def __repr__(self):
        return f"Remaining bullets: {self.bullets}"


# Catalogue
class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name):
        self.products.append(product_name)

    def get_by_letter(self, first_letter):
        return [i for i in self.products if i.startswith(first_letter)]

    def __repr__(self):
        to_return = f"Items in the {self.name} catalogue:\n"
        to_return += '\n'.join(sorted(self.products))
        return to_return


# Town
class Town:
    def __init__(self, name):
        self.name = name
        self.latitude = "0°N"
        self.longitude = "0°E"

    def set_latitude(self, latitude):
        self.latitude = latitude

    def set_longitude(self, longitude):
        self.longitude = longitude

    def __repr__(self):
        return f"Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}"


# Class
class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name: str, grade: float):
        if Class.__students_count > len(self.students):
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        average_grade = (sum(self.grades)/len(self.grades))
        return float(f'{average_grade:.2f}')

    def __repr__(self):
        average_grade = self.get_average_grade()
        return f"The students in {self.name}: {', '.join(self.students)}. Average grade: {average_grade}"


# Inventory
class Inventory:
    def __init__(self, __capacity):
        self.__capacity = __capacity
        self.items = []

    def add_item(self, item: str):
        if self.__capacity > len(self.items):
            self.items.append(item)
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return int(self.__capacity)

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {int(self.__capacity)-int(len(self.items))}"


# Articles
class Article:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def edit(self, new_content: str):
        self.content = new_content

    def change_author(self, new_author: str):
        self.author = new_author

    def rename(self, new_title: str):
        self.title = new_title

    def __repr__(self):
        return f"{self.title} - {self.content}: {self.author}"


# Vehicle
class Vehicle:

    def __init__(self, type, model, price):
        self.type = type
        self.model = model
        self.price = price
        self.owner = None

    def buy(self, money, owner):
        if money >= self.price and self.owner is None:
            self.owner = owner
            change = money - self.price
            return f"Successfully bought a {self.type}. Change: {change:.2f}"
        elif money < self.price:
            return "Sorry, not enough money"
        else:
            return "Car already sold"

    def sell(self):
        if self.owner:
            self.owner = None
        else:
            return "Vehicle has no owner"

    def __repr__(self):
        if self.owner:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        else:
            return f"{self.model} {self.type} is on sale: {self.price}"


# Movie
class Movie:
    __watched_movies = 0

    def __init__(self, name, director):
        self.name = name
        self.director = director
        self.watched = False

    def change_name(self, new_name):
        self.name = new_name

    def change_director(self, new_director):
        self.director = new_director

    def watch(self):
        if not self.watched:
            self.watched = True
            Movie.__watched_movies += 1

    def __repr__(self):
        return f"Movie name: {self.name}; Movie director: {self.director}. Total watched movies: {Movie.__watched_movies}"