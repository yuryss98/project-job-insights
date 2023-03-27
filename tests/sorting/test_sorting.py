import pytest
from src.pre_built.sorting import sort_by


@pytest.fixture
def fake_data():
    return [
        {
            "title": "Front end developer",
            "min_salary": "2000",
            "max_salary": "3000",
            "date_posted": "2020-10-25",
            "type": "full time"
        },
        {
            "title": "Back end developer",
            "min_salary": "3000",
            "max_salary": "4000",
            "date_posted": "2021-10-25",
            "type": "full time"
        }
    ]


@pytest.fixture
def ordem_decrescente():
    return [
        {
            "title": "Back end developer",
            "min_salary": "3000",
            "max_salary": "4000",
            "date_posted": "2021-10-25",
            "type": "full time"
        },
        {
            "title": "Front end developer",
            "min_salary": "2000",
            "max_salary": "3000",
            "date_posted": "2020-10-25",
            "type": "full time"
        },
    ]


def test_sort_by_criteria(fake_data, ordem_decrescente):
    sort_by(fake_data, 'max_salary')

    assert fake_data == ordem_decrescente
