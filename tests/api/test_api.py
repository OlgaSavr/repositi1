import pytest

@pytest.mark.change
def test_rem_name(user):
    user.name = ''
    assert user.name == ''

@pytest.mark.chek
def test_name (user):
    assert user.name == 'Olga'

@pytest.mark.chek
def test_second_name(user):
    assert user.second_name == 'Savrol'