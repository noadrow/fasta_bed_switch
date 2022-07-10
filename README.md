# Description
This script aim to help create usefull data out of CpG Ids 

## Required 
1. python3
2. python packages: pandas

# Input
This script takes a text file of CpG IDs

# Example:
for example I added the file Up_Control.sort.txt
you can run the following command in terminal: 
``` bash
python .\Id_to_bed.py .\Up_Control.sort.txt 200
```
format python .\Id_to_bed.py "FILENAME" "number of nucleotides to add in each direction"

# Output:
for a file of CpGs Ids you'll get a bed file with the usual columns:
chromosome, start position, end position 
and additional column for the IDs

# NOTE:
using the created bed file now you can also create a fasta file:

``` bash
bedtools getfasta -fi hg38.fa -bed Control_pos.bed
```
