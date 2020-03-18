import faker
import random

CHARS_FOR_PASSWORD = 'abcdefghijklmnoprstuvwxyzABCDEFGHIJKLMNOPRSTUVWXYZ!@#$%^&*()-=+_0123456789'

def generate_email_and_password():
    fake = faker.Faker()
    email = fake.email()
    password = ''.join([random.choice(CHARS_FOR_PASSWORD) for char in range(10)])
    return email, password