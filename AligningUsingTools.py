#This line imports all the required Classes to perform alignments
from Bio.Align.Applications import ClustalOmegaCommandline, MuscleCommandline, ClustalwCommandline, PrankCommandline, MafftCommandline, DialignCommandline, ProbconsCommandline, TCoffeeCommandline, MSAProbsCommandline
#This module is for running another command from the inside of the Python
import subprocess

"""
The following lines are specifying the directories in which the alignment applications are located in the computer e.g. clustalO_exe specifies the directory
in which the "clustalo.exe" is located in the computer. 
<<<<< PLEASE MODIFY THESE DIRECTORIES BEFORE USING THE CODE >>>>>
"""
# clustalO_exe = r"E:\Program Files (x86)\clustalo.exe"
# muscle_exe = r"E:\Program Files (x86)\muscle3.8.31_i86win32.exe"
# clustalW_exe = r"E:\Program Files (x86)\clustalx.exe"
# prank_exe = r"E:\Program Files (x86)\prank.exe"
mafft_exe = r"E:\Program Files (x86)\mafft.exe"
# dialign_exe = r"E:\Program Files (x86)\dialign2-2.exe"
# probcons_exe = r"E:\Program Files (x86)\probcons.exe"
# tcoffee_exe = r"E:\Program Files (x86)\t_coffee.exe"
# msaprobs_exe = r"E:\Program Files (x86)\msaprobs.exe"


# #This line prepares the command to be used in clustal omega application. 
# clustalo_cline = ClustalOmegaCommandline(clustalO_exe, infile=r"Example.fasta", outfile=r"ClustalO.fasta", verbose=True, auto=True)
# #This line shows the prepared command
# print(clustalo_cline)
# #This line runs the command to perform the alignment process
# child = subprocess.Popen(str(clustalo_cline))
# #This line shows a message to the user regarding the finishing of the command
# print("Clustal Omega Alignment Completed!")

# #This line prepares the command to be used in muscle application. 
# muscle_cline = MuscleCommandline(muscle_exe, input=r"Example.fasta", out=r"Muscle.fasta")
# #This line shows the prepared command
# print(muscle_cline)
# #This line runs the command to perform the alignment process
# child = subprocess.Popen(str(muscle_cline))
# #This line shows a message to the user regarding the finishing of the command
# print("Muscle Alignment Completed!")

# #This line prepares the command to be used in clustalw application. 
# clustalw_cline = ClustalwCommandline("C:/Program Files (x86)/ClustalW2/clustalw2.exe", infile=r"input.fasta", outfile = r"ClustalW.fasta")
# #This line shows the prepared command
# print(clustalw_cline)
# #This line shows a message to the user regarding the finishing of the command
# print("ClustalW Alignment Completed!")
# #This line runs the command to perform the alignment process
# child = subprocess.Popen(str(clustalw_cline))


# #This line prepares the command to be used in prank application. 
# prank_cline = PrankCommandline(prank_exe, d=r"Example.fasta", o=r"Prank",  f=8, notree=True, noxml=True)
# #This line shows the prepared command
# print(prank_cline)
# #This line runs the command to perform the alignment process
# child = subprocess.Popen(str(prank_cline))
# #This line shows a message to the user regarding the finishing of the command
# print("Prank Alignment Completed!")

#This line prepares the command to be used in mafft application. 
mafft_cline = MafftCommandline(mafft_exe, input=r"Example.fasta")
#This line shows the prepared command
print(mafft_cline)
#This line runs the command to perform the alignment process
child = subprocess.Popen(str(mafft_cline))
#Since Mafft application doesn't save the output to a file, we need to gather the aligned sequence from the stdout and write it to a file.
#The next 3 lines do this for us.
stdout, stderr = child
with open("Mafft.fasta", "w") as handle:
    handle.write(stdout)
#This line shows a message to the user regarding the finishing of the command
print("Mafft Alignment Completed!")

# #This line prepares the command to be used in dialign application. 
# dialign_cline = DialignCommandline(dialign_exe, input=r"Example.fasta", fn=r"Dialign", fa=True)
# #This line shows the prepared command
# print(dialign_cline)
# #This line runs the command to perform the alignment process
# child = subprocess.Popen(str(dialign_exe))
# #This line shows a message to the user regarding the finishing of the command
# print("Dialign Alignment Completed!")

# #This line prepares the command to be used in probcons application. 
# probcons_cline = ProbconsCommandline(probcons_exe, input=r"Example.fasta", clustalw=True)
# #This line shows the prepared command
# print(probcons_cline)
# #This line runs the command to perform the alignment process
# child = subprocess.Popen(str(probcons_cline))
# #Since Probcons application doesn't save the output to a file, we need to gather the aligned sequence from the stdout and write it to a file.
# #The next 3 lines do this for us.
# stdout, stderr = child
# with open("Probcons.aln", "w") as handle:
#     handle.write(stdout)
# #This line shows a message to the user regarding the finishing of the command
# print("Probcons Alignment Completed!")

# #This line prepares the command to be used in tcoffee application. 
# tcoffee_cline = TCoffeeCommandline(tcoffee_exe, infile=r"Example.fasta", output=r"clustalw", outfile=r"Tcoffee.aln")
# #This line shows the prepared command
# print(tcoffee_cline)
# #This line runs the command to perform the alignment process
# child = subprocess.Popen(str(tcoffee_cline))
# #This line shows a message to the user regarding the finishing of the command
# print("TCoffee Alignment Completed!")

# t_coffee proteases_small.fasta -mode mcoffee -output clustalw, html

# #This line prepares the command to be used in msaprobs application. 
# msaprobs_cline = MSAProbsCommandline(infile=r"Example.fasta", outfile=r"MSAProbs.cla", clustalw=True)
# #This line shows the prepared command
# print(msaprobs_cline)
# #This line runs the command to perform the alignment process
# child = subprocess.Popen(str(msaprobs_cline))
# #This line shows a message to the user regarding the finishing of the command
# print("MSAProbs Alignment Completed!")