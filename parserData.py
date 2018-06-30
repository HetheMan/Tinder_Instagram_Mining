# coding=cp1252
UNIVERSIDADES =  ["DERECHO","POLITECNICA","FARMACIA","MEDICINA","ARQUITECTURA","ENFERMERIA","BIOLOGIA","ECONOMICAS","FISIOTERAPIA","DERECHO","MAGISTERIO","HISTORIA","HUMANIDADES","PSICOLOGIA","COMPUTADORES","CIENCIAS DE LA COMPUTACION","ELECTRONICA","SISTEMAS DE INFORMACION","TURISMO","QUIMICA"]
UNIVERSIDADES_COLOQUIAL =  ["POLI","FISIO","TELECO"] #Bio lo quitamos por si rubio
ASIGNATURAS_POLITECNICA = ["INFORMATICA","TELECOMUNICACIONES","INDUSTRIALES","SISTEMAS DE LA INFORMACION","ELECTRONICA","CIENCIAS DE LA COMPUTACION","COMPUTADORES"]
SEXO_MASCULINO = ["CHICO","INDIVIDUO","MAROMO","MOZO","CHAVAL","CHAVALITO"]
SEXO_FEMENINO = []
COLORES  = ["AZULES", "VERDES","OSCUROS","CASTAÑOS","MARRONES","NEGROS"]
COLOR  = ["AZUL","VERDE","CASTAÑO","OSCURO","NEGRO","MARRON"]
COLOR_PELO = ["RUBIO","CASTAÑO","NEGRO","ROSA","AZUL","ROJO","GRIS","PELIRROJO"]
ALTURA_MASCULINO = ["ALTO","BAJO","ALTITO","BAJITO","PEQUEÑO","PEQUEÑITO"]
ALTURA_FEMENINO = []
BARBA = ["BARBA","BARBITA","BARBOTA"]
ESTILO_PELO = ["RIZADO","LARGO","CORTO","LISO","CRESTA","ONDULADO","COLETA"]

def remplazarTildes(cadena:str):
    cadena = cadena.replace("á","a")
    cadena = cadena.replace("é","e")
    cadena = cadena.replace("í","i")
    cadena = cadena.replace("ó","o")
    cadena = cadena.replace("ú","u")
    return cadena
def parserPolitecnica(universidad):
    if universidad in ASIGNATURAS_POLITECNICA:
        return "POLITECNICA"
    else:
        return universidad
def cargaInicialListasFemenino():
    global SEXO_FEMENINO
    global ALTURA_FEMENINO
    SEXO_FEMENINO= listaEnFemenino(SEXO_MASCULINO)
    ALTURA_FEMENINO= listaEnFemenino(ALTURA_MASCULINO)
def listaEnFemenino(lista):
    devolver = []
    for elemento in lista:
        if elemento == "CHAVAL":
            devolver.append("CHAVALA")
        else:
            devolver.append(elemento[:-1] + "A")
    return devolver

def parserUniUniversidad(uni):
    if uni == "POLI":
        return "POLITECNICA"
    elif uni=="FISIO":
        return "FISIOTERAPIA"    
    elif uni=="TELECO":
        return "TELECOMUNICACIONES"
    elif uni=="MICRO":
        return "MICROBIOLOGIA"
    else:
        return uni
#Limpiamos para obtener informaci�n de las personas que queremos.
def limpiar(cadena:str):
    cadena = remplazarTildes(cadena)
    for universidad in UNIVERSIDADES:
        for chico in SEXO_MASCULINO:
            if cadena.upper().find("SOY UN " + chico + " DE " + universidad) != -1:
                cadena = cadena.upper().replace ("SOY UN " + chico + " DE " + universidad,"")
        for chica in SEXO_FEMENINO:
            if cadena.upper().find("SOY UNA " + chica + " DE " + universidad) !=-1:
                cadena = cadena.upper().replace ("SOY UNA " + chica + " DE " + universidad,"")
    for chico in SEXO_MASCULINO:
            if cadena.upper().find("SOY UN " + chico) != -1:
                cadena  = cadena.upper().replace ("SOY UN " + chico,"")
    for chica in SEXO_FEMENINO:
            if cadena.upper().find("SOY UNA " + chica) != -1:
                cadena = cadena.upper().replace ("SOY UN  " + chica,"")
    for estilo in ESTILO_PELO:
        if cadena.upper().find("PANTALON " + estilo) != -1:
            cadena = cadena.upper().replace ("PANTALON " + estilo,"")  
        if cadena.upper().find("CAMISETA " + estilo) != -1:
            cadena = cadena.upper().replace ("CAMISETA " + estilo,"")
        if cadena.upper().find("CAMISA " + estilo) != -1:
            cadena = cadena.upper().replace ("CAMISA " + estilo,"")                 
    return cadena.upper()
    
def encontrarSexo(cadena:str):
    for sexo in SEXO_FEMENINO:
        if cadena.find(sexo) != -1:
            return "MUJER"
    for sexo in SEXO_MASCULINO:
        if cadena.find(sexo) != -1:
            return "HOMBRE"
    return "NO ENCONTRADO"
def encontrarUniversidad(cadena:str):
    for universidad in UNIVERSIDADES:
        if cadena.find(universidad) != -1:
            return parserPolitecnica(universidad) #Por si es una de las asignaturas de la politecnica
    for uni in UNIVERSIDADES_COLOQUIAL:
        if cadena.find(uni) != -1:
            return parserPolitecnica(parserUniUniversidad(uni))
    return "NO ENCONTRADO"
def encontrarColorOjos(cadena:str):
    for color in COLORES:
        if cadena.find("OJOS "+color) != -1 or cadena.find("OJAZOS " + color) != -1:
            return color
    for color in COLOR:
        if cadena.find("OJOS DE COLOR "+color) != -1 or cadena.find("OJAZOS DE COLOR " + color) != -1:
            return color
    return "NO ENCONTRADO"
def encontrarColorPelo(cadena:str):
    if cadena.find("CHICO RUBIO") != -1: # A veces los denoniman "EL RUBIO"
        return "RUBIO"
    if cadena.find("CHICA RUBIA") != -1: # A veces los denoniman "EL RUBIO"
        return "RUBIO"
    if cadena.find("PELIRROJA") != -1 or cadena.find("PELIRROJO") != -1: # A veces los llaman así"
        return "PELIRROJO"
    for color in COLOR_PELO:
        if cadena.find("PELO "+color) != -1 or cadena.find("PELAZO " + color) != -1 or cadena.find("PELO DE COLOR "+ color) != -1 or cadena.find("PELAZO DE COLOR " + color) != -1:
            return color
    return "NO ENCONTRADO"
def encontrarAltura(cadena:str, sexo:str):
    if sexo == "HOMBRE":
        if cadena.find("MEDIANO") != -1 or cadena.find("NO MUY ALTO")!=-1: # Va primero, es m�s restrictivo con el no muy alto
            return "MEDIANO"
        if cadena.find("ALTO") != -1 or cadena.find("ALTITO")!=-1:
            return "ALTO"
        if cadena.find("BAJO") != -1 or cadena.find("BAJITO")!=-1:
            return "BAJO"
    elif sexo == "MUJER":
        if cadena.find("MEDIANA") != -1 or cadena.find("NO MUY ALTA")!=-1: # Va primero, es m�s restrictivo con el no muy alta
            return "MEDIANO"
        if cadena.find("ALTA") != -1 or cadena.find("ALTITA")!=-1:
            return "ALTO"
        if cadena.find("BAJA") != -1 or cadena.find("BAJITA")!=-1:
            return "BAJO"
    return "NO ENCONTRADO"
def encontrarBarba(cadena:str, sexo:str): 
    #Solo si sexo es Hombre, no creo que haya mujeres barbudas en la UAH, si las hay siento no contemplarlas. 
    if sexo == "HOMBRE":
        for barba in BARBA:
            if cadena.find(barba) != -1:
                return "BARBA"
    return "NO ENCONTRADO"
def encontrarEstiloPelo(cadena:str):
    for estilo in ESTILO_PELO:
        if cadena.find(estilo) != -1:
            return estilo
    return "NO ENCONTRADO"
if __name__ =='__main__':
    cadena = "Hola, soy un chico de biología que busca a una chica de teleco de ojos azules y de pelo casta�o"
    cargaInicialListasFemenino()
    cadena = remplazarTildes(cadena)
    cadena = limpiar(cadena)
    #print(cadena)
    #print(encontrarSexo(cadena))
    print(remplazarTildes(cadena))
    #print(encontrarSexo(cadena))
    print(encontrarUniversidad(cadena))
    print(encontrarColorOjos(cadena))
    print(encontrarColorPelo(cadena))