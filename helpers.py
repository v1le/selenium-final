import faker
import random

CHARS_FOR_PASSWORD = 'almnoprstuvwxyzABCDEFGHVWXYZ!@#$%^&*()-=+_0123456789'


def generate_email_and_password():
    # create email using faker library
    fake = faker.Faker()
    email = fake.email()
    '''
        generate password for user wih length=10
        randomly choosing chars and adding to list ->
        join used to conver list with random chars to string
    '''
    password = ''.join([
        random.choice(CHARS_FOR_PASSWORD) for char in range(10)]
        )
    return email, password
