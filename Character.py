class Character():
    def __init__(self, name, secret_identity, city):
        self.name = name
        self.secret_identity = secret_identity
        self.city = city

        self.password = None

    def say_name(self):
        return "I am {}!".format(self.name)

    def set_password(self, password):
        self.password = password


batman = Character("Batman", "Bruce Wayne", "Gotham")
batman.set_password("Martha")

print(batman.say_name())
print(batman.password)
