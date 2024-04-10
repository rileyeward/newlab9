def encoder(number): #Riley Ward
    encoded = ''
    for char in number:
        x = int(char) + 3
        x = str(x)
        encoded += x
    return encoded
def decoder(new_password):
    decoded_password = ""
    for char in new_password:
        x = int(char)-3
        decoded_password +=str(x)
    return decoded_password





while True:
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit\n")

    option = int(input("Please enter an option: "))

    if option == 1:
        password = input("Please enter password to encode: ")
        new_password = encoder(password)
        print("Password has been encoded and stored!\n")

    elif option == 2:
        decoded_password=decoder(new_password)
        print("The encoded password is " + str(new_password) + ", and the original password is " + decoded_password + ".\n")

    elif option == 3:
        break