import string, random



phrase = string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation
while True:
    try:
        no_of_passwords = int(input("Please key in the number of passwords you need : " ))
        
    except ValueError:
        print("You did not key in a number")
        continue
    else:
        break
while True:
    try:
        length = int(input("please Key in the lenght of the password you need: "))
    except ValueError:
        print("You did not key in a valid number")
        continue
    else:
        break


passwords = []
for i in range(no_of_passwords):
    ps=random.sample(phrase,length)
    password=("".join(ps))
    passwords.append(password)
print(passwords)
f = open("passwords.txt", "w")
for p in passwords:
    f.write(p+"\n")
f.close()
    