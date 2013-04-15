from Bio import Phylo
tree = Phylo.read("sample.dnd", "newick")
tree.rooted = True
ancestor = tree.common_ancestor("E","A")
ancestor.name = "Common_E_A"
Phylo.draw(tree)
