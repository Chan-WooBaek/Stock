from auth import auth_register
from pytest import raises
from error import InputError, AccessError
from helper import clear

def test_case1():
    clear()
    result1 = auth_register('random@gmail.com', 'password', 'Ran', 'Dom')
    print(result1)