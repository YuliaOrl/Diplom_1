import pytest


class TestDatabase:

    buns_data = [[0, 'black bun'], [1, 'white bun'], [2, 'red bun']]

    @pytest.mark.parametrize('num, name', buns_data)
    def test_available_buns_rights(self, database, num, name):
        assert database.available_buns()[num].name == name

    ingredients_data = [[0, 'hot sauce'], [1, 'sour cream'], [2, 'chili sauce'], [3, 'cutlet'], [4, 'dinosaur'],
                        [5, 'sausage']]

    @pytest.mark.parametrize('num, name', ingredients_data)
    def test_available_ingredients_rights(self, database, num, name):
        assert database.available_ingredients()[num].name == name