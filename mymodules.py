""""A simple module to create scripts for automated download and assembly of bacterial genomes.
The tool uses NCBI SRA toolkit and the SHOVILL pipeline.
Please install these two before starting
Set current working directory via input prompt.
The accessions are stored in space-separated text file. While this is not the default way NCBI generates
accession lists, it is easier to use them. The default parameters including gzip of fastq-dump are used.
one may change fastq-dump to fasterq-dump, but the latter doesnot support automated compression.
****************************PARAMETERS******************************************************************
wd              The working directory
infile          File with space-separated list of SRA accession ids
ids             Output of get_ids containing SRA ids as list.
start,end       Index in the ids list to denote which subset of ids to be downloaded
outfile,fname   Name of output script file(s) enclosed in ''
cpus            Number of CPUs to run SHOVILL.Default: 8
depth           Maximum depth to be used for SHOVILL. Default: 100
ext             Extension for the shovill output folder. Default: _shovill"""

import os

wd = input("Enter the working directory: ")
os.chdir("{}".format(wd))
print("Directory set to: {}".format(wd))


def get_ids(infile):
    with open(infile, 'r') as f1:
        accs = f1.readlines()[0]
        #print(accs)
        outvar = [i.rstrip() for i in accs.split(" ")]
        return outvar


def sra_script_gen(wd, ids, start, end, outfile):
    with open(outfile, 'w', newline='\n', encoding='utf-8') as f2:
        for acc in ids[start:end + 1]:
            cmd1 = "/home/sujatha/sratoolkit.2.11.3-centos_linux64/bin/prefetch {}".format(acc) + '\n'
            cmd2 = "/home/sujatha/sratoolkit.2.11.3-centos_linux64/bin/fastq-dump --split-files " \
                   "--gzip {}/{}/{}.sra".format(wd, acc, acc) + '\n'
            f2.write(cmd1)
            f2.write(cmd2)

    return f2


def shovill_script_gen(wd, fname, dwnld, cpus=8, depth=150, ext="_shovill"):
    with open(fname, 'w', newline='\n', encoding='utf-8') as f3:
        for id in dwnld:
            acc_f = id + "_1.fastq.gz"
            acc_r = id + "_2.fastq.gz"
            od = id + ext
            cmd1 = "singularity exec /home/sujatha/shovill.sif shovill --trim --depth {} --R1 {}/{} --R2 {}/{} " \
                   "--outdir {}/{} --cpus 24".format(depth, wd, acc_f, wd, acc_r, wd, od) + "\n"
            f3.write(cmd1)
            cmd2 = "cp {}/{}/contigs.fa {}/{}_contigs.fasta".format(wd, od, wd, id) + "\n"
            f3.write(cmd2)
    return f3
