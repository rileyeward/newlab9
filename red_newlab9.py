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
        print("The encoded pass word is " + str(new_password) + ", and the original password is " + str() + ".\n")

    elif option == 3:
        break