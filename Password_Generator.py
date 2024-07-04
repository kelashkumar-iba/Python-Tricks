import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits
    password = "".join(random.choice(characters) for _ in range(length))
    return password

print(f"Generated Password: {generate_password(16)}")