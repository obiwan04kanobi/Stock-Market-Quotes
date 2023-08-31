
from project import valid_country_name

def test_valid_country_name():
    assert valid_country_name("United States") == True
    assert valid_country_name("Canada") == True
    assert valid_country_name("Germany") == True
    assert valid_country_name("France") == True
    assert valid_country_name("India") == True

def test_invalid_country_name():
    assert valid_country_name("South Korea") == False
    assert valid_country_name("China") == False
    assert valid_country_name("Russia") == False
    assert valid_country_name("Italy") == False
