from datetime import datetime

import pytest

from owner import Owner
from pet_type import PetType
from pet import Pet


def test_pet_type_toTuple():
    obj = PetType(2,"cat")
    assert tuple(obj) == (2,"cat")

def test_pet_type_from_Tuple():
    tupl = (3,"dog")
    obj = PetType(*tupl)
    assert obj.id == 3 and obj.typeName== "dog"


def test_pet_to_Tuple():
    obj = Pet(3,"sony",5,7)
    assert tuple(obj) == (3,"sony",5,7)


def test_pet_from_Tuple():
    tupl = (3, "sony", 5, 7)
    obj = Pet(*tupl)
    assert Pet(3, "sony", 5, 7)== obj


def test_owner_toTuple():
    obj = Owner(1,"Andrey","Hludeev",datetime(1980,3,3),"Harkiv","0668896561")
    assert tuple(obj) == (1,"Andrey","Hludeev",datetime(1980,3,3),"Harkiv","0668896561")


def test_owner_from_tuple():
    tupl = (1, "Andrey", "Hludeev", datetime(1980, 3, 3), "Harkiv", "0668896561")
    obj = Owner(*tupl)
    assert obj == Owner(1,"Andrey","Hludeev",datetime(1980,3,3),"Harkiv","0668896561")



