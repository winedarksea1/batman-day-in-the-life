class Character():
    def __init__(self, name, secret_identity, city):
        self.name = name
        self.secret_identity = secret_identity
        self.city = city

    def say_name(self):
        return "I am {}!".format(self.name)


batman = Character("Batman", "Bruce Wayne", "Gotham")

print(batman.say_name())
