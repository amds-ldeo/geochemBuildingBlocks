
# EMPA Technique-Aligned Protocol Profile (empaTAPP) (Schema)

`ada.bbr.metadata.techniqueProtocols.empaTAPP` *v0.1*

EMPA-specific extension of the base TAPP definition. Adds EPMA top-level properties (beam mode, accelerating voltage, matrix correction method), a parameter vocabulary, and an analyte-column template covering EPMA per-element acquisition and reporting fields. Vocabularies, parameter templates, and analyte-column templates ship as separate JSON files under vocab/, parameters/, and analyteColumns/ for maintainability.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# EMPA Technique-Aligned Protocol Profile (empaTAPP)

EMPA-specific extension of the base [tappDefinition](../tappDefinition/) building block. Adds top-level EPMA properties, a parameter vocabulary used in `ada:methodParameters`, and an analyte-column template used in `ada:analyteTemplate.ada:analyteColumns`.

## Structure

empaTAPP composes via `allOf`:
- `$ref: ../tappDefinition/schema.yaml` — base TAPP shape
- ADA EPMA overlay — adds EPMA-specific top-level properties (`ada:beamMode`, ...) and constrains where applicable

## Supporting files

The building block ships three sets of supporting JSON files that humans and tools reference when authoring empaTAPP instances. The schema does not currently `$ref` them as constraints; they are canonical reference data:

- `vocab/<name>.json` — `schema:DefinedTermSet` objects with `schema:hasDefinedTerm` arrays. Each is the canonical vocabulary for one EPMA enum.
- `parameters/<ParameterName>.json` — `schema:PropertyValueSpecification` template per parameter. Instances use these as `ada:methodParameters[]` entries.
- `analyteColumns/<columnName>.json` — `schema:PropertyValueSpecification` template per per-element analyte column. Instances use these as `ada:analyteTemplate.ada:analyteColumns[]` entries.

## POC scope (this version)

Three-row proof-of-concept covering one of each pattern:
- **Property** — `ada:beamMode` (top-level enum: Focused | Defocused | Raster)
- **Parameter** — `BeamRasterDimensions` (PropertyValueSpecification)
- **AnalyteColumn** — `monochromatorCrystal` (PropertyValueSpecification, references the monochromatorCrystal vocab)

The remaining ~60 rows from `docs/TAPP_EPMA_filled.xlsx` (TAPP worksheet) will be added once this POC pattern is approved.

## Dependencies

- [tappDefinition](../tappDefinition/) — base TAPP definition

## Source spec

Property/parameter/analyte-column definitions are derived from the **TAPP worksheet** of `docs/TAPP_EPMA_filled.xlsx`. The "implementation notes" column tags each row with one of `property`, `parameter`, `analyteColumn`, or a combination, plus `dataType` and `readOnly` flags.

## Examples

### empaTAPP example P1: Chi et al. 2015 (Tissintite, EPSL)
empaTAPP instance derived from publication Chi et al. 2015 (Tissintite, EPSL). Property and parameter values taken from the corresponding column of the TAPP_EPMA_filled.xlsx 'TAPP' worksheet.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/"
  },
  "@id": "ex:empaTAPP-p1",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS major/minor element minerals",
  "schema:description": "empaTAPP example derived from Chi et al. 2015 (Tissintite, EPSL).",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "EPMA-WDS",
    "schema:name": "Electron Microprobe Analysis - WDS"
  },
  "schema:agent": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "Chi Ma et al."
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Caltech GPS Division Analytical Facility"
  },
  "schema:instrument": {
    "@type": [
      "schema:Thing",
      "schema:Product",
      "https://w3id.org/nfdi4ing/metadata4ing#Instrument"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      "ada:EPMAInstrument"
    ],
    "schema:name": "JEOL JXA-8200",
    "schema:manufacturer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "JEOL"
    },
    "schema:model": {
      "@type": [
        "schema:ProductModel"
      ],
      "schema:name": "JXA-8200"
    }
  },
  "ada:beamMode": "Focused",
  "ada:acceleratingVoltageDefault": "15",
  "ada:beamDiameterDefault": "0 (focused)",
  "ada:beamCurrentDefault": "5",
  "ada:methodParameters": [
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Default Accelerating Voltage",
      "schema:valueName": "acceleratingVoltage",
      "schema:description": "Electron beam accelerating voltage in kilovolts (kV).",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "15"
    },
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Default Beam Diameter",
      "schema:valueName": "beamDiameter",
      "schema:description": "Diameter of the focused or defocused electron beam in micrometers.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "0 (focused)"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "ada": "https://ada.astromat.org/metadata/",
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/techniqueProtocols/empaTAPP/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/"
    }
  ],
  "@id": "ex:empaTAPP-p1",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS major/minor element minerals",
  "schema:description": "empaTAPP example derived from Chi et al. 2015 (Tissintite, EPSL).",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "EPMA-WDS",
    "schema:name": "Electron Microprobe Analysis - WDS"
  },
  "schema:agent": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "Chi Ma et al."
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Caltech GPS Division Analytical Facility"
  },
  "schema:instrument": {
    "@type": [
      "schema:Thing",
      "schema:Product",
      "https://w3id.org/nfdi4ing/metadata4ing#Instrument"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      "ada:EPMAInstrument"
    ],
    "schema:name": "JEOL JXA-8200",
    "schema:manufacturer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "JEOL"
    },
    "schema:model": {
      "@type": [
        "schema:ProductModel"
      ],
      "schema:name": "JXA-8200"
    }
  },
  "ada:beamMode": "Focused",
  "ada:acceleratingVoltageDefault": "15",
  "ada:beamDiameterDefault": "0 (focused)",
  "ada:beamCurrentDefault": "5",
  "ada:methodParameters": [
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Default Accelerating Voltage",
      "schema:valueName": "acceleratingVoltage",
      "schema:description": "Electron beam accelerating voltage in kilovolts (kV).",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "15"
    },
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Default Beam Diameter",
      "schema:valueName": "beamDiameter",
      "schema:description": "Diameter of the focused or defocused electron beam in micrometers.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "0 (focused)"
    }
  ]
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix bios: <https://bioschemas.org/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:empaTAPP-p1> a cdi:Activity,
        schema1:Action,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:agent [ a schema1:Person ;
            schema1:name "Chi Ma et al." ] ;
    schema1:description "empaTAPP example derived from Chi et al. 2015 (Tissintite, EPSL)." ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing,
                <https://w3id.org/nfdi4ing/metadata4ing#Instrument> ;
            schema1:additionalType "ada:EPMAInstrument",
                "nxs:BaseClass/NXinstrument" ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "JEOL" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "JXA-8200" ] ;
            schema1:name "JEOL JXA-8200" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "Caltech GPS Division Analytical Facility" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "Electron Microprobe Analysis - WDS" ;
            schema1:termCode "EPMA-WDS" ] ;
    schema1:name "EPMA-WDS major/minor element minerals" ;
    ada:acceleratingVoltageDefault "15" ;
    ada:beamCurrentDefault "5" ;
    ada:beamDiameterDefault "0 (focused)" ;
    ada:beamMode "Focused" ;
    ada:methodParameters [ a schema1:PropertyValueSpecification ;
            schema1:defaultValue "15" ;
            schema1:description "Electron beam accelerating voltage in kilovolts (kV)." ;
            schema1:name "Default Accelerating Voltage" ;
            schema1:readonlyValue true ;
            schema1:valueName "acceleratingVoltage" ;
            ada:dataType "string" ;
            ada:fieldScope "session" ;
            ada:tier "R" ],
        [ a schema1:PropertyValueSpecification ;
            schema1:defaultValue "0 (focused)" ;
            schema1:description "Diameter of the focused or defocused electron beam in micrometers." ;
            schema1:name "Default Beam Diameter" ;
            schema1:readonlyValue true ;
            schema1:valueName "beamDiameter" ;
            ada:dataType "string" ;
            ada:fieldScope "session" ;
            ada:tier "R" ] .


```


### empaTAPP example P2: Hu et al. 2020 (Coesite NWA8657, GCA)
empaTAPP instance derived from publication Hu et al. 2020 (Coesite NWA8657, GCA). Property and parameter values taken from the corresponding column of the TAPP_EPMA_filled.xlsx 'TAPP' worksheet.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/"
  },
  "@id": "ex:empaTAPP-p2",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS major/minor element minerals and glass",
  "schema:description": "empaTAPP example derived from Hu et al. 2020 (Coesite NWA8657, GCA).",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "EPMA-WDS",
    "schema:name": "Electron Microprobe Analysis - WDS"
  },
  "schema:agent": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "Sen Hu et al."
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Institute of Geology and Geophysics, Chinese Academy of Sciences (IGGCAS)"
  },
  "schema:instrument": {
    "@type": [
      "schema:Thing",
      "schema:Product",
      "https://w3id.org/nfdi4ing/metadata4ing#Instrument"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      "ada:EPMAInstrument"
    ],
    "schema:name": "JEOL JXA-8100",
    "schema:manufacturer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "JEOL"
    },
    "schema:model": {
      "@type": [
        "schema:ProductModel"
      ],
      "schema:name": "JXA-8100"
    }
  },
  "ada:beamMode": "Focused",
  "ada:acceleratingVoltageDefault": "15",
  "ada:beamCurrentDefault": "10",
  "ada:methodParameters": [
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Default Accelerating Voltage",
      "schema:valueName": "acceleratingVoltage",
      "schema:description": "Electron beam accelerating voltage in kilovolts (kV).",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "15"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "ada": "https://ada.astromat.org/metadata/",
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/techniqueProtocols/empaTAPP/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/"
    }
  ],
  "@id": "ex:empaTAPP-p2",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS major/minor element minerals and glass",
  "schema:description": "empaTAPP example derived from Hu et al. 2020 (Coesite NWA8657, GCA).",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "EPMA-WDS",
    "schema:name": "Electron Microprobe Analysis - WDS"
  },
  "schema:agent": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "Sen Hu et al."
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Institute of Geology and Geophysics, Chinese Academy of Sciences (IGGCAS)"
  },
  "schema:instrument": {
    "@type": [
      "schema:Thing",
      "schema:Product",
      "https://w3id.org/nfdi4ing/metadata4ing#Instrument"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      "ada:EPMAInstrument"
    ],
    "schema:name": "JEOL JXA-8100",
    "schema:manufacturer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "JEOL"
    },
    "schema:model": {
      "@type": [
        "schema:ProductModel"
      ],
      "schema:name": "JXA-8100"
    }
  },
  "ada:beamMode": "Focused",
  "ada:acceleratingVoltageDefault": "15",
  "ada:beamCurrentDefault": "10",
  "ada:methodParameters": [
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Default Accelerating Voltage",
      "schema:valueName": "acceleratingVoltage",
      "schema:description": "Electron beam accelerating voltage in kilovolts (kV).",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "15"
    }
  ]
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix bios: <https://bioschemas.org/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:empaTAPP-p2> a cdi:Activity,
        schema1:Action,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:agent [ a schema1:Person ;
            schema1:name "Sen Hu et al." ] ;
    schema1:description "empaTAPP example derived from Hu et al. 2020 (Coesite NWA8657, GCA)." ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing,
                <https://w3id.org/nfdi4ing/metadata4ing#Instrument> ;
            schema1:additionalType "ada:EPMAInstrument",
                "nxs:BaseClass/NXinstrument" ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "JEOL" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "JXA-8100" ] ;
            schema1:name "JEOL JXA-8100" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "Institute of Geology and Geophysics, Chinese Academy of Sciences (IGGCAS)" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "Electron Microprobe Analysis - WDS" ;
            schema1:termCode "EPMA-WDS" ] ;
    schema1:name "EPMA-WDS major/minor element minerals and glass" ;
    ada:acceleratingVoltageDefault "15" ;
    ada:beamCurrentDefault "10" ;
    ada:beamMode "Focused" ;
    ada:methodParameters [ a schema1:PropertyValueSpecification ;
            schema1:defaultValue "15" ;
            schema1:description "Electron beam accelerating voltage in kilovolts (kV)." ;
            schema1:name "Default Accelerating Voltage" ;
            schema1:readonlyValue true ;
            schema1:valueName "acceleratingVoltage" ;
            ada:dataType "string" ;
            ada:fieldScope "session" ;
            ada:tier "R" ] .


```


### empaTAPP example P3: Liu et al. 2016 (Tissint mineral chem., MAPS)
empaTAPP instance derived from publication Liu et al. 2016 (Tissint mineral chem., MAPS). Property and parameter values taken from the corresponding column of the TAPP_EPMA_filled.xlsx 'TAPP' worksheet.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/"
  },
  "@id": "ex:empaTAPP-p3",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS major/minor element minerals and glass",
  "schema:description": "empaTAPP example derived from Liu et al. 2016 (Tissint mineral chem., MAPS).",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "EPMA-WDS",
    "schema:name": "Electron Microprobe Analysis - WDS"
  },
  "schema:agent": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "Yang Liu et al."
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "University of Tennessee (Cameca SX100); Caltech (JEOL JXA-8200)"
  },
  "schema:instrument": {
    "@type": [
      "schema:Thing",
      "schema:Product",
      "https://w3id.org/nfdi4ing/metadata4ing#Instrument"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      "ada:EPMAInstrument"
    ],
    "schema:name": "Cameca; JEOL SX100 (Univ. Tennessee); JXA-8200 (Caltech)",
    "schema:manufacturer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Cameca; JEOL"
    },
    "schema:model": {
      "@type": [
        "schema:ProductModel"
      ],
      "schema:name": "SX100 (Univ. Tennessee); JXA-8200 (Caltech)"
    }
  },
  "ada:acceleratingVoltageDefault": "15",
  "ada:beamDiameterDefault": "1–2 µm focused (silicates/oxides); 5–10 µm defocused (glass/maskelynite)",
  "ada:beamCurrentDefault": "20 nA (silicates/oxides); \n10 nA (glass/maskelynite/phosphate)",
  "ada:methodParameters": [
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Default Accelerating Voltage",
      "schema:valueName": "acceleratingVoltage",
      "schema:description": "Electron beam accelerating voltage in kilovolts (kV).",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "15"
    },
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Default Beam Diameter",
      "schema:valueName": "beamDiameter",
      "schema:description": "Diameter of the focused or defocused electron beam in micrometers.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "1–2 µm focused (silicates/oxides); 5–10 µm defocused (glass/maskelynite)"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "ada": "https://ada.astromat.org/metadata/",
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/techniqueProtocols/empaTAPP/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/"
    }
  ],
  "@id": "ex:empaTAPP-p3",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS major/minor element minerals and glass",
  "schema:description": "empaTAPP example derived from Liu et al. 2016 (Tissint mineral chem., MAPS).",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "EPMA-WDS",
    "schema:name": "Electron Microprobe Analysis - WDS"
  },
  "schema:agent": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "Yang Liu et al."
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "University of Tennessee (Cameca SX100); Caltech (JEOL JXA-8200)"
  },
  "schema:instrument": {
    "@type": [
      "schema:Thing",
      "schema:Product",
      "https://w3id.org/nfdi4ing/metadata4ing#Instrument"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      "ada:EPMAInstrument"
    ],
    "schema:name": "Cameca; JEOL SX100 (Univ. Tennessee); JXA-8200 (Caltech)",
    "schema:manufacturer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Cameca; JEOL"
    },
    "schema:model": {
      "@type": [
        "schema:ProductModel"
      ],
      "schema:name": "SX100 (Univ. Tennessee); JXA-8200 (Caltech)"
    }
  },
  "ada:acceleratingVoltageDefault": "15",
  "ada:beamDiameterDefault": "1\u20132 \u00b5m focused (silicates/oxides); 5\u201310 \u00b5m defocused (glass/maskelynite)",
  "ada:beamCurrentDefault": "20 nA (silicates/oxides); \n10 nA (glass/maskelynite/phosphate)",
  "ada:methodParameters": [
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Default Accelerating Voltage",
      "schema:valueName": "acceleratingVoltage",
      "schema:description": "Electron beam accelerating voltage in kilovolts (kV).",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "15"
    },
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Default Beam Diameter",
      "schema:valueName": "beamDiameter",
      "schema:description": "Diameter of the focused or defocused electron beam in micrometers.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "1\u20132 \u00b5m focused (silicates/oxides); 5\u201310 \u00b5m defocused (glass/maskelynite)"
    }
  ]
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix bios: <https://bioschemas.org/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:empaTAPP-p3> a cdi:Activity,
        schema1:Action,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:agent [ a schema1:Person ;
            schema1:name "Yang Liu et al." ] ;
    schema1:description "empaTAPP example derived from Liu et al. 2016 (Tissint mineral chem., MAPS)." ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing,
                <https://w3id.org/nfdi4ing/metadata4ing#Instrument> ;
            schema1:additionalType "ada:EPMAInstrument",
                "nxs:BaseClass/NXinstrument" ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "Cameca; JEOL" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "SX100 (Univ. Tennessee); JXA-8200 (Caltech)" ] ;
            schema1:name "Cameca; JEOL SX100 (Univ. Tennessee); JXA-8200 (Caltech)" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "University of Tennessee (Cameca SX100); Caltech (JEOL JXA-8200)" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "Electron Microprobe Analysis - WDS" ;
            schema1:termCode "EPMA-WDS" ] ;
    schema1:name "EPMA-WDS major/minor element minerals and glass" ;
    ada:acceleratingVoltageDefault "15" ;
    ada:beamCurrentDefault """20 nA (silicates/oxides); 
10 nA (glass/maskelynite/phosphate)""" ;
    ada:beamDiameterDefault "1–2 µm focused (silicates/oxides); 5–10 µm defocused (glass/maskelynite)" ;
    ada:methodParameters [ a schema1:PropertyValueSpecification ;
            schema1:defaultValue "1–2 µm focused (silicates/oxides); 5–10 µm defocused (glass/maskelynite)" ;
            schema1:description "Diameter of the focused or defocused electron beam in micrometers." ;
            schema1:name "Default Beam Diameter" ;
            schema1:readonlyValue true ;
            schema1:valueName "beamDiameter" ;
            ada:dataType "string" ;
            ada:fieldScope "session" ;
            ada:tier "R" ],
        [ a schema1:PropertyValueSpecification ;
            schema1:defaultValue "15" ;
            schema1:description "Electron beam accelerating voltage in kilovolts (kV)." ;
            schema1:name "Default Accelerating Voltage" ;
            schema1:readonlyValue true ;
            schema1:valueName "acceleratingVoltage" ;
            ada:dataType "string" ;
            ada:fieldScope "session" ;
            ada:tier "R" ] .


```


### empaTAPP example P4: Ma et al. 2017 (Liebermannite, MAPS)
empaTAPP instance derived from publication Ma et al. 2017 (Liebermannite, MAPS). Property and parameter values taken from the corresponding column of the TAPP_EPMA_filled.xlsx 'TAPP' worksheet.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/"
  },
  "@id": "ex:empaTAPP-p4",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS major/minor element minerals",
  "schema:description": "empaTAPP example derived from Ma et al. 2017 (Liebermannite, MAPS).",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "EPMA-WDS",
    "schema:name": "Electron Microprobe Analysis - WDS"
  },
  "schema:agent": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "Chi Ma et al."
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Caltech GPS Division Analytical Facility"
  },
  "schema:instrument": {
    "@type": [
      "schema:Thing",
      "schema:Product",
      "https://w3id.org/nfdi4ing/metadata4ing#Instrument"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      "ada:EPMAInstrument"
    ],
    "schema:name": "JEOL JXA-8200",
    "schema:manufacturer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "JEOL"
    },
    "schema:model": {
      "@type": [
        "schema:ProductModel"
      ],
      "schema:name": "JXA-8200"
    }
  },
  "ada:beamMode": "Focused",
  "ada:acceleratingVoltageDefault": "15",
  "ada:beamDiameterDefault": "0 (focused)",
  "ada:beamCurrentDefault": "5",
  "ada:methodParameters": [
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Default Accelerating Voltage",
      "schema:valueName": "acceleratingVoltage",
      "schema:description": "Electron beam accelerating voltage in kilovolts (kV).",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "15"
    },
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Default Beam Diameter",
      "schema:valueName": "beamDiameter",
      "schema:description": "Diameter of the focused or defocused electron beam in micrometers.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "0 (focused)"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "ada": "https://ada.astromat.org/metadata/",
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/techniqueProtocols/empaTAPP/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/"
    }
  ],
  "@id": "ex:empaTAPP-p4",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS major/minor element minerals",
  "schema:description": "empaTAPP example derived from Ma et al. 2017 (Liebermannite, MAPS).",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "EPMA-WDS",
    "schema:name": "Electron Microprobe Analysis - WDS"
  },
  "schema:agent": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "Chi Ma et al."
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Caltech GPS Division Analytical Facility"
  },
  "schema:instrument": {
    "@type": [
      "schema:Thing",
      "schema:Product",
      "https://w3id.org/nfdi4ing/metadata4ing#Instrument"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      "ada:EPMAInstrument"
    ],
    "schema:name": "JEOL JXA-8200",
    "schema:manufacturer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "JEOL"
    },
    "schema:model": {
      "@type": [
        "schema:ProductModel"
      ],
      "schema:name": "JXA-8200"
    }
  },
  "ada:beamMode": "Focused",
  "ada:acceleratingVoltageDefault": "15",
  "ada:beamDiameterDefault": "0 (focused)",
  "ada:beamCurrentDefault": "5",
  "ada:methodParameters": [
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Default Accelerating Voltage",
      "schema:valueName": "acceleratingVoltage",
      "schema:description": "Electron beam accelerating voltage in kilovolts (kV).",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "15"
    },
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Default Beam Diameter",
      "schema:valueName": "beamDiameter",
      "schema:description": "Diameter of the focused or defocused electron beam in micrometers.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "0 (focused)"
    }
  ]
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix bios: <https://bioschemas.org/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:empaTAPP-p4> a cdi:Activity,
        schema1:Action,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:agent [ a schema1:Person ;
            schema1:name "Chi Ma et al." ] ;
    schema1:description "empaTAPP example derived from Ma et al. 2017 (Liebermannite, MAPS)." ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing,
                <https://w3id.org/nfdi4ing/metadata4ing#Instrument> ;
            schema1:additionalType "ada:EPMAInstrument",
                "nxs:BaseClass/NXinstrument" ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "JEOL" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "JXA-8200" ] ;
            schema1:name "JEOL JXA-8200" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "Caltech GPS Division Analytical Facility" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "Electron Microprobe Analysis - WDS" ;
            schema1:termCode "EPMA-WDS" ] ;
    schema1:name "EPMA-WDS major/minor element minerals" ;
    ada:acceleratingVoltageDefault "15" ;
    ada:beamCurrentDefault "5" ;
    ada:beamDiameterDefault "0 (focused)" ;
    ada:beamMode "Focused" ;
    ada:methodParameters [ a schema1:PropertyValueSpecification ;
            schema1:defaultValue "0 (focused)" ;
            schema1:description "Diameter of the focused or defocused electron beam in micrometers." ;
            schema1:name "Default Beam Diameter" ;
            schema1:readonlyValue true ;
            schema1:valueName "beamDiameter" ;
            ada:dataType "string" ;
            ada:fieldScope "session" ;
            ada:tier "R" ],
        [ a schema1:PropertyValueSpecification ;
            schema1:defaultValue "15" ;
            schema1:description "Electron beam accelerating voltage in kilovolts (kV)." ;
            schema1:name "Default Accelerating Voltage" ;
            schema1:readonlyValue true ;
            schema1:valueName "acceleratingVoltage" ;
            ada:dataType "string" ;
            ada:fieldScope "session" ;
            ada:tier "R" ] .


```


### empaTAPP example P5: Frank et al. 2023 (Ivuna CAI, MAPS)
empaTAPP instance derived from publication Frank et al. 2023 (Ivuna CAI, MAPS). Property and parameter values taken from the corresponding column of the TAPP_EPMA_filled.xlsx 'TAPP' worksheet.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/"
  },
  "@id": "ex:empaTAPP-p5",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS major/minor element minerals",
  "schema:description": "empaTAPP example derived from Frank et al. 2023 (Ivuna CAI, MAPS).",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "EPMA-WDS",
    "schema:name": "Electron Microprobe Analysis - WDS"
  },
  "schema:agent": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "David Frank et al."
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "ARES, NASA Johnson Space Center"
  },
  "schema:instrument": {
    "@type": [
      "schema:Thing",
      "schema:Product",
      "https://w3id.org/nfdi4ing/metadata4ing#Instrument"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      "ada:EPMAInstrument"
    ],
    "schema:name": "Cameca SX100",
    "schema:manufacturer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Cameca"
    },
    "schema:model": {
      "@type": [
        "schema:ProductModel"
      ],
      "schema:name": "SX100"
    }
  },
  "ada:beamMode": "Focused",
  "ada:acceleratingVoltageDefault": "20",
  "ada:beamDiameterDefault": "1 µm (focused)",
  "ada:beamCurrentDefault": "20",
  "ada:methodParameters": [
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Default Accelerating Voltage",
      "schema:valueName": "acceleratingVoltage",
      "schema:description": "Electron beam accelerating voltage in kilovolts (kV).",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "20"
    },
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Default Beam Diameter",
      "schema:valueName": "beamDiameter",
      "schema:description": "Diameter of the focused or defocused electron beam in micrometers.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "1 µm (focused)"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "ada": "https://ada.astromat.org/metadata/",
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/techniqueProtocols/empaTAPP/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/"
    }
  ],
  "@id": "ex:empaTAPP-p5",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS major/minor element minerals",
  "schema:description": "empaTAPP example derived from Frank et al. 2023 (Ivuna CAI, MAPS).",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "EPMA-WDS",
    "schema:name": "Electron Microprobe Analysis - WDS"
  },
  "schema:agent": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "David Frank et al."
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "ARES, NASA Johnson Space Center"
  },
  "schema:instrument": {
    "@type": [
      "schema:Thing",
      "schema:Product",
      "https://w3id.org/nfdi4ing/metadata4ing#Instrument"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      "ada:EPMAInstrument"
    ],
    "schema:name": "Cameca SX100",
    "schema:manufacturer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Cameca"
    },
    "schema:model": {
      "@type": [
        "schema:ProductModel"
      ],
      "schema:name": "SX100"
    }
  },
  "ada:beamMode": "Focused",
  "ada:acceleratingVoltageDefault": "20",
  "ada:beamDiameterDefault": "1 \u00b5m (focused)",
  "ada:beamCurrentDefault": "20",
  "ada:methodParameters": [
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Default Accelerating Voltage",
      "schema:valueName": "acceleratingVoltage",
      "schema:description": "Electron beam accelerating voltage in kilovolts (kV).",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "20"
    },
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Default Beam Diameter",
      "schema:valueName": "beamDiameter",
      "schema:description": "Diameter of the focused or defocused electron beam in micrometers.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "1 \u00b5m (focused)"
    }
  ]
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix bios: <https://bioschemas.org/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:empaTAPP-p5> a cdi:Activity,
        schema1:Action,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:agent [ a schema1:Person ;
            schema1:name "David Frank et al." ] ;
    schema1:description "empaTAPP example derived from Frank et al. 2023 (Ivuna CAI, MAPS)." ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing,
                <https://w3id.org/nfdi4ing/metadata4ing#Instrument> ;
            schema1:additionalType "ada:EPMAInstrument",
                "nxs:BaseClass/NXinstrument" ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "Cameca" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "SX100" ] ;
            schema1:name "Cameca SX100" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "ARES, NASA Johnson Space Center" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "Electron Microprobe Analysis - WDS" ;
            schema1:termCode "EPMA-WDS" ] ;
    schema1:name "EPMA-WDS major/minor element minerals" ;
    ada:acceleratingVoltageDefault "20" ;
    ada:beamCurrentDefault "20" ;
    ada:beamDiameterDefault "1 µm (focused)" ;
    ada:beamMode "Focused" ;
    ada:methodParameters [ a schema1:PropertyValueSpecification ;
            schema1:defaultValue "20" ;
            schema1:description "Electron beam accelerating voltage in kilovolts (kV)." ;
            schema1:name "Default Accelerating Voltage" ;
            schema1:readonlyValue true ;
            schema1:valueName "acceleratingVoltage" ;
            ada:dataType "string" ;
            ada:fieldScope "session" ;
            ada:tier "R" ],
        [ a schema1:PropertyValueSpecification ;
            schema1:defaultValue "1 µm (focused)" ;
            schema1:description "Diameter of the focused or defocused electron beam in micrometers." ;
            schema1:name "Default Beam Diameter" ;
            schema1:readonlyValue true ;
            schema1:valueName "beamDiameter" ;
            ada:dataType "string" ;
            ada:fieldScope "session" ;
            ada:tier "R" ] .


```


### empaTAPP example P6: Broussard et al. 2026 (OC002 CI chondrite, MAPS)
empaTAPP instance derived from publication Broussard et al. 2026 (OC002 CI chondrite, MAPS). Property and parameter values taken from the corresponding column of the TAPP_EPMA_filled.xlsx 'TAPP' worksheet.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/"
  },
  "@id": "ex:empaTAPP-p6",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS major/minor element minerals",
  "schema:description": "empaTAPP example derived from Broussard et al. 2026 (OC002 CI chondrite, MAPS).",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "EPMA-WDS",
    "schema:name": "Electron Microprobe Analysis - WDS"
  },
  "schema:agent": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "Broussard et al."
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Washington University in St. Louis"
  },
  "schema:instrument": {
    "@type": [
      "schema:Thing",
      "schema:Product",
      "https://w3id.org/nfdi4ing/metadata4ing#Instrument"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      "ada:EPMAInstrument"
    ],
    "schema:name": "JEOL JXA-8200",
    "schema:manufacturer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "JEOL"
    },
    "schema:model": {
      "@type": [
        "schema:ProductModel"
      ],
      "schema:name": "JXA-8200"
    }
  },
  "ada:beamMode": "Focused",
  "ada:acceleratingVoltageDefault": "15",
  "ada:beamDiameterDefault": "0 (focused)",
  "ada:beamCurrentDefault": "25 nA",
  "ada:methodParameters": [
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Default Accelerating Voltage",
      "schema:valueName": "acceleratingVoltage",
      "schema:description": "Electron beam accelerating voltage in kilovolts (kV).",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "15"
    },
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Default Beam Diameter",
      "schema:valueName": "beamDiameter",
      "schema:description": "Diameter of the focused or defocused electron beam in micrometers.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "0 (focused)"
    },
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Beam Damage Minimization",
      "schema:valueName": "BeamDamageMinimization",
      "schema:description": "Description of the approach used to minimize beam damage, especially Na- and K-loss in glasses, micas, and hydrous minerals.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "F measurement with polynomial background fit (LDE1 crystal)"
    },
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Halogen Correction on Oxygen",
      "schema:valueName": "halogenOxygenCorrection",
      "schema:description": "Whether a halogen correction was applied to calculate oxygen content by stoichiometry in halogen-bearing phases.",
      "ada:dataType": "boolean",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "Yes (F correction for fluorine-bearing phosphates; CO2 by stoichiometry for carbonates)"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "ada": "https://ada.astromat.org/metadata/",
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/techniqueProtocols/empaTAPP/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/"
    }
  ],
  "@id": "ex:empaTAPP-p6",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS major/minor element minerals",
  "schema:description": "empaTAPP example derived from Broussard et al. 2026 (OC002 CI chondrite, MAPS).",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "EPMA-WDS",
    "schema:name": "Electron Microprobe Analysis - WDS"
  },
  "schema:agent": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "Broussard et al."
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Washington University in St. Louis"
  },
  "schema:instrument": {
    "@type": [
      "schema:Thing",
      "schema:Product",
      "https://w3id.org/nfdi4ing/metadata4ing#Instrument"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      "ada:EPMAInstrument"
    ],
    "schema:name": "JEOL JXA-8200",
    "schema:manufacturer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "JEOL"
    },
    "schema:model": {
      "@type": [
        "schema:ProductModel"
      ],
      "schema:name": "JXA-8200"
    }
  },
  "ada:beamMode": "Focused",
  "ada:acceleratingVoltageDefault": "15",
  "ada:beamDiameterDefault": "0 (focused)",
  "ada:beamCurrentDefault": "25 nA",
  "ada:methodParameters": [
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Default Accelerating Voltage",
      "schema:valueName": "acceleratingVoltage",
      "schema:description": "Electron beam accelerating voltage in kilovolts (kV).",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "15"
    },
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Default Beam Diameter",
      "schema:valueName": "beamDiameter",
      "schema:description": "Diameter of the focused or defocused electron beam in micrometers.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "0 (focused)"
    },
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Beam Damage Minimization",
      "schema:valueName": "BeamDamageMinimization",
      "schema:description": "Description of the approach used to minimize beam damage, especially Na- and K-loss in glasses, micas, and hydrous minerals.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "F measurement with polynomial background fit (LDE1 crystal)"
    },
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Halogen Correction on Oxygen",
      "schema:valueName": "halogenOxygenCorrection",
      "schema:description": "Whether a halogen correction was applied to calculate oxygen content by stoichiometry in halogen-bearing phases.",
      "ada:dataType": "boolean",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "Yes (F correction for fluorine-bearing phosphates; CO2 by stoichiometry for carbonates)"
    }
  ]
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix bios: <https://bioschemas.org/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:empaTAPP-p6> a cdi:Activity,
        schema1:Action,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:agent [ a schema1:Person ;
            schema1:name "Broussard et al." ] ;
    schema1:description "empaTAPP example derived from Broussard et al. 2026 (OC002 CI chondrite, MAPS)." ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing,
                <https://w3id.org/nfdi4ing/metadata4ing#Instrument> ;
            schema1:additionalType "ada:EPMAInstrument",
                "nxs:BaseClass/NXinstrument" ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "JEOL" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "JXA-8200" ] ;
            schema1:name "JEOL JXA-8200" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "Washington University in St. Louis" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "Electron Microprobe Analysis - WDS" ;
            schema1:termCode "EPMA-WDS" ] ;
    schema1:name "EPMA-WDS major/minor element minerals" ;
    ada:acceleratingVoltageDefault "15" ;
    ada:beamCurrentDefault "25 nA" ;
    ada:beamDiameterDefault "0 (focused)" ;
    ada:beamMode "Focused" ;
    ada:methodParameters [ a schema1:PropertyValueSpecification ;
            schema1:defaultValue "15" ;
            schema1:description "Electron beam accelerating voltage in kilovolts (kV)." ;
            schema1:name "Default Accelerating Voltage" ;
            schema1:readonlyValue true ;
            schema1:valueName "acceleratingVoltage" ;
            ada:dataType "string" ;
            ada:fieldScope "session" ;
            ada:tier "R" ],
        [ a schema1:PropertyValueSpecification ;
            schema1:defaultValue "Yes (F correction for fluorine-bearing phosphates; CO2 by stoichiometry for carbonates)" ;
            schema1:description "Whether a halogen correction was applied to calculate oxygen content by stoichiometry in halogen-bearing phases." ;
            schema1:name "Halogen Correction on Oxygen" ;
            schema1:readonlyValue true ;
            schema1:valueName "halogenOxygenCorrection" ;
            ada:dataType "boolean" ;
            ada:fieldScope "session" ;
            ada:tier "R" ],
        [ a schema1:PropertyValueSpecification ;
            schema1:defaultValue "F measurement with polynomial background fit (LDE1 crystal)" ;
            schema1:description "Description of the approach used to minimize beam damage, especially Na- and K-loss in glasses, micas, and hydrous minerals." ;
            schema1:name "Beam Damage Minimization" ;
            schema1:readonlyValue true ;
            schema1:valueName "BeamDamageMinimization" ;
            ada:dataType "string" ;
            ada:fieldScope "session" ;
            ada:tier "R" ],
        [ a schema1:PropertyValueSpecification ;
            schema1:defaultValue "0 (focused)" ;
            schema1:description "Diameter of the focused or defocused electron beam in micrometers." ;
            schema1:name "Default Beam Diameter" ;
            schema1:readonlyValue true ;
            schema1:valueName "beamDiameter" ;
            ada:dataType "string" ;
            ada:fieldScope "session" ;
            ada:tier "R" ] .


```


### empaTAPP example P7: Seifert et al. 2026 (Bennu apatite, MAPS)
empaTAPP instance derived from publication Seifert et al. 2026 (Bennu apatite, MAPS). Property and parameter values taken from the corresponding column of the TAPP_EPMA_filled.xlsx 'TAPP' worksheet.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/"
  },
  "@id": "ex:empaTAPP-p7",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EMPA major element apatite (phosphate)",
  "schema:description": "empaTAPP example derived from Seifert et al. 2026 (Bennu apatite, MAPS).",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "EPMA-WDS",
    "schema:name": "Electron Microprobe Analysis - WDS"
  },
  "schema:agent": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "Seifert et al."
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "NASA Johnson Space Center (JSC)"
  },
  "schema:instrument": {
    "@type": [
      "schema:Thing",
      "schema:Product",
      "https://w3id.org/nfdi4ing/metadata4ing#Instrument"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      "ada:EPMAInstrument"
    ],
    "schema:name": "JEOL JEOL 8530 EMPA (Field Emission)",
    "schema:manufacturer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "JEOL"
    },
    "schema:model": {
      "@type": [
        "schema:ProductModel"
      ],
      "schema:name": "JEOL 8530 EMPA (Field Emission)"
    }
  },
  "ada:acceleratingVoltageDefault": "15",
  "ada:beamDiameterDefault": "2 µm",
  "ada:beamCurrentDefault": "20 nA",
  "ada:methodParameters": [
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Default Accelerating Voltage",
      "schema:valueName": "acceleratingVoltage",
      "schema:description": "Electron beam accelerating voltage in kilovolts (kV).",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "15"
    },
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Default Beam Diameter",
      "schema:valueName": "beamDiameter",
      "schema:description": "Diameter of the focused or defocused electron beam in micrometers.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "2 µm"
    },
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Beam Damage Minimization",
      "schema:valueName": "BeamDamageMinimization",
      "schema:description": "Description of the approach used to minimize beam damage, especially Na- and K-loss in glasses, micas, and hydrous minerals.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "Durango apatite tested for halogen volatilization under beam; no significant volatile loss observed between 3 µm and 10 µm spot conditions"
    },
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Halogen Correction on Oxygen",
      "schema:valueName": "halogenOxygenCorrection",
      "schema:description": "Whether a halogen correction was applied to calculate oxygen content by stoichiometry in halogen-bearing phases.",
      "ada:dataType": "boolean",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "Yes (F measured; Cl measured; OH by difference)"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "ada": "https://ada.astromat.org/metadata/",
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/techniqueProtocols/empaTAPP/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/"
    }
  ],
  "@id": "ex:empaTAPP-p7",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EMPA major element apatite (phosphate)",
  "schema:description": "empaTAPP example derived from Seifert et al. 2026 (Bennu apatite, MAPS).",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "EPMA-WDS",
    "schema:name": "Electron Microprobe Analysis - WDS"
  },
  "schema:agent": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "Seifert et al."
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "NASA Johnson Space Center (JSC)"
  },
  "schema:instrument": {
    "@type": [
      "schema:Thing",
      "schema:Product",
      "https://w3id.org/nfdi4ing/metadata4ing#Instrument"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      "ada:EPMAInstrument"
    ],
    "schema:name": "JEOL JEOL 8530 EMPA (Field Emission)",
    "schema:manufacturer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "JEOL"
    },
    "schema:model": {
      "@type": [
        "schema:ProductModel"
      ],
      "schema:name": "JEOL 8530 EMPA (Field Emission)"
    }
  },
  "ada:acceleratingVoltageDefault": "15",
  "ada:beamDiameterDefault": "2 \u00b5m",
  "ada:beamCurrentDefault": "20 nA",
  "ada:methodParameters": [
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Default Accelerating Voltage",
      "schema:valueName": "acceleratingVoltage",
      "schema:description": "Electron beam accelerating voltage in kilovolts (kV).",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "15"
    },
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Default Beam Diameter",
      "schema:valueName": "beamDiameter",
      "schema:description": "Diameter of the focused or defocused electron beam in micrometers.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "2 \u00b5m"
    },
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Beam Damage Minimization",
      "schema:valueName": "BeamDamageMinimization",
      "schema:description": "Description of the approach used to minimize beam damage, especially Na- and K-loss in glasses, micas, and hydrous minerals.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "Durango apatite tested for halogen volatilization under beam; no significant volatile loss observed between 3 \u00b5m and 10 \u00b5m spot conditions"
    },
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Halogen Correction on Oxygen",
      "schema:valueName": "halogenOxygenCorrection",
      "schema:description": "Whether a halogen correction was applied to calculate oxygen content by stoichiometry in halogen-bearing phases.",
      "ada:dataType": "boolean",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "Yes (F measured; Cl measured; OH by difference)"
    }
  ]
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix bios: <https://bioschemas.org/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:empaTAPP-p7> a cdi:Activity,
        schema1:Action,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:agent [ a schema1:Person ;
            schema1:name "Seifert et al." ] ;
    schema1:description "empaTAPP example derived from Seifert et al. 2026 (Bennu apatite, MAPS)." ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing,
                <https://w3id.org/nfdi4ing/metadata4ing#Instrument> ;
            schema1:additionalType "ada:EPMAInstrument",
                "nxs:BaseClass/NXinstrument" ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "JEOL" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "JEOL 8530 EMPA (Field Emission)" ] ;
            schema1:name "JEOL JEOL 8530 EMPA (Field Emission)" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "NASA Johnson Space Center (JSC)" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "Electron Microprobe Analysis - WDS" ;
            schema1:termCode "EPMA-WDS" ] ;
    schema1:name "EMPA major element apatite (phosphate)" ;
    ada:acceleratingVoltageDefault "15" ;
    ada:beamCurrentDefault "20 nA" ;
    ada:beamDiameterDefault "2 µm" ;
    ada:methodParameters [ a schema1:PropertyValueSpecification ;
            schema1:defaultValue "2 µm" ;
            schema1:description "Diameter of the focused or defocused electron beam in micrometers." ;
            schema1:name "Default Beam Diameter" ;
            schema1:readonlyValue true ;
            schema1:valueName "beamDiameter" ;
            ada:dataType "string" ;
            ada:fieldScope "session" ;
            ada:tier "R" ],
        [ a schema1:PropertyValueSpecification ;
            schema1:defaultValue "Yes (F measured; Cl measured; OH by difference)" ;
            schema1:description "Whether a halogen correction was applied to calculate oxygen content by stoichiometry in halogen-bearing phases." ;
            schema1:name "Halogen Correction on Oxygen" ;
            schema1:readonlyValue true ;
            schema1:valueName "halogenOxygenCorrection" ;
            ada:dataType "boolean" ;
            ada:fieldScope "session" ;
            ada:tier "R" ],
        [ a schema1:PropertyValueSpecification ;
            schema1:defaultValue "Durango apatite tested for halogen volatilization under beam; no significant volatile loss observed between 3 µm and 10 µm spot conditions" ;
            schema1:description "Description of the approach used to minimize beam damage, especially Na- and K-loss in glasses, micas, and hydrous minerals." ;
            schema1:name "Beam Damage Minimization" ;
            schema1:readonlyValue true ;
            schema1:valueName "BeamDamageMinimization" ;
            ada:dataType "string" ;
            ada:fieldScope "session" ;
            ada:tier "R" ],
        [ a schema1:PropertyValueSpecification ;
            schema1:defaultValue "15" ;
            schema1:description "Electron beam accelerating voltage in kilovolts (kV)." ;
            schema1:name "Default Accelerating Voltage" ;
            schema1:readonlyValue true ;
            schema1:valueName "acceleratingVoltage" ;
            ada:dataType "string" ;
            ada:fieldScope "session" ;
            ada:tier "R" ] .


```


### empaTAPP example P8: Zega et al. 2025 (Bennu mineralogy, Nat. Geosci.)
empaTAPP instance derived from publication Zega et al. 2025 (Bennu mineralogy, Nat. Geosci.). Property and parameter values taken from the corresponding column of the TAPP_EPMA_filled.xlsx 'TAPP' worksheet.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/"
  },
  "@id": "ex:empaTAPP-p8",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EMPA major element minerals (silicates, sulfides, oxides, carbonates, phosphates)",
  "schema:description": "empaTAPP example derived from Zega et al. 2025 (Bennu mineralogy, Nat. Geosci.).",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "EPMA-WDS",
    "schema:name": "Electron Microprobe Analysis - WDS"
  },
  "schema:agent": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "Zega et al."
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "University of Arizona (K-ALFAA); NASA JSC"
  },
  "schema:instrument": {
    "@type": [
      "schema:Thing",
      "schema:Product",
      "https://w3id.org/nfdi4ing/metadata4ing#Instrument"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      "ada:EPMAInstrument"
    ],
    "schema:name": "Cameca; JEOL Cameca SX-100 Ultra (U of Arizona); JEOL 7600F SEM with WDS (JSC)",
    "schema:manufacturer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Cameca; JEOL"
    },
    "schema:model": {
      "@type": [
        "schema:ProductModel"
      ],
      "schema:name": "Cameca SX-100 Ultra (U of Arizona); JEOL 7600F SEM with WDS (JSC)"
    }
  },
  "ada:acceleratingVoltageDefault": "15",
  "ada:beamDiameterDefault": "~1 µm focused (silicates/sulfides/oxides); variable for carbonates/phosphates",
  "ada:beamCurrentDefault": "20 nA (X-ray maps/BSE); \n20 nA silicates/sulfides/oxides;\n8 nA phosphates; \n4 nA carbonates",
  "ada:methodParameters": [
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Default Accelerating Voltage",
      "schema:valueName": "acceleratingVoltage",
      "schema:description": "Electron beam accelerating voltage in kilovolts (kV).",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "15"
    },
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Default Beam Diameter",
      "schema:valueName": "beamDiameter",
      "schema:description": "Diameter of the focused or defocused electron beam in micrometers.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "~1 µm focused (silicates/sulfides/oxides); variable for carbonates/phosphates"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "ada": "https://ada.astromat.org/metadata/",
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/techniqueProtocols/empaTAPP/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/"
    }
  ],
  "@id": "ex:empaTAPP-p8",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EMPA major element minerals (silicates, sulfides, oxides, carbonates, phosphates)",
  "schema:description": "empaTAPP example derived from Zega et al. 2025 (Bennu mineralogy, Nat. Geosci.).",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "EPMA-WDS",
    "schema:name": "Electron Microprobe Analysis - WDS"
  },
  "schema:agent": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "Zega et al."
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "University of Arizona (K-ALFAA); NASA JSC"
  },
  "schema:instrument": {
    "@type": [
      "schema:Thing",
      "schema:Product",
      "https://w3id.org/nfdi4ing/metadata4ing#Instrument"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      "ada:EPMAInstrument"
    ],
    "schema:name": "Cameca; JEOL Cameca SX-100 Ultra (U of Arizona); JEOL 7600F SEM with WDS (JSC)",
    "schema:manufacturer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Cameca; JEOL"
    },
    "schema:model": {
      "@type": [
        "schema:ProductModel"
      ],
      "schema:name": "Cameca SX-100 Ultra (U of Arizona); JEOL 7600F SEM with WDS (JSC)"
    }
  },
  "ada:acceleratingVoltageDefault": "15",
  "ada:beamDiameterDefault": "~1 \u00b5m focused (silicates/sulfides/oxides); variable for carbonates/phosphates",
  "ada:beamCurrentDefault": "20 nA (X-ray maps/BSE); \n20 nA silicates/sulfides/oxides;\n8 nA phosphates; \n4 nA carbonates",
  "ada:methodParameters": [
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Default Accelerating Voltage",
      "schema:valueName": "acceleratingVoltage",
      "schema:description": "Electron beam accelerating voltage in kilovolts (kV).",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "15"
    },
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Default Beam Diameter",
      "schema:valueName": "beamDiameter",
      "schema:description": "Diameter of the focused or defocused electron beam in micrometers.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "~1 \u00b5m focused (silicates/sulfides/oxides); variable for carbonates/phosphates"
    }
  ]
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix bios: <https://bioschemas.org/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:empaTAPP-p8> a cdi:Activity,
        schema1:Action,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:agent [ a schema1:Person ;
            schema1:name "Zega et al." ] ;
    schema1:description "empaTAPP example derived from Zega et al. 2025 (Bennu mineralogy, Nat. Geosci.)." ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing,
                <https://w3id.org/nfdi4ing/metadata4ing#Instrument> ;
            schema1:additionalType "ada:EPMAInstrument",
                "nxs:BaseClass/NXinstrument" ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "Cameca; JEOL" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "Cameca SX-100 Ultra (U of Arizona); JEOL 7600F SEM with WDS (JSC)" ] ;
            schema1:name "Cameca; JEOL Cameca SX-100 Ultra (U of Arizona); JEOL 7600F SEM with WDS (JSC)" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "University of Arizona (K-ALFAA); NASA JSC" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "Electron Microprobe Analysis - WDS" ;
            schema1:termCode "EPMA-WDS" ] ;
    schema1:name "EMPA major element minerals (silicates, sulfides, oxides, carbonates, phosphates)" ;
    ada:acceleratingVoltageDefault "15" ;
    ada:beamCurrentDefault """20 nA (X-ray maps/BSE); 
20 nA silicates/sulfides/oxides;
8 nA phosphates; 
4 nA carbonates""" ;
    ada:beamDiameterDefault "~1 µm focused (silicates/sulfides/oxides); variable for carbonates/phosphates" ;
    ada:methodParameters [ a schema1:PropertyValueSpecification ;
            schema1:defaultValue "15" ;
            schema1:description "Electron beam accelerating voltage in kilovolts (kV)." ;
            schema1:name "Default Accelerating Voltage" ;
            schema1:readonlyValue true ;
            schema1:valueName "acceleratingVoltage" ;
            ada:dataType "string" ;
            ada:fieldScope "session" ;
            ada:tier "R" ],
        [ a schema1:PropertyValueSpecification ;
            schema1:defaultValue "~1 µm focused (silicates/sulfides/oxides); variable for carbonates/phosphates" ;
            schema1:description "Diameter of the focused or defocused electron beam in micrometers." ;
            schema1:name "Default Beam Diameter" ;
            schema1:readonlyValue true ;
            schema1:valueName "beamDiameter" ;
            ada:dataType "string" ;
            ada:fieldScope "session" ;
            ada:tier "R" ] .


```


### empaTAPP example P9: McCoy et al. 2025 (Bennu evaporites, Nature)
empaTAPP instance derived from publication McCoy et al. 2025 (Bennu evaporites, Nature). Property and parameter values taken from the corresponding column of the TAPP_EPMA_filled.xlsx 'TAPP' worksheet.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/"
  },
  "@id": "ex:empaTAPP-p9",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EMPA major element minerals (carbonates, phosphates, silicates, oxides)",
  "schema:description": "empaTAPP example derived from McCoy et al. 2025 (Bennu evaporites, Nature).",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "EPMA-WDS",
    "schema:name": "Electron Microprobe Analysis - WDS"
  },
  "schema:agent": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "McCoy et al."
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Smithsonian Institution NMNH; University of Arizona (K-ALFAA)"
  },
  "schema:instrument": {
    "@type": [
      "schema:Thing",
      "schema:Product",
      "https://w3id.org/nfdi4ing/metadata4ing#Instrument"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      "ada:EPMAInstrument"
    ],
    "schema:name": "JEOL; Cameca JEOL 8530 F+ Hyperprobe FEG (Smithsonian); Cameca SX-100 (U of Arizona)",
    "schema:manufacturer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "JEOL; Cameca"
    },
    "schema:model": {
      "@type": [
        "schema:ProductModel"
      ],
      "schema:name": "JEOL 8530 F+ Hyperprobe FEG (Smithsonian); Cameca SX-100 (U of Arizona)"
    }
  },
  "ada:acceleratingVoltageDefault": "15",
  "ada:beamDiameterDefault": "1 µm (oxides/olivine); 5 µm (carbonates); 2 µm (Mg,Na phosphate)",
  "ada:beamCurrentDefault": "10 nA (carbonate/Mg,Na phosphate); \n10 nA (oxides/olivine, 1 µm)",
  "ada:methodParameters": [
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Default Accelerating Voltage",
      "schema:valueName": "acceleratingVoltage",
      "schema:description": "Electron beam accelerating voltage in kilovolts (kV).",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "15"
    },
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Default Beam Diameter",
      "schema:valueName": "beamDiameter",
      "schema:description": "Diameter of the focused or defocused electron beam in micrometers.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "1 µm (oxides/olivine); 5 µm (carbonates); 2 µm (Mg,Na phosphate)"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "ada": "https://ada.astromat.org/metadata/",
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/techniqueProtocols/empaTAPP/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/"
    }
  ],
  "@id": "ex:empaTAPP-p9",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EMPA major element minerals (carbonates, phosphates, silicates, oxides)",
  "schema:description": "empaTAPP example derived from McCoy et al. 2025 (Bennu evaporites, Nature).",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "EPMA-WDS",
    "schema:name": "Electron Microprobe Analysis - WDS"
  },
  "schema:agent": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "McCoy et al."
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Smithsonian Institution NMNH; University of Arizona (K-ALFAA)"
  },
  "schema:instrument": {
    "@type": [
      "schema:Thing",
      "schema:Product",
      "https://w3id.org/nfdi4ing/metadata4ing#Instrument"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      "ada:EPMAInstrument"
    ],
    "schema:name": "JEOL; Cameca JEOL 8530 F+ Hyperprobe FEG (Smithsonian); Cameca SX-100 (U of Arizona)",
    "schema:manufacturer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "JEOL; Cameca"
    },
    "schema:model": {
      "@type": [
        "schema:ProductModel"
      ],
      "schema:name": "JEOL 8530 F+ Hyperprobe FEG (Smithsonian); Cameca SX-100 (U of Arizona)"
    }
  },
  "ada:acceleratingVoltageDefault": "15",
  "ada:beamDiameterDefault": "1 \u00b5m (oxides/olivine); 5 \u00b5m (carbonates); 2 \u00b5m (Mg,Na phosphate)",
  "ada:beamCurrentDefault": "10 nA (carbonate/Mg,Na phosphate); \n10 nA (oxides/olivine, 1 \u00b5m)",
  "ada:methodParameters": [
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Default Accelerating Voltage",
      "schema:valueName": "acceleratingVoltage",
      "schema:description": "Electron beam accelerating voltage in kilovolts (kV).",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "15"
    },
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Default Beam Diameter",
      "schema:valueName": "beamDiameter",
      "schema:description": "Diameter of the focused or defocused electron beam in micrometers.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "1 \u00b5m (oxides/olivine); 5 \u00b5m (carbonates); 2 \u00b5m (Mg,Na phosphate)"
    }
  ]
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix bios: <https://bioschemas.org/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:empaTAPP-p9> a cdi:Activity,
        schema1:Action,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:agent [ a schema1:Person ;
            schema1:name "McCoy et al." ] ;
    schema1:description "empaTAPP example derived from McCoy et al. 2025 (Bennu evaporites, Nature)." ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing,
                <https://w3id.org/nfdi4ing/metadata4ing#Instrument> ;
            schema1:additionalType "ada:EPMAInstrument",
                "nxs:BaseClass/NXinstrument" ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "JEOL; Cameca" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "JEOL 8530 F+ Hyperprobe FEG (Smithsonian); Cameca SX-100 (U of Arizona)" ] ;
            schema1:name "JEOL; Cameca JEOL 8530 F+ Hyperprobe FEG (Smithsonian); Cameca SX-100 (U of Arizona)" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "Smithsonian Institution NMNH; University of Arizona (K-ALFAA)" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "Electron Microprobe Analysis - WDS" ;
            schema1:termCode "EPMA-WDS" ] ;
    schema1:name "EMPA major element minerals (carbonates, phosphates, silicates, oxides)" ;
    ada:acceleratingVoltageDefault "15" ;
    ada:beamCurrentDefault """10 nA (carbonate/Mg,Na phosphate); 
10 nA (oxides/olivine, 1 µm)""" ;
    ada:beamDiameterDefault "1 µm (oxides/olivine); 5 µm (carbonates); 2 µm (Mg,Na phosphate)" ;
    ada:methodParameters [ a schema1:PropertyValueSpecification ;
            schema1:defaultValue "15" ;
            schema1:description "Electron beam accelerating voltage in kilovolts (kV)." ;
            schema1:name "Default Accelerating Voltage" ;
            schema1:readonlyValue true ;
            schema1:valueName "acceleratingVoltage" ;
            ada:dataType "string" ;
            ada:fieldScope "session" ;
            ada:tier "R" ],
        [ a schema1:PropertyValueSpecification ;
            schema1:defaultValue "1 µm (oxides/olivine); 5 µm (carbonates); 2 µm (Mg,Na phosphate)" ;
            schema1:description "Diameter of the focused or defocused electron beam in micrometers." ;
            schema1:name "Default Beam Diameter" ;
            schema1:readonlyValue true ;
            schema1:valueName "beamDiameter" ;
            ada:dataType "string" ;
            ada:fieldScope "session" ;
            ada:tier "R" ] .


```


### empaTAPP example P10: Pang et al. 2016 (NWA 8003 eucrite, Sci. Rep.)
empaTAPP instance derived from publication Pang et al. 2016 (NWA 8003 eucrite, Sci. Rep.). Property and parameter values taken from the corresponding column of the TAPP_EPMA_filled.xlsx 'TAPP' worksheet.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/"
  },
  "@id": "ex:empaTAPP-p10",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS major/minor element minerals",
  "schema:description": "empaTAPP example derived from Pang et al. 2016 (NWA 8003 eucrite, Sci. Rep.).",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "EPMA-WDS",
    "schema:name": "Electron Microprobe Analysis - WDS"
  },
  "schema:agent": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "Pang et al."
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Nanjing University"
  },
  "schema:instrument": {
    "@type": [
      "schema:Thing",
      "schema:Product",
      "https://w3id.org/nfdi4ing/metadata4ing#Instrument"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      "ada:EPMAInstrument"
    ],
    "schema:name": "JEOL JEOL 8100",
    "schema:manufacturer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "JEOL"
    },
    "schema:model": {
      "@type": [
        "schema:ProductModel"
      ],
      "schema:name": "JEOL 8100"
    }
  },
  "ada:acceleratingVoltageDefault": "15",
  "ada:beamDiameterDefault": "0 focused (most minerals); 2–5 µm defocused (plagioclase and polymorphs)",
  "ada:beamCurrentDefault": "20 nA",
  "ada:methodParameters": [
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Default Accelerating Voltage",
      "schema:valueName": "acceleratingVoltage",
      "schema:description": "Electron beam accelerating voltage in kilovolts (kV).",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "15"
    },
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Default Beam Diameter",
      "schema:valueName": "beamDiameter",
      "schema:description": "Diameter of the focused or defocused electron beam in micrometers.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "0 focused (most minerals); 2–5 µm defocused (plagioclase and polymorphs)"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "ada": "https://ada.astromat.org/metadata/",
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/techniqueProtocols/empaTAPP/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/"
    }
  ],
  "@id": "ex:empaTAPP-p10",
  "@type": [
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS major/minor element minerals",
  "schema:description": "empaTAPP example derived from Pang et al. 2016 (NWA 8003 eucrite, Sci. Rep.).",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:termCode": "EPMA-WDS",
    "schema:name": "Electron Microprobe Analysis - WDS"
  },
  "schema:agent": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "Pang et al."
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Nanjing University"
  },
  "schema:instrument": {
    "@type": [
      "schema:Thing",
      "schema:Product",
      "https://w3id.org/nfdi4ing/metadata4ing#Instrument"
    ],
    "schema:additionalType": [
      "nxs:BaseClass/NXinstrument",
      "ada:EPMAInstrument"
    ],
    "schema:name": "JEOL JEOL 8100",
    "schema:manufacturer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "JEOL"
    },
    "schema:model": {
      "@type": [
        "schema:ProductModel"
      ],
      "schema:name": "JEOL 8100"
    }
  },
  "ada:acceleratingVoltageDefault": "15",
  "ada:beamDiameterDefault": "0 focused (most minerals); 2\u20135 \u00b5m defocused (plagioclase and polymorphs)",
  "ada:beamCurrentDefault": "20 nA",
  "ada:methodParameters": [
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Default Accelerating Voltage",
      "schema:valueName": "acceleratingVoltage",
      "schema:description": "Electron beam accelerating voltage in kilovolts (kV).",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "15"
    },
    {
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:name": "Default Beam Diameter",
      "schema:valueName": "beamDiameter",
      "schema:description": "Diameter of the focused or defocused electron beam in micrometers.",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:readonlyValue": true,
      "ada:tier": "R",
      "schema:defaultValue": "0 focused (most minerals); 2\u20135 \u00b5m defocused (plagioclase and polymorphs)"
    }
  ]
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix bios: <https://bioschemas.org/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:empaTAPP-p10> a cdi:Activity,
        schema1:Action,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:agent [ a schema1:Person ;
            schema1:name "Pang et al." ] ;
    schema1:description "empaTAPP example derived from Pang et al. 2016 (NWA 8003 eucrite, Sci. Rep.)." ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing,
                <https://w3id.org/nfdi4ing/metadata4ing#Instrument> ;
            schema1:additionalType "ada:EPMAInstrument",
                "nxs:BaseClass/NXinstrument" ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "JEOL" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "JEOL 8100" ] ;
            schema1:name "JEOL JEOL 8100" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "Nanjing University" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "Electron Microprobe Analysis - WDS" ;
            schema1:termCode "EPMA-WDS" ] ;
    schema1:name "EPMA-WDS major/minor element minerals" ;
    ada:acceleratingVoltageDefault "15" ;
    ada:beamCurrentDefault "20 nA" ;
    ada:beamDiameterDefault "0 focused (most minerals); 2–5 µm defocused (plagioclase and polymorphs)" ;
    ada:methodParameters [ a schema1:PropertyValueSpecification ;
            schema1:defaultValue "0 focused (most minerals); 2–5 µm defocused (plagioclase and polymorphs)" ;
            schema1:description "Diameter of the focused or defocused electron beam in micrometers." ;
            schema1:name "Default Beam Diameter" ;
            schema1:readonlyValue true ;
            schema1:valueName "beamDiameter" ;
            ada:dataType "string" ;
            ada:fieldScope "session" ;
            ada:tier "R" ],
        [ a schema1:PropertyValueSpecification ;
            schema1:defaultValue "15" ;
            schema1:description "Electron beam accelerating voltage in kilovolts (kV)." ;
            schema1:name "Default Accelerating Voltage" ;
            schema1:readonlyValue true ;
            schema1:valueName "acceleratingVoltage" ;
            ada:dataType "string" ;
            ada:fieldScope "session" ;
            ada:tier "R" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: EMPA Technique-Aligned Protocol Profile (empaTAPP)
description: EMPA-specific extension of the base TAPP definition. Adds top-level EPMA
  properties (beam mode, accelerating voltage default, matrix correction method, etc.),
  a parameter vocabulary in ada:methodParameters, and an analyte-column template covering
  EPMA per-element acquisition and reporting fields. Each ada:analyteColumns[] entry
  must match one of the catalog files in analyteColumns/ (or the inherited identifier
  column from tappDefinition); each catalog file is itself a JSON Schema whose examples[0]
  carries the canonical instance. Generated from docs/TAPP_EPMA_filled.xlsx by tools/build_empaTAPP_from_spreadsheet.py.
allOf:
- $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/techniqueProtocols/tappDefinition/schema.yaml
- type: object
  properties:
    ada:beamMode:
      description: Whether the beam was focused, defocused, or rastered over an area.
      type: string
      enum:
      - Focused
      - Defocused
      - Raster
    ada:acceleratingVoltageDefault:
      description: Electron beam accelerating voltage in kilovolts (kV).
      type: string
    ada:beamDiameterDefault:
      description: Diameter of the focused or defocused electron beam in micrometers.
      type: string
    ada:beamCurrentDefault:
      description: Probe current in nanoamperes (nA).
      type: string
    ada:matrixCorrectionMethod:
      description: X-ray matrix correction algorithm applied during data reduction.
      type: string
      enum:
      - PAP (Pouchou & Pichoir Full)
      - XPP (Simplified PAP)
      - PhiRhoZ Bastin (EPQ-91)
      - Love-Scott I
      - Love-Scott II
      - Armstrong/Love-Scott
      - Heinrich/Duncumb-Reed
      - Conventional Philibert/Duncumb-Reed
      - Other
      - Unknown
    ada:analyteTemplate:
      type: object
      properties:
        ada:analyteColumns:
          type: array
          items:
            oneOf:
            - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/techniqueProtocols/tappDefinition/schema.yaml#/$defs/AnalyteIdentifierColumn
            - $ref: https://usgin.github.io/geochemBuildingBlocks/_sources/techniqueProtocols/empaTAPP/analyteColumns/analysisOrder.json
            - $ref: https://usgin.github.io/geochemBuildingBlocks/_sources/techniqueProtocols/empaTAPP/analyteColumns/backgroundCorrectionMethod.json
            - $ref: https://usgin.github.io/geochemBuildingBlocks/_sources/techniqueProtocols/empaTAPP/analyteColumns/backgroundCountingPosition.json
            - $ref: https://usgin.github.io/geochemBuildingBlocks/_sources/techniqueProtocols/empaTAPP/analyteColumns/backgroundCountingTime.json
            - $ref: https://usgin.github.io/geochemBuildingBlocks/_sources/techniqueProtocols/empaTAPP/analyteColumns/blankCorrection.json
            - $ref: https://usgin.github.io/geochemBuildingBlocks/_sources/techniqueProtocols/empaTAPP/analyteColumns/detectionLimitMethod.json
            - $ref: https://usgin.github.io/geochemBuildingBlocks/_sources/techniqueProtocols/empaTAPP/analyteColumns/edsDeadTime.json
            - $ref: https://usgin.github.io/geochemBuildingBlocks/_sources/techniqueProtocols/empaTAPP/analyteColumns/elementEstimationMethod.json
            - $ref: https://usgin.github.io/geochemBuildingBlocks/_sources/techniqueProtocols/empaTAPP/analyteColumns/epmaTechnique.json
            - $ref: https://usgin.github.io/geochemBuildingBlocks/_sources/techniqueProtocols/empaTAPP/analyteColumns/interferenceCorrection.json
            - $ref: https://usgin.github.io/geochemBuildingBlocks/_sources/techniqueProtocols/empaTAPP/analyteColumns/interferenceCorrectionStandard.json
            - $ref: https://usgin.github.io/geochemBuildingBlocks/_sources/techniqueProtocols/empaTAPP/analyteColumns/interferingElements.json
            - $ref: https://usgin.github.io/geochemBuildingBlocks/_sources/techniqueProtocols/empaTAPP/analyteColumns/monochromatorCrystal.json
            - $ref: https://usgin.github.io/geochemBuildingBlocks/_sources/techniqueProtocols/empaTAPP/analyteColumns/normalization-standardsCorrection.json
            - $ref: https://usgin.github.io/geochemBuildingBlocks/_sources/techniqueProtocols/empaTAPP/analyteColumns/peakCountingTime.json
            - $ref: https://usgin.github.io/geochemBuildingBlocks/_sources/techniqueProtocols/empaTAPP/analyteColumns/primaryCalibrationStandard.json
            - $ref: https://usgin.github.io/geochemBuildingBlocks/_sources/techniqueProtocols/empaTAPP/analyteColumns/pulseHeightAnalyzeSetting.json
            - $ref: https://usgin.github.io/geochemBuildingBlocks/_sources/techniqueProtocols/empaTAPP/analyteColumns/secondaryReferenceMaterial.json
            - $ref: https://usgin.github.io/geochemBuildingBlocks/_sources/techniqueProtocols/empaTAPP/analyteColumns/spectrometerNumber.json
            - $ref: https://usgin.github.io/geochemBuildingBlocks/_sources/techniqueProtocols/empaTAPP/analyteColumns/timeDependentIntensityCorrection.json
            - $ref: https://usgin.github.io/geochemBuildingBlocks/_sources/techniqueProtocols/empaTAPP/analyteColumns/typicalAnalyticalAccuracy.json
            - $ref: https://usgin.github.io/geochemBuildingBlocks/_sources/techniqueProtocols/empaTAPP/analyteColumns/typicalAnalyticalPrecision.json
            - $ref: https://usgin.github.io/geochemBuildingBlocks/_sources/techniqueProtocols/empaTAPP/analyteColumns/typicalCountingStatisticsError.json
            - $ref: https://usgin.github.io/geochemBuildingBlocks/_sources/techniqueProtocols/empaTAPP/analyteColumns/typicalDetectionLimit.json
            - $ref: https://usgin.github.io/geochemBuildingBlocks/_sources/techniqueProtocols/empaTAPP/analyteColumns/wdsDetectorType.json
            - $ref: https://usgin.github.io/geochemBuildingBlocks/_sources/techniqueProtocols/empaTAPP/analyteColumns/xrayEmissionLine.json

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/techniqueProtocols/empaTAPP/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/techniqueProtocols/empaTAPP/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "prov": "http://www.w3.org/ns/prov#",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/",
    "dqv": "http://www.w3.org/ns/dqv#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/techniqueProtocols/empaTAPP/context.jsonld)

## Sources

* [TAPP_EPMA_filled.xlsx (Components / TAPP worksheet)](https://github.com/usgin/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/techniqueProtocols/empaTAPP`

