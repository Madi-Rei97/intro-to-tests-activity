from main import count_a_letter
import pytest

def test_non_alpha_letter_returns_none():
    test_sentence = "I am testing a function."
    test_letter = "4"

    result = count_a_letter(test_sentence, test_letter)

    assert result is None

def test_string_with_no_matches_returns_0():
    test_sentence = "I am testing a function."
    test_letter = "z"

    result = count_a_letter(test_sentence, test_letter)

    assert result is 0
