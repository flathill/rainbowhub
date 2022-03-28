#!/usr/bin/env python3
import sys
import os
import argparse
import traceback
from rainbowtable import RainbowTable

try:
    parser = argparse.ArgumentParser()
    parser.add_argument("hash_string", help="hash to crack")
    parser.add_argument('-r', '--rainbow_table_file', default = 'result.rt', help="name of rainbow table file")
    parser.add_argument('-d', '--debug', action='store_true')
    parser.add_argument('-v', '--verbose', action='store_true')
    args = parser.parse_args()

    rt = RainbowTable.load_from_file(args.rainbow_table_file)
    psw = rt.lookup(args.hash_string, args.debug)

    if(psw is not None):
        print("Candidate found: " + psw)
    else:
        print("No match found")

except Exception as e:
    exception_type, exception_object, exception_traceback = sys.exc_info()
    filename = exception_traceback.tb_frame.f_code.co_filename
    line_number = exception_traceback.tb_lineno

    print("Exception type: ", exception_type)
    print("File name: ", filename)
    print("Line number: ", line_number)
    print(traceback.format_exc())
