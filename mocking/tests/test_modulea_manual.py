from unittest.mock import Mock
import sys

# using basic python
sys.modules['time'] = Mock()
from app import modulea


def test_modulea():
    modulea.do_something()
    assert 1 == 1





