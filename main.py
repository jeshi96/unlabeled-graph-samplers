import sys
sys.path.insert(0,'C:/Users/Jessica Shi/Documents/Princeton/COS 397/code/util/')
import parse_graphs_format as parse
import split_tree as st
import networkx as nx
import matplotlib.pyplot as plt

path="C:/Users/Jessica Shi/Documents/Princeton/COS 397/code/unlabeled-graph-samplers/test_data/"

def main():
    f = open(path+"data1.txt","r")
    i=1
    for line in f:
        if not line.strip():
            continue
        print "LINE: "+line
        if "#" in line:
            continue
        s_tree = st.string_to_split_tree(line)
        p_graph = st.split_tree_to_graph(s_tree)
        st.export_graph(p_graph,path+"g_%d"%(i))
        i += 1
    f.close()

if __name__ == "__main__":
    main()
