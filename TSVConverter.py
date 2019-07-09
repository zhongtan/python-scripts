# Author: Zheng Hong Tan (github.com/zhongtan)
# Description: Python script that takes a TSV file and converts it into a CSV file.

import csv

# user introduction 
print("Before we begin, please specify the entire file path of the TSV file.")
print("To specify the entire file path, open a terminal session and navigate")
print("to the directory containing the TSV file and type \"pwd\" in the command")
print("prompt. Append the name of the file to the output of this prompt to get")
print("the full path to the TSV file.\n")

# get input and output files
tsv_file = input("Please specify the full directory path of the input file here: ")
out_file = input("Please specify the output file (including .csv extension): ")

try:
    with open(tsv_file) as inFile, open(out_file, 'w') as outFile:
        reader = csv.reader(inFile, delimiter='\t')
        writer = csv.writer(outFile, delimiter=',')

        for r in reader:
            out = []
            for val in r:
                out.append(val)
            writer.writerow(out)
except IOError as e:
    print("IOError: {0}".format(e))
