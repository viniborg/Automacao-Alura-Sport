from faker import Faker


class FakeUser:

    def __init__(self):
        fake = Faker()
        self.name = fake.name()
        self.password = fake.password()
