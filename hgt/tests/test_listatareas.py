import pytest
from hgt.listatareas import ListaTareas

@pytest.fixture
def lista():
    return ListaTareas()

def test_listaTarea0(lista):
    assert len(lista) == 0

def test_listaTarea1(lista):
    lista.agregar('Programación')
    assert len(lista) == 1

def test_listaTarea2(lista):
    lista.agregar('Inglés')
    lista.agregar('FOL')

    assert len(lista) == 2
    assert lista[0] == 'Inglés'
    assert lista[1] == 'FOL'

def test_listaTareaDelete(lista):
    lista.agregar('Programación')
    assert lista[0] == 'Programación'

    del lista[0]
    assert len(lista) == 0

    assert 'Programación' not in lista

def test_listaRead(lista):
    lista.agregar('Programación')
    lista.agregar('FOL')

    assert lista.read() == 'Programación' + lista.LIMITCHAR + 'FOL'

def test_listaLoad(lista):
    lista.load('Programación' + lista.LIMITCHAR + 'FOL')
    assert len(lista) == 2

    assert lista[0] == 'Programación'
    assert lista[1] == 'FOL'