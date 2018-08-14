# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 01:27:05 2018

@author: jchavezc1000
"""

import math

int_senal = 9
int_ruido = 10

relacion = float(int_senal) / float(int_ruido)
desibelios= 10 * math.log10(float(relacion))
print desibelios

#Creacion de una funcion en python 

