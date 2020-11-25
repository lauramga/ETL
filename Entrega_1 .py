#!/usr/bin/env python
# coding: utf-8

#   

# *Laura Martínez González De Aledo*

# ## Generación de ficheros de metadatos y lectura de formatos en python/R

#   

# ![images.jpg](attachment:images.jpg)

# #### ¿Qué es JSON?

# Para responder qué es JSON, debemos empezar por decir que sus siglas en inglés son por JavaScript Object Notation. Se trata de un formato para guardar e intercambiar información que cualquier persona pueda leer. Los archivos json contienen solo texto y usan la extensión .json.

# #### ¿Para qué se utiliza un archivo JSON?

# JSON es un formato que almacena información estructurada y se utiliza principalmente para transferir datos entre un servidor y un cliente.
# 
# El archivo es básicamente una alternativa más simple XML que cuenta con funciones similares.
# 
# Los desarrolladores usan JSON para trabajar con AJAX que funcionan bien juntos para lograr la carga asincrónica de los datos almacenados, lo que significa que un sitio web puede actualizar su información sin actualizar la página por lo que permite manejar el flujo de datos con mayor facilidad.

# #### Sintaxis JSON

# Hay dos elementos centrales en un objeto JSON: claves (Keys) y valores (Values).
# 
# Las Keys deben ser cadenas de caracteres *strings*. 
# 
# Los Values son un tipo de datos JSON válido. Puede tener la forma de *array*, objeto, cadena (string), booleano, número o nulo.
# 
# Un objeto JSON comienza y termina con llaves {}. Puede tener dos o más pares de claves/valor dentro, con una coma para separarlos. Así mismo, cada key es seguida por dos puntos para distinguirla del valor.

# #### Ejemplo

# In[1]:


import pandas as pd
import json


# A continuación leo un fichero en formato json

# In[2]:


j = open("all-federal-reserve-banks-total-assets_metadata.json", encoding="utf8")
data = json.load(j)
data


# ![logo%20yaml.png](attachment:logo%20yaml.png)

# #### ¿Qué es YAML?

# YAML es un formato para guardar objetos de datos con estructura de árbol. Sus siglas significan YAML Ain’t Markup Language (YAML no es otro lenguaje de marcado).
# 
# Este lenguaje es muy legible para las personas, más legible que un JSON y sobretodo que XML.

# #### ¿Para qué se utiliza Yaml?

# - Archivos de configuración
# - Traducciones
# - Representar información

# #### ¿Por que utilizar un YAML en vez de un JSON/XML ?

# - Un formato mucho más amigable
# - Fácil de entender rápidamente
# - Facilita el mapeo de estructuras de datos complejas.

# #### Ejemplo

# Definimos una función para leer un fichero YAML

# In[3]:


import yaml

def read_yaml_file(filename):
    with open(filename, 'r') as stream:
        try:
            print(yaml.safe_load(stream))
        except yaml.YAMLError as exc:
            print(exc)


# Genero un fichero yaml para posteriormente leerlo

# In[4]:


users = [{'name': 'John Doe', 'occupation': 'gardener'},
         {'name': 'Lucy Black', 'occupation': 'teacher'}]


# In[5]:


with open('users.yaml', 'w') as f:
    
    data = yaml.dump(users, f)


# Ahora lo leo con la función creada anteriormente

# In[6]:


read_yaml_file("users.yaml")


#  

#    

# A continuación queremos dar respuesta a las siguientes preguntas planteadas por el profesor:

# ### 1. ¿Se pueden leer con spark?

# La respuesta es sí, los siguientes links explican cómo hacerlo:
# - Para leer JSON  
#     *https://spark.apache.org/docs/latest/sql-data-sources-json.html*
#     
# - Para leer YALM  
#     *https://stackoverflow.com/questions/58806113/how-to-parse-a-yaml-with-spark-scala*

# ### 2. ¿Qué tipo de bases de datos No SQL usa estructuras de datos similares?

# ![Captura%20de%20pantalla%202020-11-25%20a%20las%2015.41.10%201.png](attachment:Captura%20de%20pantalla%202020-11-25%20a%20las%2015.41.10%201.png)

# ### Referencias
# 
# - *https://www.hostinger.es/tutoriales/que-es-json/* (JSON)
# - *https://fercontreras.com/conoce-que-es-un-yaml-e18e9d21ade4* (YAML)
# - *https://es.wikipedia.org/wiki/NoSQ* (Preg. 1)
# - *6. Big Data y Bases de Datos.pdf (Apuntes Gabriel)* (Preg. 2)

# In[ ]:




