# coding=cp1252
# import pytesseract
# #pytesseract.tesseract_cmd = "C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"  # this should be done only once 
# print(pytesseract.image_to_string(Image.open('./tinder_uah/test.jpg'),lang="spa"))
# #print (image_to_string(Image.open('test-english.jpg'), lang='eng'))
import pickle
try:
    import Image
except ImportError:
    from PIL import Image
from os import listdir
import pytesser
import cv2
import write as wr
import parserData as p 
#By default language is eng, and page seg mode auto
#To give specifify parameters:

text = []
NLPText = []
parsed_txt=""
def parseTextos():
    for file in listdir("tinder_uah"):
        try:
            img = cv2.imread("tinder_uah/"+file)
            #img = Image.open("tinder_uah/"+file)
            if img is not None:
                txt = pytesser.image_to_string(img,"spa") #Analyse image as a spanish word
                parsed_txt = txt.encode('cp1252').decode('utf8')
                text.append(p.limpiar((parsed_txt.replace("\n"," ")).replace("  ","."))) # Hacemos el texto legible, lo limpiamos
        except (UnicodeDecodeError,UnicodeError) as e:
            print(str(e))
            print(file,"Descartado")
        continue    
#  print(txt.encode('cp1252').decode('utf8')) #Correcto
def guardarParser():
    with open("parserTexto","wb") as f:
        pickle.dump(text,f,pickle.HIGHEST_PROTOCOL)

def cargarParser():
    global text
    with open('parserTexto', 'rb') as f:
    # The protocol version used is detected automatically, so we do not
    # have to specify it.
        text = pickle.load(f)

def extraccion_datos():
    fila =1
    wr.iniciarWorkBook()
    array = [None] * 7
    for cadena in text:
        array[wr.SEXO] = p.encontrarSexo(cadena)
        array[wr.ALTURA] = p.encontrarAltura(cadena,array[wr.SEXO])
        array[wr.BARBA] = p.encontrarBarba(cadena,array[wr.SEXO])
        array[wr.COLOR_OJOS] = p.encontrarColorOjos(cadena)
        array[wr.COLOR_PELO] = p.encontrarColorPelo(cadena)
        array[wr.ESTILO_PELO] = p.encontrarEstiloPelo(cadena)
        array[wr.UNIVERSIDAD] = p.encontrarUniversidad(cadena)
        wr.imprimirFila(array,fila)
        fila += 1
    wr.guardar()
if __name__ == "__main__":
    p.cargaInicialListasFemenino()
    #parseTextos()
    #guardarParser()
    cargarParser()
    extraccion_datos()
