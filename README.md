# From audio files in WAV format to CSV format
This repository contains a simple but very functional code that reads audio files in WAV format using the [Librosa library](https://librosa.org/ "Librosa library") and saves them in CSV or TXT format according to the user´s interests.

### Features

- The code reads the WAV files and saves them in a list;
- If you do `toCSV = True`, the audios are saved in CSV format;
- If you do `toTXT = True`, the audios are saved in TXT format;
- The `wav2csv` method returns the created dataframe.

![](https://i.imgur.com/9Pd0bj7.png)

## How to use
- Just execute in the terminal the code `python3 main.py`. This will returns something like this:

![](https://i.imgur.com/o8U6trl.png)
