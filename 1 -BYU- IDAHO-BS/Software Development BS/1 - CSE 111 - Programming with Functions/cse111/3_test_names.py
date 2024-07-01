from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

names = [('Marie', 'Toussaint', 'Toussaint; Marie'), ('Washington Burt', 'Spencer', 'Spencer; Washington Burt'), ('Bred', 'Smith Ruber', 'Smith Ruber; Bred'), ('Billie-Rose', 'Jett', 'Jett; Billie-Rose')]

def test_make_full_name():
    for lines in names:
        given_name, family_name, full_name = lines
        print(full_name)
        assert make_full_name(given_name, family_name) == full_name

def test_extract_family_name():
     for lines in names:
        _, family_name, full_name = lines
        assert extract_family_name(full_name) == family_name

def test_extract_given_name():
    for lines in names:
        given_name, _, full_name = lines
        assert extract_given_name(full_name) == given_name

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])