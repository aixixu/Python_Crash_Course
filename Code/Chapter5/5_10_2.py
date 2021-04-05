current_users = ['cohen', 'ethan', 'aixi', 'admin', 'anna']
new_users = ['cohen', 'alex', 'aixi', 'bob', 'tim']

for new_user in new_users:
    if new_user.lower() in [current_user.lower() for current_user in current_users]:
        print(f'This username({new_user}) has been used, please change it.')
    else:
        print(f'This username({new_user}) can be used.')