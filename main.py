#Zachary Reynold
#password strength checker
#8/11/2024


import string
import getpass

def check_pass():

    # getpass.getpass would not work with powershell, command prompt, or vs terminal switched getpass.getpass() to input()
    # Replace this: password = getpass.getpass("Enter Password: ") With this: password = input()

    #initial terminal prompt

    password = input("Enter Password: ")
    strength = 0
    remarks = ' '
    lower_count = upper_count = num_count = wspace_count = special_count = 0

    

    for char in password:
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        elif char == ' ':
            wspace_count += 1
        else:
            special_count += 1



    if lower_count >= 1:
        strength += 1
    if upper_count >= 1:
        strength += 1
    if num_count >= 1:
        strength += 1
    if wspace_count >= 1:
        strength += 1
    if special_count >= 1:
        strength += 1


    #password remarks

    if strength == 1:
        remarks = "Password is extremely weak"
    elif strength == 2:
        remarks = "Password is very weak"
    elif strength == 3:
        remarks = "Password is weak, consider changing"
    elif strength == 4:
        remarks = "Password is adequate"
    elif strength == 5:
        remarks = "Password is strong"

#displaying password chemistry

    print("\nYour Password Has:")
    print(f"{lower_count} lowercase characters")
    print(f"{upper_count} uppercase characters")
    print(f"{num_count} numeric characters")
    print(f"{wspace_count} whitespace characters")
    print(f"{special_count} special characters")
    print(f"\nPassword Strength: {strength}")
    print(f"Remarks: {remarks}\n")

#option to improve upon password and more insight

def ask_password(another_password=False):
    if another_password:
        choice = input("Do you want to try a new password? (y/n): ")
    else:
        choice = input("Do you want to change password strength? (y/n): ")

    while True:
        if choice.lower() == "y":
            return True
        elif choice.lower() == "n":
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
            choice = input("Do you want to try a new password? (y/n): ")

    #checks to see if script is ran directly. if it is an imported module, codeblock will be skipped

if __name__ == "__main__":
    print('+++ Welcome to Password Checker +++')
    while True:
        check_pass()
        if not ask_password(True):
            print("Exiting Password Checker. Goodbye!")
            break
