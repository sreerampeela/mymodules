# Script to extract major mutations and alternate alleles from matrix file generated using KMA read mapping to LRE sequences database
# The idea is to look for mutations in 23S rRNA of enterococci and classify as linezolid resistant
# The cutoff depth of alternate alleles is set at 10% 
# Just version 1. Should remove repeated outputs for some sequences
import os
os.chdir(f"D:/icmr_amrsn/23s_analysis/raw_data")
fin = open("J76.mat", newline='\n',encoding='utf-8')

data = [p.rstrip() for p in fin.readlines()]
print(data[:10])
indices = []

for i in data:
    if i.startswith("#") is True:
       indices.append(data.index(i))
print(indices)

# The matrix file has columns in the order Ref,A,C,G,T,N,-(gaps)
# start for the first sequence 23S rRNA of E.faecium
start = indices[0]
end = indices[1]
data_gene = []
data_new = data[start:end]
for j in data_new:
    if j.startswith("-") is False:
        data_gene.append(j)

print(len(data_gene))

bps=['A','C','G','T','N','-']
print(data_gene[0])
outfile = "J76_" + data_gene[0][1:] + "_res2.txt"
fout = open(outfile,'a',encoding='utf-8',newline='\n')
for j in data_gene[1:]:
    
    if len(j) != 0:
        if j.startswith("-") is False:
       
            data = [float(i) for i in j[2:].split("\t")]
            data_copy = data[:]
            depth = sum(data)
        
            if depth != 0:
                A1 = max(data)
                depth1 = round(A1/depth * 100,2)
                data.remove(A1)
                A2 = max(data)
                depth2 = round(A2/depth * 100,2)
                ind_a1 = data_copy.index(A1)
                ind_a2 = data_copy.index(A2)
                allele1 = bps[ind_a1]
                allele2 = bps[ind_a2]
                
                if allele1 != allele2:
                    if j[0] != allele1:
                        print(f"mutation detected {j[0]}{data_gene.index(j)}{allele1} with depth {depth1}")
                        res = f"mutation detected {j[0]}{data_gene.index(j)}{allele1} with depth {depth1}" + "\n"
                    else:
                        res = ""
                    if j[0] != allele2:
                        if depth2 >= 10: #setting alternate allele depth
                            print(f"alternate allele detected {j[0]}{data_gene.index(j)}{allele2} with depth {depth2}")
                            res = res + f"alternate allele detected {j[0]}{data_gene.index(j)}{allele2} with depth {depth2}" + "\n"
                
                if len(res) != 0:
                    fout.write(res)
           
fin.close()
fout.close()
