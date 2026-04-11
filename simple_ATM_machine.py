# Promgram to check balance, deposit and withdrawals.

balance = 2000

while True:
    print('\nPress 1 for Check Balance')
    print('Press 2 for Withdraw')
    print('Press 3 for Deposit')
    print('Press 4 for Exit')

    choice = int(input('Enter Choice: '))

    if choice == 1:
        print('Balance =', balance)

    elif choice == 2:
        withdraw = int(input('Enter amount: '))
        if withdraw <= balance:
            balance = balance - withdraw
            print(withdraw, 'Withdraw Successful')
        else:
            print('Insufficient Balance')

    elif choice == 3:
        deposit = int(input('Enter deposit amount: '))
        balance = balance + deposit
        print(deposit, 'Deposit Successful')

    elif choice == 4:
        print('Thank you for using ATM')
        break

    else:
        print('Invalid Choice')