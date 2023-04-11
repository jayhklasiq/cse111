from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name('Joshua', 'Olaoye') == 'Olaoye; Joshua'
    assert make_full_name('Edudzi', 'Agbeko') == 'Agbeko; Edudzi'
    assert make_full_name('James', 'Owolabi') == 'Owolabi; James'

    
def test_extract_family_name():
    assert extract_family_name('Elijah; Nyamkyere') == 'Elijah'
    assert extract_family_name('Joshua; Olaoye') == 'Joshua'
    assert extract_family_name('Edudzi; Agbeko') == 'Edudzi'
        
def test_extract_given_name():
    assert extract_given_name('Elijah/ Nyamkyere') == 'Nyamkyere'
    assert extract_given_name('Edudzi/ Agbeko') == 'Agbeko'
    assert extract_given_name('Joshua/ Olaoye') == 'Olaoye'
    
       
# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
