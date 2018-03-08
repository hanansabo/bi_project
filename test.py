import sklearn
import io
import os
import numpy as np
import pandas as pd


def read_vcf(path):
    with open(path, 'r') as f:
        lines = [l for l in f if not l.startswith('##')]
    return pd.read_table(
        io.StringIO(str.join(os.linesep, lines)),
        dtype={'#CHROM': str, 'POS': int, 'ID': str, 'REF': str, 'ALT': str,
               'QUAL': str, 'FILTER': str, 'INFO': str}
    ).rename(columns={'#CHROM': 'CHROM'})


if __name__ == '__main__':
    data = read_vcf("test_sample.vcf")
    headers = ["CAGI2012_CD_01", "CAGI2012_CD_02", "CAGI2012_CD_03", "CAGI2012_CD_04", "CAGI2012_CD_05",
               "CAGI2012_CD_06", "CAGI2012_CD_07", "CAGI2012_CD_08", "CAGI2012_CD_09", "CAGI2012_CD_10",
               "CAGI2012_CD_11", "CAGI2012_CD_12", "CAGI2012_CD_13", "CAGI2012_CD_14", "CAGI2012_CD_15",
               "CAGI2012_CD_16", "CAGI2012_CD_17", "CAGI2012_CD_18", "CAGI2012_CD_19", "CAGI2012_CD_20",
               "CAGI2012_CD_21", "CAGI2012_CD_22", "CAGI2012_CD_23", "CAGI2012_CD_24", "CAGI2012_CD_25",
               "CAGI2012_CD_26", "CAGI2012_CD_27", "CAGI2012_CD_28", "CAGI2012_CD_29", "CAGI2012_CD_30",
               "CAGI2012_CD_31", "CAGI2012_CD_32", "CAGI2012_CD_33", "CAGI2012_CD_34", "CAGI2012_CD_35",
               "CAGI2012_CD_36", "CAGI2012_CD_37", "CAGI2012_CD_38", "CAGI2012_CD_39", "CAGI2012_CD_40",
               "CAGI2012_CD_41", "CAGI2012_CD_42", "CAGI2012_CD_43", "CAGI2012_CD_44", "CAGI2012_CD_45",
               "CAGI2012_CD_46", "CAGI2012_CD_47", "CAGI2012_CD_48", "CAGI2012_CD_49", "CAGI2012_CD_50",
               "CAGI2012_CD_51", "CAGI2012_CD_52", "CAGI2012_CD_53", "CAGI2012_CD_54", "CAGI2012_CD_55",
               "CAGI2012CD_56", "CAGI2012_CD_57", "CAGI2012_CD_58", "CAGI2012_CD_59", "CAGI2012_CD_60",
               "CAGI2012_CD_61", "CAGI_2012_CD_62", "CAGI2012_CD_63", "CAGI2012_CD_64", "CAGI2012_CD_65",
               "CAGI2012_CD_66"]
    all_GTs= pd.DataFrame()
    for header in headers:
        extracted = data[header].str.split(':').str[0]
        #extracted=list(extracted)
        all_GTs.append(extracted.to_frame(name=header))
    all_GTs= pd.DataFrame(all_GTs)
    print(all_GTs)
    print("dont forget to delete me")
