from dataclasses import dataclass


@dataclass
class UserData:
    Email: str
    Phone_number: str
    First_name: str
    Last_name: str
    Street_address: str
    House_number: int
    post_code: int
    city: str


JOHN_TEST = UserData('john@test.com', '730543928', 'John', 'Test', 'Wlodkowica', 15, 53240, 'Wroclaw')
CHARLES_XAVIER = UserData('charles@xmen.com', '999999999', 'Charles', 'Xavier', 'Boston', 4544, 4509, 'USA')

USERS = [JOHN_TEST, CHARLES_XAVIER]
