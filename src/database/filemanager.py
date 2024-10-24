
import utils



class ManagerBufferFileData:
    def __init__(self, filenameBuffer, fileNameBackup):
        self.name_buff = filenameBuffer
        self.name_backup = fileNameBackup
        

    def saveInBufferFile(self, arr):
        data = utils.intercalate_delimiter(',', *arr)
        with open(self.filenameBuffer, 'a') as file:
            file.write(data +'\n')
        
    def formatInBackup(self, arr):
        #array_clean = [remito, unidad, tambo, lts, temp, cisterna, fecha, hora, silo]
        remito = arr[0]
        unidad = arr[1]
        tambo = arr[2] 
        lts = arr[3]
        temp = arr[4]
        cisterna = arr[5]
        fecha = arr[6]
        hora = arr[7]
        silo = arr[8]
        equi = arr[9]
       # ouput_formated = f"{fecha} {hora}, Camion:unidad, Tambo:{lts}lit, Temp:{temp}Cº, Cisterna:{cisterna}, Silo:{silo}, Equipo:{equi} 

    def saveInBuckupFile(self, arr):
        data = self.formatInBackup(arr)
        with open(self.name_backup, 'a') as file:
            file.write(data + '\n')


data1 = "12345678900,empuje,00002,00096,13.2,1,20/09/24,19:20,2"

data2 = "12345678900,AFM3,00002,00096,13.2,1,20/09/24,19:20,2"

with open('archivo.txt', 'a') as file:
    file.write(data1 +'\n')

with open('archivo.txt', 'a') as file:
    file.write(data2 +'\n')


with open('archivo.txt', "r") as fp:
    # Moving the file handle to the end of the file
    fp.seek(0, 2)

    # getting the file handle position
    print('file handle at:', fp.tell())
    '''
    # writing new content
    fp.write("\nDemonstrating tell")

    # getting the file handle position
    print('file handle at:', fp.tell())

    # move to the beginning
    fp.seek(0)
    # getting the file handle position
    print('file handle at:', fp.tell())

    # read entire file
    print('***Printing File Content***')
    print(fp.read())
    print('***Done***')

    # getting the file handle position
    print('file handle at:', fp.tell())'''

