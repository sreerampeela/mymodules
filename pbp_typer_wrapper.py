script = open("pbptyper_script2.txt",'w',newline='\n',encoding='utf-8')
ids = ["990666",'2000157','990749','2000164','2000163','2000165','2000182','2000185','2000213','2000188']
print(len(ids))
for i in ids:
    seq_file = i + ".faa"
    cmd = "echo {} >> results.tab".format(i) + '\n'
    script.write(cmd)
    for db in ['spn_pbp1a_db', 'spn_pbp2b_db', 'spn_pbp2x_db']:
        gene = db.split("_")[1]
        outfile = i + gene + ".txt"
        cmd1 = "blastp -db {} -query ../contigs/{} -outfmt 6 | sort -k12,12 -nr -k3,3 -k4,4 | " \
               "head -n 1 >> results.tab".format(db,seq_file,i) + '\n'
        script.write(cmd1)
        

script.close()
