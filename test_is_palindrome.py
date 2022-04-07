import pytest
from functions import isPalindrome

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