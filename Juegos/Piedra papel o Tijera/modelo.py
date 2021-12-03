import tensorflow as tf
import tensorflow_datasets as tfds
import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras

builder = tfds.builder('rock_paper_scissors')
info = builder.info

datos_entrenamiento = tfds.load(name="rock_paper_scissors", split="train")
datos_prueba = tfds.load(name="rock_paper_scissors", split="test")

imagenes_entrenamiento = np.array([example['image'].numpy()[:,:,0] for example in datos_entrenamiento])
etiquetas_entrenamiento = np.array([example['label'].numpy() for example in datos_entrenamiento])

imagenes_prueba = np.array([example['image'].numpy()[:,:,0] for example in datos_prueba])
etiquetas_pruebaa = np.array([example['label'].numpy() for example in datos_prueba])

imagenes_entrenamiento = imagenes_entrenamiento.reshape(2520, 300, 300, 1)
imagenes_prueba = imagenes_prueba.reshape(372, 300, 300, 1)

imagenes_entrenamiento = imagenes_entrenamiento.astype('float32')
imagenes_prueba = imagenes_prueba.astype('float32')

imagenes_entrenamiento /= 255
imagenes_prueba /= 255

modelo = keras.Sequential([
  keras.layers.AveragePooling2D(6,3, input_shape=(300,300,1)), # crea un promedio con las capas de entrada
  keras.layers.Conv2D(64, 3, activation='relu'), # capa de convolucion 
  keras.layers.Conv2D(32, 3, activation='relu'),
  keras.layers.MaxPool2D(2,2), #maximiza el input
  keras.layers.Dropout(0.5), # reduce el sobreajuste
  keras.layers.Flatten(), #reduce los resultados (comprime) de matriz a lista
  keras.layers.Dense(128, activation='relu'), # activacion: positivo o cero
  keras.layers.Dense(3, activation='softmax') # activacion: probabilidad
])

modelo.compile(optimizer='adam',
              loss=keras.losses.SparseCategoricalCrossentropy(),
              metrics=['accuracy'])

historial = modelo.fit(imagenes_entrenamiento, etiquetas_entrenamiento, epochs=5, batch_size=32)

modelo.save('modelo-piedra-papel-o-tijera.h5') 
  

  
