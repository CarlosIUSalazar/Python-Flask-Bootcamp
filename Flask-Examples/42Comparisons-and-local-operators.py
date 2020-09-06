print(1>2)
print (3 == 3)
print (3 <= 2)
print (3 != 1)

username = "admin"
check = "admin"
logged_in = True
has_permission = True

print(username == check)

#AND
print(1==2 and 2<3)


#OR
print(1==2 or 2<3)

print ( (1==2) or (2<3) or (4==4))


permission = False
print(username == check and permission) #currently permission is False

print(logged_in and has_permission)
