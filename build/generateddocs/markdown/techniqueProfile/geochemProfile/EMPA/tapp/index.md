
# EMPA Technique-Aligned Protocol Profile (empaTAPP) (Schema)

`ogch.techniqueProfile.geochemProfile.EMPA.tapp` *v0.1*

EMPA-specific extension of the base TAPP definition. Adds EPMA top-level properties (beam mode, accelerating voltage, matrix correction method), a parameter vocabulary, and an analyte-column template covering EPMA per-element acquisition and reporting fields. Vocabularies, parameter templates, and analyte-column templates ship as separate JSON files under vocab/, parameters/, and analyteColumns/ for maintainability.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### empaTAPP example JEOL8200
empaTAPP instance derived from Ma+2015 | Caltech GPS | WDS Point Analysis (JEOL 8200).
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
  "@id": "ex:empaTAPP-JEOL8200",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS Major Element Silicates/Oxides, Tissint Mars Meteorite (Caltech GPS, JEOL 8200)",
  "schema:description": "Ma et al. 2015, Earth Planet. Sci. Lett. — tissintite discovery paper (Tissint Mars meteorite). Instrument stated as \"JEOL 8200 electron microprobe\" (no JXA prefix). WDS explicitly stated (\"WDS: 15 kV; 5 nA; beam in focused mode\"). Point analysis only; no X-ray mapping reported. Probe for EPMA stated; CITZAF correction procedure (Armstrong 1995). Full standard suite with X-ray lines given. Detection limits: K=0.02, Cr=0.05, Mn=0.06 wt% from Table 1 footnote. Caltech GPS Division Analytical Facility.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV",
      "ada:beamDiameterDefault": "Focused (exact diameter N)",
      "ada:beamMode": "Focused (stated: \"beam in focused mode\")",
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        }
      ],
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "JEOL 8200 (stated as \"JEOL 8200 electron microprobe\"; no JXA prefix stated)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:matrixCorrectionMethod": "CITZAF (Armstrong 1995)",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Silicate mineral (tissintite clinopyroxene, plagioclase, maskelynite) | Oxide | Glass (melt pocket)"
          ]
        }
      ]
    }
  ],
  "ada:monitoredEleemnts": [
    "Si, Al, Ca, Na, Fe, Mg, Mn, Ti, Cr, K — all determined; no monitor-only element. \"Standards for analysis were anorthite (SiKα, AlKα, CaKα); albite (NaKα); fayalite (FeKα); forsterite (MgKα); Mn2SiO4 (MnKα); TiO2 (TiKα); Cr2O3 (CrKα); and microcline (KKα)\" (p.3)"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "EPMA-WDS"
    }
  ],
  "schema:creator": {
    "schema:name": "Chi Ma",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Caltech GPS Division Analytical Facility"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Ma et al. 2015, Earth Planet. Sci. Lett. 422:194-205; doi:10.1016/j.epsl.2015.03.057"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM (Carl Zeiss 1550VP FE-SEM, BSE imaging); EBSD (HKL system on ZEISS 1550VP); synchrotron XRD; micro-Raman"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "bios:computationalTool": [
    {
      "ada:toolRole": "acquisition",
      "schema:name": "Probe for EPMA (Probe Software, Inc.)"
    },
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "CITZAF correction procedure (Armstrong 1995)"
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Polished thin section; carbon coating N",
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 1
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
        "schema:position": 2,
        "ada:detectionLimitMethod": "missing"
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "ada:primaryStandardNameDefault": "Anorthite (SiKα, AlKα, CaKα); albite (NaKα); fayalite (FeKα); forsterite (MgKα); Mn2SiO4 (MnKα); TiO2 (TiKα); Cr2O3 (CrKα); microcline (KKα)",
  "ada:edsAcquisitionMode": "missing",
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EMPA/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:empaTAPP-JEOL8200",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS Major Element Silicates/Oxides, Tissint Mars Meteorite (Caltech GPS, JEOL 8200)",
  "schema:description": "Ma et al. 2015, Earth Planet. Sci. Lett. \u2014 tissintite discovery paper (Tissint Mars meteorite). Instrument stated as \"JEOL 8200 electron microprobe\" (no JXA prefix). WDS explicitly stated (\"WDS: 15 kV; 5 nA; beam in focused mode\"). Point analysis only; no X-ray mapping reported. Probe for EPMA stated; CITZAF correction procedure (Armstrong 1995). Full standard suite with X-ray lines given. Detection limits: K=0.02, Cr=0.05, Mn=0.06 wt% from Table 1 footnote. Caltech GPS Division Analytical Facility.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV",
      "ada:beamDiameterDefault": "Focused (exact diameter N)",
      "ada:beamMode": "Focused (stated: \"beam in focused mode\")",
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        }
      ],
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "JEOL 8200 (stated as \"JEOL 8200 electron microprobe\"; no JXA prefix stated)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:matrixCorrectionMethod": "CITZAF (Armstrong 1995)",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Silicate mineral (tissintite clinopyroxene, plagioclase, maskelynite) | Oxide | Glass (melt pocket)"
          ]
        }
      ]
    }
  ],
  "ada:monitoredEleemnts": [
    "Si, Al, Ca, Na, Fe, Mg, Mn, Ti, Cr, K \u2014 all determined; no monitor-only element. \"Standards for analysis were anorthite (SiK\u03b1, AlK\u03b1, CaK\u03b1); albite (NaK\u03b1); fayalite (FeK\u03b1); forsterite (MgK\u03b1); Mn2SiO4 (MnK\u03b1); TiO2 (TiK\u03b1); Cr2O3 (CrK\u03b1); and microcline (KK\u03b1)\" (p.3)"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "EPMA-WDS"
    }
  ],
  "schema:creator": {
    "schema:name": "Chi Ma",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Caltech GPS Division Analytical Facility"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Ma et al. 2015, Earth Planet. Sci. Lett. 422:194-205; doi:10.1016/j.epsl.2015.03.057"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM (Carl Zeiss 1550VP FE-SEM, BSE imaging); EBSD (HKL system on ZEISS 1550VP); synchrotron XRD; micro-Raman"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "bios:computationalTool": [
    {
      "ada:toolRole": "acquisition",
      "schema:name": "Probe for EPMA (Probe Software, Inc.)"
    },
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "CITZAF correction procedure (Armstrong 1995)"
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Polished thin section; carbon coating N",
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 1
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
        "schema:position": 2,
        "ada:detectionLimitMethod": "missing"
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "ada:primaryStandardNameDefault": "Anorthite (SiK\u03b1, AlK\u03b1, CaK\u03b1); albite (NaK\u03b1); fayalite (FeK\u03b1); forsterite (MgK\u03b1); Mn2SiO4 (MnK\u03b1); TiO2 (TiK\u03b1); Cr2O3 (CrK\u03b1); microcline (KK\u03b1)",
  "ada:edsAcquisitionMode": "missing",
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
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

ex:empaTAPP-JEOL8200 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Polished thin section; carbon coating N" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ;
                    ada:detectionLimitMethod "missing" ] ] ;
    schema1:creator [ a schema1:Person ;
            schema1:name "Chi Ma" ] ;
    schema1:datePublished "missing" ;
    schema1:description "Ma et al. 2015, Earth Planet. Sci. Lett. — tissintite discovery paper (Tissint Mars meteorite). Instrument stated as \"JEOL 8200 electron microprobe\" (no JXA prefix). WDS explicitly stated (\"WDS: 15 kV; 5 nA; beam in focused mode\"). Point analysis only; no X-ray mapping reported. Probe for EPMA stated; CITZAF correction procedure (Armstrong 1995). Full standard suite with X-ray lines given. Detection limits: K=0.02, Cr=0.05, Mn=0.06 wt% from Table 1 footnote. Caltech GPS Division Analytical Facility." ;
    schema1:instrument <https://example.org/instrument/EPMA>,
        <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Caltech GPS Division Analytical Facility" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "EPMA-WDS" ] ;
    schema1:name "EPMA-WDS Major Element Silicates/Oxides, Tissint Mars Meteorite (Caltech GPS, JEOL 8200)" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Silicate mineral (tissintite clinopyroxene, plagioclase, maskelynite) | Oxide | Glass (melt pocket)" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Ma et al. 2015, Earth Planet. Sci. Lett. 422:194-205; doi:10.1016/j.epsl.2015.03.057" ] ;
            schema1:url "https://ada.astromat.org/missing" ],
        [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "SEM (Carl Zeiss 1550VP FE-SEM, BSE imaging); EBSD (HKL system on ZEISS 1550VP); synchrotron XRD; micro-Raman" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:edsAcquisitionMode "missing" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "CITZAF (Armstrong 1995)" ;
    ada:monitoredEleemnts "Si, Al, Ca, Na, Fe, Mg, Mn, Ti, Cr, K — all determined; no monitor-only element. \"Standards for analysis were anorthite (SiKα, AlKα, CaKα); albite (NaKα); fayalite (FeKα); forsterite (MgKα); Mn2SiO4 (MnKα); TiO2 (TiKα); Cr2O3 (CrKα); and microcline (KKα)\" (p.3)" ;
    ada:primaryStandardNameDefault "Anorthite (SiKα, AlKα, CaKα); albite (NaKα); fayalite (FeKα); forsterite (MgKα); Mn2SiO4 (MnKα); TiO2 (TiKα); Cr2O3 (CrKα); microcline (KKα)" ;
    ada:samplingUnit "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:wdsDeadTimeCorrection "missing" ;
    bios:computationalTool [ schema1:name "CITZAF correction procedure (Armstrong 1995)" ;
            ada:toolRole "dataReduction" ],
        [ schema1:name "Probe for EPMA (Probe Software, Inc.)" ;
            ada:toolRole "acquisition" ] .

<https://example.org/instrument/EPMA> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EPMA" ;
    schema1:hasPart <https://example.org/instrument/EPMA/part/EDS-Detector>,
        <https://example.org/instrument/EPMA/part/Electron-Source>,
        <https://example.org/instrument/EPMA/part/WDS-Spectrometer> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "JEOL" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "15 kV" ;
    ada:beamDiameterDefault "Focused (exact diameter N)" ;
    ada:beamMode "Focused (stated: \"beam in focused mode\")" .

<https://example.org/instrument/EPMA/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/EPMA/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "missing" ;
    schema1:name "missing" .

<https://example.org/instrument/EPMA/part/WDS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "WDS Spectrometer" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "JEOL 8200 (stated as \"JEOL 8200 electron microprobe\"; no JXA prefix stated)" ] ;
    schema1:name "example instrumentName" .


```


### empaTAPP example P1
empaTAPP instance derived from Hu+2020 | IGGCAS | WDS Point Analysis (JEOL JXA-8100).
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
  "@id": "ex:empaTAPP-P1",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS Major Element Silicates/Oxides, NWA 8657 Shergottite (IGGCAS, JEOL JXA-8100)",
  "schema:description": "Hu et al. 2020, Geochim. Cosmochim. Acta — coesite in NWA 8657 shergottite. JEOL JXA-8100 at IGGCAS; 15 kV, 10 nA; point analysis WDS only. Matrix correction: Bence-Albee (not PAP). Full primary standard suite stated (kaersutite, jadeite, bustamite, K-feldspar, rutile, Cr2O3). Mn Kα / Cr Kβ interference correction applied. Detection limits 0.01-0.06 wt% stated per element. Analytical software not stated.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV",
      "ada:beamDiameterDefault": "Focused (exact diameter N)",
      "ada:beamMode": "Focused",
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        }
      ],
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "JXA-8100 (stated as \"JEOL JXA-8100\")",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:matrixCorrectionMethod": "Bence-Albee",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Silicate mineral (coesite, pyroxene, feldspar) | Oxide | Sulfide"
          ]
        }
      ]
    }
  ],
  "ada:monitoredEleemnts": [
    "Si, Mg, Fe, Na, Al, Ca, Mn, K, Ti, Cr — all determined. \"The EPMA standards were natural and synthetic minerals: natural kaersutite for Si, Mg and Fe, jadeite for Na and Al, bustamite for Ca and Mn, and K-feldspar for K, synthetic rutile for Ti and Cr2O3 for Cr\". Cr also carries the interference correction — \"X-ray interference of the Kα line of Mn by the Kβ line of Cr was corrected\" — but is itself determined, so it is not an orphan"
  ],
  "schema:creator": {
    "schema:name": "Sen Hu",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Institute of Geology and Geophysics, Chinese Academy of Sciences (IGGCAS), Beijing"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Hu et al. 2020, Geochim. Cosmochim. Acta 278:185-198; doi:10.1016/j.gca.2019.06.012"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM-EDS (FEI Nova NanoSEM 450); Raman spectroscopy"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Bence-Albee method"
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Polished thick section (NWA 8657); carbon coating N",
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 1
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
        "schema:position": 2,
        "ada:detectionLimitMethod": "missing"
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "ada:primaryStandardNameDefault": "Natural kaersutite (Si, Mg, Fe); jadeite (Na, Al); bustamite (Ca, Mn); K-feldspar (K); synthetic rutile (Ti); Cr2O3 (Cr)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "empa",
      "schema:termCode": "empa"
    }
  ],
  "ada:edsAcquisitionMode": "missing",
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EMPA/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:empaTAPP-P1",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS Major Element Silicates/Oxides, NWA 8657 Shergottite (IGGCAS, JEOL JXA-8100)",
  "schema:description": "Hu et al. 2020, Geochim. Cosmochim. Acta \u2014 coesite in NWA 8657 shergottite. JEOL JXA-8100 at IGGCAS; 15 kV, 10 nA; point analysis WDS only. Matrix correction: Bence-Albee (not PAP). Full primary standard suite stated (kaersutite, jadeite, bustamite, K-feldspar, rutile, Cr2O3). Mn K\u03b1 / Cr K\u03b2 interference correction applied. Detection limits 0.01-0.06 wt% stated per element. Analytical software not stated.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV",
      "ada:beamDiameterDefault": "Focused (exact diameter N)",
      "ada:beamMode": "Focused",
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        }
      ],
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "JXA-8100 (stated as \"JEOL JXA-8100\")",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:matrixCorrectionMethod": "Bence-Albee",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Silicate mineral (coesite, pyroxene, feldspar) | Oxide | Sulfide"
          ]
        }
      ]
    }
  ],
  "ada:monitoredEleemnts": [
    "Si, Mg, Fe, Na, Al, Ca, Mn, K, Ti, Cr \u2014 all determined. \"The EPMA standards were natural and synthetic minerals: natural kaersutite for Si, Mg and Fe, jadeite for Na and Al, bustamite for Ca and Mn, and K-feldspar for K, synthetic rutile for Ti and Cr2O3 for Cr\". Cr also carries the interference correction \u2014 \"X-ray interference of the K\u03b1 line of Mn by the K\u03b2 line of Cr was corrected\" \u2014 but is itself determined, so it is not an orphan"
  ],
  "schema:creator": {
    "schema:name": "Sen Hu",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Institute of Geology and Geophysics, Chinese Academy of Sciences (IGGCAS), Beijing"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Hu et al. 2020, Geochim. Cosmochim. Acta 278:185-198; doi:10.1016/j.gca.2019.06.012"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM-EDS (FEI Nova NanoSEM 450); Raman spectroscopy"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Bence-Albee method"
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Polished thick section (NWA 8657); carbon coating N",
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 1
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
        "schema:position": 2,
        "ada:detectionLimitMethod": "missing"
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "ada:primaryStandardNameDefault": "Natural kaersutite (Si, Mg, Fe); jadeite (Na, Al); bustamite (Ca, Mn); K-feldspar (K); synthetic rutile (Ti); Cr2O3 (Cr)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "empa",
      "schema:termCode": "empa"
    }
  ],
  "ada:edsAcquisitionMode": "missing",
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
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

ex:empaTAPP-P1 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ;
                    ada:detectionLimitMethod "missing" ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Polished thick section (NWA 8657); carbon coating N" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:creator [ a schema1:Person ;
            schema1:name "Sen Hu" ] ;
    schema1:datePublished "missing" ;
    schema1:description "Hu et al. 2020, Geochim. Cosmochim. Acta — coesite in NWA 8657 shergottite. JEOL JXA-8100 at IGGCAS; 15 kV, 10 nA; point analysis WDS only. Matrix correction: Bence-Albee (not PAP). Full primary standard suite stated (kaersutite, jadeite, bustamite, K-feldspar, rutile, Cr2O3). Mn Kα / Cr Kβ interference correction applied. Detection limits 0.01-0.06 wt% stated per element. Analytical software not stated." ;
    schema1:instrument <https://example.org/instrument/EPMA>,
        <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Institute of Geology and Geophysics, Chinese Academy of Sciences (IGGCAS), Beijing" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "empa" ;
            schema1:termCode "empa" ] ;
    schema1:name "EPMA-WDS Major Element Silicates/Oxides, NWA 8657 Shergottite (IGGCAS, JEOL JXA-8100)" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Silicate mineral (coesite, pyroxene, feldspar) | Oxide | Sulfide" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Hu et al. 2020, Geochim. Cosmochim. Acta 278:185-198; doi:10.1016/j.gca.2019.06.012" ] ;
            schema1:url "https://ada.astromat.org/missing" ],
        [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "SEM-EDS (FEI Nova NanoSEM 450); Raman spectroscopy" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:edsAcquisitionMode "missing" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "Bence-Albee" ;
    ada:monitoredEleemnts "Si, Mg, Fe, Na, Al, Ca, Mn, K, Ti, Cr — all determined. \"The EPMA standards were natural and synthetic minerals: natural kaersutite for Si, Mg and Fe, jadeite for Na and Al, bustamite for Ca and Mn, and K-feldspar for K, synthetic rutile for Ti and Cr2O3 for Cr\". Cr also carries the interference correction — \"X-ray interference of the Kα line of Mn by the Kβ line of Cr was corrected\" — but is itself determined, so it is not an orphan" ;
    ada:primaryStandardNameDefault "Natural kaersutite (Si, Mg, Fe); jadeite (Na, Al); bustamite (Ca, Mn); K-feldspar (K); synthetic rutile (Ti); Cr2O3 (Cr)" ;
    ada:samplingUnit "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:wdsDeadTimeCorrection "missing" ;
    bios:computationalTool [ schema1:name "Bence-Albee method" ;
            ada:toolRole "dataReduction" ] .

<https://example.org/instrument/EPMA> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EPMA" ;
    schema1:hasPart <https://example.org/instrument/EPMA/part/EDS-Detector>,
        <https://example.org/instrument/EPMA/part/Electron-Source>,
        <https://example.org/instrument/EPMA/part/WDS-Spectrometer> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "JEOL" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "15 kV" ;
    ada:beamDiameterDefault "Focused (exact diameter N)" ;
    ada:beamMode "Focused" .

<https://example.org/instrument/EPMA/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/EPMA/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "missing" ;
    schema1:name "missing" .

<https://example.org/instrument/EPMA/part/WDS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "WDS Spectrometer" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "JXA-8100 (stated as \"JEOL JXA-8100\")" ] ;
    schema1:name "example instrumentName" .


```


### empaTAPP example P2
empaTAPP instance derived from Liu+2016_UT | Cameca SX100 | WDS Mapping (U.Tennessee).
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
  "@id": "ex:empaTAPP-P2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA Major Element Silicates/Oxides+Mapping, Tissint (U. Tennessee, Cameca SX100)",
  "schema:description": "Liu et al. 2016, Meteorit. Planet. Sci. — Tissint mineral chemistry. Protocol 1 of 2: University of Tennessee Cameca SX100. Same paper also uses Caltech GPS JXA-8200 (see Liu+2016_Cal column). Point analysis AND X-ray mapping performed at UT. Specific mapping: BSE + Ca/Al/Fe/Mg Ka maps (15 kV, 20 nA, step 8-12 µm). Olivine megacryst mapping (15 kV, 200 nA, step 2 µm, dwell ~0.5 s) described as \"using the EMP\" — instrument ambiguous (may be UT or Caltech instrument). Standards, matrix correction, and software not stated.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV",
      "ada:beamDiameterDefault": "1-2 µm (olivine, pyroxene, Fe-Ti-Cr oxides); 5-10 µm defocused (maskelynite, phosphate, sulfide, glass)",
      "ada:beamMode": "Focused (olivine, pyroxene, Fe-Ti-Cr oxides); Defocused 5-10 µm (maskelynite, phosphate, sulfide, glass)",
      "schema:manufacturer": {
        "schema:name": "Cameca",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        }
      ],
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "SX100 (stated as \"Cameca SX100\")",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/empaTAPP/beamDamageMinimizationDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "beamDamageMinimizationDefault",
      "schema:name": "Beam Damage Minimization",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Defocused beam 5-10 µm for maskelynite, phosphate, sulfide, and glass"
    }
  ],
  "ada:stepSizePixelSizeDefault": "8-12 µm (BSE + Ca/Al/Fe/Mg Ka phase maps at UT); 2 µm (olivine megacryst Ka maps; instrument ambiguous)",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Silicate mineral (olivine, pyroxene, maskelynite) | Oxide (chromite, ulvospinel, ilmenite) | Sulfide | Phosphate (merrillite) | Glass (melt pocket)"
          ]
        }
      ]
    }
  ],
  "ada:monitoredEleemnts": [
    "Ca, Al, Fe, Mg — \"elemental X-ray maps (Ca Kα, Al Kα, Fe Kα, and Mg Kα) of four sections were obtained using a Cameca SX100 electron microprobe (EMP) at the University of Tennessee\" (p.3). A separate Caltech map set of two olivine megacrysts adds Fe, P, Al, Ca and Cr (p.4) but was collected on the other instrument, which this TAPP records as its own procedure column"
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Department of Earth and Planetary Sciences, University of Tennessee, Knoxville"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Liu et al. 2016, Meteorit. Planet. Sci.; doi:10.1111/maps.12726"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM (BSE imaging); petrographic microscopy; LA-ICP-MS (Agilent 7500ce, Virginia Tech)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Polished thin sections (coating type N)",
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 1
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
        "schema:position": 2,
        "ada:detectionLimitMethod": "missing"
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "empa",
      "schema:termCode": "empa"
    }
  ],
  "ada:edsAcquisitionMode": "missing",
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:primaryStandardNameDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:wdsDeadTimeCorrection": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EMPA/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:empaTAPP-P2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA Major Element Silicates/Oxides+Mapping, Tissint (U. Tennessee, Cameca SX100)",
  "schema:description": "Liu et al. 2016, Meteorit. Planet. Sci. \u2014 Tissint mineral chemistry. Protocol 1 of 2: University of Tennessee Cameca SX100. Same paper also uses Caltech GPS JXA-8200 (see Liu+2016_Cal column). Point analysis AND X-ray mapping performed at UT. Specific mapping: BSE + Ca/Al/Fe/Mg Ka maps (15 kV, 20 nA, step 8-12 \u00b5m). Olivine megacryst mapping (15 kV, 200 nA, step 2 \u00b5m, dwell ~0.5 s) described as \"using the EMP\" \u2014 instrument ambiguous (may be UT or Caltech instrument). Standards, matrix correction, and software not stated.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV",
      "ada:beamDiameterDefault": "1-2 \u00b5m (olivine, pyroxene, Fe-Ti-Cr oxides); 5-10 \u00b5m defocused (maskelynite, phosphate, sulfide, glass)",
      "ada:beamMode": "Focused (olivine, pyroxene, Fe-Ti-Cr oxides); Defocused 5-10 \u00b5m (maskelynite, phosphate, sulfide, glass)",
      "schema:manufacturer": {
        "schema:name": "Cameca",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        }
      ],
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "SX100 (stated as \"Cameca SX100\")",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/empaTAPP/beamDamageMinimizationDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "beamDamageMinimizationDefault",
      "schema:name": "Beam Damage Minimization",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Defocused beam 5-10 \u00b5m for maskelynite, phosphate, sulfide, and glass"
    }
  ],
  "ada:stepSizePixelSizeDefault": "8-12 \u00b5m (BSE + Ca/Al/Fe/Mg Ka phase maps at UT); 2 \u00b5m (olivine megacryst Ka maps; instrument ambiguous)",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Silicate mineral (olivine, pyroxene, maskelynite) | Oxide (chromite, ulvospinel, ilmenite) | Sulfide | Phosphate (merrillite) | Glass (melt pocket)"
          ]
        }
      ]
    }
  ],
  "ada:monitoredEleemnts": [
    "Ca, Al, Fe, Mg \u2014 \"elemental X-ray maps (Ca K\u03b1, Al K\u03b1, Fe K\u03b1, and Mg K\u03b1) of four sections were obtained using a Cameca SX100 electron microprobe (EMP) at the University of Tennessee\" (p.3). A separate Caltech map set of two olivine megacrysts adds Fe, P, Al, Ca and Cr (p.4) but was collected on the other instrument, which this TAPP records as its own procedure column"
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Department of Earth and Planetary Sciences, University of Tennessee, Knoxville"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Liu et al. 2016, Meteorit. Planet. Sci.; doi:10.1111/maps.12726"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM (BSE imaging); petrographic microscopy; LA-ICP-MS (Agilent 7500ce, Virginia Tech)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Polished thin sections (coating type N)",
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 1
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
        "schema:position": 2,
        "ada:detectionLimitMethod": "missing"
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "empa",
      "schema:termCode": "empa"
    }
  ],
  "ada:edsAcquisitionMode": "missing",
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:primaryStandardNameDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:wdsDeadTimeCorrection": "missing",
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

ex:empaTAPP-P2 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ;
                    ada:detectionLimitMethod "missing" ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Polished thin sections (coating type N)" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/empaTAPP/beamDamageMinimizationDefault> ;
    schema1:datePublished "missing" ;
    schema1:description "Liu et al. 2016, Meteorit. Planet. Sci. — Tissint mineral chemistry. Protocol 1 of 2: University of Tennessee Cameca SX100. Same paper also uses Caltech GPS JXA-8200 (see Liu+2016_Cal column). Point analysis AND X-ray mapping performed at UT. Specific mapping: BSE + Ca/Al/Fe/Mg Ka maps (15 kV, 20 nA, step 8-12 µm). Olivine megacryst mapping (15 kV, 200 nA, step 2 µm, dwell ~0.5 s) described as \"using the EMP\" — instrument ambiguous (may be UT or Caltech instrument). Standards, matrix correction, and software not stated." ;
    schema1:instrument <https://example.org/instrument/EPMA>,
        <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Department of Earth and Planetary Sciences, University of Tennessee, Knoxville" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "empa" ;
            schema1:termCode "empa" ] ;
    schema1:name "EPMA Major Element Silicates/Oxides+Mapping, Tissint (U. Tennessee, Cameca SX100)" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Silicate mineral (olivine, pyroxene, maskelynite) | Oxide (chromite, ulvospinel, ilmenite) | Sulfide | Phosphate (merrillite) | Glass (melt pocket)" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Liu et al. 2016, Meteorit. Planet. Sci.; doi:10.1111/maps.12726" ] ;
            schema1:url "https://ada.astromat.org/missing" ],
        [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "SEM (BSE imaging); petrographic microscopy; LA-ICP-MS (Agilent 7500ce, Virginia Tech)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:edsAcquisitionMode "missing" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:monitoredEleemnts "Ca, Al, Fe, Mg — \"elemental X-ray maps (Ca Kα, Al Kα, Fe Kα, and Mg Kα) of four sections were obtained using a Cameca SX100 electron microprobe (EMP) at the University of Tennessee\" (p.3). A separate Caltech map set of two olivine megacrysts adds Fe, P, Al, Ca and Cr (p.4) but was collected on the other instrument, which this TAPP records as its own procedure column" ;
    ada:primaryStandardNameDefault "missing" ;
    ada:samplingUnit "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:stepSizePixelSizeDefault "8-12 µm (BSE + Ca/Al/Fe/Mg Ka phase maps at UT); 2 µm (olivine megacryst Ka maps; instrument ambiguous)" ;
    ada:wdsDeadTimeCorrection "missing" .

<https://ada.astromat.org/metadata/parameter/empaTAPP/beamDamageMinimizationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Defocused beam 5-10 µm for maskelynite, phosphate, sulfide, and glass" ;
    schema1:name "Beam Damage Minimization" ;
    schema1:valueName "beamDamageMinimizationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://example.org/instrument/EPMA> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EPMA" ;
    schema1:hasPart <https://example.org/instrument/EPMA/part/EDS-Detector>,
        <https://example.org/instrument/EPMA/part/Electron-Source>,
        <https://example.org/instrument/EPMA/part/WDS-Spectrometer> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Cameca" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "15 kV" ;
    ada:beamDiameterDefault "1-2 µm (olivine, pyroxene, Fe-Ti-Cr oxides); 5-10 µm defocused (maskelynite, phosphate, sulfide, glass)" ;
    ada:beamMode "Focused (olivine, pyroxene, Fe-Ti-Cr oxides); Defocused 5-10 µm (maskelynite, phosphate, sulfide, glass)" .

<https://example.org/instrument/EPMA/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/EPMA/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "missing" ;
    schema1:name "missing" .

<https://example.org/instrument/EPMA/part/WDS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "WDS Spectrometer" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "SX100 (stated as \"Cameca SX100\")" ] ;
    schema1:name "example instrumentName" .


```


### empaTAPP example P3
empaTAPP instance derived from Liu+2016_Cal | JEOL JXA-8200 | WDS Point Analysis (Caltech GPS).
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
  "@id": "ex:empaTAPP-P3",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS Major Element Silicates/Oxides, Tissint (Caltech GPS, JEOL JXA-8200)",
  "schema:description": "Liu et al. 2016, Meteorit. Planet. Sci. — Tissint mineral chemistry. Protocol 2 of 2: Caltech GPS Division JEOL JXA-8200. Point analysis only (no mapping attributed to Caltech instrument). Conditions stated jointly for UT and Caltech instruments. Standards, matrix correction, and software not stated for EPMA.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV",
      "ada:beamDiameterDefault": "1-2 µm (olivine, pyroxene, Fe-Ti-Cr oxides); 5-10 µm defocused (maskelynite, phosphate, sulfide, glass)",
      "ada:beamMode": "Focused (olivine, pyroxene, Fe-Ti-Cr oxides); Defocused 5-10 µm (maskelynite, phosphate, sulfide, glass)",
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        }
      ],
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "JXA-8200 (stated as \"JEOL JXA-8200\")",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/empaTAPP/beamDamageMinimizationDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "beamDamageMinimizationDefault",
      "schema:name": "Beam Damage Minimization",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Defocused beam 5-10 µm for maskelynite, phosphate, sulfide, and glass"
    }
  ],
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Silicate mineral (olivine, pyroxene, maskelynite) | Oxide | Sulfide | Phosphate | Glass"
          ]
        }
      ]
    }
  ],
  "ada:monitoredEleemnts": [
    "Si, Ti, Al, Mg, Ca, Fe, Mn, Cr, Ni, Na, K, P — all determined. \"Detection limits are typically <0.03 wt% for SiO2, TiO2, Al2O3, MgO, and CaO; <0.05–0.1 wt% for FeO, MnO, Cr2O3, NiO, Na2O, K2O, and P2O5\" (p.4)"
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Division of Geological and Planetary Sciences, Caltech"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Liu et al. 2016, Meteorit. Planet. Sci.; doi:10.1111/maps.12726"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM (BSE imaging); petrographic microscopy; LA-ICP-MS (Agilent 7500ce, Virginia Tech)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Polished thin sections (coating type N)",
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 1
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
        "schema:position": 2,
        "ada:detectionLimitMethod": "missing"
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "empa",
      "schema:termCode": "empa"
    }
  ],
  "ada:edsAcquisitionMode": "missing",
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:primaryStandardNameDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EMPA/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:empaTAPP-P3",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS Major Element Silicates/Oxides, Tissint (Caltech GPS, JEOL JXA-8200)",
  "schema:description": "Liu et al. 2016, Meteorit. Planet. Sci. \u2014 Tissint mineral chemistry. Protocol 2 of 2: Caltech GPS Division JEOL JXA-8200. Point analysis only (no mapping attributed to Caltech instrument). Conditions stated jointly for UT and Caltech instruments. Standards, matrix correction, and software not stated for EPMA.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV",
      "ada:beamDiameterDefault": "1-2 \u00b5m (olivine, pyroxene, Fe-Ti-Cr oxides); 5-10 \u00b5m defocused (maskelynite, phosphate, sulfide, glass)",
      "ada:beamMode": "Focused (olivine, pyroxene, Fe-Ti-Cr oxides); Defocused 5-10 \u00b5m (maskelynite, phosphate, sulfide, glass)",
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        }
      ],
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "JXA-8200 (stated as \"JEOL JXA-8200\")",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/empaTAPP/beamDamageMinimizationDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "beamDamageMinimizationDefault",
      "schema:name": "Beam Damage Minimization",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Defocused beam 5-10 \u00b5m for maskelynite, phosphate, sulfide, and glass"
    }
  ],
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Silicate mineral (olivine, pyroxene, maskelynite) | Oxide | Sulfide | Phosphate | Glass"
          ]
        }
      ]
    }
  ],
  "ada:monitoredEleemnts": [
    "Si, Ti, Al, Mg, Ca, Fe, Mn, Cr, Ni, Na, K, P \u2014 all determined. \"Detection limits are typically <0.03 wt% for SiO2, TiO2, Al2O3, MgO, and CaO; <0.05\u20130.1 wt% for FeO, MnO, Cr2O3, NiO, Na2O, K2O, and P2O5\" (p.4)"
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Division of Geological and Planetary Sciences, Caltech"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Liu et al. 2016, Meteorit. Planet. Sci.; doi:10.1111/maps.12726"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM (BSE imaging); petrographic microscopy; LA-ICP-MS (Agilent 7500ce, Virginia Tech)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Polished thin sections (coating type N)",
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 1
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
        "schema:position": 2,
        "ada:detectionLimitMethod": "missing"
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "empa",
      "schema:termCode": "empa"
    }
  ],
  "ada:edsAcquisitionMode": "missing",
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:primaryStandardNameDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
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

ex:empaTAPP-P3 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ;
                    ada:detectionLimitMethod "missing" ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Polished thin sections (coating type N)" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/empaTAPP/beamDamageMinimizationDefault> ;
    schema1:datePublished "missing" ;
    schema1:description "Liu et al. 2016, Meteorit. Planet. Sci. — Tissint mineral chemistry. Protocol 2 of 2: Caltech GPS Division JEOL JXA-8200. Point analysis only (no mapping attributed to Caltech instrument). Conditions stated jointly for UT and Caltech instruments. Standards, matrix correction, and software not stated for EPMA." ;
    schema1:instrument <https://example.org/instrument/EPMA>,
        <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Division of Geological and Planetary Sciences, Caltech" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "empa" ;
            schema1:termCode "empa" ] ;
    schema1:name "EPMA-WDS Major Element Silicates/Oxides, Tissint (Caltech GPS, JEOL JXA-8200)" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Silicate mineral (olivine, pyroxene, maskelynite) | Oxide | Sulfide | Phosphate | Glass" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "SEM (BSE imaging); petrographic microscopy; LA-ICP-MS (Agilent 7500ce, Virginia Tech)" ] ;
            schema1:url "https://ada.astromat.org/missing" ],
        [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Liu et al. 2016, Meteorit. Planet. Sci.; doi:10.1111/maps.12726" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:edsAcquisitionMode "missing" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:monitoredEleemnts "Si, Ti, Al, Mg, Ca, Fe, Mn, Cr, Ni, Na, K, P — all determined. \"Detection limits are typically <0.03 wt% for SiO2, TiO2, Al2O3, MgO, and CaO; <0.05–0.1 wt% for FeO, MnO, Cr2O3, NiO, Na2O, K2O, and P2O5\" (p.4)" ;
    ada:primaryStandardNameDefault "missing" ;
    ada:samplingUnit "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:wdsDeadTimeCorrection "missing" .

<https://ada.astromat.org/metadata/parameter/empaTAPP/beamDamageMinimizationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Defocused beam 5-10 µm for maskelynite, phosphate, sulfide, and glass" ;
    schema1:name "Beam Damage Minimization" ;
    schema1:valueName "beamDamageMinimizationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://example.org/instrument/EPMA> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EPMA" ;
    schema1:hasPart <https://example.org/instrument/EPMA/part/EDS-Detector>,
        <https://example.org/instrument/EPMA/part/Electron-Source>,
        <https://example.org/instrument/EPMA/part/WDS-Spectrometer> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "JEOL" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "15 kV" ;
    ada:beamDiameterDefault "1-2 µm (olivine, pyroxene, Fe-Ti-Cr oxides); 5-10 µm defocused (maskelynite, phosphate, sulfide, glass)" ;
    ada:beamMode "Focused (olivine, pyroxene, Fe-Ti-Cr oxides); Defocused 5-10 µm (maskelynite, phosphate, sulfide, glass)" .

<https://example.org/instrument/EPMA/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/EPMA/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "missing" ;
    schema1:name "missing" .

<https://example.org/instrument/EPMA/part/WDS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "WDS Spectrometer" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "JXA-8200 (stated as \"JEOL JXA-8200\")" ] ;
    schema1:name "example instrumentName" .


```


### empaTAPP example JEOL8200-2
empaTAPP instance derived from Ma+2017 | JEOL 8200 | WDS Point Analysis (Caltech GPS Analytical Facility).
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
  "@id": "ex:empaTAPP-JEOL8200-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS Major Element Silicates/Glasses, Zagami (Caltech GPS Analytical Facility, JEOL 8200)",
  "schema:description": "Ma et al. 2018, Meteorit. Planet. Sci. 53:50-61 (file dated 2017) — liebermannite (KAlSi3O8) discovery from Zagami. Instrument stated as \"JEOL 8200 electron microprobe\" (no JXA prefix in text). WDS explicitly stated (\"WDS: 15 kV, 5 nA\"). Probe for EPMA; CITZAF correction (Armstrong 1995) — NOT PAP. Full standard suite and X-ray lines stated. K-mapping by EPMA also performed (used for mineral identification) but mapping conditions (step size, dwell time, current) not stated. Na diffusion observed during analysis despite low 5 nA beam current. Detection limits stated (per-element wt% values). Analytical accuracy: 1-2% for Si, Al, Ca, Na, K (feldspar standards as unknowns). Caltech GPS Division Analytical Facility.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV",
      "ada:beamDiameterDefault": "Focused (exact diameter N)",
      "ada:beamMode": "Focused (stated: \"beam in focused mode\")",
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        }
      ],
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "JEOL 8200 (stated as \"JEOL 8200 electron microprobe\"; no JXA prefix in paper)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/empaTAPP/beamDamageMinimizationDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "beamDamageMinimizationDefault",
      "schema:name": "Beam Damage Minimization",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Low beam current (5 nA); Na diffusion away from beam still observed in liebermannite"
    }
  ],
  "ada:matrixCorrectionMethod": "CITZAF (Armstrong 1995)",
  "ada:secondaryReferenceMaterialDefault": [
    "Feldspar standards run as unknowns (material names N beyond what is listed above)"
  ],
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Silicate mineral (liebermannite, lingunite, maskelynite, augite, pigeonite)"
          ]
        }
      ]
    }
  ],
  "ada:monitoredEleemnts": [
    "Si, Al, K, Ca, Na, Fe, Mg, Ti, Cr, Mn — all determined. \"Standards for analysis were Asbestos microcline (SiKa, AlKa, KKa), synthetic anorthite (CaKa), Amelia albite (NaKa), synthetic fayalite (FeKa), synthetic forsterite (MgKa), synthetic TiO2 (TiKa), synthetic Cr2O3 (CrKa), and synthetic Mn-olivine (MnKa)\", with detection limits quoted for the same ten (p.2)"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "EPMA-WDS"
    }
  ],
  "schema:creator": {
    "schema:name": "Chi Ma",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Division of Geological and Planetary Sciences Analytical Facility, Caltech"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Ma et al. 2018, Meteorit. Planet. Sci. 53:50-61; doi:10.1111/maps.13000 (file dated 2017)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM (Carl Zeiss 1550VP FE-SEM, BSE imaging); EBSD; synchrotron XRD; micro-Raman"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "bios:computationalTool": [
    {
      "ada:toolRole": "acquisition",
      "schema:name": "Probe for EPMA (Probe Software, Inc.)"
    },
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "CITZAF correction procedure (Armstrong 1995)"
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Polished thin section USNM 7619 (coating type N)",
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 1
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
        "schema:position": 2,
        "ada:detectionLimitMethod": "missing"
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "ada:primaryStandardNameDefault": "Asbestos microcline (SiKa, AlKa, KKa); synthetic anorthite (CaKa); Amelia albite (NaKa); synthetic fayalite (FeKa); synthetic forsterite (MgKa); synthetic TiO2 (TiKa); synthetic Cr2O3 (CrKa); synthetic Mn-olivine (MnKa)",
  "ada:edsAcquisitionMode": "missing",
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EMPA/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:empaTAPP-JEOL8200-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS Major Element Silicates/Glasses, Zagami (Caltech GPS Analytical Facility, JEOL 8200)",
  "schema:description": "Ma et al. 2018, Meteorit. Planet. Sci. 53:50-61 (file dated 2017) \u2014 liebermannite (KAlSi3O8) discovery from Zagami. Instrument stated as \"JEOL 8200 electron microprobe\" (no JXA prefix in text). WDS explicitly stated (\"WDS: 15 kV, 5 nA\"). Probe for EPMA; CITZAF correction (Armstrong 1995) \u2014 NOT PAP. Full standard suite and X-ray lines stated. K-mapping by EPMA also performed (used for mineral identification) but mapping conditions (step size, dwell time, current) not stated. Na diffusion observed during analysis despite low 5 nA beam current. Detection limits stated (per-element wt% values). Analytical accuracy: 1-2% for Si, Al, Ca, Na, K (feldspar standards as unknowns). Caltech GPS Division Analytical Facility.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV",
      "ada:beamDiameterDefault": "Focused (exact diameter N)",
      "ada:beamMode": "Focused (stated: \"beam in focused mode\")",
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        }
      ],
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "JEOL 8200 (stated as \"JEOL 8200 electron microprobe\"; no JXA prefix in paper)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/empaTAPP/beamDamageMinimizationDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "beamDamageMinimizationDefault",
      "schema:name": "Beam Damage Minimization",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Low beam current (5 nA); Na diffusion away from beam still observed in liebermannite"
    }
  ],
  "ada:matrixCorrectionMethod": "CITZAF (Armstrong 1995)",
  "ada:secondaryReferenceMaterialDefault": [
    "Feldspar standards run as unknowns (material names N beyond what is listed above)"
  ],
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Silicate mineral (liebermannite, lingunite, maskelynite, augite, pigeonite)"
          ]
        }
      ]
    }
  ],
  "ada:monitoredEleemnts": [
    "Si, Al, K, Ca, Na, Fe, Mg, Ti, Cr, Mn \u2014 all determined. \"Standards for analysis were Asbestos microcline (SiKa, AlKa, KKa), synthetic anorthite (CaKa), Amelia albite (NaKa), synthetic fayalite (FeKa), synthetic forsterite (MgKa), synthetic TiO2 (TiKa), synthetic Cr2O3 (CrKa), and synthetic Mn-olivine (MnKa)\", with detection limits quoted for the same ten (p.2)"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "EPMA-WDS"
    }
  ],
  "schema:creator": {
    "schema:name": "Chi Ma",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Division of Geological and Planetary Sciences Analytical Facility, Caltech"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Ma et al. 2018, Meteorit. Planet. Sci. 53:50-61; doi:10.1111/maps.13000 (file dated 2017)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM (Carl Zeiss 1550VP FE-SEM, BSE imaging); EBSD; synchrotron XRD; micro-Raman"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "bios:computationalTool": [
    {
      "ada:toolRole": "acquisition",
      "schema:name": "Probe for EPMA (Probe Software, Inc.)"
    },
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "CITZAF correction procedure (Armstrong 1995)"
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Polished thin section USNM 7619 (coating type N)",
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 1
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
        "schema:position": 2,
        "ada:detectionLimitMethod": "missing"
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "ada:primaryStandardNameDefault": "Asbestos microcline (SiKa, AlKa, KKa); synthetic anorthite (CaKa); Amelia albite (NaKa); synthetic fayalite (FeKa); synthetic forsterite (MgKa); synthetic TiO2 (TiKa); synthetic Cr2O3 (CrKa); synthetic Mn-olivine (MnKa)",
  "ada:edsAcquisitionMode": "missing",
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
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

ex:empaTAPP-JEOL8200-2 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ;
                    ada:detectionLimitMethod "missing" ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Polished thin section USNM 7619 (coating type N)" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/empaTAPP/beamDamageMinimizationDefault> ;
    schema1:creator [ a schema1:Person ;
            schema1:name "Chi Ma" ] ;
    schema1:datePublished "missing" ;
    schema1:description "Ma et al. 2018, Meteorit. Planet. Sci. 53:50-61 (file dated 2017) — liebermannite (KAlSi3O8) discovery from Zagami. Instrument stated as \"JEOL 8200 electron microprobe\" (no JXA prefix in text). WDS explicitly stated (\"WDS: 15 kV, 5 nA\"). Probe for EPMA; CITZAF correction (Armstrong 1995) — NOT PAP. Full standard suite and X-ray lines stated. K-mapping by EPMA also performed (used for mineral identification) but mapping conditions (step size, dwell time, current) not stated. Na diffusion observed during analysis despite low 5 nA beam current. Detection limits stated (per-element wt% values). Analytical accuracy: 1-2% for Si, Al, Ca, Na, K (feldspar standards as unknowns). Caltech GPS Division Analytical Facility." ;
    schema1:instrument <https://example.org/instrument/EPMA>,
        <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Division of Geological and Planetary Sciences Analytical Facility, Caltech" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "EPMA-WDS" ] ;
    schema1:name "EPMA-WDS Major Element Silicates/Glasses, Zagami (Caltech GPS Analytical Facility, JEOL 8200)" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Silicate mineral (liebermannite, lingunite, maskelynite, augite, pigeonite)" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Ma et al. 2018, Meteorit. Planet. Sci. 53:50-61; doi:10.1111/maps.13000 (file dated 2017)" ] ;
            schema1:url "https://ada.astromat.org/missing" ],
        [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "SEM (Carl Zeiss 1550VP FE-SEM, BSE imaging); EBSD; synchrotron XRD; micro-Raman" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:edsAcquisitionMode "missing" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "CITZAF (Armstrong 1995)" ;
    ada:monitoredEleemnts "Si, Al, K, Ca, Na, Fe, Mg, Ti, Cr, Mn — all determined. \"Standards for analysis were Asbestos microcline (SiKa, AlKa, KKa), synthetic anorthite (CaKa), Amelia albite (NaKa), synthetic fayalite (FeKa), synthetic forsterite (MgKa), synthetic TiO2 (TiKa), synthetic Cr2O3 (CrKa), and synthetic Mn-olivine (MnKa)\", with detection limits quoted for the same ten (p.2)" ;
    ada:primaryStandardNameDefault "Asbestos microcline (SiKa, AlKa, KKa); synthetic anorthite (CaKa); Amelia albite (NaKa); synthetic fayalite (FeKa); synthetic forsterite (MgKa); synthetic TiO2 (TiKa); synthetic Cr2O3 (CrKa); synthetic Mn-olivine (MnKa)" ;
    ada:samplingUnit "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:secondaryReferenceMaterialDefault "Feldspar standards run as unknowns (material names N beyond what is listed above)" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:wdsDeadTimeCorrection "missing" ;
    bios:computationalTool [ schema1:name "Probe for EPMA (Probe Software, Inc.)" ;
            ada:toolRole "acquisition" ],
        [ schema1:name "CITZAF correction procedure (Armstrong 1995)" ;
            ada:toolRole "dataReduction" ] .

<https://ada.astromat.org/metadata/parameter/empaTAPP/beamDamageMinimizationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Low beam current (5 nA); Na diffusion away from beam still observed in liebermannite" ;
    schema1:name "Beam Damage Minimization" ;
    schema1:valueName "beamDamageMinimizationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://example.org/instrument/EPMA> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EPMA" ;
    schema1:hasPart <https://example.org/instrument/EPMA/part/EDS-Detector>,
        <https://example.org/instrument/EPMA/part/Electron-Source>,
        <https://example.org/instrument/EPMA/part/WDS-Spectrometer> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "JEOL" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "15 kV" ;
    ada:beamDiameterDefault "Focused (exact diameter N)" ;
    ada:beamMode "Focused (stated: \"beam in focused mode\")" .

<https://example.org/instrument/EPMA/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/EPMA/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "missing" ;
    schema1:name "missing" .

<https://example.org/instrument/EPMA/part/WDS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "WDS Spectrometer" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "JEOL 8200 (stated as \"JEOL 8200 electron microprobe\"; no JXA prefix in paper)" ] ;
    schema1:name "example instrumentName" .


```


### empaTAPP example P5
empaTAPP instance derived from Frank+2023 | Cameca SX100 | WDS Point Analysis (ARES JSC).
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
  "@id": "ex:empaTAPP-P5",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA Major/Minor Element Silicates+Oxides+Sulfides, CI Chondrite (ARES JSC, Cameca SX100)",
  "schema:description": "Frank et al. 2023, Meteorit. Planet. Sci. 58:1495-1511 — CAI in Ivuna CI chondrite. ARES NASA JSC. Instrument stated as \"Cameca SX100 electron microprobe at ARES, Johnson Space Center\" — NOT JEOL JXA-8530F as in v2 header. Accelerating voltage 20 kV (not 15 kV). Both point analysis (20 kV, 20 nA, 1 µm focused) and X-ray mapping performed. X-ray mapping described but conditions (step size, dwell time, mapping beam mode) N. WDS not explicitly stated. Matrix correction and background correction method N. Peak counting time 10-50 s. Primary standard suite fully documented. Secondary standards: USNM San Carlos olivine (Fo90); Kakanui kaersutite. Detection limits stated per element group.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "20 kV",
      "ada:beamDiameterDefault": "1 µm (focused)",
      "ada:beamMode": "Focused (point analysis); mapping beam mode N",
      "schema:manufacturer": {
        "schema:name": "Cameca",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        }
      ],
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "SX100 (stated as \"Cameca SX100\")",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:secondaryReferenceMaterialDefault": [
    "USNM San Carlos olivine (Fo90); Kakanui kaersutite"
  ],
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Silicate mineral | Oxide | Sulfide | Phosphate (CI chondrite phases)"
          ]
        }
      ]
    }
  ],
  "ada:monitoredEleemnts": [
    "Si, Al, Ti, K, Na, Fe, Mg, Ca, S, Mn, Cr, Ni, P, V — all determined. \"Standards were Kakanui kaersutite for silicon, aluminum, titanium, potassium, sodium, iron, magnesium, and calcium, Canyon Diablo troilite for sulfur, rhodonite for manganese, chromium metal for chromium, nickel metal for nickel, apatite for phosphorus, and vanadium metal for vanadium\" (pp.3–4)"
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "ARES, NASA Johnson Space Center"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Frank et al. 2023, Meteorit. Planet. Sci. 58:1495-1511; doi:10.1111/maps.14083"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Petrographic microscopy; SEM-BSE (JEOL 5900LV); EPMA X-ray mapping; Cameca ims1280 ion microprobe (O isotopes; 26Al-26Mg); FIB-TEM"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:primaryStandardNameDefault": "Kakanui kaersutite (Si, Al, Ti, K, Na, Fe, Mg, Ca); Canyon Diablo troilite (S); rhodonite (Mn); chromium metal (Cr); nickel metal (Ni); apatite (P); vanadium metal (V)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "empa",
      "schema:termCode": "empa"
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
        "schema:position": 2,
        "ada:detectionLimitMethod": "missing"
      }
    ]
  },
  "ada:edsAcquisitionMode": "missing",
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EMPA/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:empaTAPP-P5",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA Major/Minor Element Silicates+Oxides+Sulfides, CI Chondrite (ARES JSC, Cameca SX100)",
  "schema:description": "Frank et al. 2023, Meteorit. Planet. Sci. 58:1495-1511 \u2014 CAI in Ivuna CI chondrite. ARES NASA JSC. Instrument stated as \"Cameca SX100 electron microprobe at ARES, Johnson Space Center\" \u2014 NOT JEOL JXA-8530F as in v2 header. Accelerating voltage 20 kV (not 15 kV). Both point analysis (20 kV, 20 nA, 1 \u00b5m focused) and X-ray mapping performed. X-ray mapping described but conditions (step size, dwell time, mapping beam mode) N. WDS not explicitly stated. Matrix correction and background correction method N. Peak counting time 10-50 s. Primary standard suite fully documented. Secondary standards: USNM San Carlos olivine (Fo90); Kakanui kaersutite. Detection limits stated per element group.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "20 kV",
      "ada:beamDiameterDefault": "1 \u00b5m (focused)",
      "ada:beamMode": "Focused (point analysis); mapping beam mode N",
      "schema:manufacturer": {
        "schema:name": "Cameca",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        }
      ],
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "SX100 (stated as \"Cameca SX100\")",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:secondaryReferenceMaterialDefault": [
    "USNM San Carlos olivine (Fo90); Kakanui kaersutite"
  ],
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Silicate mineral | Oxide | Sulfide | Phosphate (CI chondrite phases)"
          ]
        }
      ]
    }
  ],
  "ada:monitoredEleemnts": [
    "Si, Al, Ti, K, Na, Fe, Mg, Ca, S, Mn, Cr, Ni, P, V \u2014 all determined. \"Standards were Kakanui kaersutite for silicon, aluminum, titanium, potassium, sodium, iron, magnesium, and calcium, Canyon Diablo troilite for sulfur, rhodonite for manganese, chromium metal for chromium, nickel metal for nickel, apatite for phosphorus, and vanadium metal for vanadium\" (pp.3\u20134)"
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "ARES, NASA Johnson Space Center"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Frank et al. 2023, Meteorit. Planet. Sci. 58:1495-1511; doi:10.1111/maps.14083"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Petrographic microscopy; SEM-BSE (JEOL 5900LV); EPMA X-ray mapping; Cameca ims1280 ion microprobe (O isotopes; 26Al-26Mg); FIB-TEM"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:primaryStandardNameDefault": "Kakanui kaersutite (Si, Al, Ti, K, Na, Fe, Mg, Ca); Canyon Diablo troilite (S); rhodonite (Mn); chromium metal (Cr); nickel metal (Ni); apatite (P); vanadium metal (V)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "empa",
      "schema:termCode": "empa"
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
        "schema:position": 2,
        "ada:detectionLimitMethod": "missing"
      }
    ]
  },
  "ada:edsAcquisitionMode": "missing",
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
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

ex:empaTAPP-P5 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ;
                    ada:detectionLimitMethod "missing" ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "missing" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "Frank et al. 2023, Meteorit. Planet. Sci. 58:1495-1511 — CAI in Ivuna CI chondrite. ARES NASA JSC. Instrument stated as \"Cameca SX100 electron microprobe at ARES, Johnson Space Center\" — NOT JEOL JXA-8530F as in v2 header. Accelerating voltage 20 kV (not 15 kV). Both point analysis (20 kV, 20 nA, 1 µm focused) and X-ray mapping performed. X-ray mapping described but conditions (step size, dwell time, mapping beam mode) N. WDS not explicitly stated. Matrix correction and background correction method N. Peak counting time 10-50 s. Primary standard suite fully documented. Secondary standards: USNM San Carlos olivine (Fo90); Kakanui kaersutite. Detection limits stated per element group." ;
    schema1:instrument <https://example.org/instrument/EPMA>,
        <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "ARES, NASA Johnson Space Center" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "empa" ;
            schema1:termCode "empa" ] ;
    schema1:name "EPMA Major/Minor Element Silicates+Oxides+Sulfides, CI Chondrite (ARES JSC, Cameca SX100)" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Silicate mineral | Oxide | Sulfide | Phosphate (CI chondrite phases)" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "Petrographic microscopy; SEM-BSE (JEOL 5900LV); EPMA X-ray mapping; Cameca ims1280 ion microprobe (O isotopes; 26Al-26Mg); FIB-TEM" ] ;
            schema1:url "https://ada.astromat.org/missing" ],
        [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Frank et al. 2023, Meteorit. Planet. Sci. 58:1495-1511; doi:10.1111/maps.14083" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:edsAcquisitionMode "missing" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:monitoredEleemnts "Si, Al, Ti, K, Na, Fe, Mg, Ca, S, Mn, Cr, Ni, P, V — all determined. \"Standards were Kakanui kaersutite for silicon, aluminum, titanium, potassium, sodium, iron, magnesium, and calcium, Canyon Diablo troilite for sulfur, rhodonite for manganese, chromium metal for chromium, nickel metal for nickel, apatite for phosphorus, and vanadium metal for vanadium\" (pp.3–4)" ;
    ada:primaryStandardNameDefault "Kakanui kaersutite (Si, Al, Ti, K, Na, Fe, Mg, Ca); Canyon Diablo troilite (S); rhodonite (Mn); chromium metal (Cr); nickel metal (Ni); apatite (P); vanadium metal (V)" ;
    ada:samplingUnit "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:secondaryReferenceMaterialDefault "USNM San Carlos olivine (Fo90); Kakanui kaersutite" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:wdsDeadTimeCorrection "missing" .

<https://example.org/instrument/EPMA> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EPMA" ;
    schema1:hasPart <https://example.org/instrument/EPMA/part/EDS-Detector>,
        <https://example.org/instrument/EPMA/part/Electron-Source>,
        <https://example.org/instrument/EPMA/part/WDS-Spectrometer> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Cameca" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "20 kV" ;
    ada:beamDiameterDefault "1 µm (focused)" ;
    ada:beamMode "Focused (point analysis); mapping beam mode N" .

<https://example.org/instrument/EPMA/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/EPMA/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "missing" ;
    schema1:name "missing" .

<https://example.org/instrument/EPMA/part/WDS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "WDS Spectrometer" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "SX100 (stated as \"Cameca SX100\")" ] ;
    schema1:name "example instrumentName" .


```


### empaTAPP example P6
empaTAPP instance derived from Broussard+2026 | JEOL JXA-8200 | WDS Mapping (WashU).
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
  "@id": "ex:empaTAPP-P6",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS Quantitative Mapping+Analysis, CI Chondrite Minerals (WashU, JEOL JXA-8200)",
  "schema:description": "Broussard et al. 2026, Meteorit. Planet. Sci. — OC002 CI chondrite links Bennu and Ryugu. Washington University in St. Louis. Instrument stated as \"JEOL JXA-8200 electron microprobe\" — NOT JXA-8230 as in v2 header. WDS explicitly stated (\"wavelength-dispersive quantitative compositional mapping and analysis\"). CITZAF matrix correction (Armstrong 1995) — NOT PAP or XPP. MAN background for most analytes; polynomial fit for F via LDE1 crystal. Both point analysis (15 kV, 25 nA) and quantitative stage mapping performed. O by stoichiometry from cations. F is the only explicitly named analyte in methods; full list N. EDS spectrometer present but not used for quantitative analyses. Smithsonian Microbeam standards as secondary QC. No peak counting time, beam diameter, detection limits, or interference corrections stated.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV",
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "5 wavelength-dispersive spectrometers (JEOL)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:name": "example instrumentName",
      "ada:beamDiameterDefault": -9999,
      "ada:beamMode": "missing"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "JXA-8200 (stated as \"JEOL JXA-8200 electron microprobe\")",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:matrixCorrectionMethod": "CITZAF (Armstrong 1995)",
  "ada:secondaryReferenceMaterialDefault": [
    "Smithsonian Microbeam standards (specific materials and values N)"
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/empaTAPP/stageScanVsBeamScan",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/empaTAPP/stageScanVsBeamScan"
        }
      ],
      "schema:name": "Stage Scan vs. Beam Scan",
      "schema:value": "Stage scan"
    }
  ],
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Phyllosilicate (matrix) | Oxide (magnetite, ilmenite) | Sulfide (pyrrhotite, pentlandite) | Carbonate (dolomite, magnesite) | Phosphate (Ca phosphate, Na-Mg hydrous phosphate)"
          ]
        }
      ]
    }
  ],
  "ada:monitoredEleemnts": [
    "N — the paper describes quantitative EPMA stage mapping and its calibration against Smithsonian Microbeam secondary standards (p.3) but names no element"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "EPMA-WDS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Washington University in St. Louis"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Broussard et al. 2026, Meteorit. Planet. Sci.; doi:10.1111/maps.70138"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Powder XRD (Rigaku MiniFlex 600); ICP-MS (Thermo Fisher iCAP Qc, WashU); K isotope MC-ICP-MS (Neptune Plus, WashU); CO2 laser-fluorination O isotope MS (U. New Mexico); AMS (PRIME Lab, Purdue)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "bios:computationalTool": [
    {
      "ada:toolRole": "acquisition",
      "schema:name": "Probe for EPMA microanalysis software"
    },
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Probe for EPMA (CITZAF matrix correction, Armstrong 1995); CalcImage and Quantitative Microanalysis Explorer web-based tool (for stage mapping)"
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Fragments mounted and dry-polished in a petrographic thin section; carbon coating N",
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 1
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
        "schema:position": 2,
        "ada:detectionLimitMethod": "missing"
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "ada:primaryStandardNameDefault": "Natural and synthetic minerals routinely used in analytical facility (specific names N); synthetic F-phlogopite (for F, LDE1 crystal)",
  "ada:edsAcquisitionMode": "missing",
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EMPA/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:empaTAPP-P6",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS Quantitative Mapping+Analysis, CI Chondrite Minerals (WashU, JEOL JXA-8200)",
  "schema:description": "Broussard et al. 2026, Meteorit. Planet. Sci. \u2014 OC002 CI chondrite links Bennu and Ryugu. Washington University in St. Louis. Instrument stated as \"JEOL JXA-8200 electron microprobe\" \u2014 NOT JXA-8230 as in v2 header. WDS explicitly stated (\"wavelength-dispersive quantitative compositional mapping and analysis\"). CITZAF matrix correction (Armstrong 1995) \u2014 NOT PAP or XPP. MAN background for most analytes; polynomial fit for F via LDE1 crystal. Both point analysis (15 kV, 25 nA) and quantitative stage mapping performed. O by stoichiometry from cations. F is the only explicitly named analyte in methods; full list N. EDS spectrometer present but not used for quantitative analyses. Smithsonian Microbeam standards as secondary QC. No peak counting time, beam diameter, detection limits, or interference corrections stated.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV",
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "5 wavelength-dispersive spectrometers (JEOL)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:name": "example instrumentName",
      "ada:beamDiameterDefault": -9999,
      "ada:beamMode": "missing"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "JXA-8200 (stated as \"JEOL JXA-8200 electron microprobe\")",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:matrixCorrectionMethod": "CITZAF (Armstrong 1995)",
  "ada:secondaryReferenceMaterialDefault": [
    "Smithsonian Microbeam standards (specific materials and values N)"
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/empaTAPP/stageScanVsBeamScan",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/empaTAPP/stageScanVsBeamScan"
        }
      ],
      "schema:name": "Stage Scan vs. Beam Scan",
      "schema:value": "Stage scan"
    }
  ],
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Phyllosilicate (matrix) | Oxide (magnetite, ilmenite) | Sulfide (pyrrhotite, pentlandite) | Carbonate (dolomite, magnesite) | Phosphate (Ca phosphate, Na-Mg hydrous phosphate)"
          ]
        }
      ]
    }
  ],
  "ada:monitoredEleemnts": [
    "N \u2014 the paper describes quantitative EPMA stage mapping and its calibration against Smithsonian Microbeam secondary standards (p.3) but names no element"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "EPMA-WDS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Washington University in St. Louis"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Broussard et al. 2026, Meteorit. Planet. Sci.; doi:10.1111/maps.70138"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Powder XRD (Rigaku MiniFlex 600); ICP-MS (Thermo Fisher iCAP Qc, WashU); K isotope MC-ICP-MS (Neptune Plus, WashU); CO2 laser-fluorination O isotope MS (U. New Mexico); AMS (PRIME Lab, Purdue)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "bios:computationalTool": [
    {
      "ada:toolRole": "acquisition",
      "schema:name": "Probe for EPMA microanalysis software"
    },
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Probe for EPMA (CITZAF matrix correction, Armstrong 1995); CalcImage and Quantitative Microanalysis Explorer web-based tool (for stage mapping)"
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Fragments mounted and dry-polished in a petrographic thin section; carbon coating N",
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 1
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
        "schema:position": 2,
        "ada:detectionLimitMethod": "missing"
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "ada:primaryStandardNameDefault": "Natural and synthetic minerals routinely used in analytical facility (specific names N); synthetic F-phlogopite (for F, LDE1 crystal)",
  "ada:edsAcquisitionMode": "missing",
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
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

ex:empaTAPP-P6 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Fragments mounted and dry-polished in a petrographic thin section; carbon coating N" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ;
                    ada:detectionLimitMethod "missing" ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/empaTAPP/stageScanVsBeamScan> ;
    schema1:datePublished "missing" ;
    schema1:description "Broussard et al. 2026, Meteorit. Planet. Sci. — OC002 CI chondrite links Bennu and Ryugu. Washington University in St. Louis. Instrument stated as \"JEOL JXA-8200 electron microprobe\" — NOT JXA-8230 as in v2 header. WDS explicitly stated (\"wavelength-dispersive quantitative compositional mapping and analysis\"). CITZAF matrix correction (Armstrong 1995) — NOT PAP or XPP. MAN background for most analytes; polynomial fit for F via LDE1 crystal. Both point analysis (15 kV, 25 nA) and quantitative stage mapping performed. O by stoichiometry from cations. F is the only explicitly named analyte in methods; full list N. EDS spectrometer present but not used for quantitative analyses. Smithsonian Microbeam standards as secondary QC. No peak counting time, beam diameter, detection limits, or interference corrections stated." ;
    schema1:instrument <https://example.org/instrument/EPMA>,
        <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Washington University in St. Louis" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "EPMA-WDS" ] ;
    schema1:name "EPMA-WDS Quantitative Mapping+Analysis, CI Chondrite Minerals (WashU, JEOL JXA-8200)" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Phyllosilicate (matrix) | Oxide (magnetite, ilmenite) | Sulfide (pyrrhotite, pentlandite) | Carbonate (dolomite, magnesite) | Phosphate (Ca phosphate, Na-Mg hydrous phosphate)" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Broussard et al. 2026, Meteorit. Planet. Sci.; doi:10.1111/maps.70138" ] ;
            schema1:url "https://ada.astromat.org/missing" ],
        [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "Powder XRD (Rigaku MiniFlex 600); ICP-MS (Thermo Fisher iCAP Qc, WashU); K isotope MC-ICP-MS (Neptune Plus, WashU); CO2 laser-fluorination O isotope MS (U. New Mexico); AMS (PRIME Lab, Purdue)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:edsAcquisitionMode "missing" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "CITZAF (Armstrong 1995)" ;
    ada:monitoredEleemnts "N — the paper describes quantitative EPMA stage mapping and its calibration against Smithsonian Microbeam secondary standards (p.3) but names no element" ;
    ada:primaryStandardNameDefault "Natural and synthetic minerals routinely used in analytical facility (specific names N); synthetic F-phlogopite (for F, LDE1 crystal)" ;
    ada:samplingUnit "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:secondaryReferenceMaterialDefault "Smithsonian Microbeam standards (specific materials and values N)" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:wdsDeadTimeCorrection "missing" ;
    bios:computationalTool [ schema1:name "Probe for EPMA microanalysis software" ;
            ada:toolRole "acquisition" ],
        [ schema1:name "Probe for EPMA (CITZAF matrix correction, Armstrong 1995); CalcImage and Quantitative Microanalysis Explorer web-based tool (for stage mapping)" ;
            ada:toolRole "dataReduction" ] .

<https://example.org/instrument/EPMA> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EPMA" ;
    schema1:hasPart <https://example.org/instrument/EPMA/part/EDS-Detector>,
        <https://example.org/instrument/EPMA/part/Electron-Source>,
        <https://example.org/instrument/EPMA/part/WDS-Spectrometer> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "JEOL" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "15 kV" ;
    ada:beamDiameterDefault -9999 ;
    ada:beamMode "missing" .

<https://example.org/instrument/EPMA/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/EPMA/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "missing" ;
    schema1:name "missing" .

<https://example.org/instrument/EPMA/part/WDS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "WDS Spectrometer" ;
    schema1:name "5 wavelength-dispersive spectrometers (JEOL)" .

<https://example.org/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "JXA-8200 (stated as \"JEOL JXA-8200 electron microprobe\")" ] ;
    schema1:name "example instrumentName" .

<https://ada.astromat.org/metadata/parameter/empaTAPP/stageScanVsBeamScan> a schema1:PropertyValue ;
    schema1:name "Stage Scan vs. Beam Scan" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/empaTAPP/stageScanVsBeamScan> ;
    schema1:value "Stage scan" .


```


### empaTAPP example JEOL8530
empaTAPP instance derived from Seifert+2026 | JEOL 8530 | WDS Point Analysis (ARES JSC).
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
  "@id": "ex:empaTAPP-JEOL8530",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA Major Element Apatite incl. Halogens, Bennu (ARES JSC, JEOL 8530 EMPA)",
  "schema:description": "Seifert et al. 2026, Meteorit. Planet. Sci. — apatite in Bennu OSIRIS-REx samples. ARES NASA JSC. Instrument stated as \"JEOL 8530 EMPA at NASA JSC\" (no \"JXA\", no \"F\", no \"+\" suffix stated in paper). Analytical conditions: 15 kV, 20 nA, 2 µm probe size. Previous v2 values of 10/40-100 nA and 10 µm beam were WRONG — those were Durango apatite test conditions used to assess beam damage, not the actual protocol. Analytes: P, F, Cl, Ca, Mn, Fe, Na, Mg, Si, S. Apatite stoichiometry by Ketcham (2015) method (13-anion basis; OH by difference). Halogen correction on O: Yes. Primary standards: SrF2, albite, olivine, quartz, apatite, barite, tugtupite, rhodonite, ilmenite. Sample preparation: fragments embedded in epoxy, dry-polished, ion-polished (one mount), carbon coated. 14 total analyses performed.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV",
      "ada:beamDiameterDefault": "2 µm (stated as \"2 µm probe size\")",
      "ada:beamMode": "Focused (2 µm probe size stated)",
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        }
      ],
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "JEOL 8530 EMPA (stated as \"JEOL 8530 EMPA at NASA JSC\"; no F suffix or JXA prefix stated)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/empaTAPP/beamDamageMinimizationDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "beamDamageMinimizationDefault",
      "schema:name": "Beam Damage Minimization",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "2 µm probe used for all analyses; Durango apatite tested at 10 µm and 3 µm spot sizes to assess halogen volatilization; no significant loss found under adopted conditions"
    },
    {
      "@id": "ada:parameter/empaTAPP/halogenCorrectionOnOxygenDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "halogenCorrectionOnOxygenDefault",
      "schema:name": "Halogen Correction on Oxygen",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Yes (F and Cl substitution in apatite; 1-F-Cl=OH)"
    }
  ],
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Phosphate (apatite)"
          ]
        }
      ]
    }
  ],
  "ada:monitoredEleemnts": [
    "P, F, Cl, Ca, Mn, Fe, Na, Mg, Si, S — all determined. \"A total of 14 analyses were performed at 15 kV, 20 nA, using a 2 μm probe size, and included the elements P, F, Cl, Ca, Mn, Fe, Na, Mg, Si, and S\" (p.3)"
  ],
  "schema:creator": {
    "schema:name": "Logan B. Seifert",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "ARES, NASA Johnson Space Center"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Seifert et al. 2026, Meteorit. Planet. Sci.; doi:10.1111/maps.70167"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM-EDS; SIMS (Cameca ims 1280); TEM-EDS"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Fragments embedded in epoxy; dry-polished with diamond powder; one mount ion-polished before carbon coating",
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 1
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
        "schema:position": 2,
        "ada:detectionLimitMethod": "missing"
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "ada:primaryStandardNameDefault": "SrF2 (F); albite (Na); olivine (Mg, Fe, Si); quartz (Si); apatite (Ca, P); barite (S); tugtupite (Cl); rhodonite (Mn); ilmenite (Fe, Ti)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "empa",
      "schema:termCode": "empa"
    }
  ],
  "ada:edsAcquisitionMode": "missing",
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EMPA/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:empaTAPP-JEOL8530",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA Major Element Apatite incl. Halogens, Bennu (ARES JSC, JEOL 8530 EMPA)",
  "schema:description": "Seifert et al. 2026, Meteorit. Planet. Sci. \u2014 apatite in Bennu OSIRIS-REx samples. ARES NASA JSC. Instrument stated as \"JEOL 8530 EMPA at NASA JSC\" (no \"JXA\", no \"F\", no \"+\" suffix stated in paper). Analytical conditions: 15 kV, 20 nA, 2 \u00b5m probe size. Previous v2 values of 10/40-100 nA and 10 \u00b5m beam were WRONG \u2014 those were Durango apatite test conditions used to assess beam damage, not the actual protocol. Analytes: P, F, Cl, Ca, Mn, Fe, Na, Mg, Si, S. Apatite stoichiometry by Ketcham (2015) method (13-anion basis; OH by difference). Halogen correction on O: Yes. Primary standards: SrF2, albite, olivine, quartz, apatite, barite, tugtupite, rhodonite, ilmenite. Sample preparation: fragments embedded in epoxy, dry-polished, ion-polished (one mount), carbon coated. 14 total analyses performed.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV",
      "ada:beamDiameterDefault": "2 \u00b5m (stated as \"2 \u00b5m probe size\")",
      "ada:beamMode": "Focused (2 \u00b5m probe size stated)",
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        }
      ],
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "JEOL 8530 EMPA (stated as \"JEOL 8530 EMPA at NASA JSC\"; no F suffix or JXA prefix stated)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/empaTAPP/beamDamageMinimizationDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "beamDamageMinimizationDefault",
      "schema:name": "Beam Damage Minimization",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "2 \u00b5m probe used for all analyses; Durango apatite tested at 10 \u00b5m and 3 \u00b5m spot sizes to assess halogen volatilization; no significant loss found under adopted conditions"
    },
    {
      "@id": "ada:parameter/empaTAPP/halogenCorrectionOnOxygenDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "halogenCorrectionOnOxygenDefault",
      "schema:name": "Halogen Correction on Oxygen",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Yes (F and Cl substitution in apatite; 1-F-Cl=OH)"
    }
  ],
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Phosphate (apatite)"
          ]
        }
      ]
    }
  ],
  "ada:monitoredEleemnts": [
    "P, F, Cl, Ca, Mn, Fe, Na, Mg, Si, S \u2014 all determined. \"A total of 14 analyses were performed at 15 kV, 20 nA, using a 2 \u03bcm probe size, and included the elements P, F, Cl, Ca, Mn, Fe, Na, Mg, Si, and S\" (p.3)"
  ],
  "schema:creator": {
    "schema:name": "Logan B. Seifert",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "ARES, NASA Johnson Space Center"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Seifert et al. 2026, Meteorit. Planet. Sci.; doi:10.1111/maps.70167"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM-EDS; SIMS (Cameca ims 1280); TEM-EDS"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Fragments embedded in epoxy; dry-polished with diamond powder; one mount ion-polished before carbon coating",
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 1
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
        "schema:position": 2,
        "ada:detectionLimitMethod": "missing"
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "ada:primaryStandardNameDefault": "SrF2 (F); albite (Na); olivine (Mg, Fe, Si); quartz (Si); apatite (Ca, P); barite (S); tugtupite (Cl); rhodonite (Mn); ilmenite (Fe, Ti)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "empa",
      "schema:termCode": "empa"
    }
  ],
  "ada:edsAcquisitionMode": "missing",
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
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

ex:empaTAPP-JEOL8530 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Fragments embedded in epoxy; dry-polished with diamond powder; one mount ion-polished before carbon coating" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ;
                    ada:detectionLimitMethod "missing" ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/empaTAPP/beamDamageMinimizationDefault>,
        <https://ada.astromat.org/metadata/parameter/empaTAPP/halogenCorrectionOnOxygenDefault> ;
    schema1:creator [ a schema1:Person ;
            schema1:name "Logan B. Seifert" ] ;
    schema1:datePublished "missing" ;
    schema1:description "Seifert et al. 2026, Meteorit. Planet. Sci. — apatite in Bennu OSIRIS-REx samples. ARES NASA JSC. Instrument stated as \"JEOL 8530 EMPA at NASA JSC\" (no \"JXA\", no \"F\", no \"+\" suffix stated in paper). Analytical conditions: 15 kV, 20 nA, 2 µm probe size. Previous v2 values of 10/40-100 nA and 10 µm beam were WRONG — those were Durango apatite test conditions used to assess beam damage, not the actual protocol. Analytes: P, F, Cl, Ca, Mn, Fe, Na, Mg, Si, S. Apatite stoichiometry by Ketcham (2015) method (13-anion basis; OH by difference). Halogen correction on O: Yes. Primary standards: SrF2, albite, olivine, quartz, apatite, barite, tugtupite, rhodonite, ilmenite. Sample preparation: fragments embedded in epoxy, dry-polished, ion-polished (one mount), carbon coated. 14 total analyses performed." ;
    schema1:instrument <https://example.org/instrument/EPMA>,
        <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "ARES, NASA Johnson Space Center" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "empa" ;
            schema1:termCode "empa" ] ;
    schema1:name "EPMA Major Element Apatite incl. Halogens, Bennu (ARES JSC, JEOL 8530 EMPA)" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Phosphate (apatite)" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Seifert et al. 2026, Meteorit. Planet. Sci.; doi:10.1111/maps.70167" ] ;
            schema1:url "https://ada.astromat.org/missing" ],
        [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "SEM-EDS; SIMS (Cameca ims 1280); TEM-EDS" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:edsAcquisitionMode "missing" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:monitoredEleemnts "P, F, Cl, Ca, Mn, Fe, Na, Mg, Si, S — all determined. \"A total of 14 analyses were performed at 15 kV, 20 nA, using a 2 μm probe size, and included the elements P, F, Cl, Ca, Mn, Fe, Na, Mg, Si, and S\" (p.3)" ;
    ada:primaryStandardNameDefault "SrF2 (F); albite (Na); olivine (Mg, Fe, Si); quartz (Si); apatite (Ca, P); barite (S); tugtupite (Cl); rhodonite (Mn); ilmenite (Fe, Ti)" ;
    ada:samplingUnit "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:wdsDeadTimeCorrection "missing" .

<https://ada.astromat.org/metadata/parameter/empaTAPP/beamDamageMinimizationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "2 µm probe used for all analyses; Durango apatite tested at 10 µm and 3 µm spot sizes to assess halogen volatilization; no significant loss found under adopted conditions" ;
    schema1:name "Beam Damage Minimization" ;
    schema1:valueName "beamDamageMinimizationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/empaTAPP/halogenCorrectionOnOxygenDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Yes (F and Cl substitution in apatite; 1-F-Cl=OH)" ;
    schema1:name "Halogen Correction on Oxygen" ;
    schema1:valueName "halogenCorrectionOnOxygenDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://example.org/instrument/EPMA> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EPMA" ;
    schema1:hasPart <https://example.org/instrument/EPMA/part/EDS-Detector>,
        <https://example.org/instrument/EPMA/part/Electron-Source>,
        <https://example.org/instrument/EPMA/part/WDS-Spectrometer> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "JEOL" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "15 kV" ;
    ada:beamDiameterDefault "2 µm (stated as \"2 µm probe size\")" ;
    ada:beamMode "Focused (2 µm probe size stated)" .

<https://example.org/instrument/EPMA/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/EPMA/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "missing" ;
    schema1:name "missing" .

<https://example.org/instrument/EPMA/part/WDS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "WDS Spectrometer" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "JEOL 8530 EMPA (stated as \"JEOL 8530 EMPA at NASA JSC\"; no F suffix or JXA prefix stated)" ] ;
    schema1:name "example instrumentName" .


```


### empaTAPP example P8
empaTAPP instance derived from Pang+2016 | JEOL JXA-8100 | WDS Point Analysis (Nanjing U.).
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
  "@id": "ex:empaTAPP-P8",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS Major Element Silicates/Oxides, NWA 8003 Eucrite (Nanjing U., JEOL JXA-8100)",
  "schema:description": "Pang et al. 2016, Sci. Rep. 6:26063 — NWA 8003 eucrite, Nanjing University. JEOL JXA-8100 (stated as \"JEOL 8100\"). WDS explicitly stated (\"JEOL 8100 WDS\"). ZAF matrix correction (NOT \"ZAF or PAP\" as in v2; paper states ZAF). Focused beam (20 nA) for most phases; defocused 2-5 µm for plagioclase and polymorphs. Natural and synthetic mineral standards (specific names N). Detection limit better than 0.02 wt% (as stated). Analytical software not stated.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV",
      "ada:beamDiameterDefault": "Focused (exact diameter N); 2-5 µm defocused (plagioclase and polymorphs)",
      "ada:beamMode": "Focused (most phases); Defocused 2-5 µm (plagioclase and polymorphs)",
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        }
      ],
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "JXA-8100 (stated as \"JEOL 8100\")",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:matrixCorrectionMethod": "ZAF",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Silicate mineral | Oxide (eucrite phases)"
          ]
        }
      ]
    }
  ],
  "ada:monitoredEleemnts": [
    "N — \"Natural and synthetic standards were used\" (p.7) without naming them; the analysed elements are given in Supplementary Table 4, which is not in the archived PDF"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "EPMA-WDS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "State Key Laboratory for Mineral Deposits Research, Nanjing University"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Pang et al. 2016, Sci. Rep. 6:26063; doi:10.1038/srep26063"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM (BSE imaging); petrographic microscopy"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Polished thin section; carbon coating N",
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 1
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
        "schema:position": 2,
        "ada:detectionLimitMethod": "missing"
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "ada:primaryStandardNameDefault": "Natural and synthetic mineral standards (specific names N)",
  "ada:edsAcquisitionMode": "missing",
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EMPA/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:empaTAPP-P8",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS Major Element Silicates/Oxides, NWA 8003 Eucrite (Nanjing U., JEOL JXA-8100)",
  "schema:description": "Pang et al. 2016, Sci. Rep. 6:26063 \u2014 NWA 8003 eucrite, Nanjing University. JEOL JXA-8100 (stated as \"JEOL 8100\"). WDS explicitly stated (\"JEOL 8100 WDS\"). ZAF matrix correction (NOT \"ZAF or PAP\" as in v2; paper states ZAF). Focused beam (20 nA) for most phases; defocused 2-5 \u00b5m for plagioclase and polymorphs. Natural and synthetic mineral standards (specific names N). Detection limit better than 0.02 wt% (as stated). Analytical software not stated.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV",
      "ada:beamDiameterDefault": "Focused (exact diameter N); 2-5 \u00b5m defocused (plagioclase and polymorphs)",
      "ada:beamMode": "Focused (most phases); Defocused 2-5 \u00b5m (plagioclase and polymorphs)",
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        }
      ],
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "JXA-8100 (stated as \"JEOL 8100\")",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:matrixCorrectionMethod": "ZAF",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Silicate mineral | Oxide (eucrite phases)"
          ]
        }
      ]
    }
  ],
  "ada:monitoredEleemnts": [
    "N \u2014 \"Natural and synthetic standards were used\" (p.7) without naming them; the analysed elements are given in Supplementary Table 4, which is not in the archived PDF"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "EPMA-WDS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "State Key Laboratory for Mineral Deposits Research, Nanjing University"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Pang et al. 2016, Sci. Rep. 6:26063; doi:10.1038/srep26063"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM (BSE imaging); petrographic microscopy"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Polished thin section; carbon coating N",
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 1
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
        "schema:position": 2,
        "ada:detectionLimitMethod": "missing"
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "ada:primaryStandardNameDefault": "Natural and synthetic mineral standards (specific names N)",
  "ada:edsAcquisitionMode": "missing",
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
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

ex:empaTAPP-P8 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Polished thin section; carbon coating N" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ;
                    ada:detectionLimitMethod "missing" ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "Pang et al. 2016, Sci. Rep. 6:26063 — NWA 8003 eucrite, Nanjing University. JEOL JXA-8100 (stated as \"JEOL 8100\"). WDS explicitly stated (\"JEOL 8100 WDS\"). ZAF matrix correction (NOT \"ZAF or PAP\" as in v2; paper states ZAF). Focused beam (20 nA) for most phases; defocused 2-5 µm for plagioclase and polymorphs. Natural and synthetic mineral standards (specific names N). Detection limit better than 0.02 wt% (as stated). Analytical software not stated." ;
    schema1:instrument <https://example.org/instrument/EPMA>,
        <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "State Key Laboratory for Mineral Deposits Research, Nanjing University" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "EPMA-WDS" ] ;
    schema1:name "EPMA-WDS Major Element Silicates/Oxides, NWA 8003 Eucrite (Nanjing U., JEOL JXA-8100)" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Silicate mineral | Oxide (eucrite phases)" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "SEM (BSE imaging); petrographic microscopy" ] ;
            schema1:url "https://ada.astromat.org/missing" ],
        [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Pang et al. 2016, Sci. Rep. 6:26063; doi:10.1038/srep26063" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:edsAcquisitionMode "missing" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "ZAF" ;
    ada:monitoredEleemnts "N — \"Natural and synthetic standards were used\" (p.7) without naming them; the analysed elements are given in Supplementary Table 4, which is not in the archived PDF" ;
    ada:primaryStandardNameDefault "Natural and synthetic mineral standards (specific names N)" ;
    ada:samplingUnit "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:wdsDeadTimeCorrection "missing" .

<https://example.org/instrument/EPMA> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EPMA" ;
    schema1:hasPart <https://example.org/instrument/EPMA/part/EDS-Detector>,
        <https://example.org/instrument/EPMA/part/Electron-Source>,
        <https://example.org/instrument/EPMA/part/WDS-Spectrometer> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "JEOL" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "15 kV" ;
    ada:beamDiameterDefault "Focused (exact diameter N); 2-5 µm defocused (plagioclase and polymorphs)" ;
    ada:beamMode "Focused (most phases); Defocused 2-5 µm (plagioclase and polymorphs)" .

<https://example.org/instrument/EPMA/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/EPMA/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "missing" ;
    schema1:name "missing" .

<https://example.org/instrument/EPMA/part/WDS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "WDS Spectrometer" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "JXA-8100 (stated as \"JEOL 8100\")" ] ;
    schema1:name "example instrumentName" .


```


### empaTAPP example JEOL8530-2
empaTAPP instance derived from McCoy+2025_SI | JEOL 8530F+ | WDS Point Analysis (Smithsonian).
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
  "@id": "ex:empaTAPP-JEOL8530-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS Carbonate+Silicate/Oxide Composition, Bennu (Smithsonian, JEOL 8530 F+ Hyperprobe)",
  "schema:description": "McCoy et al. 2025, Nature 637:320-325 — Bennu evaporites. Protocol 1 of 2: Smithsonian Institution JEOL 8530 F+ Hyperprobe (Field Emission). Ir-coated specimens mounted on Ir-coated Parafilm. Carbonate analyses: 15 kV, 10 nA, 5 µm spot; LIFL (Fe,Mn), TAPL (Mg), PETL (Ca). Silicate/oxide analyses: 15 kV, 10 nA, 1 µm spot; broader standard suite. Both primary and secondary standard suites fully documented with USNM catalog numbers. Acquisition software and matrix correction method N. WDS not explicitly stated in text (crystal designations LIFL/TAPL/PETL confirm WDS use).",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV",
      "ada:beamDiameterDefault": "5 µm (carbonates); 1 µm (silicates/oxides)",
      "ada:beamMode": "Focused (1 µm, silicates/oxides); Focused (5 µm, carbonates)",
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Unknown",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "LIFL (Fe Ka, Mn Ka); TAPL (Mg Ka); PETL (Ca Ka) — partial; full config N",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "JXA-8530F Plus (stated as \"JEOL 8530 F+ Hyperprobe Field Emission Electron Probe Microanalyzer\")",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:secondaryReferenceMaterialDefault": [
    "Carbonates: calcite, dolomite, rhodochrosite; Silicates/oxides: magnetite, San Carlos olivine USNM 111312, Springwater olivine USNM 2566"
  ],
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Carbonate | Oxide | Silicate mineral (Bennu evaporite and host phases)"
          ]
        }
      ]
    }
  ],
  "ada:monitoredEleemnts": [
    "Fe, Mn, Mg, Ca — all determined. \"Carbonate analyses were run at 15 kV and 10 nA, with an analytical spot size of 5 µm. Fe and Mn were analysed using a LIFL crystal, Mg using a TAPL crystal and Ca using a PETL crystal\" (p.7)"
  ],
  "schema:creator": {
    "schema:name": "T. J. McCoy",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Smithsonian Institution, National Museum of Natural History"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "McCoy et al. 2025, Nature 637:320-325; doi:10.1038/s41586-024-08495-6"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM-EDS (NHM London; Smithsonian; JSC); TEM-EDS/EELS; FIB-SEM; ToF-SIMS; XRD; XANES"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Ir-coated specimens mounted on Ir-coated Parafilm",
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 1
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
        "schema:position": 2,
        "ada:detectionLimitMethod": "missing"
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "ada:primaryStandardNameDefault": "Carbonates: magnetite USNM 114887 (Fe,Mn), calcite USNM 13621 (Ca), dolomite USNM 10057 (Mg), siderite R-2460, rhodonite; Silicates/oxides: chromite USNM 117075, ilmenite USNM 96189, magnetite USNM 114887, manganite USNM 157872, bytownite R-2912, forsterite P140, San Carlos olivine USNM 111312 (Fo90), Springwater olivine USNM 2566 (Fo83)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "empa",
      "schema:termCode": "empa"
    }
  ],
  "ada:edsAcquisitionMode": "missing",
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EMPA/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:empaTAPP-JEOL8530-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS Carbonate+Silicate/Oxide Composition, Bennu (Smithsonian, JEOL 8530 F+ Hyperprobe)",
  "schema:description": "McCoy et al. 2025, Nature 637:320-325 \u2014 Bennu evaporites. Protocol 1 of 2: Smithsonian Institution JEOL 8530 F+ Hyperprobe (Field Emission). Ir-coated specimens mounted on Ir-coated Parafilm. Carbonate analyses: 15 kV, 10 nA, 5 \u00b5m spot; LIFL (Fe,Mn), TAPL (Mg), PETL (Ca). Silicate/oxide analyses: 15 kV, 10 nA, 1 \u00b5m spot; broader standard suite. Both primary and secondary standard suites fully documented with USNM catalog numbers. Acquisition software and matrix correction method N. WDS not explicitly stated in text (crystal designations LIFL/TAPL/PETL confirm WDS use).",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV",
      "ada:beamDiameterDefault": "5 \u00b5m (carbonates); 1 \u00b5m (silicates/oxides)",
      "ada:beamMode": "Focused (1 \u00b5m, silicates/oxides); Focused (5 \u00b5m, carbonates)",
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Unknown",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "LIFL (Fe Ka, Mn Ka); TAPL (Mg Ka); PETL (Ca Ka) \u2014 partial; full config N",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "JXA-8530F Plus (stated as \"JEOL 8530 F+ Hyperprobe Field Emission Electron Probe Microanalyzer\")",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:secondaryReferenceMaterialDefault": [
    "Carbonates: calcite, dolomite, rhodochrosite; Silicates/oxides: magnetite, San Carlos olivine USNM 111312, Springwater olivine USNM 2566"
  ],
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Carbonate | Oxide | Silicate mineral (Bennu evaporite and host phases)"
          ]
        }
      ]
    }
  ],
  "ada:monitoredEleemnts": [
    "Fe, Mn, Mg, Ca \u2014 all determined. \"Carbonate analyses were run at 15 kV and 10 nA, with an analytical spot size of 5 \u00b5m. Fe and Mn were analysed using a LIFL crystal, Mg using a TAPL crystal and Ca using a PETL crystal\" (p.7)"
  ],
  "schema:creator": {
    "schema:name": "T. J. McCoy",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Smithsonian Institution, National Museum of Natural History"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "McCoy et al. 2025, Nature 637:320-325; doi:10.1038/s41586-024-08495-6"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM-EDS (NHM London; Smithsonian; JSC); TEM-EDS/EELS; FIB-SEM; ToF-SIMS; XRD; XANES"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Ir-coated specimens mounted on Ir-coated Parafilm",
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 1
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
        "schema:position": 2,
        "ada:detectionLimitMethod": "missing"
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "ada:primaryStandardNameDefault": "Carbonates: magnetite USNM 114887 (Fe,Mn), calcite USNM 13621 (Ca), dolomite USNM 10057 (Mg), siderite R-2460, rhodonite; Silicates/oxides: chromite USNM 117075, ilmenite USNM 96189, magnetite USNM 114887, manganite USNM 157872, bytownite R-2912, forsterite P140, San Carlos olivine USNM 111312 (Fo90), Springwater olivine USNM 2566 (Fo83)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "empa",
      "schema:termCode": "empa"
    }
  ],
  "ada:edsAcquisitionMode": "missing",
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
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

ex:empaTAPP-JEOL8530-2 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Ir-coated specimens mounted on Ir-coated Parafilm" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ;
                    ada:detectionLimitMethod "missing" ] ] ;
    schema1:creator [ a schema1:Person ;
            schema1:name "T. J. McCoy" ] ;
    schema1:datePublished "missing" ;
    schema1:description "McCoy et al. 2025, Nature 637:320-325 — Bennu evaporites. Protocol 1 of 2: Smithsonian Institution JEOL 8530 F+ Hyperprobe (Field Emission). Ir-coated specimens mounted on Ir-coated Parafilm. Carbonate analyses: 15 kV, 10 nA, 5 µm spot; LIFL (Fe,Mn), TAPL (Mg), PETL (Ca). Silicate/oxide analyses: 15 kV, 10 nA, 1 µm spot; broader standard suite. Both primary and secondary standard suites fully documented with USNM catalog numbers. Acquisition software and matrix correction method N. WDS not explicitly stated in text (crystal designations LIFL/TAPL/PETL confirm WDS use)." ;
    schema1:instrument <https://example.org/instrument/EPMA>,
        <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Smithsonian Institution, National Museum of Natural History" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "empa" ;
            schema1:termCode "empa" ] ;
    schema1:name "EPMA-WDS Carbonate+Silicate/Oxide Composition, Bennu (Smithsonian, JEOL 8530 F+ Hyperprobe)" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Carbonate | Oxide | Silicate mineral (Bennu evaporite and host phases)" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "McCoy et al. 2025, Nature 637:320-325; doi:10.1038/s41586-024-08495-6" ] ;
            schema1:url "https://ada.astromat.org/missing" ],
        [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "SEM-EDS (NHM London; Smithsonian; JSC); TEM-EDS/EELS; FIB-SEM; ToF-SIMS; XRD; XANES" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:edsAcquisitionMode "missing" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:monitoredEleemnts "Fe, Mn, Mg, Ca — all determined. \"Carbonate analyses were run at 15 kV and 10 nA, with an analytical spot size of 5 µm. Fe and Mn were analysed using a LIFL crystal, Mg using a TAPL crystal and Ca using a PETL crystal\" (p.7)" ;
    ada:primaryStandardNameDefault "Carbonates: magnetite USNM 114887 (Fe,Mn), calcite USNM 13621 (Ca), dolomite USNM 10057 (Mg), siderite R-2460, rhodonite; Silicates/oxides: chromite USNM 117075, ilmenite USNM 96189, magnetite USNM 114887, manganite USNM 157872, bytownite R-2912, forsterite P140, San Carlos olivine USNM 111312 (Fo90), Springwater olivine USNM 2566 (Fo83)" ;
    ada:samplingUnit "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:secondaryReferenceMaterialDefault "Carbonates: calcite, dolomite, rhodochrosite; Silicates/oxides: magnetite, San Carlos olivine USNM 111312, Springwater olivine USNM 2566" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:wdsDeadTimeCorrection "missing" .

<https://example.org/instrument/EPMA> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EPMA" ;
    schema1:hasPart <https://example.org/instrument/EPMA/part/EDS-Detector>,
        <https://example.org/instrument/EPMA/part/Electron-Source>,
        <https://example.org/instrument/EPMA/part/WDS-Spectrometer> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "JEOL" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "15 kV" ;
    ada:beamDiameterDefault "5 µm (carbonates); 1 µm (silicates/oxides)" ;
    ada:beamMode "Focused (1 µm, silicates/oxides); Focused (5 µm, carbonates)" .

<https://example.org/instrument/EPMA/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/EPMA/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "Unknown" ;
    schema1:name "missing" .

<https://example.org/instrument/EPMA/part/WDS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "WDS Spectrometer" ;
    schema1:name "LIFL (Fe Ka, Mn Ka); TAPL (Mg Ka); PETL (Ca Ka) — partial; full config N" .

<https://example.org/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "JXA-8530F Plus (stated as \"JEOL 8530 F+ Hyperprobe Field Emission Electron Probe Microanalyzer\")" ] ;
    schema1:name "example instrumentName" .


```


### empaTAPP example P10
empaTAPP instance derived from McCoy+2025_UA | Cameca SX-100 | WDS Point Analysis (K-ALFAA U.Arizona).
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
  "@id": "ex:empaTAPP-P10",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS Phosphate+Carbonate Composition, Bennu (K-ALFAA U.Arizona, Cameca SX-100)",
  "schema:description": "McCoy et al. 2025, Nature 637:320-325 — Bennu evaporites. Protocol 2 of 2: U. Arizona K-ALFAA Cameca SX-100. 20 nm carbon coat. WDS explicitly stated for phosphate analyses. Mg,Na phosphate analyses: 15 kV, 8 nA, 1 µm. Carbonate analyses at K-ALFAA also mentioned; conditions N. Full primary standard suite documented for phosphates and carbonates. Acquisition software and matrix correction method N.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV",
      "ada:beamDiameterDefault": "1 µm",
      "ada:beamMode": "Focused (1 µm)",
      "schema:manufacturer": {
        "schema:name": "Cameca",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        }
      ],
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "SX-100 (stated as \"Cameca SX-100 electron microprobe located at K-ALFAA\")",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Phosphate (Mg,Na phosphate) | Carbonate (Bennu evaporite phases)"
          ]
        }
      ]
    }
  ],
  "ada:monitoredEleemnts": [
    "F, P, Ca, Si, Mg, Fe, Al, S, K, Cl (Mg,Na phosphate) and Na, Si, Mg, Ca, Mn (carbonates) — all determined. \"The standards used for Mg,Na phosphate were fluorapatite (F, P, Ca), Fo92 olivine (Si, Mg), rhodonite (Mg), fayalite (Fe), anorthite (Al), baryte (S), potassium feldspar (K) and scapolite (Cl). For carbonates, the standards used were albite (Na), Fo92 olivine (Si), dolomite (Mg), calcite (Ca), Mn...\" (p.7)"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "EPMA-WDS"
    }
  ],
  "schema:creator": {
    "schema:name": "T. J. Zega",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Kuiper-Arizona Laboratory for Astromaterials Analysis (K-ALFAA), University of Arizona"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "McCoy et al. 2025, Nature 637:320-325; doi:10.1038/s41586-024-08495-6"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM-EDS (NHM London; Smithsonian; JSC); TEM-EDS/EELS; FIB-SEM; ToF-SIMS; XRD; XANES"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Polished section; 20 nm carbon coat",
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 1
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
        "schema:position": 2,
        "ada:detectionLimitMethod": "missing"
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "ada:primaryStandardNameDefault": "Phosphates: fluorapatite (F, P, Ca), Fo92 olivine (Si, Mg), rhodonite (Mn), fayalite (Fe), anorthite (Al), baryte (S), K-feldspar (K), scapolite (Cl); Carbonates: albite (Na), Fo olivine (Si), dolomite (Mg), calcite (Ca), Mn carbonate (Mn), apatite (P), baryte (S), fayalite (Fe)",
  "ada:edsAcquisitionMode": "missing",
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EMPA/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:empaTAPP-P10",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS Phosphate+Carbonate Composition, Bennu (K-ALFAA U.Arizona, Cameca SX-100)",
  "schema:description": "McCoy et al. 2025, Nature 637:320-325 \u2014 Bennu evaporites. Protocol 2 of 2: U. Arizona K-ALFAA Cameca SX-100. 20 nm carbon coat. WDS explicitly stated for phosphate analyses. Mg,Na phosphate analyses: 15 kV, 8 nA, 1 \u00b5m. Carbonate analyses at K-ALFAA also mentioned; conditions N. Full primary standard suite documented for phosphates and carbonates. Acquisition software and matrix correction method N.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV",
      "ada:beamDiameterDefault": "1 \u00b5m",
      "ada:beamMode": "Focused (1 \u00b5m)",
      "schema:manufacturer": {
        "schema:name": "Cameca",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        }
      ],
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "SX-100 (stated as \"Cameca SX-100 electron microprobe located at K-ALFAA\")",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Phosphate (Mg,Na phosphate) | Carbonate (Bennu evaporite phases)"
          ]
        }
      ]
    }
  ],
  "ada:monitoredEleemnts": [
    "F, P, Ca, Si, Mg, Fe, Al, S, K, Cl (Mg,Na phosphate) and Na, Si, Mg, Ca, Mn (carbonates) \u2014 all determined. \"The standards used for Mg,Na phosphate were fluorapatite (F, P, Ca), Fo92 olivine (Si, Mg), rhodonite (Mg), fayalite (Fe), anorthite (Al), baryte (S), potassium feldspar (K) and scapolite (Cl). For carbonates, the standards used were albite (Na), Fo92 olivine (Si), dolomite (Mg), calcite (Ca), Mn...\" (p.7)"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "EPMA-WDS"
    }
  ],
  "schema:creator": {
    "schema:name": "T. J. Zega",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Kuiper-Arizona Laboratory for Astromaterials Analysis (K-ALFAA), University of Arizona"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "McCoy et al. 2025, Nature 637:320-325; doi:10.1038/s41586-024-08495-6"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM-EDS (NHM London; Smithsonian; JSC); TEM-EDS/EELS; FIB-SEM; ToF-SIMS; XRD; XANES"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Polished section; 20 nm carbon coat",
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 1
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
        "schema:position": 2,
        "ada:detectionLimitMethod": "missing"
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "ada:primaryStandardNameDefault": "Phosphates: fluorapatite (F, P, Ca), Fo92 olivine (Si, Mg), rhodonite (Mn), fayalite (Fe), anorthite (Al), baryte (S), K-feldspar (K), scapolite (Cl); Carbonates: albite (Na), Fo olivine (Si), dolomite (Mg), calcite (Ca), Mn carbonate (Mn), apatite (P), baryte (S), fayalite (Fe)",
  "ada:edsAcquisitionMode": "missing",
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
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

ex:empaTAPP-P10 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Polished section; 20 nm carbon coat" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ;
                    ada:detectionLimitMethod "missing" ] ] ;
    schema1:creator [ a schema1:Person ;
            schema1:name "T. J. Zega" ] ;
    schema1:datePublished "missing" ;
    schema1:description "McCoy et al. 2025, Nature 637:320-325 — Bennu evaporites. Protocol 2 of 2: U. Arizona K-ALFAA Cameca SX-100. 20 nm carbon coat. WDS explicitly stated for phosphate analyses. Mg,Na phosphate analyses: 15 kV, 8 nA, 1 µm. Carbonate analyses at K-ALFAA also mentioned; conditions N. Full primary standard suite documented for phosphates and carbonates. Acquisition software and matrix correction method N." ;
    schema1:instrument <https://example.org/instrument/EPMA>,
        <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Kuiper-Arizona Laboratory for Astromaterials Analysis (K-ALFAA), University of Arizona" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "EPMA-WDS" ] ;
    schema1:name "EPMA-WDS Phosphate+Carbonate Composition, Bennu (K-ALFAA U.Arizona, Cameca SX-100)" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Phosphate (Mg,Na phosphate) | Carbonate (Bennu evaporite phases)" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "SEM-EDS (NHM London; Smithsonian; JSC); TEM-EDS/EELS; FIB-SEM; ToF-SIMS; XRD; XANES" ] ;
            schema1:url "https://ada.astromat.org/missing" ],
        [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "McCoy et al. 2025, Nature 637:320-325; doi:10.1038/s41586-024-08495-6" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:edsAcquisitionMode "missing" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:monitoredEleemnts "F, P, Ca, Si, Mg, Fe, Al, S, K, Cl (Mg,Na phosphate) and Na, Si, Mg, Ca, Mn (carbonates) — all determined. \"The standards used for Mg,Na phosphate were fluorapatite (F, P, Ca), Fo92 olivine (Si, Mg), rhodonite (Mg), fayalite (Fe), anorthite (Al), baryte (S), potassium feldspar (K) and scapolite (Cl). For carbonates, the standards used were albite (Na), Fo92 olivine (Si), dolomite (Mg), calcite (Ca), Mn...\" (p.7)" ;
    ada:primaryStandardNameDefault "Phosphates: fluorapatite (F, P, Ca), Fo92 olivine (Si, Mg), rhodonite (Mn), fayalite (Fe), anorthite (Al), baryte (S), K-feldspar (K), scapolite (Cl); Carbonates: albite (Na), Fo olivine (Si), dolomite (Mg), calcite (Ca), Mn carbonate (Mn), apatite (P), baryte (S), fayalite (Fe)" ;
    ada:samplingUnit "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:wdsDeadTimeCorrection "missing" .

<https://example.org/instrument/EPMA> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EPMA" ;
    schema1:hasPart <https://example.org/instrument/EPMA/part/EDS-Detector>,
        <https://example.org/instrument/EPMA/part/Electron-Source>,
        <https://example.org/instrument/EPMA/part/WDS-Spectrometer> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Cameca" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "15 kV" ;
    ada:beamDiameterDefault "1 µm" ;
    ada:beamMode "Focused (1 µm)" .

<https://example.org/instrument/EPMA/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/EPMA/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "missing" ;
    schema1:name "missing" .

<https://example.org/instrument/EPMA/part/WDS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "WDS Spectrometer" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "SX-100 (stated as \"Cameca SX-100 electron microprobe located at K-ALFAA\")" ] ;
    schema1:name "example instrumentName" .


```


### empaTAPP example P11
empaTAPP instance derived from Zega+2025 | Cameca SX-100 Ultra | WDS Point Analysis (K-ALFAA U.Arizona).
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
  "@id": "ex:empaTAPP-P11",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA Major Element Silicates/Sulfides/Oxides/Phosphates/Carbonates, Bennu (K-ALFAA, Cameca SX-100 Ultra)",
  "schema:description": "Zega et al. 2025, Nat. Geosci. — mineralogical evidence for hydrothermal alteration of Bennu. K-ALFAA, University of Arizona. Instrument stated as \"SX-100 Ultra electron microprobe in the K-ALFAA\". IMPORTANT: v2 had \"no protocol details reported\" — this was WRONG. The paper provides detailed EPMA conditions: X-ray maps and BSE images: 15 kV, 20 nA. Silicates/sulfides/oxides: 15 kV, 20 nA, focused, 20 s peak, 10 s/bg each side. Phosphates: 15 kV, 8 nA, 2 µm defocused, 20 s peak, 10 s/bg each side. Carbonates: 15 kV, 4 nA, 2 µm, 10 s peak, 5 s/bg each side. Standards: \"well-characterized natural and synthetic materials\" (specific names N). Phase maps generated using XMapTools. WDS and matrix correction NOT explicitly stated in paper.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV",
      "ada:beamDiameterDefault": "Focused (silicates, sulfides, oxides); 2 µm defocused (phosphates, carbonates)",
      "ada:beamMode": "Focused (silicates, sulfides, oxides); Defocused 2 µm (phosphates, carbonates)",
      "schema:manufacturer": {
        "schema:name": "Cameca",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        }
      ],
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "SX-100 Ultra (stated as \"SX-100 Ultra electron microprobe in the K-ALFAA\")",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/empaTAPP/beamDamageMinimizationDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "beamDamageMinimizationDefault",
      "schema:name": "Beam Damage Minimization",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Defocused 2 µm beam for phosphates (8 nA) and carbonates (4 nA)"
    }
  ],
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Silicate mineral | Sulfide | Oxide | Phosphate | Carbonate (Bennu samples)"
          ]
        }
      ]
    }
  ],
  "ada:monitoredEleemnts": [
    "N — \"Well-characterized natural and synthetic materials were used as standards\" (p.9); the paper gives beam conditions and count times for silicates, sulfides, oxides, phosphates and carbonates but names no element"
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Kuiper-Arizona Laboratory for Astromaterials Analysis (K-ALFAA), University of Arizona"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Zega et al. 2025, Nat. Geosci.; doi:10.1038/s41561-025-01741-0"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM-EDS; TEM-EDS/EELS; FIB-SEM; XRD; XANES"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "XMapTools (for phase maps)"
    }
  ],
  "ada:primaryStandardNameDefault": "Well-characterized natural and synthetic materials (specific names N)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "empa",
      "schema:termCode": "empa"
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
        "schema:position": 2,
        "ada:detectionLimitMethod": "missing"
      }
    ]
  },
  "ada:edsAcquisitionMode": "missing",
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EMPA/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:empaTAPP-P11",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA Major Element Silicates/Sulfides/Oxides/Phosphates/Carbonates, Bennu (K-ALFAA, Cameca SX-100 Ultra)",
  "schema:description": "Zega et al. 2025, Nat. Geosci. \u2014 mineralogical evidence for hydrothermal alteration of Bennu. K-ALFAA, University of Arizona. Instrument stated as \"SX-100 Ultra electron microprobe in the K-ALFAA\". IMPORTANT: v2 had \"no protocol details reported\" \u2014 this was WRONG. The paper provides detailed EPMA conditions: X-ray maps and BSE images: 15 kV, 20 nA. Silicates/sulfides/oxides: 15 kV, 20 nA, focused, 20 s peak, 10 s/bg each side. Phosphates: 15 kV, 8 nA, 2 \u00b5m defocused, 20 s peak, 10 s/bg each side. Carbonates: 15 kV, 4 nA, 2 \u00b5m, 10 s peak, 5 s/bg each side. Standards: \"well-characterized natural and synthetic materials\" (specific names N). Phase maps generated using XMapTools. WDS and matrix correction NOT explicitly stated in paper.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV",
      "ada:beamDiameterDefault": "Focused (silicates, sulfides, oxides); 2 \u00b5m defocused (phosphates, carbonates)",
      "ada:beamMode": "Focused (silicates, sulfides, oxides); Defocused 2 \u00b5m (phosphates, carbonates)",
      "schema:manufacturer": {
        "schema:name": "Cameca",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        }
      ],
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "SX-100 Ultra (stated as \"SX-100 Ultra electron microprobe in the K-ALFAA\")",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/empaTAPP/beamDamageMinimizationDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "beamDamageMinimizationDefault",
      "schema:name": "Beam Damage Minimization",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Defocused 2 \u00b5m beam for phosphates (8 nA) and carbonates (4 nA)"
    }
  ],
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Silicate mineral | Sulfide | Oxide | Phosphate | Carbonate (Bennu samples)"
          ]
        }
      ]
    }
  ],
  "ada:monitoredEleemnts": [
    "N \u2014 \"Well-characterized natural and synthetic materials were used as standards\" (p.9); the paper gives beam conditions and count times for silicates, sulfides, oxides, phosphates and carbonates but names no element"
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Kuiper-Arizona Laboratory for Astromaterials Analysis (K-ALFAA), University of Arizona"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Zega et al. 2025, Nat. Geosci.; doi:10.1038/s41561-025-01741-0"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM-EDS; TEM-EDS/EELS; FIB-SEM; XRD; XANES"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "XMapTools (for phase maps)"
    }
  ],
  "ada:primaryStandardNameDefault": "Well-characterized natural and synthetic materials (specific names N)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "empa",
      "schema:termCode": "empa"
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
        "schema:position": 2,
        "ada:detectionLimitMethod": "missing"
      }
    ]
  },
  "ada:edsAcquisitionMode": "missing",
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
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

ex:empaTAPP-P11 a cdi:Activity,
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
                    schema1:position 2 ;
                    ada:detectionLimitMethod "missing" ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/empaTAPP/beamDamageMinimizationDefault> ;
    schema1:datePublished "missing" ;
    schema1:description "Zega et al. 2025, Nat. Geosci. — mineralogical evidence for hydrothermal alteration of Bennu. K-ALFAA, University of Arizona. Instrument stated as \"SX-100 Ultra electron microprobe in the K-ALFAA\". IMPORTANT: v2 had \"no protocol details reported\" — this was WRONG. The paper provides detailed EPMA conditions: X-ray maps and BSE images: 15 kV, 20 nA. Silicates/sulfides/oxides: 15 kV, 20 nA, focused, 20 s peak, 10 s/bg each side. Phosphates: 15 kV, 8 nA, 2 µm defocused, 20 s peak, 10 s/bg each side. Carbonates: 15 kV, 4 nA, 2 µm, 10 s peak, 5 s/bg each side. Standards: \"well-characterized natural and synthetic materials\" (specific names N). Phase maps generated using XMapTools. WDS and matrix correction NOT explicitly stated in paper." ;
    schema1:instrument <https://example.org/instrument/EPMA>,
        <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Kuiper-Arizona Laboratory for Astromaterials Analysis (K-ALFAA), University of Arizona" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "empa" ;
            schema1:termCode "empa" ] ;
    schema1:name "EPMA Major Element Silicates/Sulfides/Oxides/Phosphates/Carbonates, Bennu (K-ALFAA, Cameca SX-100 Ultra)" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Silicate mineral | Sulfide | Oxide | Phosphate | Carbonate (Bennu samples)" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Zega et al. 2025, Nat. Geosci.; doi:10.1038/s41561-025-01741-0" ] ;
            schema1:url "https://ada.astromat.org/missing" ],
        [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "SEM-EDS; TEM-EDS/EELS; FIB-SEM; XRD; XANES" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:edsAcquisitionMode "missing" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:monitoredEleemnts "N — \"Well-characterized natural and synthetic materials were used as standards\" (p.9); the paper gives beam conditions and count times for silicates, sulfides, oxides, phosphates and carbonates but names no element" ;
    ada:primaryStandardNameDefault "Well-characterized natural and synthetic materials (specific names N)" ;
    ada:samplingUnit "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:wdsDeadTimeCorrection "missing" ;
    bios:computationalTool [ schema1:name "XMapTools (for phase maps)" ;
            ada:toolRole "dataReduction" ] .

<https://ada.astromat.org/metadata/parameter/empaTAPP/beamDamageMinimizationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Defocused 2 µm beam for phosphates (8 nA) and carbonates (4 nA)" ;
    schema1:name "Beam Damage Minimization" ;
    schema1:valueName "beamDamageMinimizationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://example.org/instrument/EPMA> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EPMA" ;
    schema1:hasPart <https://example.org/instrument/EPMA/part/EDS-Detector>,
        <https://example.org/instrument/EPMA/part/Electron-Source>,
        <https://example.org/instrument/EPMA/part/WDS-Spectrometer> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Cameca" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "15 kV" ;
    ada:beamDiameterDefault "Focused (silicates, sulfides, oxides); 2 µm defocused (phosphates, carbonates)" ;
    ada:beamMode "Focused (silicates, sulfides, oxides); Defocused 2 µm (phosphates, carbonates)" .

<https://example.org/instrument/EPMA/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/EPMA/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "missing" ;
    schema1:name "missing" .

<https://example.org/instrument/EPMA/part/WDS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "WDS Spectrometer" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "SX-100 Ultra (stated as \"SX-100 Ultra electron microprobe in the K-ALFAA\")" ] ;
    schema1:name "example instrumentName" .


```


### empaTAPP example P12
empaTAPP instance derived from Barnes+2025 | JEOL JXA-8230 | WDS Point Analysis (CRPG Nancy).
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
  "@id": "ex:empaTAPP-P12",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA Major Element Silicates/Oxides/Carbonates, Bennu Anhydrous Minerals (CRPG Nancy, JEOL JXA-8230)",
  "schema:description": "Barnes et al. 2025, Nat. Astron. — variety and origin of accreted materials in Bennu. Protocol 1 of 2: CRPG Nancy, JEOL JXA-8230. Instrument has 5 WDS spectrometers + 1 SDD EDS; per-analyte technique (WDS vs. EDS) not stated. Two analytical sessions: session 1 (no Na, K); session 2 (with Na, K). Counting times are stated as total peak + background combined: 200 ms for minor elements (Al, Ti, Ca, Mn, Cr) and 20 ms for major elements (Mg, Fe, Si) — unusually short, possibly per-pixel for fast mapping mode. Full primary standard suite stated with element assignments. Full per-element detection limits stated. Matrix correction method not stated. Sample preparation done at Université Côte d'Azur (not at CRPG). Beam current not stated for NHM protocol; 3 nA mentioned in text is for SEM-EDS (different instrument).",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "20 kV",
      "ada:beamDiameterDefault": "1 µm (point analysis); 5×5 µm² raster area for carbonates",
      "ada:beamMode": "Focused (1 µm, point analysis); Rastered 5×5 µm² for carbonates",
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "5 wavelength-dispersive spectrometers (JEOL)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "JXA-8230 (stated as \"JEOL JXA-8230 electron microprobe analyser (EPMA)\")",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/empaTAPP/beamRasterDimensionsDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "beamRasterDimensionsDefault",
      "schema:name": "Beam Raster Dimensions",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 5,
      "schema:description": "5×5 µm² for carbonates"
    }
  ],
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Silicate mineral (olivine, pyroxene) | Oxide | Carbonate (anhydrous minerals in Bennu aggregate particles)"
          ]
        }
      ]
    }
  ],
  "ada:monitoredEleemnts": [
    "Session 1: Al, Ti, Ca, Cr, Mn, Ni, Mg, Fe, Si. Session 2: Na, K, Al, Ti, Ca, Cr, Mn, Ni, Mg, Fe, Si. All determined. \"We used two different settings to determine the chemical compositions of minerals: (1) Al, Ti, Ca, Cr, Mn, Ni, Mg, Fe and Si (session 1) and (2) Na, K, Al, Ti, Ca, Cr, Mn, Ni, Mg, Fe and Si (session 2)\" (p.11)"
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Centre de Recherches Pétrographiques et Géochimiques (CRPG), Nancy, France"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Barnes et al. 2025, Nat. Astron.; doi:10.1038/s41550-025-02631-6"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM-BSE (JEOL JSM-6510, 15 kV, 3 nA); SEM-EDS (multi-element mapping); SIMS (CAMECA IMS 1270 E7, CRPG); NanoSIMS (K-ALFAA); ICP-MS; MC-ICP-MS; noble gas MS"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Aggregate particles (<1 mm) mounted in epoxy at Université Côte d'Azur; polished; carbon coated (thickness N)",
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 1
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
        "schema:position": 2,
        "ada:detectionLimitMethod": "missing"
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "ada:primaryStandardNameDefault": "Springwater olivine (Mg, Si); fayalite (Fe); wollastonite (Ca); albite (Na, Al); orthoclase (K); rutile (Ti); Ni metal (Ni); chromite (Cr); rhodochrosite (Mn)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "empa",
      "schema:termCode": "empa"
    }
  ],
  "ada:edsAcquisitionMode": "missing",
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EMPA/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:empaTAPP-P12",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA Major Element Silicates/Oxides/Carbonates, Bennu Anhydrous Minerals (CRPG Nancy, JEOL JXA-8230)",
  "schema:description": "Barnes et al. 2025, Nat. Astron. \u2014 variety and origin of accreted materials in Bennu. Protocol 1 of 2: CRPG Nancy, JEOL JXA-8230. Instrument has 5 WDS spectrometers + 1 SDD EDS; per-analyte technique (WDS vs. EDS) not stated. Two analytical sessions: session 1 (no Na, K); session 2 (with Na, K). Counting times are stated as total peak + background combined: 200 ms for minor elements (Al, Ti, Ca, Mn, Cr) and 20 ms for major elements (Mg, Fe, Si) \u2014 unusually short, possibly per-pixel for fast mapping mode. Full primary standard suite stated with element assignments. Full per-element detection limits stated. Matrix correction method not stated. Sample preparation done at Universit\u00e9 C\u00f4te d'Azur (not at CRPG). Beam current not stated for NHM protocol; 3 nA mentioned in text is for SEM-EDS (different instrument).",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "20 kV",
      "ada:beamDiameterDefault": "1 \u00b5m (point analysis); 5\u00d75 \u00b5m\u00b2 raster area for carbonates",
      "ada:beamMode": "Focused (1 \u00b5m, point analysis); Rastered 5\u00d75 \u00b5m\u00b2 for carbonates",
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "5 wavelength-dispersive spectrometers (JEOL)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "JXA-8230 (stated as \"JEOL JXA-8230 electron microprobe analyser (EPMA)\")",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/empaTAPP/beamRasterDimensionsDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "beamRasterDimensionsDefault",
      "schema:name": "Beam Raster Dimensions",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 5,
      "schema:description": "5\u00d75 \u00b5m\u00b2 for carbonates"
    }
  ],
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Silicate mineral (olivine, pyroxene) | Oxide | Carbonate (anhydrous minerals in Bennu aggregate particles)"
          ]
        }
      ]
    }
  ],
  "ada:monitoredEleemnts": [
    "Session 1: Al, Ti, Ca, Cr, Mn, Ni, Mg, Fe, Si. Session 2: Na, K, Al, Ti, Ca, Cr, Mn, Ni, Mg, Fe, Si. All determined. \"We used two different settings to determine the chemical compositions of minerals: (1) Al, Ti, Ca, Cr, Mn, Ni, Mg, Fe and Si (session 1) and (2) Na, K, Al, Ti, Ca, Cr, Mn, Ni, Mg, Fe and Si (session 2)\" (p.11)"
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Centre de Recherches P\u00e9trographiques et G\u00e9ochimiques (CRPG), Nancy, France"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Barnes et al. 2025, Nat. Astron.; doi:10.1038/s41550-025-02631-6"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM-BSE (JEOL JSM-6510, 15 kV, 3 nA); SEM-EDS (multi-element mapping); SIMS (CAMECA IMS 1270 E7, CRPG); NanoSIMS (K-ALFAA); ICP-MS; MC-ICP-MS; noble gas MS"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Aggregate particles (<1 mm) mounted in epoxy at Universit\u00e9 C\u00f4te d'Azur; polished; carbon coated (thickness N)",
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 1
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
        "schema:position": 2,
        "ada:detectionLimitMethod": "missing"
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "ada:primaryStandardNameDefault": "Springwater olivine (Mg, Si); fayalite (Fe); wollastonite (Ca); albite (Na, Al); orthoclase (K); rutile (Ti); Ni metal (Ni); chromite (Cr); rhodochrosite (Mn)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "empa",
      "schema:termCode": "empa"
    }
  ],
  "ada:edsAcquisitionMode": "missing",
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
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

ex:empaTAPP-P12 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ;
                    ada:detectionLimitMethod "missing" ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Aggregate particles (<1 mm) mounted in epoxy at Université Côte d'Azur; polished; carbon coated (thickness N)" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/empaTAPP/beamRasterDimensionsDefault> ;
    schema1:datePublished "missing" ;
    schema1:description "Barnes et al. 2025, Nat. Astron. — variety and origin of accreted materials in Bennu. Protocol 1 of 2: CRPG Nancy, JEOL JXA-8230. Instrument has 5 WDS spectrometers + 1 SDD EDS; per-analyte technique (WDS vs. EDS) not stated. Two analytical sessions: session 1 (no Na, K); session 2 (with Na, K). Counting times are stated as total peak + background combined: 200 ms for minor elements (Al, Ti, Ca, Mn, Cr) and 20 ms for major elements (Mg, Fe, Si) — unusually short, possibly per-pixel for fast mapping mode. Full primary standard suite stated with element assignments. Full per-element detection limits stated. Matrix correction method not stated. Sample preparation done at Université Côte d'Azur (not at CRPG). Beam current not stated for NHM protocol; 3 nA mentioned in text is for SEM-EDS (different instrument)." ;
    schema1:instrument <https://example.org/instrument/EPMA>,
        <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Centre de Recherches Pétrographiques et Géochimiques (CRPG), Nancy, France" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "empa" ;
            schema1:termCode "empa" ] ;
    schema1:name "EPMA Major Element Silicates/Oxides/Carbonates, Bennu Anhydrous Minerals (CRPG Nancy, JEOL JXA-8230)" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Silicate mineral (olivine, pyroxene) | Oxide | Carbonate (anhydrous minerals in Bennu aggregate particles)" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Barnes et al. 2025, Nat. Astron.; doi:10.1038/s41550-025-02631-6" ] ;
            schema1:url "https://ada.astromat.org/missing" ],
        [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "SEM-BSE (JEOL JSM-6510, 15 kV, 3 nA); SEM-EDS (multi-element mapping); SIMS (CAMECA IMS 1270 E7, CRPG); NanoSIMS (K-ALFAA); ICP-MS; MC-ICP-MS; noble gas MS" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:edsAcquisitionMode "missing" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:monitoredEleemnts "Session 1: Al, Ti, Ca, Cr, Mn, Ni, Mg, Fe, Si. Session 2: Na, K, Al, Ti, Ca, Cr, Mn, Ni, Mg, Fe, Si. All determined. \"We used two different settings to determine the chemical compositions of minerals: (1) Al, Ti, Ca, Cr, Mn, Ni, Mg, Fe and Si (session 1) and (2) Na, K, Al, Ti, Ca, Cr, Mn, Ni, Mg, Fe and Si (session 2)\" (p.11)" ;
    ada:primaryStandardNameDefault "Springwater olivine (Mg, Si); fayalite (Fe); wollastonite (Ca); albite (Na, Al); orthoclase (K); rutile (Ti); Ni metal (Ni); chromite (Cr); rhodochrosite (Mn)" ;
    ada:samplingUnit "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:wdsDeadTimeCorrection "missing" .

<https://ada.astromat.org/metadata/parameter/empaTAPP/beamRasterDimensionsDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 5 ;
    schema1:description "5×5 µm² for carbonates" ;
    schema1:name "Beam Raster Dimensions" ;
    schema1:valueName "beamRasterDimensionsDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://example.org/instrument/EPMA> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EPMA" ;
    schema1:hasPart <https://example.org/instrument/EPMA/part/EDS-Detector>,
        <https://example.org/instrument/EPMA/part/Electron-Source>,
        <https://example.org/instrument/EPMA/part/WDS-Spectrometer> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "JEOL" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "20 kV" ;
    ada:beamDiameterDefault "1 µm (point analysis); 5×5 µm² raster area for carbonates" ;
    ada:beamMode "Focused (1 µm, point analysis); Rastered 5×5 µm² for carbonates" .

<https://example.org/instrument/EPMA/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/EPMA/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "missing" ;
    schema1:name "missing" .

<https://example.org/instrument/EPMA/part/WDS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "WDS Spectrometer" ;
    schema1:name "5 wavelength-dispersive spectrometers (JEOL)" .

<https://example.org/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "JXA-8230 (stated as \"JEOL JXA-8230 electron microprobe analyser (EPMA)\")" ] ;
    schema1:name "example instrumentName" .


```


### empaTAPP example P13
empaTAPP instance derived from Barnes+2025 | Cameca SX100 | WDS Point Analysis (NHM London).
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
  "@id": "ex:empaTAPP-P13",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA Major/Minor Element Anhydrous Silicates, Bennu (NHM London, Cameca SX100)",
  "schema:description": "Barnes et al. 2025, Nat. Astron. — variety and origin of accreted materials in Bennu. Protocol 2 of 2: NHM London, CAMECA SX100. Stated instrument: \"CAMECA SX100 electron microprobe\". Target minerals: olivine and pyroxene (anhydrous silicates). 20 kV, 1 µm focused beam. Beam current not stated for EPMA (3 nA in text refers to SEM-EDS on separate Zeiss EVO instrument). Detection limits ~250 ppm for transition metals. Standards, matrix correction, WDS spectrometer details not stated. Analyte list not explicitly given; implied Si, Mg, Fe, Ca, Mn, Cr, Ni, Al, Ti from context. SEM-EDS at NHM is a separate instrument (Zeiss EVO 15LS + Oxford X-Max80) calibrated at 20 kV, 3 nA. Carbon coat: initial coat for SEM/EPMA (thickness N); additional coat to ~30 nm total was for subsequent SIMS, not EPMA.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "20 kV",
      "ada:beamDiameterDefault": "1 µm (focused)",
      "ada:beamMode": "Focused (1 µm)",
      "schema:manufacturer": {
        "schema:name": "Cameca",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        }
      ],
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "SX100 (stated as \"CAMECA SX100 electron microprobe\")",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Silicate mineral (olivine, pyroxene) in Bennu aggregate particles"
          ]
        }
      ]
    }
  ],
  "ada:monitoredEleemnts": [
    "N — the paper gives beam conditions and a detection limit for transition metals of about 250 ppm for the NHM London instrument (p.13) but names no element"
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Natural History Museum (NHM), London, UK"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Barnes et al. 2025, Nat. Astron.; doi:10.1038/s41550-025-02631-6"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM-EDS (Zeiss EVO 15LS + Oxford X-Max80, 20 kV, 3 nA); NanoSIMS (OU); SIMS (CAMECA ims-1280-HR, Hokkaido); laser fluorination O isotopes (OU)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Mounted in resin blocks; polished at NHM London; fragmented during polishing (P1, P2); initial carbon coat for SEM/EPMA (thickness N); additional coat added after for SIMS (total ~30 nm)",
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 1
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
        "schema:position": 2,
        "ada:detectionLimitMethod": "missing"
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "empa",
      "schema:termCode": "empa"
    }
  ],
  "ada:edsAcquisitionMode": "missing",
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:primaryStandardNameDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EMPA/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:empaTAPP-P13",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA Major/Minor Element Anhydrous Silicates, Bennu (NHM London, Cameca SX100)",
  "schema:description": "Barnes et al. 2025, Nat. Astron. \u2014 variety and origin of accreted materials in Bennu. Protocol 2 of 2: NHM London, CAMECA SX100. Stated instrument: \"CAMECA SX100 electron microprobe\". Target minerals: olivine and pyroxene (anhydrous silicates). 20 kV, 1 \u00b5m focused beam. Beam current not stated for EPMA (3 nA in text refers to SEM-EDS on separate Zeiss EVO instrument). Detection limits ~250 ppm for transition metals. Standards, matrix correction, WDS spectrometer details not stated. Analyte list not explicitly given; implied Si, Mg, Fe, Ca, Mn, Cr, Ni, Al, Ti from context. SEM-EDS at NHM is a separate instrument (Zeiss EVO 15LS + Oxford X-Max80) calibrated at 20 kV, 3 nA. Carbon coat: initial coat for SEM/EPMA (thickness N); additional coat to ~30 nm total was for subsequent SIMS, not EPMA.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "20 kV",
      "ada:beamDiameterDefault": "1 \u00b5m (focused)",
      "ada:beamMode": "Focused (1 \u00b5m)",
      "schema:manufacturer": {
        "schema:name": "Cameca",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        }
      ],
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "SX100 (stated as \"CAMECA SX100 electron microprobe\")",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Silicate mineral (olivine, pyroxene) in Bennu aggregate particles"
          ]
        }
      ]
    }
  ],
  "ada:monitoredEleemnts": [
    "N \u2014 the paper gives beam conditions and a detection limit for transition metals of about 250 ppm for the NHM London instrument (p.13) but names no element"
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Natural History Museum (NHM), London, UK"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Barnes et al. 2025, Nat. Astron.; doi:10.1038/s41550-025-02631-6"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM-EDS (Zeiss EVO 15LS + Oxford X-Max80, 20 kV, 3 nA); NanoSIMS (OU); SIMS (CAMECA ims-1280-HR, Hokkaido); laser fluorination O isotopes (OU)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Mounted in resin blocks; polished at NHM London; fragmented during polishing (P1, P2); initial carbon coat for SEM/EPMA (thickness N); additional coat added after for SIMS (total ~30 nm)",
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 1
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
        "schema:position": 2,
        "ada:detectionLimitMethod": "missing"
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "empa",
      "schema:termCode": "empa"
    }
  ],
  "ada:edsAcquisitionMode": "missing",
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:primaryStandardNameDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
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

ex:empaTAPP-P13 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ;
                    ada:detectionLimitMethod "missing" ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Mounted in resin blocks; polished at NHM London; fragmented during polishing (P1, P2); initial carbon coat for SEM/EPMA (thickness N); additional coat added after for SIMS (total ~30 nm)" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "Barnes et al. 2025, Nat. Astron. — variety and origin of accreted materials in Bennu. Protocol 2 of 2: NHM London, CAMECA SX100. Stated instrument: \"CAMECA SX100 electron microprobe\". Target minerals: olivine and pyroxene (anhydrous silicates). 20 kV, 1 µm focused beam. Beam current not stated for EPMA (3 nA in text refers to SEM-EDS on separate Zeiss EVO instrument). Detection limits ~250 ppm for transition metals. Standards, matrix correction, WDS spectrometer details not stated. Analyte list not explicitly given; implied Si, Mg, Fe, Ca, Mn, Cr, Ni, Al, Ti from context. SEM-EDS at NHM is a separate instrument (Zeiss EVO 15LS + Oxford X-Max80) calibrated at 20 kV, 3 nA. Carbon coat: initial coat for SEM/EPMA (thickness N); additional coat to ~30 nm total was for subsequent SIMS, not EPMA." ;
    schema1:instrument <https://example.org/instrument/EPMA>,
        <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Natural History Museum (NHM), London, UK" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "empa" ;
            schema1:termCode "empa" ] ;
    schema1:name "EPMA Major/Minor Element Anhydrous Silicates, Bennu (NHM London, Cameca SX100)" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Silicate mineral (olivine, pyroxene) in Bennu aggregate particles" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Barnes et al. 2025, Nat. Astron.; doi:10.1038/s41550-025-02631-6" ] ;
            schema1:url "https://ada.astromat.org/missing" ],
        [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "SEM-EDS (Zeiss EVO 15LS + Oxford X-Max80, 20 kV, 3 nA); NanoSIMS (OU); SIMS (CAMECA ims-1280-HR, Hokkaido); laser fluorination O isotopes (OU)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:edsAcquisitionMode "missing" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:monitoredEleemnts "N — the paper gives beam conditions and a detection limit for transition metals of about 250 ppm for the NHM London instrument (p.13) but names no element" ;
    ada:primaryStandardNameDefault "missing" ;
    ada:samplingUnit "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:wdsDeadTimeCorrection "missing" .

<https://example.org/instrument/EPMA> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EPMA" ;
    schema1:hasPart <https://example.org/instrument/EPMA/part/EDS-Detector>,
        <https://example.org/instrument/EPMA/part/Electron-Source>,
        <https://example.org/instrument/EPMA/part/WDS-Spectrometer> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Cameca" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "20 kV" ;
    ada:beamDiameterDefault "1 µm (focused)" ;
    ada:beamMode "Focused (1 µm)" .

<https://example.org/instrument/EPMA/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/EPMA/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "missing" ;
    schema1:name "missing" .

<https://example.org/instrument/EPMA/part/WDS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "WDS Spectrometer" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "SX100 (stated as \"CAMECA SX100 electron microprobe\")" ] ;
    schema1:name "example instrumentName" .


```


### empaTAPP example P14
empaTAPP instance derived from Neuman+2025 | WashU St. Louis | WDS Mapping (JEOL JXA-8200).
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
  "@id": "ex:empaTAPP-P14",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS quantitative compositional mapping, Apollo 17 core 73001 continuous thin sections (Washington University in St. Louis)",
  "schema:description": "Multi-pass WDS mapping: two passes per stage map, five elements each; 18 hr per map; 20 x 10^6 fully quantitative analyses across all slides. Recorded in the acquisition-pass proposal (2026-09-08) as the evidence that EPMA partitions the target-species domain across passes. Reported detail: ada:matrixCorrectionMethod = Full Phi(rho-z) correction applied at each pixel, of the form C = k x ZAF, where ZAF is the compositionally dependent correction for atomic number, X-ray absorption and characteristic fluorescence in both sample and standard.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV (stage maps and BSE mosaic)",
      "ada:beamDiameterDefault": "10 um (fixed)",
      "ada:beamMode": "Fixed 10 um beam (stated 'a fixed 10 um electron beam')",
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "N/A - WDS mapping; no EDS used for the EPMA work",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/EPMA/part/EDS-Detector",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "Fixed wavelength-dispersive spectrometers; count not stated (five elements collected per pass)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "JEOL JXA-8200",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/empaTAPP/beamRasterDimensionsDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "beamRasterDimensionsDefault",
      "schema:name": "Beam Raster Dimensions",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N/A - stage scan, not beam scan"
    },
    {
      "@id": "ada:parameter/empaTAPP/stageScanVsBeamScan",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/empaTAPP/stageScanVsBeamScan"
        }
      ],
      "schema:name": "Stage Scan vs. Beam Scan",
      "schema:value": "Stage scan (stated 'EPMA stage maps')"
    }
  ],
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "preAnalysisImagingAndScreeningDefault",
          "schema:name": "Pre-Analysis Imaging and Screening",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "BSE mosaic: approximately 325 backscattered-electron images collected with the JEOL guide-net mapping software at 15 kV, 2 nA probe current and 70x magnification, stitched with the ImageJ Fiji grid-collection stitching plug-in (Donovan et al., 2021) into a 20k x 5k pixel mosaic at ~1.5 um pixel resolution"
        },
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Lunar regolith (Apollo 17 double drive tube, lower section 73001), as continuous thin sections"
          ]
        }
      ]
    }
  ],
  "ada:matrixCorrectionMethod": "ZAF",
  "ada:stepSizePixelSizeDefault": "9.5 um (stage maps); ~1.5 um per pixel (BSE mosaic)",
  "ada:channelTemplate": {
    "ada:defaultChannels": [
      "N - spectrometer-to-element assignments not stated"
    ],
    "ada:channelColumns": [
      {
        "schema:valueName": "channel",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "example instrumentName"
      },
      {
        "@id": "ada:channelColumn/empaTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCountingTime",
        "schema:name": "Background Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/empaTAPP/backgroundPosition",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundPosition",
        "schema:name": "Background Position(s)",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:channelColumn/empaTAPP/diffractingCrystal",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "diffractingCrystal",
        "schema:name": "Diffracting Crystal",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/empaTAPP/dwellTimePerPixel",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerPixel",
        "schema:name": "Dwell Time per Pixel",
        "ada:dataType": "number",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/empaTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "peakCountingTime",
        "schema:name": "Peak Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/empaTAPP/proportionalCounterDetector",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "proportionalCounterDetector",
        "schema:name": "Proportional Counter / Detector",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:channelColumn/empaTAPP/sequence",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "sequence",
        "schema:name": "Sequence",
        "ada:dataType": "integer"
      },
      {
        "@id": "ada:channelColumn/empaTAPP/wdsPhaSetting",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "wdsPhaSetting",
        "schema:name": "WDS PHA Setting",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:channelColumn/empaTAPP/xRayLine",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayLine",
        "schema:name": "X-ray Line",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "ada:samplingUnitSelectionCriteriaDefault": "N - continuous thin sections of the whole core; five stage maps per section, no selection rule stated",
  "ada:monitoredEleemnts": [
    "Pass 1: Mg, Al, Fe, Ca, Ti. Pass 2: Na, Si, Mn, K, Cr. All determined. \"Two passes were used to collect X-ray intensities for Mg, Al, Fe, Ca, and Ti in pass 1, and Na, Si, Mn, K, and Cr in pass 2\" (p.6)"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "EPMA-WDS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Washington University in St. Louis"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Neuman et al. 2025, J. Geophys. Res. Planets 130, e2024JE008556; doi:10.1029/2024JE008556 (section 2.6)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "BSE mosaic imaging (same JEOL JXA-8200); QEMSCAN (FEI QUANTA 650 FEG-SEM, Univ. Manchester); optical microscopy (Keyence VHX 7000, NASA JSC); micro-XCT (custom NSI instrument, UTCT)",
        "schema:description": "Single-element and RGB composite X-ray maps are compared with BSE and optical image mosaics (reflected light, plane polarized, crossed polars) to discriminate crystalline from glassy phases; an Al-Mg-Fe RGB composite X-ray map is used to discriminate feldspathic (red) from ferromagnesian (green and blue) phases"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnit": "Analysis point - each map pixel is a fully quantitative analysis (1,024 x 1,024 per stage map; five stage maps per thin section; 20 x 10^6 analyses across all slides)",
  "bios:computationalTool": [
    {
      "ada:toolRole": "acquisition",
      "schema:name": "JEOL guide-net mapping software (BSE mosaic); N for the WDS stage maps"
    },
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Probe Software CalcImage and Probe for EPMA (full Phi(rho-z) correction at each pixel); MATLAB routines generating 32-bit floating point .tiff quantitative maps; Fiji and MATLAB for stitching; ENVI input image stacks"
    }
  ],
  "ada:analyticalMode": [
    "WDS Mapping"
  ],
  "ada:reportedProperties": [
    "Quantitative element and oxide wt.% maps; cation stoichiometry; derived mineral endmember maps (32-bit floating point .tiff)"
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Core extruded and dissected in 0.5 cm depth intervals; the remaining material impregnated with epoxy to create a continuous thin section set of the entire core; sections are 50 x 25 mm. Carbon coating N",
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 1
      },
      {
        "schema:name": "Data reduction",
        "ada:detectionLimitMethod": "N - attributed to the MAN background correction dedicating all map collection time to on-peak measurement, 'which improves precision and detection limits'",
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "ada:primaryStandardNameDefault": "N - 'EPMA standards having a range of average atomic number Z' are used for the MAN background calibration; individual standards not named",
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:edsAcquisitionMode": "missing",
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:wdsDeadTimeCorrection": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EMPA/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:empaTAPP-P14",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS quantitative compositional mapping, Apollo 17 core 73001 continuous thin sections (Washington University in St. Louis)",
  "schema:description": "Multi-pass WDS mapping: two passes per stage map, five elements each; 18 hr per map; 20 x 10^6 fully quantitative analyses across all slides. Recorded in the acquisition-pass proposal (2026-09-08) as the evidence that EPMA partitions the target-species domain across passes. Reported detail: ada:matrixCorrectionMethod = Full Phi(rho-z) correction applied at each pixel, of the form C = k x ZAF, where ZAF is the compositionally dependent correction for atomic number, X-ray absorption and characteristic fluorescence in both sample and standard.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV (stage maps and BSE mosaic)",
      "ada:beamDiameterDefault": "10 um (fixed)",
      "ada:beamMode": "Fixed 10 um beam (stated 'a fixed 10 um electron beam')",
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "N/A - WDS mapping; no EDS used for the EPMA work",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/EPMA/part/EDS-Detector",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "Fixed wavelength-dispersive spectrometers; count not stated (five elements collected per pass)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "JEOL JXA-8200",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/empaTAPP/beamRasterDimensionsDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "beamRasterDimensionsDefault",
      "schema:name": "Beam Raster Dimensions",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N/A - stage scan, not beam scan"
    },
    {
      "@id": "ada:parameter/empaTAPP/stageScanVsBeamScan",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/empaTAPP/stageScanVsBeamScan"
        }
      ],
      "schema:name": "Stage Scan vs. Beam Scan",
      "schema:value": "Stage scan (stated 'EPMA stage maps')"
    }
  ],
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "preAnalysisImagingAndScreeningDefault",
          "schema:name": "Pre-Analysis Imaging and Screening",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "BSE mosaic: approximately 325 backscattered-electron images collected with the JEOL guide-net mapping software at 15 kV, 2 nA probe current and 70x magnification, stitched with the ImageJ Fiji grid-collection stitching plug-in (Donovan et al., 2021) into a 20k x 5k pixel mosaic at ~1.5 um pixel resolution"
        },
        {
          "schema:name": "Target Material",
          "schema:value": [
            "Lunar regolith (Apollo 17 double drive tube, lower section 73001), as continuous thin sections"
          ]
        }
      ]
    }
  ],
  "ada:matrixCorrectionMethod": "ZAF",
  "ada:stepSizePixelSizeDefault": "9.5 um (stage maps); ~1.5 um per pixel (BSE mosaic)",
  "ada:channelTemplate": {
    "ada:defaultChannels": [
      "N - spectrometer-to-element assignments not stated"
    ],
    "ada:channelColumns": [
      {
        "schema:valueName": "channel",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:name": "example instrumentName"
      },
      {
        "@id": "ada:channelColumn/empaTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCountingTime",
        "schema:name": "Background Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/empaTAPP/backgroundPosition",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundPosition",
        "schema:name": "Background Position(s)",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:channelColumn/empaTAPP/diffractingCrystal",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "diffractingCrystal",
        "schema:name": "Diffracting Crystal",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/empaTAPP/dwellTimePerPixel",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerPixel",
        "schema:name": "Dwell Time per Pixel",
        "ada:dataType": "number",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/empaTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "peakCountingTime",
        "schema:name": "Peak Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:channelColumn/empaTAPP/proportionalCounterDetector",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "proportionalCounterDetector",
        "schema:name": "Proportional Counter / Detector",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:channelColumn/empaTAPP/sequence",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "sequence",
        "schema:name": "Sequence",
        "ada:dataType": "integer"
      },
      {
        "@id": "ada:channelColumn/empaTAPP/wdsPhaSetting",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "wdsPhaSetting",
        "schema:name": "WDS PHA Setting",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:channelColumn/empaTAPP/xRayLine",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayLine",
        "schema:name": "X-ray Line",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "ada:samplingUnitSelectionCriteriaDefault": "N - continuous thin sections of the whole core; five stage maps per section, no selection rule stated",
  "ada:monitoredEleemnts": [
    "Pass 1: Mg, Al, Fe, Ca, Ti. Pass 2: Na, Si, Mn, K, Cr. All determined. \"Two passes were used to collect X-ray intensities for Mg, Al, Fe, Ca, and Ti in pass 1, and Na, Si, Mn, K, and Cr in pass 2\" (p.6)"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "EPMA-WDS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Washington University in St. Louis"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Neuman et al. 2025, J. Geophys. Res. Planets 130, e2024JE008556; doi:10.1029/2024JE008556 (section 2.6)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "BSE mosaic imaging (same JEOL JXA-8200); QEMSCAN (FEI QUANTA 650 FEG-SEM, Univ. Manchester); optical microscopy (Keyence VHX 7000, NASA JSC); micro-XCT (custom NSI instrument, UTCT)",
        "schema:description": "Single-element and RGB composite X-ray maps are compared with BSE and optical image mosaics (reflected light, plane polarized, crossed polars) to discriminate crystalline from glassy phases; an Al-Mg-Fe RGB composite X-ray map is used to discriminate feldspathic (red) from ferromagnesian (green and blue) phases"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnit": "Analysis point - each map pixel is a fully quantitative analysis (1,024 x 1,024 per stage map; five stage maps per thin section; 20 x 10^6 analyses across all slides)",
  "bios:computationalTool": [
    {
      "ada:toolRole": "acquisition",
      "schema:name": "JEOL guide-net mapping software (BSE mosaic); N for the WDS stage maps"
    },
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Probe Software CalcImage and Probe for EPMA (full Phi(rho-z) correction at each pixel); MATLAB routines generating 32-bit floating point .tiff quantitative maps; Fiji and MATLAB for stitching; ENVI input image stacks"
    }
  ],
  "ada:analyticalMode": [
    "WDS Mapping"
  ],
  "ada:reportedProperties": [
    "Quantitative element and oxide wt.% maps; cation stoichiometry; derived mineral endmember maps (32-bit floating point .tiff)"
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Core extruded and dissected in 0.5 cm depth intervals; the remaining material impregnated with epoxy to create a continuous thin section set of the entire core; sections are 50 x 25 mm. Carbon coating N",
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 1
      },
      {
        "schema:name": "Data reduction",
        "ada:detectionLimitMethod": "N - attributed to the MAN background correction dedicating all map collection time to on-peak measurement, 'which improves precision and detection limits'",
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "ada:primaryStandardNameDefault": "N - 'EPMA standards having a range of average atomic number Z' are used for the MAN background calibration; individual standards not named",
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:edsAcquisitionMode": "missing",
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:wdsDeadTimeCorrection": "missing",
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

ex:empaTAPP-P14 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ;
                    ada:detectionLimitMethod "N - attributed to the MAN background correction dedicating all map collection time to on-peak measurement, 'which improves precision and detection limits'" ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Core extruded and dissected in 0.5 cm depth intervals; the remaining material impregnated with epoxy to create a continuous thin section set of the entire core; sections are 50 x 25 mm. Carbon coating N" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/empaTAPP/beamRasterDimensionsDefault>,
        <https://ada.astromat.org/metadata/parameter/empaTAPP/stageScanVsBeamScan> ;
    schema1:datePublished "missing" ;
    schema1:description "Multi-pass WDS mapping: two passes per stage map, five elements each; 18 hr per map; 20 x 10^6 fully quantitative analyses across all slides. Recorded in the acquisition-pass proposal (2026-09-08) as the evidence that EPMA partitions the target-species domain across passes. Reported detail: ada:matrixCorrectionMethod = Full Phi(rho-z) correction applied at each pixel, of the form C = k x ZAF, where ZAF is the compositionally dependent correction for atomic number, X-ray absorption and characteristic fluorescence in both sample and standard." ;
    schema1:instrument <https://example.org/instrument/EPMA>,
        <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Washington University in St. Louis" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "EPMA-WDS" ] ;
    schema1:name "EPMA-WDS quantitative compositional mapping, Apollo 17 core 73001 continuous thin sections (Washington University in St. Louis)" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Lunar regolith (Apollo 17 double drive tube, lower section 73001), as continuous thin sections" ],
                <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "Single-element and RGB composite X-ray maps are compared with BSE and optical image mosaics (reflected light, plane polarized, crossed polars) to discriminate crystalline from glassy phases; an Al-Mg-Fe RGB composite X-ray map is used to discriminate feldspathic (red) from ferromagnesian (green and blue) phases" ;
                    schema1:name "BSE mosaic imaging (same JEOL JXA-8200); QEMSCAN (FEI QUANTA 650 FEG-SEM, Univ. Manchester); optical microscopy (Keyence VHX 7000, NASA JSC); micro-XCT (custom NSI instrument, UTCT)" ] ;
            schema1:url "https://ada.astromat.org/missing" ],
        [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Neuman et al. 2025, J. Geophys. Res. Planets 130, e2024JE008556; doi:10.1029/2024JE008556 (section 2.6)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    schema1:variableMeasured [ schema1:defaultValue "missing" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analyticalMode "WDS Mapping" ;
    ada:channelTemplate [ ada:channelColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "channel" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/channelColumn/empaTAPP/backgroundCountingTime>,
                <https://ada.astromat.org/metadata/channelColumn/empaTAPP/backgroundPosition>,
                <https://ada.astromat.org/metadata/channelColumn/empaTAPP/diffractingCrystal>,
                <https://ada.astromat.org/metadata/channelColumn/empaTAPP/dwellTimePerPixel>,
                <https://ada.astromat.org/metadata/channelColumn/empaTAPP/peakCountingTime>,
                <https://ada.astromat.org/metadata/channelColumn/empaTAPP/proportionalCounterDetector>,
                <https://ada.astromat.org/metadata/channelColumn/empaTAPP/sequence>,
                <https://ada.astromat.org/metadata/channelColumn/empaTAPP/wdsPhaSetting>,
                <https://ada.astromat.org/metadata/channelColumn/empaTAPP/xRayLine> ;
            ada:defaultChannels "N - spectrometer-to-element assignments not stated" ] ;
    ada:edsAcquisitionMode "missing" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "ZAF" ;
    ada:monitoredEleemnts "Pass 1: Mg, Al, Fe, Ca, Ti. Pass 2: Na, Si, Mn, K, Cr. All determined. \"Two passes were used to collect X-ray intensities for Mg, Al, Fe, Ca, and Ti in pass 1, and Na, Si, Mn, K, and Cr in pass 2\" (p.6)" ;
    ada:primaryStandardNameDefault "N - 'EPMA standards having a range of average atomic number Z' are used for the MAN background calibration; individual standards not named" ;
    ada:reportedProperties "Quantitative element and oxide wt.% maps; cation stoichiometry; derived mineral endmember maps (32-bit floating point .tiff)" ;
    ada:samplingUnit "Analysis point - each map pixel is a fully quantitative analysis (1,024 x 1,024 per stage map; five stage maps per thin section; 20 x 10^6 analyses across all slides)" ;
    ada:samplingUnitSelectionCriteriaDefault "N - continuous thin sections of the whole core; five stage maps per section, no selection rule stated" ;
    ada:stepSizePixelSizeDefault "9.5 um (stage maps); ~1.5 um per pixel (BSE mosaic)" ;
    ada:wdsDeadTimeCorrection "missing" ;
    bios:computationalTool [ schema1:name "Probe Software CalcImage and Probe for EPMA (full Phi(rho-z) correction at each pixel); MATLAB routines generating 32-bit floating point .tiff quantitative maps; Fiji and MATLAB for stitching; ENVI input image stacks" ;
            ada:toolRole "dataReduction" ],
        [ schema1:name "JEOL guide-net mapping software (BSE mosaic); N for the WDS stage maps" ;
            ada:toolRole "acquisition" ] .

<https://ada.astromat.org/metadata/channelColumn/empaTAPP/backgroundCountingTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Background Counting Time" ;
    schema1:valueName "backgroundCountingTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/channelColumn/empaTAPP/backgroundPosition> a schema1:PropertyValueSpecification ;
    schema1:name "Background Position(s)" ;
    schema1:valueName "backgroundPosition" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/empaTAPP/diffractingCrystal> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Diffracting Crystal" ;
    schema1:valueName "diffractingCrystal" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/empaTAPP/dwellTimePerPixel> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Dwell Time per Pixel" ;
    schema1:valueName "dwellTimePerPixel" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/channelColumn/empaTAPP/peakCountingTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Peak Counting Time" ;
    schema1:valueName "peakCountingTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/channelColumn/empaTAPP/proportionalCounterDetector> a schema1:PropertyValueSpecification ;
    schema1:name "Proportional Counter / Detector" ;
    schema1:valueName "proportionalCounterDetector" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/empaTAPP/sequence> a schema1:PropertyValueSpecification ;
    schema1:name "Sequence" ;
    schema1:valueName "sequence" ;
    ada:dataType "integer" .

<https://ada.astromat.org/metadata/channelColumn/empaTAPP/wdsPhaSetting> a schema1:PropertyValueSpecification ;
    schema1:name "WDS PHA Setting" ;
    schema1:valueName "wdsPhaSetting" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/channelColumn/empaTAPP/xRayLine> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "X-ray Line" ;
    schema1:valueName "xRayLine" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/empaTAPP/beamRasterDimensionsDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N/A - stage scan, not beam scan" ;
    schema1:name "Beam Raster Dimensions" ;
    schema1:valueName "beamRasterDimensionsDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "BSE mosaic: approximately 325 backscattered-electron images collected with the JEOL guide-net mapping software at 15 kV, 2 nA probe current and 70x magnification, stitched with the ImageJ Fiji grid-collection stitching plug-in (Donovan et al., 2021) into a 20k x 5k pixel mosaic at ~1.5 um pixel resolution" ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:valueName "preAnalysisImagingAndScreeningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://example.org/instrument/EPMA> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EPMA" ;
    schema1:hasPart <https://example.org/instrument/EPMA/part/EDS-Detector>,
        <https://example.org/instrument/EPMA/part/Electron-Source>,
        <https://example.org/instrument/EPMA/part/WDS-Spectrometer> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "JEOL" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "15 kV (stage maps and BSE mosaic)" ;
    ada:beamDiameterDefault "10 um (fixed)" ;
    ada:beamMode "Fixed 10 um beam (stated 'a fixed 10 um electron beam')" .

<https://example.org/instrument/EPMA/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:description "N/A - WDS mapping; no EDS used for the EPMA work" ;
    schema1:name "missing" .

<https://example.org/instrument/EPMA/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "missing" ;
    schema1:name "missing" .

<https://example.org/instrument/EPMA/part/WDS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "WDS Spectrometer" ;
    schema1:name "Fixed wavelength-dispersive spectrometers; count not stated (five elements collected per pass)" .

<https://example.org/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "JEOL JXA-8200" ] ;
    schema1:name "example instrumentName" .

<https://ada.astromat.org/metadata/parameter/empaTAPP/stageScanVsBeamScan> a schema1:PropertyValue ;
    schema1:name "Stage Scan vs. Beam Scan" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/empaTAPP/stageScanVsBeamScan> ;
    schema1:value "Stage scan (stated 'EPMA stage maps')" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: EPMA/EMPA Technique-Aligned Protocol Profile (empaTAPP)
description: Electron-probe microanalysis (EPMA/EMPA, WDS/EDS) extension of the base
  TAPP definition, generated from tapp/Current TAPPs/EPMA_TAPP_v68.csv via the path-driven
  pipeline (bootstrap_schemapaths.py + build_pathdriven.py).
allOf:
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/calibrationFactor/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/compositionQC/schema.yaml#/$defs/ProcedureIdentification
- type: object
  properties:
    schema:instrument:
      type: array
      items:
        type: object
        allOf:
        - if:
            properties:
              schema:additionalType:
                contains:
                  const: EPMA
                schema:inDefinedTermSet: ada:vocab/instrumentType
            required:
            - schema:additionalType
          then:
            properties:
              ada:acceleratingVoltageDefault:
                description: Electron beam accelerating voltage in kilovolts (kV).
                  Justify any deviation from the standard operating voltage.
                anyOf:
                - type: number
                - type: string
              ada:beamDiameterDefault:
                description: Diameter of the electron beam in micrometers. 0 indicates
                  a fully focused beam. Document defocused diameter when used to minimize
                  beam damage or improve spatial averaging for beam-sensitive phases.
                anyOf:
                - type: number
                - type: string
              ada:beamMode:
                description: Whether the electron beam was operated as a stationary
                  focused spot, defocused to a specified diameter, or rastered over
                  a small area during a single-point analysis. Must be consistent
                  with the Beam Diameter and Beam Raster Dimensions fields. For mapping,
                  beam scanning is controlled by Step Size / Pixel Size and Stage
                  Scan vs. Beam Scan instead.
                anyOf:
                - type: string
                  enum:
                  - Focused
                  - Defocused
                  - Rastered
                  - N/A
                  - None
                  - missing
                - type: string
                readOnly: true
              schema:hasPart:
                type: array
                items:
                  type: object
                  allOf:
                  - if:
                      properties:
                        schema:additionalType:
                          contains:
                            const: EDS Detector
                          schema:inDefinedTermSet: ada:vocab/instrumentComponentType
                      required:
                      - schema:additionalType
                    then:
                      properties:
                        schema:description:
                          description: EDS detector type, manufacturer, number of
                            detector elements, active area and solid angle, window
                            type, and geometry (take-off angle, position). List multiple
                            detectors separately. Record 'N/A' where the procedure
                            has no EDS detector.
                          anyOf:
                          - type: string
                            readOnly: true
                          - type: array
                            items:
                              type: string
                              readOnly: true
                  - if:
                      properties:
                        schema:additionalType:
                          contains:
                            const: Electron Source
                          schema:inDefinedTermSet: ada:vocab/instrumentComponentType
                      required:
                      - schema:additionalType
                    then:
                      properties:
                        schema:description:
                          description: Type of electron gun used in the instrument.
                          anyOf:
                          - type: string
                            enum:
                            - Cold-FEG
                            - Schottky FEG (X-FEG)
                            - Schottky FEG (standard)
                            - "Field emission gun (FEG) \u2014 subtype not specified"
                            - LaB6 / CeB6
                            - Tungsten (W)
                            - Unknown
                            - N/A
                            - None
                            - missing
                            readOnly: true
                          - type: array
                            items:
                              type: string
                              enum:
                              - Cold-FEG
                              - Schottky FEG (X-FEG)
                              - Schottky FEG (standard)
                              - "Field emission gun (FEG) \u2014 subtype not specified"
                              - LaB6 / CeB6
                              - Tungsten (W)
                              - Unknown
                              - N/A
                              - None
                              - missing
                              readOnly: true
                      required:
                      - schema:description
                  - if:
                      properties:
                        schema:additionalType:
                          contains:
                            const: WDS Spectrometer
                          schema:inDefinedTermSet: ada:vocab/instrumentComponentType
                      required:
                      - schema:additionalType
                    then:
                      properties:
                        schema:name:
                          description: Number, type, and crystal range of WDS spectrometers
                            on the instrument. Include manufacturer, model, and crystal
                            range. For SEM-WDS configurations (third-party WDS on
                            a non-EPMA platform), include WDS manufacturer and model.
                          anyOf:
                          - type: string
                            readOnly: true
                          - type: array
                            items:
                              type: string
                              readOnly: true
                allOf:
                - contains:
                    properties:
                      schema:additionalType:
                        contains:
                          const: Electron Source
                        schema:inDefinedTermSet: ada:vocab/instrumentComponentType
                    required:
                    - schema:additionalType
              schema:manufacturer:
                type: object
                properties:
                  schema:name:
                    description: Manufacturer of the instrument that performs the
                      measurement, recorded as a controlled value. Where a procedure
                      couples a sample-introduction system to an analysing instrument,
                      this records the analysing instrument. Instrument Model gives
                      the specific designation.
                    type: string
                    enum:
                    - JEOL
                    - Cameca
                    - Unknown
                    - N/A
                    - None
                    - missing
                    readOnly: true
                required:
                - schema:name
            required:
            - ada:acceleratingVoltageDefault
            - ada:beamDiameterDefault
            - ada:beamMode
            - schema:manufacturer
        - if:
            properties:
              schema:additionalType:
                contains:
                  const: SEM
                schema:inDefinedTermSet: ada:vocab/instrumentType
            required:
            - schema:additionalType
          then:
            properties:
              schema:model:
                type: object
                properties:
                  schema:name:
                    description: Model designation of the instrument that performs
                      the measurement, including any generation or configuration suffix.
                      Conventionally written with the manufacturer name included;
                      Instrument Manufacturer records the vendor separately, as a
                      controlled value, so that procedures remain findable by vendor.
                    type: string
                    readOnly: true
                required:
                - schema:name
            required:
            - schema:model
      allOf:
      - contains:
          properties:
            schema:additionalType:
              contains:
                const: EPMA
              schema:inDefinedTermSet: ada:vocab/instrumentType
          required:
          - schema:additionalType
      - contains:
          properties:
            schema:additionalType:
              contains:
                const: SEM
              schema:inDefinedTermSet: ada:vocab/instrumentType
          required:
          - schema:additionalType
    ada:analyteTemplate:
      type: object
      properties:
        ada:analyteColumns:
          type: array
          items:
            anyOf:
            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/AnalyteIdentifierColumn
            - title: Target Species Estimation Method
              description: Whether elemental concentrations were calculated directly
                from measured X-ray intensities, or estimated by cation stoichiometry
                (e.g., oxygen calculated from cation proportions in silicates; carbon
                from stoichiometry in carbonates).
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/empaTAPP/targetSpeciesEstimationMethod
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: targetSpeciesEstimationMethod
                schema:name:
                  const: Target Species Estimation Method
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: true
                ada:tier:
                  const: R
                schema:defaultValue:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
            - title: Analytical Accuracy
              description: Offset between measured and accepted reference values for
                secondary standards, expressed as percent relative bias. Include reference
                material, reference value source, and the measured value.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/empaTAPP/analyticalAccuracy
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: analyticalAccuracy
                schema:name:
                  const: Analytical Accuracy
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: false
                ada:tier:
                  const: R
                schema:defaultValue:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
            - title: Analytical Precision
              description: Reproducibility of repeated measurements on the same or
                equivalent reference material, expressed as 1-sigma relative standard
                deviation (%). Include reference material name, number of analyses
                (n), and the measured value.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/empaTAPP/analyticalPrecision
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: analyticalPrecision
                schema:name:
                  const: Analytical Precision
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: false
                ada:tier:
                  const: R
                schema:defaultValue:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
            - title: X-ray Background Correction Method
              description: 'Method used to estimate and subtract background X-ray
                intensity beneath the peak. For WDS: typically 2-point off-peak linear
                interpolation or Mean Atomic Number (MAN) background model. For EDS:
                spectral background fitting or top-hat filter applied during spectral
                processing.'
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/empaTAPP/xRayBackgroundCorrectionMethod
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: xRayBackgroundCorrectionMethod
                schema:name:
                  const: X-ray Background Correction Method
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: false
                ada:tier:
                  const: M
                schema:defaultValue:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
              - schema:defaultValue
            - title: Beam Current
              description: Probe current in nanoamperes (nA). Often varies by phase
                type or target species; record the procedure-standard value(s).
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/empaTAPP/beamCurrent
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: beamCurrent
                schema:name:
                  const: Beam Current
                ada:dataType:
                  const: number
                schema:readonlyValue:
                  const: false
                ada:tier:
                  const: M
                schema:defaultValue:
                  anyOf:
                  - type: number
                  - type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
              - schema:defaultValue
            - title: Blank Correction
              description: Method and reference material(s) used to determine and
                subtract blank signal contributions (e.g., carbon coat contribution
                to C signal, or background contamination for trace elements).
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/empaTAPP/blankCorrection
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: blankCorrection
                schema:name:
                  const: Blank Correction
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: false
                ada:tier:
                  const: R
                schema:defaultValue:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
            - title: Counting Statistics Error
              description: "Uncertainty predicted from counting statistics \u2014
                the theoretical limit set by the Poisson distribution of the counts
                accumulated \u2014 for each reported quantity per analysis, with the
                sigma level stated. Derived from the counts on the target species
                together with those on any background or blank subtracted from it.
                Distinct from the scatter actually observed within a measurement or
                between repeated measurements, which is recorded separately."
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/empaTAPP/countingStatisticsError
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: countingStatisticsError
                schema:name:
                  const: Counting Statistics Error
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: false
                ada:tier:
                  const: R
                schema:defaultValue:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
            - title: EPMA Technique per Target Species
              description: Whether the measurement was made by WDS or EDS. Applies
                where a procedure uses both WDS and EDS.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/empaTAPP/epmaTechniquePerTargetSpecies
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: epmaTechniquePerTargetSpecies
                schema:name:
                  const: EPMA Technique per Target Species
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: true
                ada:tier:
                  const: M
                schema:defaultValue:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
              - schema:defaultValue
            - title: Interference Correction Standard
              description: Reference material used to quantify and calibrate the interference
                correction.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/empaTAPP/interferenceCorrectionStandard
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: interferenceCorrectionStandard
                schema:name:
                  const: Interference Correction Standard
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: true
                ada:tier:
                  const: R
                schema:defaultValue:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
            - title: X-ray Line Overlap Corrections Applied
              description: Whether a spectral interference correction was applied.
                Common interferences include Ti Kb on V Ka, Cr Kb on Mn Ka, and Ba
                La on Ti Ka.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/empaTAPP/xRayLineOverlapCorrectionsApplied
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: xRayLineOverlapCorrectionsApplied
                schema:name:
                  const: X-ray Line Overlap Corrections Applied
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: true
                ada:tier:
                  const: M
                schema:defaultValue:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
              - schema:defaultValue
            - title: Interfering Elements
              description: Element(s) whose X-ray lines overlap with the measured
                peak, requiring a correction.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/empaTAPP/interferingElements
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: interferingElements
                schema:name:
                  const: Interfering Elements
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: true
                ada:tier:
                  const: R
                schema:defaultValue:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
            - title: Time-Dependent Intensity Correction
              description: Type of time-dependent intensity (TDI) correction applied
                to compensate for beam-induced volatilization or migration of sensitive
                elements (e.g., Na, K, F in glasses, feldspars, carbonates).
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/empaTAPP/timeDependentIntensityCorrection
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: timeDependentIntensityCorrection
                schema:name:
                  const: Time-Dependent Intensity Correction
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: false
                ada:tier:
                  const: R
                schema:defaultValue:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
          allOf:
          - contains:
              title: Target Species Estimation Method
              description: Whether elemental concentrations were calculated directly
                from measured X-ray intensities, or estimated by cation stoichiometry
                (e.g., oxygen calculated from cation proportions in silicates; carbon
                from stoichiometry in carbonates).
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/empaTAPP/targetSpeciesEstimationMethod
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: targetSpeciesEstimationMethod
                schema:name:
                  const: Target Species Estimation Method
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: true
                ada:tier:
                  const: R
                schema:defaultValue:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
            minContains: 0
            maxContains: 1
          - contains:
              title: Analytical Accuracy
              description: Offset between measured and accepted reference values for
                secondary standards, expressed as percent relative bias. Include reference
                material, reference value source, and the measured value.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/empaTAPP/analyticalAccuracy
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: analyticalAccuracy
                schema:name:
                  const: Analytical Accuracy
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: false
                ada:tier:
                  const: R
                schema:defaultValue:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
            minContains: 0
            maxContains: 1
          - contains:
              title: Analytical Precision
              description: Reproducibility of repeated measurements on the same or
                equivalent reference material, expressed as 1-sigma relative standard
                deviation (%). Include reference material name, number of analyses
                (n), and the measured value.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/empaTAPP/analyticalPrecision
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: analyticalPrecision
                schema:name:
                  const: Analytical Precision
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: false
                ada:tier:
                  const: R
                schema:defaultValue:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
            minContains: 0
            maxContains: 1
          - contains:
              title: X-ray Background Correction Method
              description: 'Method used to estimate and subtract background X-ray
                intensity beneath the peak. For WDS: typically 2-point off-peak linear
                interpolation or Mean Atomic Number (MAN) background model. For EDS:
                spectral background fitting or top-hat filter applied during spectral
                processing.'
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/empaTAPP/xRayBackgroundCorrectionMethod
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: xRayBackgroundCorrectionMethod
                schema:name:
                  const: X-ray Background Correction Method
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: false
                ada:tier:
                  const: M
                schema:defaultValue:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
              - schema:defaultValue
            minContains: 0
            maxContains: 1
          - contains:
              title: Beam Current
              description: Probe current in nanoamperes (nA). Often varies by phase
                type or target species; record the procedure-standard value(s).
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/empaTAPP/beamCurrent
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: beamCurrent
                schema:name:
                  const: Beam Current
                ada:dataType:
                  const: number
                schema:readonlyValue:
                  const: false
                ada:tier:
                  const: M
                schema:defaultValue:
                  anyOf:
                  - type: number
                  - type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
              - schema:defaultValue
            minContains: 0
            maxContains: 1
          - contains:
              title: Blank Correction
              description: Method and reference material(s) used to determine and
                subtract blank signal contributions (e.g., carbon coat contribution
                to C signal, or background contamination for trace elements).
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/empaTAPP/blankCorrection
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: blankCorrection
                schema:name:
                  const: Blank Correction
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: false
                ada:tier:
                  const: R
                schema:defaultValue:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
            minContains: 0
            maxContains: 1
          - contains:
              title: Counting Statistics Error
              description: "Uncertainty predicted from counting statistics \u2014
                the theoretical limit set by the Poisson distribution of the counts
                accumulated \u2014 for each reported quantity per analysis, with the
                sigma level stated. Derived from the counts on the target species
                together with those on any background or blank subtracted from it.
                Distinct from the scatter actually observed within a measurement or
                between repeated measurements, which is recorded separately."
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/empaTAPP/countingStatisticsError
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: countingStatisticsError
                schema:name:
                  const: Counting Statistics Error
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: false
                ada:tier:
                  const: R
                schema:defaultValue:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
            minContains: 0
            maxContains: 1
          - contains:
              title: EPMA Technique per Target Species
              description: Whether the measurement was made by WDS or EDS. Applies
                where a procedure uses both WDS and EDS.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/empaTAPP/epmaTechniquePerTargetSpecies
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: epmaTechniquePerTargetSpecies
                schema:name:
                  const: EPMA Technique per Target Species
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: true
                ada:tier:
                  const: M
                schema:defaultValue:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
              - schema:defaultValue
            minContains: 0
            maxContains: 1
          - contains:
              title: Interference Correction Standard
              description: Reference material used to quantify and calibrate the interference
                correction.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/empaTAPP/interferenceCorrectionStandard
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: interferenceCorrectionStandard
                schema:name:
                  const: Interference Correction Standard
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: true
                ada:tier:
                  const: R
                schema:defaultValue:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
            minContains: 0
            maxContains: 1
          - contains:
              title: X-ray Line Overlap Corrections Applied
              description: Whether a spectral interference correction was applied.
                Common interferences include Ti Kb on V Ka, Cr Kb on Mn Ka, and Ba
                La on Ti Ka.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/empaTAPP/xRayLineOverlapCorrectionsApplied
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: xRayLineOverlapCorrectionsApplied
                schema:name:
                  const: X-ray Line Overlap Corrections Applied
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: true
                ada:tier:
                  const: M
                schema:defaultValue:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
              - schema:defaultValue
            minContains: 0
            maxContains: 1
          - contains:
              title: Interfering Elements
              description: Element(s) whose X-ray lines overlap with the measured
                peak, requiring a correction.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/empaTAPP/interferingElements
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: interferingElements
                schema:name:
                  const: Interfering Elements
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: true
                ada:tier:
                  const: R
                schema:defaultValue:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
            minContains: 0
            maxContains: 1
          - contains:
              title: Time-Dependent Intensity Correction
              description: Type of time-dependent intensity (TDI) correction applied
                to compensate for beam-induced volatilization or migration of sensitive
                elements (e.g., Na, K, F in glasses, feldspars, carbonates).
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/empaTAPP/timeDependentIntensityCorrection
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: timeDependentIntensityCorrection
                schema:name:
                  const: Time-Dependent Intensity Correction
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: false
                ada:tier:
                  const: R
                schema:defaultValue:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
            minContains: 0
            maxContains: 1
    ada:channelTemplate:
      type: object
      properties:
        ada:channelColumns:
          type: array
          items:
            anyOf:
            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/ChannelIdentifierColumn
            - title: Background Counting Time
              description: Total time spent counting at off-peak background position(s)
                in seconds, summed across all background positions.
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/empaTAPP/backgroundCountingTime
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: backgroundCountingTime
                schema:name:
                  const: Background Counting Time
                ada:dataType:
                  const: number
                schema:readonlyValue:
                  const: false
                ada:tier:
                  const: M
                schema:defaultValue:
                  anyOf:
                  - anyOf:
                    - type: number
                    - type: string
                  - type: array
                    items:
                      anyOf:
                      - type: number
                      - type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
              - schema:defaultValue
            - title: Background Position(s)
              description: Location(s) of off-peak background measurement(s) relative
                to the peak, in mm or sin-theta, and whether on the high- or low-energy
                side.
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/empaTAPP/backgroundPosition
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: backgroundPosition
                schema:name:
                  const: Background Position(s)
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: false
                ada:tier:
                  const: R
                schema:defaultValue:
                  anyOf:
                  - type: string
                  - type: array
                    items:
                      type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
            - title: Diffracting Crystal
              description: Analyzing crystal (monochromator).
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/empaTAPP/diffractingCrystal
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: diffractingCrystal
                schema:name:
                  const: Diffracting Crystal
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: true
                ada:tier:
                  const: M
                schema:defaultValue:
                  anyOf:
                  - type: string
                  - type: array
                    items:
                      type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
              - schema:defaultValue
            - title: Dwell Time per Pixel
              description: 'Time spent acquiring X-ray signal at each pixel during
                X-ray mapping, in milliseconds. For WDS: one value per spectrometer
                assignment per pixel. For EDS: total live-time per spectrum per pixel,
                a single value.'
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/empaTAPP/dwellTimePerPixel
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: dwellTimePerPixel
                schema:name:
                  const: Dwell Time per Pixel
                ada:dataType:
                  const: number
                schema:readonlyValue:
                  const: false
                ada:tier:
                  const: M
                schema:defaultValue:
                  anyOf:
                  - anyOf:
                    - type: number
                    - type: string
                  - type: array
                    items:
                      anyOf:
                      - type: number
                      - type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
              - schema:defaultValue
            - title: Peak Counting Time
              description: Time spent counting X-ray intensity at the peak position,
                in seconds. Adjustments stay within procedure-defined bounds.
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/empaTAPP/peakCountingTime
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: peakCountingTime
                schema:name:
                  const: Peak Counting Time
                ada:dataType:
                  const: number
                schema:readonlyValue:
                  const: false
                ada:tier:
                  const: M
                schema:defaultValue:
                  anyOf:
                  - anyOf:
                    - type: number
                    - type: string
                  - type: array
                    items:
                      anyOf:
                      - type: number
                      - type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
              - schema:defaultValue
            - title: Proportional Counter / Detector
              description: Type of detector used.
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/empaTAPP/proportionalCounterDetector
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: proportionalCounterDetector
                schema:name:
                  const: Proportional Counter / Detector
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: true
                ada:tier:
                  const: R
                schema:defaultValue:
                  anyOf:
                  - type: string
                  - type: array
                    items:
                      type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
            - title: Sequence
              description: "Order in which spectrometer assignments are acquired,
                and \u2014 where the element suite exceeds the number of spectrometers
                \u2014 the passes the acquisition is divided into. Within a single
                pass all assigned spectrometers collect simultaneously, including
                at every pixel in X-ray mapping; a suite larger than the spectrometer
                count therefore requires the acquisition to be run more than once,
                each pass covering a different subset of elements."
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/empaTAPP/sequence
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: sequence
                schema:name:
                  const: Sequence
                ada:dataType:
                  const: integer
                schema:readonlyValue:
                  const: true
                ada:tier:
                  const: R
                schema:defaultValue:
                  anyOf:
                  - anyOf:
                    - type: number
                    - type: string
                  - type: array
                    items:
                      anyOf:
                      - type: number
                      - type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
            - title: WDS PHA Setting
              description: Pulse height analyzer (PHA) setting for the WDS detector.
                Integral mode accepts all pulses above a threshold; Differential mode
                selects a narrow energy window to reject higher-order reflections
                and escape peaks.
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/empaTAPP/wdsPhaSetting
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: wdsPhaSetting
                schema:name:
                  const: WDS PHA Setting
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: true
                ada:tier:
                  const: R
                schema:defaultValue:
                  anyOf:
                  - type: string
                  - type: array
                    items:
                      type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
            - title: X-ray Line
              description: X-ray emission line measured.
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/empaTAPP/xRayLine
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: xRayLine
                schema:name:
                  const: X-ray Line
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: true
                ada:tier:
                  const: M
                schema:defaultValue:
                  anyOf:
                  - type: string
                  - type: array
                    items:
                      type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
              - schema:defaultValue
          allOf:
          - contains:
              title: Background Counting Time
              description: Total time spent counting at off-peak background position(s)
                in seconds, summed across all background positions.
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/empaTAPP/backgroundCountingTime
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: backgroundCountingTime
                schema:name:
                  const: Background Counting Time
                ada:dataType:
                  const: number
                schema:readonlyValue:
                  const: false
                ada:tier:
                  const: M
                schema:defaultValue:
                  anyOf:
                  - anyOf:
                    - type: number
                    - type: string
                  - type: array
                    items:
                      anyOf:
                      - type: number
                      - type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
              - schema:defaultValue
            minContains: 0
            maxContains: 1
          - contains:
              title: Background Position(s)
              description: Location(s) of off-peak background measurement(s) relative
                to the peak, in mm or sin-theta, and whether on the high- or low-energy
                side.
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/empaTAPP/backgroundPosition
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: backgroundPosition
                schema:name:
                  const: Background Position(s)
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: false
                ada:tier:
                  const: R
                schema:defaultValue:
                  anyOf:
                  - type: string
                  - type: array
                    items:
                      type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
            minContains: 0
            maxContains: 1
          - contains:
              title: Diffracting Crystal
              description: Analyzing crystal (monochromator).
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/empaTAPP/diffractingCrystal
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: diffractingCrystal
                schema:name:
                  const: Diffracting Crystal
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: true
                ada:tier:
                  const: M
                schema:defaultValue:
                  anyOf:
                  - type: string
                  - type: array
                    items:
                      type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
              - schema:defaultValue
            minContains: 0
            maxContains: 1
          - contains:
              title: Dwell Time per Pixel
              description: 'Time spent acquiring X-ray signal at each pixel during
                X-ray mapping, in milliseconds. For WDS: one value per spectrometer
                assignment per pixel. For EDS: total live-time per spectrum per pixel,
                a single value.'
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/empaTAPP/dwellTimePerPixel
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: dwellTimePerPixel
                schema:name:
                  const: Dwell Time per Pixel
                ada:dataType:
                  const: number
                schema:readonlyValue:
                  const: false
                ada:tier:
                  const: M
                schema:defaultValue:
                  anyOf:
                  - anyOf:
                    - type: number
                    - type: string
                  - type: array
                    items:
                      anyOf:
                      - type: number
                      - type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
              - schema:defaultValue
            minContains: 0
            maxContains: 1
          - contains:
              title: Peak Counting Time
              description: Time spent counting X-ray intensity at the peak position,
                in seconds. Adjustments stay within procedure-defined bounds.
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/empaTAPP/peakCountingTime
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: peakCountingTime
                schema:name:
                  const: Peak Counting Time
                ada:dataType:
                  const: number
                schema:readonlyValue:
                  const: false
                ada:tier:
                  const: M
                schema:defaultValue:
                  anyOf:
                  - anyOf:
                    - type: number
                    - type: string
                  - type: array
                    items:
                      anyOf:
                      - type: number
                      - type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
              - schema:defaultValue
            minContains: 0
            maxContains: 1
          - contains:
              title: Proportional Counter / Detector
              description: Type of detector used.
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/empaTAPP/proportionalCounterDetector
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: proportionalCounterDetector
                schema:name:
                  const: Proportional Counter / Detector
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: true
                ada:tier:
                  const: R
                schema:defaultValue:
                  anyOf:
                  - type: string
                  - type: array
                    items:
                      type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
            minContains: 0
            maxContains: 1
          - contains:
              title: Sequence
              description: "Order in which spectrometer assignments are acquired,
                and \u2014 where the element suite exceeds the number of spectrometers
                \u2014 the passes the acquisition is divided into. Within a single
                pass all assigned spectrometers collect simultaneously, including
                at every pixel in X-ray mapping; a suite larger than the spectrometer
                count therefore requires the acquisition to be run more than once,
                each pass covering a different subset of elements."
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/empaTAPP/sequence
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: sequence
                schema:name:
                  const: Sequence
                ada:dataType:
                  const: integer
                schema:readonlyValue:
                  const: true
                ada:tier:
                  const: R
                schema:defaultValue:
                  anyOf:
                  - anyOf:
                    - type: number
                    - type: string
                  - type: array
                    items:
                      anyOf:
                      - type: number
                      - type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
            minContains: 0
            maxContains: 1
          - contains:
              title: WDS PHA Setting
              description: Pulse height analyzer (PHA) setting for the WDS detector.
                Integral mode accepts all pulses above a threshold; Differential mode
                selects a narrow energy window to reject higher-order reflections
                and escape peaks.
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/empaTAPP/wdsPhaSetting
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: wdsPhaSetting
                schema:name:
                  const: WDS PHA Setting
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: true
                ada:tier:
                  const: R
                schema:defaultValue:
                  anyOf:
                  - type: string
                  - type: array
                    items:
                      type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
            minContains: 0
            maxContains: 1
          - contains:
              title: X-ray Line
              description: X-ray emission line measured.
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/empaTAPP/xRayLine
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: xRayLine
                schema:name:
                  const: X-ray Line
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: true
                ada:tier:
                  const: M
                schema:defaultValue:
                  anyOf:
                  - type: string
                  - type: array
                    items:
                      type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
              - schema:defaultValue
            minContains: 0
            maxContains: 1
        ada:defaultChannels:
          type: array
          items:
            anyOf:
            - type: string
            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/DefinedTerm
    schema:additionalProperty:
      type: array
      items:
        anyOf:
        - title: Beam Damage Minimization
          description: Measures taken to minimize beam damage, particularly volatilization
            or migration of Na, K, F, and Cl in hydrous minerals, glasses, feldspars,
            phosphates, and carbonates. Document approach, beam conditions used, and
            phases for which it was applied.
          type: object
          properties:
            '@id':
              const: ada:parameter/empaTAPP/beamDamageMinimizationDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: beamDamageMinimizationDefault
            schema:name:
              const: Beam Damage Minimization
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
        - title: Beam Raster Dimensions
          description: "Dimensions of the small area over which the beam is rastered
            at a single analysis point, reported as width \xD7 height in \xB5m. Applicable
            when Beam Mode = Rastered; defines the effective spatial footprint of
            the measurement. Not applicable when mapping."
          type: object
          properties:
            '@id':
              const: ada:parameter/empaTAPP/beamRasterDimensionsDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: beamRasterDimensionsDefault
            schema:name:
              const: Beam Raster Dimensions
            ada:dataType:
              const: number
            ada:fieldScope:
              const: session
            schema:readonlyValue:
              const: false
            ada:tier:
              const: R
            schema:unitText:
              const: "\xB5m x \xB5m"
          required:
          - '@id'
          - '@type'
          - schema:valueName
          - schema:name
          - ada:dataType
          - ada:fieldScope
        - title: Drift Correction
          description: Method used to monitor and correct for instrument drift (beam
            current drift, spectrometer drift) during the analytical session.
          type: object
          properties:
            '@id':
              const: ada:parameter/empaTAPP/driftCorrectionDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: driftCorrectionDefault
            schema:name:
              const: Drift Correction
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
        - title: EDS Spectral Processing Type
          description: Method used to process EDS spectra and extract net peak intensities
            from raw spectral data. Applied before quantification (see Matrix Correction
            Method). Common approaches include background fitting and subtraction
            followed by peak integration, and filter fit or Gaussian deconvolution
            for overlapping peaks.
          type: object
          properties:
            '@id':
              const: ada:parameter/empaTAPP/edsSpectralProcessingType
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/empaTAPP/edsSpectralProcessingType
            schema:name:
              const: EDS Spectral Processing Type
            schema:value:
              type: string
          required:
          - '@id'
          - '@type'
          - schema:propertyID
          - schema:name
          - schema:value
          readOnly: true
        - title: Halogen Correction on Oxygen
          description: Whether oxygen content was adjusted to account for halogen
            substitution (F and/or Cl replacing OH) in halogen-bearing phases such
            as apatite, amphibole, and mica, where oxygen is calculated by stoichiometry.
          type: object
          properties:
            '@id':
              const: ada:parameter/empaTAPP/halogenCorrectionOnOxygenDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: halogenCorrectionOnOxygenDefault
            schema:name:
              const: Halogen Correction on Oxygen
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
        - title: Stage Scan vs. Beam Scan
          description: For mapping modes, whether the map was acquired by moving the
            stage while the beam is held fixed (stage scan), or by deflecting the
            beam across the field while the stage is stationary (beam scan).
          type: object
          properties:
            '@id':
              const: ada:parameter/empaTAPP/stageScanVsBeamScan
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/empaTAPP/stageScanVsBeamScan
            schema:name:
              const: Stage Scan vs. Beam Scan
            schema:value:
              type: string
          required:
          - '@id'
          - '@type'
          - schema:propertyID
          - schema:name
          - schema:value
          readOnly: true
      allOf:
      - contains:
          title: Beam Damage Minimization
          description: Measures taken to minimize beam damage, particularly volatilization
            or migration of Na, K, F, and Cl in hydrous minerals, glasses, feldspars,
            phosphates, and carbonates. Document approach, beam conditions used, and
            phases for which it was applied.
          type: object
          properties:
            '@id':
              const: ada:parameter/empaTAPP/beamDamageMinimizationDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: beamDamageMinimizationDefault
            schema:name:
              const: Beam Damage Minimization
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
          title: Beam Raster Dimensions
          description: "Dimensions of the small area over which the beam is rastered
            at a single analysis point, reported as width \xD7 height in \xB5m. Applicable
            when Beam Mode = Rastered; defines the effective spatial footprint of
            the measurement. Not applicable when mapping."
          type: object
          properties:
            '@id':
              const: ada:parameter/empaTAPP/beamRasterDimensionsDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: beamRasterDimensionsDefault
            schema:name:
              const: Beam Raster Dimensions
            ada:dataType:
              const: number
            ada:fieldScope:
              const: session
            schema:readonlyValue:
              const: false
            ada:tier:
              const: R
            schema:unitText:
              const: "\xB5m x \xB5m"
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
          title: Drift Correction
          description: Method used to monitor and correct for instrument drift (beam
            current drift, spectrometer drift) during the analytical session.
          type: object
          properties:
            '@id':
              const: ada:parameter/empaTAPP/driftCorrectionDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: driftCorrectionDefault
            schema:name:
              const: Drift Correction
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
          title: EDS Spectral Processing Type
          description: Method used to process EDS spectra and extract net peak intensities
            from raw spectral data. Applied before quantification (see Matrix Correction
            Method). Common approaches include background fitting and subtraction
            followed by peak integration, and filter fit or Gaussian deconvolution
            for overlapping peaks.
          type: object
          properties:
            '@id':
              const: ada:parameter/empaTAPP/edsSpectralProcessingType
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/empaTAPP/edsSpectralProcessingType
            schema:name:
              const: EDS Spectral Processing Type
            schema:value:
              type: string
          required:
          - '@id'
          - '@type'
          - schema:propertyID
          - schema:name
          - schema:value
          readOnly: true
        minContains: 0
        maxContains: 1
      - contains:
          title: Halogen Correction on Oxygen
          description: Whether oxygen content was adjusted to account for halogen
            substitution (F and/or Cl replacing OH) in halogen-bearing phases such
            as apatite, amphibole, and mica, where oxygen is calculated by stoichiometry.
          type: object
          properties:
            '@id':
              const: ada:parameter/empaTAPP/halogenCorrectionOnOxygenDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: halogenCorrectionOnOxygenDefault
            schema:name:
              const: Halogen Correction on Oxygen
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
          title: Stage Scan vs. Beam Scan
          description: For mapping modes, whether the map was acquired by moving the
            stage while the beam is held fixed (stage scan), or by deflecting the
            beam across the field while the stage is stationary (beam scan).
          type: object
          properties:
            '@id':
              const: ada:parameter/empaTAPP/stageScanVsBeamScan
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/empaTAPP/stageScanVsBeamScan
            schema:name:
              const: Stage Scan vs. Beam Scan
            schema:value:
              type: string
          required:
          - '@id'
          - '@type'
          - schema:propertyID
          - schema:name
          - schema:value
          readOnly: true
        minContains: 0
        maxContains: 1
    ada:edsAcquisitionMode:
      description: "Spatial acquisition sub-strategy for EDS measurements: stationary-beam
        point acquisition, line scan (beam stepped along a transect at defined intervals),
        or area map / spectrum image (beam rastered over a pixel grid). Specifies
        how the beam is positioned during data collection within the declared analytical
        mode. Record 'N/A' where the procedure has no EDS detector. 'Point' covers
        what the literature also calls spot or point-spectrum analysis. 'Map' and
        'Spectrum image' are distinct acquisitions, not synonyms: a map may retain
        element intensities alone, whereas a spectrum image retains a full spectrum
        at every pixel and can be requantified afterwards \u2014 record which was
        acquired. Where more than one mode was used, join them with '; ' rather than
        looking for a combined member."
      type: string
      enum:
      - Point
      - Line scan
      - Map
      - Spectrum image
      - N/A
      - None
      - missing
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
                  type: object
                  allOf:
                  - if:
                      properties:
                        schema:name:
                          const: Target Material
                      required:
                      - schema:name
                    then:
                      properties:
                        schema:value:
                          type: array
                          items:
                            description: General description of the material type(s)
                              this procedure is designed to analyse.
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
                              - N/A
                              - None
                              - missing
                            - type: string
                            readOnly: true
                allOf:
                - contains:
                    $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Procedure_preAnalysisImagingAndScreening
                  minContains: 0
                  maxContains: 1
                - contains:
                    properties:
                      schema:name:
                        const: Target Material
                    required:
                    - schema:name
      allOf:
      - contains:
          properties:
            '@type':
              contains:
                const: https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample
          required:
          - '@type'
    ada:edsLiveTimePerPointOrPixelDefault:
      description: EDS spectral acquisition live time per analysis point in seconds.
        Previously referred to as "EDS Acquisition Time" in this TAPP and commonly
        used under that name in EPMA and SEM-EDS contexts. Renamed to align with TEM-EDS
        usage, where the per-point vs. per-pixel distinction (point/line mode vs.
        spectrum image) is explicit. In EPMA, acquisition is always per point.
      anyOf:
      - type: number
      - type: string
    schema:actionProcess:
      type: object
      properties:
        schema:step:
          type: array
          items:
            type: object
            allOf:
            - if:
                properties:
                  schema:name:
                    const: Data reduction
                required:
                - schema:name
              then:
                properties:
                  schema:additionalProperty:
                    type: array
                    items:
                      anyOf:
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/aggregation/schema.yaml#/$defs/Param_Procedure_analysisInclusionAndRejectionCriteria
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Procedure_constantsReferenceValues
                    allOf:
                    - contains:
                        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/aggregation/schema.yaml#/$defs/Param_Procedure_analysisInclusionAndRejectionCriteria
                      minContains: 0
                      maxContains: 1
                    - contains:
                        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Procedure_constantsReferenceValues
                      minContains: 0
                      maxContains: 1
          allOf:
          - contains:
              properties:
                schema:name:
                  const: Data reduction
              required:
              - schema:name
    ada:massAbsorptionCoefficients:
      description: Database of mass absorption coefficients used in the matrix correction.
      type: string
      enum:
      - LINEMU
      - CITZMU
      - MCMASTER
      - MAC30
      - MACJTA
      - FFAST
      - Unknown
      - N/A
      - None
      - missing
      readOnly: true
    ada:matrixCorrectionMethod:
      description: "X-ray matrix correction algorithm applied during quantitative
        EDS or WDS data reduction. For X-ray mapping, applies when raw count maps
        are converted to quantitative concentration maps. Where the k-factors or calibration
        constants themselves came from \u2014 measured standards, a vendor library,
        or theoretical cross-sections \u2014 is a separate question answered by this
        technique's calibration-standard field, not here; a procedure may be both
        absorption-corrected and standardless."
      anyOf:
      - type: string
        enum:
        - PAP (Pouchou & Pichoir Full)
        - XPP (Simplified PAP)
        - PhiRhoZ Bastin (EPQ-91)
        - Love-Scott I
        - Love-Scott II
        - Armstrong / Love-Scott
        - ZAF
        - CITZAF (Armstrong 1995)
        - Bence-Albee
        - Unknown
        - N/A
        - None
        - missing
      - type: string
      readOnly: true
    ada:stepSizePixelSizeDefault:
      description: Distance between adjacent measurement points in the X-ray map in
        micrometers, defining the spatial resolution. Report both X and Y step if
        they differ.
      anyOf:
      - type: number
      - type: string
    ada:wdsDeadTimeCorrection:
      description: "Method used to correct for WDS proportional counter dead time
        at high count rates. Unlike EDS dead time \u2014 which is hardware-managed
        and reported as a session QC percentage (see EDS Dead Time) \u2014 WDS dead
        time correction is a user-selectable algorithm in the data reduction software.
        No separate measured WDS dead time value is reported; the correction is applied
        transparently during intensity-to-concentration conversion. Record the algorithm
        here and any instrument-specific constant alongside it \u2014 'Default constant
        (manufacturer) \u2014 3 \xB5s, Cameca'. The instrument vendor itself is recorded
        by Instrument Manufacturer, not by this field's allowed values."
      anyOf:
      - type: string
        enum:
        - Default constant (manufacturer)
        - Adjusted constant
        - Logarithmic
        - High-precision (Probe for EPMA)
        - Super-precision (Probe for EPMA)
        - Unknown
        - N/A
        - None
        - missing
      - type: string
      readOnly: true
    ada:monitoredEleemnts:
      type: array
      items:
        description: Specific elements monitored in this procedure, grouped by the
          target species they serve where they serve one. Includes elements monitored
          only to correct an interference, which serve no target species and so have
          no parent. The target species list is given by the Target Species field
          and is never inferred from the elements appearing here. The X-ray line,
          diffracting crystal, spectrometer assignment and counting times used for
          each monitored element are recorded in their own fields, keyed to this one.
        type: string
        readOnly: true
    ada:analyticalMode:
      type: array
      items:
        type: string
        enum:
        - EDS Point Analysis
        - EDS Mapping
        - WDS Point Analysis
        - WDS Mapping
  required:
  - ada:edsAcquisitionMode
  - ada:edsLiveTimePerPointOrPixelDefault
  - ada:massAbsorptionCoefficients
  - ada:matrixCorrectionMethod
  - ada:stepSizePixelSizeDefault
  - ada:wdsDeadTimeCorrection

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EMPA/tapp/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EMPA/tapp/schema.yaml)


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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EMPA/tapp/context.jsonld)

## Sources

* [TAPP_EPMA_filled.xlsx (Components / TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/EMPA/tapp`

