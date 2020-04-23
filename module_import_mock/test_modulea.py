import pytest
from pytest_mock import mocker


# stub a import that a module under test uses
###############

# using basic python
import time
# sys.modules['time'] = Mock()
import modulea
def test_modulea():
    modulea.do_something()
    assert 1 == 1

# using pytest-mock
def test_modulea(mocker):
    mocker.patch.object(modulea, "time")
    mocker.ANY
    modulea.do_something()
    assert 1 == 1

# using pytest-mock getting a return value to time.sleep
def test_modulea(mocker):
    mocker.patch.object(modulea, "time")
    mocker.patch("modulea.time.sleep", return_value="This a a fake return value from time.sleep")
    print(modulea.do_something2())
    assert 1 == 1

# using pytest-mock checking patched usage
def test_modulea(mocker):
    mocker.patch.object(modulea, "time")
    mocker.patch("modulea.time.sleep", return_value="This a a fake return value from time.sleep")
    print(modulea.do_something2())
    assert 1 == 1

# using pytest-mock
def test_modulea(mocker):
    mocker.patch.object(modulea, "time")
    mocker.ANY
    modulea.do_something()
    assert 1 == 1

#using standard python

from unittest.mock import Mock
from unittest.mock import patch

# stub
@patch("modulea.time")
def test_modulea_1(mock_time):
    modulea.do_something()
    assert 1 == 1

# mock
@patch("modulea.time")
def test_modulea_1(mock_time):
    modulea.do_something()
    assert 1 == 1

#from mock import Mock
#mock = Mock()
#print mock.call_count