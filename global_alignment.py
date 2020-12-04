import os
from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio import pairwise2


'''

Separate sequences in fasta file into different files

'''

records = SeqIO.parse('____file____.fna', 'fasta')

#split fasta file into two groups
def split_even(records,n):
    step = len(records)//n
    grouped = []
    for i in range(n):
        if i == (n-1):
            grouped.append(records[i*step:])
        else:
            grouped.append(records[i*step:(i*step)+step])
    return grouped

n = 2
records = []
for record in SeqIO.parse('____file____.fna', 'fasta'):
    records.append(record)
    
batches = split_even(records,n) #splitting
     
#write each sequence to separate files 
for i,batch in enumerate(batches):
    SeqIO.write(batch,'seq_{}.fasta'.format(i+1),'fasta')

    
''' 

Begin pairwise sequence alignment

'''


# Assign sequence files to variables
seq_1 = open('seq_1.fasta')
seq_1.readline() 

x = seq_1.read().replace('\n','')

seq_2 = open('seq_2.fasta')
seq_2.readline()

y = seq_2.read().replace('\n','')

# Import format_alignment method
from Bio.pairwise2 import format_alignment

# A match score of 2, a mismatch score of -1.Gap open penalty of -0.5 and gap extension penalty of -0.1
alignments = pairwise2.align.globalms(x, y,2,-1,-0.5,-0.1)
# Format and print alignments
for a in alignments:
    print(format_alignment(*a))