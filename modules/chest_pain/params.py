phentoypes_dictionary = {
			"hypertension": "http://phenotypes.healthdatagateway.org/api/v1/public/phenotypes/PH189/version/378/export/codes/?format=json",
			"smoking": "http://phenotypes.healthdatagateway.org/api/v1/public/phenotypes/PH982/version/2160/export/codes/?format=json",
			"diabetes": "http://phenotypes.healthdatagateway.org/api/v1/public/phenotypes/PH152/version/304/export/codes/?format=json",
			"myocardial_infarction": "http://phenotypes.healthdatagateway.org/api/v1/public/phenotypes/PH215/version/430/export/codes/?format=json",
			"heart_failure": "http://phenotypes.healthdatagateway.org/api/v1/public/phenotypes/PH182/version/364/export/codes/?format=json",
			"stroke": "http://phenotypes.healthdatagateway.org/api/v1/public/phenotypes/PH85/version/170/export/codes/?format=json",
			"ischaemic_stroke": "http://phenotypes.healthdatagateway.org/api/v1/public/phenotypes/PH56/version/112/export/codes/?format=json"
			}

opcs_dictionary = {
			"pci_procedure" : ["K49", "K49.1", "K49.2", "K49.3","K49.4", "K49.8", "K49.9", "K50",
								"K50.1", "K50.4", "K50.8", "K50.9","K75", "K75.1", "K75.2", "K75.3", 
								"K75.4", "K75.8", "K75.9"],
			"coronary_bypass_grafting" : ["K49", "K49.1", "K49.2", "K49.3","K49.4", "K49.8", "K49.9", "K50",
											"K50.1", "K50.4", "K50.8", "K50.9","K75", "K75.1", "K75.2", "K75.3", 
											"K75.4", "K75.8", "K75.9"],
            "angiography" : ["K63.1", "K63.2", "K63.3", "K63.4", "K63.5", "K63.6", "K65.1", "K65.2", "K65.3", "K65.8", "K65.9" ]
			}

icd10_dictionary = {
			  "cardiovascular_death" : ["I00","I01","I02","I03","I04","I05","I06","I07","I08","I09","I10","I11","I12",
                             		"I13","I14","I15","I16","I17","I18","I19","I20","I21","I22","I23","I24","I25","I26","I27",
									"I28","I29","I30","I31","I32","I33","I34","I35","I36","I37","I38","I39","I40","I41","I42","I43",
									"I44","I45","I46","I47","I48","I49","I50","I51","I52","I53","I54","I55","I56","I57","I58","I59",
									"I60","I61","I62","I63","I64","I65","I66","I67","I68","I69","I70","I71","I72","I73","I74","I75",
                                    "I76","I77","I78","I79","I80","I81","I82","I83","I84","I85","I86","I87","I88","I89","I90","I91",
									"I92","I93","I94","I95","I96","I97","I98","I99"],
                "cardiac_death" : ["I05","I06","I07","I08","I09","I20","I21","I22","I23","I24","I25","I30","I31","I32","I33","I34",
                                   "I35","I36","I37","I38","I39","I40","I41","I42","I43","I44","I45","I46","I47","I48","I49","I50","I51"]
				}