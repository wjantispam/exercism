import random
import string
from datetime import datetime

class Robot:
    def __init__(self):
        random.seed(datetime.now())
        self.name = random.choice(string.ascii_uppercase)   \
        + random.choice(string.ascii_uppercase) \
        + random.choice(string.digits) \
        + random.choice(string.digits) \
        + random.choice(string.digits)

    def reset(self):
        random.seed(datetime.now())
        aa = random.choice(string.ascii_uppercase)   \
        + random.choice(string.ascii_uppercase) \
        + random.choice(string.digits) \
        + random.choice(string.digits) \
        + random.choice(string.digits)

        return aa
