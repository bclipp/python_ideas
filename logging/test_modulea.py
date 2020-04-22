import pytest
import sys
import log
import modulesa.modulea as ma


def test_modulea():
    log.setup_custom_logger()
    ma.do_something()
    assert 1 == 1
