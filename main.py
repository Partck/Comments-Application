import time

options = ["create new comment", "edit comment", "delete comment", "reply comment"]

   
def main():
    while True:
        user = input('Please enter your name:')
        if not user:
            print("User must have a name")
            break
        password = input('Please enter a password:')
        if not password:
            print("User must have a password")
            break
        
        time.sleep(0.8)
        greeting = 'Hello, {}! Welcome to Comments-Agile. please login to begin creating posts'.format(user)
    
        print(greeting)

        log_user = input('Please enter your account name:')
        log_pass = input('Enter your account password:')

        time.sleep(0.8)
        print("\n")
        print("1. Create a new comment")
        print("2. Edit comment")
        print("3. Delete comment")
        print("4. Reply to a new comment")
        print("\n")
        
        choice = input("Enter choice of action:")
        if choice != int:
            print("Choice must be numeral")
            break

        comment = input('enter new comment:')

    
if __name__ == '__main__':
    main()
