#1. At first, make sure you installed the python3 on your ubuntu machine
    https://tecadmin.net/install-python-3-8-ubuntu/

 #2. Install needed python libraries.
    - Open the terminal in project folder.
    - Terminal Command: `pip3 install -r requirements.txt`

#3. Execution File Setting.
    - You can find `clustalw-2.1-linux-x86_64-libcppstatic.tar.gz` file in project folder. 
	If not, Download muscle execution file for Linux on following URL.
		http://www.clustal.org/download/current/
    - Extract this `tar.gz` file.
    - Move the extracted `clustalw2` file into `/usr/bin/`.
    	If you have any problem in this step, you can move the file on terminal.
    	Terminal Command: `sudo mv clustalw2 /usr/bin/`

#4. Run the script.
    - Make sure the name of input file is `input.fasta`. If not, please rename to `input.fasta`.
    - Run
	Terminal Command: `python3 clustalw_ubu.py`
    - After running the script, please find `output.fasta` file. This is the result file.
 
