# program to turn a text file into its byte
# representation in unicode
import sys
script, encoding, error, input_file = sys.argv


def main(encoding, errors):
    input_data = open(input_file, encoding="utf-16").read()

    raw_bytes = input_data.encode(encoding, errors=errors)

    open("ex_23a_output.txt", "w").write(str(raw_bytes))


main(encoding, error)