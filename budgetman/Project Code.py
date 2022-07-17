import time  # the time module for functions such as timer, sleep and time display


def user_input():
    user_inp = str(input("""Which tool do you want to use:
    1) Budget Manager
    2) Expense Distributor
    """))

    if user_inp == '1' or user_inp == 'Budget Manager':
        budget_management()
    elif user_inp == '2' or user_inp == 'Expense Distributor':
        expense_distributor()


def user_input2():
    user_inp2 = str(input("\n\nDo you want to try again: "))
    if user_inp2 == 'yes':
        user_input()
    elif user_inp2 == 'no':
        print("Thank you for using our system")


def budget_management():  # creating a function to call for the budget management code
    budget = int(input("Enter your budget: Rs."))

    no_of_expense = int(input("Enter the number of expense made: "))

    dat = {k: [] for k in range(1, no_of_expense+1)}    # creating a dictionary for storage of user input as 'values'

    data = {}

    total = 0

    print("""Enter the Label and the Amount paid WHEN PROMPTED :""")

    for i, j in dat.items():               # items() is function used to return key:value pairs
        dat[i].append(str(input('Label: ')))
        dat[i].append(int(input('Amount: ')))

    print(' ')
    print("Processing data...")
    time.sleep(5)         # the sleep function of time module to stop all processes for a given amount of time

    print("*"*30)
    print("This is the data we have: ")
    print('_'*30)

    print("{:<7} {:<13} {:<10}".format('SNo.', 'Label', 'Amount'))
    # string formatting used for more easier to maintain code, and also to space out the data in the output

    for k, v in dat.items():
        Label, Amount = v     # assigning the two items inside each list as Label and Amount
        print("{:<7} {:<13} {:<10}".format(k, Label, Amount))
        data[Label] = Amount
    print("_"*30)
    print("*"*30)

    time.sleep(3.5)

    for key, value in data.items():
        total = total + value

    print(' ')
    print('Processing', end='')
    for f in range(18):
        print('.', end='')
        time.sleep(0.35)

    print('\n\nDone! :)')
    time.sleep(2)
    print(' ')

    print('Remarks: ')
    if total <= budget:
        print("You are good to go")
    else:
        print("Maybe you should cut costs for the {}".format(max(data, key=data.get)))

        # the function max() is returning the maximum value from the dictionary to be displayed
    user_input2()


def expense_distributor():
    num = int(input('Enter the No. of People: '))
    tab_dat = ['a', 0, 'c', 0, 'e', 0, 'g', 0, 'i', 0, 'k', 0, 'm', 0, 'o', 0, 'q', 0, 's', 0, 'u', 0, 'w', 0, 'y', 0]
    # a list of variables  ^

    for n in range(0, 2 * num, 2):
        tab_dat[n] = str(input('Enter their name: '))

    a = str(input('Did somebody pay: '))

    while a == 'yes':
        b = str(input('Who paid: '))
        c = int(input('How much he/she paid: '))
        tab_dat[tab_dat.index(b) + 1] += c
        a = str(input('Did somebody else pay: '))
        pass
    else:
        var1 = 0
        for g in range(1, 2 * num + 1, 2):
            var1 += tab_dat[g]
        var2 = var1 / num
        for j in range(1, 2 * num + 1, 2):
            tab_dat[j] = str(int(tab_dat[j] - var2))
    sp = '+' + len('NAME') * '-' + '+'
    for m in range(0, 2 * num, 2):
        if len(tab_dat[m]) > len(tab_dat[m + 1]):
            sp = sp + len(tab_dat[m]) * '-' + '+'
        else:
            sp = sp + len(tab_dat[m + 1]) * '-' + '+'
    col1 = '|' + 'NAME' + '|'
    col2 = '|' + 'RUPS' + '|'
    for o in range(0, 2 * num, 2):
        x = len(tab_dat[o])
        y = len(tab_dat[o + 1])
        diff = y - x
        if x > y:
            col1 = col1 + tab_dat[o] + '|'
        else:
            col1 = col1 + tab_dat[o] + (diff * ' ') + '|'
    for p in range(1, 2 * num + 1, 2):
        x = len(tab_dat[p - 1])
        y = len(tab_dat[p])
        diff = x - y
        if x > y:
            col2 = col2 + tab_dat[p] + diff * ' ' + '|'
        else:
            col2 = col2 + tab_dat[p] + '|'

    print("\n\nProcessing", end='')
    for i in range(18):
        print(".", end='')
        time.sleep(0.35)

    print("\n\nThis is the data we have: ")

    print(sp)
    print(col1)
    print(sp)
    print(col2)
    print(sp)
    user_input2()


user_input()

