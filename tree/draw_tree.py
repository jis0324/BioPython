import os
input_fasta = "input.fasta"
output = "output"
"""
Infer a gene tree using PhyML. First, convert the alignment from step 3 to “relaxed Phylip” format :
"""

from Bio import AlignIO

AlignIO.convert(input_fasta, "fasta", f"{output}.phy", "phylip-relaxed")

"""
Feed the alignment to PhyML using the command line wrapper:
"""

from Bio.Phylo.Applications import PhymlCommandline

cmdline = PhymlCommandline(
    input=f"{output}.phy", datatype="aa", model="WAG", alpha="e", bootstrap=100
)
out_log, err_log = cmdline()

"""
Load the gene tree with Phylo, 
and take a quick look at the topology. 
(PhyML writes the tree to a file named after the input file plus “_phyml_tree.txt”.)
"""

from Bio import Phylo

egfr_tree = Phylo.read(f"{output}.phy_phyml_tree.txt", "newick")
Phylo.draw(egfr_tree)

"""
Remove unneeded files
"""
unneeded_files = [
    f"{output}.phy_phyml_boot_stats.txt",
    f"{output}.phy_phyml_boot_trees.txt",
    f"{output}.phy_phyml_stats.txt",
]

for unneeded_file in unneeded_files:
    if os.path.exists(unneeded_file):
        os.remove(unneeded_file)
