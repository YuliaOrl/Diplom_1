import pytest
from bun import Bun
from burger import Burger
from ingredient import Ingredient
from database import Database
from data import *
from unittest.mock import Mock


@pytest.fixture()
def bun():
    bun = Bun(BUN_NAME, 100)
    return bun


@pytest.fixture()
def ingredient_filling():
    ingredient = Ingredient(INGREDIENT_TYPE_FILLING, FILLING_NAME, 100)
    return ingredient


@pytest.fixture()
def ingredient_sauce():
    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, SAUCE_NAME, 200)
    return ingredient


@pytest.fixture()
def burger():
    burger = Burger()
    return burger


@pytest.fixture()
def burger_with_filling():
    burger = Burger()

    mock_bun = Mock()
    mock_bun.get_name.return_value = BUN_NAME
    mock_bun.get_price.return_value = 100

    mock_ingredient_filling = Mock()
    mock_ingredient_filling.get_type.return_value = INGREDIENT_TYPE_FILLING
    mock_ingredient_filling.get_name.return_value = FILLING_NAME
    mock_ingredient_filling.get_price.return_value = 100

    mock_ingredient_sauce = Mock()
    mock_ingredient_sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
    mock_ingredient_sauce.get_name.return_value = SAUCE_NAME
    mock_ingredient_sauce.get_price.return_value = 200

    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient_filling)
    burger.add_ingredient(mock_ingredient_sauce)
    return burger


@pytest.fixture()
def database():
    database = Database()
    return database
