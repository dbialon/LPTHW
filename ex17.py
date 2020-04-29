# -- coding: utf-8 --

from sys import argv, exit
from os.path import exists

from_file = argv[1]
to_file = argv[2]

print(f"Copying from {from_file} to {to_file}")

## we could do these on one line. How?
## in_file = open(from_file)
## indata = in_file.read()
indata = open(from_file).read()
## solution

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

## out_file = open(to_file, 'w')
## out_file.write(indata)
open(to_file, 'w').write(indata)

print("Alright! All done.")
exit(0)

## always close the file
## out_file.close() 
## in_file.close()
## in this case it's not necessary to close the files
## as they are not defined as the code has been altered
## in lines 11-13 and 22-24