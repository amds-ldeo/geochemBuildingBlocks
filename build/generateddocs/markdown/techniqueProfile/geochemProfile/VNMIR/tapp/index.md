
# VNMIR Technique-Aligned Procedure Profile (vnmirTAPP) (Schema)

`ogch.techniqueProfile.geochemProfile.VNMIR.tapp` *v0.1*

Visible, near- and mid-infrared reflectance/emissivity spectroscopy extension of the base TAPP definition. Basic procedure-tier fields are required top-level ada: properties; Advanced procedure-tier fields are schema:additionalProperty[] PropertyValueSpecification entries. VNMIR has no per-element analyte axis, so no ada:analyteTemplate is defined. DRAFT - generated from draftTAPPs/VNMIR_TAPP_draft_v2.csv by tools/build_tapp.py; the source table has not been through Phase 0 review.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### vnmirTAPP example Hiroi2023
vnmirTAPP instance derived from ADA n=19 | Hiroi2023 | Brown U. | Thermo/Nicolet Nexus 870 FTIR.
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
  "@id": "ex:vnmirTAPP-Hiroi2023",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "vnmir protocol — Hiroi2023",
  "schema:description": "vnmirTAPP instance derived from ADA n=19 | Hiroi2023 | Brown U. | Thermo/Nicolet Nexus 870 FTIR (publication column of VNMIR_TAPP_draft_v2.csv).",
  "ada:instrumentManufacturer": "Thermo Fisher Scientific (Nicolet)",
  "ada:instrumentModel": "Thermo/Nicolet Nexus 870 FTIR",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Visible, near-, and mid-infrared spectroscopy"
    }
  ],
  "schema:creator": {
    "schema:name": "Hiroi, Takahiro",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Brown University",
    "schema:identifier": "https://ror.org/05gq02987"
  },
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "This material is supported by NASA PSEF grant. | NASA PSEF | (+1 more)"
    }
  ],
  "ada:analyticalMode": [
    "Spectral Point"
  ],
  "ada:reportedProperties": [
    "Wavelength (nm) (nm) | Reflectance | Reflectance (Reflectance) | Standard Deviation"
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
  "ada:beamsplitter": "missing",
  "ada:calibrationStandardsDefault": "missing",
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:detector": "missing",
  "ada:measurementEnvironmentDefault": "missing",
  "ada:measurementType": "missing",
  "ada:numberOfScansDefault": -9999,
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:spectralRangeMaximum": -9999,
  "ada:spectralRangeMinimum": -9999,
  "ada:spectralResolutionDefault": -9999,
  "ada:spotSizeDefault": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/VNMIR/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:vnmirTAPP-Hiroi2023",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "vnmir protocol \u2014 Hiroi2023",
  "schema:description": "vnmirTAPP instance derived from ADA n=19 | Hiroi2023 | Brown U. | Thermo/Nicolet Nexus 870 FTIR (publication column of VNMIR_TAPP_draft_v2.csv).",
  "ada:instrumentManufacturer": "Thermo Fisher Scientific (Nicolet)",
  "ada:instrumentModel": "Thermo/Nicolet Nexus 870 FTIR",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Visible, near-, and mid-infrared spectroscopy"
    }
  ],
  "schema:creator": {
    "schema:name": "Hiroi, Takahiro",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Brown University",
    "schema:identifier": "https://ror.org/05gq02987"
  },
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "This material is supported by NASA PSEF grant. | NASA PSEF | (+1 more)"
    }
  ],
  "ada:analyticalMode": [
    "Spectral Point"
  ],
  "ada:reportedProperties": [
    "Wavelength (nm) (nm) | Reflectance | Reflectance (Reflectance) | Standard Deviation"
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
  "ada:beamsplitter": "missing",
  "ada:calibrationStandardsDefault": "missing",
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:detector": "missing",
  "ada:measurementEnvironmentDefault": "missing",
  "ada:measurementType": "missing",
  "ada:numberOfScansDefault": -9999,
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:spectralRangeMaximum": -9999,
  "ada:spectralRangeMinimum": -9999,
  "ada:spectralResolutionDefault": -9999,
  "ada:spotSizeDefault": -9999,
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

ex:vnmirTAPP-Hiroi2023 a cdi:Activity,
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
            schema1:name "Hiroi, Takahiro" ] ;
    schema1:datePublished "missing" ;
    schema1:description "vnmirTAPP instance derived from ADA n=19 | Hiroi2023 | Brown U. | Thermo/Nicolet Nexus 870 FTIR (publication column of VNMIR_TAPP_draft_v2.csv)." ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "This material is supported by NASA PSEF grant. | NASA PSEF | (+1 more)" ] ;
    schema1:location [ a schema1:Place ;
            schema1:identifier "https://ror.org/05gq02987" ;
            schema1:name "Brown University" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Visible, near-, and mid-infrared spectroscopy" ] ;
    schema1:name "vnmir protocol — Hiroi2023" ;
    schema1:variableMeasured [ schema1:defaultValue "missing" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analyticalMode "Spectral Point" ;
    ada:beamsplitter "missing" ;
    ada:calibrationStandardsDefault "missing" ;
    ada:constantsAndReferenceValuesUsedDefault "missing" ;
    ada:detector "missing" ;
    ada:instrumentManufacturer "Thermo Fisher Scientific (Nicolet)" ;
    ada:instrumentModel "Thermo/Nicolet Nexus 870 FTIR" ;
    ada:measurementEnvironmentDefault "missing" ;
    ada:measurementType "missing" ;
    ada:numberOfScansDefault -9999 ;
    ada:reportedProperties "Wavelength (nm) (nm) | Reflectance | Reflectance (Reflectance) | Standard Deviation" ;
    ada:samplingUnit "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:spectralRangeMaximum -9999 ;
    ada:spectralRangeMinimum -9999 ;
    ada:spectralResolutionDefault -9999 ;
    ada:spotSizeDefault -9999 ;
    ada:targetMaterial "missing" .


```


### vnmirTAPP example Hiroi2023-2
vnmirTAPP instance derived from ADA n=13 | Hiroi2023 | Brown U. | Custom bi-directional.
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
  "@id": "ex:vnmirTAPP-Hiroi2023-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "vnmir protocol — Hiroi2023-2",
  "schema:description": "vnmirTAPP instance derived from ADA n=13 | Hiroi2023 | Brown U. | Custom bi-directional (publication column of VNMIR_TAPP_draft_v2.csv).",
  "ada:instrumentManufacturer": "Custom-built",
  "ada:instrumentModel": "Custom bi-directional",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Visible, near-, and mid-infrared spectroscopy"
    }
  ],
  "schema:creator": {
    "schema:name": "Hiroi, Takahiro",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Brown University",
    "schema:identifier": "https://ror.org/05gq02987"
  },
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "This material is supported by NASA PSEF grant. | This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program and NASA Planetary Science Enabling Facilities program 80NSSC23K0198. | (+1 more)"
    }
  ],
  "ada:analyticalMode": [
    "Spectral Point"
  ],
  "ada:reportedProperties": [
    "Wavelength (nm) (nm) | Reflectance | Standard Deviation | Reflectance (Reflectance) | Standard Deviation (Reflectance)"
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
  "ada:beamsplitter": "missing",
  "ada:calibrationStandardsDefault": "missing",
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:detector": "missing",
  "ada:measurementEnvironmentDefault": "missing",
  "ada:measurementType": "missing",
  "ada:numberOfScansDefault": -9999,
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:spectralRangeMaximum": -9999,
  "ada:spectralRangeMinimum": -9999,
  "ada:spectralResolutionDefault": -9999,
  "ada:spotSizeDefault": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/VNMIR/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:vnmirTAPP-Hiroi2023-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "vnmir protocol \u2014 Hiroi2023-2",
  "schema:description": "vnmirTAPP instance derived from ADA n=13 | Hiroi2023 | Brown U. | Custom bi-directional (publication column of VNMIR_TAPP_draft_v2.csv).",
  "ada:instrumentManufacturer": "Custom-built",
  "ada:instrumentModel": "Custom bi-directional",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Visible, near-, and mid-infrared spectroscopy"
    }
  ],
  "schema:creator": {
    "schema:name": "Hiroi, Takahiro",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Brown University",
    "schema:identifier": "https://ror.org/05gq02987"
  },
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "This material is supported by NASA PSEF grant. | This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program and NASA Planetary Science Enabling Facilities program 80NSSC23K0198. | (+1 more)"
    }
  ],
  "ada:analyticalMode": [
    "Spectral Point"
  ],
  "ada:reportedProperties": [
    "Wavelength (nm) (nm) | Reflectance | Standard Deviation | Reflectance (Reflectance) | Standard Deviation (Reflectance)"
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
  "ada:beamsplitter": "missing",
  "ada:calibrationStandardsDefault": "missing",
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:detector": "missing",
  "ada:measurementEnvironmentDefault": "missing",
  "ada:measurementType": "missing",
  "ada:numberOfScansDefault": -9999,
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:spectralRangeMaximum": -9999,
  "ada:spectralRangeMinimum": -9999,
  "ada:spectralResolutionDefault": -9999,
  "ada:spotSizeDefault": -9999,
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

ex:vnmirTAPP-Hiroi2023-2 a cdi:Activity,
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
            schema1:name "Hiroi, Takahiro" ] ;
    schema1:datePublished "missing" ;
    schema1:description "vnmirTAPP instance derived from ADA n=13 | Hiroi2023 | Brown U. | Custom bi-directional (publication column of VNMIR_TAPP_draft_v2.csv)." ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "This material is supported by NASA PSEF grant. | This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program and NASA Planetary Science Enabling Facilities program 80NSSC23K0198. | (+1 more)" ] ;
    schema1:location [ a schema1:Place ;
            schema1:identifier "https://ror.org/05gq02987" ;
            schema1:name "Brown University" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Visible, near-, and mid-infrared spectroscopy" ] ;
    schema1:name "vnmir protocol — Hiroi2023-2" ;
    schema1:variableMeasured [ schema1:defaultValue "missing" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analyticalMode "Spectral Point" ;
    ada:beamsplitter "missing" ;
    ada:calibrationStandardsDefault "missing" ;
    ada:constantsAndReferenceValuesUsedDefault "missing" ;
    ada:detector "missing" ;
    ada:instrumentManufacturer "Custom-built" ;
    ada:instrumentModel "Custom bi-directional" ;
    ada:measurementEnvironmentDefault "missing" ;
    ada:measurementType "missing" ;
    ada:numberOfScansDefault -9999 ;
    ada:reportedProperties "Wavelength (nm) (nm) | Reflectance | Standard Deviation | Reflectance (Reflectance) | Standard Deviation (Reflectance)" ;
    ada:samplingUnit "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:spectralRangeMaximum -9999 ;
    ada:spectralRangeMinimum -9999 ;
    ada:spectralResolutionDefault -9999 ;
    ada:spotSizeDefault -9999 ;
    ada:targetMaterial "missing" .


```


### vnmirTAPP example Milliken2024
vnmirTAPP instance derived from ADA n=2 | Milliken2024 | Brown U. | Bruker LUMOS FTIR microscope.
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
  "@id": "ex:vnmirTAPP-Milliken2024",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "vnmir protocol — Milliken2024",
  "schema:description": "vnmirTAPP instance derived from ADA n=2 | Milliken2024 | Brown U. | Bruker LUMOS FTIR microscope (publication column of VNMIR_TAPP_draft_v2.csv).",
  "ada:instrumentManufacturer": "Bruker",
  "ada:instrumentModel": "Bruker LUMOS FTIR microscope",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Visible, near-, and mid-infrared spectroscopy"
    }
  ],
  "schema:creator": {
    "schema:name": "Milliken, Ralph",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Brown University",
    "schema:identifier": "https://ror.org/05gq02987"
  },
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program."
    }
  ],
  "ada:analyticalMode": [
    "Spectral Point"
  ],
  "ada:reportedProperties": [
    "Wavenumber (cm-1) (cm-1) | Reflectance (Reflectance)"
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
  "ada:beamsplitter": "missing",
  "ada:calibrationStandardsDefault": "missing",
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:detector": "missing",
  "ada:measurementEnvironmentDefault": "missing",
  "ada:measurementType": "missing",
  "ada:numberOfScansDefault": -9999,
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:spectralRangeMaximum": -9999,
  "ada:spectralRangeMinimum": -9999,
  "ada:spectralResolutionDefault": -9999,
  "ada:spotSizeDefault": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/VNMIR/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:vnmirTAPP-Milliken2024",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "vnmir protocol \u2014 Milliken2024",
  "schema:description": "vnmirTAPP instance derived from ADA n=2 | Milliken2024 | Brown U. | Bruker LUMOS FTIR microscope (publication column of VNMIR_TAPP_draft_v2.csv).",
  "ada:instrumentManufacturer": "Bruker",
  "ada:instrumentModel": "Bruker LUMOS FTIR microscope",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Visible, near-, and mid-infrared spectroscopy"
    }
  ],
  "schema:creator": {
    "schema:name": "Milliken, Ralph",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Brown University",
    "schema:identifier": "https://ror.org/05gq02987"
  },
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program."
    }
  ],
  "ada:analyticalMode": [
    "Spectral Point"
  ],
  "ada:reportedProperties": [
    "Wavenumber (cm-1) (cm-1) | Reflectance (Reflectance)"
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
  "ada:beamsplitter": "missing",
  "ada:calibrationStandardsDefault": "missing",
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:detector": "missing",
  "ada:measurementEnvironmentDefault": "missing",
  "ada:measurementType": "missing",
  "ada:numberOfScansDefault": -9999,
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:spectralRangeMaximum": -9999,
  "ada:spectralRangeMinimum": -9999,
  "ada:spectralResolutionDefault": -9999,
  "ada:spotSizeDefault": -9999,
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

ex:vnmirTAPP-Milliken2024 a cdi:Activity,
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
            schema1:name "Milliken, Ralph" ] ;
    schema1:datePublished "missing" ;
    schema1:description "vnmirTAPP instance derived from ADA n=2 | Milliken2024 | Brown U. | Bruker LUMOS FTIR microscope (publication column of VNMIR_TAPP_draft_v2.csv)." ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program." ] ;
    schema1:location [ a schema1:Place ;
            schema1:identifier "https://ror.org/05gq02987" ;
            schema1:name "Brown University" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Visible, near-, and mid-infrared spectroscopy" ] ;
    schema1:name "vnmir protocol — Milliken2024" ;
    schema1:variableMeasured [ schema1:defaultValue "missing" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analyticalMode "Spectral Point" ;
    ada:beamsplitter "missing" ;
    ada:calibrationStandardsDefault "missing" ;
    ada:constantsAndReferenceValuesUsedDefault "missing" ;
    ada:detector "missing" ;
    ada:instrumentManufacturer "Bruker" ;
    ada:instrumentModel "Bruker LUMOS FTIR microscope" ;
    ada:measurementEnvironmentDefault "missing" ;
    ada:measurementType "missing" ;
    ada:numberOfScansDefault -9999 ;
    ada:reportedProperties "Wavenumber (cm-1) (cm-1) | Reflectance (Reflectance)" ;
    ada:samplingUnit "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:spectralRangeMaximum -9999 ;
    ada:spectralRangeMinimum -9999 ;
    ada:spectralResolutionDefault -9999 ;
    ada:spotSizeDefault -9999 ;
    ada:targetMaterial "missing" .


```


### vnmirTAPP example Keller2024
vnmirTAPP instance derived from ADA n=1 | Keller2024 | NASA Johnson Space Center | JEOL 2500SE.
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
  "@id": "ex:vnmirTAPP-Keller2024",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "vnmir protocol — Keller2024",
  "schema:description": "vnmirTAPP instance derived from ADA n=1 | Keller2024 | NASA Johnson Space Center | JEOL 2500SE (publication column of VNMIR_TAPP_draft_v2.csv).",
  "ada:instrumentManufacturer": "Unknown",
  "ada:instrumentModel": "JEOL 2500SE",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Visible, near-, and mid-infrared spectroscopy"
    }
  ],
  "schema:creator": {
    "schema:name": "Keller, Lindsay",
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
  "ada:analyticalMode": [
    "Spectral Point"
  ],
  "ada:reportedProperties": [
    "wavenumber (3999.49) | Clays (Percent transmission) | dolomite (Percent transmission) | calcite (Percent transmission) | MgPO4 (Percent transmission)"
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
  "ada:beamsplitter": "missing",
  "ada:calibrationStandardsDefault": "missing",
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:detector": "missing",
  "ada:measurementEnvironmentDefault": "missing",
  "ada:measurementType": "missing",
  "ada:numberOfScansDefault": -9999,
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:spectralRangeMaximum": -9999,
  "ada:spectralRangeMinimum": -9999,
  "ada:spectralResolutionDefault": -9999,
  "ada:spotSizeDefault": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/VNMIR/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:vnmirTAPP-Keller2024",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "vnmir protocol \u2014 Keller2024",
  "schema:description": "vnmirTAPP instance derived from ADA n=1 | Keller2024 | NASA Johnson Space Center | JEOL 2500SE (publication column of VNMIR_TAPP_draft_v2.csv).",
  "ada:instrumentManufacturer": "Unknown",
  "ada:instrumentModel": "JEOL 2500SE",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Visible, near-, and mid-infrared spectroscopy"
    }
  ],
  "schema:creator": {
    "schema:name": "Keller, Lindsay",
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
  "ada:analyticalMode": [
    "Spectral Point"
  ],
  "ada:reportedProperties": [
    "wavenumber (3999.49) | Clays (Percent transmission) | dolomite (Percent transmission) | calcite (Percent transmission) | MgPO4 (Percent transmission)"
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
  "ada:beamsplitter": "missing",
  "ada:calibrationStandardsDefault": "missing",
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:detector": "missing",
  "ada:measurementEnvironmentDefault": "missing",
  "ada:measurementType": "missing",
  "ada:numberOfScansDefault": -9999,
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:spectralRangeMaximum": -9999,
  "ada:spectralRangeMinimum": -9999,
  "ada:spectralResolutionDefault": -9999,
  "ada:spotSizeDefault": -9999,
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

ex:vnmirTAPP-Keller2024 a cdi:Activity,
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
            schema1:name "Keller, Lindsay" ] ;
    schema1:datePublished "missing" ;
    schema1:description "vnmirTAPP instance derived from ADA n=1 | Keller2024 | NASA Johnson Space Center | JEOL 2500SE (publication column of VNMIR_TAPP_draft_v2.csv)." ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program." ] ;
    schema1:location [ a schema1:Place ;
            schema1:identifier "https://ror.org/04xx4z452" ;
            schema1:name "NASA Johnson Space Center" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Visible, near-, and mid-infrared spectroscopy" ] ;
    schema1:name "vnmir protocol — Keller2024" ;
    schema1:variableMeasured [ schema1:defaultValue "missing" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analyticalMode "Spectral Point" ;
    ada:beamsplitter "missing" ;
    ada:calibrationStandardsDefault "missing" ;
    ada:constantsAndReferenceValuesUsedDefault "missing" ;
    ada:detector "missing" ;
    ada:instrumentManufacturer "Unknown" ;
    ada:instrumentModel "JEOL 2500SE" ;
    ada:measurementEnvironmentDefault "missing" ;
    ada:measurementType "missing" ;
    ada:numberOfScansDefault -9999 ;
    ada:reportedProperties "wavenumber (3999.49) | Clays (Percent transmission) | dolomite (Percent transmission) | calcite (Percent transmission) | MgPO4 (Percent transmission)" ;
    ada:samplingUnit "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:spectralRangeMaximum -9999 ;
    ada:spectralRangeMinimum -9999 ;
    ada:spectralResolutionDefault -9999 ;
    ada:spotSizeDefault -9999 ;
    ada:targetMaterial "missing" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: VNMIR Technique-Aligned Procedure Profile (vnmirTAPP)
description: 'Visible, near- and mid-infrared reflectance/emissivity spectroscopy
  extension of the base TAPP definition. Basic procedure-tier fields are required
  top-level ada: properties; Advanced procedure-tier fields are schema:additionalProperty[]
  PropertyValueSpecification entries. VNMIR has no per-element analyte axis, so no
  ada:analyteTemplate is defined. DRAFT - generated from draftTAPPs/VNMIR_TAPP_draft_v2.csv
  by tools/build_tapp.py; the source table has not been through Phase 0 review.'
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
                  anyOf:
                  - title: Sample Heated
                    description: Whether the sample was heated during measurement.
                      Record 'N/A' where the procedure does not control sample temperature.
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/vnmirTAPP/sampleHeatedDefault
                      '@type':
                        const:
                        - schema:PropertyValueSpecification
                      schema:valueName:
                        const: sampleHeatedDefault
                      schema:name:
                        const: Sample Heated
                      ada:dataType:
                        const: string
                      ada:fieldScope:
                        const: session
                      schema:readonlyValue:
                        const: false
                      ada:tier:
                        const: R
                    required:
                    - '@id'
                    - '@type'
                    - schema:valueName
                    - schema:name
                    - ada:dataType
                    - ada:fieldScope
                  - title: Vacuum Exposed Sample
                    description: Whether this sample was exposed to vacuum before
                      or during measurement, which alters adsorbed water and therefore
                      the spectrum.
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/vnmirTAPP/vacuumExposedSampleDefault
                      '@type':
                        const:
                        - schema:PropertyValueSpecification
                      schema:valueName:
                        const: vacuumExposedSampleDefault
                      schema:name:
                        const: Vacuum Exposed Sample
                      ada:dataType:
                        const: string
                      ada:fieldScope:
                        const: session
                      schema:readonlyValue:
                        const: false
                      ada:tier:
                        const: R
                    required:
                    - '@id'
                    - '@type'
                    - schema:valueName
                    - schema:name
                    - ada:dataType
                    - ada:fieldScope
                  - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Procedure_preAnalysisImagingAndScreening
                allOf:
                - contains:
                    title: Sample Heated
                    description: Whether the sample was heated during measurement.
                      Record 'N/A' where the procedure does not control sample temperature.
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/vnmirTAPP/sampleHeatedDefault
                      '@type':
                        const:
                        - schema:PropertyValueSpecification
                      schema:valueName:
                        const: sampleHeatedDefault
                      schema:name:
                        const: Sample Heated
                      ada:dataType:
                        const: string
                      ada:fieldScope:
                        const: session
                      schema:readonlyValue:
                        const: false
                      ada:tier:
                        const: R
                    required:
                    - '@id'
                    - '@type'
                    - schema:valueName
                    - schema:name
                    - ada:dataType
                    - ada:fieldScope
                  minContains: 0
                  maxContains: 1
                - contains:
                    title: Vacuum Exposed Sample
                    description: Whether this sample was exposed to vacuum before
                      or during measurement, which alters adsorbed water and therefore
                      the spectrum.
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/vnmirTAPP/vacuumExposedSampleDefault
                      '@type':
                        const:
                        - schema:PropertyValueSpecification
                      schema:valueName:
                        const: vacuumExposedSampleDefault
                      schema:name:
                        const: Vacuum Exposed Sample
                      ada:dataType:
                        const: string
                      ada:fieldScope:
                        const: session
                      schema:readonlyValue:
                        const: false
                      ada:tier:
                        const: R
                    required:
                    - '@id'
                    - '@type'
                    - schema:valueName
                    - schema:name
                    - ada:dataType
                    - ada:fieldScope
                  minContains: 0
                  maxContains: 1
                - contains:
                    $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Procedure_preAnalysisImagingAndScreening
                  minContains: 0
                  maxContains: 1
      allOf:
      - contains:
          properties:
            '@type':
              contains:
                const: https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample
          required:
          - '@type'
    ada:instrumentManufacturer:
      description: Manufacturer of the instrument that performs the measurement, recorded
        as a controlled value. Where a procedure couples a sample-introduction system
        to an analysing instrument, this records the analysing instrument. Instrument
        Model gives the specific designation.
      type: string
      enum:
      - Thermo Fisher Scientific (Nicolet)
      - Bruker
      - ASD / Malvern Panalytical
      - Agilent
      - PerkinElmer
      - Shimadzu
      - Analytik Jena
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
    ada:detector:
      description: Detector fitted to the spectrometer for this procedure.
      anyOf:
      - type: string
        enum:
        - MCT/A
        - MCT/B
        - DTGS
        - InSb
        - Si photodiode
        - Microbolometer
        - N/A
        - None
        - missing
      - type: string
      readOnly: true
    ada:beamsplitter:
      description: Beamsplitter fitted for this procedure; it sets the accessible
        spectral range. Record 'N/A' where the procedure uses no interferometer.
      anyOf:
      - type: string
        enum:
        - KBr
        - CaF2
        - ZnSe
        - Mylar
        - Quartz
        - N/A
        - None
        - missing
      - type: string
      readOnly: true
    ada:spectralRangeMinimum:
      description: Short-wavelength (or low-wavenumber) limit the procedure acquires.
      anyOf:
      - type: number
      - type: string
      readOnly: true
    ada:spectralRangeMaximum:
      description: Long-wavelength (or high-wavenumber) limit the procedure acquires.
      anyOf:
      - type: number
      - type: string
      readOnly: true
    ada:spectralResolutionDefault:
      description: Instrumental spectral resolution the procedure operates at.
      anyOf:
      - type: number
      - type: string
    schema:additionalProperty:
      type: array
      items:
        anyOf:
        - title: Spectral Sampling
          description: 'Spacing between adjacent recorded spectral points. Distinct
            from resolution: sampling may oversample the instrumental resolution.'
          type: object
          properties:
            '@id':
              const: ada:parameter/vnmirTAPP/spectralSampling
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/vnmirTAPP/spectralSampling
            schema:name:
              const: Spectral Sampling
            schema:value:
              anyOf:
              - type: number
              - type: string
            schema:unitText:
              type: string
          required:
          - '@id'
          - '@type'
          - schema:propertyID
          - schema:name
          - schema:value
          - schema:unitText
          readOnly: true
        - title: Emissivity Maximum Fit Region Minimum
          description: Short-wavelength limit of the window over which the emissivity
            maximum is fitted. Record 'N/A' where Measurement Type is not Emissivity.
          type: object
          properties:
            '@id':
              const: ada:parameter/vnmirTAPP/emissivityMaximumFitRegionMinimumDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: emissivityMaximumFitRegionMinimumDefault
            schema:name:
              const: Emissivity Maximum Fit Region Minimum
            ada:dataType:
              const: number
            ada:fieldScope:
              const: session
            schema:readonlyValue:
              const: false
            ada:tier:
              const: R
            schema:unitText:
              type: string
          required:
          - '@id'
          - '@type'
          - schema:valueName
          - schema:name
          - ada:dataType
          - ada:fieldScope
        - title: Emissivity Maximum Fit Region Maximum
          description: Long-wavelength limit of the window over which the emissivity
            maximum is fitted. Record 'N/A' where Measurement Type is not Emissivity.
          type: object
          properties:
            '@id':
              const: ada:parameter/vnmirTAPP/emissivityMaximumFitRegionMaximumDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: emissivityMaximumFitRegionMaximumDefault
            schema:name:
              const: Emissivity Maximum Fit Region Maximum
            ada:dataType:
              const: number
            ada:fieldScope:
              const: session
            schema:readonlyValue:
              const: false
            ada:tier:
              const: R
            schema:unitText:
              type: string
          required:
          - '@id'
          - '@type'
          - schema:valueName
          - schema:name
          - ada:dataType
          - ada:fieldScope
      allOf:
      - contains:
          title: Spectral Sampling
          description: 'Spacing between adjacent recorded spectral points. Distinct
            from resolution: sampling may oversample the instrumental resolution.'
          type: object
          properties:
            '@id':
              const: ada:parameter/vnmirTAPP/spectralSampling
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/vnmirTAPP/spectralSampling
            schema:name:
              const: Spectral Sampling
            schema:value:
              anyOf:
              - type: number
              - type: string
            schema:unitText:
              type: string
          required:
          - '@id'
          - '@type'
          - schema:propertyID
          - schema:name
          - schema:value
          - schema:unitText
          readOnly: true
        minContains: 0
        maxContains: 1
      - contains:
          title: Emissivity Maximum Fit Region Minimum
          description: Short-wavelength limit of the window over which the emissivity
            maximum is fitted. Record 'N/A' where Measurement Type is not Emissivity.
          type: object
          properties:
            '@id':
              const: ada:parameter/vnmirTAPP/emissivityMaximumFitRegionMinimumDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: emissivityMaximumFitRegionMinimumDefault
            schema:name:
              const: Emissivity Maximum Fit Region Minimum
            ada:dataType:
              const: number
            ada:fieldScope:
              const: session
            schema:readonlyValue:
              const: false
            ada:tier:
              const: R
            schema:unitText:
              type: string
          required:
          - '@id'
          - '@type'
          - schema:valueName
          - schema:name
          - ada:dataType
          - ada:fieldScope
        minContains: 0
        maxContains: 1
      - contains:
          title: Emissivity Maximum Fit Region Maximum
          description: Long-wavelength limit of the window over which the emissivity
            maximum is fitted. Record 'N/A' where Measurement Type is not Emissivity.
          type: object
          properties:
            '@id':
              const: ada:parameter/vnmirTAPP/emissivityMaximumFitRegionMaximumDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: emissivityMaximumFitRegionMaximumDefault
            schema:name:
              const: Emissivity Maximum Fit Region Maximum
            ada:dataType:
              const: number
            ada:fieldScope:
              const: session
            schema:readonlyValue:
              const: false
            ada:tier:
              const: R
            schema:unitText:
              type: string
          required:
          - '@id'
          - '@type'
          - schema:valueName
          - schema:name
          - ada:dataType
          - ada:fieldScope
        minContains: 0
        maxContains: 1
    ada:measurementType:
      description: Radiometric quantity the procedure reports.
      anyOf:
      - type: string
        enum:
        - Reflectance (bidirectional)
        - Reflectance (biconical)
        - Reflectance (hemispherical)
        - Emissivity
        - Transmittance
        - Absorbance
        - N/A
        - None
        - missing
      - type: string
      readOnly: true
    ada:measurementEnvironmentDefault:
      description: Atmosphere the measurement chamber is held in.
      anyOf:
      - type: string
        enum:
        - Ambient air
        - Purged (dry N2)
        - Purged (dry air)
        - Vacuum
        - Simulated planetary
        - N/A
        - None
        - missing
      - type: string
    ada:spotSizeDefault:
      description: Diameter of the analysed area for a point measurement, or the pixel
        footprint for a map.
      anyOf:
      - type: number
      - type: string
    ada:numberOfScansDefault:
      description: Interferograms co-added per reported spectrum.
      anyOf:
      - type: integer
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
    ada:calibrationStandardsDefault:
      description: Reference materials measured to calibrate the reported quantity,
        with source.
      type: string
    ada:analyticalMode:
      type: array
      items:
        type: string
        enum:
        - Spectral Point
        - Overview Image
        - Spectral Map
  required:
  - ada:targetMaterial
  - ada:instrumentManufacturer
  - ada:instrumentModel
  - ada:detector
  - ada:beamsplitter
  - ada:spectralRangeMinimum
  - ada:spectralRangeMaximum
  - ada:spectralResolutionDefault
  - ada:measurementType
  - ada:measurementEnvironmentDefault
  - ada:spotSizeDefault
  - ada:numberOfScansDefault
  - ada:constantsAndReferenceValuesUsedDefault
  - ada:calibrationStandardsDefault

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/VNMIR/tapp/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/VNMIR/tapp/schema.yaml)


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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/VNMIR/tapp/context.jsonld)

## Sources

* [VNMIR_TAPP_draft_v2.csv (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/VNMIR/tapp`

