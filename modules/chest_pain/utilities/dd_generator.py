from chest_pain.params import phentoypes_dictionary
from pandas import DataFrame, Series, read_csv
from json import loads
from urllib.request import urlopen
from flatten_json import flatten 
from black import format_file_contents, FileMode

# loading df with icd10, read code v2, v3



def generate_dd():

    """
    This function is used to obtain the codes from the phenotypes listed at the protocol producting a dictionary
    with the category, the subcategory and the mapping systems used.

    Args:
        
    Returns:
        A dataframe
    Example:
    df = mapper(
                phenotype = 'hypertension'
                )
    """
    mapping_icd10_snomed = read_csv(". /hdruk_chest_pain_collaboration_docs/datafiles/mappings_icd10.csv")
    out = {}
    aux_result = []
    for k, v in phentoypes_dictionary.items():
            response = urlopen(v)
            data_json = loads(response.read())
            df = DataFrame(data_json)
            aux_dic_list = []
            aux_dic = {}
            if(df[df.coding_system == "ICD10 codes"].size):
                #getting ICD10 codes, df preparation
                df = df[df.coding_system == "ICD10 codes"]
                df["code"] = df.code.str.replace(".","",regex = True)
                df = df.rename(columns = {"code":"icd10_code","concept_id":"concept_id_ph","concept_version_id":"concept_version_id_ph","description":"description_ph"})
                df[["disease","category"]]=df['code_attributes'].apply(flatten).apply(Series)
                # merging icd10, snomed df with icd10, phenotype
                mapping_icd10_snomed["icd10_term"] = mapping_icd10_snomed.icd10_code.apply(lambda x: x[0:3])
                df_phenotype = mapping_icd10_snomed.merge(df[["icd10_code","category","concept_id_ph","concept_version_id_ph","phenotype_id","phenotype_version_id","phenotype_name","disease", "description_ph"]], on = "icd10_code")    
                if(df_phenotype.size == 0):
                    df_phenotype = mapping_icd10_snomed.merge(df[["icd10_code","category","concept_id_ph","concept_version_id_ph","phenotype_id","phenotype_version_id","phenotype_name","disease", "description_ph"]], left_on = "icd10_term" ,right_on = "icd10_code")         
                    df_phenotype = df_phenotype.rename(columns = {"icd10_term":"icd10_code"})
                for subcat in df_phenotype.category.drop_duplicates().values:
                    aux_result.append({"mapping":"icd_10","members":df_phenotype[df_phenotype.category==subcat].icd10_code.drop_duplicates().values})
                    aux_result.append({"mapping":"snomed","members":df_phenotype[df_phenotype.category==subcat].snomed_concept_id.drop_duplicates().values})
                    aux_dic[subcat] = aux_result
                    aux_dic_list.append(aux_dic)
                    aux_dic = {}
                    aux_result = []
            elif(df[df.coding_system == "SNOMED  CT codes"].size):
                df = df.rename(columns = {"code":"snomed_concept_id","concept_id":"concept_id_ph","concept_version_id":"concept_version_id_ph","description":"description_ph"})
                df["disease"] = ""
                df["category"] = df["concept_name"]
                mapping_icd10_snomed.snomed_concept_id = mapping_icd10_snomed.snomed_concept_id.astype(str)
                df_phenotype = mapping_icd10_snomed.merge(df[["snomed_concept_id","category","concept_id_ph","concept_version_id_ph","phenotype_id","phenotype_version_id","phenotype_name","disease", "description_ph"]], on = "snomed_concept_id")
                for subcat in df_phenotype.category.drop_duplicates().values:
                    aux_result.append({"mapping":"icd_10","members":df_phenotype[df_phenotype.category==subcat].icd10_code.drop_duplicates().values})
                    aux_result.append({"mapping":"snomed","members":df_phenotype[df_phenotype.category==subcat].snomed_concept_id.drop_duplicates().values})
                    aux_dic[subcat] = aux_result
                    aux_dic_list.append(aux_dic)
                    aux_dic = {}
                    aux_result = []
            out[k] = {"url": v, "mapping": aux_dic_list}    
    
    dd_py = ""
    for k, v in out.items():
        line = f"{k} = {v}\n\n"
        # replace non-ascii characters
        line = line.encode(encoding="ascii", errors="replace").decode().replace("?", "")
        dd_py += line        

    dd_py = format_file_contents(dd_py, fast=True, mode=FileMode())
    with open("../data/dd.py", "wt") as f:
        f.write(dd_py)

    print("Successfully created black formatted nhsdd.py")

    print(dd_py)
        
    return df_phenotype

if __name__ == "__main__":
    # generate_ndd()

    print(
        "Generating avoidable_admissions/data/nhsdd.py and avoidable_admissions/data/nhsdd_snomed.py"
    )
    generate_dd()