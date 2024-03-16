import pandas as pd
#import matplotlib.pyplot as plt

#crear diccionario
"""data2 = { 
    'Nombres' : ['Juan', 'Maria', 'Carlos', 'Luis', 'Ana', 'Jaime', 'Flor', 'Anibal', 'Anastasia', 'Dolores'],
    'Apellidos' : ['Coral', 'Martinez', 'Rosero', 'Muñoz', 'Lopez', 'Zambrano', 'Rosales', 'Burbano', 'Perez', 'Ortiz'],
    'Edad' : [20, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    'Matematicas' : [85, 90, 75, 88, 92, 70, 82, 94, 85, 78],
    'Ciencias' : [78, 85, 80, 92, 87, 87, 86, 98, 57, 87]
}"""

#crear un datafreme a partir de un diccionario
#df = pd.DataFrame(data2)

#guardar el dataframe en un archivo cvs
#df.to_csv ('C:\Users\Udenar\Desktop\TalentoTech\practica_pyhton_SQL')

#df.to_csv('datos2sql.csv') #Guardamos los datos directamente en la carpeta donde se ejecuta el script
#print ("archivo creado satisfactoriamente")


df = pd.read_csv('datos2sql.csv') 

print("Primeras filas")
print (df.head())

#Resumen estadistico
print("\nResumen esttadisitico de las calificaciones")
print (df[['Matematicas', 'Ciencias']].describe())

#calcular promedios
df['Promedio'] = df[['Matematicas', 'Ciencias']].mean(axis=1)


#filtrar estudiantes que obtuvieron promedio superior a 80
print('Estudiantes con un promedio superior a 80')
print(df[df['Promedio'] > 80])









