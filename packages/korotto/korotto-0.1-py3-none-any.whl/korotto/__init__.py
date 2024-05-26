# korotto/__init__.py

import random
import string

def korotto(length=12, use_uppercase=True, use_numbers=True, use_special_chars=True):
    char_set = string.ascii_lowercase
    if use_uppercase:
        char_set += string.ascii_uppercase
    if use_numbers:
        char_set += string.digits
    if use_special_chars:
        char_set += string.punctuation
    
    password = ''.join(random.choice(char_set) for _ in range(length))
    return password
