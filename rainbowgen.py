#!/usr/bin/env python3
import sys
import os
import argparse
import traceback
from rainbowtable import RainbowTable

try:
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--algorithm', default = 'sha256', help="md5 or sha1 or sha224 or sha256 or sha384 or sha512")
    parser.add_argument('-c', '--charset', default = 'dict',     help="charset must be included in config.ini")
    parser.add_argument('-m', '--min_length', default = 6,       help="minimum length of passwords",type=int)
    parser.add_argument('-M', '--max_length', default = 8,       help="maximum length of passwords",type=int)
    parser.add_argument('-l', '--chain_length', default = 2,     help="length of each chain",type=int)
    parser.add_argument('-n', '--number_of_chains', default = 2, help="number of chains generated",type=int)
    parser.add_argument('-r', '--rainbow_table_file', default = 'result.rt', help="name of rainbow table file")
    parser.add_argument('-d', '--debug', action='store_true')
    parser.add_argument('-v', '--verbose', action='store_true')
    args = parser.parse_args()

    rt = RainbowTable(args.algorithm, args.charset, args.min_length, args.max_length, args.chain_length, args.number_of_chains, args.rainbow_table_file, args.verbose, args.debug)
    rt.generate_table()
    rt.save_to_file(args.rainbow_table_file)

except Exception as e:
    exception_type, exception_object, exception_traceback = sys.exc_info()
    filename = exception_traceback.tb_frame.f_code.co_filename
    line_number = exception_traceback.tb_lineno

    print("Exception type: ", exception_type)
    print("File name: ", filename)
    print("Line number: ", line_number)
    print(traceback.format_exc())
