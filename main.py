"""
Created by kardantel at 3/23/2021
__author__ = 'Carlos Pimentel'
__email__ = 'carlosdpimenteld@gmail.com'
"""

import warnings
import os
from utils import Utils
warnings.filterwarnings('ignore')

utils = Utils()


def main():
    listaAudios = os.listdir("./wav")
    df = utils.wav2csv(listaAudios, "audios_neo.csv", toCSV=True, toTXT=True)
    print(df)


if __name__ == "__main__":
    main()
