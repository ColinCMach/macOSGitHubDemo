
def encode(password):
    new_password = ""
    for i in password_input:
        new_password += str(int(i) + 3)

    return new_password


if __name__ == '__main__':
    password_input = input("Enter your password: ")

    new_password = encode(password_input)

    print("Encoded Password is ", new_password)



