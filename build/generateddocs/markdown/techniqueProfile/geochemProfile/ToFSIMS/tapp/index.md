
# Time-of-Flight Secondary Ion Mass Spectrometer Technique-Aligned Procedure Profile (tofsimsTAPP) (Schema)

`ogch.techniqueProfile.geochemProfile.ToFSIMS.tapp` *v0.1*

Time-of-Flight Secondary Ion Mass Spectrometer extension of the base TAPP definition. CORE-ONLY DRAFT: the native technique layer is empty. ToFSIMS has no ADA detail schema and no technique-specific property in any ADA record, so there was nothing to seed one from and none was invented. This registers the procedure skeleton and needs Phase 0 seed papers before it says anything ToFSIMS-specific. Generated from draftTAPPs/ToFSIMS_TAPP_draft_v2.csv by tools/build_tapp.py.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### tofsimsTAPP example P0
tofsimsTAPP instance derived from ADA n=3 | Rickard, William | Curtin University | IONTOF M6.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/",
    "prov": "http://www.w3.org/ns/prov#"
  },
  "@id": "ex:tofsimsTAPP-P0",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "tofsims protocol — P0",
  "schema:description": "tofsimsTAPP instance derived from ADA n=3 | Rickard, William | Curtin University | IONTOF M6 (publication column of ToFSIMS_TAPP_draft_v2.csv).",
  "ada:instrumentManufacturer": "Unknown",
  "ada:instrumentModel": "IONTOF M6",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Time-of-Flight Secondary Ion Mass Spectrometer"
    }
  ],
  "schema:creator": {
    "schema:name": "Rickard, William",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Curtin University"
  },
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "Australian Research Council LIEF190100053; Space Science and Technology Centre and the John de Laeter Centre at Curtin University."
    }
  ],
  "schema:actionProcess": {
    "@type": [
      "schema:HowTo"
    ],
    "schema:step": [
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Sample preparation",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 1,
        "schema:description": "missing"
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2
      }
    ]
  },
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:targetMaterial": "missing",
  "schema:datePublished": "missing"
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    },
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/ToFSIMS/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:tofsimsTAPP-P0",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "tofsims protocol \u2014 P0",
  "schema:description": "tofsimsTAPP instance derived from ADA n=3 | Rickard, William | Curtin University | IONTOF M6 (publication column of ToFSIMS_TAPP_draft_v2.csv).",
  "ada:instrumentManufacturer": "Unknown",
  "ada:instrumentModel": "IONTOF M6",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Time-of-Flight Secondary Ion Mass Spectrometer"
    }
  ],
  "schema:creator": {
    "schema:name": "Rickard, William",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Curtin University"
  },
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "Australian Research Council LIEF190100053; Space Science and Technology Centre and the John de Laeter Centre at Curtin University."
    }
  ],
  "schema:actionProcess": {
    "@type": [
      "schema:HowTo"
    ],
    "schema:step": [
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Sample preparation",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 1,
        "schema:description": "missing"
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2
      }
    ]
  },
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:targetMaterial": "missing",
  "schema:datePublished": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix bios: <https://bioschemas.org/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:tofsimsTAPP-P0 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "missing" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:creator [ a schema1:Person ;
            schema1:name "Rickard, William" ] ;
    schema1:datePublished "missing" ;
    schema1:description "tofsimsTAPP instance derived from ADA n=3 | Rickard, William | Curtin University | IONTOF M6 (publication column of ToFSIMS_TAPP_draft_v2.csv)." ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "Australian Research Council LIEF190100053; Space Science and Technology Centre and the John de Laeter Centre at Curtin University." ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "Curtin University" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Time-of-Flight Secondary Ion Mass Spectrometer" ] ;
    schema1:name "tofsims protocol — P0" ;
    ada:constantsAndReferenceValuesUsedDefault "missing" ;
    ada:instrumentManufacturer "Unknown" ;
    ada:instrumentModel "IONTOF M6" ;
    ada:samplingUnit "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:targetMaterial "missing" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Time-of-Flight Secondary Ion Mass Spectrometer Technique-Aligned Procedure
  Profile (tofsimsTAPP)
description: 'Time-of-Flight Secondary Ion Mass Spectrometer extension of the base
  TAPP definition. CORE-ONLY DRAFT: the native technique layer is empty. ToFSIMS has
  no ADA detail schema and no technique-specific property in any ADA record, so there
  was nothing to seed one from and none was invented. This registers the procedure
  skeleton and needs Phase 0 seed papers before it says anything ToFSIMS-specific.
  Generated from draftTAPPs/ToFSIMS_TAPP_draft_v2.csv by tools/build_tapp.py.'
allOf:
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/calibrationFactor/schema.yaml#/$defs/ProcedureIdentification
- type: object
  properties:
    ada:targetMaterial:
      description: General description of the material type(s) this procedure is designed
        to analyse.
      anyOf:
      - type: string
        enum:
        - Silicate mineral
        - Silicate glass
        - Oxide
        - Sulfide
        - Carbonate
        - Phosphate
        - Metal or alloy
        - Organic matter
        - Bulk regolith or soil
        - Meteorite (bulk)
        - Ice or hydrate
        - Synthetic analogue
        - N/A
        - None
        - missing
      - type: string
      readOnly: true
    schema:object:
      type: array
      items:
        type: object
        allOf:
        - if:
            properties:
              '@type':
                contains:
                  const: https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample
            required:
            - '@type'
          then:
            properties:
              schema:additionalProperty:
                type: array
                items:
                  $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Procedure_preAnalysisImagingAndScreening
                allOf:
                - contains:
                    $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Procedure_preAnalysisImagingAndScreening
                  minContains: 0
                  maxContains: 1
    ada:instrumentManufacturer:
      description: Manufacturer of the instrument that performs the measurement, recorded
        as a controlled value. Where a procedure couples a sample-introduction system
        to an analysing instrument, this records the analysing instrument. Instrument
        Model gives the specific designation.
      type: string
      enum:
      - WITec
      - Renishaw
      - HORIBA
      - Bruker
      - Thermo Fisher Scientific
      - Custom-built
      - Unknown
      - N/A
      - None
      - missing
      readOnly: true
    ada:instrumentModel:
      description: Model designation of the instrument that performs the measurement,
        including any generation or configuration suffix. Conventionally written with
        the manufacturer name included; Instrument Manufacturer records the vendor
        separately, as a controlled value, so that procedures remain findable by vendor.
      type: string
      readOnly: true
    ada:constantsAndReferenceValuesUsedDefault:
      description: Physical constants and reference values used in data reduction
        to calculate the final reported quantity (e.g., decay constants for age calculation,
        standard isotope ratios, or other citable reference values used in a correction
        or calculation), together with their source. Distinct from the Group 6 reference-material
        fields, which document accepted values for specific calibration/validation
        materials rather than universal physical constants. Record "None" if no citable,
        revisable physical constants feed into this procedure's data reduction.
      type: string
  required:
  - ada:targetMaterial
  - ada:instrumentManufacturer
  - ada:instrumentModel
  - ada:constantsAndReferenceValuesUsedDefault

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/ToFSIMS/tapp/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/ToFSIMS/tapp/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "prov": "http://www.w3.org/ns/prov#",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/",
    "nxs": "https://manual.nexusformat.org/classes/",
    "dqv": "http://www.w3.org/ns/dqv#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "wd": "https://www.wikidata.org/entity/",
    "cdif": "https://w3id.org/cdif/",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/ToFSIMS/tapp/context.jsonld)

## Sources

* [ToFSIMS_TAPP_draft_v2.csv (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/ToFSIMS/tapp`

