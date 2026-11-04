from typing import TextIO
#para correr los test hago, python3 test.py en la carpeta con ambos archivos
def calcular_promedio_por_estudiante (notas:list[ tuple[str,float]])->dict[str,float]:
    aux: dict[str,list[float]]={}
    for (alumno, nota) in notas:
        if alumno not in aux.keys():
            aux[alumno]=[]
        aux[alumno].append(nota)
    res:dict[str,list[float]]={}
    for (alumno,lista_notas) in aux.items():
        largo:int=len(lista_notas)
        suma_notas:float=0.0
        for nota in lista_notas:
            suma_notas+=nota
        res[alumno]=suma_notas/largo
    return res
            
def contar_lineas (nombre_archivo:str)->int:
    archivo_contenido:TextIO = open(nombre_archivo, 'r')
    lista:list[str]=archivo_contenido.readlines()
    res:int=len(lista)
    nombre_archivo.close()
    return (res)
# print(contar_lineas("nombre del path"))
def clonar_sin_comentarios(nombre_archivo_entrada:str,nombre_archivo_salida:str):
    archivo_de_entrada:TextIO=open(nombre_archivo_entrada, 'r')
    lista:list[str]=archivo_de_entrada.readlines()
    archivo_de_entrada.close()
    archivo_salida:TextIO=open(nombre_archivo_salida,'w')
    for linea in lista:
        a:int=0
        if linea[a]!='#':
            while linea[a] == ' ':
                a+=1
            if linea[a]!='#':
                archivo_salida.write(linea)
    archivo_salida.close()

def agrupar_por_longitud(nombre_archivo:list[str])->dict[int,int]:
    res:dict[int,int]={}
    archivo_de_entrada:TextIO=open(nombre_archivo,'r')
    lista:list[str]=archivo_de_entrada.readlines()
    archivo_de_entrada.close()
    todasPalabras:list[str]=unirTodas(lista)
    for palabra in todasPalabras:
        num:int=contarYeliminar(len(palabra),todasPalabras)
        if len(palabra) not in res.keys():
            res[len(palabra)]=num
    return res

def unirTodas(lista:list[str])->list[str]:
    res:list[str]=[]
    palabra:str=""
    for linea in lista:
        for caracter in linea:
            if caracter!=' ':
                palabra+=caracter
            else:
                res.append(palabra)
                palabra=""
    return res

def contarYeliminar(n:int,lista:list[str])->int:
    res:int=0
    for palabra in lista:
        if len(palabra)==n:
            res+=1
            lista.remove(palabra)
#este esta medio mal leer bien el codigo del campus