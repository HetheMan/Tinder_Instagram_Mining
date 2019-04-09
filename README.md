### Data Mining: Tinder UAH en Instagram con Python
Extracción del conocimiento de las imágenes publicadas por la cuenta Tinder de la universidad de Alcala de Henares.
Con Data Mining extraemos la información de la cuenta de Tinder de la Universidad de Alcala de Henares.La extracción de la información la entendemos como:

## Recopilación de datos
* Seleccion, limpieza y transformación
* Minería de datos
* Interpretación
* Tras esto llegamos al conocimiento.

## Objetivo
Existe una cuenta de Instagram en la que estudiantes mandan mensajes privados, estos mensajes tienen el propósito de encontrar a una persona en particular al más puro estilo Tinder. Las personas que llevan la cuenta cuelgan la foto para que todos los seguidores puedan verlo. Esto lo comentamos en el articulo. Por lo tanto queremos sumar la información de todas las fotos y sacar estadísticas.

## Recopilación de los datos
Usamos instagram-scrapper, un modulo de Python. Sacamos las fotos de cualquier perfil público, y para los privados necesitamos seguirlos. Lo instalamos con:
```
pip install instagram-scraper
```

Para descargar todas las fotos, escribimos el siguiente comando directamente en el cmd:
```
instagram-scraper tinder_uah -u micuenta -p micontraseña
```

Tarda un poco (dependiendo de cuántas fotos haya) y todas las fotos se exportan en una carpeta del directorio actual llamada por nuestro nombre de usuario de instagram.

## Selección, limpieza y transformación
Todo el código a partir de este momento esta subido en Github. Destaco el proceso. Dependencias externas:

### Images
* CV2: cargar imagenes
* Pytesser: Leer texto imagenes
En scrapper.py primero leemos las imagenes y guardamos los string en un archivo, después limpiamos los string y nos guardamos la informacion en una tabla en Excel.
```
if __name__ == "__main__":
p.cargaInicialListasFemenino()
#parseTextos() #Descomentar para leer imagenes
#guardarParser() #Descomentar para leer imagenes
cargarParser(
extraccion_datos()
Primero cargamos las estrucutras de datos del parser que nos faltan p.cargaInicialListasFemenino() (cambiar de masculino a femenino). Después leemos las imagenes parseTextos() y guardamos la lista de String resultante guardarParser(). Los siguientes metodos cargan esta lista (persistencia) cargarParser y depuran los datos que nos interesan, guardamos los datos en una tabla Excel.
```
##Minería de datos
Dependencias externas:

* Pandas: Minería de Datos.
En extraccion.py:
```
if __name__ == "__main__":
tabla=crearDataframe("foobar.xls")
tabla =remplazarNoEncontrado(tabla)
tablaHombre = tabla.loc[tabla['SEXO']=="HOMBRE"]
tablaMujer = tabla.loc[tabla['SEXO']=="MUJER"]
exportarSerie(tabla,"AMBOS.json")
exportarSerie(tablaHombre,"HOMBRE.json")
exportarSerie(tabla,"MUJER.json")
```
Leemos la tabla, luego quitamos las fotos en las que no se haya encontrado ningún sexo. Después hacemos 3 conjuntos, el conjunto total y dos subconjuntos,uno para cada sexo. Por último exportamos las series en formato JSON, estos JSON tendrás las frecuencias de cada caracteristica, las que se pueden ver en el articulo de exposición.
