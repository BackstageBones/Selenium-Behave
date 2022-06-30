import random
from enum import Enum


class ClothingType(dict):
    Types = {'Clothes': 1,
             'Shoes': 2, 'Accessories': 3}


class UpperClothingTypeEnum(Enum):
    TSHIRST_AND_POLO = 1
    BLOUSES_AND_SHIRTS = 5


class Cards(Enum):
    VISA_UNAUTHENTICATED = '4111111111111111'

    def expire_date_gen(self):
        return ''.join('0' + str(random.randint(1, 12)) + '/' + str(random.randint(23, 29)))

    def security_code_gen(self):
        return ''.join(random.sample(range(1, 9), 3))
