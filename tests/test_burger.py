import pytest
from data import *


class TestBurger:

    def test_set_buns_rights(self, burger, bun):
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient_rights(self, burger, ingredient_filling):
        burger.add_ingredient(ingredient_filling)
        assert len(burger.ingredients) == 1 and burger.ingredients[0].type == INGREDIENT_TYPE_FILLING

    @pytest.mark.parametrize('index, type', [[0, INGREDIENT_TYPE_SAUCE], [1, INGREDIENT_TYPE_FILLING]])
    def test_remove_ingredient_rights(self, burger, ingredient_filling, ingredient_sauce, index, type):
        burger.ingredients = [ingredient_filling, ingredient_sauce]
        burger.remove_ingredient(index)
        assert len(burger.ingredients) == 1 and burger.ingredients[0].type == type

    @pytest.mark.parametrize('index, new_index', [[1, 0], [0, 1]])
    def test_move_ingredient_rights(self, burger, ingredient_filling, ingredient_sauce, index, new_index):
        burger.ingredients = [ingredient_filling, ingredient_sauce]
        burger.move_ingredient(index, new_index)
        assert len(burger.ingredients) == 2 and burger.ingredients[0].type == INGREDIENT_TYPE_SAUCE

    def test_get_price_rights(self, burger_with_filling):
        assert burger_with_filling.get_price() == 500

    def test_get_receipt_rights(self, burger_with_filling):
        receipt = burger_with_filling.get_receipt()
        assert f'(==== {BUN_NAME} ====)' and f'(= filling {FILLING_NAME} =)' and f'(= sauce {SAUCE_NAME} =)' \
               and 'Price: 500' in receipt
