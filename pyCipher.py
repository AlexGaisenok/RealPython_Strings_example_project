import random
def cipher_message(message):
    ciphered = ''
    shift = random.randint(0, 256)
    print('Random shift is:', shift)
    for s in message:
        ciphered = ciphered+chr(ord(s)+shift)
    return ciphered

def decipher_message(ciphered_message, shift):
    message = ''
    for s in ciphered_message:
        message = message+chr(ord(s)-int(shift))
    return message

menu_chosen = True
while menu_chosen:
    print("pyCipher/Decipher script version 1.0")
    print("-----------------")
    print("1. Encrypt message")
    print("2. Decrypt message")
    print("3. About")
    print("4. Exit")
    
    menu_chosen = int(input("Chose menu option: "))

    if menu_chosen == 1:
        print('Enter your message and hit Enter: ')
        message = input()
        print('encrypted text: ',cipher_message(message))
    elif menu_chosen == 2:
        print('Enter ciphered message and hit Enter: ')
        ciphered_message = input()
        print('Enter shift and hit Enter: ')
        shift = input()
        print('decrypted text: ',decipher_message(ciphered_message, shift))
    elif menu_chosen == 3:
        print('''
    This script was written after working through the course on https://realpython.com/courses/python-strings/
    Thank you very much Christopher Bailey and all the community of RealPython.com for really cool tutorials and courses!
    Future colleague and pythonista Alex Gaisenok. February 2022.
             ''')
    elif menu_chosen == 4:
        print("\n Goodbye")
        menu_chosen = False
    else:
        print("\n Not Valid Choice Try again \n")