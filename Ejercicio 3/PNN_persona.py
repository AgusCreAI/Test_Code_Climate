#!/usr/bin/env python3
# -*- coding: utf-8 -*-


###############################################################################
#
# Module name: persona.py
# Author(s): Fernando Diez
# Date: 18/04/2024
# Purpose:  Definición de clase persona, para gestionar empleados de la compañía
#
##############################################################################


class persona:

    def __init__(self, datos):
        '''
        Constructor de la clase persona. Almacena los datos leídos de un archivo

        Parameters
        ----------
        datos : list
            Lista de datos leídos del fichero de empleados.

        Returns
        -------
        None.

        '''
        self.info = datos
        self.nombre = datos.split(',')[1]
        self.apellido = datos.split(',')[2]
        self.NIF = datos.split(',')[0]
        self.movil = datos.split(',')[3]
        self.CCC = datos.split(',')[4]
        self.fecha = ''

        
    
    
    def contrata(self, fecha):
        '''
        Método de la clase persona que anota la fecha de contrato de un empleado

        Parameters
        ----------
        fecha : str
            Fecha de contrato en formato dd/mm/aaaa.

        Returns
        -------
        None.

        '''
        self.fecha = fecha
        
    
    def imprimePersona(self):
        '''
        Método de la clase persona que imprime los datos de una persona.

        Returns
        -------
        None.

        '''
        print(f'\nNombre: {self.nombre}')
        print(f'Apellido: {self.apellido}')
        print(f'NIF: {self.NIF}')
        print(f'Teléfono: {self.movil}')
        print(f'CCC: {self.CCC}')
        print(f'Contrato: {self.fecha}')