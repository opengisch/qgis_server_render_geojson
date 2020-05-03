import pytest
import os

@pytest.fixture
def test_data_path():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(dir_path, 'demodata')
