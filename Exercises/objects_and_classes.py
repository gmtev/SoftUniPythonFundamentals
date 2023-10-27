# Comment
class Comment:
    def __init__(self, username, content, likes=0):
        self.username = username
        self.content = content
        self.likes = likes


comment = Comment("user1", "I like this book")
print(comment.username)
print(comment.content)
print(comment.likes)


# Party
class Party:
    def __init__(self):
        self.people = []


party = Party()
line = input()
while line != "End":
    party.people.append(line)
    line = input()
print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")


# Email
class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
info = input()
while info != "Stop":
    sender, receiver, content = info.split()
    email_info = Email(sender, receiver, content)
    emails.append(email_info)
    info = input()
indexes = [int(i) for i in input().split(", ")]
for index in indexes:
    emails[index].send()
for current_email in emails:
    print(current_email.get_info())


# Zoo
class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        message = ""
        if species == "mammal":
            message += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
        elif species == "fish":
            message += f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
        elif species == "bird":
            message += f"Birds in {self.name}: {', '.join(self.birds)}\n"
        message += f"Total animals: {Zoo.__animals}"
        return message


zoo_name = input()
zoo_object = Zoo(zoo_name)
count_of_animals = int(input())
for i in range(count_of_animals):
    species, name = input().split()
    zoo_object.add_animal(species, name)
searched = input()
print(zoo_object.get_info(searched))


# Circle
class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = diameter / 2

    def calculate_circumference(self):
        return Circle.__pi * self.diameter

    def calculate_area(self):
        return Circle.__pi * self.radius * self.radius

    def calculate_area_of_sector(self, angle):
        return (angle/360) * Circle.__pi * self.radius * self.radius


circle = Circle(10)
angle = 5
print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")
