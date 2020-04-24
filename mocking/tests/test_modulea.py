# from app import modulea
from unittest.mock import patch
import app.modulea as modulea
from time import sleep
# patching
# stub
@patch("modulea.time.sleep")
def test_module_stub(mock_time):
    modulea.do_something()
    assert 1 == 1

# mock
@patch("modulea.time")
def test_modulea_sleep(mock_time):
    mock_time.sleep.side_effect = sleep
    modulea.do_something()
    assert mock_time.sleep.call_count == 5

# mock
@patch("modulea.time.sleep")
def test_modulea_time(mock_time):
    modulea.mycode()
    assert mock_time.call_count == 5

# using mock object