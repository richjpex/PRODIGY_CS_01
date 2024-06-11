import sys

def getText():
    text = input("Enter your message: ")
    return text

def getShift():
    shift = 0
    while True:
        print("Enter shift from 1-25:", end = " ")
        shift = int(input())
        if (shift >= 1 and shift <= 25):
            return shift
        else:
            print("Invalid shift.")

def getTranslatedText(mode, text, shift):
    if mode == 1:
        shift = -shift
    translated = ''

    for symbol in text:
        if symbol.isalpha():
            num = ord(symbol)
            num += shift

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            translated += chr(num)
        else:
            translated += symbol

    print(f"\n{translated}", end = " ")

char = 'y'
while (char == 'y' or char == 'Y'):
    print("""
Welcome to de_ciper!
Choose a deciphering option: 
1. Shift message to left
2. Shift message to right
3. Brute force message
0. Exit """)
    mode = int(input("Enter option: "))
    if (mode == 1 or mode == 2):
        text = getText()
        shift = getShift()
        print("This is the new message:", end = " ")
        getTranslatedText(mode, text, shift)
    elif (mode == 3):
        text = getText()
        print("Brute-forcing text . . .")
        for i in range (1, 26):
            getTranslatedText(mode, text, i)
            print(f"(Shift = {i}) ", end = "")
            #print()
    elif (mode == 0):
        sys.exit(0)
    else:
        "Invalid option"
    print()
    char = input("Repeat? (Y/N) ")