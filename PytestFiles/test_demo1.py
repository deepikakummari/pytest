import pytest
@pytest.mark.login
def test_m1():
    a=4
    b=3
    assert b+1==a
    assert a==b
def test_m2():
    assert True
@pytest.mark.login
def test_m3():
    assert False
@pytest.mark.login
def test_m4():
    name="deepika"
    assert name.upper()=="DEEPIKA"
def test_m5():
    assert "ruthu"=="RUTHU"
@pytest.mark.login
def test_login():
    assert "admin"=="admin"



