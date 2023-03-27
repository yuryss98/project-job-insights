import pytest
from src.pre_built.counter import count_ocurrences
from unittest.mock import mock_open, patch

PATH = 'data/jobs.csv'


@pytest.fixture
def fake_data():
    return """
JavaScript JavaScript JavaScript JavaScript
Python Python Python
"""


def test_counter(fake_data):
    with patch("builtins.open", mock_open(read_data=fake_data)):
        assert count_ocurrences(PATH, "JAVASCRIPT") == 4
