#PASSWORD GENERATOR
import random
import string 
def generate_password(length):
    lowercase_alphabets = string.ascii_lowercase
    uppercase_alphabets = string.ascii_uppercase
    numbers = string.digits
    special_characters = string.punctuation
    combine_characters = (lowercase_alphabets + uppercase_alphabets + numbers  + special_characters)
    password = ""
    for i in range(length):
        random_character = random.choice(combine_characters)
        password += random_character
    return password 
print("_____PASSWORD GENERATOR_____")
password_len = int(input("Enter password length:"))
if password_len < 4 :
    print("password length should be atleast 4...")
else:
    final_password = generate_password(password_len)
    print("Your Password is :",final_password)