import pytest
from hgt.evento import Evento


@pytest.fixture
def evento():
    return Evento(1, "FOL", True, 3, 10, 7, 14)

def test_evento(evento):
    pass