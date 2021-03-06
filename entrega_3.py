# -*- coding: utf-8 -*-
"""Entrega_3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1th6o8a6yw1KqEFXW4Su-3VPRuz483-Lo
"""



"""*Laura Martínez González de Aledo*

## Histograma de los puntos de los visitantes

__OBJETIVO:__ 

Replicar la función histogram de los rdd, esta nos ofrece una lista de tuplas formadas por los cortes de las columnas y las frecuencias de cada columna.

Realizo un mapeo sobre el rdd liga_parsed y me quedo con los puntos de los equipos visitantes.

En primer lugar se ha de inicializar el contexto spark.
"""

!apt-get install openjdk-8-jdk-headless -qq > /dev/null
!wget -q https://www-us.apache.org/dist/spark/spark-2.4.7/spark-2.4.7-bin-hadoop2.7.tgz
!tar xf spark-2.4.7-bin-hadoop2.7.tgz 
!pip install -q findspark 

import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64" 
os.environ["SPARK_HOME"] = "/content/spark-2.4.7-bin-hadoop2.7"

import findspark 
findspark.init()
from pyspark import SparkContext
sc = SparkContext()
from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[*]").getOrCreate()

"""
Ahora cargamos el archivo propiamente dicho:"""

data_file = "./partidosLigaNBA.csv"
liga_data = sc.textFile(data_file)

liga_data.count()

liga_data.take(3)

"""Quito el header y los playoffs"""

liga_data_split = liga_data.filter(lambda x: "PTS" not in x).filter(lambda x: "Playoffs" not in x)

import re

ejemplo = liga_data_split.take(2)

"""Media de la diferencia de puntos por año"""

liga_parsed = liga_data_split.map(lambda line:parse_log(line))

"""Calculo la diferencia de puntos por partido, me quedaré con el año en que se jugó el partido y esa diferencia."""

diferencia_puntos = liga_parsed.map(lambda x: (x[3], abs((int(x[6])-int(x[8])))))

"""Ahora agrupo en función del año."""

diferencia_agrupada = diferencia_puntos.reduceByKey(lambda x,y: x + y)

"""Calculo el número de partidos que se han jugado por año. El método es parecido al de antes, pero hago un conteo."""

num_partidos = liga_parsed.map(lambda x: (x[3],1)).reduceByKey(lambda x,y: x + y)

"""
Ahora realizo un join de los dos rdd, diferencia de puntos y número de partidos, divido la diferencia entre el número de partidos."""

diferencia_agrupada.join(num_partidos).map(lambda x:(x[0],(x[1][0]/x[1][1]))).sortByKey().collect()

type(visitor_points)

"""Hago un collect y almaceno la lista en una variable."""

import re
x = visitor_points.collect()

"""Ordeno los elementos de la lista."""

x.sort()

Calculo los cuaertiles.

# 25%

x[int(len(x)*.25)]

# 50%

x[int(len(x)*.50)]

# 75%

x[int(len(x)*.75)]

"""Defino una función para aplicar luego mediante un map, me clasifica los puntos en los cuartiles."""

def cuartiles(puntos):
    if puntos <= 98:
        if puntos <= 91:
            return (1)
        else:
            return (2)
    else:
        if puntos <= 107:
            return (3)
        else:
            return (4)

"""Aplico el map con la función cuartiles, genero también un contador, de esta forma tendremos un rdd con tuplas que tendrán como key o label el cuartil correspondiente y la frecuencia como valor."""

visitor_points.map(lambda x: (cuartiles(x),1)).reduceByKey(lambda y,z: y + z).collect()

labels, ys = zip(*visitor_points)
xs = np.arange(len(labels)) 
width = 1

plt.bar(xs, ys, width, align='center')

plt.xticks(xs, labels) 
plt.yticks(ys)

sc.stop()