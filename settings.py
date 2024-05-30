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


# '\\TRP project\\2024_03_11\\2024_03_11_0003.abf',
# '\\TRP project\\2024_03_11\\2024_03_11_0006.abf',
# '\\TRP project\\2024_03_11\\2024_03_11_0008.abf',
# '\\TRP project\\2024_03_11\\2024_03_11_0009.abf',

# '\\TRP project\\2024_03_12\\2024_03_12_0001.abf',
# '\\TRP project\\2024_03_12\\2024_03_12_0003.abf',
# '\\TRP project\\2024_03_12\\2024_03_12_0005.abf',
    
# '/TRP project/2024_03_24/2024_03_24_0001.abf',

# '/TRP project/2024_03_25/2024_03_25_0009.abf',
# '/TRP project/2024_03_25/2024_03_25_0011.abf',

# '/TRP project/2024_03_26_M1/2024_03_26_0001.abf',
# '/TRP project/2024_03_26_M1/2024_03_26_0003.abf',
    
# '/TRP project/2024_03_26_M2/2024_03_26_0007.abf',

# '/TRP project/2024_04_08/2024_04_09_0004.abf',

# '/TRP project/2024_04_09/2024_04_09_0006.abf',

# '/TRP project/2024_04_18/2024_04_18_0003.abf',

# '/TRP project/2024_05_21_M1/2024_05_21_0006.abf',
# '/TRP project/2024_05_21_M2/2024_05_21_0009.abf',
# '/TRP project/2024_05_22/2024_05_22_0010.abf',
# '/TRP project/2024_05_23_M1/2024_05_23_0001.abf',
# '/TRP project/2024_05_23_M2/2024_05_23_0004.abf',
# '/TRP project/2024_05_23_M2/2024_05_23_0008.abf',

# '/TRP project/2024_05_28_M1/2024_05_28_0001.abf',
# '/TRP project/2024_05_28_M1/2024_05_28_0003.abf',
# '/TRP project/2024_05_29_M1/2024_05_29_0008.abf',
# '/TRP project/2024_05_29_M1/2024_05_29_0012.abf',
# '/TRP project/2024_05_29_M2/2024_05_29_0016.abf',
# '/TRP project/2024_05_29_M3/2024_05_29_0020.abf',



]

if __name__ == '__main__':
    ABF_make_gap_free = __import__('ABF-rc-remover')
    ABF_make_gap_free.main()
