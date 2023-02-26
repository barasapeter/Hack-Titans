import string
import random

def generate_password(length=8):

    #define character sets 
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    
    #  combining the character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    #generate the password
    password = ''.join(random.choice(all_characters) for i in range(length))

    return password

# sample usage
if __name__ == "__main__":
    password = generate_password(10)
    print(password)
