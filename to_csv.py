import csv

ur_infile = input("Input File:")
ur_outfile=input("Output File:")

with open(ur_infile) as fin, open(ur_outfile, 'w') as fout:
    o=csv.writer(fout)
    for line in fin:
        o.writerow(line.split())