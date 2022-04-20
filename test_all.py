import pytest
from functions import *

class FakeInput:
    def __init__(self, dividend, divisor):
        self.prompt_to_value = {
            "Enter a number: ": str(dividend),
            "Enter another number: ": str(divisor),
        }

    def input(self, prompt):
        return self.prompt_to_value[prompt]

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

@pytest.mark.parametrize("second,expected", [((10, 10), 5), ((5, 17), 7), ((17, 6.5), 12.5), ((-2, -5), 16.55294535724685)])
def test_dist_success(second, expected):
    x1, y1 = (5, 10)
    x2, y2 = second

    assert dist(x1, y1, x2, y2) == expected

def test_dist_bad_points():
    x1, y1 = ("hello", "world")
    x2, y2 = ("world", "hello")

    with pytest.raises(TypeError):
        dist(x1, y1, x2, y2)

@pytest.mark.parametrize("dividend,divisor,quotient", [(30, 5, 6.0), (2, -1, -2.0), (-20, -5, 4.0), (1, 4, 0.25)])
def test_divide_success(capsys, monkeypatch, dividend, divisor, quotient):
    fake_input = FakeInput(dividend, divisor)
    monkeypatch.setattr("builtins.input", fake_input.input)
    divide()

    stdout, stderr = capsys.readouterr()
    assert stdout.strip() == f'Your numbers divided is: {quotient}'

def test_divide_by_zero(monkeypatch):
    fake_input = FakeInput(1, 0)
    monkeypatch.setattr("builtins.input", fake_input.input)
    with pytest.raises(ZeroDivisionError):
        divide()

def test_divide_with_floats(capsys, monkeypatch):
    fake_input = FakeInput(0.25, 0.25)
    monkeypatch.setattr("builtins.input", fake_input.input)
    divide()

    stdout, stderr = capsys.readouterr()
    assert stdout.strip() == "Your numbers divided is: 1.0"

def test_divide_with_bad_input(monkeypatch):
    fake_input = FakeInput("hello", 0.25)
    monkeypatch.setattr("builtins.input", fake_input.input)
    with pytest.raises(TypeError):
        divide()

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


@pytest.mark.parametrize("word", ["racecar", "tacocat",])
def test_is_palindrome_success(word):
    assert isPalindrome(word)

@pytest.mark.parametrize("word", ["word", "thisisnotapalindrome",])
def test_is_palindrome_failure(word):
    assert not isPalindrome(word)

@pytest.mark.parametrize("word", ["RaCEcAr", "TaCOcAt",])
def test_is_palindrome_capitalized(word):
    assert isPalindrome(word)

def test_is_palindrome_bad_type():
    with pytest.raises(TypeError):
        isPalindrome(121)

@pytest.mark.parametrize("dividend,divisor,quotient", [(30, 5, 6.0), (2, -1, -2.0), (-20, -5, 4.0), (1, 4, 0.25)])
def test_number_success(dividend, divisor, quotient):
    assert numbers(dividend, divisor) == quotient

def test_number_by_zero():
    with pytest.raises(ZeroDivisionError):
        numbers(1, 0)

def test_number_with_floats():
    assert numbers(0.25, 0.25) == 1

def test_numbers_with_bad_input():
    with pytest.raises(TypeError):
        numbers("hello", 0.25)
    
def test_open_file_success(capsys):
    openFile("testing.txt")

    stdout, stderr = capsys.readouterr()

    assert stdout.strip() == "File opened."

def test_open_file_nonexistent():
    with pytest.raises(FileNotFoundError):
        openFile("nonexistant.txt")

@pytest.mark.parametrize("filename", [123, [], {}])
def test_open_file_bad_input(filename):
    with pytest.raises((TypeError)):
        openFile(filename)

@pytest.mark.parametrize("num,result", [(4, 2), (9, 3), (20, 4.47213595499958)])
def test_sq_success(num, result):
    assert sq(num) == result

@pytest.mark.parametrize("num,result", [(4.8, 2.1908902300206643), (9.0, 3), (15.75, 3.968626966596886)])
def test_sq_with_floats(num, result):
    assert sq(num) == result

def test_sq_with_negative():
    with pytest.raises(ValueError):
        sq(-1)
    
