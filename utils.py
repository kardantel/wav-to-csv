import warnings
import pandas as pd
import numpy as np
import librosa
warnings.filterwarnings('ignore')


class Utils:
    '''
    Class that contains auxiliar methods used.
    '''
    @classmethod
    def wav2csv(cls, audio_list, file_name, toCSV=False, toTXT=False):
        '''
        Función que crea y regresa un dataframe con extensión CSV a partir de
        archivos de audio. Las columnas son la cantidad de datos de cada audio
        y las filas son cada uno de los audios individuales. De forma opcional
        el usuario puede guardar el dataframe y transformar este archivo CSV en
        formato TXT que se guarda en la carpeta 'txt'.

        Para cargar los archivos de audio se utiliza la librería Librosa que
        entrega los valores muestreados ya normalizados entre 0 y 1.

        ## Parámetros

        audio_list: Lista con los nombres de los audios a guardar en el
            dataframe.
        file_name: Nombre del archivo CSV creado.
        toCSV: Booleano [opcional]
            Si es True guarda, en formato CSV, los audios que se encuentren en
            la carperta 'wav', en la carpeta 'csv'. El valor por defecto
            'toCSVt=False', evita la conversión.
        toTXT: Booleano [opcional]
            Si es True convierte el archivo CSV creado en formato TXT y se
            guarda en la carpeta de nombre 'csv' que debe estar creada antes de
            la ejecución. El valor por defecto 'toTXT=False', evita la
            conversión. El nombre del archivo TXT es el mismo ingresado en
            variable 'file_name'.
        '''
        # Icialización de varaibles.
        tamano = 0
        lista = []

        print("Working with WAV files...")
        # Se recorre la lista de audios.
        for i in audio_list:
            # Se cargan los archivos .wav normalizados.
            sonido, _ = librosa.load(f'wav/{i}', sr=None)
            # Se eliminan los valores del audio iguales a 0.
            sonido = np.delete(sonido, np.where(sonido == 0))
            # Se agregan cada uno de los audios a la lista.
            lista.append(sonido)

            # Se guarda el tamaño del audio más grande para que ese sea el
            # número máximo de columnas del dataframe.
            if len(sonido) > tamano:
                tamano = len(sonido)

        # Se crean los valores de las columnas del dataframe.
        columns = np.arange(0, tamano)
        # Se crea el dataframe y los valores NaN se cambian por 0.
        df = pd.DataFrame(lista, columns=columns).fillna(0)

        # Si se escoge guardar en formato .txt ejecuta.
        if toCSV:
            print("Saving CSV file...")
            df.to_csv(f'csv/{file_name}', index=False)
        elif toTXT:
            print("Saving TXT file...")
            with open(f'csv/{file_name}', 'r') as inp, open('csv/' + file_name[:-4] + '.txt', 'w') as out:
                for line in inp:
                    line = line.replace(',', ' ')
                    out.write(line)

        return df
