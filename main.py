import random

chars = '!@#$%^&*()-=_+`~[]{]\|;:,<.>/?ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'

print("You past passwords may have been compromised.  Generate something stronger below.")

passwordLength = input('Requested length: ')
passwordLength = int(passwordLength)

print('See below: ')

passwordtextdocument = open('supersecurepassworddocument.txt', 'w')
for p in range(passwordLength):
    password = ''
    for c in range(passwordLength):
        password = ""
        password += random.choice(chars)
    print (password)
    passwordtextdocument.write(password)
passwordtextdocument.close()

print('There you go!')
