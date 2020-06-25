import argparse
import sys

from KRNG import RNGs

def main():
    '''generate a Kitten based random number'''
    sys.stdout.write(str(RNGs.KRN()))

if __name__ == "__main__":
    main()