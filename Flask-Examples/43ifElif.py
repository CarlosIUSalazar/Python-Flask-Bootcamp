username = 'admin'
check = 'admin'
permission = True

if 1==2:
    print('Access Granted')
elif 1==3:
    print('Middle condition true!')
else:
    print('All not true!')


if username == 'admin' and permission:
    print("full access")
elif username == 'admin' and permission==False:
    print("Admin access only, no full permission")
else:
    print("NO access")
