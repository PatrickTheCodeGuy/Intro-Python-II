# Implement a class to hold room information. This should have name and
# description attributes.


class Room():
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items

    def __repr__(self):
        return f'This is the {self.name}. {self.description}'
