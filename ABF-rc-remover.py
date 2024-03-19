#!/usr/bin/env python3

import numpy as np 
import pyabf
import settings as s


def convert(filename, MIN_X, MAX_X):

    abf = pyabf.ABF(filename)

    for i in range(abf.sweepCount):

        abf.setSweep(i, 0)
        abf.sweepY[:]
        abf.sweepY[MIN_X:MAX_X] = np. zeros(len(abf.sweepY[MIN_X:MAX_X]))

    abf.saveABF1(filename + s.SAVE_FILE_NAME_ENDING)  # , s.OUTPUT_FREQ*1000) - to save in different samplerate
    print(filename, ' proceed successfull')


def main():

    # converting ms to sample count
    MIN_X = s.MIN_X * s.FREQ
    MAX_X = s.MAX_X * s.FREQ

    for path in s.FILES_LIST:
        try:
            convert(s.DIRECTORY + path, MIN_X, MAX_X)
        except Exception as e: print(e)

    print('\nQueue proceed successfull')

if __name__ == '__main__':
    main()