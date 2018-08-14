# -*- coding: utf-8 -*-
"""
Created on Sun Aug 12 22:39:37 2018

@author: jchavezc1000

We have to delete the lowercase and punctuation marks

To calculate the frecuency we need to storage all tokens 
"""
#Libraries
import re, string

#Leemos el archivo txt con el texto de prueba
file = open('texto.txt', 'r');
data = file.readlines();
file.close();


diccionario ={};
contador = 0;
tam=0;
minuscula ="";


#Guardamos cafa una de las palabras en un diccionario
for renglon in data:
        print 'Renglo: %s'%(renglon)
        lista=renglon.split();
        print 'lista %s'%(lista);
        #revisar expresiones regulares
        #Ya que tenemos la lista ahora tomamos su tamaño
        for palabra in lista:
            print '%s\n'%(palabra.lower())
            minuscula=palabra.lower();
            
def remove_punctuation ( text ):
    return re.sub('[%s]' % re.escape(string.punctuation), ' ', text)
