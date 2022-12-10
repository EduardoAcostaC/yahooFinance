# Importar librerias de python
import numpy as np;
import pandas as pd;
from pandas_datareader import DataReader; # Imprtar la libreria de datareader 


# Solicitar al usuario que accion quiere conocer y validar que sea de tipo string
siglas = input(str('Introduce la accion a consultar:')); 

# Validar que la entrada del usuario se encuentre en mayusculas
siglas.upper;

# Hacer la peticion de los datos 
datos = DataReader(siglas, data_source = 'yahoo', start = '2016-1-1');
#Si necesitas ver todos los datos usa esto
#print(datos);

# Obtener los datos de la columna High 
datoHigh = np.array(datos['High']); #Se convierten a una lista para poder iterar sobre cada elemento y hacer lo correspondiente
datoLow = np.array(datos['Low']);
datoOpen = np.array(datos['Open']);
datoClose = np.array(datos['Close']);
datoVolume = np.array(datos['Volume']);
datoAdjclose = np.array(datos['Adj Close']);
#print(datoHigh); #Descomentar si quieres ver como quedo la lista
#print(len(datoHigh)); #Conocer la cantidad de datos La cantidad de datos es 1748 para todos los casos

sumaHigh = np.sum(datoHigh, axis = 0); #Sumar los datos de la columna correspondiente
sumaLow = np.sum(datoLow, axis = 0); #Sumar los datos de la columna correspondiente
sumaOpen = np.sum(datoOpen, axis = 0); #Sumar los datos de la columna correspondiente
sumaClose = np.sum(datoClose, axis = 0); #Sumar los datos de la columna correspondiente
sumaVolume = np.sum(datoVolume, axis = 0); #Sumar los datos de la columna correspondiente
sumaAdjclose = np.sum(datoAdjclose, axis = 0); #Sumar los datos de la columna correspondiente
#print(sumaLow) #Imprimir la suma de la variable que necesites


# Calcular la varianza de cada uno de los datos
varHigh = np.var(datoHigh);
varLow = np.var(datoLow);
varOpen = np.var(datoOpen);
varClose = np.var(datoClose);
varVolume = np.var(datoVolume);
varAdjclose = np.var(datoAdjclose);
#print(varHigh); #Imprimir la varianza de cada una de las variables


# Calcular la desviacion estandar
stdHigh = np.std(datoHigh);
stdLow = np.std(datoLow);
stdOpen = np.std(datoOpen);
stdClose = np.std(datoClose);
stdVolume = np.std(datoVolume);
stdAdjclose = np.std(datoAdjclose);
#print(stdHigh) #Imprimir la desviacion estandar de cada una de las variables

