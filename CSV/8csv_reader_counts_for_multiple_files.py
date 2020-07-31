# !/usr/bin/env python3
import csv
import sys
import glob
import os
input_path = sys.argv[1]
file_counter = 0
# print(input_path) 查看input_path是否有问题
for input_file in glob.glob(os.path.join(input_path, 'sales_*')):
    row_counter = 1
    with open(input_file, 'r') as csv_in_file:
        filereader = csv.reader(csv_in_file)
        header = next(filereader, None)
        for row in filereader:
            row_counter += 1
        print('{0!s}: \t{1:d} rows \t {2:d} clumns'.format(os.path.basename(input_file), row_counter, len(header)))
        file_counter += 1
print('Number of files: {0:d}'.format(file_counter))