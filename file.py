import random

def generateOTP(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    n = len(characters)
    otp = "".join(random.choice(characters) for _ in range(length))
    return otp

if __name__ == '__main__':
    # Declare the length of OTP
    length = 6
    print("Your OTP is -", generateOTP(length))
