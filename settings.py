#!/usr/bin/env python3

# Parameters:

TEMPLATE_ABF = 'template.abf'

FREQ = 20  # Samplerate in kHz
STEP = 100  # ms
COUNT = 20

MIN_X = 330  # ms
MAX_X = 510  # ms

OUTPUT_FREQ = 20  # Samplerate in kHz

DIRECTORY = 'F:/Lab Work Files/Patch-clamp data'    # full path to directory with files, leave empty if you run this script in it
SAVE_FILE_NAME_ENDING = '_training_series_splitted_by_sweeps.abf'

FILES_LIST = [
    


]

if __name__ == '__main__':
    ABF_make_gap_free = __import__(ABF-make-gap-free)
    ABF_make_gap_free.main()
