import threading
import serial
import time

def leer_puerto_serial(puerto, baudrate, nombre):
    ser = serial.Serial(puerto, baudrate)
    while True:
        '''if ser.in_waiting > 0:
            datos = ser.readline().decode('utf-8').rstrip()
            print(f"{nombre} recibió: {datos}")'''
        print(f"Puerto , {ser.name}. listen.....\n") 
        x = ser.read(100) 
        ser.reset_input_buffer() 

        print(f"cumplido byte o timeout={timeout}, se leyo: {x}\n") 
        string_data = x.decode('utf-8')  # converting to strings
        
        input_array = parse_comma_delim_to_array(string_data)
        valid = len(input_array) == 9 and True or False 
        print("esperar 2 segundos...\n") 
        if valid:
            array_clean = clean_str_input(input_array)
            #array_clean.append(2) ->sera funcion del puerto o sino hay letras es el 1
            #manFile.saveData(output/input_array)
            output_cnsole = intercalate_delimiter(',', *array_clean)
            #
            print(f"OK->>>> dato limpiado:{output}\n")
            #manFile.saveData(output/input_array)
        else:
            print("ATENTION->>>el dato fue descartado\n")
        time.sleep(2)
        print("cumplido 2 segundos..se repite el loop\n") 


if __name__ == "__main__":
    # Configuraciones de los puertos seriales
    puerto1 = 'COM1'  # Cambia 'COM1' por el nombre real del puerto serial
    puerto2 = 'COM2'  # Cambia 'COM2' por el nombre real del puerto serial
    baudrate = 9600

    # Creación de los hilos
    hilo1 = threading.Thread(target=leer_puerto_serial, args=(puerto1, baudrate, "Hilo1"))
    hilo2 = threading.Thread(target=leer_puerto_serial, args=(puerto2, baudrate, "Hilo2"))

    # Iniciar los hilos
    hilo1.start()
    hilo2.start()

    # esperar hasta que los hilos finalizen .Es para mantener el programa principal activo
    hilo1.join()
    hilo2.join()

''' #otra forma
    ports  = ['com3', 'com5']
    threads = [] #lista con los hilos 

    #inicar un hilo para cada puerto:
    for port in ports:
        thread = threading.Thread(target=leer_puerto_serial, args=(port, baudrate, f"Hilo del puerto {port}"))
        thread.start()
        threads.append(thread) #agregar a la lista de hilos activos.

    # asegurar que el prog prin espera a que todos los hilos terminen antes de finalizar.
    for tread in threads:
        thread.join()
'''