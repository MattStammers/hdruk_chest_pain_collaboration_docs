## Data Models

This area contains the key documentation pertaining to the desired data models for the project. 

Below is a summary of the key items for the project

###	Linked individual patient level data

#### Essential data 
1. Demographics 
- Age (number [%] <40 years, 40-49, 50-59, 60-69, 70-79, 80-89, >90 years)
- Sex (number [%] women)
2. Laboratory data
- First cardiac troponin concentration (number [%] <5 ng/L, 5 ng/L to URL, above URL)
- Maximum cardiac troponin concentration in 24 hours (number [%] <5 ng/L, 5 ng/L to URL, above URL)
- Serial cardiac troponin measurments (number [%] 1, 2, 3 or more)
3. Index diagnosis
- SNOMED codes for Emergency Department (provisional diagnosis)
- ICD-10 codes for hospital discharge (final diagnosis)
4. Outcomes
- Proportion discharged directly from Emergency Department (number [%])
- Myocardial infarction or cardiac death 30 days from discharge (number [%])
- Duration of index hospital stay (number [%])(<2 hours, 2-4 hours, 5-24 hours, 25-48 hours, 49-72 hours, 73-96 hours, 97-120 hours, 121-144 hours, >145 hours)
- Any non-elective reattendance within 30 days of discharge (number [%])

#### Desirable data 
1. Demographics 
- Ethnicity (number [%] of patients stratified by census ethnic grouping: White, Mixed or multiple ethnic groups, Asian or Asian British, Black or Black Caribbean or African, Other, Unknown)
- Social and economic deprivation (number [%] by Scottish Index of Multiple Deprivation [SIMD] score in Scotland or Townsend Deprivation score in England by quintiles)
2. Cardiovascular risk factors from GP Read or SNOMED codes 
- Smoking status (number [%] current, former, non, e-cigarette)
- Diabetes mellitus (number [%] yes or no)
- Hypertension (number [%] yes or no)
- Hyperlipidemia (number [%], prescription of a lipid lowering therapy)
- Past medical history from HES or SMR01 and or GP Read codes (lifetime look back)
- Previous myocardial infarction (number [%], yes or no)
- Previous coronary revascularisation (number [%], yes or no)
- Heart failure (number [%], yes or no)
- Cerebrovascular disease (number [%], yes or no)
3. Laboratory data
- First estimated glomerular filtration rate (number [%] <30, 30 to 60, above 60)
4. Outcomes
- Myocardial infarction within 30 days of discharge (number [%])
- Cardiac death within 30 days of discharge (number [%])
- Cardiovascular death within 30 days of discharge (number [%])
- All cause death within 30 days of discharge (number [%])
- Coronary angiography during index presentation or within 30 days of discharge (number [%])
- PCI or CABG during index presentation or within 30 days of discharge (number [%])

#### Aspirational data 
1. Investigations
- Electrocardiogram (number [%])
- Exercise tolerance test (number [%])
- CT coronary angiogram (number [%])
- Echocardiogram (number [%])
- Treatment
- New prescription for anti-platelet drug (number [%])
- New prescription for lipid lowering therapy (number [%]) 
2. Follow up
- GP attendance within 30 days of discharge (number [%]) 
- Outpatient appointment within 30 days (number [%])

### Full Data Dictionary 

|Measure	Source	Definition	Codelists / Rules|
|:----|
|Attendance with possible myocardial infarction	Laboratory data	Measured hs-cTn within 24 hours of Emergency admission (ED or AMRU that accepts urgent assessments)	Classification by presence or absence of myocardial injury (any hs-cTn >99th centile upper reference limit [URL] within 24 hours of attendance) and into risk groups as low (<5 ng/L) or intermediate (5 ng/L to URL) risk in those without myocardial injury.Risk factor – hypertension	Primary and secondary care	HDR UK phenotype – distinguishes hypertension| secondary hypertension and history of hypertension 	(https://phenotypes.healthdatagateway.org/phenotypes/PH189/version/378/detail/Risk) factor – smoking	Primary care	HDR UK phenotype classifying Non-smoker| Ex-smoker or current smoker	(https://www.caliberresearch.org/portal/show/)smoking_status_gprdRisk factor – lipids	Prescribing 	Any lipid lowering therapy prescribed in 6 months prior to attendance	BNF Section 0212: Lipid-regulating drugs|
|Risk factor - ethnicity	Primary and secondary care	Combined sourcing of any record of ethnicity using Census high-level grouping	Classification: White| Mixed or multiple ethnic groups| Asian or Asian British| Black or Black Caribbean or African| Other| Unknown|
|Risk factor – diabetes	Primary and secondary care	HDR UK phenotype – any code (no time limit)	https://phenotypes.healthdatagateway.org/phenotypes/PH152/version/304/detail/|
|History of myocardial infarction	Primary and secondary care	HDR UK phenotype – any code (no time limit)	https://phenotypes.healthdatagateway.org/phenotypes/PH215/version/430/detail/|
|History of heart failure	Primary and secondary care	HDR UK phenotype – any code (no time limit)	https://phenotypes.healthdatagateway.org/phenotypes/PH182/version/364/detail/|
|History of cerebrovascular disease	Primary and secondary care	Any of 2 HDR UK phenotypes (stroke or ischaemic stroke) – any code (no time limit)	(https://phenotypes.healthdatagateway.org/phenotypes/PH85/version/170/detail/) (https://phenotypes.healthdatagateway.org/phenotypes/PH56/version/112/detail/History of coronary revascularisation)	Secondary care OPCS or local cardiac procedure database	Lookback for any prior code (no time limit)	PCI procedure: K49| K49.1| K49.2| K49.3| K49.4| K49.8| K49.9| K50| K50.1| K50.4| K50.8| K50.9| K75| K75.1| K75.2| K75.3| K75.4| K75.8| K75.9|
|Coronary bypass grafting: K40.| K41.| K42.| K43.| K44.|
|Duration of stay	Secondary care	Time (hours) from attendance to discharge or death 	Discharge is defined by time leaving ED discharge if not admitted| or inpatient discharge time if admitted.|
|Any reattendance	Secondary care	Any non-elective attendance to either an Emergency Department or hospital inpatient episode	N/A|
|Reattendance with myocardial infarction	Secondary care	Any hospital episode with relevant ICD-10 code in position 1 or 2 of admission record	ICD-10 codes: I21 and I22 including subclassifications|
|Cardiac death	Death registry	Any recorded death including relevant ICD-10 code in position 1 or 2 of record	ICD-10 codes: I05-I09| I20-I25| and I30-I51|
|Cardiovascular death	Death registry	Any recorded death including relevant ICD-10 code in position 1 or 2 of death record	ICD-10 codes: I00-I99|
|All-cause death	Death registry	Any recorded death including date of death	N/A|
|Coronary revascularisation	Secondary care OPCS codes and/or local cardiac procedure database		Angiography: K63.1| K63.2| K63.3| K63.4| K63.5| K63.6| K65.1| K65.2| K65.3| K65.8| K65.9|
|PCI procedure: K49| K49.1| K49.2| K49.3| K49.4| K49.8| K49.9| K50| K50.1| K50.4| K50.8| K50.9| K75| K75.1| K75.2| K75.3| K75.4| K75.8| K75.9|
|Coronary bypass grafting: K40.| K41.| K42.| K43.| K44.|
