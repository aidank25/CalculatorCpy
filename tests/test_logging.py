import pytest
import logging
from app.calculation import Division
from app.logger import setup_logger

setup_logger()

def test_logging(caplog):
    with caplog.at_level(logging.ERROR):
        with pytest.raises(ZeroDivisionError):
            test_division = Division(10,0)
            test_division.compute()

    assert "Attempted to divide by zero." in caplog.text