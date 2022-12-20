# Base for email and password for account creation
import string

# Declaring checkers
sp = string.punctuation
email = ''
password = ''
letters = string.ascii_letters

# Checking the user's inputted email
while True:
    email = input('Enter your email \n')
    email = email.lower()
    if email[0] in letters:
        pass
    else:
        continue
    if "@" in email:
        pass
    else:
        print('Enter your email again')
        continue
    if email.endswith('.com'):
        break
    else:
        continue
# Checking the user's inputted password
while True:
    print('Enter your password')
    password = input()
    lcount = 0
    ucount = 0
    ncount = 0
    spcount = 0
    totalcount = 0
    for letter in password:

        if letter.islower():
            lcount = lcount + 1
            totalcount += 1
        if letter.isupper():
            ucount = ucount + 1
            totalcount += 1
        if letter.isnumeric():
            ncount = ncount + 1
            totalcount += 1
        if letter in sp:
            spcount = spcount + 1
            totalcount += 1

    if lcount < 1:
        print('password must contain 1 lowercase character')
        continue

    if ucount < 1:
        print('password must contain 1 uppercase character')
        continue

    if ncount < 1:
        print('password must contain at least 1 numerical character')
        continue

    if spcount < 1:
        print('password must contain at least 1 special character')
        continue

    if totalcount > 1:
        break

print("Email is:", email)
print("Password is:", password)
