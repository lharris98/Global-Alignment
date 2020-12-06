import argparse

from Bio import SeqIO
from Bio import pairwise2

# Input fasta file
description = "Python command line program that will take a fasta file with two DNA sequences and globally align them."
parser = argparse.ArgumentParser(description=description)
parser.add_argument(
        "filename",
        help="Faste file with two DNA sequences",
        metavar="<fasta file>")

args = parser.parse_args()

'''

Separate sequences in fasta file and assign to different files

'''

records = [record for record in SeqIO.parse(args.filename, 'fasta')]

if len(records) != 2:
    print("Too many sequences")
    exit()
    
''' 

Begin global alignment

'''

seq_1,seq_2 = records

# Import format_alignment method
from Bio.pairwise2 import format_alignment

# A match score of 2, a mismatch score of -1.Gap open penalty of -0.5 and gap extension penalty of -0.1
alignments = pairwise2.align.globalms(seq_1.seq, seq_2.seq,2,-1,-0.5,-0.1)

# Format and print alignments
for a in alignments:
    print(format_alignment(*a))
