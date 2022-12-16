# script to download networks from STRING using API
import os
import subprocess
import requests
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

# CLUSTERING HYPOTHETICAL PROTEINS
def cluster_proteins(prot_seqs_files):
    """To cluster hypothetical protein sequences. Input is a list of fasta files"""
    all_prots = []
    for fasta in prot_seqs_files:
        records = SeqIO.parse(fasta,"fasta")
        for record in records:
            seqrec = SeqRecord(record.seq,id=record.id)
            all_prots.append(seqrec)
            
    with open("total_prots.fasta",'a') as fout:
        for rec in all_prots:
            SeqIO.write(rec,fout,"fasta")
    cmd = f"/mnt/d/cd-hit-v4.8.1-2019-0228/cd-hit -i total_prots.fasta -o spn_clustered_prots.fasta -c 0.9 -T 4 -p 1" #add full path to CD-HIT
    print("Starting clustering of proteins...")
    os.system(cmd)


def get_string_network(fname):
    """Imports the STRING network via API for the sequences in fname File"""
    string_api_url = "https://version-11-5.string-db.org/api"
    output_format = "tsv-no-header"
    method = "interaction_partners"
    request_url = "/".join([string_api_url, output_format, method])

    records = SeqIO.parse(fname,"fasta")
    for record in records:
        string_id = record.id
        print(string_id)
        params = {
            "identifiers" : string_id, 
            "species" : 2, 
            "caller_identity" : "srirambds.murthy@gmail.com", #specify email/app name
            "required_score" : 700 # specify score
        }
        response = requests.post(request_url, data=params)
        with open("string_interactions.tab",'a') as fout:
            fout.write(response.text)
        print(f"Written protein interactions for {string_id}")
        os.system("sleep 10") #timeout 10 for windows systems
