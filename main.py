import time
from register import Register
from login import Login
from comments import Comments

regis = Register()
log_in = Login()
comment = Comments()

def main():
    while True:
        print("\n")
        user = input('Please enter your name:')
        if not user:
            print("User must have a name")
            break
        password = input('Please enter a password:')
        if not password:
            print("User must have a password")
            break
        regis.add(user, password)
        varin = regis.get_user(1)
        
        print("\n")
        print("\n")
        time.sleep(0.8)
        greeting = 'Hello, {}! Welcome to Comments-Agile. please login to begin creating posts'.format(user)
    
        print(greeting)

        log_user = input('Please enter your account name:')
        log_pass = input('Enter your account password:')
        
        if not log_user:
            print("must have username to login")
            break
        if not log_pass:
            print("must have a password")
            break
        
        variba = log_in.login(log_user, log_pass)
        if not variba:
            print("User by those details doesn't exist")
            break
        
        time.sleep(0.8)
        print("\n")
        print("OPTIONS")
        print("1. Create a new comment")
        print("2. Edit comment")
        print("3. Delete comment")
        print("4. Reply to a new comment")
        print("\n")
    
        choice = input("Enter choice of action:")
        opts = ["1", "2", "3", "4"]
        if choice not in opts:
            print("Choice must be numeral")
            break
        
        if choice == opts[0]:
            print("\n")
            post = input("Enter your new comment:\n")

            if not post:
                print('Empty comment field')
                break
            post = comment.create_comments(post, log_user)
            time.sleep(0.8)
            print("comment created by {} ".format(log_user))
            print("comment id : #{}".format(post['id']))
        

        elif choice == opts[1]:
            print("\n")
            post = input("Enter your new comment:\n")
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        

    
if __name__ == '__main__':
    main()
