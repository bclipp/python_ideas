import app.modulea as modulea
from unittest.mock import Mock

# stub
def test_module_stub():
    break_manager = Mock()
    modulea.do_something_refactor(break_manager)
    assert 1 == 1

# mock
def test_modulea_sleep():
    break_manager = Mock()
    modulea.do_something_refactor(break_manager)
    assert break_manager.take_break.call_count == 5
