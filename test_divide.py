import pytest
from functions import divide

class FakeInput:
    def __init__(self, dividend, divisor):
        self.prompt_to_value = {
            "Enter a number: ": str(dividend),
            "Enter another number: ": str(divisor),
        }

    def input(self, prompt):
        return self.prompt_to_value[prompt]

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