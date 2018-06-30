import pandas as pd
import numpy as np
import write as wr
import json
def crearDataframe(cadena:str):
    return pd.read_excel(cadena)
def remplazarValorColumna(data,columna,valor,remplazar):
    return data[columna].replace(valor,remplazar)
def remplazarNoEncontrado(data):
    return data.replace("NO ENCONTRADO",np.NaN)
def buscarPorValorEnColumna(data,valor,columna):
    return data.loc[data[columna] == valor]
    #df.loc[df['column_name'].isin(some_values)]
def contarValoresColumna(data,columna):
    data[columna].value_counts()
def getFrecuenciasSexoDetalle(data):
    frecuencias = data['SEXO'].value_counts()
    frecuenciaHombre = frecuencias['HOMBRE']
    frecuenciaMujer = frecuencias['MUJER']
    return frecuenciaHombre, frecuenciaMujer
def getFrecuenciasSexo(data):
    return data['SEXO'].value_counts()
def getFrecuenciasUniversidad(data):
    return data['UNIVERSIDAD'].value_counts()
def getFrecuenciasColorOjos(data):
    return data['COLOR_OJOS'].value_counts()
def getFrecuenciasColorPelo(data):
    return data['COLOR_PELO'].value_counts()   
def getFrecuenciasAltura(data):
    return data['ALTURA'].value_counts()
def getFrecuenciasBarba(data):
    return data['BARBA'].value_counts()
def getFrecuenciasEstiloPelo(data):
    return data['ESTILO PELO'].value_counts()
def imprimirInforme(tabla):
    frecHombre,frecMujer = getFrecuenciasSexo(tabla)
    wr.imprimirInforme(frecHombre,frecMujer,getFrecuenciasUniversidad(tabla),getFrecuenciasColorOjos(tabla),getFrecuenciasColorPelo(tabla),getFrecuenciasBarba(tabla),getFrecuenciasAltura(tabla),getFrecuenciasEstiloPelo(tabla))
def verColumnas(data):
    print(data.columns.values)
def imprimirJSON(data,nombre):
    with open("json/"+nombre,'w') as outfile:
        json.dump(data,outfile)
def anadirCabeceraJSON(jsons,eslista):
    return ""+"\""+eslista+"\""+": "+ jsons +""
def concatenarElementosJSON(elementos):
    completo = "{ " +elementos[0]
    for elemento in elementos[1:]:
        completo = completo +", "+elemento 
    return completo + " }"
def imprimirTextoJson(texto,nombre):
    with open("json/"+nombre,'w') as outfile:
        outfile.write(texto)
def transformarenArray(elementos):
    name = []
    data = [] 
    for i in range(0,elementos.size):
        name.append(elementos.index[i])
        data.append(elementos[i])
    return name,data
def transformarenArrayJSON(elementos,nombre):
    name,data = transformarenArray(elementos)
    nombreArray = comillas("name")+":" + comillas(nombre)
    lista = []
    for i in range(0,len(name)):
        cadena = "{"+"\"name\":" + "\""+name[i]+"\"" + "," + "\"data\":" + "\""+ str(data[i]) + "\"" + "}"
        lista.append(cadena)
    retorno = lista[0]
    for elemento in lista[1:]:
        retorno = retorno + "," + elemento
    return " {" + nombreArray + "," + comillas("data")+":"+  "[" + retorno + "]" +"}"
def comillas(nombre):
    return "\""+ nombre + "\""
def arrayElementosJSON(elementos):
    return "[" + elementos +"]"
def juntarArrays(arrays):
    retorno = arrays[0]
    for elemento in arrays[1:]:
        retorno = retorno + "," + elemento
    return retorno
def juntarEnComponente(nombre,componente):
    return "\"name\":" + "\""+nombre+"\"" + "," + "\"data\":" +  componente
def exportarSerie(tabla,nombreaExportar):
    
    sexos=transformarenArrayJSON(getFrecuenciasSexo(tabla),"SEXO")
    universidades=transformarenArrayJSON(getFrecuenciasUniversidad(tabla),"UNIVERSIDADES")
    colorOjos=transformarenArrayJSON(getFrecuenciasColorOjos(tabla),"COLOR_OJOS")
    colorPelo=transformarenArrayJSON(getFrecuenciasColorPelo(tabla),"COLOR_PELO")
    #barba=transformarenArrayJSON(getFrecuenciasBarba(tabla),"BARBA")
    altura=transformarenArrayJSON(getFrecuenciasAltura(tabla),"ALTURA")
    estiloPelo=transformarenArrayJSON(getFrecuenciasAltura(tabla),"ESTILO_PELO")
    lista = []
    lista.append(sexos)
    lista.append(universidades)
    lista.append(colorOjos)
    lista.append(colorPelo)
    #lista.append(barba)
    lista.append(altura)
    lista.append(estiloPelo)
    t = juntarArrays(lista)
    imprimirTextoJson("["+t+"]",nombreaExportar)
if __name__ == "__main__":
    tabla=crearDataframe("foobar.xls")
    tabla =remplazarNoEncontrado(tabla)
    tablaHombre = tabla.loc[tabla['SEXO']=="HOMBRE"]
    tablaMujer = tabla.loc[tabla['SEXO']=="HOMBRE"]
    exportarSerie(tabla,"AMBOS.json")
    exportarSerie(tablaHombre,"HOMBRE.json")
    exportarSerie(tabla,"MUJER.json")
    # lista_JSON = []
    # sexos = anadirCabeceraJSON(getFrecuenciasSexo(tabla).to_json(),"SEXO")
    # universidades = anadirCabeceraJSON(arrayElementosJSON(getFrecuenciasUniversidad(tabla).to_json()),"UNIVERSIDADES")
    # colorOjos = anadirCabeceraJSON(getFrecuenciasColorOjos(tabla).to_json(),"COLOR_OJOS")
    # colorPelo = anadirCabeceraJSON(getFrecuenciasColorPelo(tabla).to_json(),"COLOR_PELO")
    # barba = anadirCabeceraJSON(getFrecuenciasBarba(tabla).to_json(),"BARBA")
    # altura = anadirCabeceraJSON(getFrecuenciasAltura(tabla).to_json(),"ALTURA")
    # estiloPelo = anadirCabeceraJSON(getFrecuenciasEstiloPelo(tabla).to_json(),"ESTILO_PELO")
    # # lista_JSON.append(sexos)
    # lista_JSON.append(universidades)
    # # lista_JSON.append(colorOjos)
    # # lista_JSON.append(colorPelo)
    # # lista_JSON.append(barba)
    # # lista_JSON.append(altura)
    # # lista_JSON.append(estiloPelo)
    # completo=concatenarElementosJSON(lista_JSON)
    # imprimirTextoJson(completo,"Instagram_Mining.json")
    # print(concatenarElementosJSON(lista_JSON))
    
   
    # imprimirJSON(getFrecuenciasSexo(tabla),"sexos.txt")
    # imprimirJSON(getFrecuenciasUniversidad(tabla),"universidades.txt")
    # imprimirJSON(getFrecuenciasColorOjos(tabla),"colorOjos.txt")
    # imprimirJSON(getFrecuenciasColorPelo(tabla),"colorPelo.txt")
    # imprimirJSON(getFrecuenciasBarba(tabla),"barba.txt")
    # imprimirJSON(getFrecuenciasAltura(tabla),"altura.txt")
    # imprimirJSON(getFrecuenciasEstiloPelo(tabla),"estiloPelo.txt")
    # print(getFrecuenciasSexo(tabla))
    # print(getFrecuenciasUniversidad(tabla))
    # print(getFrecuenciasColorOjos(tabla))
    # print(getFrecuenciasColorPelo(tabla))
    # print(getFrecuenciasBarba(tabla))
    # print(getFrecuenciasAltura(tabla))
    # print(getFrecuenciasEstiloPelo(tabla))

    # print("FRECUENCIAS POR SEXO HOMBRE")
    # tablaHombre = tabla.loc[tabla['SEXO']=='HOMBRE']
    # print(getFrecuenciasSexo(tablaHombre))
    # print(getFrecuenciasUniversidad(tablaHombre))
    # print(getFrecuenciasColorOjos(tablaHombre))
    # print(getFrecuenciasColorPelo(tablaHombre))
    # print(getFrecuenciasBarba(tablaHombre))
    # print(getFrecuenciasAltura(tablaHombre))
    # print(getFrecuenciasEstiloPelo(tablaHombre))

    # print("FRECUENCIAS POR SEXO MUJER")
    # tablaMujer = tabla.loc[tabla['SEXO']=='MUJER']
    # print(getFrecuenciasSexo(tablaMujer))
    # print(getFrecuenciasUniversidad(tablaMujer))
    # print(getFrecuenciasColorOjos(tablaMujer))
    # print(getFrecuenciasColorPelo(tablaMujer))
    # print(getFrecuenciasBarba(tablaMujer))
    # print(getFrecuenciasAltura(tablaMujer))
    # print(getFrecuenciasEstiloPelo(tablaMujer))

    
    #table.describe()