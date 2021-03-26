#This line imports all the required Classes to perform alignments
from Bio.Align.Applications import ClustalwCommandline
#This module is for running another command from the inside of the Python
import subprocess, time, os, psutil, sys

# Max CPU Usage Value while processing
max_cpu = 0

# Max Memory Usage Value while processing
max_memo = 0

# Total execution time
elsapsedTime = 0

# The parent path that contains this file
base_dir = os.path.dirname(os.path.abspath(__file__))

# The path of clustalw file.
clustalW_exe = "clustalw2"

#This line prepares the command to be used in clustalw application. 
clustalw_cline = ClustalwCommandline(clustalW_exe, infile=os.path.join(base_dir, "input.fasta"))

#This line is to save the starting time of mafft 
timeStarted = time.time() 

#This line runs the command to perform the alignment process
# child = subprocess.Popen(str(clustalw_cline), shell=True, universal_newlines=True)
# child = subprocess.Popen(clustalW_exe, shell=True, universal_newlines=True)
child = subprocess.Popen(['gnome-terminal', '--', clustalW_exe])

# waiting until subprocee is running
time.sleep(90)
# print("\n")

while True:
    
    #This line is to compute the elapsed time 
    elsapsedTime = time.time() - timeStarted
    
    # current cpu usage
    cur_cpu = psutil.cpu_percent()

    # Store if current cpu usage is bigger
    max_cpu = cur_cpu if cur_cpu > max_cpu else max_cpu

    # current memory usage
    cur_memory = psutil.virtual_memory().percent

    # Store if current memory usage is bigger
    max_memo = cur_memory if cur_memory > max_memo else max_memo
    
    # print("Execution Time: {}s / CPU Usage: {}% / Memory Usage: {}%".format(int(elsapsedTime), cur_cpu, cur_memory), end="\r")
    
    # Check subprocess status.
    poll = child.poll()
    if poll is None:
        # subprocess is alive yet.
        time.sleep(60)
        continue
    else:
        # subprocess already finished.
        break

print("\nFinished Successfully", end="\n")
print("Execution Time: {}".format(int(elsapsedTime)))
print("Max CPU Usage : {}".format(max_cpu))
print("Max Memory Usage : {}".format(max_memo))
