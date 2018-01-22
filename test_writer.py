# test_capitalize.py

# test_capitalize.py

import pytest
def capital_case(x):
    if not isinstance(x, str):
        raise TypeError('Please provide a string argument')
    return x.capitalize()

def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'

def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        capital_case(9)


"""
def writer():
	variable = "Something"
	print variable

	return variable

def test_writer():
	assert writer() == "Something"


def adder(x):
	return x+1


def test_adder():
	assert adder(3) == 5
"""