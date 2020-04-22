import sys
from unittest.mock import Mock
sys.modules['time'] = Mock()
import modulesa.modulea as ma


def test_modulea():
    ma.do_something()
    assert 1 == 1
