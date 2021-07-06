#1. At first, make sure you installed the python3 on your ubuntu machine
    https://tecadmin.net/install-python-3-8-ubuntu/

 #2. Install needed python libraries.
    - Open the terminal in project folder.
    - Terminal Command: `pip3 install -r requirements.txt`

#3. Execution File Setting.
    - You can find `mafft_7.475-1_amd64.deb` file in project folder. 
	If not, Download mafft execution file for Linux on following URL.
		https://mafft.cbrc.jp/alignment/software/linux.html
    - Install.
        Terminal Command: `sudo dpkg -i mafft_7.475-1_amd64.deb`
        
#4. Run the script.
    - Make sure the name of input file is `input.fasta`. If not, please rename to `input.fasta`.
    - Run
	Terminal Command: `python3 mafft_ubu.py`
    - After running the script, please find `output.fasta` file. This is the result file.
 
