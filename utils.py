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
        ## English:
        Function that creates and returns a dataframe with a CSV extension from
        audio files. The columns are the amount of data for each audio and the
        rows are each of the individual audios. Optionally, the user can save
        the dataframe and transform this CSV file into TXT format that is saved
        in the 'txt' folder.

        To load the audio files, the Librosa library is used, which delivers
        the sampled values already normalized between 0 and 1.

        ## Parameters

        audio_list: array-like
            List with the names of the audios to be saved in the dataframe.
        file_name: str
            Name of the created CSV file.
        toCSV: Boolean [optional]
            If it's True saves, in CSV format, the audios found in the 'wav'
            folder, in the 'csv' folder. The default value 'toCSVt = False',
            prevents conversion.
        toTXT: Boolean [optional]
            If it is True, it converts the created CSV file into TXT format and
            is saved in the folder named 'csv' that must be created before
            execution. The default value 'toTXT = False', prevents conversion.
            The name of the TXT file is the same one entered in variable
            'file_name'.

        ## Español:
        Función que crea y regresa un dataframe con extensión CSV a partir de
        archivos de audio. Las columnas son la cantidad de datos de cada audio
        y las filas son cada uno de los audios individuales. De forma opcional
        el usuario puede guardar el dataframe y transformar este archivo CSV en
        formato TXT que se guarda en la carpeta 'txt'.

        Para cargar los archivos de audio se utiliza la librería Librosa que
        entrega los valores muestreados ya normalizados entre 0 y 1.

        ## Parámetros

        audio_list: array-like
            Lista con los nombres de los audios a guardar en el dataframe.
        file_name: str
            Nombre del archivo CSV creado.
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
        # Variable initialization.
        tamano = 0
        lista = []

        print("Working with WAV files...")
        # The list of audios is scrolled.
        for i in audio_list:
            # The normalized WAV files are loaded.
            sonido, _ = librosa.load(f'wav/{i}', sr=None)
            # Audio values equal to zero (0) are removed.
            sonido = np.delete(sonido, np.where(sonido == 0))
            # Each of the audios are added to the list.
            lista.append(sonido)

            # The size of the largest audio is saved so that this is the
            # maximum number of columns in the dataframe.
            if len(sonido) > tamano:
                tamano = len(sonido)

        # The values of the columns of the dataframe are created.
        columns = np.arange(0, tamano)
        # The dataframe is created and the NaN values are changed to 0.
        df = pd.DataFrame(lista, columns=columns).fillna(0)

        # Option to save audios in CSV or TXT formats.
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
