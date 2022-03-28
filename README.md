# RainbowHub
[![CircleCI](https://circleci.com/gh/bobctr/rainbowhub.svg?style=svg)](https://circleci.com/gh/bobctr/rainbowhub) [![codecov](https://codecov.io/gh/bobctr/rainbowhub/branch/master/graph/badge.svg)](https://codecov.io/gh/bobctr/rainbowhub)


Simple Rainbow tables implementation.

## What a rainbow table is and how it is implemented
https://en.wikipedia.org/wiki/Rainbow_table

https://www.geeksforgeeks.org/understanding-rainbow-table-attack/

A **rainbow table** is a complex data structure used for hash cracking, whose main goal is making the task significantly more time-efficient than brute-forcing, while keeping the space on disk needed very small compared to hash tables.

Rainbow tables contain *precomputed hash chains*, which are generated with a sequence of hash/reduce function application on a starting random plaintext, where only the head and the tail of each chain are stored.
These chains are then used during the cracking process, where the target hash is reduced/hashed multiple times until a match with a chain tail is found.
After that, the corresponding chain is generated again until the target hash is matched.

Rainbow tables can be easily countered adding a *salt* (small random string of bytes) to a stored hash.

## What I have learned
The purpose of this project is to understand how a rainbow table is implemented and used, with a practical approach.
While developing, I found myself dealing with various challenges, that gave me a deeper understanding on:

  1. **How hashing and rainbow tables work**, and how some hashing algorithms can be exploited efficiently, finding the compromise between a brute-force approach and a pure lookup table
  2. How to master and combine common **data structures** to build an efficient solution (lists, dictionaries, ...)
  3. Python API and modules such as
     * _argparse_ -- to easily handle arguments for my scripts
     * _hashing_ -- to use SHA1 and MD5 hash functions
     * _pickle_ -- to store in a file the generated table, and restore it for cracking
     * _itertools_ -- to generate random passwords to start chains with
  4. Python **Unit Tests** run with _pytest_ module
  5. Continuous Integration (build, test, code coverage on **CircleCI**) 

## Key features
  - Custom rainbow table generator
    - support charset (lower_alphanumeric, alphanumeria, ascii, numeric, dict)
      - dict: specify original dictionary file
    - support algorithm (MD5, SHA1, SHA224, SHA256, SHA384, SHA512)
  - Table serialization
  
------

### Configuration
All the charset available with their respective names are written in ```config/config.ini```.
If you want to add a custom one, just add it at the end of the file.

### Run
To generate a new table

```
usage: python3 rainbowgen.py [-h] [-a ALGORITHM] [-c CHARSET] [-D DICTIONARY_FILE] [-m MIN_LENGTH] [-M MAX_LENGTH]
                     [-l CHAIN_LENGTH] [-n NUMBER_OF_CHAINS] [-r RAINBOW_TABLE_FILE] [-d] [-v]

```
- ```ALGORITHM```: name of the hashing algorithm (currently SHA1 and MD5 are available) (default: sha1)
- ```CHARSET_NAME```: name of the charset used to generate random plaintext (available charsets are defined in config/config.ini) (default: dict)
- ```DICTIONARY_FILE```: path od dictiname file name (default:dict/sample.txt)
- ```MIN_LENGTH```: range for random plaintext length (default: 6)
- ```MAX_LENGTH```: range for random plaintext length (default: 8)
- ```CHAIN_LENGTH```: number of *hash/reduce* iterations for each chain (default: 2)
- ```NUMBER_OF_CHAINS```: number of tuples *head_plaintext/tail_hash* that will be generated (default: 2)
- ```RAINBOW_TABLE_FILE```: path of rainbow table fileoutput file (conventionally with extension *.rt*) (default:result.rt)

To try cracking a hash:

```
usage: python3 rainbowcrack.py [-h] [-r RAINBOW_TABLE_FILE] [-d] [-v] hash_string
```
- ```hash_string```: string containing the hash to crack
- ```RAINBOW_TABLE_FILE```: file containing the generated rainbow table (conventionally with extension *.rt*)

Example:
To generate a new table with default option
```
python3 rainbowgen.py
```
To generate a new table with dictionary mode
```
python3 rainbowgen.py --charset dict --dictionary_file dict/original.txt
```
To generate a new table with charset ascii
```
python3 rainbowgen.py --charset ascii --min_length 8 --max_length 12 --chain_length 10 --number_of_chains 10
```
To try crack a hash
```
python3 rainbowcrack 948134107bce4ae2d990bb08466c6d9eede4146bc13d255d4760509b28fe722d
```
