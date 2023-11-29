import string
import random

def kagi(panjang):
    return "".join(random.choice(string.ascii_letters) for i in range(panjang))
