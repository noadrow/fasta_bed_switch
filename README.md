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

Another possibal work-flow is to start with a fasta file and convert it to bed file 
``` bash
python .\fasta_record_to_bed.py .\Control_400_hg38.fa 
```
This script will return the record names of the fasta file as bed

Then you can intersect them with the file infinium.bed
that containes all infinium illumina CpG sites following cut for the 4th column if you wish to collect only the CpGs sites that were on the original fasta file

``` bash
bedtools intersect -a Control_400_hg38.bed -b illumina.bed | cut -f4 > new.bed 

```
