from sys import argv, exit

script, source, target = argv

print(f"Copying from {source} to {target}")

## indata = open(source).read()
## out_file = open(target, 'w')
## out_file.write(indata)
open(target, 'w').write(open(source).read())
## out_file.close()
exit(0)