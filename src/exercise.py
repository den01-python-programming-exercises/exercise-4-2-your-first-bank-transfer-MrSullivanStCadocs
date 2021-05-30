def main():
    #write your code below this line
    Matthews_account = Account("Matthew's account", 1000)
    my_account = Account("My account", 0)

    Matthews_account.withdraw(100)
    my_account.deposit(100)
    print(Matthews_account)
    print(my_account)

if __name__ == '__main__':
   from account import Account
   main()
else:
   from src.account import Account


