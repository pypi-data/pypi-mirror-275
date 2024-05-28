from tmf.tuflow_model_files.dataclasses.types import is_a_number, is_a_number_or_var


def test_is_a_number():
    assert is_a_number('1.0') == True
    assert is_a_number('1') == True
    assert is_a_number('1.0.0') == False
    assert is_a_number('hello') == False


def test_is_a_number_or_var():
    assert is_a_number_or_var('1.0') == True
    assert is_a_number_or_var('1') == True
    assert is_a_number_or_var('1.0.0') == False
    assert is_a_number_or_var('hello') == False
    assert is_a_number_or_var('<<CELL_SIZE>>') == True
