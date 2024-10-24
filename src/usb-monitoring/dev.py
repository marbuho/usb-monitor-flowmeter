import re
import serial
import time

'''#Exp regular caracteres que sean letras o numeros o puntos '.', al menos 4:
FORMAT_UNIDAD = r'^[a-zA-Z0-9.]{' + str(4) + r',}$'
#Exp regular 11 caracteres que sean numeros:
FORMAT_REMIT = r'^\d{11}'
#Exp regular tambo 5 caracteres que sean numeros:
FORMAT_TAMBO = r'^\d{5}'
#Exp regular litros 5 caracteres que sean numeros:
FORMAT_LITROS = r'^\d{5}'
#Exp regular temperatura dd.d caracteres que sean numeros:
FORMAT_TEMP=  r'^\d{2}\.\d{1}$'
#Exp regular cisterna al menos 1 caracter y que sean numeros:
FORMAT_CISTERNA=  r'^\d+$'
#Exp regular silo al menos 1 caracter y que sean numeros:
FORMAT_SILO=  r'^\d+$'
#Exp regular fecha que sean dd/mm/aa
FORMAT_FECHA = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{2}$'
#Exp regular hora que sean hh:mm
FORMAT_HORA = r'^([01][0-9]|2[0-3]):[0-5][0-9]$'
#valida que un campo cumple con una exp regular'''

'''def validate_pattern(exp_reg, data):
    pattern = re.compile(exp_reg)
    if pattern.fullmatch(data):
        return True
    else:
        return False'''

def parse_comma_delim_to_array(string):
    pattern = r'[^,]+'
    arr = re.findall(pattern, string)
    return arr

def clean_str_input(arr):
    remito = clean_point_from_numbers(arr[0])
    unidad = clean_point_from_str(arr[1])
    tambo = str(int(arr[2]) ) #limpia 0 a la izq y convierte en str 0002->2
    lts = str(int(arr[3]) ) #limpia 0 a la izq y convierte en str 00423->423
    temp = arr[4]
    cisterna = arr[5]
    fecha = arr[6]
    hora = arr[7]
    silo = clean_point_from_numbers(arr[8])
    line_clean = [remito, unidad, tambo, lts, temp, cisterna, fecha, hora, silo]
    
    return line_clean

#FORMATO: 9 campos <remmito>,<unidad>,<tambo>,<litros>,<temperatura>,<cisterna>,<fecha>,<hora>,<silo>
def validate_arr(arr, length):
    cond1 = len(arr)==length
    '''if not cond1: return False
    cond2 = validate_pattern(FORMAT_REMIT ,arr[0])
    if not cond2: return False
    cond3 = validate_pattern(FORMAT_UNIDAD,arr[1])
    if not cond3: return False
    print("paso los test")'''
    return True
    

# Eliminar puntos de la cadena
def clean_point_from_str(string):
    string_without_points = string.rstrip('.')
    string_clean = re.sub(r'[^a-zA-Z0-9]', '', string_without_points)
    return string_clean

# Eliminar puntos o carac extraños en una cadena de numeros '2yyy.*..->2'
def clean_point_from_numbers(string):
    string_without_points = string.rstrip('.')
    string_clean = re.sub(r'[^0-9]', '', string_without_points)
    return string_clean

def intercalate_delimiter(delimiter, *variables):
    variables_str = [str(var) for var in variables]
    result = delimiter.join(variables_str)
    return result
timeout=0.5
ser = serial.Serial('com4', timeout=timeout)
ser.reset_input_buffer() 
cont=15
while cont:
    
    print()
    print(f"Puerto , {ser.name}. listen.....") 
    print()
    x = ser.read(100) 
    print("se limpia el buffer") 
    ser.reset_input_buffer() 
    print(f"cumplido byte o timeout={timeout}, se leyo: {x}") 
    print() 
    string_data = x.decode('utf-8')  # converting to string
    input_array = parse_comma_delim_to_array(string_data)
    valid = len(input_array) == 9 and True or False 
    print("esperar 2 segundos") 
    if valid:
        string = clean_str_input(input_array)
        output = intercalate_delimiter(',', *string)
        print(f"OK->>>> dato limpiado:{output}")
        print() 
    else:
        print("ATENTION->>>el dato fue descartado")
        print() 
    time.sleep(2)
    print() 
    print("cumplido 2 segundos..se repite el loop") 
    cont-=1
ser.close()


#Datas de prueba "simula lo que suele enviar el plc"
#input_raw = ".................YYYYYYYYYY" # basura-> a descartar
#input_raw = "...........12345678900,empuje,00002,00096,13.2,1,20/09/24,19:20,2" # dato util-> limpiar
#input_raw = "           12345678900,empuje,00002,00096,13.2,1,20/09/24,19:20,2yyyyyyy       " # dato util-> limpiar
#input_raw = "12345678900,empuje,00002,00096,13.2,1,20/09/24,19:20,2yyyyyyy" # dato util-> limpiar
#input_raw = "12345678900,empuje,00002,00096,13.2,1,20/09/24,19:20,2" # dato util-> limpiar
