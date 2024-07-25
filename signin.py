username = input("Type your username: ")
password = input("Type your password: ")

with open('signin.txt', "a") as sigin_in_file:
    sigin_in_file.write(f"{username}, {password} \n")

# sigin_in_file = open("signin.txt", 'w+')

# sigin_in_file.write(f"{username}, {password}")
sigin_in_file.close()