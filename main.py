import account
import expense

account.create_table()
expense.create_table()
delAcc = account.DeleteAcc()
while True:
    print("===Expense Tracker===")
    print("\n1. Sign up")
    print("2. Sign in")
    print("3. Quit")

    choice = int(input("Choose option: "))

    createAccount = account.CreateAcc()
    login = account.Login()
    if choice == 1:
        createAccount.signup()

    elif choice == 2:
        userID = login.signin()
        if userID:
            print("\nWELCOME TO EXPENSE TRACKER")
            while True:
                print("\n1. Add expense")
                print("2. View expense")
                print("3. Delete expense")
                print("4. Logout")
                print("5. DELETE MY ACCOUNT")
                exp_choice = int(input("Enter: "))
                if exp_choice == 1:
                    expense.add_expense(userID)

                elif exp_choice == 2:
                    expense.view_expense(userID)

                elif exp_choice == 3:
                    expense.delete_expense(userID)

                elif exp_choice == 4:
                    break

                elif exp_choice == 5:
                    dele = account.DeleteAcc().deleteacc(userID)
                    if dele:
                        break

                else:
                    print("Invalid choice!")

    elif choice == 3:
        print("Quiting...")
        break

    else:
        print("Invalid choice!")