def new_password(oldpassword, newpassword):
    if oldpassword != newpassword and len(newpassword) >= 6:
        for c in newpassword:
            if c in '0123456789':
                return True
            else:
                return False
    else:
        return False

res = new_password('vakProg17' , 'python')
print(res)

print(new_password('huprog17' , 'huprog17'))
print(new_password('vakProg17' , 'pro'))

