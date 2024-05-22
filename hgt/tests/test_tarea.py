import pytest 
from hgt.tarea import Tarea

@pytest.fixture
def tarea():
    return Tarea(1, "Programación", False)

def test_read(tarea):
    assert tarea.read() == "1|&&|Programación|&&|False"


def test_update(tarea):
    tarea.update(2, "Sistemas", True)
    assert tarea.read() == "2|&&|Sistemas|&&|True"


def test_delete(tarea):
    tarea.delete()
    assert tarea.read() == 'None|&&|None|&&|None'