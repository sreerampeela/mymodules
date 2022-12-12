import os
os.chdir("D:/kims_2021/ghru_contigs/reordered_contigs")
# files = os.listdir()
# print(type(files))
file_names = "ERR2090225,ERR3227834,ERR4784551,ERR4784667,ERR4784547,ERR4784688,ERR4784684,ERR4784692,ERR4784605,ERR3227765," \
            "ERR4784676,ERR4784696,SRR8879299,ERR3227775,ERR3227773,ERR3227779,ERR3227784,ERR3227767,ERR3227746,SRR8879297," \
            "SRR8879296,ERR3227783,ERR3227781,SRR8879298,ERR3227771,CRL_SPN_03_S2_L001,CRL_SPN_07_S4_L001,CRL_SPN_02_S1_L001," \
            "CRL_SPN_06_S3_L001,SPN4_S44_L001,CRL_SPN_08_S5_L001,CRL_SPN_13_S6_L001,CRL_SPN_14_S7_L001,CRL_SPN_20_S13_L001," \
            "CRL_SPN_15_S8_L001,CRL_SPN_16_S9_L001,CRL_SPN_17_S10_L001,CRL_SPN_18_S11_L001,CRL_SPN_35_S21_L001," \
            "CRL_SPN_19_S12_L001,CRL_SPN_23_S14_L001,CRL_SPN_27_S17_L001,CRL_SPN_25_S16_L001,CRL_SPN_29_S18_L001," \
            "Spn_31_S14_L001,CRL_SPN_32_S19_L001,Spn_28_S13_L001,CRL_SPN_33_S20_L001,CRL_SPN_42_S22_L001,CRL_SPN_43_S23_L001," \
            "CRL_SPN_46_S25_L001,Spn_44_S22_L001,CRL_SPN_45_S24_L001,CRL_SPN_59_S31_L001,CRL_SPN_60_S32_L001," \
            "CRL_SPN_61_S33_L001,CRL_SPN_62_S34_L001,CRL_SPN_53_S26_L001,spn_52_S25_L001,CRL_SPN_56_S28_L001," \
            "CRL_SPN_57_S29_L001,spn_55_S26_L001,CRL_SPN_54_S27_L001,CRL_SPN_58_S30_L001,CRL_SPN_66_S35_L001,CRL_SPN_69_S38_L001," \
            "CRL_SPN_68_S37_L001,CRL_SPN_67_S36_L001,Spn_81_S16_L001,Spn_80_S15_L001,Spn_79_S18_L001,Spn_82_S17_L001," \
            "CRL_SPN_77_S40_L001,CRL_SPN_78_S41_L001,CRL_SPN_76_S39_L001".split(",")
sample_names = "SF1916,SF1927,3277,3690,6487,2585,1192,2445,A308,EX3714,P276,6800,1453,927,SF4850,P766,P20011,A2258," \
               "A1645,P924,SF621,A1917,P776,7484,7861,5066,4998,B23927,B21333,B21699,SF5006,126,415,500,664,1801,1862," \
               "2061,2101,2220,EX4584,SF2320,B12510,3069,2285,B14465,2343,3668,EX7831,4267,4075,4249,4167,6178,4800,5118," \
               "5993,5515,5088,5926,6036,B25182,B25147,SF5143,6234,6494,6414,SF5506,7044,7079,B29157,7193,SF6046," \
               "B28457,EX11768".split(",")
script_file = open("prokka_wrapper2.sh",'w',encoding='utf-8',newline='\n')
print(len(sample_names),len(file_names))
for i in range(len(file_names)):
    file_id = file_names[i] + ".fasta"
    sample_id = sample_names[i]
    print(file_id,sample_id)
    cmd = f"sudo docker run -v $PWD:/data staphb/prokka prokka --prefix {sample_id} --addgenes --centre KIMS " \
          f"--genus Streptococcus --species pneumoniae --strain {sample_id} " \
          f"--cpus 8 --rfam /data/{file_id}" + '\n'
    print(cmd)
    script_file.write(cmd)


script_file.close()
