#1. At first, make sure you installed the python3 on your ubuntu machine
    https://tecadmin.net/install-python-3-8-ubuntu/

 #2. Install needed python libraries.
    - Open the terminal in project folder.
    - Terminal Command: `pip3 install -r requirements.txt`

#3. Execution File Setting.
    - You can find `T-COFFEE_installer_Version_13.45.0.4846264_linux_x64.bin` file in project folder. 
	If not, Download install file for Linux on following URL.
		http://www.tcoffee.org/Packages/Stable/Latest/T-COFFEE_installer_Version_13.45.0.4846264_linux_x64.bin
    - Install.
        Terminal Command: `chmod a+x T-COFFEE_installer_Version_13.45.0.4846264_linux_x64.bin`
        Terminal Command: `./T-COFFEE_installer_Version_13.45.0.4846264_linux_x64.bin`
    - restart Terminal.

#4. Run the script.
    - Run
	    Terminal Command: `python3 mcoffee_ubu.py`
    - Type the full path of input file.
    - After running the script, please find `output.fasta` file. This is the result file.
 
