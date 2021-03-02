from data import data

def auth_register(email, password, name_first, name_last):
    User.validate_email(email)
    
    new_user = User(
        email=email,
        password=password,
        name_first=name_first,
        name_last=name_last,
        username_str=User.generate_username(name_first, name_last),
        permission_id=User.generate_permission(u_id)
    )

    data['users'].append(new_user)
