#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###############################################################################
#
# Module name: gestion.py
# Author(s): Fernando Diez
# Date: 18/04/2024
# Purpose:  Programa principal de gestión de la compañía
#
##############################################################################

import os
import PNN_aux_gestion as bsns
        
    
# ==================== #
#  PROGRAMA PRINCIPAL  #
# ==================== #

if __name__ == '__main__':
    opcion = 0
    # DEFINIMOS LAS ESTRUCTURAS DE DATOS PARA ALMACENAR INFORMACIÓN DE EMPLEADOS
    listadoPersonas = dict()        # PERSONAS CANDIDATAS A CONTRATAR
    listaContrataciones = list()    # DNIs A CONTRATAR
    
    while opcion != 9:
        os.system('clear')      # LIMPIA LA CONSOLA
        opcion = bsns.menu()    # EJECUTA MENU
        
        # LECTURA DE DATOS DE PERSONAS Y DE DNI PARA CONTRATAR
        if opcion == 1:
            fileEmp = input('Introduce el nombre del fichero de personas: ')
            bsns.leeEmpleados(fileEmp, listadoPersonas)
            fileDNI = input('Introduce el nombre del fichero de DNIs a contratar: ')
            bsns.leeDNIContrataciones(fileDNI, listaContrataciones)
            fechaContrato = input('Introduce la fecha de contrato en formato dd/mm/aaaa: ')
            
            # RECORREMOS LA LISTA DE DNIs PARA CONTRATAR Y SI ALGUNO COINCIDE
            # CON EL DNI DE LA PERSONA DEL LISTADO DE PERSONAS, 
            # SE LE CONTRATA
            for dni in listaContrataciones:
                for nif,item in listadoPersonas.items():
                    if dni == nif:
                        item.contrata(fechaContrato)
        
        # IMPRIME LISTA DE EMPLEADOS
        elif opcion == 2:
            bsns.impresion('e', listadoPersonas)
            input('\nPulse una tecla para continuar')
            
        # IMPRIME LISTA DE CANDIDATOS
        elif opcion == 3:
            bsns.impresion('c', listadoPersonas)
            input('\nPulse una tecla para continuar')
        
        # PIDE DNI PARA BUSCAR E IMPRIMIR LOS DATOS DEL EMPLEADO (SI EXISTE)
        elif opcion == 4:
            nif = input('Teclea el DNI a buscar: ')
            p = bsns.buscaPersona(nif, listadoPersonas)
            if p == None:
                print(f'La persona de DNI {nif} no está en la compañía')
                print()
                input('Pulse una tecla para continuar')
            else:
                p.imprimePersona()
                input('Pulse una tecla para continuar')
