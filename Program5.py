from msvcrt import getch
import sys
import serial
import io
import random 
import time
import threading
import keyboard

# variables inicio globales
ver_valores = 1     # flag para imprimir valores para debug
alfa_num = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
mng_puerto_entrada = 0  #manejador del puerto de entrada
mng_puerto_salida =  0  #manejador del puerto de salida
str_id_PC = '' # string con el id de la PC
num_jugadores = 0 # numero de jugadores conectados (0-x) serian x+1 jugadores
str_PC_maestro = '' # string del serial de la PC maestro
seriales_jugadores = [] # list de seriales de todas las PC conectadas
#
# variables fin

# Funciones

def buscar_Puertos_Seriales(): 
    # Funcion buscar_Puertos_Seriales Busca los poertos seriales fisicos en la PC (No necesariamente estan disponibles)
    # Parametros: sin parametros
    # Retorna: list ser_puertos [enteros con los puertos disponibles, string xx de puertos disponibles, manejadores sin inicializar del puerto]
    ports = ['COM%s' % (i + 1) for i in range(100)]
    puertos_com = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            puertos_com.append(port)
        except (OSError, serial.SerialException):
            pass
    # puertos_com=sorted(x[0] for x in comports()) # funcion de serial que retorna las compuertas seriales existentes en la PC
    #if ver_valores: print (puertos_com)
    est_puerto = []    # estructura del puerto serial individual
                        # contiene puerto X, COMX, 0 = int, string, manejador de puerto
    ser_puertos = []    # estructura con todos los puertos seriales disponibles est_puertos
    int_puertos_fisicos = len(puertos_com) # cantidad de puertos fisicos
    for p in range(0, int_puertos_fisicos):
        if(len(puertos_com[p])==5):   # si es un puerto COM >9 (tiene 5 caracteres) y asumiendo que no hay puertos COM >99
            int_dec=int(puertos_com[p][3])  # 1er caracter decena
            int_uni=int(puertos_com[p][4])  # 2nd caracter unidad
        else:
            int_dec=0                       # 1er caracter decena
            int_uni=int(puertos_com[p][3])  # 2nd caracter unidad
        str_puerto = "COM"+str(int_dec*10+int_uni) # cadena con el nombre del puerto
        try:    # intenta abrir el puerto esperando error o exito
            # abre el puerto para ver si esta disponible
            ser = serial.Serial(str_puerto, 9600, 8, timeout=1)
            ser.close() # se pudo abrir, se cierra el puerto
            est_puerto.append(int_dec*10+int_uni)      # agrega al vector de enteros el valor de com detectado X
            est_puerto.append(str_puerto)              # agrega al vector de string el valor de com detectado COMX
            est_puerto.append(0)                       # agrega manejador del puerto en 0
            #if ver_valores:print(str(int_dec*10+int_uni)+ " " + puertos_com[p])
            ser_puertos.append(est_puerto)            # agrega la informacion del puerto a la lista de puertos
        except serial.SerialException: # no se pudo abrir el puerto
            # if ver_valores:print(str_puerto+ " No disponible")
            pass
        est_puerto = [] # vacia el vector
    return ser_puertos # retorna la lista de puertos disponibles

def seleccionar_Puerto(puertos, accion):
    # Funcion seleccionar_Puerto
    # Parametros: list puertos,  string accion
    #             lista con los puertos disponibles, string con la accion a mostrar
    # Retorna: int_puertos puerto seleccionado (1 ...99) 0 para no seleccion
    sel=0 # bandera para el while
    int_puertos_disponibles = len(puertos) # cantidad de puertos disponibles
    while(sel==0):
        print("Escoja un puerto para " + accion)
        print(" 0 para cancelar")
        for p in range(0, int_puertos_disponibles):
            if(p>9):
                espacio=""
            else:
                espacio=" "
            print(espacio+str(int(p+1))+ " COM"+str(puertos[p][0]))
        puerto_sel=input("Su eleccion: ")
        try:
            puerto_sel=int(puerto_sel)
            if(puerto_sel==0):
                return 0
            if(puerto_sel <= int_puertos_disponibles):
                    sel=1    
                    continue
            else:
                print("Eleccion invalida " + str(puerto_sel))
                continue
        except ValueError:
            print("Eleccion invalida " + str(puerto_sel))
            continue
    # while end
    return puerto_sel
    
def configurar_Puertos_PC(lst_puertos_fisicos):
    # Funcion configurar_Puertos_PC
    # Parametros: lst_puertos_fisicos = listado de puertos fisicos
    # Retorna: list configPuertosPC [ent 1, sal 1] [ent 2, sal 2]
    lst_puertos=[]
    lst_puertos.append(seleccionar_Puerto(lst_puertos_fisicos, "entrada")-1) # entero del puerto de entrada X
    lst_puertos.append(seleccionar_Puerto(lst_puertos_fisicos, "salida")-1)  # entero del puerto de salida Y
    return lst_puertos

def serial_Write(str_data):
    # Funcion serial_Write
    # Parametros: data a esribir
    # Retorna: int data numero de bytes escritos
    # time.sleep(2)
    data = mng_puerto_salida.write(bytes(str_data.encode()))
    return data

def serial_Write_con_Respuesta(str_data):
    # Funcion serial_Write_Respuesta
    # Parametros: data a esribir
    # Retorna: serial de PC destino, nensaje a enviar, data completa leida formato decode
    # time.sleep(2)
    data = mng_puerto_salida.write(bytes(str_data.encode()))
    str_data_entrada = ''
    while(str_data_entrada==''):
        str_serial, str_mensaje, str_data_entrada = serial_Readline()
    return str_serial, str_mensaje, str_data_entrada  

def serial_Read(bytes_a_leer):
    # Funcion serial_Read
    # Parametros: bytes_a_leer (numero de bytes a leer)
    # Retorna: data leida formato decode
    data = mng_puerto_entrada.read(bytes_a_leer).decode()
    return data

def serial_Readline(): 
    # Funcion serial_Readline
    # Parametros:
    # Retorna: serial de PC destino, nensaje a enviar, data completa leida formato decode
    data = mng_puerto_entrada.readline().decode() 
    serial = data[0:10]
    mensaje = data[10:len(data)-1]
    return serial, mensaje, data

def busqueda_equipos_conectados(): 
    # busqueda_equipos_conectados
    # Parametros: 
    # Retorna: numeros de equipos conectados y seriales de equipos
    num_PC = 0
    listo=False
    str_serial = [] # crea lista de PC (Esta 1, la 2 es la anterior en el anilli y asi
    str_serial.append(str_id_PC) # agrega en la primera posicion la id de esta PC
    num_datos_escritos = serial_Write(str_id_PC) # envia este id ala PC siguiente
    # print("Enviando: "+ str_id_PC)
    # p = len(str_id_PC)
    
    print("Esperando conexion de otros equipos")
    while(not listo): # bucle para concatenar todas las PC del anillo
        str_data_entrada = ''
        while(str_data_entrada == ''): # espera por un id nuevo que se envie de la PC anterior
            str_data_entrada = serial_Read(10)
        # print("Recibiendo: "+ str_data_entrada)
        if (str_data_entrada == str_id_PC): # listo, dio la vuelta el serial de esta PC
                listo = True
        else:
            num_PC += 1
            str_serial.append(str_data_entrada) # agrega en la primera posicion la id de esta PC
            num_datos_escritos = serial_Write(str_data_entrada)
        #    print("Enviando: "+ str_data_entrada)
    # fin while        
    
    # voltea el vector de seriales para mas facil manejo
    # PC(actual), PC(Siguiente, que recibe de Maestro), ...PC Ultimo(Su siguiente es el Maestro)
    id_sentido_salida = [str_serial[0]]
    for p in range(num_PC,0,-1):
        id_sentido_salida.append(str_serial[p])
    return(num_PC, id_sentido_salida)

def iniciar_partida(solicitar_inicio_partida, name):
    # iniciar_partida (usa hilo)
    # Parametros: solicitar_inicio_partida [], name = nombre del thread
    # Retorna: nada
    print("Presione ("+solicitar_inicio_partida[0]+") para ser Maestro e iniciar partida\n")
    print("Si va a ser Esclavo solo espere")
    tecla = solicitar_inicio_partida[0]
    seguir_hilo = True
    while(seguir_hilo):
        if keyboard.is_pressed(tecla) == True:
            getch()
            seguir_hilo = False
            solicitar_inicio_partida[1] = 's'
        elif solicitar_inicio_partida[1] == 's':
            seguir_hilo = False
    return

def iniciar_partida_manual(): 
    # Inicia partida manual. 
    # Parametros: 
    # Retorna: id de la PC maestra
    solicitar_inicio_partida = []
    solicitar_inicio_partida.append(str_id_PC[0])
    solicitar_inicio_partida.append('')
        
    hilo_solicitar = threading.Thread(target = iniciar_partida, args =(solicitar_inicio_partida, 'thread_inicio'))
    print("Esperando que alguien inicie partida")
    hilo_solicitar.start()
        
    str_data_entrada=''
    
    # num_datos_escritos = serial_Write(mng_puerto_salida, str_data_salida)
    while(str_data_entrada==''):
        str_data_entrada = serial_Read(10)
        if(solicitar_inicio_partida[1]=='s'): #esta PC solicito un inicio de partida
            print("Esta PC solicito inicio de partida")
            str_data_entrada=str_id_PC
    solicitar_inicio_partida[1] = 's' # para que el hilo termine
    # manda info de master a la siguiente PC
    num_datos_escritos = serial_Write(str_data_entrada)
        
    # si esta es la PC que solicito ser master, va a recibir la cadena que envio de regreso por el anillo
    if str_data_entrada==str_id_PC:    # espera a que el mensaje llegue
        str_data_entrada=''  
        while(str_data_entrada==''):
            str_data_entrada = serial_Read(10)
        
    return (str_data_entrada)

def liberar_Esclavas():
    # liberar_Esclavas
    # Parametros: 
    # Retorna: nada
    for p in range(num_jugadores, -1,-1):
        num_datos_escritos = serial_Write(seriales_jugadores[p]+'\n')
        # no espera respuesta porque el anillo se rompe
        print(f"{seriales_jugadores[p]} PC {p} Termino")

    return
# Inicio de programa

# ser = serial.Serial("COM1", 9600, 8, timeout=1) para ocupar cualquier com 

# genera ID de la PC de 10 caracteres a partir de la variable alfa_num, declarada al comienzo,
# podemos considerarla unica ya que la probabilidad que se repita en 2, 3 ....o N ocasiones es muy baja
str_id_PC = ""
for p in range(0,10):
    str_id_PC = str_id_PC + str(alfa_num[random.randint(0, len(alfa_num)-1)]) 

# identifica los puertos seriales de la PC, devuelve lista con [X, "COMX", manejador del puerto=0], desecha los que estan abiertos
lst_puertos_fisicos = buscar_Puertos_Seriales() # solo son los puertos disponibles para usar

# str_nombre_PC = input("Nombre de la PC: ")
str_nombre_PC = "Perico de los Palotes"

# lst_puertos_PC = lista de [COM entrada, COM salida] de la PC
lst_puertos_PC = configurar_Puertos_PC(lst_puertos_fisicos)

# estos mng_puerto_xxxx solo tienen el manejador de puerto del COM de entrada, salida de la PC
mng_puerto_entrada = serial.Serial(lst_puertos_fisicos[lst_puertos_PC[0]][1], 9600, 8, timeout=1)
if(lst_puertos_PC[0] ==lst_puertos_PC[1]):
    mng_puerto_salida = mng_puerto_entrada  # si es el mismo puerto de entrada y salida
else:    
    mng_puerto_salida = serial.Serial(lst_puertos_fisicos[lst_puertos_PC[1]][1], 9600, 8, timeout=1)

print(f"Recibiendo por: " + mng_puerto_entrada.name + " Enviando por: "+ mng_puerto_salida.name)

# busca conexiones hasta recibir respuesta, cerrandose el anillo serial
print("Asegurese de que todas la PCs estan encendidas y\ndebidamente conectados sus cables seriales.")
print("Yo puedo conectarlas, pero no puedo hacer magia.")
print("El numero de jugadores a conectarse es ilimitado (Minimo 2).")
print("Presione una tecla para buscar jugadores")
getch()

num_jugadores, seriales_jugadores = busqueda_equipos_conectados() #str_id_PC, mng_puerto_entrada, mng_puerto_salida)
print(f"Numero de jugadores encontrados: {num_jugadores+1}")
print(f"Serial de esta PC: {str_id_PC}")
print("Seriales de PCs Conectadas:")
print(seriales_jugadores)

# espera por inicio de partida por alguno de los jugadores
# busca quien empezara la partida para personalizarla,
# por lo tanto sera el maestro y las demas esclavas
str_PC_maestro = iniciar_partida_manual()

# establece flag maestro = 1 o 0 para esta PC
print("PC Maestro: " + str_PC_maestro)
if(str_PC_maestro==str_id_PC): # esta es la PC maestro
    print("Esta PC es Maestro.")
    maestro=1
else:                        # esta PC es esclavo
    maestro=0
    print("Esta PC es Esclava.")
    
print(seriales_jugadores)


# a partir de aqui el programa se bifurca en si es maestro o es esclavo
# las funciones que se usan son:
# num_data_escrita = serial_Write("cadena") para enviar a la siguiente PC
# cadena debe empezar con el serial de 10 caracteres de la PC a recibir y terminar con '\n'
# la longitud de la data entre el serial y '\n' puede ser variable, si en vacio terminan todos
# num_data_escrita es el numero de caracteres escrito si acaso se necesita
#
# cadena = serial_Readline() para leer una cadena de la PC anterior en el anillo
# cadena contiene toda la cadena leida, comenzando con el serial de la PC que recibe
# el mensaje, la data a procesar por la PC destino y termina con '\n'
#
# esta parte es solo para ver el funcionamiento, no tiene que estar en en programa
#
# # las variables necesarias para funcionar son las siguientes
# mng_puerto_entrada = 0  #manejador del puerto de entrada
# mng_puerto_salida =  0  #manejador del puerto de salida
# str_id_PC = '' # string con el id de la PC
# num_jugadores = 0 # numero de jugadores conectados (0-x) serian x+1 jugadores
# str_PC_maestro = '' # string del serial de la PC maestro
# seriales_jugadores = [] # list de seriales de todas las PC conectadas

#
#

if(maestro==1):    # programa maestro" 
    # soy la PC 0
    PC_destino=1
    while(PC_destino):    
        print("PC Maestro: " + str_id_PC + " PC 1")
        print("PC Esclavas disponibles (Sentido Conexion de Salida):")
        for p in range(1,num_jugadores+1):
            print(f"{p} {seriales_jugadores[p]} PC {p+1}")
        PC_destino=int(input("A cual PC quiere mandarle un mensaje (0 para terminar)?: "))
        if(PC_destino==0):
            break
        data_a_enviar=input("Mensaje a enviar: ")

        str_completo=seriales_jugadores[PC_destino] + data_a_enviar+'\n'
        # Enviando datos a PC siguiente PC
        # y espera obligado respuesta del esclavo, podria venir con data extra de otros PCs (no implementado)
        str_serial, str_mensaje, str_data_entrada = serial_Write_con_Respuesta(str_completo)
        print("Recibiendo de: " + str_serial)
        print("Mensaje: " + str_mensaje)
    # while end
    # se termino el envio de datos 
    # enviar mensaje a todas las PCs para que se  desconecten
    liberar_Esclavas()
    
else:              # programa esclavo"
    print("PC Esclava " + str_id_PC)
    seguir = True
    while(seguir):
        str_data_entrada = ''
        while(str_data_entrada==''):
            str_serial, str_mensaje, str_data_entrada = serial_Readline()
        # print("Recibiendo :"+str_data_entrada)
        # lee encabezado para saber para que PC es el mensaje
        if(str_serial == str_id_PC): # es data para esta PC
            # print("Es para esta PC")
            if(len(str_mensaje)==0): # no hay data en el mensaje, aunque podria ser una accion para terminar
                seguir = False  # para terminar, no envia respuesta
            else:
                # envia respuesta al Maestro
                str_data_salida = str_serial + "Recibido: " + str_mensaje + " Gracias\n"
                num_datos_escritos = serial_Write(str_data_salida) # no espera respuesta
            print("El mensaje es " + str_mensaje)
            
        else:   # no es data para esta PC
            # print("No es data para esta PC")
            # envia la misma data para que llegue a la PC destino
            num_datos_escritos = serial_Write(str_data_entrada)
            # print("Enviando a la siguiente PC :\n"+ str_data_entrada)
    # while end


#cierra los puertos
mng_puerto_salida.close()
mng_puerto_entrada.close()
print("Presione una tecla para finalizar el programa")
getch()
exit(0)