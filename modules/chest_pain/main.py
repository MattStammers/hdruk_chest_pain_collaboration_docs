# import pandas 
from params import phentoypes_dictionary, icd10_dictionary, opcs_dictionary
from utilities.dd_generator import *

def main():
    generate_dd_pheno(phentoypes_dictionary,"./datafiles/mappings_icd10.csv")
    generate_dd_icd10(icd10_dictionary,"./datafiles/mappings_icd10.csv")
    generate_dd_opcs(opcs_dictionary,"./datafiles/mappings_opcs.csv")

if __name__ == '__main__':
    main()