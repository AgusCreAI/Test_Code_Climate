#!/usr/bin/env python3
# -*- coding: utf-8 -*-
########################################################################
#
# Module name: FDR_ejercicio1.py
# Author(s): Fernando Díez
# Date: 29/05/2024
# Purpose: Segundo examen parcial
#
########################################################################

###
# EJERCICIO 1
###

import statistics as s

def leeNotasClase(archivo):
    '''
    Lee las notas de un archivo de notas

    Parameters
    ----------
    archivo : file
        Nombre del archivo que contiene los IDs y las notas de los estudiantes en cada asignatura.

    Returns
    -------
    nombresAsignaturas : list
        lista con los nombres de las asignaturas.
    notasEstudiantes : list
        lista de listas con las notas de los estudiantes.
    '''
    notasEstudiantes = list()
    idsYnotasEstudiantes = list()
    f = open(archivo,'r')
    for line in f:
        line = line.rstrip('\n')
        if line.startswith('Estudiante'):
            continue
        else:
            notasEstudiantes = notasEstudiantes + [line.split(';')]
    solonotas = [x[1:] for x in notasEstudiantes]
    solonotas = [list(map(int,x)) for x in solonotas]
    idsEstudiantes = [x[0] for x in notasEstudiantes]                       
    for i in range(len(solonotas)):
        idsYnotasEstudiantes.append([idsEstudiantes[i]] + solonotas[i])

    return idsYnotasEstudiantes


def mejorEstudiante(lista):
    '''
    Esta función recibe una lista de listas, cada una de las cuales contiene:
        ['IDx', n1, n2, n3, n4, n5] siendo IDx el identificador del estudiante
        y nj (j=1, ..., 5), su nota en cada una de las asignaturas

    Parameters
    ----------
    lista : list
        Lista de listas: [['IDa', na1, na2, na3, na4, na5], ..., ['IDz', nz1, nz2, nz3, nz4, nz5]].

    Returns
    -------
    elmejor : str
        Identificador del estudiante con la mejor media.
    mejormedia : float
        Valor de la media del mejor estudiante.
    '''
    # DEBES SUSTITUIR LAS DOS LINEAS SIGUIENTES POR TU CODIFICACION
    mejor_nota_media = 0
    mejor_estudiante = ''
    for nota_idx in lista:
        estudiante = nota_idx[0]
        nota_media = (max(nota_idx[1:]) - min(nota_idx[1:])) / 2
        if nota_media > mejor_nota_media:
            mejor_nota_media = nota_media
            mejor_estudiante = estudiante
    return mejor_estudiante, mejor_nota_media


def peorEstudiante(lista):
    '''
    Esta función recibe una lista de listas, cada una de las cuales contiene:
        ['IDx', n1, n2, n3, n4, n5] siendo IDx el identificador del estudiante
        y nj (j=1, ..., 5), su nota en cada una de las asignaturas

    Parameters
    ----------
    lista : list
        Lista de listas: [['IDa', na1, na2, na3, na4, na5], ..., ['IDz', nz1, nz2, nz3, nz4, nz5]].

    Returns
    -------
    elpeor : str
        Identificador del estudiante con la peor media.
    peormedia : float
        Valor de la media del peor estudiante.
    '''
    # DEBES SUSTITUIR LAS DOS LINEAS SIGUIENTES POR TU CODIFICACION
    peor_nota_media = 11
    peor_estudiante = ''
    for nota_idx in lista:
        estudiante = nota_idx[0]
        nota_media = (max(nota_idx[1:]) - min(nota_idx[1:])) / 2
        if nota_media < peor_nota_media:
            peor_nota_media = nota_media
            peor_estudiante = estudiante
    return peor_estudiante, peor_nota_media


###
# EJERCICIO 2
###

class EstacionMetro:
    '''
    Clase que representa una estación de metro.

    Atributos:
        nombre (str): Nombre de la estación. Inicializa al nombre que se indique.
        correspondencias (list[int]): Lista de identificadores de las estaciones con las que conecta. Inicializa a []
        numeroCorrespondencias (int): Número de estaciones con las que conecta. Inicializa a 0
    '''

    def __init__(self, nombre):
        self.nombre = nombre
        self.correspondencias = []
        self.numeroCorrespondencias = 0
    
    def setCorrespondencias(self, lista):
        '''
        Este método anota en el atributo correspondencias la lista de líneas con las que hay correspondencia en 
        la estacionMetro.
        Parameters
        ----------
        lista : list
            Lista con las líneas con las que hay correspondencia.
            
        Returns
        -------
        None.

        '''
        self.correspondencias = lista
    
    
class LineaMetro:
    '''
    Clase que representa una línea de metro.

    Atributos:
        numero (int): Número identificativo de la línea. Inicializa al numero que se indique
        estaciones (list[EstacionMetro]): Lista de estaciones que pertenecen a la línea. Inicializa a []
        numeroEstaciones (int): Número de estaciones en la línea. Inicializa a 0
    '''

    def __init__(self, numero):
        self.numero = numero
        self.estaciones = []
        self.numeroEstaciones = 0
    
    
    def setEstaciones(self, lista):
        '''
        Este método anota en el atributo estaciones la lista de instancias de EstacionMetro.

        Parameters
        ----------
        lista : list
            Lista con las EstacionMetro que hay en la linea.

        Returns
        -------
        None.

        '''
        self.estaciones = lista


class RedMetro:
    '''
    Clase que representa una red de metro.

    Atributos:
        ciudad (str): Nombre de la ciudad donde se encuentra la red. Inicializa al nombre que se indique
        lineas (list[LineaMetro]): Lista de líneas de metro que pertenecen a la red. Inicializa a []
        numeroLineas (int): Número de líneas de metro en la red. Inicializa a 0
    '''

    def __init__(self, ciudad):
        self.ciudad = ciudad
        self.lineas = []
        self.numeroLineas = 0


###
# EJERCICIO 3
###

# PARA EL EJERCICIO 3 DEBES DESCARGAR LOS MODULOS .py QUE SE INDICAN EN EL
# ENUNCIADO Y ENTREGAR 2 MÓDULOS POR SEPARADO

###
# EJERCICIO 4
###

import math 

def CatalanNumber(n):
    '''
    Esta función calcula e imprime los n primeros numneros de Catalan

    Parameters
    ----------
    n : int >= 0
        n-ésimo número de Catalan que se desea obtener.

    Returns
    -------
    catalan: int
        n-ésimo número de Catalan.
    '''
    # DEBES SUSTITUIR LAS DOS LINEAS SIGUIENTES POR TU CODIFICACION
    return math.factorial(2 * n) // (math.factorial(n + 1) * math.factorial(n))
            

###
# PROGRAMA PRINCIPAL. ¡¡¡ NO TOCAR !!!
###

if __name__ == '__main__':
    
    opcion = int(input('\nIndica el ejercicio que deseas ejecutar (1, 2 o 3): '))
    if opcion == 1:
        print("\n######   E J E R C I C I O --- 1   ###### ")
        archivo = 'notas.csv'
        # Se leen las notas (ESTO SE TE DA HECHO)
        idsYnotas = leeNotasClase(archivo)
        
        # Se calcula el mejor estudiante (ESTO DEBES HACERLO TÚ)
        idMejor, mediaMejor = mejorEstudiante(idsYnotas)
        
        # Se calcula el peor estudiante (ESTO DEBES HACERLO TÚ)
        idPeor, mediaPeor = peorEstudiante(idsYnotas)
    
        print(f'\nEl mejor estudiante es {idMejor} con media {mediaMejor}')
        print(f'El peor estudiante es {idPeor} con media {mediaPeor}\n\n')
    elif opcion == 2:
        print("\n######   E J E R C I C I O --- 2   ###### ")
    
        # Crear una estación de metro
        estacion1 = EstacionMetro("Gran Vía")
        estacion2 = EstacionMetro("Chueca")
        estacion3 = EstacionMetro("Alonso Martinez")
    
        # Agregar correspondencias a las estaciones creadas
        estacion1.setCorrespondencias([1])
        estacion1.numeroCorrespondencias = len(estacion1.correspondencias)
        estacion2.setCorrespondencias([])
        estacion2.numeroCorrespondencias = len(estacion2.correspondencias)
        estacion3.setCorrespondencias([4, 10])
        estacion3.numeroCorrespondencias = len(estacion3.correspondencias)
    
        # Crear una línea de metro
        linea1 = LineaMetro(5)
    
        # Agregar estaciones a la línea
        linea1.setEstaciones([estacion1, estacion2, estacion3])
        linea1.numeroEstaciones = len(linea1.estaciones)
    
        # Crear una red de metro
        redMetro = RedMetro("Madrid")
    
        # Agregar líneas a la red
        redMetro.lineas.append(linea1)
        redMetro.numeroLineas = len(redMetro.lineas)
    
        # Imprimir información de la red
        print(f"Ciudad: {redMetro.ciudad}")
        print(f"Número de líneas: {redMetro.numeroLineas}")
        
        for linea in redMetro.lineas:
            print(f"\nLínea {linea.numero}:")
            for estacion in linea.estaciones:
                print(f"- {estacion.nombre} (correspondencias: {estacion.correspondencias})")
    else:
        print("\n######   E J E R C I C I O --- 3   ###### ")
        for i in range(26):
            print(f'{CatalanNumber(i):.0f}') 

