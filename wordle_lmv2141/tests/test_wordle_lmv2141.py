import pytest

from wordle_lmv2141 import validate_guess, check_guess



@pytest.fixture
def common_word_list():
    return [
        "crane", "apple", "hello", "world", "python", 
        "house", "water", "light", "music", "dream",
        "happy", "smile", "peace", "heart", "brain",
        "table", "chair", "phone", "paper", "green"
    ]


# =============================================================================
# PART 1: BASIC TESTING (JUST PICKING 2 TESTS)
# =============================================================================

def test_validate_guess():
    """
    Test the validate_guess function with various inputs.
    """

    assert validate_guess("apple") == True      # Valid inputs (correct length, lowercase, alphabetic)

    assert validate_guess("cranes") == False    # Invalid inputs: wrong length
    assert validate_guess("AppLE") == False     # Invalid inputs: uppercase letters
    assert validate_guess('---..') == False     # Invalid inputs: non-alphabetic

    assert validate_guess("")   == False        # Edge cases: empty string
    assert validate_guess(None) == False        # Edge cases: None value
    assert validate_guess(12345) == False       # Edge cases: non-string input

def test_check_guess_basic():
    """
    Test basic check_guess functionality
    """
    all_match_result = [('c', 'green'), ('r', 'green'), ('a', 'green'), ('n', 'green'), ('e', 'green')]
    assert check_guess("crane", "crane") == all_match_result    # All letters match

    no_match_result = [('c', 'gray'), ('l', 'gray'), ('o', 'gray'), ('c', 'gray'), ('k', 'gray')]
    assert check_guess("brain", "clock") == no_match_result     # No letters match

    mix_result = [('c', 'green'), ('h', 'gray'), ('a', 'green'), ('i', 'gray'), ('r', 'yellow')]
    assert check_guess("crane", "chair") == mix_result          # Mixed matches
    

    assert check_guess("crane", "crrane") == []

