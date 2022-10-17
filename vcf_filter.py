import os
# print(os.listdir())

def vcf_filter(infile,outfile,filton,start):
    """Filters a VCF file with the filtering option in the Info column alone
        infile : input vcf file
        outfile : output vcf file
        filton : term to filter in the INFO field
        start : starting for the header"""
    vcf_in = open(infile,'r',encoding='utf-8',newline='\n')
    vcf_out = open(outfile, 'a',encoding='utf-8',newline='\n')
    vcf_data = vcf_in.readlines()[start:] #
    vcf_header = vcf_in.readlines()[:start]
    for i in vcf_header:
        vcf_out.write(i)
    for j in vcf_data:
        # vcf_ann = j.split("\t")[7]
        if filton not in j:
            vcf_out.write(j)

    vcf_in.close()
    vcf_out.close()
