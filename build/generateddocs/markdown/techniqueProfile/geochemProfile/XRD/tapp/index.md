
# XRD Technique-Aligned Procedure Profile (xrdTAPP) (Schema)

`ogch.techniqueProfile.geochemProfile.XRD.tapp` *v0.1*

X-ray diffraction extension of the base TAPP definition. XRD reports phases rather than per-element concentrations, so no ada:analyteTemplate is defined; no mode-flag columns, since it delivers a single technique componentType. DRAFT - generated from draftTAPPs/XRD_TAPP_draft_v2.csv by tools/build_tapp.py; the source table has not been through Phase 0 review.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### xrdTAPP example King2024
xrdTAPP instance derived from ADA n=2 | King2024 | Natural History Museum | (NHM)Position Sensitive Detector X-ray Diffraction.
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
  "@id": "ex:xrdTAPP-King2024",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "xrd protocol — King2024",
  "schema:description": "xrdTAPP instance derived from ADA n=2 | King2024 | Natural History Museum | (NHM)Position Sensitive Detector X-ray Diffraction (publication column of XRD_TAPP_draft_v2.csv).",
  "ada:instrumentManufacturer": "Custom-built",
  "ada:instrumentModel": "(NHM)Position Sensitive Detector X-ray Diffraction",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "X-ray diffraction"
    }
  ],
  "schema:creator": {
    "schema:name": "King, Ashley",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Natural History Museum",
    "schema:identifier": "https://ror.org/039zvsn29"
  },
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program."
    }
  ],
  "ada:reportedProperties": [
    "Angle (degrees 2theta) | Intensity (counts)"
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
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:diffractometerGeometry": "missing",
  "ada:sampleMountDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stepSizeDefault": -9999,
  "ada:targetMaterial": "missing",
  "ada:timePerStepDefault": -9999,
  "ada:xRayWavelength": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XRD/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:xrdTAPP-King2024",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "xrd protocol \u2014 King2024",
  "schema:description": "xrdTAPP instance derived from ADA n=2 | King2024 | Natural History Museum | (NHM)Position Sensitive Detector X-ray Diffraction (publication column of XRD_TAPP_draft_v2.csv).",
  "ada:instrumentManufacturer": "Custom-built",
  "ada:instrumentModel": "(NHM)Position Sensitive Detector X-ray Diffraction",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "X-ray diffraction"
    }
  ],
  "schema:creator": {
    "schema:name": "King, Ashley",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Natural History Museum",
    "schema:identifier": "https://ror.org/039zvsn29"
  },
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program."
    }
  ],
  "ada:reportedProperties": [
    "Angle (degrees 2theta) | Intensity (counts)"
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
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:diffractometerGeometry": "missing",
  "ada:sampleMountDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stepSizeDefault": -9999,
  "ada:targetMaterial": "missing",
  "ada:timePerStepDefault": -9999,
  "ada:xRayWavelength": -9999,
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

ex:xrdTAPP-King2024 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "missing" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ] ] ;
    schema1:creator [ a schema1:Person ;
            schema1:name "King, Ashley" ] ;
    schema1:datePublished "missing" ;
    schema1:description "xrdTAPP instance derived from ADA n=2 | King2024 | Natural History Museum | (NHM)Position Sensitive Detector X-ray Diffraction (publication column of XRD_TAPP_draft_v2.csv)." ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program." ] ;
    schema1:location [ a schema1:Place ;
            schema1:identifier "https://ror.org/039zvsn29" ;
            schema1:name "Natural History Museum" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "X-ray diffraction" ] ;
    schema1:name "xrd protocol — King2024" ;
    schema1:variableMeasured [ schema1:defaultValue "missing" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:constantsAndReferenceValuesUsedDefault "missing" ;
    ada:diffractometerGeometry "missing" ;
    ada:instrumentManufacturer "Custom-built" ;
    ada:instrumentModel "(NHM)Position Sensitive Detector X-ray Diffraction" ;
    ada:reportedProperties "Angle (degrees 2theta) | Intensity (counts)" ;
    ada:sampleMountDefault "missing" ;
    ada:samplingUnit "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:stepSizeDefault -9999 ;
    ada:targetMaterial "missing" ;
    ada:timePerStepDefault -9999 ;
    ada:xRayWavelength -9999 .


```


### xrdTAPP example King2024-2
xrdTAPP instance derived from ADA n=1 | King2024 | NASA Johnson Space Center | (JSC-ARES)Malvern PANalytical XPert Pro XRD.
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
  "@id": "ex:xrdTAPP-King2024-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "xrd protocol — King2024-2",
  "schema:description": "xrdTAPP instance derived from ADA n=1 | King2024 | NASA Johnson Space Center | (JSC-ARES)Malvern PANalytical XPert Pro XRD (publication column of XRD_TAPP_draft_v2.csv).",
  "ada:instrumentManufacturer": "Malvern PANalytical",
  "ada:instrumentModel": "(JSC-ARES)Malvern PANalytical XPert Pro XRD",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "X-ray diffraction"
    }
  ],
  "schema:creator": {
    "schema:name": "King, Ashley",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "NASA Johnson Space Center",
    "schema:identifier": "https://ror.org/04xx4z452"
  },
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program."
    }
  ],
  "ada:reportedProperties": [
    "Angle (degrees 2theta) | Intensity (counts)"
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
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:diffractometerGeometry": "missing",
  "ada:sampleMountDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stepSizeDefault": -9999,
  "ada:targetMaterial": "missing",
  "ada:timePerStepDefault": -9999,
  "ada:xRayWavelength": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XRD/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:xrdTAPP-King2024-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "xrd protocol \u2014 King2024-2",
  "schema:description": "xrdTAPP instance derived from ADA n=1 | King2024 | NASA Johnson Space Center | (JSC-ARES)Malvern PANalytical XPert Pro XRD (publication column of XRD_TAPP_draft_v2.csv).",
  "ada:instrumentManufacturer": "Malvern PANalytical",
  "ada:instrumentModel": "(JSC-ARES)Malvern PANalytical XPert Pro XRD",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "X-ray diffraction"
    }
  ],
  "schema:creator": {
    "schema:name": "King, Ashley",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "NASA Johnson Space Center",
    "schema:identifier": "https://ror.org/04xx4z452"
  },
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program."
    }
  ],
  "ada:reportedProperties": [
    "Angle (degrees 2theta) | Intensity (counts)"
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
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:diffractometerGeometry": "missing",
  "ada:sampleMountDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stepSizeDefault": -9999,
  "ada:targetMaterial": "missing",
  "ada:timePerStepDefault": -9999,
  "ada:xRayWavelength": -9999,
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

ex:xrdTAPP-King2024-2 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "missing" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ] ] ;
    schema1:creator [ a schema1:Person ;
            schema1:name "King, Ashley" ] ;
    schema1:datePublished "missing" ;
    schema1:description "xrdTAPP instance derived from ADA n=1 | King2024 | NASA Johnson Space Center | (JSC-ARES)Malvern PANalytical XPert Pro XRD (publication column of XRD_TAPP_draft_v2.csv)." ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program." ] ;
    schema1:location [ a schema1:Place ;
            schema1:identifier "https://ror.org/04xx4z452" ;
            schema1:name "NASA Johnson Space Center" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "X-ray diffraction" ] ;
    schema1:name "xrd protocol — King2024-2" ;
    schema1:variableMeasured [ schema1:defaultValue "missing" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:constantsAndReferenceValuesUsedDefault "missing" ;
    ada:diffractometerGeometry "missing" ;
    ada:instrumentManufacturer "Malvern PANalytical" ;
    ada:instrumentModel "(JSC-ARES)Malvern PANalytical XPert Pro XRD" ;
    ada:reportedProperties "Angle (degrees 2theta) | Intensity (counts)" ;
    ada:sampleMountDefault "missing" ;
    ada:samplingUnit "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:stepSizeDefault -9999 ;
    ada:targetMaterial "missing" ;
    ada:timePerStepDefault -9999 ;
    ada:xRayWavelength -9999 .


```


### xrdTAPP example King2023
xrdTAPP instance derived from ADA n=1 | King2023 | Natural History Museum | Rigaku Rapid 2 Micro-XRD.
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
  "@id": "ex:xrdTAPP-King2023",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "xrd protocol — King2023",
  "schema:description": "xrdTAPP instance derived from ADA n=1 | King2023 | Natural History Museum | Rigaku Rapid 2 Micro-XRD (publication column of XRD_TAPP_draft_v2.csv).",
  "ada:instrumentManufacturer": "Rigaku",
  "ada:instrumentModel": "Rigaku Rapid 2 Micro-XRD",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "X-ray diffraction"
    }
  ],
  "schema:creator": {
    "schema:name": "King, Ashley",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Natural History Museum",
    "schema:identifier": "https://ror.org/039zvsn29"
  },
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program."
    }
  ],
  "ada:reportedProperties": [
    "Angle (degrees 2theta) | Intensity (counts)"
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
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:diffractometerGeometry": "missing",
  "ada:sampleMountDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stepSizeDefault": -9999,
  "ada:targetMaterial": "missing",
  "ada:timePerStepDefault": -9999,
  "ada:xRayWavelength": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XRD/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:xrdTAPP-King2023",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "xrd protocol \u2014 King2023",
  "schema:description": "xrdTAPP instance derived from ADA n=1 | King2023 | Natural History Museum | Rigaku Rapid 2 Micro-XRD (publication column of XRD_TAPP_draft_v2.csv).",
  "ada:instrumentManufacturer": "Rigaku",
  "ada:instrumentModel": "Rigaku Rapid 2 Micro-XRD",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "X-ray diffraction"
    }
  ],
  "schema:creator": {
    "schema:name": "King, Ashley",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Natural History Museum",
    "schema:identifier": "https://ror.org/039zvsn29"
  },
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program."
    }
  ],
  "ada:reportedProperties": [
    "Angle (degrees 2theta) | Intensity (counts)"
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
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:diffractometerGeometry": "missing",
  "ada:sampleMountDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stepSizeDefault": -9999,
  "ada:targetMaterial": "missing",
  "ada:timePerStepDefault": -9999,
  "ada:xRayWavelength": -9999,
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

ex:xrdTAPP-King2023 a cdi:Activity,
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
            schema1:name "King, Ashley" ] ;
    schema1:datePublished "missing" ;
    schema1:description "xrdTAPP instance derived from ADA n=1 | King2023 | Natural History Museum | Rigaku Rapid 2 Micro-XRD (publication column of XRD_TAPP_draft_v2.csv)." ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program." ] ;
    schema1:location [ a schema1:Place ;
            schema1:identifier "https://ror.org/039zvsn29" ;
            schema1:name "Natural History Museum" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "X-ray diffraction" ] ;
    schema1:name "xrd protocol — King2023" ;
    schema1:variableMeasured [ schema1:defaultValue "missing" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:constantsAndReferenceValuesUsedDefault "missing" ;
    ada:diffractometerGeometry "missing" ;
    ada:instrumentManufacturer "Rigaku" ;
    ada:instrumentModel "Rigaku Rapid 2 Micro-XRD" ;
    ada:reportedProperties "Angle (degrees 2theta) | Intensity (counts)" ;
    ada:sampleMountDefault "missing" ;
    ada:samplingUnit "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:stepSizeDefault -9999 ;
    ada:targetMaterial "missing" ;
    ada:timePerStepDefault -9999 ;
    ada:xRayWavelength -9999 .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: XRD Technique-Aligned Procedure Profile (xrdTAPP)
description: X-ray diffraction extension of the base TAPP definition. XRD reports
  phases rather than per-element concentrations, so no ada:analyteTemplate is defined;
  no mode-flag columns, since it delivers a single technique componentType. DRAFT
  - generated from draftTAPPs/XRD_TAPP_draft_v2.csv by tools/build_tapp.py; the source
  table has not been through Phase 0 review.
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
    ada:sampleMountDefault:
      description: The holder or mounting geometry the specimen is presented in. Distinct
        from Sample Preparation Method, which states how the material was brought
        to that form.
      anyOf:
      - type: string
        enum:
        - Zero-background holder
        - Capillary (transmission)
        - Flat plate (reflection)
        - Spinner stage
        - Fibre mount
        - N/A
        - None
        - missing
      - type: string
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
      - Malvern PANalytical
      - Rigaku
      - Bruker
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
    ada:diffractometerGeometry:
      description: Optical geometry of the diffractometer.
      anyOf:
      - type: string
        enum:
        - Bragg-Brentano (theta-2theta)
        - Debye-Scherrer (transmission)
        - Parallel beam
        - Micro-focus with area detector
        - N/A
        - None
        - missing
      - type: string
      readOnly: true
    ada:xRayWavelength:
      description: Wavelength of the incident radiation, with the anode and any monochromator
        that selects it.
      anyOf:
      - type: number
      - type: string
      readOnly: true
    ada:stepSizeDefault:
      description: Angular increment between recorded points.
      anyOf:
      - type: number
      - type: string
    ada:timePerStepDefault:
      description: Counting time at each angular step.
      anyOf:
      - type: number
      - type: string
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
  - ada:sampleMountDefault
  - ada:instrumentManufacturer
  - ada:instrumentModel
  - ada:diffractometerGeometry
  - ada:xRayWavelength
  - ada:stepSizeDefault
  - ada:timePerStepDefault
  - ada:constantsAndReferenceValuesUsedDefault

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XRD/tapp/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XRD/tapp/schema.yaml)


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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XRD/tapp/context.jsonld)

## Sources

* [XRD_TAPP_draft_v2.csv (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/XRD/tapp`

