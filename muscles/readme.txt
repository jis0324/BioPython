#1. At first, make sure you installed the python3 on your ubuntu machine
    https://tecadmin.net/install-python-3-8-ubuntu/

 #2. Install needed python libraries.
    - Open the terminal in project folder.
    - Terminal Command: `pip3 install -r requirements.txt`

#3. Execution File Setting.
    - You can find `muscle3.8.31_i86linux64.tar.gz` file in project folder. 
	If not, Download muscle execution file for Linux on following URL.
		https://www.drive5.com/muscle/downloads.htm
    - Extract this `tar.gz` file.
    - Move the extracted file into `/usr/bin/`.
    	If you have any problem in this step, you can move the file on terminal.
    	Terminal Command: `sudo mv muscle3.8.31_i86linux64 /usr/bin/`

#4. Run the script.
    - Make sure the name of input file is `input.fasta`. If not, please rename to `input.fasta`.
    - Run
	Terminal Command: `python3 muscles_ubu.py`
    - After running the script, please find `output.fasta` file. This is the result file.
 
