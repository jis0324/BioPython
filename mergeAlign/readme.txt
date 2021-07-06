#1. At first, make sure you installed the python3 on your ubuntu machine
    https://tecadmin.net/install-python-3-8-ubuntu/

 #2. Install needed python libraries.
    - Open the terminal in project folder.
    - Terminal Command: `pip3 install -r requirements.txt`

#3. Run the script.
    - Reference :
	To combine multiple alignments:
        % python MergeAlign.py -a path/to/folder -f path/to/file -s path/to/file
        
    	-a --alignments
        	ARG: path to a folder
        	Path to a folder containing all the FASTA alignments you want to combine.
        	All the alignments must be of the same set of sequences.
        
    	OPTIONAL :
    	
    	-f --fasta
        	ARG: filename
        	Final alignment is saved as a FASTA file with this name.
        
    	-s --score
        	ARG: filename
        	Final scores are saved as a list in a text file with this name.
        
    	-t --score
        	ARG: number >0 and <= 1
        	Only columns with a score > threshold are outputted.
        	Only works in conjection with -f.

    	Additional arguments:

    	-h, --help
        	ARG: none
        	Get command line arguments.
    
    - After running the script, please find the result file in the path that you set when you run the script as -f argument.
 
