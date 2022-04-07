import pytest
from functions import displayItem

def test_display_item_success(capsys):
    displayItem(["apple", "banana", "coconut"], 1)

    stdout, stderr = capsys.readouterr()

    assert "banana" in stdout.strip()

def test_display_item_out_of_bounds():
    with pytest.raises(IndexError):
        displayItem(["apple"], 1)

@pytest.mark.parametrize("index", ["index", [], {}])
def test_display_item_nonnumerical_index(index):
    with pytest.raises((TypeError)):
        displayItem(["apple", "banana", "coconut"], index)

@pytest.mark.parametrize("numbers", ["String", 123])
def test_display_item_noniterable_numbers(numbers):
    with pytest.raises(TypeError):
        displayItem(numbers, 0)