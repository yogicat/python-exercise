def house_password(password):
    if len(password) >= 10:
        if password.upper() == password or password.lower() == password:
            return False
        else:
            return any(char.isdigit() for char in password)
    else:
        return False

    # solution 2.
    # if data.isdigit() or data.islower() or data.isupper() or data.isalpha() or len(data) < 10:
    #   return False
    # return True


print(house_password('A1213pokl'))
print(house_password('bAse730onE'))
