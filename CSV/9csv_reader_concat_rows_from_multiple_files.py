# !/usr/bin/env python3
import csv
import sys
import glob
import os
input_path = sys.argv[1]
output_file = sys.argv[2]

#print(input_path)
first_file = True
for input_file in glob.glob(os.path.join(input_path, 'sales_*')):
    print(os.path.basename(input_file))
    with open(input_file, 'r') as csv_in_file:
        with open(output_file, 'a') as csv_out_file:
            filereader = csv.reader(csv_in_file)
            filewriter = csv.writer(csv_out_file)
            if first_file:
                for row in filereader:
                    filewriter.writerow(row)
                first_file = False
            else:
                header = next(filereader, None)
                for row in filereader:
                    filewriter.writerow(row)