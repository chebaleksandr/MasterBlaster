# MasterBlaster
Tool for fast BLAST search and name contigs  
![MasterBLASTer](https://github.com/chebaleksandr/MasterBlaster/blob/master/mad-max-3-master-blaster.jpg)  
## Description
For input this script take fasta file with unnamed sequences, BLAST it and return fasta file with named sequences, like: 
```
>rr  
GAAACAATTTGGTTGGTACCAATTAAGCAACTCAAAGTGACCTATCACCATTTGAGAAGCCAGTCTCAAGAAGCAGCCTATTATCAAAGAACAGGATATGGCTCGGATATTTTGTACGAATGTAATCAGC  

>Lichtheimia ramosa strain JMRC FSU:6197 genome assembly, scaffold: SCAF9  
GAAACAATTTGGTTGGTACCAATTAAGCAACTCAAAGTGACCTATCACCATTTGAGAAGCCAGTCTCAAGAAGCAGCCTATTATCAAAGAACAGGATATGGCTCGGATATTTTGTACGAATGTAATCAGC
```
## Dependencies
To run this script, you nees __python3__, and current libraries:  
  [argparse](https://docs.python.org/3/library/argparse.html)  
  [biopython](http://biopython.org/)  
  [fileinput](https://docs.python.org/2/library/fileinput.html)  

## Run
This script needs just two arguments:  
  __-in__ - input file (file with unnamed sequences)  
  __-out__ - output file (file for named sequences)  

You need write full path/to/the/file, like that:
```
python MasterBlaster.py -in path/to/my/unnamed_sequences_file.fasta -out path/to/the/file_with_named_sequences.fasta
```

