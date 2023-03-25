# Bu proje, bir şifrenin gücünü ve karmaşıklığını kontrol eden ve kullanıcıya geri bildirim sağlayan bir program oluşturmayı içerir.
# (This project involves creating a program that checks the strength and complexity of a password and provides feedback to the user.)

import string

def check_password_strength(password):
    if len(password) < 8:
        return 'Password must be at least 8 characters long.'
    elif not any(char.isdigit() for char in password):
        return 'Password must contain at least one digit character.'
    elif not any(char.isupper() for char in password):
        return 'Password must contain at least one uppercase character.'
    elif not any(char.islower() for char in password):
        return 'Password must contain at least one lowercase character.'
    elif not any(char in string.punctuation for char in password):
        return 'Password must contain at least one special character.'
    else:
        return 'Password is strong and complex!'

password = input('Enter a password: ')
strength = check_password_strength(password)
print(strength)