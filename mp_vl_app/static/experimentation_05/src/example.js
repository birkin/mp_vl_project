const schema = {
    "$schema":"http://json-schema.org/draft-07/schema",
    "$id": "http://mappingviolence.com/schemas/poi_schema.json",
    "type": "object",
    "properties": {
        "id": {"type":"string"},
        "title": {"type":"string"}, // field also called "name"
        "eventCategory": {
            "type": "string",
            "enum": ["Event that Triggered Racial Violence", "Racial Violence", "Anti-Violence Advocacy"],
        },
        "description": {"type":"string"},
        "location": {"type":"string"},
        "latitude": {"type":"number"},
        "longitude": {"type":"number"},
        "locationRationale": {"type":"string"},
        "date": {
            "type": "object",
            "properties": {
                "year": {"type":"integer"},
                "month": {"type":"integer"},
                "day": {"type":"integer"},
                "modifier": {
                    "type": "string",
                    "enum": ["Early", "Mid", "Late", "Around"]
                }
            }
        },
        "aggressors": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "race": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "enum": [
                                "Unknown",
                                "African American",
                                "White",
                                "Indian", 
                                "Chinese",
                                "Japanese",  
                                "Filipinos",
                                "Hindus",
                                "American Indian",
                                "Other"
                            ]
                        }
                    },
                    "ethnicity": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "enum": [
                                "Unknown",
                                "Austria",
                                "Belgium",
                                "Canada-French",
                                "Canada - Other",
                                "Denmark",
                                "England",
                                "France",
                                "Germany",
                                "Greece",
                                "Holland",
                                "Hungary",
                                "Ireland",
                                "Italy",
                                "Mexico",
                                "Norway",
                                "Roumania",
                                "Russia",
                                "Scotland",
                                "Spain",
                                "Sweden",
                                "Switzerland",
                                "Turkey in Asia",
                                "Turkey in Europe",
                                "Wales",
                                "Other",
                                "American Indian (list nation as additional entry if known)",
                            ]
                        }
                    },
                    "nationality": {
                        "type": "string",
                        "enum": [
                            "Unknown",
                            "Austria",
                            "Belgium",
                            "Canada-French",
                            "Canada - Other",
                            "Denmark",
                            "England",
                            "France",
                            "Germany",
                            "Greece",
                            "Holland",
                            "Hungary",
                            "Ireland",
                            "Italy",
                            "Mexico",
                            "Norway",
                            "Roumania",
                            "Russia",
                            "Scotland",
                            "Spain",
                            "Sweden",
                            "Switzerland",
                            "Turkey in Asia",
                            "Turkey in Europe",
                            "Wales",
                            "Other",
                            "American Indian (list nation as additional entry if known)",
                        ]
                    },
                    "gender": {"type": "string"},
                    "maritalStatus": {
                        "type": "string",
                        "enum": [
                            "Unknown",
                            "Single",
                            "Married",
                            "Widowed",
                            "Divorced",
                        ]
                    },
                    "occupation": {
                        "type": "string",
                        "enum": [
                            "Stock Raising laborer",
                            "Agricultural laborer",
                            "Railroad",
                            "Mine laborer",
                            "Quarry laborer",
                            "Construction",
                            "Farmer - agriculture",
                            "Teacher",
                            "Lawyer",
                            "Rancher - stock raising",
                            "Texas Ranger",
                            "Sheriff",
                            "Local law enforcement",
                            "Federal agent",
                            "US Border Patrol",
                            "Prison Guard",
                            "Cattle brand inspector",
                            "Bread and other bakery products",
                            "Brick and tile",
                            "Cars and shop construction and repairs by steam-railroad companies",
                            "Cotton goods",
                            "Flour mill and grist mill products",
                            "Food preparation",
                            "Foundry and machine shop products",
                            "Gas, illuminating, and heating",
                            "Ice, manufactured",
                            "Leather Goods",
                            "Liquors malt",
                            "Lumber and timber products",
                            "Oil, cottonseed, and cake",
                            "Printing and publishing",
                            "Rice, cleaning and polishing",
                            "Slaughtering and meat packing",
                            "Other"
                        ]
                    },
                    "age": {"type": "string"},
                    "literacy": {
                        "type": "string",
                        "enum": [
                            "Unknown",
                            "Can Read",
                            "Can Write",
                            "Cannot Read",
                            "Cannot Write",
                        ]
                    },
                }
            }
        },
        "victims": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "race": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "enum": [
                                "Unknown",
                                "African American",
                                "White",
                                "Indian", 
                                "Chinese",
                                "Japanese",  
                                "Filipinos",
                                "Hindus",
                                "American Indian",
                                "Other"
                            ]
                        }
                    },
                    "ethnicity": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "enum": [
                                "Unknown",
                                "Austria",
                                "Belgium",
                                "Canada-French",
                                "Canada - Other",
                                "Denmark",
                                "England",
                                "France",
                                "Germany",
                                "Greece",
                                "Holland",
                                "Hungary",
                                "Ireland",
                                "Italy",
                                "Mexico",
                                "Norway",
                                "Roumania",
                                "Russia",
                                "Scotland",
                                "Spain",
                                "Sweden",
                                "Switzerland",
                                "Turkey in Asia",
                                "Turkey in Europe",
                                "Wales",
                                "Other",
                                "American Indian (list nation as additional entry if known)",
                            ]
                        }
                    },
                    "nationality": {
                        "type": "string",
                        "enum": [
                            "Unknown",
                            "Austria",
                            "Belgium",
                            "Canada-French",
                            "Canada - Other",
                            "Denmark",
                            "England",
                            "France",
                            "Germany",
                            "Greece",
                            "Holland",
                            "Hungary",
                            "Ireland",
                            "Italy",
                            "Mexico",
                            "Norway",
                            "Roumania",
                            "Russia",
                            "Scotland",
                            "Spain",
                            "Sweden",
                            "Switzerland",
                            "Turkey in Asia",
                            "Turkey in Europe",
                            "Wales",
                            "Other",
                            "American Indian (list nation as additional entry if known)",
                        ]
                    },
                    "gender": {"type": "string"},
                    "maritalStatus": {
                        "type": "string",
                        "enum": [
                            "Unknown",
                            "Single",
                            "Married",
                            "Widowed",
                            "Divorced",
                        ]
                    },
                    "occupation": {
                        "type": "string",
                        "enum": [
                            "Stock Raising laborer",
                            "Agricultural laborer",
                            "Railroad",
                            "Mine laborer",
                            "Quarry laborer",
                            "Construction",
                            "Farmer - agriculture",
                            "Teacher",
                            "Lawyer",
                            "Rancher - stock raising",
                            "Texas Ranger",
                            "Sheriff",
                            "Local law enforcement",
                            "Federal agent",
                            "US Border Patrol",
                            "Prison Guard",
                            "Cattle brand inspector",
                            "Bread and other bakery products",
                            "Brick and tile",
                            "Cars and shop construction and repairs by steam-railroad companies",
                            "Cotton goods",
                            "Flour mill and grist mill products",
                            "Food preparation",
                            "Foundry and machine shop products",
                            "Gas, illuminating, and heating",
                            "Ice, manufactured",
                            "Leather Goods",
                            "Liquors malt",
                            "Lumber and timber products",
                            "Oil, cottonseed, and cake",
                            "Printing and publishing",
                            "Rice, cleaning and polishing",
                            "Slaughtering and meat packing",
                            "Other"
                        ]
                    },
                    "age": {"type": "string"},
                    "literacy": {
                        "type": "string",
                        "enum": [
                            "Unknown",
                            "Can Read",
                            "Can Write",
                            "Cannot Read",
                            "Cannot Write",
                        ]
                    },
                }
            }
        },
        "numberOfVictims": {
            "type": "integer",
        },
        "victimCategory": {
            "type": "array",
            "items": {
                "type": "string",
                "enum": ["Unknown", "Anti-Mexican", "Anti-Black", "Anti-Asian", "Anti-American Indian", "Nativist (targeting religious or ethnic minorities)"],
            }
        },
        "aggressorCategory": {
            "type": "array",
            "items": {
                "type": "string",
                "enum": ["Unknown", "Vigilante", "Extralegal Violence", "Posse"],
            }
        },      
        "typesOfViolence": {
            "type": "array",
            "items": {
                "type": "string",
                "enum": ["Unknown", "Lynching", "Attempted Lynching", "Murder", "Rape", "Physical Assault", "Intimidation"],
            }
        },
        "caseOutcomeType": {
            "$id": "test",
            "type": "string",
            "enum": ["Disavowed or Erased Violence", "Seeking Justice"]
        },
        "caseOutcomeForDisavowedOrErasedViolence": {
            "type": "array",
            "items": {
                "type": "string",
                "enum": ["No Known Official Investigations", "No Known Arrests", "No Known Indictments", "No Known Prosecutions", "No Known Death Certificate(s)", "Media Endorses Violence", "Officials Endorse Violence"]
            }
        },
        "caseOutcomeForSeekingJustice": {
            "type": "array",
            "items": {
                "type": "string",
                "enum": [
                    "Media Condemns Violence",
                    "State Investigations",
                    "Federal Investigations",
                    "Foreign Consul Investigations",
                    "Aggressors Arrested",
                    "Aggressors Indicted",
                    "Aggressors Prosecuted",
                    "Public Protest",
                    "Armed Protest",
                    "Witness, Survivor, or Victim Testimony",
                    "Family or Witness Advocacy",
                ]
            }
        },
        "allegedCrime": {
            "type": "array",
            "items": {
                "type": "string",
                "enum": [
                    "Unknown",
                    "Banditry",
                    "Sexual assault or rape",
                    "Theft",
                    "Murder",
                    "Sedition",
                    "Escaping Arrest",
                    "Failing to Register for Draft",
                    "Other"
                ]
            }
        },
        "availableRecords": {
            "type": "array",
            "items": {
                "type": "string",
                "enum": [
                    "Newspaper Articles",
                    "Black Press",
                    "Spanish Language Press",
                    "English Press",
                    "Death Certificate",
                    "Law Enforcement Records",
                    "Consulate Records",
                    "Census Records",
                    "Federal Records",
                    "State Records",
                    "Family Records",
                    "Secondary Sources",
                    "Testimony",
                ]
            }
        },
        "womenInvolved": {
            "type": "string",
            "enum": ["Unknown", "Women were involved", "Women were not involved"]
        },
        "primarySources": {
            "type": "array",
            "items": {"type":"string"}
        },
        "secondarySources": {
            "type": "array",
            "items": {"type":"string"}
        },
        "researcherNotes": {"type":"string"},
        "metadata": {
            "type": "object",
            "properties": {
                "lastEditedBy": {
                    "type": "string"
                }
            }
        }
    },
    "required": ["id", "title", "description", "location", "latitude", "longitude"],
    "additionalProperties": false
};

const uischema = {
    "type": "VerticalLayout",
    "elements": [
        {
            "type": "Control",
            "label": "Event Category",
            "scope": "#/properties/eventCategory"
        },
        {
            "type": "Control",
            "label": "Title",
            "scope": "#/properties/title"
        },
        {
            "type": "Control",
            "label": "Description",
            "scope": "#/properties/description",
            "options": {
                "multi": true
            }
        },
        {
            "type": "Group",
            "label": "Location Information",
            "elements": [
                {
                    "type": "HorizontalLayout",
                    "elements": [
                        {
                            "type": "Control",
                            "label": "Location",
                            "scope": "#/properties/location"
                        }
                    ]
                },
                {
                    "type": "HorizontalLayout",
                    "elements": [
                        {
                            "type": "Control",
                            "label": "Latitude",
                            "scope": "#/properties/latitude"
                        },
                        {
                            "type": "Control",
                            "label": "Longitude",
                            "scope": "#/properties/longitude"
                        }
                    ]
                },
                {
                    "type": "HorizontalLayout",
                    "elements": [
                        {
                            "type": "Control",
                            "label": "Location Rationale",
                            "scope": "#/properties/locationRationale"
                        }
                    ]
                }
            ]
        },
        {
            "type": "Group",
            "label": "Date",
            "elements": [
                {
                    "type": "HorizontalLayout",
                    "elements": [
                        {
                            "type": "Control",
                            "label": "Modifier",
                            "scope": "#/properties/date/properties/modifier"
                        },
                        {
                            "type": "Control",
                            "label": "Year",
                            "scope": "#/properties/date/properties/year"
                        },
                        {
                            "type": "Control",
                            "label": "Month",
                            "scope": "#/properties/date/properties/month"
                        },
                        {
                            "type": "Control",
                            "label": "Day",
                            "scope": "#/properties/date/properties/day"
                        },
                    ]
                },
            ]
        },
        {
            "type": "Group",
            "label": "Victims",
            "elements": [
                {
                    "type": "VerticalLayout",
                    "elements": [
                        {
                            "type": "Control",
                            "label": "People",
                            "scope": "#/properties/victims"
                        },
                        {
                            "type": "Control",
                            "label": "Number of Victims",
                            "scope": "#/properties/numberOfVictims"
                        },
                        {
                            "type": "Control",
                            "label": "Victim Category",
                            "scope": "#/properties/victimCategory"
                        }
                    ]
                },
            ]
        },
        {
            "type": "Group",
            "label": "Aggressors",
            "elements": [
                {
                    "type": "VerticalLayout",
                    "elements": [
                        {
                            "type": "Control",
                            "label": "People",
                            "scope": "#/properties/aggressors"
                        },
                        {
                            "type": "Control",
                            "label": "Aggressor Category",
                            "scope": "#/properties/aggressorCategory"
                        }
                    ]
                },
            ]
        },
        {
            "type": "Group",
            "label": "Metadata",
            "elements": [
                {
                    "type": "VerticalLayout",
                    "elements": [
                        {
                            "type": "Control",
                            "label": "Women Involved?",
                            "scope": "#/properties/womenInvolved"
                        },
                        {
                            "type": "Control",
                            "label": "Types of Violence",
                            "scope": "#/properties/typesOfViolence"
                        },
                        {
                            "type": "Control",
                            "label": "Case Outcome Type",
                            "scope": "#/properties/caseOutcomeType"
                        },
                        {
                            "type": "Control",
                            "label": "Case Outcome",
                            "scope": "#/properties/caseOutcomeForDisavowedOrErasedViolence",
                            "rule": {
                                "effect": "SHOW",
                                "condition": {
                                    "scope": "#/properties/caseOutcomeType",
                                    "schema": { "enum": ["Disavowed or Erased Violence"] }
                                }
                            }
                        },
                        {
                            "type": "Control",
                            "label": "Case Outcome",
                            "scope": "#/properties/caseOutcomeForSeekingJustice",
                            "rule": {
                                "effect": "SHOW",
                                "condition": {
                                    "scope": "#/properties/caseOutcomeType",
                                    "schema": { "enum": ["Seeking Justice"] }
                                }
                            }
                        },
                        {
                            "type": "Control",
                            "label": "Alleged Crime",
                            "scope": "#/properties/allegedCrime"
                        },
                        {
                            "type": "Control",
                            "label": "Available Records",
                            "scope": "#/properties/availableRecords"
                        }
                    ]
                }
            ]
        },
        {
            "type": "Group",
            "label": "Sources",
            "elements": [
                {
                    "type": "VerticalLayout",
                    "elements": [
                        {
                            "type": "Control",
                            "label": "Primary Sources",
                            "scope": "#/properties/primarySources"
                        },
                        {
                            "type": "Control",
                            "label": "Secondary Sources",
                            "scope": "#/properties/secondarySources"
                        },
                    ]
                }
            ]
        },
        {
            "type": "VerticalLayout",
            "elements": [
                {
                    "type": "Control",
                    "label": "Researcher Notes",
                    "scope": "#/properties/researcherNotes",
                    "options": {
                        "multi": true,
                    }
                }
            ]
        }
    ]
};

export { schema, uischema };