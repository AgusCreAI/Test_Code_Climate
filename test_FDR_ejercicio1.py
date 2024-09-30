import pytest
from examen_PROG1 import (
    leeNotasClase,
    mejorEstudiante,
    peorEstudiante,
    EstacionMetro,
    LineaMetro,
    RedMetro,
    CatalanNumber
)

# Pruebas para las funciones de notas de estudiantes
def test_mejorEstudiante():
    lista = [
        ['ID1', 8, 9, 7, 10, 6],
        ['ID2', 5, 5, 5, 5, 5],
        ['ID3', 10, 10, 9, 9, 8]
    ]
    mejor_estudiante, mejor_media = mejorEstudiante(lista)
    assert mejor_estudiante == 'ID1'
    assert mejor_media == 2.0  # (10 - 6) / 2

def test_peorEstudiante():
    lista = [
        ['ID1', 8, 9, 7, 10, 6],
        ['ID2', 5, 5, 5, 5, 5],
        ['ID3', 10, 10, 9, 9, 8]
    ]
    peor_estudiante, peor_media = peorEstudiante(lista)
    assert peor_estudiante == 'ID2'
    assert peor_media == 0.0  # (5 - 5) / 2

# Prueba para la función de lectura de notas
def test_leeNotasClase(tmpdir):
    # Creamos un archivo temporal para simular las notas
    archivo = tmpdir.join("notas.csv")
    archivo.write(
        "Estudiante;Nota1;Nota2;Nota3;Nota4;Nota5\n"
        "ID1;8;9;7;10;6\n"
        "ID2;5;5;5;5;5\n"
        "ID3;10;10;9;9;8\n"
    )
    
    resultado = leeNotasClase(str(archivo))
    assert resultado == [
        ['ID1', 8, 9, 7, 10, 6],
        ['ID2', 5, 5, 5, 5, 5],
        ['ID3', 10, 10, 9, 9, 8]
    ]

# Pruebas para las clases de la red de metro
def test_estacion_metro():
    estacion = EstacionMetro("Sol")
    assert estacion.nombre == "Sol"
    assert estacion.correspondencias == []
    assert estacion.numeroCorrespondencias == 0

    estacion.setCorrespondencias([1, 2])
    assert estacion.correspondencias == [1, 2]
    assert estacion.numeroCorrespondencias == 0  # el setter no cambia esto directamente

def test_linea_metro():
    estacion1 = EstacionMetro("Sol")
    estacion2 = EstacionMetro("Opera")
    
    linea = LineaMetro(1)
    assert linea.numero == 1
    assert linea.estaciones == []
    assert linea.numeroEstaciones == 0
    
    linea.setEstaciones([estacion1, estacion2])
    assert linea.estaciones == [estacion1, estacion2]
    assert linea.numeroEstaciones == 0  # el setter no cambia esto directamente

def test_red_metro():
    red = RedMetro("Madrid")
    assert red.ciudad == "Madrid"
    assert red.lineas == []
    assert red.numeroLineas == 0

    linea = LineaMetro(1)
    red.lineas.append(linea)
    red.numeroLineas = len(red.lineas)
    assert red.numeroLineas == 1

# Pruebas para la función CatalanNumber
def test_CatalanNumber():
    assert CatalanNumber(0) == 1
    assert CatalanNumber(1) == 1
    assert CatalanNumber(2) == 2
    assert CatalanNumber(3) == 5
    assert CatalanNumber(4) == 14
