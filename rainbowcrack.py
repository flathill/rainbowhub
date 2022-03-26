import sys
import os
import argparse
from rainbowtable import RainbowTable

try:
    parser = argparse.ArgumentParser()
    parser.add_argument("hash_string", help="hash to crack")
    parser.add_argument("rainbow_table_file", help="name of file containing a valid rainbow table"
    " (generated from rainbowgen.py)")
    parser.add_argument('-d', '--debug', action='store_true')
    parser.add_argument('-v', '--verbose', action='store_true')
    args = parser.parse_args()

    rt = RainbowTable.load_from_file(args.rainbow_table_file)
    psw = rt.lookup(args.hash_string, args.verbose, args.debug)

    if(psw is not None):
        print("Candidate found: " + psw)
    else:
        print("No match found")

except Exception as e:
    print("ERROR: " + str(e))
