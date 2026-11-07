from queue import Queue as Cola
'''
  =========================================
  EJERCICIO 1
  =========================================
'''
def stock_productos(stock_cambios:list[tuple[str,int]])->dict[str,tuple[int,int]]:
    res:dict[str,tuple[int,int]]={}
    actual:tuple[int,int]
    for (nombre,cantidad) in stock_cambios:
        if nombre not in res.keys():
            res[nombre]=(cantidad,cantidad)
        else:
            actual=res[nombre]
            actual=compararTupla(actual,cantidad)
            res[nombre]=actual
    return res
'''
  =========================================
  EJERCICIO 2
  =========================================
'''
def compararTupla(actual:tuple[int,int],nuevo:int)->tuple[int,int]:
    max:int
    min:int
    if (nuevo>actual[1]):
        max=nuevo
    else:
        max=actual[1]
    if(nuevo<actual[0]):
        min=nuevo
    else:
        min=actual[0]
    res:tuple[int,int]=(min,max)
    return res

def es_primo(n:int)->bool:
    res:bool=True
    if(n==1 or n==0):
        res=False
    for d in range(2,n):
        if(n%d==0):
            res=False
    return res

def filtrar_codigos_primos(codigos_barra:list[int])->list[int]:
    res:list[int]=[]
    for codigo in codigos_barra:
        if es_primo(codigo%1000):
            res.append(codigo)
    return res
'''
  =========================================
  EJERCICIO 3
  =========================================
'''
def secuencia_mas_larga(tipos_pacientes_atendidos:list[str])->int:
    contador_actual:int=0
    contador_res:int=0

    res:int=0
    for k in range(len(tipos_pacientes_atendidos)):
        i:int=k
        while(i<len(tipos_pacientes_atendidos) and (tipos_pacientes_atendidos[i]=="gato" or tipos_pacientes_atendidos[i]=="perro")):
            contador_actual+=1
            i+=1
        if contador_res<contador_actual:
            res=k
            contador_res=contador_actual
        contador_actual=0
    return res
'''
  =========================================
  EJERCICIO 4
  =========================================
'''
def un_responsable_por_turno(grilla_horaria:list[list[str]])->list[tuple[bool,bool]]:
    res:list[tuple[bool,bool]]=[]
    dias:list[str]
    for i in range(len(grilla_horaria[0])):
        dias=i_esima_columna(i,grilla_horaria)
        res.append((primeros4iguales(dias),ultimos4iguales(dias)))
    return res

def i_esima_columna(i:int,matriz:list[list[str]])->list[str]:
    res:list[str]=[]
    for fila in matriz:
        res.append(fila[i])
    return res

def primeros4iguales(lista:list[str])->bool:
    return(lista[0]==lista[1]==lista[2]==lista[3])

def ultimos4iguales(lista:list[str])->bool:
    return(lista[4]==lista[5]==lista[6]==lista[7])
'''
  =========================================
  EJERCICIO 5
  =========================================
'''
def promedio_de_salidas(registro:dict[str,list[int]])->dict[str,tuple[int,float]]:
    res:dict[str,tuple[int,float]]={}
    for amigo in registro.keys():
        res[amigo]=promedio_de_uno(registro[amigo])
    return res


def promedio_de_uno(lista:list[int])->tuple[int,float]:
    res:tuple[int,float]
    suma:int=0
    contador:int=0
    for num in lista:
        if num!=0 and num!=61:
            suma+=num
            contador+=1
    if contador==0:
        res=(0,0.0)
    else:
        res=(contador,suma/contador)
    return res
'''
  =========================================
  EJERCICIO 6
  =========================================
'''
def tiempo_mas_rapido(tiempos_salas:list[int])->int:
    indice_actual:int
    tiempo_actual:int=tiempos_salas[0]
    for i in range(len(tiempos_salas)-1):
        if tiempos_salas[i]<tiempo_actual and tiempos_salas[i]!=0:
            indice_actual=i
            tiempo_actual=tiempos_salas[i]
    if tiempo_actual>tiempos_salas[len(tiempos_salas)-1] and tiempos_salas[len(tiempos_salas)-1]!=0:
        indice_actual=len(tiempos_salas)-1
    return indice_actual
'''
  =========================================
  EJERCICIO 7
  =========================================
'''
def racha_mas_larga(tiempos:list[int])->tuple[int,int]:
    res:tuple[int,int]=(0,0)
    tupla_aux:tuple[int,int]
    indice_auxiliar:int
    for i in range(len(tiempos)):
        indice_auxiliar=i
        while (indice_auxiliar<=len(tiempos)-1) and 61>tiempos[indice_auxiliar]>0:
            indice_auxiliar+=1
        tupla_aux=(i,indice_auxiliar)
        if (res[1]-res[0]<indice_auxiliar-i):
            res=tupla_aux
    return res
'''
  =========================================
  EJERCICIO 8
  =========================================
'''
def escape_solitario(amigos_por_salas:list[list[int]])->list[int]:
    res:list[int]=[]
    for i in range(len(amigos_por_salas)):
        if fue3solo(amigos_por_salas[i]):
            res.append(i)
    return res


def fue3solo(lista:list[int])->bool:
    return(lista[0]==0 and lista[1]==0 and lista[2]!=0 and lista[3]==0)
'''
  =========================================
  EJERCICIO 9
  =========================================
'''
def torneo_de_gallinas(estrategias:dict[str,str])->dict[str,int]:
    res:dict[str,int]={}
    puntaje_jugador_actual:int=0
    for jugador in estrategias.keys():
        for jugador2 in estrategias.keys():
            if jugador!=jugador2:
                puntaje_jugador_actual=puntaje_jugador_actual+calculoPuntaje(estrategias[jugador],estrategias[jugador2])
        res[jugador]=puntaje_jugador_actual
        puntaje_jugador_actual=0
    return res


def calculoPuntaje(estrategia_a_calcular:str,estrategia_oponente:str)->int:
    puntaje:int
    if estrategia_a_calcular=="me desvio siempre" and estrategia_oponente=="me desvio siempre":
        puntaje=-10
    elif(estrategia_a_calcular=="me desvio siempre" and estrategia_oponente=="me la banco y no me desvio"):
        puntaje=-15
    elif(estrategia_oponente=="me desvio siempre" and estrategia_a_calcular=="me la banco y no me desvio"):
        puntaje=10
    elif(estrategia_a_calcular=="me la banco y no me desvio" and estrategia_oponente=="me la banco y no me desvio"):
        puntaje=-5
    return puntaje
'''
  =========================================
  EJERCICIO 10
  =========================================
'''
def reordenar_cola_priorizando_vips(filaClientes:Cola[tuple[str,str]])->Cola[str]:
    filaClientes_aux:Cola[tuple[str,str]]=Cola()
    res:Cola[str]=Cola()
    vips:Cola[str]=Cola()
    normales:Cola[str]=Cola()
    cliente:tuple[str,str]
    while not filaClientes.empty:
        cliente=filaClientes.get()
        filaClientes_aux.put(cliente)
        if cliente[1]=="vip":
            vips.put(cliente[0])
        else:
            normales.put(cliente[0])
    while not filaClientes_aux.empty():
        filaClientes.put(filaClientes_aux.get())
    while not vips.empty():
        res.put(vips.get())
    while not normales.empty():
        res.put(normales.get())
    return res
'''
  =========================================
  EJERCICIO 11
  =========================================
'''
def eliminar_primera_letra(palabra:str)->str:
    res:str=""
    for i in range(len(palabra)-1):
        res=res+palabra[i+1]
    return res

def cuantos_sufijos_son_palindromos(texto:str)->int:
    contador_sufijos_palindromos:int=0
    palabra:str=texto
    for i in range(len(palabra)):
        if esPalindromo(palabra)and palabra!="":
            contador_sufijos_palindromos+=1
        palabra=eliminar_primera_letra(palabra)
    return contador_sufijos_palindromos

def esPalindromo(palabra:str)->bool:
    palabra_reves:str=""
    for letra in palabra:
        palabra_reves=letra+palabra_reves
    return palabra_reves==palabra

'''
  =========================================
  EJERCICIO 12
  =========================================
''' 
def quien_gano_el_tateti_facilito(tablero:list[list[str]])->int:
    res:int
    if ganoJugador(tablero,"X"):
        res=1
    elif ganoJugador(tablero,"O"):
        res=2
    else:
        res=0
    if ganoJugador(tablero,"X") and ganoJugador(tablero,"O"):
        res=3
    return res


def ganoJugador(tablero:list[list[str]],jugador:str)->bool:
    res:bool=False
    for i in range(len(tablero)):
        columna:list[str]=i_esima_columna2(tablero,i)
        for j in range(len(columna)-2):
            if(columna[j]==columna[j+1]==columna[j+2]==jugador):
                res=True
    return res

def i_esima_columna2(tablero:list[list[str]],i:int)->list[str]:
    res:list[str]=[]
    for fila in tablero:
        res.append(fila[i])
    return res
'''
  =========================================
  EJERCICIO 13
  =========================================
''' 

def orden_de_atencion(urgentes:Cola[int],postergables:Cola[int])->Cola[int]:
    urgentes_aux:Cola[int]=Cola()
    cliente_urgente:int
    cliente_postergable:int
    res:Cola[int]=Cola()
    postergables_aux:Cola[int]=Cola()
    while not urgentes.empty() or not postergables.empty():
        cliente_urgente=urgentes.get()
        cliente_postergable=postergables.get()
        urgentes_aux.put(cliente_urgente)
        postergables_aux.put(cliente_postergable)
        res.put(cliente_urgente)
        res.put(cliente_postergable)
    while not urgentes_aux.empty():
        urgentes.put(urgentes_aux.get())

    while not postergables_aux.empty():
        postergables.put(postergables_aux.get())
    return res
'''
  =========================================
  EJERCICIO 14
  =========================================
''' 
def alarma_epidemiologica(registros:list[tuple[int,str]],infecciosas:list[str],umbral:float)->dict[str,float]:
    contador_actual:int=0
    res:dict[str,float]={}
    porcentaje_actual:float
    total_pacientes:int=len(registros)
    for enfermedad in infecciosas:
        for i in range(len(registros)):
            if enfermedad==registros[i][1]:
                contador_actual+=1
        if contador_actual!=0:
            porcentaje_actual=contador_actual/total_pacientes
        if porcentaje_actual>=umbral:
            res[enfermedad]=porcentaje_actual
        porcentaje_actual=0.0
        contador_actual=0
    return res
'''
  =========================================
  EJERCICIO 15
  =========================================
''' 

def sumarTodos(lista:list[int])->int:
    res:int=0
    for i in lista:
        res+=i
    return res
def empleado_del_mes(horas:dict[int,list[int]])->list[int]:
    res:list[int]=[]
    if len(horas.keys())!=0:
        hora_buscada:int=mayorCantidadDeHoras(horas)
        for empleado in horas.keys():
            if(sumarTodos(horas[empleado])==hora_buscada):
                res.append(empleado)
    return res
def mayorCantidadDeHoras(horas:dict[int,list[int]])->int:
    max_actaul:int=0
    max_historico:int=sumarTodos(horas[list(horas.keys())[0]])
    for empleado in horas.keys():
        max_actaul=sumarTodos(horas[empleado])
        if max_actaul>max_historico:
            max_historico=max_actaul
    return max_historico
'''
  =========================================
  EJERCICIO 16
  =========================================
''' 
def promedioPiso(piso:list[bool])->float:
    ocupadas:int=0
    for cama in piso:
        if (cama):
            ocupadas+=1
    return(ocupadas/len(piso))

def nivel_de_ocupacion(camas_por_piso:list[list[bool]])->list[float]:
    res:list[float]=[]
    for piso in camas_por_piso:
        res.append(promedioPiso(piso))
    return res