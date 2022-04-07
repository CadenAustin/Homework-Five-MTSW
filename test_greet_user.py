import pytest
from functions import greetUser

@pytest.mark.parametrize("name", [("Joe", "Bob", "Dylan"), ("France", "Pierre", "Wright")])
def test_greet_user_success(capsys, name):
    first, middle, last = name
    greetUser(first, middle, last)

    stdout, stderr = capsys.readouterr()
    assert stdout.strip() == f"Hello!\nWelcome to the program {first} {middle} {last}\nGlad to have you!"

def test_greet_user_string_but_nummeric():
    first, middle, last = ("Leo", "5423", "Scaper")
    with pytest.raises(ValueError):
        greetUser(first, middle, last)

def test_greet_user_non_string():
    first, middle, last = (123, 456, 7890)
    with pytest.raises(TypeError):
        greetUser(first, middle, last)