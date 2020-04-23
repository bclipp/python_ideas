from unittest.mock import Mock
import sys

# using basic python
import time
sys.modules['time'] = Mock()
import modulea
def test_modulea():
    modulea.do_something()
    assert 1 == 1



