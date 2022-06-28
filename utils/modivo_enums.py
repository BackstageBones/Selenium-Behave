from enum import Enum


class ClothingType(dict):
    Types = {'Clothes': 1,
             'Shoes': 2, 'Accessories': 3}


class UpperClothingTypeEnum(Enum):
    TSHIRST_AND_POLO = 1
    BLOUSES_AND_SHIRTS = 5
