import csv
from pprint import pprint
from io import StringIO
import pandas as pd
import sys

INPUT_ref = 'infinium.bed'
INPUT_control = 'Up_Control.sort.txt'

Control_list = []
Prog_list = []

#OUTPUT_control = 'Control_pos.bed'
OUTPUT_control = sys.argv[1]

Control_pos_list = ""

i = 0
#determin length of each sequence
length = 200

for line_control in open(INPUT_control,"r"):

    Control_list.append(line_control.replace('\n',''))
    
for chunk in pd.read_csv(INPUT_ref,sep='\t',header=0, on_bad_lines='skip').dropna().iterrows():

    chunk_chr = str(chunk[1][0])
    chunk_start = str(int(chunk[1][1])-length)
    chunk_end = str(int(chunk[1][2])+length)
    chunk_ID = str(chunk[1][3])
    
    if chunk_ID in Control_list:
        Control_pos_list+= chunk_chr+"\t"+chunk_start+"\t"+chunk_end+"\t"+chunk_ID+"\n"
        i += 1

    if (i>(len(Control_list)+len(Prog_list))):
        break

open(OUTPUT_control,"w").write(Control_pos_list)



