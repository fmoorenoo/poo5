import pytest
from prueba28.jugador.persona import Persona

@pytest.fixture
def persona():
    return Persona("Ferxxo")

def test_create(persona):
    assert persona.read() == "Ferxxo"