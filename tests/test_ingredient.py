import pytest
from data import *


class TestIngredient:

    def test_get_price_rights(self, ingredient_filling):
        assert ingredient_filling.get_price() == 100

    def test_get_name_rights(self, ingredient_filling):
        assert ingredient_filling.get_name() == FILLING_NAME

    def test_get_type_rights(self, ingredient_filling):
        assert ingredient_filling.get_type() == INGREDIENT_TYPE_FILLING
