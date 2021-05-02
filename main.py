import random
print("You past passwords may have been compromised.  Generate something stronger below.")
password_characters = '!@#$%^&*()-=_+`~[]{]\|;:,<.>/?ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
lengthofpassword = input('Requested length: ')
lengthofpassword = int(lengthofpassword)
print('See below: ')
passwordtextdocument = open('supersecurepassworddocument.txt', 'w')
for a in range(lengthofpassword):
    password = ''
    for b in range(lengthofpassword):
        password = ""
        password = random.choice(password_characters)
    print (password)
    passwordtextdocument.write(password)
passwordtextdocument.close()
print('There you go!')
