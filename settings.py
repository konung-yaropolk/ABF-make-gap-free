#!/usr/bin/env python3

# Parameters:

TEMPLATE_ABF = 'template.abf'

FREQ = 20  # Samplerate in kHz
OUTPUT_FREQ = 20  # Samplerate in kHz

MIN_X = 150  # ms
MAX_X = 300  # ms


DIRECTORY = 'F:/Lab Work Files/Patch-clamp data'    # full path to directory with files, leave empty if you run this script in it
SAVE_FILE_NAME_ENDING = '_noRC.abf'

FILES_LIST = [

'\\TRP project\\2024_03_12\\2024_03_12_0001.abf',
'\\TRP project\\2024_03_12\\2024_03_12_0005.abf',


]

if __name__ == '__main__':
    ABF_make_gap_free = __import__('ABF-rc-remover')
    ABF_make_gap_free.main()
