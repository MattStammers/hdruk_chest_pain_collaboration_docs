# import pandas 
from pandas import DataFrame, concat
from params import phentoypes_dictionary
from utilities.processing_steps import mapper

def main():
    df_out = DataFrame()
    for key in phentoypes_dictionary.keys():
        try:
            aux = mapper(key)
            df_out = concat([df_out,aux])
        except:
            pass

    df_out.to_csv("./hdruk_chest_pain_collaboration_docs/datafiles/snomed_phenotypes.csv")

if __name__ == '__main__':
    main()