import csv
from pprint import pprint
from io import StringIO


INPUT = 'infinium-methylationepic-v-1-0-b5-manifest-file.csv'
OUTPUT = 'infinium.bed'

f = open(INPUT)
raw_lines = f.readlines()

lines = raw_lines[7:]
header_row = lines[0]
content = u''.join(lines)
sio = StringIO(content)

dict_reader = csv.DictReader(sio)
needed_cols_raw = "CHR_hg38,Start_hg38,End_hg38,Name"
needed_cols = needed_cols_raw.split(',')

# Show a result: pprint(next(dict_reader))

writer = csv.writer(open(OUTPUT, 'w'), dialect='excel-tab')

writer.writerow(needed_cols)
for row in dict_reader:
  append_row = []
  for col in needed_cols:
    append_row.append(row[col])
  writer.writerow(append_row)



