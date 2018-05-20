#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 20 10:34:20 2018

@author: aleksandr
"""

from Bio.Blast import NCBIWWW, NCBIXML
from Bio import SeqIO
import argparse
import fileinput

if __name__ == "__main__":
     
    parser = argparse.ArgumentParser(description = 'This script allow ')

    parser.add_argument('-in', '--input_file',help='Open file with data', action='store',required=True)
    parser.add_argument('-out', '--output_file', help='Save result in file', action='store',required=True)

    args = parser.parse_args()

    file_in = args.input_file
    file_out = args.ouput_file
    
    backet = {}

    with open(file_in,"r") as fasta:
        sequences = list(SeqIO.parse(fasta, "fasta"))
    for record in sequences:
        print(record.name)
        result = NCBIWWW.qblast("blastn", "nr", record.seq,hitlist_size=1)
        print('recieved')
        blast = NCBIXML.read(result)
        print('print')
        species =blast.alignments[0].hit_def
        #species = vid.findall(alignment.title)
        if species in backet:
            backet[species].append(str(record.seq))
        else:
            backet[species] = [str(record.seq)]
    
    keylist = list(backet.keys())
    keylist.sort()
    
    with open(file_out,"w") as fasta:
        for organism in keylist:
            print(organism)
            for seq in backet[organism]: 
                fasta.write('>'+organism+'\n')
                fasta.write(str(seq)+'\n')