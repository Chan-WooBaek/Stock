"""
data = {
    'users': [
        {

        }
    ]
}
"""

import re

data = {
    'users': []
}

class User(object):
    def __init__(self, u_id=None, email=None, password=None, name_first=None, 
    name_last=None, username_str=None, permission_id=None):
        self.u_id = u_id
        self.email = email
        self.password = password
        self.name_first = name_first
        self.name_last = name_last
        self.username_str = username_str
        self.permission_id = permission_id

    def generate_username(name_first, name_last, u_id):
        username = name_first + name_last + u_id
        self.username_str = username
        return self.username_str

    def generate_uid(self)
        u_id = len(data['users'])
        self.u_id = u_id

    def get_uid(self):
        return self.u_id
    
    def validate_email(email):
        regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if re.search(regex, email) is None:
            raise InputError(description='Invalid Email Format')
