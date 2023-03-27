import pytest
from src.pre_built.brazilian_jobs import read_brazilian_file
from unittest.mock import patch


@pytest.fixture
def mocked_job():
    return [{"title": "Maquinista", "salary": "2000", "type": "trainee"}]


def mocked_read(path):
    return [{"titulo": "Maquinista", "salario": "2000", "tipo": "trainee"}]


def test_brazilian_jobs(mocked_job):
    with patch("src.insights.jobs.read", mocked_read):
        assert (
            read_brazilian_file("tests/mocks/brazilians_jobs.csv")
            == mocked_job
        )
