
import modulea
from unittest.mock import patch
from time import sleep


# stub
@patch("modulea.time.sleep")
def test_module_stub(mock_time):
    modulea.do_something()
    assert 1 == 1

# mock
@patch("modulea.time")
def test_modulea_1(mock_time):
    # mock_time.get.side_effect = sleep
    modulea.do_something()
    assert mock_time.get.call_count == 5

#from mock import Mock
#mock = Mock()
#print mock.call_count