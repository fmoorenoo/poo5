import pytest
from prueba28.jugador.jugador import Jugador

@pytest.fixture
def jugador():
    return Jugador("Messi", "Bádminton")

def test_read(jugador):
    assert jugador.read() == "Messi,Bádminton"