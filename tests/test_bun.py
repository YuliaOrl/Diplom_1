import pytest
from data import BUN_NAME

class TestBun:

    def test_get_name_rights(self, bun):
        assert bun.get_name() == BUN_NAME

    def test_get_price_rights(self, bun):
        assert bun.get_price() == 100
