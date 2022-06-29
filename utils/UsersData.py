from dataclasses import dataclass


@dataclass
class Users:
    Email: str
    Phone_number: str
    First_name: str
    Last_name: str
    Street_address: str
    House_number: int
    post_code: int
    city: str


JOHN_TEST = Users('john@test.com', '730543928', 'John', 'Test', 'Wlodkowica', 15, 53240, 'Wroclaw')
