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
        pass

    def get_info(self, species):
        pass


zoo_name = input()
zoo_object = Zoo(zoo_name)
count_of_animals = int(input())
