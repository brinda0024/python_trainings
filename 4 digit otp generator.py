#It is a simple code to generate a 4 digit long OTP using "random" library

import random

otp = random.randint(1000, 10000)
print(otp)
