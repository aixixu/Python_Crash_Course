users = ['cohen', 'ethan', 'aixi', 'admin', 'anna']
if len(users) == 0:
    print('We need to find some users!')
else:
    for user in users:
        if user == 'admin':
            print(f'Hello {user}, would you like to see a status report.')
        else:
            print(f'Hello {user}, thank you for logging in again.')
    users.clear()
    users
    