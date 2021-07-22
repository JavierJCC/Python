#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 18:54:32 2021

@author: javier
"""

from scapy.all import * 
import nltk
import codecs
import matplotlib.pyplot as plt
    
def imprime_paquetes(packetes):
    for i, paquete in enumerate(packetes):
        hexdump(paquete)
        
def imprime_origen_destino_ether(paquetes, fname):
    f = codecs.open(fname, 'w', encoding='utf-8')#open a UTF-8 text file for writing
    for i, paquete in enumerate(paquetes):
        f.write(str(i) + ' ' + str(paquete[Ether].type) + '\n');
        f.write(str(i) + ' ' + paquete[Ether].src + '\n');
        f.write(str(i) + ' ' + paquete[Ether].dst + '\n');
    f.close()
    print('Message of writeList(myList, fname): '+fname+'\n')
    
def imprime_origen_destino_ipv6(paquetes, fname):
    f = codecs.open(fname, 'w', encoding='utf-8')#open a UTF-8 text file for writing
    direccionesipv6=set((paquete[IPv6].src, paquete[IPv6].dst) for paquete in paquetes if paquete.haslayer(IPv6))
    for direccion in direccionesipv6:
        f.write(str(direccion)+'\n')
    f.close()
    print('Message of writeList(myList, fname): '+fname+'\n')
    return direccionesipv6
    
def imprime_origen_destino_ipv4(fname, inputfile):
    f = codecs.open(fname, 'w', encoding='utf-8')#open a UTF-8 text file for writing
    direcciones = set((p[IP].src, p[IP].dst) for p in PcapReader(inputfile) if IP in p)
    print('Tupla de direcciones')
    for direccion in direcciones:
        f.write(str(direccion))
        f.write('\n')
    f.close();
    print('Message of writeList(myList, fname): '+fname+'\n')
    return direcciones

def crea_diccionario_de_tramas(paquetes):
    dicPaquetes={}
    for i, paquete in enumerate(paquetes):
        print(paquete)

def cuenta_ipv4(direcciones, paquetes):
    f = codecs.open(fname, 'w', encoding='utf-8')
    origen=''
    destino=''
    counter=0;
    infoconteo={}
    for direccion in direcciones:
        origen=direccion[0]
        destino=direccion[1]
        for paquete in paquetes:
            if IP in paquete:
                if paquete[IP].src == origen and paquete[IP].dst == destino:
                    counter=counter+1
        #print(counter)
        infoconteo[direccion]=counter
        counter=0;
    return infoconteo

def cuenta_ipv6(direcciones, paquetes):
    origen = ''
    destino = ''
    counter = 0
    infoconteo = {}
    for direccion in direcciones:
        origen=direccion[0]
        destino=direccion[1]
        for paquete in paquetes:
            if paquete.haslayer(IPv6):
                if paquete[IPv6].src == origen and paquete[IPv6].dst == destino:
                    counter=counter+1
        infoconteo[direccion]=counter
        counter=0
    return infoconteo
    
def writeDict(myDict, fname):
    '''writeDict(myDict, fname) writes dictionary to text file'''
    f = codecs.open(fname, "w", encoding="utf-8")#open a UTF-8 text file for writing
    print ('Escribiendo archivo...')
    num=0
    for key, value in myDict.items():
        f.write(str(key)+': '+str(value)+'\n')
    f.close()
    
def grafica_barras(diccionario):
    llaves=[]
    valores=[]
    
    for llave in diccionario.keys():
        llaves.append(str(llave))
        
    for valor in diccionario.values():
        valores.append(valor)
        
    print(llaves)
    print(valores)
    width = 0.75 # the width of the bars 
    plt.barh(llaves, valores, width, color="green")
    plt.ylabel('Direcciones IPs')
    plt.xlabel('Número de consultas')
    plt.title('Grafica')
    plt.show()

if __name__=='__main__':
    inputfile='pruebas.pcap'
    paquetes = sniff(offline='pruebas.pcap');
    fname = 'ether.txt'
    fname2 = 'ipv6.txt'
    fname3 = 'ipv4.txt'
    print(paquetes[1].show())
    hexdump(paquetes[1])
    print(paquetes[3].show())
    print(paquetes[0].getlayer(IP))
    #imprime_paquetes(packetes);
    #imprime_origen_destino_ether(paquetes, fname)
    direccionesipv6 = imprime_origen_destino_ipv6(paquetes, fname2)
    direccionesipv4 = imprime_origen_destino_ipv4(fname3, inputfile)
    dict_ipv4 = cuenta_ipv4(direccionesipv4, paquetes)
    writeDict(dict_ipv4, 'FrecuenciaIPV4.txt')
    grafica_barras(dict_ipv4)
    print('cuenta ipv6')
    dict_ipv6 = cuenta_ipv6(direccionesipv6, paquetes)
    writeDict(dict_ipv4, 'FrecuenciaIPV6.txt')
    
    