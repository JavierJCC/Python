print 'programa que calcula la frecuencia de cualquier texto \n';

"""Comensamos cargando el archivo"""
file = open('texto.txt', 'r');
data = file.readlines();
file.close();

diccionario ={};
contador = 0;

for renglon in data:
	for palabra in renglon.split(' '):
		contador +=1 ;
		print 'N° palabra %s y palabra %s \n'%(str (contador), palabra)
        diccionario[str(contador)]=palabra;


print 'Diccionario';

"""
Juego con cadenas
"""
primeracadena='hola';
segundacadena='-mundo';

print primeracadena + segundacadena;

entrada=raw_input();

print entrada


#condicionales 

if int(entrada) > 0:
    print 'La entrada es positiva'
else:
    print 'La entrada es negatica'
        
ent=raw_input('Prueba del bloque try except\n');
try:
    far=float(ent);
    result=(far - 32.0) * 5.0 / 9.0;
    print result
except:
    print 'por favor, introduzca el numero';


"""
print 'El tamaño del diccionario es %i \n'+diccionario.len();
Ya que se divido en palabras procederemos a separar los signos de puntuación
"""