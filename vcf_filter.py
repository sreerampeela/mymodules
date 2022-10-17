import os
# print(os.listdir())

def vcf_filter(infile,outfile,filton):
    """Filters a VCF file with the filtering option in the Info column alone
        infile : input vcf file
        outfile : output vcf file
        filton : term to filter in the INFO field"""
    vcf_in = open(infile,'r',encoding='utf-8',newline='\n')
    vcf_out = open(outfile, 'a',encoding='utf-8',newline='\n')
    vcf_data = vcf_in.readlines()[34:]
    vcf_header = vcf_in.readlines()[:34]
    for i in vcf_header:
        vcf_out.write(i)
    for j in vcf_data:
        # vcf_ann = j.split("\t")[7]
        if filton not in j:
            vcf_out.write(j)

    vcf_in.close()
    vcf_out.close()


# vcf_in = open("merged_test.vcf",'r',encoding='utf-8',newline='\n')
# vcf_out = open("merged_filtered.vcf",'w',encoding='utf-8',newline='\n')

# vcf_lines = vcf_in.readlines()[34:]
# # print(vcf_lines[:2])
# vcf_header = vcf_in.readlines()[:34]
# for i in vcf_header:
#     vcf_out.write(str(i)+"\n")
# for j in vcf_lines:
#     vcf_ann = j.split('\t')[7].split("|")[1]
#     # print(vcf_ann)
#     if vcf_ann != "synonymous_variant":
#         vcf_out.write(str(j)+"\n")


# vcf_in.close()
# vcf_out.close()

vcf_filter("B12510.vcf","B12510_filt.vcf","synonymous")