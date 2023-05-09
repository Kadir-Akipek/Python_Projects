import random
import string

def generate_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    domain = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
    extension = random.choice(['com', 'org', 'net'])
    return f"{username}@{domain}.{extension}"

with open('data.txt', 'w') as file:
    for i in range(50):
        text = ''.join(random.choices(string.ascii_lowercase + ' ', k=random.randint(50, 200)))
        email = generate_email()
        file.write(text + email + text + '\n')