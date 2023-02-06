import pytest

from utils.utils import load_operations, ex_operations, last_values, edited_data

def test_load_operations():
    assert len(load_operations()) > 0


def test_ex_operations(list_1):
    assert ex_operations([]) == []
    assert len(ex_operations(list_1)) == 4


def test_last_values(list_1, list_2):
    assert len(last_values(list_1, 2)) == 2
    assert len(last_values(list_2)) == 4


def test_edited_data(list_3):
    assert len(edited_data(list_3)) == 5
    assert len(edited_data(list_3)) == 5
