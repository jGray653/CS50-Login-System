from project import login, create, descision
import pytest

def test_login():
    assert login("John_123", "pas1234") == "User Doesn't Exist, Please Create An Account\n"
    assert login("Jay_944", "wzh9951") == "Hello, Jay Gray"
    assert login("Jay_944", "pas1234") == "Incorrect Password"
    assert login("John_793", "lfb2682") == "Hello, John Doe"

def test_create():
    assert create("Jay Gray") == "User Already Exists, Please Try Again"
    assert create("Jane Doe") == "User Created! Please Sign In!"
    # ^ Must be deleted from the csv file after running pytest, otherwise it will show a failure if run again


def test_descision():
    assert descision("7") == "Invalid Selection, Please Try Again\n"
