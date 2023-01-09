import sys
sys.path.insert(0,f"c:\\users\\user\\appdata\\local\\programs\\python\\python310\\lib\\site-packages")

import pandas as pd
import networkx as nx
from scipy.stats import ttest_1samp

# reading the observed network from STRING
original_graph = nx.read_edgelist("ncbi_3_large_component.tab",create_using=nx.DiGraph(), nodetype = str)
observed = nx.betweenness_centrality(original_graph)

print(nx.number_of_nodes(original_graph))

# Creating data for random graphs using double edge swap
full_data = []
for i in range(5):
    graph_new = "rand_" + str(i)
    gaph_rand = nx.read_adjlist(graph_new)
    graph_rand = nx.double_edge_swap(original_graph.to_undirected(), nswap=1000, max_tries=10000, seed=1987)
    nx.write_adjlist(graph_rand,graph_new,delimiter='\t')
    data = nx.betweenness_centrality(gaph_rand) # returns a dict with gene, value pairs
    full_data.append(data) # append each network metrics to the data list

# print(len(full_data))

df_rand = pd.DataFrame(full_data) # convert the data into a Pandas dataframe
print(df_rand.shape)

# Calculate p value for 1 sample t test using observed mean and random mean
for gene in observed.keys():
    cent_value = observed[gene]
    mean_rand_cent = df_rand[gene].mean()
    print(gene,cent_value,mean_rand_cent)
    print(ttest_1samp(df_rand[gene],cent_value))

