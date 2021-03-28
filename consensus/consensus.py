# imports all the required Classes to read alignments
from Bio import SeqIO, AlignIO
import os

# The parent path that contains this file
base_dir = os.path.dirname(os.path.abspath(__file__))

# file_path
file_path = f"{base_dir}/output.fasta"

# length of alignment
alignment_length = AlignIO.read(file_path, "fasta").get_alignment_length()

# define list variable that contain final result
final_consensus_list = list()

# iter columns (column1, column2, column3...)
for column_index in range(alignment_length):
    # pairs list per column (column1, column2 ...)
    """
    column_list is https://prnt.sc/10wh76n
    for example : ["-", "G", "A"]
    """
    column_list = [seq_record.seq[column_index] for seq_record in SeqIO.parse(file_path, "fasta")]

    # result of column ("-":3, "G":3.5, "A":3.5...)
    """
    The element of column_consensus_list is https://prnt.sc/10wi0to
    for example : [{"letter":"-", "value":"3"},{"letter":"G", "value":"3.5"},{"letter":"A", "value":"3.5"}]
    """
    column_consensus_list = list()

    # iterate elements of column(A[1][1], A[2][1], A[3][1]...)
    """
    https://prnt.sc/10wi4e9
    """
    for i in column_list:
        # result each selecting character
        column_ele = {
            "letter": i,
            "value" : 0
        }

        # iter rows in column(A[1][1], A[1][2], A[1][3]...)
        for j in column_list:
            # if same
            if i == j:
                column_ele["value"] += 0
            # if not same
            else:
                # if anyone is "-"
                if i == "-" or j == "-":
                    column_ele["value"] += 1.5
                # diff characters.
                else:
                    column_ele["value"] += 2
        
        column_consensus_list.append(column_ele)
    
    # get minium cost and letter from column_consensus_list
    """
        will select minimum one value `{"letter":"-", "value":"3"}` 
                from column_consensus_list [{"letter":"-", "value":"3"},{"letter":"G", "value":"3.5"},{"letter":"A", "value":"3.5"}]
    """ 
    min_item = dict()
    for item in column_consensus_list:
        if not min_item:
            min_item = item
        else:
            if min_item["value"] > item["value"]:
                min_item = item

    # append the column data(minium cost & letter) to final result
    final_consensus_list.append(min_item)

    print(f"Column {column_index} => Letter : {min_item['letter']}, Value : {min_item['value']}")

# make append text for Consensus Sequence
consensus_sequence_text = ">Consensus Sequence : "
consensus_sequence_text += " ".join([" " + item["letter"] + " " for item in final_consensus_list])

# make append text for Column Value
column_value_list = [item["value"] for item in final_consensus_list]
column_value_text = ""
for item in column_value_list:
    if "." in str(item):
        column_value_text += str(item)
    else:
        column_value_text += " "+str(item)+" "
    column_value_text += " "

column_value = ">   Column Value    : " + column_value_text + " = " + str(sum(column_value_list))

# append to file
with open(file_path, "a") as output_file:
    output_file.write(f"\n{consensus_sequence_text}\n{column_value}")