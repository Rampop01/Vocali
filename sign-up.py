# Step 1: Take user inputs
name = input("Enter your name: ")
email = input("Enter your email: ")
password = input("Enter your password: ")

# Read the accounts file
with open("accounts.txt", 'r') as file:
    # Read the accounts line by line, and store them as strings
    accounts = [line.strip() for line in file.readlines()]

    # Skip the first line, which is a header
    accounts = accounts[1:]

# Check if the username or email already exists
account_exist = False
for account in accounts:
    parts = account.strip().split(', ')

    # make sure the length of the split is 3, repesenting the [name, email and password]
    if len(parts) == 3:
        existing_username, existing_email, existing_password = parts
        if (existing_username == name):
            print(f"FAILED: Account with username '" + name + "' already exist.")
            account_exist = True
            break

        if (existing_email == email):
            print(f"FAILED: Account with email '" + email + "' already exist.")
            account_exist = True
            break

# If the username or email does already exists
if not account_exist:
    with open("accounts.txt", 'a') as file:
        new_account_details = name + ", " + email  + ", " + password + "\n"
        file.write(new_account_details)
        print("SUCCESS: Account created.")
