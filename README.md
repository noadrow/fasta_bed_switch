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
python .\Id_to_bed.py .\Up_Control.sort.txt
```

# Output:
for a file of CpGs Ids you'll get a bed file with the usual columns:
chromosome, start position, end position 
and additional column for the IDs

# NOTE:
now you can use bedtools to get also a fasta file out:
``` bash
bedtools getfasta -fi hg38.fa -bed Control_pos.bed
```
