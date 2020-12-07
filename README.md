# global-alignment

Python command line program that will take a fasta file with two DNA sequences and globally align them.

Biopython must be installed to use this program. 

To make executable from the command line, type the command: $ chmod +x global-alignment.py. 

Input a single positional argument of the fasta file containing only two DNA sequences. The program will then run and the alignment result will be printed to standard output. If too many arguments are included, or the fasta file includes more than two sequences, the program will not run and a help message will prompt the user for the proper input. 
