#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###############################################################################
#
# Module name: empresa.py
# Author(s): Fernando Diez
# Date: 18/04/2024
# Purpose:  Funciones auxiliares de gestión de la compañía
#
##############################################################################

import PNN_persona as hmn


def leeEmpleados(f, d):
    '''
    Esta función lee la lista de personas candidatas a contratar

    Parameters
    ----------
    f : str
        Nombre del fichero con los DNIs de las personas que hay que contratar.
    d : dict
        diccionario que almacena los empleados a contrarar.

    Returns
    -------
    None.

    '''
    #Abrir archivo
    with open(f, 'r') as f:
        contenido = f.read()
        for datos_empleados in contenido.split('\n'):
            p = hmn.persona(datos_empleados)
            d[p.NIF] = p


def leeDNIContrataciones(f, l):
    '''
    Esta función lee el listado de los DNI de las personas que hay que contratar

    Parameters
    ----------
    f : str
        Nombre del fichero con los datos de las personas.
    l : list
        Lista con los DNIs de las personas del fichero a contratar

    Returns
    -------
    None.
    '''
    with open(f, 'r') as f:
        contenido = f.read()
        l.extend(contenido.split('\n'))

def buscaPersona(nif, listado):
    '''
    Busca un persona según su DNI en el diccionario de personas

    Parameters
    ----------
    nif : str
        DNI de la persona a buscar.
    listado : dict
        Diccionario que contiene la información de las personas.

    Returns
    -------
    persona: instancia de la clase persona en el caso de que exista la clave DNI buscado
    None: en el caso de que NO exista la clave DNI buscado
    '''
    try:
        return listado[nif]
    except:
        None


    
def impresion(v, lp):
    '''
    Imprime la lista de personas contratadas o candidatas dependiendo de la opción
    de menú seleccionada por el usuario

    Parameters
    ----------
    v : str
        Carácter 'e' para empleados y 'c' para candidatos.
    lp : dict
        Diccionario que contiene la secuencia de personas, con contrato o candidatas

    Returns
    -------
    None.

    '''
    if v == 'e':
        for clave, dato in lp.items():
            dato.imprimePersona()
    if v == 'c':
        for clave, dato in lp.items():
            if dato.fecha == '':
                dato.imprimePersona()


def menu():
    '''
    Menu principal del programa

    Returns
    -------
    opt : int
        Opción seleccionada por el usuario.
    '''
    print('===========================================================')
    print('=                                                         =')
    print('=       SELECCIONE UNA OPCIÓN DEL MENÚ                    =')
    print('=       ------------------------------                    =')
    print('=                                                         =')
    print('=       1. CONTRATAR                                      =')
    print('=       2. IMPRIMIR EMPLEADOS                             =')
    print('=       3. IMPRIMIR CANDIDATOS                            =')
    print('=       4. BUSCAR EMPLEADO                                =')
    print('=       9. TERMINAR                                       =')
    print('=                                                         =')
    print('===========================================================')
    
    opt = int(input('TECLEE EL NÚMERO DE LA OPCIÓN DESEADA: '))
    return opt