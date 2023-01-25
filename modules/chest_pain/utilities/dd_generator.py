from pandas import DataFrame, Series, read_csv
from json import loads
from urllib.request import urlopen
from flatten_json import flatten 
from black import format_file_contents, FileMode

def generate_dd_pheno(phenotypes_dictionary,mappings_icd10_snomed_path):

    """
    This function is used to obtain the codes from the phenotypes listed at the protocol producting a dictionary
    with the category, the subcategory and the mapping systems used.
   
    """
    mapping_icd10_snomed = read_csv(mappings_icd10_snomed_path)
    out = {}
    aux_result = []
    for k, v in phenotypes_dictionary.items():
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
                    members_icd10 = [
                    i
                    for i in df_phenotype[df_phenotype.category==subcat].icd10_code.astype(str).drop_duplicates().values
                    ]
                    members_snomed = [
                    int(i)
                    for i in df_phenotype[df_phenotype.category==subcat].snomed_concept_id.astype(str).astype(float).drop_duplicates().values
                    ]
                    aux_result = [{"mapping_system":"icd_10","members":members_icd10},{"mapping_system":"snomed","members":members_snomed}]
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
                    members_icd10 = [
                    i
                    for i in df_phenotype[df_phenotype.category==subcat].icd10_code.astype(str).drop_duplicates().values
                    ]
                    members_snomed = [
                    int(i)
                    for i in df_phenotype[df_phenotype.category==subcat].snomed_concept_id.astype(str).astype(float).drop_duplicates().values
                    ]
                    aux_result = [{"mapping_system":"icd_10","members":members_icd10},{"mapping_system":"snomed","members":members_snomed}]
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
        #line = line.replace('(','').replace(')','')  
        dd_py += line        

    dd_py = format_file_contents(dd_py, fast=True, mode=FileMode())
    with open("./modules/chest_pain/data/dd.py", "wt") as f:
        f.write(dd_py)

    print("Successfully created black formatted dd.py")

    print(dd_py)
        
    
def generate_dd_opcs(opcs_dictionary, mappings_snomed_opcs_path):
        mapping_opcs_snomed = read_csv(mappings_snomed_opcs_path)
        out = {}
        aux_dic_list = []
        for k, v in opcs_dictionary.items():
            aux_dic = {}
            aux = DataFrame(v, columns = ["opcs_term"])
            aux.opcs_term = aux.opcs_term.str.replace(".","",regex=True)
            aux_merge = aux.merge(mapping_opcs_snomed[["opcs_term","snomed_concept_id"]], on = "opcs_term")
            members_opcs = [
            i
            for i in aux_merge.opcs_term.drop_duplicates().values
            ]
            members_snomed = [
            int(i)
            for i in aux_merge.snomed_concept_id.drop_duplicates().values
            ]
            aux_dic = [{"mapping_system":"icd_10","members":members_opcs},{"mapping_system":"snomed","members":members_snomed}]
            aux_dic_list.append(aux_dic)

            out[k] = {"mapping": aux_dic_list}
    
        dd_opcs = ""
        for k, v in out.items():
            line = f"{k} = {v}\n\n"
            # replace non-ascii characters
            line = line.encode(encoding="ascii", errors="replace").decode().replace("?", "")
            dd_opcs += line        

        dd_opcs = format_file_contents(dd_opcs, fast=True, mode=FileMode())
        with open("./modules/chest_pain/data/dd_opcs.py", "wt") as f:
            f.write(dd_opcs)

        print("Successfully created black formatted dd_opcs.py")

        print(dd_opcs)

def generate_dd_icd10(icd10_dictionary, mappings_icd10_snomed_path):
        mapping_icd10_snomed = read_csv(mappings_icd10_snomed_path)
        out = {}
        aux_dic = {}
        aux_dic_list = []
        for k, v in icd10_dictionary.items():
            aux = DataFrame(v, columns = ["icd10_code"])
            aux_merge = aux.merge(mapping_icd10_snomed[["icd10_code","snomed_concept_id"]], on = "icd10_code")
            mapping_icd10_snomed["icd10_term"] = mapping_icd10_snomed.icd10_code.apply(lambda x: x[0:3])
            if(aux_merge.size == 0):
                aux_merge = aux.merge(mapping_icd10_snomed[["icd10_code","snomed_concept_id", "icd10_term"]],left_on = "icd10_code", right_on = "icd10_term" )         
                aux_merge = aux_merge.rename(columns = {"icd10_term":"icd10_code"})
            members_icd10 = [
            i
            for i in aux_merge.icd10_code.drop_duplicates().values
            ]
            members_snomed = [
            int(i)
            for i in aux_merge.snomed_concept_id.drop_duplicates().values
            ]
            aux_dic = [{"mapping_system":"icd_10","members":members_icd10},{"mapping_system":"snomed","members":members_snomed}]
            aux_dic_list.append(aux_dic)
            out[k] = {"mapping": aux_dic_list}
    
        dd_icd10 = ""
        for k, v in out.items():
            line = f"{k} = {v}\n\n"
            # replace non-ascii characters
            line = line.encode(encoding="ascii", errors="replace").decode().replace("?", "")
            dd_icd10 += line        

        dd_icd10 = format_file_contents(dd_icd10, fast=True, mode=FileMode())
        with open("./modules/chest_pain/data/dd_icd10.py", "wt") as f:
            f.write(dd_icd10)

        print("Successfully created black formatted dd_icd10.py")

        print(dd_icd10)
