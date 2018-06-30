import xlwt
SEXO = 0
UNIVERSIDAD = SEXO  + 1 
COLOR_OJOS = UNIVERSIDAD + 1 
COLOR_PELO = COLOR_OJOS + 1 
ALTURA = COLOR_PELO + 1
BARBA = ALTURA + 1
ESTILO_PELO = BARBA + 1  

book = xlwt.Workbook()
sheet = book.add_sheet("Tinder")

#INICIALIZAMOS WORKBOOK
def iniciarWorkBook():    
    sheet.write(0,SEXO,"SEXO")
    sheet.write(0,UNIVERSIDAD,"UNIVERSIDAD")
    sheet.write(0,COLOR_OJOS,"COLOR_OJOS")
    sheet.write(0,COLOR_PELO,"COLOR_PELO")
    sheet.write(0,ALTURA,"ALTURA")
    sheet.write(0,BARBA,"BARBA")
    sheet.write(0,ESTILO_PELO,"ESTILO PELO")
def imprimirFila(array,fila):
    sheet.write(fila,SEXO,array[SEXO])
    sheet.write(fila,UNIVERSIDAD,array[UNIVERSIDAD])
    sheet.write(fila,COLOR_OJOS,array[COLOR_OJOS])
    sheet.write(fila,COLOR_PELO,array[COLOR_PELO])
    sheet.write(fila,ALTURA,array[ALTURA])
    sheet.write(fila,BARBA,array[BARBA])
    sheet.write(fila,ESTILO_PELO,array[ESTILO_PELO])
def guardar():
    book.save("foobar.xls")

def imprimirInforme(frecuenciaHombre,frecuenciaMujer,arrayUniversidad,arrayColorOjos,arrayColorPelo,arrayBarba,arrayAltura,arrayEstiloPelo):
    informeBook = xlwt.Workbook()
    informe = informeBook.add_sheet("Informe")
    sheet.write(0,0,"FRECUENCIA HOMBRE")
    sheet.write(0,1,"FRECUENCIA MUJER")
    offset = 2 
    for i in range(0,arrayUniversidad.size):
        informe.write(0,i + offset,"FRECUENCIA UNIVERSIDAD" + arrayUniversidad.index[i] )
        informe.write(1,i + offset,arrayUniversidad[i].item())
    offset = offset + arrayUniversidad.size 
    for i in range(0,arrayColorOjos.size):
        informe.write(0,i+offset,"FRECUENCIA OJOS" + arrayColorOjos.index[i] )
        informe.write(1,i + offset,arrayColorOjos[i].item())
    offset = offset + arrayColorOjos.size
    for i in range(0,arrayColorPelo.size):
        informe.write(0,i+offset,"FRECUENCIA PELO " + arrayColorPelo.index[i] )
        informe.write(1,i + offset,arrayColorPelo[i].item())
    offset = offset + arrayColorPelo.size
    for i in range(0,arrayAltura.size):
        informe.write(0,i+ offset,"FRECUENCIA ALTURA" + arrayAltura.index[i] )
        informe.write(1,i + offset,arrayAltura[i].item())
    offset = offset + arrayAltura.size
    for i in range(0,arrayBarba.size):
        informe.write(0,i+ offset,"FRECUENCIA Barba" + arrayBarba.index[i] )
        informe.write(1,i + offset,arrayBarba[i].item())
    offset = offset + arrayBarba.size
    for i in range(0,arrayEstiloPelo.size):
        informe.write(0,i+ offset,"FRECUENCIA Barba" + arrayEstiloPelo.index[i] )
        informe.write(1,i + offset,arrayEstiloPelo[i].item())
    informeBook.save("InformeWorkBook.xls") 

    
