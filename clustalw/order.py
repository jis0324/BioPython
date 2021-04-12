#This line imports all the required Classes to perform alignments
from Bio import SeqIO, AlignIO

import os

# The parent path that contains this file
base_dir = os.path.dirname(os.path.abspath(__file__))

# reading the alignments
print("Reading Alignments...")
alignments = AlignIO.read(os.path.join(base_dir, "output.fasta"), "fasta")

# sorting the alignments
print("Ordering Alignments...")
alignments.sort(key = lambda alignment : int(alignment.id))

# re-writing the alignments
print("Re-Writing Alignments...")
SeqIO.write(alignments, os.path.join(base_dir, "output.fasta"), "fasta")
