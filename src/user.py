from data import data, User

def user_profile(u_id, permission_id):
    '''
    input format: (
        'u_id': integer
        'permission_id': string
    )

    For a valid user, returns information about their u_id, email, password, first name, last name, username_str 
    and permission_id

    output format: {
        user: {
            'u_id' : string,
            'email': string,
            'name_first': string,
            'name_last': string,
            'password': string,

        }
    }
    '''

