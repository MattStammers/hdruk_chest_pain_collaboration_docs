from pandas import DataFrame, Series, read_csv
from json import loads
from urllib.request import urlopen
from flatten_json import flatten 

# loading df with icd10, read code v2, v3
mapping_icd10_snomed = read_csv('./hdruk_chest_pain_collaboration_docs/datafiles/mappings_icd10.csv',index_col=0)
mapping_icd10_snomed["icd10_code"] = mapping_icd10_snomed["icd10_term"].apply(lambda x: x[0:3])
mapping_icd10_snomed["snomed_concept_id"] = mapping_icd10_snomed["snomed_concept_id"].astype(str)
phentoypes_dictionary = {
			"hypertension": "http://phenotypes.healthdatagateway.org/api/v1/public/phenotypes/PH189/version/378/export/codes/?format=json",
			"smoking": "http://phenotypes.healthdatagateway.org/api/v1/public/phenotypes/PH982/version/2160/export/codes/?format=json",
			"diabetes": "http://phenotypes.healthdatagateway.org/api/v1/public/phenotypes/PH152/version/304/export/codes/?format=json",
			"myocardial_infarction": "http://phenotypes.healthdatagateway.org/api/v1/public/phenotypes/PH215/version/430/export/codes/?format=json",
			"heart_failure": "http://phenotypes.healthdatagateway.org/api/v1/public/phenotypes/PH182/version/364/export/codes/?format=json",
			"stroke": "http://phenotypes.healthdatagateway.org/api/v1/public/phenotypes/PH85/version/170/export/codes/?format=json",
			"ischaemic_stroke": "http://phenotypes.healthdatagateway.org/api/v1/public/phenotypes/PH56/version/112/export/codes/?format=json"
			}

def mapper(phenotype: str):

  """
  This function receives an phenotype from the ones listed at the protocol and returns a 
  merged dataframe with codes from different systems (icd10, med codes, phenotype and snomed).
  Args:
      
  Returns:
      A dataframe
  Example:
    df = mapper(
                phenotype = 'hypertension'
                )
  """
  url = phentoypes_dictionary [phenotype]
  response = urlopen(url)
  # storing the JSON response 
  data_json = loads(response.read())
  # converting to pandas df
  df = DataFrame(data_json)
  
  if(df[df.coding_system == "ICD10 codes"].size):
    #getting ICD10 codes, df preparation
    df = df[df.coding_system == "ICD10 codes"]
    df = df.rename(columns = {"code":"icd10_code","concept_id":"concept_id_ph","concept_version_id":"concept_version_id_ph","description":"description_ph"})
    df[["disease","category"]]=df['code_attributes'].apply(flatten).apply(Series)
    # merging icd10, snomed df with icd10, phenotype
    df_phenotype = mapping_icd10_snomed.merge(df[["icd10_code","category","concept_id_ph","concept_version_id_ph","phenotype_id","phenotype_version_id","phenotype_name","disease", "description_ph"]], on = "icd10_code")
  elif(df[df.coding_system == "SNOMED  CT codes"].size):
    df = df.rename(columns = {"code":"snomed_concept_id","concept_id":"concept_id_ph","concept_version_id":"concept_version_id_ph","description":"description_ph"})
    df["disease"] = ""
    df["category"] = ""
    df_phenotype = mapping_icd10_snomed.merge(df[["snomed_concept_id","category","concept_id_ph","concept_version_id_ph","phenotype_id","phenotype_version_id","phenotype_name","disease", "description_ph"]], on = "snomed_concept_id", how = "left")
  return df_phenotype