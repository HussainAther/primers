# -*- coding: utf-8 -*-
import sys
import csv

import numpy as np
import pandas as pd

"""
Script to store the forward and reverse complement primers from the
excel sheet.

USAGE:

    "python parse.py <file_with_list_of_primers>"

"""
inputseqfile = sys.argv[1]

def remove_non_ascii(text):
    return unidecode(unicode(text, encoding = "utf-8"))

def in_dna(text):
    result = ""
    for i in text.upper():
        if i in "ACGT" and i != "":
            result += i
    return result

alt_map = {"ins":"0"}
complement = {"A": "T", "C": "G", "G": "C", "T": "A"}

def rev(seq):
    """
    Find the reverse complement of a DNA string
    """
    for k,v in alt_map.items():
        seq = seq.replace(k,v)
    bases = list(seq)
    bases = reversed([complement.get(base,base) for base in bases])
    bases = ''.join(bases)
    for k,v in alt_map.items():
        bases = bases.replace(v,k)
    return bases

primerdict = {} # store each primer sequence with its corresponding primer name in this dictionary

df = pd.read_csv("HBlabprimers.csv") # read in the .csv file as a pandas DataFrame

for i in (df.index):
    seq_name = str(df.iloc[i]["Primer name"]) # get the sequence name
    seq = in_dna(str(df.iloc[i]["Sequence"])) # get the sequence as a DNA string. remove all extra characters as we do this.
    revseq = rev(seq) # get the reverse complement of the DNA sequence string
    primerdict[seq] = seq_name # store sequence as key and sequence name as value
    primerdict[revseq] = seq_name + "_rev" # store the key reverse sequence with the item plus "_rev"

foundprimers = []

with open(inputseqfile) as file:
    count = 0
    for seq in file:
        seq = seq.replace("\n", "")
        revseq = rev(seq)
        if seq in primerdict:
            print("Found primer: " + str(primerdict[seq]))
            count += 1
        elif revseq in primerdict:
            print("Found primer: " + str(primerdict[revseq]))
            count += 1
    print("Total primers: " + str(count))



