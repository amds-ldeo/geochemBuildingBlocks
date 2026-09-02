
# TEM Technique-Aligned Protocol Profile (temTAPP) (Schema)

`ogch.techniqueProfile.geochemProfile.TEM.tapp` *v0.1*

Transmission electron microscopy (TEM/STEM, incl. EDS/EELS) extension of the base TAPP definition. Basic protocol-tier fields are required top-level ada: properties; Advanced protocol-tier fields are schema:additionalProperty[] entries; an ada:analyteTemplate carries per-element columns. Generated from docs/TEM_TAPP_v7.xlsx by tools/build_tapp.py.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### temTAPP example Chaves2023
temTAPP instance derived from Chaves2023 | Synthetic magnetite | TEM+STEM imaging + EDS.
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
  "@id": "ex:temTAPP-Chaves2023",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "tem protocol — Chaves2023",
  "schema:description": "Probe size <1 nm stated for STEM-EDS maps and profiles (Sec 2.6) Reported detail: ada:analyticalSubModeDefault = BF-TEM; HRTEM (TEM Imaging); HAADF-STEM (STEM Imaging); ada:edsAcquisitionModeDefault = Line scan; Spectrum image (map).",
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
            "Oxide (synthetic magnetite Fe3O4, 99.9% purity, Sigma Aldrich; dry-sieved <45 µm; pressed into pellets at 1500 psi)"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/temTAPP/samplePreparationDetailsDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "samplePreparationDetailsDefault",
            "schema:name": "Sample Preparation Details",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "~0.1 µm C coating deposited with e-beam (5 kV, 0.8 nA); ~4 µm W coating deposited with ion beam (30 kV, 0.26 nA); thinning: CCS mode 30 kV / 0.75 nA → 0.26 nA → 90 nA; final thinning: CCS mode 16 kV / 0.47 nA; target foil thickness not stated"
          }
        ],
        "schema:description": "FIB lift-out (Ga ion)",
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
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:instrument": [
    {
      "schema:additionalType": [
        "TEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "ThermoFisher Scientific (FEI)",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "FEI Talos 200 kV",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Super-X EDS system; four silicon drift detectors (SDD)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/EDS-Detector",
          "schema:name": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "4D-STEM Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/4D-STEM-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Aberration Corrector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Aberration-Corrector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EELS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/EELS-Spectrometer"
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
          "@id": "ex:instrument/TEM/part/Electron-Source"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Imaging Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Imaging-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Monochromator",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Monochromator"
        }
      ],
      "ada:acceleratingVoltageDefault": "200 kV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/TEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:spectroscopicDetectorDefault": "EDS only",
  "ada:analyticalSubModeDefault": "BF-TEM",
  "ada:edsAcquisitionModeDefault": "Spectrum image",
  "ada:edsQuantificationMethod": "Cliff-Lorimer (k-factor)",
  "ada:phaseIdentificationMethod": "Manual d-spacing comparison: HRTEM lattice fringes; 2.5 Å → magnetite (311); 1.4 Å and 2.0 Å → metallic iron (110) and (200); 2.9 Å / 2.5 Å / 1.6 Å → magnetite (220)/(311)/(511)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "TEM/STEM"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Purdue University"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "FIB-SEM; XPS; VNIR reflectance spectroscopy",
        "schema:description": "FIB-SEM (Helios G4 UX, Purdue) prepared electron-transparent lamellae from irradiated pellets (performed before TEM, destructive prep step); XPS and VNIR spectroscopy performed in parallel on same irradiated pellets for chemical and spectral characterization"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:cameraLengthDefault": -9999,
  "ada:convergenceSemiAngle": -9999,
  "ada:edsCalibrationStandardDefault": "missing",
  "ada:eelsAcquisitionModeDefault": "missing",
  "ada:eelsAcquisitionTimePerSpectrumDefault": -9999,
  "ada:eelsCollectionSemiAngle": -9999,
  "ada:eelsEnergyLossRangeDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stemDwellTimePerPixelDefault": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/TEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:temTAPP-Chaves2023",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "tem protocol \u2014 Chaves2023",
  "schema:description": "Probe size <1 nm stated for STEM-EDS maps and profiles (Sec 2.6) Reported detail: ada:analyticalSubModeDefault = BF-TEM; HRTEM (TEM Imaging); HAADF-STEM (STEM Imaging); ada:edsAcquisitionModeDefault = Line scan; Spectrum image (map).",
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
            "Oxide (synthetic magnetite Fe3O4, 99.9% purity, Sigma Aldrich; dry-sieved <45 \u00b5m; pressed into pellets at 1500 psi)"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/temTAPP/samplePreparationDetailsDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "samplePreparationDetailsDefault",
            "schema:name": "Sample Preparation Details",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "~0.1 \u00b5m C coating deposited with e-beam (5 kV, 0.8 nA); ~4 \u00b5m W coating deposited with ion beam (30 kV, 0.26 nA); thinning: CCS mode 30 kV / 0.75 nA \u2192 0.26 nA \u2192 90 nA; final thinning: CCS mode 16 kV / 0.47 nA; target foil thickness not stated"
          }
        ],
        "schema:description": "FIB lift-out (Ga ion)",
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
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:instrument": [
    {
      "schema:additionalType": [
        "TEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "ThermoFisher Scientific (FEI)",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "FEI Talos 200 kV",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Super-X EDS system; four silicon drift detectors (SDD)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/EDS-Detector",
          "schema:name": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "4D-STEM Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/4D-STEM-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Aberration Corrector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Aberration-Corrector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EELS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/EELS-Spectrometer"
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
          "@id": "ex:instrument/TEM/part/Electron-Source"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Imaging Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Imaging-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Monochromator",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Monochromator"
        }
      ],
      "ada:acceleratingVoltageDefault": "200 kV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/TEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:spectroscopicDetectorDefault": "EDS only",
  "ada:analyticalSubModeDefault": "BF-TEM",
  "ada:edsAcquisitionModeDefault": "Spectrum image",
  "ada:edsQuantificationMethod": "Cliff-Lorimer (k-factor)",
  "ada:phaseIdentificationMethod": "Manual d-spacing comparison: HRTEM lattice fringes; 2.5 \u00c5 \u2192 magnetite (311); 1.4 \u00c5 and 2.0 \u00c5 \u2192 metallic iron (110) and (200); 2.9 \u00c5 / 2.5 \u00c5 / 1.6 \u00c5 \u2192 magnetite (220)/(311)/(511)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "TEM/STEM"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Purdue University"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "FIB-SEM; XPS; VNIR reflectance spectroscopy",
        "schema:description": "FIB-SEM (Helios G4 UX, Purdue) prepared electron-transparent lamellae from irradiated pellets (performed before TEM, destructive prep step); XPS and VNIR spectroscopy performed in parallel on same irradiated pellets for chemical and spectral characterization"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:cameraLengthDefault": -9999,
  "ada:convergenceSemiAngle": -9999,
  "ada:edsCalibrationStandardDefault": "missing",
  "ada:eelsAcquisitionModeDefault": "missing",
  "ada:eelsAcquisitionTimePerSpectrumDefault": -9999,
  "ada:eelsCollectionSemiAngle": -9999,
  "ada:eelsEnergyLossRangeDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stemDwellTimePerPixelDefault": -9999,
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

ex:temTAPP-Chaves2023 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/temTAPP/samplePreparationDetailsDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "FIB lift-out (Ga ion)" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "Probe size <1 nm stated for STEM-EDS maps and profiles (Sec 2.6) Reported detail: ada:analyticalSubModeDefault = BF-TEM; HRTEM (TEM Imaging); HAADF-STEM (STEM Imaging); ada:edsAcquisitionModeDefault = Line scan; Spectrum image (map)." ;
    schema1:instrument <https://example.org/instrument/TEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Purdue University" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "TEM/STEM" ] ;
    schema1:name "tem protocol — Chaves2023" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Oxide (synthetic magnetite Fe3O4, 99.9% purity, Sigma Aldrich; dry-sieved <45 µm; pressed into pellets at 1500 psi)" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "FIB-SEM (Helios G4 UX, Purdue) prepared electron-transparent lamellae from irradiated pellets (performed before TEM, destructive prep step); XPS and VNIR spectroscopy performed in parallel on same irradiated pellets for chemical and spectral characterization" ;
                    schema1:name "FIB-SEM; XPS; VNIR reflectance spectroscopy" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalSubModeDefault "BF-TEM" ;
    ada:cameraLengthDefault -9999 ;
    ada:convergenceSemiAngle -9999 ;
    ada:edsAcquisitionModeDefault "Spectrum image" ;
    ada:edsCalibrationStandardDefault "missing" ;
    ada:edsQuantificationMethod "Cliff-Lorimer (k-factor)" ;
    ada:eelsAcquisitionModeDefault "missing" ;
    ada:eelsAcquisitionTimePerSpectrumDefault -9999 ;
    ada:eelsCollectionSemiAngle -9999 ;
    ada:eelsEnergyLossRangeDefault "missing" ;
    ada:phaseIdentificationMethod "Manual d-spacing comparison: HRTEM lattice fringes; 2.5 Å → magnetite (311); 1.4 Å and 2.0 Å → metallic iron (110) and (200); 2.9 Å / 2.5 Å / 1.6 Å → magnetite (220)/(311)/(511)" ;
    ada:samplingUnit "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:spectroscopicDetectorDefault "EDS only" ;
    ada:stemDwellTimePerPixelDefault -9999 .

<https://ada.astromat.org/metadata/parameter/temTAPP/samplePreparationDetailsDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "~0.1 µm C coating deposited with e-beam (5 kV, 0.8 nA); ~4 µm W coating deposited with ion beam (30 kV, 0.26 nA); thinning: CCS mode 30 kV / 0.75 nA → 0.26 nA → 90 nA; final thinning: CCS mode 16 kV / 0.47 nA; target foil thickness not stated" ;
    schema1:name "Sample Preparation Details" ;
    schema1:valueName "samplePreparationDetailsDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://example.org/instrument/TEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "TEM" ;
    schema1:hasPart <https://example.org/instrument/TEM/part/4D-STEM-Detector>,
        <https://example.org/instrument/TEM/part/Aberration-Corrector>,
        <https://example.org/instrument/TEM/part/EDS-Detector>,
        <https://example.org/instrument/TEM/part/EELS-Spectrometer>,
        <https://example.org/instrument/TEM/part/Electron-Source>,
        <https://example.org/instrument/TEM/part/Imaging-Detector>,
        <https://example.org/instrument/TEM/part/Monochromator> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "ThermoFisher Scientific (FEI)" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "FEI Talos 200 kV" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "200 kV" .

<https://example.org/instrument/TEM/part/4D-STEM-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "4D-STEM Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Aberration-Corrector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Aberration Corrector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:description "Super-X EDS system; four silicon drift detectors (SDD)" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/EELS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EELS Spectrometer" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Imaging-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Imaging Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Monochromator> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Monochromator" ;
    schema1:name "missing" .


```


### temTAPP example Zega2025
temTAPP instance derived from Zega2025 | Bennu particles | STEM+EDS+SAED (U of A HF5000).
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
  "@id": "ex:temTAPP-Zega2025",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "tem protocol — Zega2025",
  "schema:description": "Probe size 136 pm stated for EDS spectrum images (Methods/TEM/U of A) Reported detail: ada:analyticalSubModeDefault = HAADF-STEM; BF-STEM (STEM Imaging); BF-TEM; HRTEM (TEM Imaging); SAED (Electron Diffraction); ada:edsAcquisitionModeDefault = Spectrum image (map).",
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
            "Silicate mineral (sheet silicates: serpentine/saponite); Sulfide (pyrrhotite/pentlandite); Oxide (magnetite); Carbonate; Organic matter/IOM (C nanoglobules) — OSIRIS-REx Bennu returned samples"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/temTAPP/samplePreparationDetailsDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "samplePreparationDetailsDefault",
            "schema:name": "Sample Preparation Details",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "ThermoScientific Helios G3 FIB-SEM (K-ALFAA); 12-µm × 4-µm C capping layer; lamellae thinned to electron transparency at 30 keV, 2.5 to 0.8 nA; standard stair-step method"
          }
        ],
        "schema:description": "FIB lift-out (Ga ion)",
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
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/temTAPP/imageProcessingMethodsAppliedDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "imageProcessingMethodsAppliedDefault",
            "schema:name": "Image Processing Methods Applied",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Selective quantification: summed spectra extracted from specific phyllosilicate domains in EDS spectrum images"
          }
        ],
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
  "schema:instrument": [
    {
      "schema:additionalType": [
        "TEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "Hitachi",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "Hitachi HF5000 (200 keV)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Cold-FEG",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/Electron-Source",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "Aberration Corrector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Probe Cs-corrected (STEM)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/Aberration-Corrector",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Oxford Instruments X-Max N100 TLE EDS; dual 100 mm² windowless SDDs; Ω = 2.0 sr",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/EDS-Detector",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "EELS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Gatan Quantum EELS (post-column)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/EELS-Spectrometer",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "Imaging Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "BF, DF, SE STEM detectors; Gatan OneView 4096×4096 CMOS camera",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/Imaging-Detector",
          "schema:name": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "4D-STEM Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/4D-STEM-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Monochromator",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Monochromator"
        }
      ],
      "ada:acceleratingVoltageDefault": "200 keV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/TEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:spectroscopicDetectorDefault": "EDS and EELS",
  "ada:analyticalSubModeDefault": "BF-STEM",
  "ada:stemDwellTimePerPixelDefault": "8 µs (EDS spectrum image frame time per pixel)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/temTAPP/stemScanDimensionsDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "stemScanDimensionsDefault",
      "schema:name": "STEM Scan Dimensions",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 512,
      "schema:description": "512×512 pixels (EDS spectrum images)"
    },
    {
      "@id": "ada:parameter/temTAPP/edsEnergyRangeDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "edsEnergyRangeDefault",
      "schema:name": "EDS Energy Range",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "20 keV (2048 channels)"
    }
  ],
  "ada:edsAcquisitionModeDefault": "Spectrum image",
  "ada:phaseIdentificationMethod": "CRISP software (SAED patterns); Adobe Photoshop d-spacing measurement based on calibrated camera constants",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "TEM/STEM"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "K-ALFAA (Kuiper-Arizona Laboratory for Astromaterials Analysis), University of Arizona"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "FIB-SEM; SEM; EMPA; XRD; CL spectroscopy; XANES (synchrotron)",
        "schema:description": "FIB-SEM (TS Helios G3, K-ALFAA) prepared TEM sections from SEM/EMPA-characterized particles; SEM/EMPA/XRD/CL provided mm–µm scale context before TEM; XANES at ALS beamline 5.3.2.2 acquired on FIB sections for Fe oxidation state"
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
      "schema:name": "CRISP (SAED analysis); Adobe Photoshop (d-spacing measurement from calibrated camera constants)"
    }
  ],
  "ada:cameraLengthDefault": -9999,
  "ada:convergenceSemiAngle": -9999,
  "ada:edsCalibrationStandardDefault": "missing",
  "ada:edsQuantificationMethod": "missing",
  "ada:eelsAcquisitionModeDefault": "missing",
  "ada:eelsAcquisitionTimePerSpectrumDefault": -9999,
  "ada:eelsCollectionSemiAngle": -9999,
  "ada:eelsEnergyLossRangeDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/TEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:temTAPP-Zega2025",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "tem protocol \u2014 Zega2025",
  "schema:description": "Probe size 136 pm stated for EDS spectrum images (Methods/TEM/U of A) Reported detail: ada:analyticalSubModeDefault = HAADF-STEM; BF-STEM (STEM Imaging); BF-TEM; HRTEM (TEM Imaging); SAED (Electron Diffraction); ada:edsAcquisitionModeDefault = Spectrum image (map).",
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
            "Silicate mineral (sheet silicates: serpentine/saponite); Sulfide (pyrrhotite/pentlandite); Oxide (magnetite); Carbonate; Organic matter/IOM (C nanoglobules) \u2014 OSIRIS-REx Bennu returned samples"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/temTAPP/samplePreparationDetailsDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "samplePreparationDetailsDefault",
            "schema:name": "Sample Preparation Details",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "ThermoScientific Helios G3 FIB-SEM (K-ALFAA); 12-\u00b5m \u00d7 4-\u00b5m C capping layer; lamellae thinned to electron transparency at 30 keV, 2.5 to 0.8 nA; standard stair-step method"
          }
        ],
        "schema:description": "FIB lift-out (Ga ion)",
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
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/temTAPP/imageProcessingMethodsAppliedDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "imageProcessingMethodsAppliedDefault",
            "schema:name": "Image Processing Methods Applied",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Selective quantification: summed spectra extracted from specific phyllosilicate domains in EDS spectrum images"
          }
        ],
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
  "schema:instrument": [
    {
      "schema:additionalType": [
        "TEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "Hitachi",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "Hitachi HF5000 (200 keV)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Cold-FEG",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/Electron-Source",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "Aberration Corrector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Probe Cs-corrected (STEM)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/Aberration-Corrector",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Oxford Instruments X-Max N100 TLE EDS; dual 100 mm\u00b2 windowless SDDs; \u03a9 = 2.0 sr",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/EDS-Detector",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "EELS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Gatan Quantum EELS (post-column)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/EELS-Spectrometer",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "Imaging Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "BF, DF, SE STEM detectors; Gatan OneView 4096\u00d74096 CMOS camera",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/Imaging-Detector",
          "schema:name": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "4D-STEM Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/4D-STEM-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Monochromator",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Monochromator"
        }
      ],
      "ada:acceleratingVoltageDefault": "200 keV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/TEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:spectroscopicDetectorDefault": "EDS and EELS",
  "ada:analyticalSubModeDefault": "BF-STEM",
  "ada:stemDwellTimePerPixelDefault": "8 \u00b5s (EDS spectrum image frame time per pixel)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/temTAPP/stemScanDimensionsDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "stemScanDimensionsDefault",
      "schema:name": "STEM Scan Dimensions",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 512,
      "schema:description": "512\u00d7512 pixels (EDS spectrum images)"
    },
    {
      "@id": "ada:parameter/temTAPP/edsEnergyRangeDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "edsEnergyRangeDefault",
      "schema:name": "EDS Energy Range",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "20 keV (2048 channels)"
    }
  ],
  "ada:edsAcquisitionModeDefault": "Spectrum image",
  "ada:phaseIdentificationMethod": "CRISP software (SAED patterns); Adobe Photoshop d-spacing measurement based on calibrated camera constants",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "TEM/STEM"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "K-ALFAA (Kuiper-Arizona Laboratory for Astromaterials Analysis), University of Arizona"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "FIB-SEM; SEM; EMPA; XRD; CL spectroscopy; XANES (synchrotron)",
        "schema:description": "FIB-SEM (TS Helios G3, K-ALFAA) prepared TEM sections from SEM/EMPA-characterized particles; SEM/EMPA/XRD/CL provided mm\u2013\u00b5m scale context before TEM; XANES at ALS beamline 5.3.2.2 acquired on FIB sections for Fe oxidation state"
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
      "schema:name": "CRISP (SAED analysis); Adobe Photoshop (d-spacing measurement from calibrated camera constants)"
    }
  ],
  "ada:cameraLengthDefault": -9999,
  "ada:convergenceSemiAngle": -9999,
  "ada:edsCalibrationStandardDefault": "missing",
  "ada:edsQuantificationMethod": "missing",
  "ada:eelsAcquisitionModeDefault": "missing",
  "ada:eelsAcquisitionTimePerSpectrumDefault": -9999,
  "ada:eelsCollectionSemiAngle": -9999,
  "ada:eelsEnergyLossRangeDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
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

ex:temTAPP-Zega2025 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/temTAPP/samplePreparationDetailsDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "FIB lift-out (Ga ion)" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/temTAPP/imageProcessingMethodsAppliedDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/temTAPP/edsEnergyRangeDefault>,
        <https://ada.astromat.org/metadata/parameter/temTAPP/stemScanDimensionsDefault> ;
    schema1:datePublished "missing" ;
    schema1:description "Probe size 136 pm stated for EDS spectrum images (Methods/TEM/U of A) Reported detail: ada:analyticalSubModeDefault = HAADF-STEM; BF-STEM (STEM Imaging); BF-TEM; HRTEM (TEM Imaging); SAED (Electron Diffraction); ada:edsAcquisitionModeDefault = Spectrum image (map)." ;
    schema1:instrument <https://example.org/instrument/TEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "K-ALFAA (Kuiper-Arizona Laboratory for Astromaterials Analysis), University of Arizona" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "TEM/STEM" ] ;
    schema1:name "tem protocol — Zega2025" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Silicate mineral (sheet silicates: serpentine/saponite); Sulfide (pyrrhotite/pentlandite); Oxide (magnetite); Carbonate; Organic matter/IOM (C nanoglobules) — OSIRIS-REx Bennu returned samples" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "FIB-SEM (TS Helios G3, K-ALFAA) prepared TEM sections from SEM/EMPA-characterized particles; SEM/EMPA/XRD/CL provided mm–µm scale context before TEM; XANES at ALS beamline 5.3.2.2 acquired on FIB sections for Fe oxidation state" ;
                    schema1:name "FIB-SEM; SEM; EMPA; XRD; CL spectroscopy; XANES (synchrotron)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalSubModeDefault "BF-STEM" ;
    ada:cameraLengthDefault -9999 ;
    ada:convergenceSemiAngle -9999 ;
    ada:edsAcquisitionModeDefault "Spectrum image" ;
    ada:edsCalibrationStandardDefault "missing" ;
    ada:edsQuantificationMethod "missing" ;
    ada:eelsAcquisitionModeDefault "missing" ;
    ada:eelsAcquisitionTimePerSpectrumDefault -9999 ;
    ada:eelsCollectionSemiAngle -9999 ;
    ada:eelsEnergyLossRangeDefault "missing" ;
    ada:phaseIdentificationMethod "CRISP software (SAED patterns); Adobe Photoshop d-spacing measurement based on calibrated camera constants" ;
    ada:samplingUnit "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:spectroscopicDetectorDefault "EDS and EELS" ;
    ada:stemDwellTimePerPixelDefault "8 µs (EDS spectrum image frame time per pixel)" ;
    bios:computationalTool [ schema1:name "CRISP (SAED analysis); Adobe Photoshop (d-spacing measurement from calibrated camera constants)" ;
            ada:toolRole "dataReduction" ] .

<https://ada.astromat.org/metadata/parameter/temTAPP/edsEnergyRangeDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "20 keV (2048 channels)" ;
    schema1:name "EDS Energy Range" ;
    schema1:valueName "edsEnergyRangeDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/temTAPP/imageProcessingMethodsAppliedDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Selective quantification: summed spectra extracted from specific phyllosilicate domains in EDS spectrum images" ;
    schema1:name "Image Processing Methods Applied" ;
    schema1:valueName "imageProcessingMethodsAppliedDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/temTAPP/samplePreparationDetailsDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "ThermoScientific Helios G3 FIB-SEM (K-ALFAA); 12-µm × 4-µm C capping layer; lamellae thinned to electron transparency at 30 keV, 2.5 to 0.8 nA; standard stair-step method" ;
    schema1:name "Sample Preparation Details" ;
    schema1:valueName "samplePreparationDetailsDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/temTAPP/stemScanDimensionsDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 512 ;
    schema1:description "512×512 pixels (EDS spectrum images)" ;
    schema1:name "STEM Scan Dimensions" ;
    schema1:valueName "stemScanDimensionsDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://example.org/instrument/TEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "TEM" ;
    schema1:hasPart <https://example.org/instrument/TEM/part/4D-STEM-Detector>,
        <https://example.org/instrument/TEM/part/Aberration-Corrector>,
        <https://example.org/instrument/TEM/part/EDS-Detector>,
        <https://example.org/instrument/TEM/part/EELS-Spectrometer>,
        <https://example.org/instrument/TEM/part/Electron-Source>,
        <https://example.org/instrument/TEM/part/Imaging-Detector>,
        <https://example.org/instrument/TEM/part/Monochromator> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Hitachi" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Hitachi HF5000 (200 keV)" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "200 keV" .

<https://example.org/instrument/TEM/part/4D-STEM-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "4D-STEM Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Aberration-Corrector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Aberration Corrector" ;
    schema1:description "Probe Cs-corrected (STEM)" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:description "Oxford Instruments X-Max N100 TLE EDS; dual 100 mm² windowless SDDs; Ω = 2.0 sr" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/EELS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EELS Spectrometer" ;
    schema1:description "Gatan Quantum EELS (post-column)" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "Cold-FEG" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Imaging-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Imaging Detector" ;
    schema1:description "BF, DF, SE STEM detectors; Gatan OneView 4096×4096 CMOS camera" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Monochromator> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Monochromator" ;
    schema1:name "missing" .


```


### temTAPP example Zega2025-2
temTAPP instance derived from Zega2025 | Bennu particles | STEM+EDS (UCB TitanX).
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
  "@id": "ex:temTAPP-Zega2025-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "tem protocol — Zega2025-2",
  "schema:description": "Beam energy range 80–300 keV; specific voltage per dataset not stated Reported detail: ada:analyticalSubModeDefault = HAADF-STEM (STEM Imaging); ada:edsAcquisitionModeDefault = Spectrum image (map).",
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
            "Silicate mineral (sheet silicates: serpentine/saponite); Sulfide (pyrrhotite/pentlandite); Oxide (magnetite); Carbonate; Organic matter/IOM (C nanoglobules) — OSIRIS-REx Bennu returned samples"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/temTAPP/samplePreparationDetailsDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "samplePreparationDetailsDefault",
            "schema:name": "Sample Preparation Details",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "FEI Helios G4 UX (Molecular Foundry, LBNL); Ga+ coarse milling 16–30 keV; polishing down to 1 keV; thickness <100 to 600 nm (thicker for Fe-L XANES and tomography; thinner for C-K and TEM)"
          }
        ],
        "schema:description": "FIB lift-out (Ga ion)",
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
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/temTAPP/imageProcessingMethodsAppliedDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "imageProcessingMethodsAppliedDefault",
            "schema:name": "Image Processing Methods Applied",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Sequential map acquisition combined in Python to control light-element volatilization"
          }
        ],
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
  "schema:instrument": [
    {
      "schema:additionalType": [
        "TEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "ThermoFisher Scientific (FEI)",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "FEI TitanX",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Bruker quad SDD; Ω = 0.6 sr",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/EDS-Detector",
          "schema:name": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "4D-STEM Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/4D-STEM-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Aberration Corrector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Aberration-Corrector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EELS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/EELS-Spectrometer"
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
          "@id": "ex:instrument/TEM/part/Electron-Source"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Imaging Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Imaging-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Monochromator",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Monochromator"
        }
      ],
      "ada:acceleratingVoltageDefault": "80–300 keV (range; specific voltage per dataset not stated)",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/TEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:spectroscopicDetectorDefault": "EDS only",
  "ada:analyticalSubModeDefault": "ADF",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/temTAPP/stemProbeCurrentDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "stemProbeCurrentDefault",
      "schema:name": "STEM Probe Current",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 0.25,
      "schema:description": "<0.25 nA"
    },
    {
      "@id": "ada:parameter/temTAPP/stemFrameAveragingDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "stemFrameAveragingDefault",
      "schema:name": "STEM Frame Averaging",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Sequential acquisition several minutes to >1 h; combined using Python (light-element volatilization control)"
    }
  ],
  "ada:edsAcquisitionModeDefault": "Spectrum image",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "TEM/STEM"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Molecular Foundry, Lawrence Berkeley National Laboratory"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "FIB-SEM; XANES (synchrotron)",
        "schema:description": "FIB-SEM (FEI Helios G4 UX, Molecular Foundry) prepared TEM sections; XANES acquired at ALS beamline 5.3.2.2 on same sections for C/Fe chemistry"
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
      "schema:name": "Python (sequential map combination)"
    }
  ],
  "ada:cameraLengthDefault": -9999,
  "ada:convergenceSemiAngle": -9999,
  "ada:edsCalibrationStandardDefault": "missing",
  "ada:edsQuantificationMethod": "missing",
  "ada:eelsAcquisitionModeDefault": "missing",
  "ada:eelsAcquisitionTimePerSpectrumDefault": -9999,
  "ada:eelsCollectionSemiAngle": -9999,
  "ada:eelsEnergyLossRangeDefault": "missing",
  "ada:phaseIdentificationMethod": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stemDwellTimePerPixelDefault": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/TEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:temTAPP-Zega2025-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "tem protocol \u2014 Zega2025-2",
  "schema:description": "Beam energy range 80\u2013300 keV; specific voltage per dataset not stated Reported detail: ada:analyticalSubModeDefault = HAADF-STEM (STEM Imaging); ada:edsAcquisitionModeDefault = Spectrum image (map).",
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
            "Silicate mineral (sheet silicates: serpentine/saponite); Sulfide (pyrrhotite/pentlandite); Oxide (magnetite); Carbonate; Organic matter/IOM (C nanoglobules) \u2014 OSIRIS-REx Bennu returned samples"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/temTAPP/samplePreparationDetailsDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "samplePreparationDetailsDefault",
            "schema:name": "Sample Preparation Details",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "FEI Helios G4 UX (Molecular Foundry, LBNL); Ga+ coarse milling 16\u201330 keV; polishing down to 1 keV; thickness <100 to 600 nm (thicker for Fe-L XANES and tomography; thinner for C-K and TEM)"
          }
        ],
        "schema:description": "FIB lift-out (Ga ion)",
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
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/temTAPP/imageProcessingMethodsAppliedDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "imageProcessingMethodsAppliedDefault",
            "schema:name": "Image Processing Methods Applied",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Sequential map acquisition combined in Python to control light-element volatilization"
          }
        ],
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
  "schema:instrument": [
    {
      "schema:additionalType": [
        "TEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "ThermoFisher Scientific (FEI)",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "FEI TitanX",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Bruker quad SDD; \u03a9 = 0.6 sr",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/EDS-Detector",
          "schema:name": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "4D-STEM Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/4D-STEM-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Aberration Corrector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Aberration-Corrector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EELS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/EELS-Spectrometer"
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
          "@id": "ex:instrument/TEM/part/Electron-Source"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Imaging Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Imaging-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Monochromator",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Monochromator"
        }
      ],
      "ada:acceleratingVoltageDefault": "80\u2013300 keV (range; specific voltage per dataset not stated)",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/TEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:spectroscopicDetectorDefault": "EDS only",
  "ada:analyticalSubModeDefault": "ADF",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/temTAPP/stemProbeCurrentDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "stemProbeCurrentDefault",
      "schema:name": "STEM Probe Current",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 0.25,
      "schema:description": "<0.25 nA"
    },
    {
      "@id": "ada:parameter/temTAPP/stemFrameAveragingDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "stemFrameAveragingDefault",
      "schema:name": "STEM Frame Averaging",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Sequential acquisition several minutes to >1 h; combined using Python (light-element volatilization control)"
    }
  ],
  "ada:edsAcquisitionModeDefault": "Spectrum image",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "TEM/STEM"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Molecular Foundry, Lawrence Berkeley National Laboratory"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "FIB-SEM; XANES (synchrotron)",
        "schema:description": "FIB-SEM (FEI Helios G4 UX, Molecular Foundry) prepared TEM sections; XANES acquired at ALS beamline 5.3.2.2 on same sections for C/Fe chemistry"
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
      "schema:name": "Python (sequential map combination)"
    }
  ],
  "ada:cameraLengthDefault": -9999,
  "ada:convergenceSemiAngle": -9999,
  "ada:edsCalibrationStandardDefault": "missing",
  "ada:edsQuantificationMethod": "missing",
  "ada:eelsAcquisitionModeDefault": "missing",
  "ada:eelsAcquisitionTimePerSpectrumDefault": -9999,
  "ada:eelsCollectionSemiAngle": -9999,
  "ada:eelsEnergyLossRangeDefault": "missing",
  "ada:phaseIdentificationMethod": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stemDwellTimePerPixelDefault": -9999,
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

ex:temTAPP-Zega2025-2 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/temTAPP/samplePreparationDetailsDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "FIB lift-out (Ga ion)" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/temTAPP/imageProcessingMethodsAppliedDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/temTAPP/stemFrameAveragingDefault>,
        <https://ada.astromat.org/metadata/parameter/temTAPP/stemProbeCurrentDefault> ;
    schema1:datePublished "missing" ;
    schema1:description "Beam energy range 80–300 keV; specific voltage per dataset not stated Reported detail: ada:analyticalSubModeDefault = HAADF-STEM (STEM Imaging); ada:edsAcquisitionModeDefault = Spectrum image (map)." ;
    schema1:instrument <https://example.org/instrument/TEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Molecular Foundry, Lawrence Berkeley National Laboratory" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "TEM/STEM" ] ;
    schema1:name "tem protocol — Zega2025-2" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Silicate mineral (sheet silicates: serpentine/saponite); Sulfide (pyrrhotite/pentlandite); Oxide (magnetite); Carbonate; Organic matter/IOM (C nanoglobules) — OSIRIS-REx Bennu returned samples" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "FIB-SEM (FEI Helios G4 UX, Molecular Foundry) prepared TEM sections; XANES acquired at ALS beamline 5.3.2.2 on same sections for C/Fe chemistry" ;
                    schema1:name "FIB-SEM; XANES (synchrotron)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalSubModeDefault "ADF" ;
    ada:cameraLengthDefault -9999 ;
    ada:convergenceSemiAngle -9999 ;
    ada:edsAcquisitionModeDefault "Spectrum image" ;
    ada:edsCalibrationStandardDefault "missing" ;
    ada:edsQuantificationMethod "missing" ;
    ada:eelsAcquisitionModeDefault "missing" ;
    ada:eelsAcquisitionTimePerSpectrumDefault -9999 ;
    ada:eelsCollectionSemiAngle -9999 ;
    ada:eelsEnergyLossRangeDefault "missing" ;
    ada:phaseIdentificationMethod "missing" ;
    ada:samplingUnit "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:spectroscopicDetectorDefault "EDS only" ;
    ada:stemDwellTimePerPixelDefault -9999 ;
    bios:computationalTool [ schema1:name "Python (sequential map combination)" ;
            ada:toolRole "dataReduction" ] .

<https://ada.astromat.org/metadata/parameter/temTAPP/imageProcessingMethodsAppliedDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Sequential map acquisition combined in Python to control light-element volatilization" ;
    schema1:name "Image Processing Methods Applied" ;
    schema1:valueName "imageProcessingMethodsAppliedDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/temTAPP/samplePreparationDetailsDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "FEI Helios G4 UX (Molecular Foundry, LBNL); Ga+ coarse milling 16–30 keV; polishing down to 1 keV; thickness <100 to 600 nm (thicker for Fe-L XANES and tomography; thinner for C-K and TEM)" ;
    schema1:name "Sample Preparation Details" ;
    schema1:valueName "samplePreparationDetailsDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/temTAPP/stemFrameAveragingDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Sequential acquisition several minutes to >1 h; combined using Python (light-element volatilization control)" ;
    schema1:name "STEM Frame Averaging" ;
    schema1:valueName "stemFrameAveragingDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/temTAPP/stemProbeCurrentDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 2.5e-01 ;
    schema1:description "<0.25 nA" ;
    schema1:name "STEM Probe Current" ;
    schema1:valueName "stemProbeCurrentDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://example.org/instrument/TEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "TEM" ;
    schema1:hasPart <https://example.org/instrument/TEM/part/4D-STEM-Detector>,
        <https://example.org/instrument/TEM/part/Aberration-Corrector>,
        <https://example.org/instrument/TEM/part/EDS-Detector>,
        <https://example.org/instrument/TEM/part/EELS-Spectrometer>,
        <https://example.org/instrument/TEM/part/Electron-Source>,
        <https://example.org/instrument/TEM/part/Imaging-Detector>,
        <https://example.org/instrument/TEM/part/Monochromator> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "ThermoFisher Scientific (FEI)" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "FEI TitanX" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "80–300 keV (range; specific voltage per dataset not stated)" .

<https://example.org/instrument/TEM/part/4D-STEM-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "4D-STEM Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Aberration-Corrector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Aberration Corrector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:description "Bruker quad SDD; Ω = 0.6 sr" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/EELS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EELS Spectrometer" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Imaging-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Imaging Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Monochromator> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Monochromator" ;
    schema1:name "missing" .


```


### temTAPP example Zega2025-3
temTAPP instance derived from Zega2025 | Bennu particles | TEM+STEM+EDS+SAED (Goethe Talos F200X).
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
  "@id": "ex:temTAPP-Zega2025-3",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "tem protocol — Zega2025-3",
  "schema:description": "temTAPP instance derived from Zega2025 | Bennu particles | TEM+STEM+EDS+SAED (Goethe Talos F200X) (publication column of TEM_TAPP_v48.csv). Reported detail: ada:analyticalSubModeDefault = HAADF-STEM (STEM Imaging); BF-TEM (TEM Imaging); SAED (Electron Diffraction).",
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
            "Silicate mineral (sheet silicates: serpentine/saponite); Sulfide (pyrrhotite/pentlandite); Oxide (magnetite); Carbonate; Organic matter/IOM (C nanoglobules) — OSIRIS-REx Bennu returned samples"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/temTAPP/samplePreparationDetailsDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "samplePreparationDetailsDefault",
            "schema:name": "Sample Preparation Details",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Grain crushed; ethanol added to powder; copper mesh grid with lacey carbon support touched to suspension until all material picked up"
          }
        ],
        "schema:description": "Crushing / dispersion on grid",
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
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:instrument": [
    {
      "schema:additionalType": [
        "TEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "ThermoFisher Scientific (FEI)",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "ThermoScientific Talos F200-X G2 S/TEM",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Four windowless ThermoScientific EDS silicon drift detectors",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/EDS-Detector",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "Imaging Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "ThermoScientific Ceta-S 4096×4096 16 M camera (TEM images and SAED patterns)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/Imaging-Detector",
          "schema:name": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "4D-STEM Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/4D-STEM-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Aberration Corrector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Aberration-Corrector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EELS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/EELS-Spectrometer"
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
          "@id": "ex:instrument/TEM/part/Electron-Source"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Monochromator",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Monochromator"
        }
      ],
      "ada:acceleratingVoltageDefault": "200 kV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/TEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:spectroscopicDetectorDefault": "EDS only",
  "ada:analyticalSubModeDefault": "BF-TEM",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/temTAPP/haadfCollectionAnglesDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "haadfCollectionAnglesDefault",
      "schema:name": "HAADF Collection Angles",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Inner 58 mrad (HAADF)"
    },
    {
      "@id": "ada:parameter/temTAPP/diffractionCameraLengthCalibrationMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "diffractionCameraLengthCalibrationMethodDefault",
      "schema:name": "Diffraction Camera Length Calibration Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "External standard (AGAR S106 cross grating, 3 mm)"
    },
    {
      "@id": "ada:parameter/temTAPP/diffractionCalibrationReferenceDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "diffractionCalibrationReferenceDefault",
      "schema:name": "Diffraction Calibration Reference",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "External standard (AGAR S106 cross grating, 3 mm)"
    }
  ],
  "ada:convergenceSemiAngle": "10.5 mrad",
  "ada:phaseIdentificationMethod": "Manual d-spacing comparison (SAED patterns; camera constant calibrated with AGAR S106 cross grating)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "TEM/STEM"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Schwiete Cosmochemistry Laboratory, Goethe University Frankfurt"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "None"
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
      "schema:name": "ThermoScientific Velox"
    },
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "ThermoScientific Velox"
    }
  ],
  "ada:cameraLengthDefault": -9999,
  "ada:edsAcquisitionModeDefault": "missing",
  "ada:edsCalibrationStandardDefault": "missing",
  "ada:edsQuantificationMethod": "missing",
  "ada:eelsAcquisitionModeDefault": "missing",
  "ada:eelsAcquisitionTimePerSpectrumDefault": -9999,
  "ada:eelsCollectionSemiAngle": -9999,
  "ada:eelsEnergyLossRangeDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stemDwellTimePerPixelDefault": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/TEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:temTAPP-Zega2025-3",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "tem protocol \u2014 Zega2025-3",
  "schema:description": "temTAPP instance derived from Zega2025 | Bennu particles | TEM+STEM+EDS+SAED (Goethe Talos F200X) (publication column of TEM_TAPP_v48.csv). Reported detail: ada:analyticalSubModeDefault = HAADF-STEM (STEM Imaging); BF-TEM (TEM Imaging); SAED (Electron Diffraction).",
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
            "Silicate mineral (sheet silicates: serpentine/saponite); Sulfide (pyrrhotite/pentlandite); Oxide (magnetite); Carbonate; Organic matter/IOM (C nanoglobules) \u2014 OSIRIS-REx Bennu returned samples"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/temTAPP/samplePreparationDetailsDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "samplePreparationDetailsDefault",
            "schema:name": "Sample Preparation Details",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Grain crushed; ethanol added to powder; copper mesh grid with lacey carbon support touched to suspension until all material picked up"
          }
        ],
        "schema:description": "Crushing / dispersion on grid",
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
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:instrument": [
    {
      "schema:additionalType": [
        "TEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "ThermoFisher Scientific (FEI)",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "ThermoScientific Talos F200-X G2 S/TEM",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Four windowless ThermoScientific EDS silicon drift detectors",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/EDS-Detector",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "Imaging Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "ThermoScientific Ceta-S 4096\u00d74096 16 M camera (TEM images and SAED patterns)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/Imaging-Detector",
          "schema:name": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "4D-STEM Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/4D-STEM-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Aberration Corrector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Aberration-Corrector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EELS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/EELS-Spectrometer"
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
          "@id": "ex:instrument/TEM/part/Electron-Source"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Monochromator",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Monochromator"
        }
      ],
      "ada:acceleratingVoltageDefault": "200 kV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/TEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:spectroscopicDetectorDefault": "EDS only",
  "ada:analyticalSubModeDefault": "BF-TEM",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/temTAPP/haadfCollectionAnglesDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "haadfCollectionAnglesDefault",
      "schema:name": "HAADF Collection Angles",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Inner 58 mrad (HAADF)"
    },
    {
      "@id": "ada:parameter/temTAPP/diffractionCameraLengthCalibrationMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "diffractionCameraLengthCalibrationMethodDefault",
      "schema:name": "Diffraction Camera Length Calibration Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "External standard (AGAR S106 cross grating, 3 mm)"
    },
    {
      "@id": "ada:parameter/temTAPP/diffractionCalibrationReferenceDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "diffractionCalibrationReferenceDefault",
      "schema:name": "Diffraction Calibration Reference",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "External standard (AGAR S106 cross grating, 3 mm)"
    }
  ],
  "ada:convergenceSemiAngle": "10.5 mrad",
  "ada:phaseIdentificationMethod": "Manual d-spacing comparison (SAED patterns; camera constant calibrated with AGAR S106 cross grating)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "TEM/STEM"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Schwiete Cosmochemistry Laboratory, Goethe University Frankfurt"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "None"
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
      "schema:name": "ThermoScientific Velox"
    },
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "ThermoScientific Velox"
    }
  ],
  "ada:cameraLengthDefault": -9999,
  "ada:edsAcquisitionModeDefault": "missing",
  "ada:edsCalibrationStandardDefault": "missing",
  "ada:edsQuantificationMethod": "missing",
  "ada:eelsAcquisitionModeDefault": "missing",
  "ada:eelsAcquisitionTimePerSpectrumDefault": -9999,
  "ada:eelsCollectionSemiAngle": -9999,
  "ada:eelsEnergyLossRangeDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stemDwellTimePerPixelDefault": -9999,
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

ex:temTAPP-Zega2025-3 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/temTAPP/samplePreparationDetailsDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Crushing / dispersion on grid" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/temTAPP/diffractionCalibrationReferenceDefault>,
        <https://ada.astromat.org/metadata/parameter/temTAPP/diffractionCameraLengthCalibrationMethodDefault>,
        <https://ada.astromat.org/metadata/parameter/temTAPP/haadfCollectionAnglesDefault> ;
    schema1:datePublished "missing" ;
    schema1:description "temTAPP instance derived from Zega2025 | Bennu particles | TEM+STEM+EDS+SAED (Goethe Talos F200X) (publication column of TEM_TAPP_v48.csv). Reported detail: ada:analyticalSubModeDefault = HAADF-STEM (STEM Imaging); BF-TEM (TEM Imaging); SAED (Electron Diffraction)." ;
    schema1:instrument <https://example.org/instrument/TEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Schwiete Cosmochemistry Laboratory, Goethe University Frankfurt" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "TEM/STEM" ] ;
    schema1:name "tem protocol — Zega2025-3" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Silicate mineral (sheet silicates: serpentine/saponite); Sulfide (pyrrhotite/pentlandite); Oxide (magnetite); Carbonate; Organic matter/IOM (C nanoglobules) — OSIRIS-REx Bennu returned samples" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "None" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalSubModeDefault "BF-TEM" ;
    ada:cameraLengthDefault -9999 ;
    ada:convergenceSemiAngle "10.5 mrad" ;
    ada:edsAcquisitionModeDefault "missing" ;
    ada:edsCalibrationStandardDefault "missing" ;
    ada:edsQuantificationMethod "missing" ;
    ada:eelsAcquisitionModeDefault "missing" ;
    ada:eelsAcquisitionTimePerSpectrumDefault -9999 ;
    ada:eelsCollectionSemiAngle -9999 ;
    ada:eelsEnergyLossRangeDefault "missing" ;
    ada:phaseIdentificationMethod "Manual d-spacing comparison (SAED patterns; camera constant calibrated with AGAR S106 cross grating)" ;
    ada:samplingUnit "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:spectroscopicDetectorDefault "EDS only" ;
    ada:stemDwellTimePerPixelDefault -9999 ;
    bios:computationalTool [ schema1:name "ThermoScientific Velox" ;
            ada:toolRole "acquisition" ],
        [ schema1:name "ThermoScientific Velox" ;
            ada:toolRole "dataReduction" ] .

<https://ada.astromat.org/metadata/parameter/temTAPP/diffractionCalibrationReferenceDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "External standard (AGAR S106 cross grating, 3 mm)" ;
    schema1:name "Diffraction Calibration Reference" ;
    schema1:valueName "diffractionCalibrationReferenceDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/temTAPP/diffractionCameraLengthCalibrationMethodDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "External standard (AGAR S106 cross grating, 3 mm)" ;
    schema1:name "Diffraction Camera Length Calibration Method" ;
    schema1:valueName "diffractionCameraLengthCalibrationMethodDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/temTAPP/haadfCollectionAnglesDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Inner 58 mrad (HAADF)" ;
    schema1:name "HAADF Collection Angles" ;
    schema1:valueName "haadfCollectionAnglesDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/temTAPP/samplePreparationDetailsDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Grain crushed; ethanol added to powder; copper mesh grid with lacey carbon support touched to suspension until all material picked up" ;
    schema1:name "Sample Preparation Details" ;
    schema1:valueName "samplePreparationDetailsDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://example.org/instrument/TEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "TEM" ;
    schema1:hasPart <https://example.org/instrument/TEM/part/4D-STEM-Detector>,
        <https://example.org/instrument/TEM/part/Aberration-Corrector>,
        <https://example.org/instrument/TEM/part/EDS-Detector>,
        <https://example.org/instrument/TEM/part/EELS-Spectrometer>,
        <https://example.org/instrument/TEM/part/Electron-Source>,
        <https://example.org/instrument/TEM/part/Imaging-Detector>,
        <https://example.org/instrument/TEM/part/Monochromator> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "ThermoFisher Scientific (FEI)" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "ThermoScientific Talos F200-X G2 S/TEM" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "200 kV" .

<https://example.org/instrument/TEM/part/4D-STEM-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "4D-STEM Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Aberration-Corrector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Aberration Corrector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:description "Four windowless ThermoScientific EDS silicon drift detectors" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/EELS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EELS Spectrometer" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Imaging-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Imaging Detector" ;
    schema1:description "ThermoScientific Ceta-S 4096×4096 16 M camera (TEM images and SAED patterns)" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Monochromator> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Monochromator" ;
    schema1:name "missing" .


```


### temTAPP example Zega2025-4
temTAPP instance derived from Zega2025 | Bennu particles | STEM+EDS+HRTEM+SAED (JSC JEOL 2500SE).
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
  "@id": "ex:temTAPP-Zega2025-4",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "tem protocol — Zega2025-4",
  "schema:description": "2-nm probe stated for EDS spectrum images; final FIB section ~100 nm thick Reported detail: ada:analyticalSubModeDefault = BF-STEM; DF-STEM (STEM Imaging); HRTEM (TEM Imaging); SAED (Electron Diffraction); ada:edsAcquisitionModeDefault = Spectrum image (map); ada:edsQuantificationMethod = Cliff-Lorimer (k-factor from well-characterized standards; Thermo System7).",
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
            "Silicate mineral (sheet silicates: serpentine/saponite); Sulfide (pyrrhotite/pentlandite); Oxide (magnetite); Carbonate; Organic matter/IOM (C nanoglobules) — OSIRIS-REx Bennu returned samples"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/temTAPP/samplePreparationDetailsDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "samplePreparationDetailsDefault",
            "schema:name": "Sample Preparation Details",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "FEI Quanta3D600 dual-beam FIB-SEM; e-beam C cap 0.5–1 µm + ion-beam C cap 2–3 µm; milling 30 kV Ga+ → 16 kV → 5 kV final; ~100 nm thick; ion-beam Pt weld to Cu half grids"
          }
        ],
        "schema:description": "FIB lift-out (Ga ion)",
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
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:instrument": [
    {
      "schema:additionalType": [
        "TEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "JEOL 2500SE (200 kV)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "JEOL 70 mm² SDD",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/EDS-Detector",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "EELS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Gatan Tridiem GIF",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/EELS-Spectrometer",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "Imaging Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "BF, DF, SE STEM detectors; Gatan OneView 4096×4096 CMOS camera (HRTEM and electron diffraction)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/Imaging-Detector",
          "schema:name": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "4D-STEM Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/4D-STEM-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Aberration Corrector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Aberration-Corrector"
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
          "@id": "ex:instrument/TEM/part/Electron-Source"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Monochromator",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Monochromator"
        }
      ],
      "ada:acceleratingVoltageDefault": "200 kV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/TEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:spectroscopicDetectorDefault": "EDS and EELS",
  "ada:analyticalSubModeDefault": "BF-STEM",
  "ada:stemDwellTimePerPixelDefault": "50 µs",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/temTAPP/stemScanDimensionsDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "stemScanDimensionsDefault",
      "schema:name": "STEM Scan Dimensions",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 256,
      "schema:description": "256×200 pixels (EDS spectrum images)"
    },
    {
      "@id": "ada:parameter/temTAPP/stemFrameAveragingDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "stemFrameAveragingDefault",
      "schema:name": "STEM Frame Averaging",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Successive frames until counting statistics <1% for major elements"
    }
  ],
  "ada:edsAcquisitionModeDefault": "Spectrum image",
  "ada:edsQuantificationMethod": "Cliff-Lorimer (k-factor)",
  "ada:edsCalibrationStandardDefault": "k-factors from well-characterized standards (standards not specified); Thermo System7",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "TEM/STEM"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "ARES Division, NASA Johnson Space Center"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "FIB-SEM; SEM; XRD",
        "schema:description": "FIB-SEM (FEI Quanta3D600) prepared TEM sections from particles characterized by SEM; XRD provided bulk mineralogy context"
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
      "schema:name": "Thermo System7"
    },
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Thermo System7 (EDS quantification)"
    }
  ],
  "ada:cameraLengthDefault": -9999,
  "ada:convergenceSemiAngle": -9999,
  "ada:eelsAcquisitionModeDefault": "missing",
  "ada:eelsAcquisitionTimePerSpectrumDefault": -9999,
  "ada:eelsCollectionSemiAngle": -9999,
  "ada:eelsEnergyLossRangeDefault": "missing",
  "ada:phaseIdentificationMethod": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/TEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:temTAPP-Zega2025-4",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "tem protocol \u2014 Zega2025-4",
  "schema:description": "2-nm probe stated for EDS spectrum images; final FIB section ~100 nm thick Reported detail: ada:analyticalSubModeDefault = BF-STEM; DF-STEM (STEM Imaging); HRTEM (TEM Imaging); SAED (Electron Diffraction); ada:edsAcquisitionModeDefault = Spectrum image (map); ada:edsQuantificationMethod = Cliff-Lorimer (k-factor from well-characterized standards; Thermo System7).",
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
            "Silicate mineral (sheet silicates: serpentine/saponite); Sulfide (pyrrhotite/pentlandite); Oxide (magnetite); Carbonate; Organic matter/IOM (C nanoglobules) \u2014 OSIRIS-REx Bennu returned samples"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/temTAPP/samplePreparationDetailsDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "samplePreparationDetailsDefault",
            "schema:name": "Sample Preparation Details",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "FEI Quanta3D600 dual-beam FIB-SEM; e-beam C cap 0.5\u20131 \u00b5m + ion-beam C cap 2\u20133 \u00b5m; milling 30 kV Ga+ \u2192 16 kV \u2192 5 kV final; ~100 nm thick; ion-beam Pt weld to Cu half grids"
          }
        ],
        "schema:description": "FIB lift-out (Ga ion)",
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
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:instrument": [
    {
      "schema:additionalType": [
        "TEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "JEOL 2500SE (200 kV)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "JEOL 70 mm\u00b2 SDD",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/EDS-Detector",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "EELS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Gatan Tridiem GIF",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/EELS-Spectrometer",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "Imaging Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "BF, DF, SE STEM detectors; Gatan OneView 4096\u00d74096 CMOS camera (HRTEM and electron diffraction)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/Imaging-Detector",
          "schema:name": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "4D-STEM Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/4D-STEM-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Aberration Corrector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Aberration-Corrector"
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
          "@id": "ex:instrument/TEM/part/Electron-Source"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Monochromator",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Monochromator"
        }
      ],
      "ada:acceleratingVoltageDefault": "200 kV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/TEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:spectroscopicDetectorDefault": "EDS and EELS",
  "ada:analyticalSubModeDefault": "BF-STEM",
  "ada:stemDwellTimePerPixelDefault": "50 \u00b5s",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/temTAPP/stemScanDimensionsDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "stemScanDimensionsDefault",
      "schema:name": "STEM Scan Dimensions",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 256,
      "schema:description": "256\u00d7200 pixels (EDS spectrum images)"
    },
    {
      "@id": "ada:parameter/temTAPP/stemFrameAveragingDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "stemFrameAveragingDefault",
      "schema:name": "STEM Frame Averaging",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Successive frames until counting statistics <1% for major elements"
    }
  ],
  "ada:edsAcquisitionModeDefault": "Spectrum image",
  "ada:edsQuantificationMethod": "Cliff-Lorimer (k-factor)",
  "ada:edsCalibrationStandardDefault": "k-factors from well-characterized standards (standards not specified); Thermo System7",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "TEM/STEM"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "ARES Division, NASA Johnson Space Center"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "FIB-SEM; SEM; XRD",
        "schema:description": "FIB-SEM (FEI Quanta3D600) prepared TEM sections from particles characterized by SEM; XRD provided bulk mineralogy context"
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
      "schema:name": "Thermo System7"
    },
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Thermo System7 (EDS quantification)"
    }
  ],
  "ada:cameraLengthDefault": -9999,
  "ada:convergenceSemiAngle": -9999,
  "ada:eelsAcquisitionModeDefault": "missing",
  "ada:eelsAcquisitionTimePerSpectrumDefault": -9999,
  "ada:eelsCollectionSemiAngle": -9999,
  "ada:eelsEnergyLossRangeDefault": "missing",
  "ada:phaseIdentificationMethod": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
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

ex:temTAPP-Zega2025-4 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/temTAPP/samplePreparationDetailsDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "FIB lift-out (Ga ion)" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/temTAPP/stemFrameAveragingDefault>,
        <https://ada.astromat.org/metadata/parameter/temTAPP/stemScanDimensionsDefault> ;
    schema1:datePublished "missing" ;
    schema1:description "2-nm probe stated for EDS spectrum images; final FIB section ~100 nm thick Reported detail: ada:analyticalSubModeDefault = BF-STEM; DF-STEM (STEM Imaging); HRTEM (TEM Imaging); SAED (Electron Diffraction); ada:edsAcquisitionModeDefault = Spectrum image (map); ada:edsQuantificationMethod = Cliff-Lorimer (k-factor from well-characterized standards; Thermo System7)." ;
    schema1:instrument <https://example.org/instrument/TEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "ARES Division, NASA Johnson Space Center" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "TEM/STEM" ] ;
    schema1:name "tem protocol — Zega2025-4" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Silicate mineral (sheet silicates: serpentine/saponite); Sulfide (pyrrhotite/pentlandite); Oxide (magnetite); Carbonate; Organic matter/IOM (C nanoglobules) — OSIRIS-REx Bennu returned samples" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "FIB-SEM (FEI Quanta3D600) prepared TEM sections from particles characterized by SEM; XRD provided bulk mineralogy context" ;
                    schema1:name "FIB-SEM; SEM; XRD" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalSubModeDefault "BF-STEM" ;
    ada:cameraLengthDefault -9999 ;
    ada:convergenceSemiAngle -9999 ;
    ada:edsAcquisitionModeDefault "Spectrum image" ;
    ada:edsCalibrationStandardDefault "k-factors from well-characterized standards (standards not specified); Thermo System7" ;
    ada:edsQuantificationMethod "Cliff-Lorimer (k-factor)" ;
    ada:eelsAcquisitionModeDefault "missing" ;
    ada:eelsAcquisitionTimePerSpectrumDefault -9999 ;
    ada:eelsCollectionSemiAngle -9999 ;
    ada:eelsEnergyLossRangeDefault "missing" ;
    ada:phaseIdentificationMethod "missing" ;
    ada:samplingUnit "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:spectroscopicDetectorDefault "EDS and EELS" ;
    ada:stemDwellTimePerPixelDefault "50 µs" ;
    bios:computationalTool [ schema1:name "Thermo System7 (EDS quantification)" ;
            ada:toolRole "dataReduction" ],
        [ schema1:name "Thermo System7" ;
            ada:toolRole "acquisition" ] .

<https://ada.astromat.org/metadata/parameter/temTAPP/samplePreparationDetailsDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "FEI Quanta3D600 dual-beam FIB-SEM; e-beam C cap 0.5–1 µm + ion-beam C cap 2–3 µm; milling 30 kV Ga+ → 16 kV → 5 kV final; ~100 nm thick; ion-beam Pt weld to Cu half grids" ;
    schema1:name "Sample Preparation Details" ;
    schema1:valueName "samplePreparationDetailsDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/temTAPP/stemFrameAveragingDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Successive frames until counting statistics <1% for major elements" ;
    schema1:name "STEM Frame Averaging" ;
    schema1:valueName "stemFrameAveragingDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/temTAPP/stemScanDimensionsDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 256 ;
    schema1:description "256×200 pixels (EDS spectrum images)" ;
    schema1:name "STEM Scan Dimensions" ;
    schema1:valueName "stemScanDimensionsDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://example.org/instrument/TEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "TEM" ;
    schema1:hasPart <https://example.org/instrument/TEM/part/4D-STEM-Detector>,
        <https://example.org/instrument/TEM/part/Aberration-Corrector>,
        <https://example.org/instrument/TEM/part/EDS-Detector>,
        <https://example.org/instrument/TEM/part/EELS-Spectrometer>,
        <https://example.org/instrument/TEM/part/Electron-Source>,
        <https://example.org/instrument/TEM/part/Imaging-Detector>,
        <https://example.org/instrument/TEM/part/Monochromator> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "JEOL" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "JEOL 2500SE (200 kV)" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "200 kV" .

<https://example.org/instrument/TEM/part/4D-STEM-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "4D-STEM Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Aberration-Corrector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Aberration Corrector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:description "JEOL 70 mm² SDD" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/EELS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EELS Spectrometer" ;
    schema1:description "Gatan Tridiem GIF" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Imaging-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Imaging Detector" ;
    schema1:description "BF, DF, SE STEM detectors; Gatan OneView 4096×4096 CMOS camera (HRTEM and electron diffraction)" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Monochromator> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Monochromator" ;
    schema1:name "missing" .


```


### temTAPP example Matsumoto2021
temTAPP instance derived from Matsumoto2021 | Lunar soil | BF/DF TEM + ADF-STEM + SAED (Jena FEI Tecnai G2 FEG).
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
  "@id": "ex:temTAPP-Matsumoto2021",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "tem protocol — Matsumoto2021",
  "schema:description": "Ar ion milling (Fischione NanoMill, ultra-low energy, Kyushu Univ) applied as additional cleaning step after FIB thinning Reported detail: ada:analyticalSubModeDefault = BF-TEM; DF-TEM; ADF-STEM; SAED (Electron Diffraction).",
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
            "Lunar soil grains (iron sulfides: troilite, NC-pyrrhotite; pyroxene; Apollo 11 soil 10084; Apollo 17 soil 78481,49)"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/temTAPP/samplePreparationDetailsDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "samplePreparationDetailsDefault",
            "schema:name": "Sample Preparation Details",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "FEI Helios NanoLab G3 CX (Kyoto Univ): e-beam Pt coating at 5 kV; Ga+ Pt coating at 30 kV; section thinned to ~100 nm at 30 kV Ga+; cleaned at 5 kV Ga+; additional Ar ion milling (Fischione NanoMill, ultra-low energy, Kyushu Univ)"
          }
        ],
        "schema:description": "FIB lift-out (Ga+)",
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
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:instrument": [
    {
      "schema:additionalType": [
        "TEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "ThermoFisher Scientific (FEI)",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "FEI Tecnai G2 FEG",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/TEM",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "4D-STEM Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/4D-STEM-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Aberration Corrector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Aberration-Corrector"
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
          "@id": "ex:instrument/TEM/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EELS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/EELS-Spectrometer"
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
          "@id": "ex:instrument/TEM/part/Electron-Source"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Imaging Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Imaging-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Monochromator",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Monochromator"
        }
      ],
      "schema:name": "example instrumentName"
    }
  ],
  "ada:analyticalSubModeDefault": "BF-TEM",
  "ada:phaseIdentificationMethod": "SAED indexing: BCC structure for metallic iron; troilite 2C superstructure reflections vs NiAs 1C base reflections; NC-pyrrhotite non-integral superstructure spots (NC values 3.6–6.5); dark-field imaging using specific reflections to image phase distributions",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "TEM/STEM"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Institute for Geosciences, Friedrich Schiller University Jena, Germany"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM (JSM-7001F); SEM-EDX (Oxford Inca X-act); FIB (FEI Helios NanoLab G3 CX)",
        "schema:description": "SEM (JSM-7001F, Kyushu Univ, 2.0 kV secondary electron imaging) surveyed grain surfaces and selected iron sulfide targets; SEM-EDX (Oxford Inca X-act) identified mineral phases on grain surface; FIB (FEI Helios NanoLab G3 CX, Kyoto Univ) prepared electron-transparent foil (e-beam Pt 5 kV + Ga+ Pt 30 kV; thinned to ~100 nm; cleaned at 5 kV Ga+); additional Ar ion milling (Fischione NanoMill, ultra-low energy, Kyushu Univ) performed after FIB"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:cameraLengthDefault": -9999,
  "ada:convergenceSemiAngle": -9999,
  "ada:edsAcquisitionModeDefault": "missing",
  "ada:edsCalibrationStandardDefault": "missing",
  "ada:edsQuantificationMethod": "missing",
  "ada:eelsAcquisitionModeDefault": "missing",
  "ada:eelsAcquisitionTimePerSpectrumDefault": -9999,
  "ada:eelsCollectionSemiAngle": -9999,
  "ada:eelsEnergyLossRangeDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:spectroscopicDetectorDefault": "missing",
  "ada:stemDwellTimePerPixelDefault": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/TEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:temTAPP-Matsumoto2021",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "tem protocol \u2014 Matsumoto2021",
  "schema:description": "Ar ion milling (Fischione NanoMill, ultra-low energy, Kyushu Univ) applied as additional cleaning step after FIB thinning Reported detail: ada:analyticalSubModeDefault = BF-TEM; DF-TEM; ADF-STEM; SAED (Electron Diffraction).",
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
            "Lunar soil grains (iron sulfides: troilite, NC-pyrrhotite; pyroxene; Apollo 11 soil 10084; Apollo 17 soil 78481,49)"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/temTAPP/samplePreparationDetailsDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "samplePreparationDetailsDefault",
            "schema:name": "Sample Preparation Details",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "FEI Helios NanoLab G3 CX (Kyoto Univ): e-beam Pt coating at 5 kV; Ga+ Pt coating at 30 kV; section thinned to ~100 nm at 30 kV Ga+; cleaned at 5 kV Ga+; additional Ar ion milling (Fischione NanoMill, ultra-low energy, Kyushu Univ)"
          }
        ],
        "schema:description": "FIB lift-out (Ga+)",
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
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:instrument": [
    {
      "schema:additionalType": [
        "TEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "ThermoFisher Scientific (FEI)",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "FEI Tecnai G2 FEG",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/TEM",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "4D-STEM Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/4D-STEM-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Aberration Corrector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Aberration-Corrector"
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
          "@id": "ex:instrument/TEM/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EELS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/EELS-Spectrometer"
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
          "@id": "ex:instrument/TEM/part/Electron-Source"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Imaging Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Imaging-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Monochromator",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Monochromator"
        }
      ],
      "schema:name": "example instrumentName"
    }
  ],
  "ada:analyticalSubModeDefault": "BF-TEM",
  "ada:phaseIdentificationMethod": "SAED indexing: BCC structure for metallic iron; troilite 2C superstructure reflections vs NiAs 1C base reflections; NC-pyrrhotite non-integral superstructure spots (NC values 3.6\u20136.5); dark-field imaging using specific reflections to image phase distributions",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "TEM/STEM"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Institute for Geosciences, Friedrich Schiller University Jena, Germany"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM (JSM-7001F); SEM-EDX (Oxford Inca X-act); FIB (FEI Helios NanoLab G3 CX)",
        "schema:description": "SEM (JSM-7001F, Kyushu Univ, 2.0 kV secondary electron imaging) surveyed grain surfaces and selected iron sulfide targets; SEM-EDX (Oxford Inca X-act) identified mineral phases on grain surface; FIB (FEI Helios NanoLab G3 CX, Kyoto Univ) prepared electron-transparent foil (e-beam Pt 5 kV + Ga+ Pt 30 kV; thinned to ~100 nm; cleaned at 5 kV Ga+); additional Ar ion milling (Fischione NanoMill, ultra-low energy, Kyushu Univ) performed after FIB"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:cameraLengthDefault": -9999,
  "ada:convergenceSemiAngle": -9999,
  "ada:edsAcquisitionModeDefault": "missing",
  "ada:edsCalibrationStandardDefault": "missing",
  "ada:edsQuantificationMethod": "missing",
  "ada:eelsAcquisitionModeDefault": "missing",
  "ada:eelsAcquisitionTimePerSpectrumDefault": -9999,
  "ada:eelsCollectionSemiAngle": -9999,
  "ada:eelsEnergyLossRangeDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:spectroscopicDetectorDefault": "missing",
  "ada:stemDwellTimePerPixelDefault": -9999,
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

ex:temTAPP-Matsumoto2021 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/temTAPP/samplePreparationDetailsDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "FIB lift-out (Ga+)" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "Ar ion milling (Fischione NanoMill, ultra-low energy, Kyushu Univ) applied as additional cleaning step after FIB thinning Reported detail: ada:analyticalSubModeDefault = BF-TEM; DF-TEM; ADF-STEM; SAED (Electron Diffraction)." ;
    schema1:instrument <https://example.org/instrument/TEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Institute for Geosciences, Friedrich Schiller University Jena, Germany" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "TEM/STEM" ] ;
    schema1:name "tem protocol — Matsumoto2021" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Lunar soil grains (iron sulfides: troilite, NC-pyrrhotite; pyroxene; Apollo 11 soil 10084; Apollo 17 soil 78481,49)" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "SEM (JSM-7001F, Kyushu Univ, 2.0 kV secondary electron imaging) surveyed grain surfaces and selected iron sulfide targets; SEM-EDX (Oxford Inca X-act) identified mineral phases on grain surface; FIB (FEI Helios NanoLab G3 CX, Kyoto Univ) prepared electron-transparent foil (e-beam Pt 5 kV + Ga+ Pt 30 kV; thinned to ~100 nm; cleaned at 5 kV Ga+); additional Ar ion milling (Fischione NanoMill, ultra-low energy, Kyushu Univ) performed after FIB" ;
                    schema1:name "SEM (JSM-7001F); SEM-EDX (Oxford Inca X-act); FIB (FEI Helios NanoLab G3 CX)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalSubModeDefault "BF-TEM" ;
    ada:cameraLengthDefault -9999 ;
    ada:convergenceSemiAngle -9999 ;
    ada:edsAcquisitionModeDefault "missing" ;
    ada:edsCalibrationStandardDefault "missing" ;
    ada:edsQuantificationMethod "missing" ;
    ada:eelsAcquisitionModeDefault "missing" ;
    ada:eelsAcquisitionTimePerSpectrumDefault -9999 ;
    ada:eelsCollectionSemiAngle -9999 ;
    ada:eelsEnergyLossRangeDefault "missing" ;
    ada:phaseIdentificationMethod "SAED indexing: BCC structure for metallic iron; troilite 2C superstructure reflections vs NiAs 1C base reflections; NC-pyrrhotite non-integral superstructure spots (NC values 3.6–6.5); dark-field imaging using specific reflections to image phase distributions" ;
    ada:samplingUnit "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:spectroscopicDetectorDefault "missing" ;
    ada:stemDwellTimePerPixelDefault -9999 .

<https://ada.astromat.org/metadata/parameter/temTAPP/samplePreparationDetailsDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "FEI Helios NanoLab G3 CX (Kyoto Univ): e-beam Pt coating at 5 kV; Ga+ Pt coating at 30 kV; section thinned to ~100 nm at 30 kV Ga+; cleaned at 5 kV Ga+; additional Ar ion milling (Fischione NanoMill, ultra-low energy, Kyushu Univ)" ;
    schema1:name "Sample Preparation Details" ;
    schema1:valueName "samplePreparationDetailsDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://example.org/instrument/TEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "TEM" ;
    schema1:hasPart <https://example.org/instrument/TEM/part/4D-STEM-Detector>,
        <https://example.org/instrument/TEM/part/Aberration-Corrector>,
        <https://example.org/instrument/TEM/part/EDS-Detector>,
        <https://example.org/instrument/TEM/part/EELS-Spectrometer>,
        <https://example.org/instrument/TEM/part/Electron-Source>,
        <https://example.org/instrument/TEM/part/Imaging-Detector>,
        <https://example.org/instrument/TEM/part/Monochromator> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "ThermoFisher Scientific (FEI)" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "FEI Tecnai G2 FEG" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/TEM/part/4D-STEM-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "4D-STEM Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Aberration-Corrector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Aberration Corrector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/EELS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EELS Spectrometer" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Imaging-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Imaging Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Monochromator> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Monochromator" ;
    schema1:name "missing" .


```


### temTAPP example Matsumoto2021-2
temTAPP instance derived from Matsumoto2021 | Lunar soil | TEM + EDS quantitative (Kyushu JEOL JEM-3200FSK).
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
  "@id": "ex:temTAPP-Matsumoto2021-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "tem protocol — Matsumoto2021-2",
  "schema:description": "k-factor standards: troilite (Cape York iron meteorite) for Fe and S; millerite (Sanany, Ural, Russia) for Ni and S; Ar ion milling (Fischione NanoMill, ultra-low energy, Kyushu Univ) applied as additional FIB section cleaning step Reported detail: ada:analyticalSubModeDefault = BF-TEM; ADF-STEM; STEM-EDS (line profiles; quantitative); ada:edsAcquisitionModeDefault = Line scan; quantitative point analysis; ada:edsQuantificationMethod = Cliff-Lorimer (thin film approximation); k-factors calibrated from reference standards.",
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
            "Lunar soil grains (iron sulfides: troilite, NC-pyrrhotite; pyroxene; Apollo 11 soil 10084; Apollo 17 soil 78481,49)"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/temTAPP/samplePreparationDetailsDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "samplePreparationDetailsDefault",
            "schema:name": "Sample Preparation Details",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "FEI Helios NanoLab G3 CX (Kyoto Univ): e-beam Pt coating at 5 kV; Ga+ Pt coating at 30 kV; section thinned to ~100 nm at 30 kV Ga+; cleaned at 5 kV Ga+; additional Ar ion milling (Fischione NanoMill, ultra-low energy, Kyushu Univ)"
          }
        ],
        "schema:description": "FIB lift-out (Ga+)",
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
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:instrument": [
    {
      "schema:additionalType": [
        "TEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "JEOL JEM-3200FSK",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "JEOL JED-2300 EDX detector",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/EDS-Detector",
          "schema:name": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "4D-STEM Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/4D-STEM-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Aberration Corrector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Aberration-Corrector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EELS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/EELS-Spectrometer"
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
          "@id": "ex:instrument/TEM/part/Electron-Source"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Imaging Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Imaging-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Monochromator",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Monochromator"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/TEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:spectroscopicDetectorDefault": "EDS only",
  "ada:analyticalSubModeDefault": "BF-TEM",
  "ada:edsAcquisitionModeDefault": "Line scan",
  "ada:edsQuantificationMethod": "Cliff-Lorimer (k-factor)",
  "ada:phaseIdentificationMethod": "Quantitative EDX (Cliff-Lorimer): Fe/S atomic ratio to distinguish troilite (Fe/S ≈ 1.03 ± 0.04) from NC-pyrrhotite; EDX maps used to confirm elemental distributions (Fe, S, O, Si, Ca)",
  "ada:edsCalibrationStandardDefault": "Troilite nodule from Cape York iron meteorite (Fe, S); terrestrial millerite from Sanany, Ural, Russia (Ni, S)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "TEM/STEM"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Ultramicroscopy Research Center, Kyushu University, Japan"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM (JSM-7001F); SEM-EDX (Oxford Inca X-act); FIB (FEI Helios NanoLab G3 CX)",
        "schema:description": "SEM (JSM-7001F, Kyushu Univ, 2.0 kV secondary electron imaging) surveyed grain surfaces and selected iron sulfide targets; SEM-EDX (Oxford Inca X-act) identified mineral phases on grain surface; FIB (FEI Helios NanoLab G3 CX, Kyoto Univ) prepared electron-transparent foil (e-beam Pt 5 kV + Ga+ Pt 30 kV; thinned to ~100 nm; cleaned at 5 kV Ga+); additional Ar ion milling (Fischione NanoMill, ultra-low energy, Kyushu Univ) performed after FIB"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:cameraLengthDefault": -9999,
  "ada:convergenceSemiAngle": -9999,
  "ada:eelsAcquisitionModeDefault": "missing",
  "ada:eelsAcquisitionTimePerSpectrumDefault": -9999,
  "ada:eelsCollectionSemiAngle": -9999,
  "ada:eelsEnergyLossRangeDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stemDwellTimePerPixelDefault": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/TEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:temTAPP-Matsumoto2021-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "tem protocol \u2014 Matsumoto2021-2",
  "schema:description": "k-factor standards: troilite (Cape York iron meteorite) for Fe and S; millerite (Sanany, Ural, Russia) for Ni and S; Ar ion milling (Fischione NanoMill, ultra-low energy, Kyushu Univ) applied as additional FIB section cleaning step Reported detail: ada:analyticalSubModeDefault = BF-TEM; ADF-STEM; STEM-EDS (line profiles; quantitative); ada:edsAcquisitionModeDefault = Line scan; quantitative point analysis; ada:edsQuantificationMethod = Cliff-Lorimer (thin film approximation); k-factors calibrated from reference standards.",
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
            "Lunar soil grains (iron sulfides: troilite, NC-pyrrhotite; pyroxene; Apollo 11 soil 10084; Apollo 17 soil 78481,49)"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/temTAPP/samplePreparationDetailsDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "samplePreparationDetailsDefault",
            "schema:name": "Sample Preparation Details",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "FEI Helios NanoLab G3 CX (Kyoto Univ): e-beam Pt coating at 5 kV; Ga+ Pt coating at 30 kV; section thinned to ~100 nm at 30 kV Ga+; cleaned at 5 kV Ga+; additional Ar ion milling (Fischione NanoMill, ultra-low energy, Kyushu Univ)"
          }
        ],
        "schema:description": "FIB lift-out (Ga+)",
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
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:instrument": [
    {
      "schema:additionalType": [
        "TEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "JEOL JEM-3200FSK",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "JEOL JED-2300 EDX detector",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/EDS-Detector",
          "schema:name": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "4D-STEM Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/4D-STEM-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Aberration Corrector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Aberration-Corrector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EELS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/EELS-Spectrometer"
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
          "@id": "ex:instrument/TEM/part/Electron-Source"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Imaging Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Imaging-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Monochromator",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Monochromator"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/TEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:spectroscopicDetectorDefault": "EDS only",
  "ada:analyticalSubModeDefault": "BF-TEM",
  "ada:edsAcquisitionModeDefault": "Line scan",
  "ada:edsQuantificationMethod": "Cliff-Lorimer (k-factor)",
  "ada:phaseIdentificationMethod": "Quantitative EDX (Cliff-Lorimer): Fe/S atomic ratio to distinguish troilite (Fe/S \u2248 1.03 \u00b1 0.04) from NC-pyrrhotite; EDX maps used to confirm elemental distributions (Fe, S, O, Si, Ca)",
  "ada:edsCalibrationStandardDefault": "Troilite nodule from Cape York iron meteorite (Fe, S); terrestrial millerite from Sanany, Ural, Russia (Ni, S)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "TEM/STEM"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Ultramicroscopy Research Center, Kyushu University, Japan"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM (JSM-7001F); SEM-EDX (Oxford Inca X-act); FIB (FEI Helios NanoLab G3 CX)",
        "schema:description": "SEM (JSM-7001F, Kyushu Univ, 2.0 kV secondary electron imaging) surveyed grain surfaces and selected iron sulfide targets; SEM-EDX (Oxford Inca X-act) identified mineral phases on grain surface; FIB (FEI Helios NanoLab G3 CX, Kyoto Univ) prepared electron-transparent foil (e-beam Pt 5 kV + Ga+ Pt 30 kV; thinned to ~100 nm; cleaned at 5 kV Ga+); additional Ar ion milling (Fischione NanoMill, ultra-low energy, Kyushu Univ) performed after FIB"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:cameraLengthDefault": -9999,
  "ada:convergenceSemiAngle": -9999,
  "ada:eelsAcquisitionModeDefault": "missing",
  "ada:eelsAcquisitionTimePerSpectrumDefault": -9999,
  "ada:eelsCollectionSemiAngle": -9999,
  "ada:eelsEnergyLossRangeDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stemDwellTimePerPixelDefault": -9999,
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

ex:temTAPP-Matsumoto2021-2 a cdi:Activity,
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
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/temTAPP/samplePreparationDetailsDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "FIB lift-out (Ga+)" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "k-factor standards: troilite (Cape York iron meteorite) for Fe and S; millerite (Sanany, Ural, Russia) for Ni and S; Ar ion milling (Fischione NanoMill, ultra-low energy, Kyushu Univ) applied as additional FIB section cleaning step Reported detail: ada:analyticalSubModeDefault = BF-TEM; ADF-STEM; STEM-EDS (line profiles; quantitative); ada:edsAcquisitionModeDefault = Line scan; quantitative point analysis; ada:edsQuantificationMethod = Cliff-Lorimer (thin film approximation); k-factors calibrated from reference standards." ;
    schema1:instrument <https://example.org/instrument/TEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Ultramicroscopy Research Center, Kyushu University, Japan" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "TEM/STEM" ] ;
    schema1:name "tem protocol — Matsumoto2021-2" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Lunar soil grains (iron sulfides: troilite, NC-pyrrhotite; pyroxene; Apollo 11 soil 10084; Apollo 17 soil 78481,49)" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "SEM (JSM-7001F, Kyushu Univ, 2.0 kV secondary electron imaging) surveyed grain surfaces and selected iron sulfide targets; SEM-EDX (Oxford Inca X-act) identified mineral phases on grain surface; FIB (FEI Helios NanoLab G3 CX, Kyoto Univ) prepared electron-transparent foil (e-beam Pt 5 kV + Ga+ Pt 30 kV; thinned to ~100 nm; cleaned at 5 kV Ga+); additional Ar ion milling (Fischione NanoMill, ultra-low energy, Kyushu Univ) performed after FIB" ;
                    schema1:name "SEM (JSM-7001F); SEM-EDX (Oxford Inca X-act); FIB (FEI Helios NanoLab G3 CX)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalSubModeDefault "BF-TEM" ;
    ada:cameraLengthDefault -9999 ;
    ada:convergenceSemiAngle -9999 ;
    ada:edsAcquisitionModeDefault "Line scan" ;
    ada:edsCalibrationStandardDefault "Troilite nodule from Cape York iron meteorite (Fe, S); terrestrial millerite from Sanany, Ural, Russia (Ni, S)" ;
    ada:edsQuantificationMethod "Cliff-Lorimer (k-factor)" ;
    ada:eelsAcquisitionModeDefault "missing" ;
    ada:eelsAcquisitionTimePerSpectrumDefault -9999 ;
    ada:eelsCollectionSemiAngle -9999 ;
    ada:eelsEnergyLossRangeDefault "missing" ;
    ada:phaseIdentificationMethod "Quantitative EDX (Cliff-Lorimer): Fe/S atomic ratio to distinguish troilite (Fe/S ≈ 1.03 ± 0.04) from NC-pyrrhotite; EDX maps used to confirm elemental distributions (Fe, S, O, Si, Ca)" ;
    ada:samplingUnit "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:spectroscopicDetectorDefault "EDS only" ;
    ada:stemDwellTimePerPixelDefault -9999 .

<https://ada.astromat.org/metadata/parameter/temTAPP/samplePreparationDetailsDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "FEI Helios NanoLab G3 CX (Kyoto Univ): e-beam Pt coating at 5 kV; Ga+ Pt coating at 30 kV; section thinned to ~100 nm at 30 kV Ga+; cleaned at 5 kV Ga+; additional Ar ion milling (Fischione NanoMill, ultra-low energy, Kyushu Univ)" ;
    schema1:name "Sample Preparation Details" ;
    schema1:valueName "samplePreparationDetailsDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://example.org/instrument/TEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "TEM" ;
    schema1:hasPart <https://example.org/instrument/TEM/part/4D-STEM-Detector>,
        <https://example.org/instrument/TEM/part/Aberration-Corrector>,
        <https://example.org/instrument/TEM/part/EDS-Detector>,
        <https://example.org/instrument/TEM/part/EELS-Spectrometer>,
        <https://example.org/instrument/TEM/part/Electron-Source>,
        <https://example.org/instrument/TEM/part/Imaging-Detector>,
        <https://example.org/instrument/TEM/part/Monochromator> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "JEOL" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "JEOL JEM-3200FSK" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/TEM/part/4D-STEM-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "4D-STEM Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Aberration-Corrector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Aberration Corrector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:description "JEOL JED-2300 EDX detector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/EELS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EELS Spectrometer" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Imaging-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Imaging Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Monochromator> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Monochromator" ;
    schema1:name "missing" .


```


### temTAPP example Matsumoto2021-3
temTAPP instance derived from Matsumoto2021 | Lunar soil | STEM-EDS mapping + HR-STEM (Kyushu JEOL JEM-ARM200F).
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
  "@id": "ex:temTAPP-Matsumoto2021-3",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "tem protocol — Matsumoto2021-3",
  "schema:description": "\"ARM\" designation implies probe Cs-correction (JEOL naming convention) but corrector type/details not stated; Ar ion milling (Fischione NanoMill, ultra-low energy, Kyushu Univ) applied as additional FIB section cleaning step Reported detail: ada:analyticalSubModeDefault = HAADF-STEM (ADF imaging); STEM-EDS (spectrum image map); HR-STEM; ada:edsAcquisitionModeDefault = Spectrum image (map).",
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
            "Lunar soil grains (iron sulfides: troilite, NC-pyrrhotite; pyroxene; Apollo 11 soil 10084; Apollo 17 soil 78481,49)"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/temTAPP/samplePreparationDetailsDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "samplePreparationDetailsDefault",
            "schema:name": "Sample Preparation Details",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "FEI Helios NanoLab G3 CX (Kyoto Univ): e-beam Pt coating at 5 kV; Ga+ Pt coating at 30 kV; section thinned to ~100 nm at 30 kV Ga+; cleaned at 5 kV Ga+; additional Ar ion milling (Fischione NanoMill, ultra-low energy, Kyushu Univ)"
          }
        ],
        "schema:description": "FIB lift-out (Ga+)",
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
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:instrument": [
    {
      "schema:additionalType": [
        "TEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "JEOL JEM-ARM200F",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "JEOL JED-2300T EDX detector",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/EDS-Detector",
          "schema:name": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "4D-STEM Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/4D-STEM-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Aberration Corrector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Aberration-Corrector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EELS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/EELS-Spectrometer"
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
          "@id": "ex:instrument/TEM/part/Electron-Source"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Imaging Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Imaging-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Monochromator",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Monochromator"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/TEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:spectroscopicDetectorDefault": "EDS only",
  "ada:analyticalSubModeDefault": "ADF",
  "ada:edsAcquisitionModeDefault": "Spectrum image",
  "ada:phaseIdentificationMethod": "HR-STEM + FFT: imaging of (001) plane stacking and distortions in iron sulfides; qualitative lattice fringe analysis (no explicit d-spacing phase matching stated)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "TEM/STEM"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Ultramicroscopy Research Center, Kyushu University, Japan"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM (JSM-7001F); SEM-EDX (Oxford Inca X-act); FIB (FEI Helios NanoLab G3 CX)",
        "schema:description": "SEM (JSM-7001F, Kyushu Univ, 2.0 kV secondary electron imaging) surveyed grain surfaces and selected iron sulfide targets; SEM-EDX (Oxford Inca X-act) identified mineral phases on grain surface; FIB (FEI Helios NanoLab G3 CX, Kyoto Univ) prepared electron-transparent foil (e-beam Pt 5 kV + Ga+ Pt 30 kV; thinned to ~100 nm; cleaned at 5 kV Ga+); additional Ar ion milling (Fischione NanoMill, ultra-low energy, Kyushu Univ) performed after FIB"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:cameraLengthDefault": -9999,
  "ada:convergenceSemiAngle": -9999,
  "ada:edsCalibrationStandardDefault": "missing",
  "ada:edsQuantificationMethod": "missing",
  "ada:eelsAcquisitionModeDefault": "missing",
  "ada:eelsAcquisitionTimePerSpectrumDefault": -9999,
  "ada:eelsCollectionSemiAngle": -9999,
  "ada:eelsEnergyLossRangeDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stemDwellTimePerPixelDefault": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/TEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:temTAPP-Matsumoto2021-3",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "tem protocol \u2014 Matsumoto2021-3",
  "schema:description": "\"ARM\" designation implies probe Cs-correction (JEOL naming convention) but corrector type/details not stated; Ar ion milling (Fischione NanoMill, ultra-low energy, Kyushu Univ) applied as additional FIB section cleaning step Reported detail: ada:analyticalSubModeDefault = HAADF-STEM (ADF imaging); STEM-EDS (spectrum image map); HR-STEM; ada:edsAcquisitionModeDefault = Spectrum image (map).",
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
            "Lunar soil grains (iron sulfides: troilite, NC-pyrrhotite; pyroxene; Apollo 11 soil 10084; Apollo 17 soil 78481,49)"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/temTAPP/samplePreparationDetailsDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "samplePreparationDetailsDefault",
            "schema:name": "Sample Preparation Details",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "FEI Helios NanoLab G3 CX (Kyoto Univ): e-beam Pt coating at 5 kV; Ga+ Pt coating at 30 kV; section thinned to ~100 nm at 30 kV Ga+; cleaned at 5 kV Ga+; additional Ar ion milling (Fischione NanoMill, ultra-low energy, Kyushu Univ)"
          }
        ],
        "schema:description": "FIB lift-out (Ga+)",
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
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:instrument": [
    {
      "schema:additionalType": [
        "TEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "JEOL JEM-ARM200F",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "JEOL JED-2300T EDX detector",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/EDS-Detector",
          "schema:name": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "4D-STEM Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/4D-STEM-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Aberration Corrector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Aberration-Corrector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EELS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/EELS-Spectrometer"
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
          "@id": "ex:instrument/TEM/part/Electron-Source"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Imaging Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Imaging-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Monochromator",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Monochromator"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/TEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:spectroscopicDetectorDefault": "EDS only",
  "ada:analyticalSubModeDefault": "ADF",
  "ada:edsAcquisitionModeDefault": "Spectrum image",
  "ada:phaseIdentificationMethod": "HR-STEM + FFT: imaging of (001) plane stacking and distortions in iron sulfides; qualitative lattice fringe analysis (no explicit d-spacing phase matching stated)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "TEM/STEM"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Ultramicroscopy Research Center, Kyushu University, Japan"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM (JSM-7001F); SEM-EDX (Oxford Inca X-act); FIB (FEI Helios NanoLab G3 CX)",
        "schema:description": "SEM (JSM-7001F, Kyushu Univ, 2.0 kV secondary electron imaging) surveyed grain surfaces and selected iron sulfide targets; SEM-EDX (Oxford Inca X-act) identified mineral phases on grain surface; FIB (FEI Helios NanoLab G3 CX, Kyoto Univ) prepared electron-transparent foil (e-beam Pt 5 kV + Ga+ Pt 30 kV; thinned to ~100 nm; cleaned at 5 kV Ga+); additional Ar ion milling (Fischione NanoMill, ultra-low energy, Kyushu Univ) performed after FIB"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:cameraLengthDefault": -9999,
  "ada:convergenceSemiAngle": -9999,
  "ada:edsCalibrationStandardDefault": "missing",
  "ada:edsQuantificationMethod": "missing",
  "ada:eelsAcquisitionModeDefault": "missing",
  "ada:eelsAcquisitionTimePerSpectrumDefault": -9999,
  "ada:eelsCollectionSemiAngle": -9999,
  "ada:eelsEnergyLossRangeDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stemDwellTimePerPixelDefault": -9999,
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

ex:temTAPP-Matsumoto2021-3 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/temTAPP/samplePreparationDetailsDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "FIB lift-out (Ga+)" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "\"ARM\" designation implies probe Cs-correction (JEOL naming convention) but corrector type/details not stated; Ar ion milling (Fischione NanoMill, ultra-low energy, Kyushu Univ) applied as additional FIB section cleaning step Reported detail: ada:analyticalSubModeDefault = HAADF-STEM (ADF imaging); STEM-EDS (spectrum image map); HR-STEM; ada:edsAcquisitionModeDefault = Spectrum image (map)." ;
    schema1:instrument <https://example.org/instrument/TEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Ultramicroscopy Research Center, Kyushu University, Japan" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "TEM/STEM" ] ;
    schema1:name "tem protocol — Matsumoto2021-3" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Lunar soil grains (iron sulfides: troilite, NC-pyrrhotite; pyroxene; Apollo 11 soil 10084; Apollo 17 soil 78481,49)" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "SEM (JSM-7001F, Kyushu Univ, 2.0 kV secondary electron imaging) surveyed grain surfaces and selected iron sulfide targets; SEM-EDX (Oxford Inca X-act) identified mineral phases on grain surface; FIB (FEI Helios NanoLab G3 CX, Kyoto Univ) prepared electron-transparent foil (e-beam Pt 5 kV + Ga+ Pt 30 kV; thinned to ~100 nm; cleaned at 5 kV Ga+); additional Ar ion milling (Fischione NanoMill, ultra-low energy, Kyushu Univ) performed after FIB" ;
                    schema1:name "SEM (JSM-7001F); SEM-EDX (Oxford Inca X-act); FIB (FEI Helios NanoLab G3 CX)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalSubModeDefault "ADF" ;
    ada:cameraLengthDefault -9999 ;
    ada:convergenceSemiAngle -9999 ;
    ada:edsAcquisitionModeDefault "Spectrum image" ;
    ada:edsCalibrationStandardDefault "missing" ;
    ada:edsQuantificationMethod "missing" ;
    ada:eelsAcquisitionModeDefault "missing" ;
    ada:eelsAcquisitionTimePerSpectrumDefault -9999 ;
    ada:eelsCollectionSemiAngle -9999 ;
    ada:eelsEnergyLossRangeDefault "missing" ;
    ada:phaseIdentificationMethod "HR-STEM + FFT: imaging of (001) plane stacking and distortions in iron sulfides; qualitative lattice fringe analysis (no explicit d-spacing phase matching stated)" ;
    ada:samplingUnit "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:spectroscopicDetectorDefault "EDS only" ;
    ada:stemDwellTimePerPixelDefault -9999 .

<https://ada.astromat.org/metadata/parameter/temTAPP/samplePreparationDetailsDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "FEI Helios NanoLab G3 CX (Kyoto Univ): e-beam Pt coating at 5 kV; Ga+ Pt coating at 30 kV; section thinned to ~100 nm at 30 kV Ga+; cleaned at 5 kV Ga+; additional Ar ion milling (Fischione NanoMill, ultra-low energy, Kyushu Univ)" ;
    schema1:name "Sample Preparation Details" ;
    schema1:valueName "samplePreparationDetailsDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://example.org/instrument/TEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "TEM" ;
    schema1:hasPart <https://example.org/instrument/TEM/part/4D-STEM-Detector>,
        <https://example.org/instrument/TEM/part/Aberration-Corrector>,
        <https://example.org/instrument/TEM/part/EDS-Detector>,
        <https://example.org/instrument/TEM/part/EELS-Spectrometer>,
        <https://example.org/instrument/TEM/part/Electron-Source>,
        <https://example.org/instrument/TEM/part/Imaging-Detector>,
        <https://example.org/instrument/TEM/part/Monochromator> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "JEOL" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "JEOL JEM-ARM200F" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/TEM/part/4D-STEM-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "4D-STEM Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Aberration-Corrector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Aberration Corrector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:description "JEOL JED-2300T EDX detector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/EELS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EELS Spectrometer" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Imaging-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Imaging Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Monochromator> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Monochromator" ;
    schema1:name "missing" .


```


### temTAPP example KellerBerger2014
temTAPP instance derived from KellerBerger2014 | Itokawa regolith grains | STEM + EDS spectrum imaging (JSC JEOL 2500SE).
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
  "@id": "ex:temTAPP-KellerBerger2014",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "tem protocol — KellerBerger2014",
  "schema:description": "Incident probe diameter 4 nm for spectrum imaging (9 nA); EDS spectrum images: successive layers combined for >10% counting statistics per pixel; solar flare track density ~2×10¹⁰ cm⁻² in RA-QD02-0211 Reported detail: ada:analyticalSubModeDefault = BF-STEM; DF-STEM; HRTEM (TEM Imaging); SAED (Electron Diffraction); STEM-EDS (spectrum imaging); ada:edsAcquisitionModeDefault = Spectrum image (map); line profile.",
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
            "Itokawa olivine regolith grains (RA-QD02-0125, ~37 µm olivine single crystal; RA-QD02-0211, ~41 µm olivine single crystal); comparison: Apollo 17 lunar soil 71501 olivine grains (20–45 µm fraction)"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/temTAPP/samplePreparationDetailsDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "samplePreparationDetailsDefault",
            "schema:name": "Sample Preparation Details",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Particles embedded in low-viscosity epoxy; thin sections ~60 nm thick prepared by ultramicrotomy"
          }
        ],
        "schema:description": "Ultramicrotomy",
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
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:instrument": [
    {
      "schema:additionalType": [
        "TEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "JEOL 2500SE 200-kV STEM",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Thermo-Noran thin-window energy-dispersive X-ray (EDX) spectrometer",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/EDS-Detector",
          "schema:name": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "4D-STEM Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/4D-STEM-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Aberration Corrector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Aberration-Corrector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EELS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/EELS-Spectrometer"
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
          "@id": "ex:instrument/TEM/part/Electron-Source"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Imaging Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Imaging-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Monochromator",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Monochromator"
        }
      ],
      "ada:acceleratingVoltageDefault": "200 kV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/TEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:spectroscopicDetectorDefault": "EDS only",
  "ada:analyticalSubModeDefault": "BF-STEM",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/temTAPP/stemProbeDiameterDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "stemProbeDiameterDefault",
      "schema:name": "STEM Probe Diameter",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 4,
      "schema:description": "4 nm"
    },
    {
      "@id": "ada:parameter/temTAPP/stemProbeCurrentDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "stemProbeCurrentDefault",
      "schema:name": "STEM Probe Current",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 9,
      "schema:description": "9 nA"
    },
    {
      "@id": "ada:parameter/temTAPP/stemScanDimensionsDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "stemScanDimensionsDefault",
      "schema:name": "STEM Scan Dimensions",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 256,
      "schema:description": "256 × 204 pixels (typical; optimized to limit over- or under-sampling with 4-nm probe)"
    },
    {
      "@id": "ada:parameter/temTAPP/stemFrameAveragingDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "stemFrameAveragingDefault",
      "schema:name": "STEM Frame Averaging",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Multiple consecutive spectrum image layers accumulated (target: >10% counting statistics per pixel for major elements)"
    },
    {
      "@id": "ada:parameter/temTAPP/edsCountingStatisticsAccumulationCriterionDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "edsCountingStatisticsAccumulationCriterionDefault",
      "schema:name": "EDS Counting Statistics / Accumulation Criterion",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Successive layers averaged for >10% counting statistics"
    }
  ],
  "ada:stemDwellTimePerPixelDefault": "50 µs/pixel",
  "ada:edsAcquisitionModeDefault": "Spectrum image",
  "ada:phaseIdentificationMethod": "HRTEM lattice fringes + SAED: metallic npFe0 grains (<5 nm) identified by bcc iron d-spacings (Fig. 6 FFT: iron 110 spacings); pyrrhotite superstructure reflections present in core and absent in disordered rim (SAED + FFT); olivine composition by TEM-EDX (Fo70)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "TEM/STEM"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Robert M. Walker Laboratory for Space Science, Code KR, Astromaterials Research and Exploration Science (ARES), NASA Johnson Space Center"
  },
  "ada:cameraLengthDefault": -9999,
  "ada:convergenceSemiAngle": -9999,
  "ada:edsCalibrationStandardDefault": "missing",
  "ada:edsQuantificationMethod": "missing",
  "ada:eelsAcquisitionModeDefault": "missing",
  "ada:eelsAcquisitionTimePerSpectrumDefault": -9999,
  "ada:eelsCollectionSemiAngle": -9999,
  "ada:eelsEnergyLossRangeDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/TEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:temTAPP-KellerBerger2014",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "tem protocol \u2014 KellerBerger2014",
  "schema:description": "Incident probe diameter 4 nm for spectrum imaging (9 nA); EDS spectrum images: successive layers combined for >10% counting statistics per pixel; solar flare track density ~2\u00d710\u00b9\u2070 cm\u207b\u00b2 in RA-QD02-0211 Reported detail: ada:analyticalSubModeDefault = BF-STEM; DF-STEM; HRTEM (TEM Imaging); SAED (Electron Diffraction); STEM-EDS (spectrum imaging); ada:edsAcquisitionModeDefault = Spectrum image (map); line profile.",
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
            "Itokawa olivine regolith grains (RA-QD02-0125, ~37 \u00b5m olivine single crystal; RA-QD02-0211, ~41 \u00b5m olivine single crystal); comparison: Apollo 17 lunar soil 71501 olivine grains (20\u201345 \u00b5m fraction)"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/temTAPP/samplePreparationDetailsDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "samplePreparationDetailsDefault",
            "schema:name": "Sample Preparation Details",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Particles embedded in low-viscosity epoxy; thin sections ~60 nm thick prepared by ultramicrotomy"
          }
        ],
        "schema:description": "Ultramicrotomy",
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
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:instrument": [
    {
      "schema:additionalType": [
        "TEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "JEOL 2500SE 200-kV STEM",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Thermo-Noran thin-window energy-dispersive X-ray (EDX) spectrometer",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/EDS-Detector",
          "schema:name": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "4D-STEM Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/4D-STEM-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Aberration Corrector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Aberration-Corrector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EELS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/EELS-Spectrometer"
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
          "@id": "ex:instrument/TEM/part/Electron-Source"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Imaging Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Imaging-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Monochromator",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Monochromator"
        }
      ],
      "ada:acceleratingVoltageDefault": "200 kV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/TEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:spectroscopicDetectorDefault": "EDS only",
  "ada:analyticalSubModeDefault": "BF-STEM",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/temTAPP/stemProbeDiameterDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "stemProbeDiameterDefault",
      "schema:name": "STEM Probe Diameter",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 4,
      "schema:description": "4 nm"
    },
    {
      "@id": "ada:parameter/temTAPP/stemProbeCurrentDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "stemProbeCurrentDefault",
      "schema:name": "STEM Probe Current",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 9,
      "schema:description": "9 nA"
    },
    {
      "@id": "ada:parameter/temTAPP/stemScanDimensionsDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "stemScanDimensionsDefault",
      "schema:name": "STEM Scan Dimensions",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 256,
      "schema:description": "256 \u00d7 204 pixels (typical; optimized to limit over- or under-sampling with 4-nm probe)"
    },
    {
      "@id": "ada:parameter/temTAPP/stemFrameAveragingDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "stemFrameAveragingDefault",
      "schema:name": "STEM Frame Averaging",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Multiple consecutive spectrum image layers accumulated (target: >10% counting statistics per pixel for major elements)"
    },
    {
      "@id": "ada:parameter/temTAPP/edsCountingStatisticsAccumulationCriterionDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "edsCountingStatisticsAccumulationCriterionDefault",
      "schema:name": "EDS Counting Statistics / Accumulation Criterion",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Successive layers averaged for >10% counting statistics"
    }
  ],
  "ada:stemDwellTimePerPixelDefault": "50 \u00b5s/pixel",
  "ada:edsAcquisitionModeDefault": "Spectrum image",
  "ada:phaseIdentificationMethod": "HRTEM lattice fringes + SAED: metallic npFe0 grains (<5 nm) identified by bcc iron d-spacings (Fig. 6 FFT: iron 110 spacings); pyrrhotite superstructure reflections present in core and absent in disordered rim (SAED + FFT); olivine composition by TEM-EDX (Fo70)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "TEM/STEM"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Robert M. Walker Laboratory for Space Science, Code KR, Astromaterials Research and Exploration Science (ARES), NASA Johnson Space Center"
  },
  "ada:cameraLengthDefault": -9999,
  "ada:convergenceSemiAngle": -9999,
  "ada:edsCalibrationStandardDefault": "missing",
  "ada:edsQuantificationMethod": "missing",
  "ada:eelsAcquisitionModeDefault": "missing",
  "ada:eelsAcquisitionTimePerSpectrumDefault": -9999,
  "ada:eelsCollectionSemiAngle": -9999,
  "ada:eelsEnergyLossRangeDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
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

ex:temTAPP-KellerBerger2014 a cdi:Activity,
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
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/temTAPP/samplePreparationDetailsDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Ultramicrotomy" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/temTAPP/edsCountingStatisticsAccumulationCriterionDefault>,
        <https://ada.astromat.org/metadata/parameter/temTAPP/stemFrameAveragingDefault>,
        <https://ada.astromat.org/metadata/parameter/temTAPP/stemProbeCurrentDefault>,
        <https://ada.astromat.org/metadata/parameter/temTAPP/stemProbeDiameterDefault>,
        <https://ada.astromat.org/metadata/parameter/temTAPP/stemScanDimensionsDefault> ;
    schema1:datePublished "missing" ;
    schema1:description "Incident probe diameter 4 nm for spectrum imaging (9 nA); EDS spectrum images: successive layers combined for >10% counting statistics per pixel; solar flare track density ~2×10¹⁰ cm⁻² in RA-QD02-0211 Reported detail: ada:analyticalSubModeDefault = BF-STEM; DF-STEM; HRTEM (TEM Imaging); SAED (Electron Diffraction); STEM-EDS (spectrum imaging); ada:edsAcquisitionModeDefault = Spectrum image (map); line profile." ;
    schema1:instrument <https://example.org/instrument/TEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Robert M. Walker Laboratory for Space Science, Code KR, Astromaterials Research and Exploration Science (ARES), NASA Johnson Space Center" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "TEM/STEM" ] ;
    schema1:name "tem protocol — KellerBerger2014" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Itokawa olivine regolith grains (RA-QD02-0125, ~37 µm olivine single crystal; RA-QD02-0211, ~41 µm olivine single crystal); comparison: Apollo 17 lunar soil 71501 olivine grains (20–45 µm fraction)" ] ] ;
    ada:analyticalSubModeDefault "BF-STEM" ;
    ada:cameraLengthDefault -9999 ;
    ada:convergenceSemiAngle -9999 ;
    ada:edsAcquisitionModeDefault "Spectrum image" ;
    ada:edsCalibrationStandardDefault "missing" ;
    ada:edsQuantificationMethod "missing" ;
    ada:eelsAcquisitionModeDefault "missing" ;
    ada:eelsAcquisitionTimePerSpectrumDefault -9999 ;
    ada:eelsCollectionSemiAngle -9999 ;
    ada:eelsEnergyLossRangeDefault "missing" ;
    ada:phaseIdentificationMethod "HRTEM lattice fringes + SAED: metallic npFe0 grains (<5 nm) identified by bcc iron d-spacings (Fig. 6 FFT: iron 110 spacings); pyrrhotite superstructure reflections present in core and absent in disordered rim (SAED + FFT); olivine composition by TEM-EDX (Fo70)" ;
    ada:samplingUnit "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:spectroscopicDetectorDefault "EDS only" ;
    ada:stemDwellTimePerPixelDefault "50 µs/pixel" .

<https://ada.astromat.org/metadata/parameter/temTAPP/edsCountingStatisticsAccumulationCriterionDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Successive layers averaged for >10% counting statistics" ;
    schema1:name "EDS Counting Statistics / Accumulation Criterion" ;
    schema1:valueName "edsCountingStatisticsAccumulationCriterionDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/temTAPP/samplePreparationDetailsDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Particles embedded in low-viscosity epoxy; thin sections ~60 nm thick prepared by ultramicrotomy" ;
    schema1:name "Sample Preparation Details" ;
    schema1:valueName "samplePreparationDetailsDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/temTAPP/stemFrameAveragingDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Multiple consecutive spectrum image layers accumulated (target: >10% counting statistics per pixel for major elements)" ;
    schema1:name "STEM Frame Averaging" ;
    schema1:valueName "stemFrameAveragingDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/temTAPP/stemProbeCurrentDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 9 ;
    schema1:description "9 nA" ;
    schema1:name "STEM Probe Current" ;
    schema1:valueName "stemProbeCurrentDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/temTAPP/stemProbeDiameterDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 4 ;
    schema1:description "4 nm" ;
    schema1:name "STEM Probe Diameter" ;
    schema1:valueName "stemProbeDiameterDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/temTAPP/stemScanDimensionsDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 256 ;
    schema1:description "256 × 204 pixels (typical; optimized to limit over- or under-sampling with 4-nm probe)" ;
    schema1:name "STEM Scan Dimensions" ;
    schema1:valueName "stemScanDimensionsDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://example.org/instrument/TEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "TEM" ;
    schema1:hasPart <https://example.org/instrument/TEM/part/4D-STEM-Detector>,
        <https://example.org/instrument/TEM/part/Aberration-Corrector>,
        <https://example.org/instrument/TEM/part/EDS-Detector>,
        <https://example.org/instrument/TEM/part/EELS-Spectrometer>,
        <https://example.org/instrument/TEM/part/Electron-Source>,
        <https://example.org/instrument/TEM/part/Imaging-Detector>,
        <https://example.org/instrument/TEM/part/Monochromator> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "JEOL" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "JEOL 2500SE 200-kV STEM" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "200 kV" .

<https://example.org/instrument/TEM/part/4D-STEM-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "4D-STEM Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Aberration-Corrector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Aberration Corrector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:description "Thermo-Noran thin-window energy-dispersive X-ray (EDX) spectrometer" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/EELS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EELS Spectrometer" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Imaging-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Imaging Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Monochromator> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Monochromator" ;
    schema1:name "missing" .


```


### temTAPP example Zeng2024
temTAPP instance derived from Zeng2024 | Chang'e-5 lunar glass bead | HAADF-STEM + EDS mapping (Guangdong FEI Talos F200S).
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
  "@id": "ex:temTAPP-Zeng2024",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "tem protocol — Zeng2024",
  "schema:description": "EDS quantification via Velox 2.14 using Brown-Powell ionization cross-section model; FIB foil preparation and STEM imaging at 30 kV/0.4 nA also performed on FEI Scios FIB/SEM (Institute of Geochemistry, CAS) as a coupled step prior to TEM analysis on Talos F200S Reported detail: ada:analyticalSubModeDefault = BF-TEM; HAADF-STEM; STEM-EDS (X-ray mapping); ada:edsAcquisitionModeDefault = Spectrum image (map).",
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
            "Chang'e-5 lunar glass bead (basaltic impact glass, ~350×400 µm; CE5C0600YJFM00304; micrometeorite impact crater rim)"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/temTAPP/samplePreparationDetailsDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "samplePreparationDetailsDefault",
            "schema:name": "Sample Preparation Details",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "FEI Scios dual-beam FIB/SEM (Institute of Geochemistry, CAS): glass bead coated with gold prior to FIB; FIB slice ~15 µm length × ~10 µm width × 90–100 nm thick; 30 kV, 0.4 nA beam current"
          }
        ],
        "schema:description": "FIB lift-out (Ga+)",
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
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:instrument": [
    {
      "schema:additionalType": [
        "TEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "ThermoFisher Scientific (FEI)",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "FEI Talos F200S",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Bruker xflash 6T 30 silicon drift detector",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/EDS-Detector",
          "schema:name": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "4D-STEM Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/4D-STEM-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Aberration Corrector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Aberration-Corrector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EELS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/EELS-Spectrometer"
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
          "@id": "ex:instrument/TEM/part/Electron-Source"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Imaging Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Imaging-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Monochromator",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Monochromator"
        }
      ],
      "ada:acceleratingVoltageDefault": "200 kV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/TEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:spectroscopicDetectorDefault": "EDS only",
  "ada:analyticalSubModeDefault": "BF-TEM",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/temTAPP/stemProbeCurrentDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "stemProbeCurrentDefault",
      "schema:name": "STEM Probe Current",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 1,
      "schema:description": "1–2 nA (stated as beam current for analysis conditions)"
    }
  ],
  "ada:edsAcquisitionModeDefault": "Spectrum image",
  "ada:edsQuantificationMethod": "Brown–Powell ionization cross-section model (implemented in Velox 2.14)",
  "ada:phaseIdentificationMethod": "FFT from BF-TEM images (no SAED): rutile (TiO2, polycrystalline 2–15 nm); trigonal Ti2O (P3̄m1, zone axis [1 1 2̄ 3]; a=2.983 Å, c=4.804 Å); triclinic Ti2O (P1, zone axis [5 16 12]; a=10.453 Å, b=10.895 Å, c=12.206 Å); d-spacings and zone axes matched to crystal structure parameters",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "TEM/STEM"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Analysis and Test Center, Guangdong University of Technology, Guangzhou, China"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "FIB-SEM (FEI Scios dual-beam); SEM-BSE; SEM-EDS",
        "schema:description": "FEI Scios dual-beam FIB/SEM (Institute of Geochemistry, CAS, Guiyang): BSE and SE imaging at 5 kV/0.8 nA (7 mm WD); EDS mapping at 20 kV/1.6 nA; FIB foil preparation at 30 kV/0.4 nA; STEM imaging of FIB slice at 30 kV/0.4 nA using the same FIB/SEM instrument (all performed prior to TEM on Talos F200S)"
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
      "schema:name": "Velox Revision 2.14 (Thermo Fisher Scientific)"
    },
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Velox Revision 2.14 (Thermo Fisher Scientific)"
    }
  ],
  "ada:cameraLengthDefault": -9999,
  "ada:convergenceSemiAngle": -9999,
  "ada:edsCalibrationStandardDefault": "missing",
  "ada:eelsAcquisitionModeDefault": "missing",
  "ada:eelsAcquisitionTimePerSpectrumDefault": -9999,
  "ada:eelsCollectionSemiAngle": -9999,
  "ada:eelsEnergyLossRangeDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stemDwellTimePerPixelDefault": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/TEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:temTAPP-Zeng2024",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "tem protocol \u2014 Zeng2024",
  "schema:description": "EDS quantification via Velox 2.14 using Brown-Powell ionization cross-section model; FIB foil preparation and STEM imaging at 30 kV/0.4 nA also performed on FEI Scios FIB/SEM (Institute of Geochemistry, CAS) as a coupled step prior to TEM analysis on Talos F200S Reported detail: ada:analyticalSubModeDefault = BF-TEM; HAADF-STEM; STEM-EDS (X-ray mapping); ada:edsAcquisitionModeDefault = Spectrum image (map).",
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
            "Chang'e-5 lunar glass bead (basaltic impact glass, ~350\u00d7400 \u00b5m; CE5C0600YJFM00304; micrometeorite impact crater rim)"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/temTAPP/samplePreparationDetailsDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "samplePreparationDetailsDefault",
            "schema:name": "Sample Preparation Details",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "FEI Scios dual-beam FIB/SEM (Institute of Geochemistry, CAS): glass bead coated with gold prior to FIB; FIB slice ~15 \u00b5m length \u00d7 ~10 \u00b5m width \u00d7 90\u2013100 nm thick; 30 kV, 0.4 nA beam current"
          }
        ],
        "schema:description": "FIB lift-out (Ga+)",
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
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:instrument": [
    {
      "schema:additionalType": [
        "TEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "ThermoFisher Scientific (FEI)",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "FEI Talos F200S",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Bruker xflash 6T 30 silicon drift detector",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/EDS-Detector",
          "schema:name": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "4D-STEM Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/4D-STEM-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Aberration Corrector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Aberration-Corrector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EELS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/EELS-Spectrometer"
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
          "@id": "ex:instrument/TEM/part/Electron-Source"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Imaging Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Imaging-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Monochromator",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Monochromator"
        }
      ],
      "ada:acceleratingVoltageDefault": "200 kV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/TEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:spectroscopicDetectorDefault": "EDS only",
  "ada:analyticalSubModeDefault": "BF-TEM",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/temTAPP/stemProbeCurrentDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "stemProbeCurrentDefault",
      "schema:name": "STEM Probe Current",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 1,
      "schema:description": "1\u20132 nA (stated as beam current for analysis conditions)"
    }
  ],
  "ada:edsAcquisitionModeDefault": "Spectrum image",
  "ada:edsQuantificationMethod": "Brown\u2013Powell ionization cross-section model (implemented in Velox 2.14)",
  "ada:phaseIdentificationMethod": "FFT from BF-TEM images (no SAED): rutile (TiO2, polycrystalline 2\u201315 nm); trigonal Ti2O (P3\u0304m1, zone axis [1 1 2\u0304 3]; a=2.983 \u00c5, c=4.804 \u00c5); triclinic Ti2O (P1, zone axis [5 16 12]; a=10.453 \u00c5, b=10.895 \u00c5, c=12.206 \u00c5); d-spacings and zone axes matched to crystal structure parameters",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "TEM/STEM"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Analysis and Test Center, Guangdong University of Technology, Guangzhou, China"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "FIB-SEM (FEI Scios dual-beam); SEM-BSE; SEM-EDS",
        "schema:description": "FEI Scios dual-beam FIB/SEM (Institute of Geochemistry, CAS, Guiyang): BSE and SE imaging at 5 kV/0.8 nA (7 mm WD); EDS mapping at 20 kV/1.6 nA; FIB foil preparation at 30 kV/0.4 nA; STEM imaging of FIB slice at 30 kV/0.4 nA using the same FIB/SEM instrument (all performed prior to TEM on Talos F200S)"
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
      "schema:name": "Velox Revision 2.14 (Thermo Fisher Scientific)"
    },
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Velox Revision 2.14 (Thermo Fisher Scientific)"
    }
  ],
  "ada:cameraLengthDefault": -9999,
  "ada:convergenceSemiAngle": -9999,
  "ada:edsCalibrationStandardDefault": "missing",
  "ada:eelsAcquisitionModeDefault": "missing",
  "ada:eelsAcquisitionTimePerSpectrumDefault": -9999,
  "ada:eelsCollectionSemiAngle": -9999,
  "ada:eelsEnergyLossRangeDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stemDwellTimePerPixelDefault": -9999,
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

ex:temTAPP-Zeng2024 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/temTAPP/samplePreparationDetailsDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "FIB lift-out (Ga+)" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/temTAPP/stemProbeCurrentDefault> ;
    schema1:datePublished "missing" ;
    schema1:description "EDS quantification via Velox 2.14 using Brown-Powell ionization cross-section model; FIB foil preparation and STEM imaging at 30 kV/0.4 nA also performed on FEI Scios FIB/SEM (Institute of Geochemistry, CAS) as a coupled step prior to TEM analysis on Talos F200S Reported detail: ada:analyticalSubModeDefault = BF-TEM; HAADF-STEM; STEM-EDS (X-ray mapping); ada:edsAcquisitionModeDefault = Spectrum image (map)." ;
    schema1:instrument <https://example.org/instrument/TEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Analysis and Test Center, Guangdong University of Technology, Guangzhou, China" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "TEM/STEM" ] ;
    schema1:name "tem protocol — Zeng2024" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Chang'e-5 lunar glass bead (basaltic impact glass, ~350×400 µm; CE5C0600YJFM00304; micrometeorite impact crater rim)" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "FEI Scios dual-beam FIB/SEM (Institute of Geochemistry, CAS, Guiyang): BSE and SE imaging at 5 kV/0.8 nA (7 mm WD); EDS mapping at 20 kV/1.6 nA; FIB foil preparation at 30 kV/0.4 nA; STEM imaging of FIB slice at 30 kV/0.4 nA using the same FIB/SEM instrument (all performed prior to TEM on Talos F200S)" ;
                    schema1:name "FIB-SEM (FEI Scios dual-beam); SEM-BSE; SEM-EDS" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalSubModeDefault "BF-TEM" ;
    ada:cameraLengthDefault -9999 ;
    ada:convergenceSemiAngle -9999 ;
    ada:edsAcquisitionModeDefault "Spectrum image" ;
    ada:edsCalibrationStandardDefault "missing" ;
    ada:edsQuantificationMethod "Brown–Powell ionization cross-section model (implemented in Velox 2.14)" ;
    ada:eelsAcquisitionModeDefault "missing" ;
    ada:eelsAcquisitionTimePerSpectrumDefault -9999 ;
    ada:eelsCollectionSemiAngle -9999 ;
    ada:eelsEnergyLossRangeDefault "missing" ;
    ada:phaseIdentificationMethod "FFT from BF-TEM images (no SAED): rutile (TiO2, polycrystalline 2–15 nm); trigonal Ti2O (P3̄m1, zone axis [1 1 2̄ 3]; a=2.983 Å, c=4.804 Å); triclinic Ti2O (P1, zone axis [5 16 12]; a=10.453 Å, b=10.895 Å, c=12.206 Å); d-spacings and zone axes matched to crystal structure parameters" ;
    ada:samplingUnit "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:spectroscopicDetectorDefault "EDS only" ;
    ada:stemDwellTimePerPixelDefault -9999 ;
    bios:computationalTool [ schema1:name "Velox Revision 2.14 (Thermo Fisher Scientific)" ;
            ada:toolRole "acquisition" ],
        [ schema1:name "Velox Revision 2.14 (Thermo Fisher Scientific)" ;
            ada:toolRole "dataReduction" ] .

<https://ada.astromat.org/metadata/parameter/temTAPP/samplePreparationDetailsDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "FEI Scios dual-beam FIB/SEM (Institute of Geochemistry, CAS): glass bead coated with gold prior to FIB; FIB slice ~15 µm length × ~10 µm width × 90–100 nm thick; 30 kV, 0.4 nA beam current" ;
    schema1:name "Sample Preparation Details" ;
    schema1:valueName "samplePreparationDetailsDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/temTAPP/stemProbeCurrentDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:description "1–2 nA (stated as beam current for analysis conditions)" ;
    schema1:name "STEM Probe Current" ;
    schema1:valueName "stemProbeCurrentDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://example.org/instrument/TEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "TEM" ;
    schema1:hasPart <https://example.org/instrument/TEM/part/4D-STEM-Detector>,
        <https://example.org/instrument/TEM/part/Aberration-Corrector>,
        <https://example.org/instrument/TEM/part/EDS-Detector>,
        <https://example.org/instrument/TEM/part/EELS-Spectrometer>,
        <https://example.org/instrument/TEM/part/Electron-Source>,
        <https://example.org/instrument/TEM/part/Imaging-Detector>,
        <https://example.org/instrument/TEM/part/Monochromator> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "ThermoFisher Scientific (FEI)" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "FEI Talos F200S" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "200 kV" .

<https://example.org/instrument/TEM/part/4D-STEM-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "4D-STEM Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Aberration-Corrector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Aberration Corrector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:description "Bruker xflash 6T 30 silicon drift detector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/EELS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EELS Spectrometer" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Imaging-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Imaging Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Monochromator> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Monochromator" ;
    schema1:name "missing" .


```


### temTAPP example Dobrica2022
temTAPP instance derived from Dobrica2022 | Antarctic micrometeorite 03-36-46 | STEM + nanodiffraction + EDS (UH Manoa Titan G2).
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
  "@id": "ex:temTAPP-Dobrica2022",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "tem protocol — Dobrica2022",
  "schema:description": "FIB sections transferred to Cu TEM half-grids (not standard full grids); nanodiffraction used 0.1–0.3 mrad convergence angle in STEM mode (quasi-parallel beam); some carbonate compositions and modulation measurements reported using Molecular Foundry TitanX EDS (see separate column) Reported detail: ada:analyticalSubModeDefault = DF-STEM; BF-STEM; BF-TEM; HRTEM (TEM Imaging); Nanodiffraction (STEM mode, near-parallel probe); SAED (Electron Diffraction).",
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
            "Antarctic micrometeorite 03-36-46 (hydrated fine-grained AMM, H-FgMM, 84×114 µm; carbonates, phyllosilicates, magnetite, sulfides, phosphates; Concordia snow collection 2002 campaign)"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/temTAPP/samplePreparationDetailsDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "samplePreparationDetailsDefault",
            "schema:name": "Sample Preparation Details",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Helios 660 dual-beam FIB-SEM (AEMC, UH Manoa): particle polished and C-coated; Pt deposited by e-beam deposition then by ion beam deposition; sections (~2 µm thick) transferred to Cu TEM half-grids; final thinning at 2 kV, 72 pA with section on TEM grid; 4 FIB sections: UH-001 (carbonate region A), UH-002 (carbonate region B), UH-003 (Ca-phosphates), UH-006 (magnetite)"
          }
        ],
        "schema:description": "FIB lift-out (Ga+)",
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
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:instrument": [
    {
      "schema:additionalType": [
        "TEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "ThermoFisher Scientific (FEI)",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "FEI Titan G2 analytical (S)TEM",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:acceleratingVoltageDefault": "300 kV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/TEM",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "4D-STEM Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/4D-STEM-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Aberration Corrector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Aberration-Corrector"
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
          "@id": "ex:instrument/TEM/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EELS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/EELS-Spectrometer"
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
          "@id": "ex:instrument/TEM/part/Electron-Source"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Imaging Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Imaging-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Monochromator",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Monochromator"
        }
      ],
      "schema:name": "example instrumentName"
    }
  ],
  "ada:spectroscopicDetectorDefault": "EDS only",
  "ada:analyticalSubModeDefault": "BF-STEM",
  "ada:convergenceSemiAngle": "0.1–0.3 mrad (for nanodiffraction in STEM mode)",
  "ada:cameraLengthDefault": "295 mm (stated for nanodiffraction)",
  "ada:phaseIdentificationMethod": "Electron nanodiffraction (STEM mode, 0.1–0.3 mrad convergence, 295 mm camera length) + EDS; SAED for crystallographic characterization; FFT from HRTEM images (dolomite, ankerite, phosphide barringerite); d-spacing comparisons for carbonate phases",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "TEM/STEM"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Advanced Electron Microscopy Center (AEMC), University of Hawai'i at Manoa, USA"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "FIB-SEM (Helios 660 dual-beam); SEM-BSE",
        "schema:description": "Helios 660 dual-beam FIB-SEM (AEMC, UH Manoa): BSE imaging of polished, C-coated section for mineral identification; FIB preparation of 4 electron-transparent sections (Pt deposition: e-beam first, then ion beam; sections transferred to Cu TEM half-grids with micromanipulator; final thinning at 2 kV, 72 pA with section on TEM grid)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:edsAcquisitionModeDefault": "missing",
  "ada:edsCalibrationStandardDefault": "missing",
  "ada:edsQuantificationMethod": "missing",
  "ada:eelsAcquisitionModeDefault": "missing",
  "ada:eelsAcquisitionTimePerSpectrumDefault": -9999,
  "ada:eelsCollectionSemiAngle": -9999,
  "ada:eelsEnergyLossRangeDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stemDwellTimePerPixelDefault": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/TEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:temTAPP-Dobrica2022",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "tem protocol \u2014 Dobrica2022",
  "schema:description": "FIB sections transferred to Cu TEM half-grids (not standard full grids); nanodiffraction used 0.1\u20130.3 mrad convergence angle in STEM mode (quasi-parallel beam); some carbonate compositions and modulation measurements reported using Molecular Foundry TitanX EDS (see separate column) Reported detail: ada:analyticalSubModeDefault = DF-STEM; BF-STEM; BF-TEM; HRTEM (TEM Imaging); Nanodiffraction (STEM mode, near-parallel probe); SAED (Electron Diffraction).",
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
            "Antarctic micrometeorite 03-36-46 (hydrated fine-grained AMM, H-FgMM, 84\u00d7114 \u00b5m; carbonates, phyllosilicates, magnetite, sulfides, phosphates; Concordia snow collection 2002 campaign)"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/temTAPP/samplePreparationDetailsDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "samplePreparationDetailsDefault",
            "schema:name": "Sample Preparation Details",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Helios 660 dual-beam FIB-SEM (AEMC, UH Manoa): particle polished and C-coated; Pt deposited by e-beam deposition then by ion beam deposition; sections (~2 \u00b5m thick) transferred to Cu TEM half-grids; final thinning at 2 kV, 72 pA with section on TEM grid; 4 FIB sections: UH-001 (carbonate region A), UH-002 (carbonate region B), UH-003 (Ca-phosphates), UH-006 (magnetite)"
          }
        ],
        "schema:description": "FIB lift-out (Ga+)",
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
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:instrument": [
    {
      "schema:additionalType": [
        "TEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "ThermoFisher Scientific (FEI)",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "FEI Titan G2 analytical (S)TEM",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:acceleratingVoltageDefault": "300 kV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/TEM",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "4D-STEM Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/4D-STEM-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Aberration Corrector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Aberration-Corrector"
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
          "@id": "ex:instrument/TEM/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EELS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/EELS-Spectrometer"
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
          "@id": "ex:instrument/TEM/part/Electron-Source"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Imaging Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Imaging-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Monochromator",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Monochromator"
        }
      ],
      "schema:name": "example instrumentName"
    }
  ],
  "ada:spectroscopicDetectorDefault": "EDS only",
  "ada:analyticalSubModeDefault": "BF-STEM",
  "ada:convergenceSemiAngle": "0.1\u20130.3 mrad (for nanodiffraction in STEM mode)",
  "ada:cameraLengthDefault": "295 mm (stated for nanodiffraction)",
  "ada:phaseIdentificationMethod": "Electron nanodiffraction (STEM mode, 0.1\u20130.3 mrad convergence, 295 mm camera length) + EDS; SAED for crystallographic characterization; FFT from HRTEM images (dolomite, ankerite, phosphide barringerite); d-spacing comparisons for carbonate phases",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "TEM/STEM"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Advanced Electron Microscopy Center (AEMC), University of Hawai'i at Manoa, USA"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "FIB-SEM (Helios 660 dual-beam); SEM-BSE",
        "schema:description": "Helios 660 dual-beam FIB-SEM (AEMC, UH Manoa): BSE imaging of polished, C-coated section for mineral identification; FIB preparation of 4 electron-transparent sections (Pt deposition: e-beam first, then ion beam; sections transferred to Cu TEM half-grids with micromanipulator; final thinning at 2 kV, 72 pA with section on TEM grid)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:edsAcquisitionModeDefault": "missing",
  "ada:edsCalibrationStandardDefault": "missing",
  "ada:edsQuantificationMethod": "missing",
  "ada:eelsAcquisitionModeDefault": "missing",
  "ada:eelsAcquisitionTimePerSpectrumDefault": -9999,
  "ada:eelsCollectionSemiAngle": -9999,
  "ada:eelsEnergyLossRangeDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stemDwellTimePerPixelDefault": -9999,
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

ex:temTAPP-Dobrica2022 a cdi:Activity,
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
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/temTAPP/samplePreparationDetailsDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "FIB lift-out (Ga+)" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "FIB sections transferred to Cu TEM half-grids (not standard full grids); nanodiffraction used 0.1–0.3 mrad convergence angle in STEM mode (quasi-parallel beam); some carbonate compositions and modulation measurements reported using Molecular Foundry TitanX EDS (see separate column) Reported detail: ada:analyticalSubModeDefault = DF-STEM; BF-STEM; BF-TEM; HRTEM (TEM Imaging); Nanodiffraction (STEM mode, near-parallel probe); SAED (Electron Diffraction)." ;
    schema1:instrument <https://example.org/instrument/TEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Advanced Electron Microscopy Center (AEMC), University of Hawai'i at Manoa, USA" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "TEM/STEM" ] ;
    schema1:name "tem protocol — Dobrica2022" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Antarctic micrometeorite 03-36-46 (hydrated fine-grained AMM, H-FgMM, 84×114 µm; carbonates, phyllosilicates, magnetite, sulfides, phosphates; Concordia snow collection 2002 campaign)" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "Helios 660 dual-beam FIB-SEM (AEMC, UH Manoa): BSE imaging of polished, C-coated section for mineral identification; FIB preparation of 4 electron-transparent sections (Pt deposition: e-beam first, then ion beam; sections transferred to Cu TEM half-grids with micromanipulator; final thinning at 2 kV, 72 pA with section on TEM grid)" ;
                    schema1:name "FIB-SEM (Helios 660 dual-beam); SEM-BSE" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalSubModeDefault "BF-STEM" ;
    ada:cameraLengthDefault "295 mm (stated for nanodiffraction)" ;
    ada:convergenceSemiAngle "0.1–0.3 mrad (for nanodiffraction in STEM mode)" ;
    ada:edsAcquisitionModeDefault "missing" ;
    ada:edsCalibrationStandardDefault "missing" ;
    ada:edsQuantificationMethod "missing" ;
    ada:eelsAcquisitionModeDefault "missing" ;
    ada:eelsAcquisitionTimePerSpectrumDefault -9999 ;
    ada:eelsCollectionSemiAngle -9999 ;
    ada:eelsEnergyLossRangeDefault "missing" ;
    ada:phaseIdentificationMethod "Electron nanodiffraction (STEM mode, 0.1–0.3 mrad convergence, 295 mm camera length) + EDS; SAED for crystallographic characterization; FFT from HRTEM images (dolomite, ankerite, phosphide barringerite); d-spacing comparisons for carbonate phases" ;
    ada:samplingUnit "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:spectroscopicDetectorDefault "EDS only" ;
    ada:stemDwellTimePerPixelDefault -9999 .

<https://ada.astromat.org/metadata/parameter/temTAPP/samplePreparationDetailsDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Helios 660 dual-beam FIB-SEM (AEMC, UH Manoa): particle polished and C-coated; Pt deposited by e-beam deposition then by ion beam deposition; sections (~2 µm thick) transferred to Cu TEM half-grids; final thinning at 2 kV, 72 pA with section on TEM grid; 4 FIB sections: UH-001 (carbonate region A), UH-002 (carbonate region B), UH-003 (Ca-phosphates), UH-006 (magnetite)" ;
    schema1:name "Sample Preparation Details" ;
    schema1:valueName "samplePreparationDetailsDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://example.org/instrument/TEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "TEM" ;
    schema1:hasPart <https://example.org/instrument/TEM/part/4D-STEM-Detector>,
        <https://example.org/instrument/TEM/part/Aberration-Corrector>,
        <https://example.org/instrument/TEM/part/EDS-Detector>,
        <https://example.org/instrument/TEM/part/EELS-Spectrometer>,
        <https://example.org/instrument/TEM/part/Electron-Source>,
        <https://example.org/instrument/TEM/part/Imaging-Detector>,
        <https://example.org/instrument/TEM/part/Monochromator> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "ThermoFisher Scientific (FEI)" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "FEI Titan G2 analytical (S)TEM" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "300 kV" .

<https://example.org/instrument/TEM/part/4D-STEM-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "4D-STEM Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Aberration-Corrector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Aberration Corrector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/EELS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EELS Spectrometer" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Imaging-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Imaging Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Monochromator> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Monochromator" ;
    schema1:name "missing" .


```


### temTAPP example Dobrica2022-2
temTAPP instance derived from Dobrica2022 | Antarctic micrometeorite 03-36-46 | STEM-EDS hyperspectral mapping (Mol. Foundry TitanX).
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
  "@id": "ex:temTAPP-Dobrica2022-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "tem protocol — Dobrica2022-2",
  "schema:description": "EDS analysis areas 5–10 nm (Molecular Foundry); compositions displayed as color-coded maps in Esprit 1.9; O abundances noted as subject to variable self-absorption; compositions normalized to 100% Reported detail: ada:analyticalSubModeDefault = HAADF-STEM (Z-contrast); STEM-EDS (hyperspectral map); ada:edsAcquisitionModeDefault = Spectrum image (hyperspectral map).",
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
            "Antarctic micrometeorite 03-36-46 (hydrated fine-grained AMM, H-FgMM, 84×114 µm; carbonates, phyllosilicates, magnetite, sulfides, phosphates; Concordia snow collection 2002 campaign)"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/temTAPP/samplePreparationDetailsDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "samplePreparationDetailsDefault",
            "schema:name": "Sample Preparation Details",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Helios 660 dual-beam FIB-SEM (AEMC, UH Manoa): particle polished and C-coated; Pt deposited by e-beam deposition then by ion beam deposition; sections (~2 µm thick) transferred to Cu TEM half-grids; final thinning at 2 kV, 72 pA with section on TEM grid; 4 FIB sections: UH-001 (carbonate region A), UH-002 (carbonate region B), UH-003 (Ca-phosphates), UH-006 (magnetite)"
          }
        ],
        "schema:description": "FIB lift-out (Ga+)",
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
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:instrument": [
    {
      "schema:additionalType": [
        "TEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "ThermoFisher Scientific (FEI)",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "FEI TitanX 80–300 kV (\"ChemiSTEM\")",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Four windowless silicon drift detectors (SDD); 0.7 sr solid angle",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/EDS-Detector",
          "schema:name": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "4D-STEM Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/4D-STEM-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Aberration Corrector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Aberration-Corrector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EELS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/EELS-Spectrometer"
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
          "@id": "ex:instrument/TEM/part/Electron-Source"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Imaging Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Imaging-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Monochromator",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Monochromator"
        }
      ],
      "ada:acceleratingVoltageDefault": "200 kV (EDS maps acquired at 200 kV; instrument range 80–300 kV)",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/TEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:spectroscopicDetectorDefault": "EDS only",
  "ada:analyticalSubModeDefault": "ADF",
  "ada:edsAcquisitionModeDefault": "Spectrum image",
  "ada:phaseIdentificationMethod": "EDS quantification: compositions normalized to 100%; carbonate chemistry (MgCO3–CaCO3–(Fe+Mn)CO3 ternary) used for dolomite/ankerite ID; structural formulae from EDS spot analyses over 5–10 nm areas; detection limit <0.1 wt% (stated for TEM EDS measurements)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/temTAPP/edsDetectionLimitDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "edsDetectionLimitDefault",
      "schema:name": "EDS Detection Limit",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 0.1,
      "schema:description": "<0.1 wt% (stated for TEM EDS measurements)"
    }
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "TEM/STEM"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Molecular Foundry, Lawrence Berkeley National Laboratory, USA"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "FIB-SEM (Helios 660 dual-beam); SEM-BSE",
        "schema:description": "Helios 660 dual-beam FIB-SEM (AEMC, UH Manoa): BSE imaging of polished, C-coated section for mineral identification; FIB preparation of 4 electron-transparent sections (Pt deposition: e-beam first, then ion beam; sections transferred to Cu TEM half-grids with micromanipulator; final thinning at 2 kV, 72 pA with section on TEM grid)"
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
      "schema:name": "Bruker Esprit 1.9"
    }
  ],
  "ada:cameraLengthDefault": -9999,
  "ada:convergenceSemiAngle": -9999,
  "ada:edsCalibrationStandardDefault": "missing",
  "ada:edsQuantificationMethod": "missing",
  "ada:eelsAcquisitionModeDefault": "missing",
  "ada:eelsAcquisitionTimePerSpectrumDefault": -9999,
  "ada:eelsCollectionSemiAngle": -9999,
  "ada:eelsEnergyLossRangeDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stemDwellTimePerPixelDefault": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/TEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:temTAPP-Dobrica2022-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "tem protocol \u2014 Dobrica2022-2",
  "schema:description": "EDS analysis areas 5\u201310 nm (Molecular Foundry); compositions displayed as color-coded maps in Esprit 1.9; O abundances noted as subject to variable self-absorption; compositions normalized to 100% Reported detail: ada:analyticalSubModeDefault = HAADF-STEM (Z-contrast); STEM-EDS (hyperspectral map); ada:edsAcquisitionModeDefault = Spectrum image (hyperspectral map).",
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
            "Antarctic micrometeorite 03-36-46 (hydrated fine-grained AMM, H-FgMM, 84\u00d7114 \u00b5m; carbonates, phyllosilicates, magnetite, sulfides, phosphates; Concordia snow collection 2002 campaign)"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/temTAPP/samplePreparationDetailsDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "samplePreparationDetailsDefault",
            "schema:name": "Sample Preparation Details",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Helios 660 dual-beam FIB-SEM (AEMC, UH Manoa): particle polished and C-coated; Pt deposited by e-beam deposition then by ion beam deposition; sections (~2 \u00b5m thick) transferred to Cu TEM half-grids; final thinning at 2 kV, 72 pA with section on TEM grid; 4 FIB sections: UH-001 (carbonate region A), UH-002 (carbonate region B), UH-003 (Ca-phosphates), UH-006 (magnetite)"
          }
        ],
        "schema:description": "FIB lift-out (Ga+)",
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
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:instrument": [
    {
      "schema:additionalType": [
        "TEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "ThermoFisher Scientific (FEI)",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "FEI TitanX 80\u2013300 kV (\"ChemiSTEM\")",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Four windowless silicon drift detectors (SDD); 0.7 sr solid angle",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/EDS-Detector",
          "schema:name": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "4D-STEM Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/4D-STEM-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Aberration Corrector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Aberration-Corrector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EELS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/EELS-Spectrometer"
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
          "@id": "ex:instrument/TEM/part/Electron-Source"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Imaging Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Imaging-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Monochromator",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Monochromator"
        }
      ],
      "ada:acceleratingVoltageDefault": "200 kV (EDS maps acquired at 200 kV; instrument range 80\u2013300 kV)",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/TEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:spectroscopicDetectorDefault": "EDS only",
  "ada:analyticalSubModeDefault": "ADF",
  "ada:edsAcquisitionModeDefault": "Spectrum image",
  "ada:phaseIdentificationMethod": "EDS quantification: compositions normalized to 100%; carbonate chemistry (MgCO3\u2013CaCO3\u2013(Fe+Mn)CO3 ternary) used for dolomite/ankerite ID; structural formulae from EDS spot analyses over 5\u201310 nm areas; detection limit <0.1 wt% (stated for TEM EDS measurements)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/temTAPP/edsDetectionLimitDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "edsDetectionLimitDefault",
      "schema:name": "EDS Detection Limit",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 0.1,
      "schema:description": "<0.1 wt% (stated for TEM EDS measurements)"
    }
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "TEM/STEM"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Molecular Foundry, Lawrence Berkeley National Laboratory, USA"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "FIB-SEM (Helios 660 dual-beam); SEM-BSE",
        "schema:description": "Helios 660 dual-beam FIB-SEM (AEMC, UH Manoa): BSE imaging of polished, C-coated section for mineral identification; FIB preparation of 4 electron-transparent sections (Pt deposition: e-beam first, then ion beam; sections transferred to Cu TEM half-grids with micromanipulator; final thinning at 2 kV, 72 pA with section on TEM grid)"
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
      "schema:name": "Bruker Esprit 1.9"
    }
  ],
  "ada:cameraLengthDefault": -9999,
  "ada:convergenceSemiAngle": -9999,
  "ada:edsCalibrationStandardDefault": "missing",
  "ada:edsQuantificationMethod": "missing",
  "ada:eelsAcquisitionModeDefault": "missing",
  "ada:eelsAcquisitionTimePerSpectrumDefault": -9999,
  "ada:eelsCollectionSemiAngle": -9999,
  "ada:eelsEnergyLossRangeDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stemDwellTimePerPixelDefault": -9999,
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

ex:temTAPP-Dobrica2022-2 a cdi:Activity,
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
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/temTAPP/samplePreparationDetailsDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "FIB lift-out (Ga+)" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/temTAPP/edsDetectionLimitDefault> ;
    schema1:datePublished "missing" ;
    schema1:description "EDS analysis areas 5–10 nm (Molecular Foundry); compositions displayed as color-coded maps in Esprit 1.9; O abundances noted as subject to variable self-absorption; compositions normalized to 100% Reported detail: ada:analyticalSubModeDefault = HAADF-STEM (Z-contrast); STEM-EDS (hyperspectral map); ada:edsAcquisitionModeDefault = Spectrum image (hyperspectral map)." ;
    schema1:instrument <https://example.org/instrument/TEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Molecular Foundry, Lawrence Berkeley National Laboratory, USA" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "TEM/STEM" ] ;
    schema1:name "tem protocol — Dobrica2022-2" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Antarctic micrometeorite 03-36-46 (hydrated fine-grained AMM, H-FgMM, 84×114 µm; carbonates, phyllosilicates, magnetite, sulfides, phosphates; Concordia snow collection 2002 campaign)" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "Helios 660 dual-beam FIB-SEM (AEMC, UH Manoa): BSE imaging of polished, C-coated section for mineral identification; FIB preparation of 4 electron-transparent sections (Pt deposition: e-beam first, then ion beam; sections transferred to Cu TEM half-grids with micromanipulator; final thinning at 2 kV, 72 pA with section on TEM grid)" ;
                    schema1:name "FIB-SEM (Helios 660 dual-beam); SEM-BSE" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalSubModeDefault "ADF" ;
    ada:cameraLengthDefault -9999 ;
    ada:convergenceSemiAngle -9999 ;
    ada:edsAcquisitionModeDefault "Spectrum image" ;
    ada:edsCalibrationStandardDefault "missing" ;
    ada:edsQuantificationMethod "missing" ;
    ada:eelsAcquisitionModeDefault "missing" ;
    ada:eelsAcquisitionTimePerSpectrumDefault -9999 ;
    ada:eelsCollectionSemiAngle -9999 ;
    ada:eelsEnergyLossRangeDefault "missing" ;
    ada:phaseIdentificationMethod "EDS quantification: compositions normalized to 100%; carbonate chemistry (MgCO3–CaCO3–(Fe+Mn)CO3 ternary) used for dolomite/ankerite ID; structural formulae from EDS spot analyses over 5–10 nm areas; detection limit <0.1 wt% (stated for TEM EDS measurements)" ;
    ada:samplingUnit "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:spectroscopicDetectorDefault "EDS only" ;
    ada:stemDwellTimePerPixelDefault -9999 ;
    bios:computationalTool [ schema1:name "Bruker Esprit 1.9" ;
            ada:toolRole "dataReduction" ] .

<https://ada.astromat.org/metadata/parameter/temTAPP/edsDetectionLimitDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1e-01 ;
    schema1:description "<0.1 wt% (stated for TEM EDS measurements)" ;
    schema1:name "EDS Detection Limit" ;
    schema1:valueName "edsDetectionLimitDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/temTAPP/samplePreparationDetailsDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Helios 660 dual-beam FIB-SEM (AEMC, UH Manoa): particle polished and C-coated; Pt deposited by e-beam deposition then by ion beam deposition; sections (~2 µm thick) transferred to Cu TEM half-grids; final thinning at 2 kV, 72 pA with section on TEM grid; 4 FIB sections: UH-001 (carbonate region A), UH-002 (carbonate region B), UH-003 (Ca-phosphates), UH-006 (magnetite)" ;
    schema1:name "Sample Preparation Details" ;
    schema1:valueName "samplePreparationDetailsDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://example.org/instrument/TEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "TEM" ;
    schema1:hasPart <https://example.org/instrument/TEM/part/4D-STEM-Detector>,
        <https://example.org/instrument/TEM/part/Aberration-Corrector>,
        <https://example.org/instrument/TEM/part/EDS-Detector>,
        <https://example.org/instrument/TEM/part/EELS-Spectrometer>,
        <https://example.org/instrument/TEM/part/Electron-Source>,
        <https://example.org/instrument/TEM/part/Imaging-Detector>,
        <https://example.org/instrument/TEM/part/Monochromator> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "ThermoFisher Scientific (FEI)" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "FEI TitanX 80–300 kV (\"ChemiSTEM\")" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "200 kV (EDS maps acquired at 200 kV; instrument range 80–300 kV)" .

<https://example.org/instrument/TEM/part/4D-STEM-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "4D-STEM Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Aberration-Corrector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Aberration Corrector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:description "Four windowless silicon drift detectors (SDD); 0.7 sr solid angle" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/EELS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EELS Spectrometer" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Imaging-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Imaging Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Monochromator> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Monochromator" ;
    schema1:name "missing" .


```


### temTAPP example Singerling2025
temTAPP instance derived from Singerling2025 | Bennu OREX-800045-102 | BF-TEM + HAADF-STEM + SAED + EDS (Goethe TS Talos F200X G2).
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
  "@id": "ex:temTAPP-Singerling2025",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "tem protocol — Singerling2025",
  "schema:description": "Na,Ca carbonate grains extremely beam-sensitive: amorphized under electron beam; samples re-analyzed in 4 sessions (Dec 2023 – Dec 2024) to track terrestrial alteration; NO FIB used (authors note FIB may destroy beam-sensitive Na,Ca carbonates); underlying TEM data deposited at AstroMat (Table A4 supplementary); note: same Goethe lab and instrument (Talos F200X G2) as in Zega2025 Reported detail: ada:analyticalSubModeDefault = BF-TEM; HAADF-STEM; SAED (Electron Diffraction); STEM-EDS (point; map); ada:edsAcquisitionModeDefault = Spectrum image (map); point analysis; ada:edsQuantificationMethod = Cliff-Lorimer (k-factor) method; no absorption corrections.",
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
            "Bennu particle OREX-800045-102 (OSIRIS-REx sample): Na,Ca carbonates (gaylussite/pirssonite), phyllosilicates, sulfides"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/temTAPP/samplePreparationDetailsDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "samplePreparationDetailsDefault",
            "schema:name": "Sample Preparation Details",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Particle crushed between two glass slides; ethanol dropped onto powder; TEM copper mesh grid with lacey carbon support touched to suspension; allowed to dry; gentle plasma cleaning performed before inserting into microscope"
          }
        ],
        "schema:description": "Crushing / dispersion on grid",
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
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:instrument": [
    {
      "schema:additionalType": [
        "TEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "Unknown",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "Thermo Scientific Talos F200X G2 S/TEM",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Super-X G2 EDS system: four windowless silicon drift detectors; collection solid angle up to 0.9 srad",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/EDS-Detector",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "Imaging Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "TS Ceta-S 4k × 4k 16M camera (TEM images and SAED)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/Imaging-Detector",
          "schema:name": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "4D-STEM Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/4D-STEM-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Aberration Corrector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Aberration-Corrector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EELS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/EELS-Spectrometer"
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
          "@id": "ex:instrument/TEM/part/Electron-Source"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Monochromator",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Monochromator"
        }
      ],
      "ada:acceleratingVoltageDefault": "200 kV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/TEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:spectroscopicDetectorDefault": "EDS only",
  "ada:analyticalSubModeDefault": "BF-TEM",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/temTAPP/haadfCollectionAnglesDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "haadfCollectionAnglesDefault",
      "schema:name": "HAADF Collection Angles",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Convergence semi-angle 10.5 mrad; inner collection semi-angle 58 mrad"
    },
    {
      "@id": "ada:parameter/temTAPP/diffractionCameraLengthCalibrationMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "diffractionCameraLengthCalibrationMethodDefault",
      "schema:name": "Diffraction Camera Length Calibration Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "External standard: Cross Grating 3 mm S106 from AGAR (image magnification and camera constant calibrations)"
    },
    {
      "@id": "ada:parameter/temTAPP/diffractionCalibrationReferenceDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "diffractionCalibrationReferenceDefault",
      "schema:name": "Diffraction Calibration Reference",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "AGAR S106 Cross Grating 3 mm (camera constant calibration)"
    }
  ],
  "ada:convergenceSemiAngle": "10.5 mrad",
  "ada:edsAcquisitionModeDefault": "Spectrum image",
  "ada:edsQuantificationMethod": "Cliff-Lorimer (k-factor)",
  "ada:phaseIdentificationMethod": "SAED (few reflections due to beam sensitivity / poor crystallinity) matched against literature crystal structures (Dickens and Brown 1969 for gaylussite/pirssonite; McKie and Frankis 1977 for nyerereite); EDS cation ratios compared to theoretical mineral formulae (H and reliable O not measurable by EDS)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "TEM/STEM"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Schwiete Cosmochemistry Laboratory, Goethe University, Frankfurt, Germany"
  },
  "bios:computationalTool": [
    {
      "ada:toolRole": "acquisition",
      "schema:name": "TS Velox"
    },
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "TS Velox"
    }
  ],
  "ada:cameraLengthDefault": -9999,
  "ada:edsCalibrationStandardDefault": "missing",
  "ada:eelsAcquisitionModeDefault": "missing",
  "ada:eelsAcquisitionTimePerSpectrumDefault": -9999,
  "ada:eelsCollectionSemiAngle": -9999,
  "ada:eelsEnergyLossRangeDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stemDwellTimePerPixelDefault": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/TEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:temTAPP-Singerling2025",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "tem protocol \u2014 Singerling2025",
  "schema:description": "Na,Ca carbonate grains extremely beam-sensitive: amorphized under electron beam; samples re-analyzed in 4 sessions (Dec 2023 \u2013 Dec 2024) to track terrestrial alteration; NO FIB used (authors note FIB may destroy beam-sensitive Na,Ca carbonates); underlying TEM data deposited at AstroMat (Table A4 supplementary); note: same Goethe lab and instrument (Talos F200X G2) as in Zega2025 Reported detail: ada:analyticalSubModeDefault = BF-TEM; HAADF-STEM; SAED (Electron Diffraction); STEM-EDS (point; map); ada:edsAcquisitionModeDefault = Spectrum image (map); point analysis; ada:edsQuantificationMethod = Cliff-Lorimer (k-factor) method; no absorption corrections.",
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
            "Bennu particle OREX-800045-102 (OSIRIS-REx sample): Na,Ca carbonates (gaylussite/pirssonite), phyllosilicates, sulfides"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/temTAPP/samplePreparationDetailsDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "samplePreparationDetailsDefault",
            "schema:name": "Sample Preparation Details",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Particle crushed between two glass slides; ethanol dropped onto powder; TEM copper mesh grid with lacey carbon support touched to suspension; allowed to dry; gentle plasma cleaning performed before inserting into microscope"
          }
        ],
        "schema:description": "Crushing / dispersion on grid",
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
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:instrument": [
    {
      "schema:additionalType": [
        "TEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "Unknown",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "Thermo Scientific Talos F200X G2 S/TEM",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Super-X G2 EDS system: four windowless silicon drift detectors; collection solid angle up to 0.9 srad",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/EDS-Detector",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "Imaging Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "TS Ceta-S 4k \u00d7 4k 16M camera (TEM images and SAED)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/Imaging-Detector",
          "schema:name": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "4D-STEM Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/4D-STEM-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Aberration Corrector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Aberration-Corrector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EELS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/EELS-Spectrometer"
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
          "@id": "ex:instrument/TEM/part/Electron-Source"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Monochromator",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Monochromator"
        }
      ],
      "ada:acceleratingVoltageDefault": "200 kV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/TEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:spectroscopicDetectorDefault": "EDS only",
  "ada:analyticalSubModeDefault": "BF-TEM",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/temTAPP/haadfCollectionAnglesDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "haadfCollectionAnglesDefault",
      "schema:name": "HAADF Collection Angles",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Convergence semi-angle 10.5 mrad; inner collection semi-angle 58 mrad"
    },
    {
      "@id": "ada:parameter/temTAPP/diffractionCameraLengthCalibrationMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "diffractionCameraLengthCalibrationMethodDefault",
      "schema:name": "Diffraction Camera Length Calibration Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "External standard: Cross Grating 3 mm S106 from AGAR (image magnification and camera constant calibrations)"
    },
    {
      "@id": "ada:parameter/temTAPP/diffractionCalibrationReferenceDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "diffractionCalibrationReferenceDefault",
      "schema:name": "Diffraction Calibration Reference",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "AGAR S106 Cross Grating 3 mm (camera constant calibration)"
    }
  ],
  "ada:convergenceSemiAngle": "10.5 mrad",
  "ada:edsAcquisitionModeDefault": "Spectrum image",
  "ada:edsQuantificationMethod": "Cliff-Lorimer (k-factor)",
  "ada:phaseIdentificationMethod": "SAED (few reflections due to beam sensitivity / poor crystallinity) matched against literature crystal structures (Dickens and Brown 1969 for gaylussite/pirssonite; McKie and Frankis 1977 for nyerereite); EDS cation ratios compared to theoretical mineral formulae (H and reliable O not measurable by EDS)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "TEM/STEM"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Schwiete Cosmochemistry Laboratory, Goethe University, Frankfurt, Germany"
  },
  "bios:computationalTool": [
    {
      "ada:toolRole": "acquisition",
      "schema:name": "TS Velox"
    },
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "TS Velox"
    }
  ],
  "ada:cameraLengthDefault": -9999,
  "ada:edsCalibrationStandardDefault": "missing",
  "ada:eelsAcquisitionModeDefault": "missing",
  "ada:eelsAcquisitionTimePerSpectrumDefault": -9999,
  "ada:eelsCollectionSemiAngle": -9999,
  "ada:eelsEnergyLossRangeDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stemDwellTimePerPixelDefault": -9999,
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

ex:temTAPP-Singerling2025 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/temTAPP/samplePreparationDetailsDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Crushing / dispersion on grid" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/temTAPP/diffractionCalibrationReferenceDefault>,
        <https://ada.astromat.org/metadata/parameter/temTAPP/diffractionCameraLengthCalibrationMethodDefault>,
        <https://ada.astromat.org/metadata/parameter/temTAPP/haadfCollectionAnglesDefault> ;
    schema1:datePublished "missing" ;
    schema1:description "Na,Ca carbonate grains extremely beam-sensitive: amorphized under electron beam; samples re-analyzed in 4 sessions (Dec 2023 – Dec 2024) to track terrestrial alteration; NO FIB used (authors note FIB may destroy beam-sensitive Na,Ca carbonates); underlying TEM data deposited at AstroMat (Table A4 supplementary); note: same Goethe lab and instrument (Talos F200X G2) as in Zega2025 Reported detail: ada:analyticalSubModeDefault = BF-TEM; HAADF-STEM; SAED (Electron Diffraction); STEM-EDS (point; map); ada:edsAcquisitionModeDefault = Spectrum image (map); point analysis; ada:edsQuantificationMethod = Cliff-Lorimer (k-factor) method; no absorption corrections." ;
    schema1:instrument <https://example.org/instrument/TEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Schwiete Cosmochemistry Laboratory, Goethe University, Frankfurt, Germany" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "TEM/STEM" ] ;
    schema1:name "tem protocol — Singerling2025" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Bennu particle OREX-800045-102 (OSIRIS-REx sample): Na,Ca carbonates (gaylussite/pirssonite), phyllosilicates, sulfides" ] ] ;
    ada:analyticalSubModeDefault "BF-TEM" ;
    ada:cameraLengthDefault -9999 ;
    ada:convergenceSemiAngle "10.5 mrad" ;
    ada:edsAcquisitionModeDefault "Spectrum image" ;
    ada:edsCalibrationStandardDefault "missing" ;
    ada:edsQuantificationMethod "Cliff-Lorimer (k-factor)" ;
    ada:eelsAcquisitionModeDefault "missing" ;
    ada:eelsAcquisitionTimePerSpectrumDefault -9999 ;
    ada:eelsCollectionSemiAngle -9999 ;
    ada:eelsEnergyLossRangeDefault "missing" ;
    ada:phaseIdentificationMethod "SAED (few reflections due to beam sensitivity / poor crystallinity) matched against literature crystal structures (Dickens and Brown 1969 for gaylussite/pirssonite; McKie and Frankis 1977 for nyerereite); EDS cation ratios compared to theoretical mineral formulae (H and reliable O not measurable by EDS)" ;
    ada:samplingUnit "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:spectroscopicDetectorDefault "EDS only" ;
    ada:stemDwellTimePerPixelDefault -9999 ;
    bios:computationalTool [ schema1:name "TS Velox" ;
            ada:toolRole "acquisition" ],
        [ schema1:name "TS Velox" ;
            ada:toolRole "dataReduction" ] .

<https://ada.astromat.org/metadata/parameter/temTAPP/diffractionCalibrationReferenceDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "AGAR S106 Cross Grating 3 mm (camera constant calibration)" ;
    schema1:name "Diffraction Calibration Reference" ;
    schema1:valueName "diffractionCalibrationReferenceDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/temTAPP/diffractionCameraLengthCalibrationMethodDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "External standard: Cross Grating 3 mm S106 from AGAR (image magnification and camera constant calibrations)" ;
    schema1:name "Diffraction Camera Length Calibration Method" ;
    schema1:valueName "diffractionCameraLengthCalibrationMethodDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/temTAPP/haadfCollectionAnglesDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Convergence semi-angle 10.5 mrad; inner collection semi-angle 58 mrad" ;
    schema1:name "HAADF Collection Angles" ;
    schema1:valueName "haadfCollectionAnglesDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/temTAPP/samplePreparationDetailsDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Particle crushed between two glass slides; ethanol dropped onto powder; TEM copper mesh grid with lacey carbon support touched to suspension; allowed to dry; gentle plasma cleaning performed before inserting into microscope" ;
    schema1:name "Sample Preparation Details" ;
    schema1:valueName "samplePreparationDetailsDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://example.org/instrument/TEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "TEM" ;
    schema1:hasPart <https://example.org/instrument/TEM/part/4D-STEM-Detector>,
        <https://example.org/instrument/TEM/part/Aberration-Corrector>,
        <https://example.org/instrument/TEM/part/EDS-Detector>,
        <https://example.org/instrument/TEM/part/EELS-Spectrometer>,
        <https://example.org/instrument/TEM/part/Electron-Source>,
        <https://example.org/instrument/TEM/part/Imaging-Detector>,
        <https://example.org/instrument/TEM/part/Monochromator> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Unknown" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Thermo Scientific Talos F200X G2 S/TEM" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "200 kV" .

<https://example.org/instrument/TEM/part/4D-STEM-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "4D-STEM Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Aberration-Corrector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Aberration Corrector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:description "Super-X G2 EDS system: four windowless silicon drift detectors; collection solid angle up to 0.9 srad" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/EELS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EELS Spectrometer" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Imaging-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Imaging Detector" ;
    schema1:description "TS Ceta-S 4k × 4k 16M camera (TEM images and SAED)" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Monochromator> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Monochromator" ;
    schema1:name "missing" .


```


### temTAPP example Thompson2020
temTAPP instance derived from Thompson2020 | Murchison CM2 (laser-irradiated) | BF/DF-STEM + HRTEM + STEM-EDX (JSC JEOL 2500SE).
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
  "@id": "ex:temTAPP-Thompson2020",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "tem protocol — Thompson2020",
  "schema:description": "STEM probe diameter = 2 nm (used for EDS spectrum imaging); 1% counting statistics criterion for EDX accumulation. Same instrument (JEOL 2500SE at ARES JSC) as KellerBerger2014. Phase ID relies entirely on HRTEM+FFT (no SAED used). Reported detail: ada:analyticalSubModeDefault = BF-STEM; DF-STEM; HRTEM; STEM-EDS spectrum imaging (maps + line profiles); ada:edsAcquisitionModeDefault = Spectrum imaging (spatially resolved maps and line profiles); successive accumulated scans.",
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
            "CM2 carbonaceous chondrite (Murchison); laboratory-simulated progressively space-weathered chips (1×, 2×, 5× pulsed-laser irradiation passes)"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/temTAPP/samplePreparationDetailsDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "samplePreparationDetailsDefault",
            "schema:name": "Sample Preparation Details",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "FEI Quanta 3D FIB-SEM at JSC; four electron-transparent sections (<100 nm thick): (1) 1× matrix, (2) 5× matrix, (3) 5× sulfide grain, (4) 5× olivine grain"
          }
        ],
        "schema:description": "FIB lift-out (Ga+)",
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
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:instrument": [
    {
      "schema:additionalType": [
        "TEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "JEOL 2500SE",
        "@type": [
          "schema:ProductModel"
        ]
      },
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
          "@id": "ex:instrument/TEM/part/Electron-Source",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Thin-window Thermo energy-dispersive X-ray spectrometer; 50 mm² detector; configured for large solid-angle X-ray collection",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/EDS-Detector",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "Imaging Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "BF detector; DF (ADF) detector",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/Imaging-Detector",
          "schema:name": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "4D-STEM Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/4D-STEM-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Aberration Corrector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Aberration-Corrector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EELS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/EELS-Spectrometer"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Monochromator",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Monochromator"
        }
      ],
      "ada:acceleratingVoltageDefault": "200 kV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/TEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:spectroscopicDetectorDefault": "N/A",
  "ada:analyticalSubModeDefault": "BF-STEM",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/temTAPP/stemProbeDiameterDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "stemProbeDiameterDefault",
      "schema:name": "STEM Probe Diameter",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 2,
      "schema:description": "2 nm"
    },
    {
      "@id": "ada:parameter/temTAPP/stemFrameAveragingDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "stemFrameAveragingDefault",
      "schema:name": "STEM Frame Averaging",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Successive scans accumulated until major element counts achieved 1% counting statistics"
    },
    {
      "@id": "ada:parameter/temTAPP/edsCountingStatisticsAccumulationCriterionDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "edsCountingStatisticsAccumulationCriterionDefault",
      "schema:name": "EDS Counting Statistics / Accumulation Criterion",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Successive scans accumulated until major element counts achieved 1% counting statistics"
    }
  ],
  "ada:stemDwellTimePerPixelDefault": "50 µs (kept short to prevent beam damage)",
  "ada:edsAcquisitionModeDefault": "Map",
  "ada:phaseIdentificationMethod": "HRTEM lattice fringe imaging + FFT; EDS composition maps (no SAED; phase ID by d-spacings from HRTEM); phases identified: pentlandite, Fe-Ni-S, magnetite, serpentine, chrysotile, olivine, metallic Fe",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Scanning Transmission Electron Microscopy (STEM); High-Resolution TEM (HRTEM); STEM-EDS spectrum imaging"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "ARES, NASA Johnson Space Center, Houston, TX, USA"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Pulsed laser irradiation (space weathering simulation); VIS-NIR reflectance spectroscopy (ASD FieldSpec 3); FTIR (Bruker Vertex/Hyperion); Mössbauer spectroscopy (MIMOS-II); μL2MS (two-step laser mass spectrometry); FIB-SEM (FEI Quanta 3D at JSC)",
        "schema:description": "Multi-technique coordinated study; TEM/STEM used for microstructural and chemical characterization of FIB-extracted sections from laser-irradiated Murchison chips; STEM results correlated with reflectance, FTIR, and organic chemistry data"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:cameraLengthDefault": -9999,
  "ada:convergenceSemiAngle": -9999,
  "ada:edsCalibrationStandardDefault": "missing",
  "ada:edsQuantificationMethod": "missing",
  "ada:eelsAcquisitionModeDefault": "missing",
  "ada:eelsAcquisitionTimePerSpectrumDefault": -9999,
  "ada:eelsCollectionSemiAngle": -9999,
  "ada:eelsEnergyLossRangeDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/TEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:temTAPP-Thompson2020",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "tem protocol \u2014 Thompson2020",
  "schema:description": "STEM probe diameter = 2 nm (used for EDS spectrum imaging); 1% counting statistics criterion for EDX accumulation. Same instrument (JEOL 2500SE at ARES JSC) as KellerBerger2014. Phase ID relies entirely on HRTEM+FFT (no SAED used). Reported detail: ada:analyticalSubModeDefault = BF-STEM; DF-STEM; HRTEM; STEM-EDS spectrum imaging (maps + line profiles); ada:edsAcquisitionModeDefault = Spectrum imaging (spatially resolved maps and line profiles); successive accumulated scans.",
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
            "CM2 carbonaceous chondrite (Murchison); laboratory-simulated progressively space-weathered chips (1\u00d7, 2\u00d7, 5\u00d7 pulsed-laser irradiation passes)"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/temTAPP/samplePreparationDetailsDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "samplePreparationDetailsDefault",
            "schema:name": "Sample Preparation Details",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "FEI Quanta 3D FIB-SEM at JSC; four electron-transparent sections (<100 nm thick): (1) 1\u00d7 matrix, (2) 5\u00d7 matrix, (3) 5\u00d7 sulfide grain, (4) 5\u00d7 olivine grain"
          }
        ],
        "schema:description": "FIB lift-out (Ga+)",
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
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:instrument": [
    {
      "schema:additionalType": [
        "TEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "JEOL 2500SE",
        "@type": [
          "schema:ProductModel"
        ]
      },
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
          "@id": "ex:instrument/TEM/part/Electron-Source",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Thin-window Thermo energy-dispersive X-ray spectrometer; 50 mm\u00b2 detector; configured for large solid-angle X-ray collection",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/EDS-Detector",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "Imaging Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "BF detector; DF (ADF) detector",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/Imaging-Detector",
          "schema:name": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "4D-STEM Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/4D-STEM-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Aberration Corrector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Aberration-Corrector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EELS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/EELS-Spectrometer"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Monochromator",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Monochromator"
        }
      ],
      "ada:acceleratingVoltageDefault": "200 kV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/TEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:spectroscopicDetectorDefault": "N/A",
  "ada:analyticalSubModeDefault": "BF-STEM",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/temTAPP/stemProbeDiameterDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "stemProbeDiameterDefault",
      "schema:name": "STEM Probe Diameter",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 2,
      "schema:description": "2 nm"
    },
    {
      "@id": "ada:parameter/temTAPP/stemFrameAveragingDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "stemFrameAveragingDefault",
      "schema:name": "STEM Frame Averaging",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Successive scans accumulated until major element counts achieved 1% counting statistics"
    },
    {
      "@id": "ada:parameter/temTAPP/edsCountingStatisticsAccumulationCriterionDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "edsCountingStatisticsAccumulationCriterionDefault",
      "schema:name": "EDS Counting Statistics / Accumulation Criterion",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Successive scans accumulated until major element counts achieved 1% counting statistics"
    }
  ],
  "ada:stemDwellTimePerPixelDefault": "50 \u00b5s (kept short to prevent beam damage)",
  "ada:edsAcquisitionModeDefault": "Map",
  "ada:phaseIdentificationMethod": "HRTEM lattice fringe imaging + FFT; EDS composition maps (no SAED; phase ID by d-spacings from HRTEM); phases identified: pentlandite, Fe-Ni-S, magnetite, serpentine, chrysotile, olivine, metallic Fe",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Scanning Transmission Electron Microscopy (STEM); High-Resolution TEM (HRTEM); STEM-EDS spectrum imaging"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "ARES, NASA Johnson Space Center, Houston, TX, USA"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Pulsed laser irradiation (space weathering simulation); VIS-NIR reflectance spectroscopy (ASD FieldSpec 3); FTIR (Bruker Vertex/Hyperion); M\u00f6ssbauer spectroscopy (MIMOS-II); \u03bcL2MS (two-step laser mass spectrometry); FIB-SEM (FEI Quanta 3D at JSC)",
        "schema:description": "Multi-technique coordinated study; TEM/STEM used for microstructural and chemical characterization of FIB-extracted sections from laser-irradiated Murchison chips; STEM results correlated with reflectance, FTIR, and organic chemistry data"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:cameraLengthDefault": -9999,
  "ada:convergenceSemiAngle": -9999,
  "ada:edsCalibrationStandardDefault": "missing",
  "ada:edsQuantificationMethod": "missing",
  "ada:eelsAcquisitionModeDefault": "missing",
  "ada:eelsAcquisitionTimePerSpectrumDefault": -9999,
  "ada:eelsCollectionSemiAngle": -9999,
  "ada:eelsEnergyLossRangeDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
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

ex:temTAPP-Thompson2020 a cdi:Activity,
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
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/temTAPP/samplePreparationDetailsDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "FIB lift-out (Ga+)" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/temTAPP/edsCountingStatisticsAccumulationCriterionDefault>,
        <https://ada.astromat.org/metadata/parameter/temTAPP/stemFrameAveragingDefault>,
        <https://ada.astromat.org/metadata/parameter/temTAPP/stemProbeDiameterDefault> ;
    schema1:datePublished "missing" ;
    schema1:description "STEM probe diameter = 2 nm (used for EDS spectrum imaging); 1% counting statistics criterion for EDX accumulation. Same instrument (JEOL 2500SE at ARES JSC) as KellerBerger2014. Phase ID relies entirely on HRTEM+FFT (no SAED used). Reported detail: ada:analyticalSubModeDefault = BF-STEM; DF-STEM; HRTEM; STEM-EDS spectrum imaging (maps + line profiles); ada:edsAcquisitionModeDefault = Spectrum imaging (spatially resolved maps and line profiles); successive accumulated scans." ;
    schema1:instrument <https://example.org/instrument/TEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "ARES, NASA Johnson Space Center, Houston, TX, USA" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Scanning Transmission Electron Microscopy (STEM); High-Resolution TEM (HRTEM); STEM-EDS spectrum imaging" ] ;
    schema1:name "tem protocol — Thompson2020" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "CM2 carbonaceous chondrite (Murchison); laboratory-simulated progressively space-weathered chips (1×, 2×, 5× pulsed-laser irradiation passes)" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "Multi-technique coordinated study; TEM/STEM used for microstructural and chemical characterization of FIB-extracted sections from laser-irradiated Murchison chips; STEM results correlated with reflectance, FTIR, and organic chemistry data" ;
                    schema1:name "Pulsed laser irradiation (space weathering simulation); VIS-NIR reflectance spectroscopy (ASD FieldSpec 3); FTIR (Bruker Vertex/Hyperion); Mössbauer spectroscopy (MIMOS-II); μL2MS (two-step laser mass spectrometry); FIB-SEM (FEI Quanta 3D at JSC)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalSubModeDefault "BF-STEM" ;
    ada:cameraLengthDefault -9999 ;
    ada:convergenceSemiAngle -9999 ;
    ada:edsAcquisitionModeDefault "Map" ;
    ada:edsCalibrationStandardDefault "missing" ;
    ada:edsQuantificationMethod "missing" ;
    ada:eelsAcquisitionModeDefault "missing" ;
    ada:eelsAcquisitionTimePerSpectrumDefault -9999 ;
    ada:eelsCollectionSemiAngle -9999 ;
    ada:eelsEnergyLossRangeDefault "missing" ;
    ada:phaseIdentificationMethod "HRTEM lattice fringe imaging + FFT; EDS composition maps (no SAED; phase ID by d-spacings from HRTEM); phases identified: pentlandite, Fe-Ni-S, magnetite, serpentine, chrysotile, olivine, metallic Fe" ;
    ada:samplingUnit "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:spectroscopicDetectorDefault "N/A" ;
    ada:stemDwellTimePerPixelDefault "50 µs (kept short to prevent beam damage)" .

<https://ada.astromat.org/metadata/parameter/temTAPP/edsCountingStatisticsAccumulationCriterionDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Successive scans accumulated until major element counts achieved 1% counting statistics" ;
    schema1:name "EDS Counting Statistics / Accumulation Criterion" ;
    schema1:valueName "edsCountingStatisticsAccumulationCriterionDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/temTAPP/samplePreparationDetailsDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "FEI Quanta 3D FIB-SEM at JSC; four electron-transparent sections (<100 nm thick): (1) 1× matrix, (2) 5× matrix, (3) 5× sulfide grain, (4) 5× olivine grain" ;
    schema1:name "Sample Preparation Details" ;
    schema1:valueName "samplePreparationDetailsDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/temTAPP/stemFrameAveragingDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Successive scans accumulated until major element counts achieved 1% counting statistics" ;
    schema1:name "STEM Frame Averaging" ;
    schema1:valueName "stemFrameAveragingDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/temTAPP/stemProbeDiameterDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 2 ;
    schema1:description "2 nm" ;
    schema1:name "STEM Probe Diameter" ;
    schema1:valueName "stemProbeDiameterDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://example.org/instrument/TEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "TEM" ;
    schema1:hasPart <https://example.org/instrument/TEM/part/4D-STEM-Detector>,
        <https://example.org/instrument/TEM/part/Aberration-Corrector>,
        <https://example.org/instrument/TEM/part/EDS-Detector>,
        <https://example.org/instrument/TEM/part/EELS-Spectrometer>,
        <https://example.org/instrument/TEM/part/Electron-Source>,
        <https://example.org/instrument/TEM/part/Imaging-Detector>,
        <https://example.org/instrument/TEM/part/Monochromator> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "JEOL" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "JEOL 2500SE" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "200 kV" .

<https://example.org/instrument/TEM/part/4D-STEM-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "4D-STEM Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Aberration-Corrector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Aberration Corrector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:description "Thin-window Thermo energy-dispersive X-ray spectrometer; 50 mm² detector; configured for large solid-angle X-ray collection" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/EELS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EELS Spectrometer" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "Unknown" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Imaging-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Imaging Detector" ;
    schema1:description "BF detector; DF (ADF) detector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Monochromator> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Monochromator" ;
    schema1:name "missing" .


```


### temTAPP example Xing2023
temTAPP instance derived from Xing2023 | REVIEW: TEM methods for nanoscale mineralogy in NEPS | No original protocol data.
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
  "@id": "ex:temTAPP-Xing2023",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "tem protocol — Xing2023",
  "schema:description": "Review paper — no original analytical data. Key points: (1) FIB is dominant sample prep method in NEPS; plasma cleaning recommended to reduce contamination. (2) Aberration-corrected HAADF-STEM enables atomic-resolution phase ID. (3) Cryo-TEM holder recommended for beam-sensitive samples (clay minerals, Fe-Mn oxyhydroxides). (4) EDS detection limit ~1000 ppm; EELS preferred for trace elements and valence state analysis. DOI: 10.1021/acsearthspacechem.2c00278",
  "ada:edsQuantificationMethod": "EDS described as \"mostly semiquantitative\"; standard-based quantification (matched thickness/composition standard) achieves ~0.1% error; quantitative EDS rarely performed without standards",
  "ada:phaseIdentificationMethod": "Reviews SAED; NBD (nanobeam diffraction); CBED; HRTEM + FFT; aberration-corrected HAADF-STEM + FFT (atomic-resolution phase ID)",
  "ada:edsCalibrationStandardDefault": "Standard sample with similar thickness and chemical composition recommended for quantitative EDS; enables ~0.1% compositional error",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/temTAPP/edsDetectionLimitDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "edsDetectionLimitDefault",
      "schema:name": "EDS Detection Limit",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 1000,
      "schema:description": "EDS detection limit: ~1000 ppm (~0.1 wt%) for major elements"
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Review covers: FIB (described as most important method in NEPS); ultramicrotomy; Ar ion milling; powder dispersion on carbon-film grid",
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
        "schema:position": 2
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
      "schema:name": "tem",
      "schema:termCode": "tem"
    }
  ],
  "schema:instrument": [
    {
      "@id": "ex:instrument/TEM",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:additionalType": [
        "TEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:name": "missing",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "4D-STEM Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/4D-STEM-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Aberration Corrector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Aberration-Corrector"
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
          "@id": "ex:instrument/TEM/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EELS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/EELS-Spectrometer"
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
          "@id": "ex:instrument/TEM/part/Electron-Source"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Imaging Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Imaging-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Monochromator",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Monochromator"
        }
      ]
    }
  ],
  "ada:analyticalSubModeDefault": "missing",
  "ada:cameraLengthDefault": -9999,
  "ada:convergenceSemiAngle": -9999,
  "ada:edsAcquisitionModeDefault": "missing",
  "ada:eelsAcquisitionModeDefault": "missing",
  "ada:eelsAcquisitionTimePerSpectrumDefault": -9999,
  "ada:eelsCollectionSemiAngle": -9999,
  "ada:eelsEnergyLossRangeDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:spectroscopicDetectorDefault": "missing",
  "ada:stemDwellTimePerPixelDefault": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/TEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:temTAPP-Xing2023",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "tem protocol \u2014 Xing2023",
  "schema:description": "Review paper \u2014 no original analytical data. Key points: (1) FIB is dominant sample prep method in NEPS; plasma cleaning recommended to reduce contamination. (2) Aberration-corrected HAADF-STEM enables atomic-resolution phase ID. (3) Cryo-TEM holder recommended for beam-sensitive samples (clay minerals, Fe-Mn oxyhydroxides). (4) EDS detection limit ~1000 ppm; EELS preferred for trace elements and valence state analysis. DOI: 10.1021/acsearthspacechem.2c00278",
  "ada:edsQuantificationMethod": "EDS described as \"mostly semiquantitative\"; standard-based quantification (matched thickness/composition standard) achieves ~0.1% error; quantitative EDS rarely performed without standards",
  "ada:phaseIdentificationMethod": "Reviews SAED; NBD (nanobeam diffraction); CBED; HRTEM + FFT; aberration-corrected HAADF-STEM + FFT (atomic-resolution phase ID)",
  "ada:edsCalibrationStandardDefault": "Standard sample with similar thickness and chemical composition recommended for quantitative EDS; enables ~0.1% compositional error",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/temTAPP/edsDetectionLimitDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "edsDetectionLimitDefault",
      "schema:name": "EDS Detection Limit",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 1000,
      "schema:description": "EDS detection limit: ~1000 ppm (~0.1 wt%) for major elements"
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Review covers: FIB (described as most important method in NEPS); ultramicrotomy; Ar ion milling; powder dispersion on carbon-film grid",
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
        "schema:position": 2
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
      "schema:name": "tem",
      "schema:termCode": "tem"
    }
  ],
  "schema:instrument": [
    {
      "@id": "ex:instrument/TEM",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:additionalType": [
        "TEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:name": "missing",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "4D-STEM Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/4D-STEM-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Aberration Corrector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Aberration-Corrector"
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
          "@id": "ex:instrument/TEM/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EELS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/EELS-Spectrometer"
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
          "@id": "ex:instrument/TEM/part/Electron-Source"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Imaging Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Imaging-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Monochromator",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Monochromator"
        }
      ]
    }
  ],
  "ada:analyticalSubModeDefault": "missing",
  "ada:cameraLengthDefault": -9999,
  "ada:convergenceSemiAngle": -9999,
  "ada:edsAcquisitionModeDefault": "missing",
  "ada:eelsAcquisitionModeDefault": "missing",
  "ada:eelsAcquisitionTimePerSpectrumDefault": -9999,
  "ada:eelsCollectionSemiAngle": -9999,
  "ada:eelsEnergyLossRangeDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:spectroscopicDetectorDefault": "missing",
  "ada:stemDwellTimePerPixelDefault": -9999,
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

ex:temTAPP-Xing2023 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Review covers: FIB (described as most important method in NEPS); ultramicrotomy; Ar ion milling; powder dispersion on carbon-film grid" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/temTAPP/edsDetectionLimitDefault> ;
    schema1:datePublished "missing" ;
    schema1:description "Review paper — no original analytical data. Key points: (1) FIB is dominant sample prep method in NEPS; plasma cleaning recommended to reduce contamination. (2) Aberration-corrected HAADF-STEM enables atomic-resolution phase ID. (3) Cryo-TEM holder recommended for beam-sensitive samples (clay minerals, Fe-Mn oxyhydroxides). (4) EDS detection limit ~1000 ppm; EELS preferred for trace elements and valence state analysis. DOI: 10.1021/acsearthspacechem.2c00278" ;
    schema1:instrument <https://example.org/instrument/TEM> ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "tem" ;
            schema1:termCode "tem" ] ;
    schema1:name "tem protocol — Xing2023" ;
    ada:analyticalSubModeDefault "missing" ;
    ada:cameraLengthDefault -9999 ;
    ada:convergenceSemiAngle -9999 ;
    ada:edsAcquisitionModeDefault "missing" ;
    ada:edsCalibrationStandardDefault "Standard sample with similar thickness and chemical composition recommended for quantitative EDS; enables ~0.1% compositional error" ;
    ada:edsQuantificationMethod "EDS described as \"mostly semiquantitative\"; standard-based quantification (matched thickness/composition standard) achieves ~0.1% error; quantitative EDS rarely performed without standards" ;
    ada:eelsAcquisitionModeDefault "missing" ;
    ada:eelsAcquisitionTimePerSpectrumDefault -9999 ;
    ada:eelsCollectionSemiAngle -9999 ;
    ada:eelsEnergyLossRangeDefault "missing" ;
    ada:phaseIdentificationMethod "Reviews SAED; NBD (nanobeam diffraction); CBED; HRTEM + FFT; aberration-corrected HAADF-STEM + FFT (atomic-resolution phase ID)" ;
    ada:samplingUnit "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:spectroscopicDetectorDefault "missing" ;
    ada:stemDwellTimePerPixelDefault -9999 .

<https://ada.astromat.org/metadata/parameter/temTAPP/edsDetectionLimitDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1000 ;
    schema1:description "EDS detection limit: ~1000 ppm (~0.1 wt%) for major elements" ;
    schema1:name "EDS Detection Limit" ;
    schema1:valueName "edsDetectionLimitDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://example.org/instrument/TEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "TEM" ;
    schema1:hasPart <https://example.org/instrument/TEM/part/4D-STEM-Detector>,
        <https://example.org/instrument/TEM/part/Aberration-Corrector>,
        <https://example.org/instrument/TEM/part/EDS-Detector>,
        <https://example.org/instrument/TEM/part/EELS-Spectrometer>,
        <https://example.org/instrument/TEM/part/Electron-Source>,
        <https://example.org/instrument/TEM/part/Imaging-Detector>,
        <https://example.org/instrument/TEM/part/Monochromator> ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/4D-STEM-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "4D-STEM Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Aberration-Corrector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Aberration Corrector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/EELS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EELS Spectrometer" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Imaging-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Imaging Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Monochromator> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Monochromator" ;
    schema1:name "missing" .


```


### temTAPP example Seifert2026
temTAPP instance derived from Seifert2026 | Bennu OREX-803173-100 apatite | BF/DF-STEM + EDS (JSC JEOL 2500SE).
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
  "@id": "ex:temTAPP-Seifert2026",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "tem protocol — Seifert2026",
  "schema:description": "Same instrument (JEOL 2500SE at JSC ARES) as KellerBerger2014 and Thompson2020. HAADF-STEM images shown in Figures 5–7 but no HAADF angles stated. EDS compositions in Table 2 are normalized to 100%; actual quantification method not stated. FIB prep technique references: Holzapfel et al. 2009; Seifert et al. 2022; Zega et al. 2007. Reported detail: ada:analyticalSubModeDefault = BF-STEM; DF-STEM; HAADF-STEM; STEM-EDS mapping; ada:edsAcquisitionModeDefault = Spectrum imaging (EDS elemental maps); false-color RGB maps.",
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
            "Bennu carbonaceous asteroid sample (OSIRIS-REx return); apatite grains in phyllosilicate-rich matrix"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/temTAPP/samplePreparationDetailsDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "samplePreparationDetailsDefault",
            "schema:name": "Sample Preparation Details",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "FEI Quanta 3D FEG FIB-SEM at JSC; stair-step milling; in situ extraction; thinned to electron transparency (≤100 nm); techniques following Holzapfel et al. 2009, Seifert et al. 2022, Zega et al. 2007"
          }
        ],
        "schema:description": "FIB lift-out (Ga+)",
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
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:instrument": [
    {
      "schema:additionalType": [
        "TEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "JEOL 2500SE",
        "@type": [
          "schema:ProductModel"
        ]
      },
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
          "@id": "ex:instrument/TEM/part/Electron-Source",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "JEOL 60 mm² silicon-drift detector (SDD) for EDS",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/EDS-Detector",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "Imaging Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "BF STEM detector; DF STEM detector; SE STEM detector",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/Imaging-Detector",
          "schema:name": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "4D-STEM Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/4D-STEM-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Aberration Corrector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Aberration-Corrector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EELS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/EELS-Spectrometer"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Monochromator",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Monochromator"
        }
      ],
      "ada:acceleratingVoltageDefault": "200 kV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/TEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:spectroscopicDetectorDefault": "N/A",
  "ada:analyticalSubModeDefault": "BF-STEM",
  "ada:edsAcquisitionModeDefault": "Map",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Scanning Transmission Electron Microscopy (STEM); Energy-Dispersive X-ray Spectroscopy (EDS)"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Electron Beam Analysis Laboratories, ARES, NASA Johnson Space Center, Houston, TX, USA"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM (JEOL 7600F + 7900F with Oxford EDS/EBSD/CL at JSC); EMPA (JEOL 8530 at JSC, 15 kV 20 nA 2 µm probe)",
        "schema:description": "Coordinated SEM-EMPA-TEM study of Bennu apatite; TEM provides nanoscale crystallographic and chemical characterization of FIB section from apatite cluster; SAED confirms single-crystal vs. polycrystalline nature"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:cameraLengthDefault": -9999,
  "ada:convergenceSemiAngle": -9999,
  "ada:edsCalibrationStandardDefault": "missing",
  "ada:edsQuantificationMethod": "missing",
  "ada:eelsAcquisitionModeDefault": "missing",
  "ada:eelsAcquisitionTimePerSpectrumDefault": -9999,
  "ada:eelsCollectionSemiAngle": -9999,
  "ada:eelsEnergyLossRangeDefault": "missing",
  "ada:phaseIdentificationMethod": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stemDwellTimePerPixelDefault": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/TEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:temTAPP-Seifert2026",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "tem protocol \u2014 Seifert2026",
  "schema:description": "Same instrument (JEOL 2500SE at JSC ARES) as KellerBerger2014 and Thompson2020. HAADF-STEM images shown in Figures 5\u20137 but no HAADF angles stated. EDS compositions in Table 2 are normalized to 100%; actual quantification method not stated. FIB prep technique references: Holzapfel et al. 2009; Seifert et al. 2022; Zega et al. 2007. Reported detail: ada:analyticalSubModeDefault = BF-STEM; DF-STEM; HAADF-STEM; STEM-EDS mapping; ada:edsAcquisitionModeDefault = Spectrum imaging (EDS elemental maps); false-color RGB maps.",
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
            "Bennu carbonaceous asteroid sample (OSIRIS-REx return); apatite grains in phyllosilicate-rich matrix"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/temTAPP/samplePreparationDetailsDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "samplePreparationDetailsDefault",
            "schema:name": "Sample Preparation Details",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "FEI Quanta 3D FEG FIB-SEM at JSC; stair-step milling; in situ extraction; thinned to electron transparency (\u2264100 nm); techniques following Holzapfel et al. 2009, Seifert et al. 2022, Zega et al. 2007"
          }
        ],
        "schema:description": "FIB lift-out (Ga+)",
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
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:instrument": [
    {
      "schema:additionalType": [
        "TEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "JEOL 2500SE",
        "@type": [
          "schema:ProductModel"
        ]
      },
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
          "@id": "ex:instrument/TEM/part/Electron-Source",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "JEOL 60 mm\u00b2 silicon-drift detector (SDD) for EDS",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/EDS-Detector",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "Imaging Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "BF STEM detector; DF STEM detector; SE STEM detector",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/Imaging-Detector",
          "schema:name": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "4D-STEM Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/4D-STEM-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Aberration Corrector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Aberration-Corrector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EELS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/EELS-Spectrometer"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Monochromator",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Monochromator"
        }
      ],
      "ada:acceleratingVoltageDefault": "200 kV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/TEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:spectroscopicDetectorDefault": "N/A",
  "ada:analyticalSubModeDefault": "BF-STEM",
  "ada:edsAcquisitionModeDefault": "Map",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Scanning Transmission Electron Microscopy (STEM); Energy-Dispersive X-ray Spectroscopy (EDS)"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Electron Beam Analysis Laboratories, ARES, NASA Johnson Space Center, Houston, TX, USA"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM (JEOL 7600F + 7900F with Oxford EDS/EBSD/CL at JSC); EMPA (JEOL 8530 at JSC, 15 kV 20 nA 2 \u00b5m probe)",
        "schema:description": "Coordinated SEM-EMPA-TEM study of Bennu apatite; TEM provides nanoscale crystallographic and chemical characterization of FIB section from apatite cluster; SAED confirms single-crystal vs. polycrystalline nature"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:cameraLengthDefault": -9999,
  "ada:convergenceSemiAngle": -9999,
  "ada:edsCalibrationStandardDefault": "missing",
  "ada:edsQuantificationMethod": "missing",
  "ada:eelsAcquisitionModeDefault": "missing",
  "ada:eelsAcquisitionTimePerSpectrumDefault": -9999,
  "ada:eelsCollectionSemiAngle": -9999,
  "ada:eelsEnergyLossRangeDefault": "missing",
  "ada:phaseIdentificationMethod": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stemDwellTimePerPixelDefault": -9999,
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

ex:temTAPP-Seifert2026 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/temTAPP/samplePreparationDetailsDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "FIB lift-out (Ga+)" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "Same instrument (JEOL 2500SE at JSC ARES) as KellerBerger2014 and Thompson2020. HAADF-STEM images shown in Figures 5–7 but no HAADF angles stated. EDS compositions in Table 2 are normalized to 100%; actual quantification method not stated. FIB prep technique references: Holzapfel et al. 2009; Seifert et al. 2022; Zega et al. 2007. Reported detail: ada:analyticalSubModeDefault = BF-STEM; DF-STEM; HAADF-STEM; STEM-EDS mapping; ada:edsAcquisitionModeDefault = Spectrum imaging (EDS elemental maps); false-color RGB maps." ;
    schema1:instrument <https://example.org/instrument/TEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Electron Beam Analysis Laboratories, ARES, NASA Johnson Space Center, Houston, TX, USA" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Scanning Transmission Electron Microscopy (STEM); Energy-Dispersive X-ray Spectroscopy (EDS)" ] ;
    schema1:name "tem protocol — Seifert2026" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Bennu carbonaceous asteroid sample (OSIRIS-REx return); apatite grains in phyllosilicate-rich matrix" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "Coordinated SEM-EMPA-TEM study of Bennu apatite; TEM provides nanoscale crystallographic and chemical characterization of FIB section from apatite cluster; SAED confirms single-crystal vs. polycrystalline nature" ;
                    schema1:name "SEM (JEOL 7600F + 7900F with Oxford EDS/EBSD/CL at JSC); EMPA (JEOL 8530 at JSC, 15 kV 20 nA 2 µm probe)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalSubModeDefault "BF-STEM" ;
    ada:cameraLengthDefault -9999 ;
    ada:convergenceSemiAngle -9999 ;
    ada:edsAcquisitionModeDefault "Map" ;
    ada:edsCalibrationStandardDefault "missing" ;
    ada:edsQuantificationMethod "missing" ;
    ada:eelsAcquisitionModeDefault "missing" ;
    ada:eelsAcquisitionTimePerSpectrumDefault -9999 ;
    ada:eelsCollectionSemiAngle -9999 ;
    ada:eelsEnergyLossRangeDefault "missing" ;
    ada:phaseIdentificationMethod "missing" ;
    ada:samplingUnit "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:spectroscopicDetectorDefault "N/A" ;
    ada:stemDwellTimePerPixelDefault -9999 .

<https://ada.astromat.org/metadata/parameter/temTAPP/samplePreparationDetailsDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "FEI Quanta 3D FEG FIB-SEM at JSC; stair-step milling; in situ extraction; thinned to electron transparency (≤100 nm); techniques following Holzapfel et al. 2009, Seifert et al. 2022, Zega et al. 2007" ;
    schema1:name "Sample Preparation Details" ;
    schema1:valueName "samplePreparationDetailsDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://example.org/instrument/TEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "TEM" ;
    schema1:hasPart <https://example.org/instrument/TEM/part/4D-STEM-Detector>,
        <https://example.org/instrument/TEM/part/Aberration-Corrector>,
        <https://example.org/instrument/TEM/part/EDS-Detector>,
        <https://example.org/instrument/TEM/part/EELS-Spectrometer>,
        <https://example.org/instrument/TEM/part/Electron-Source>,
        <https://example.org/instrument/TEM/part/Imaging-Detector>,
        <https://example.org/instrument/TEM/part/Monochromator> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "JEOL" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "JEOL 2500SE" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "200 kV" .

<https://example.org/instrument/TEM/part/4D-STEM-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "4D-STEM Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Aberration-Corrector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Aberration Corrector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:description "JEOL 60 mm² silicon-drift detector (SDD) for EDS" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/EELS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EELS Spectrometer" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "Unknown" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Imaging-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Imaging Detector" ;
    schema1:description "BF STEM detector; DF STEM detector; SE STEM detector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Monochromator> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Monochromator" ;
    schema1:name "missing" .


```


### temTAPP example Seifert2026-2
temTAPP instance derived from Seifert2026 | Bennu OREX-803173-100 apatite | HAADF-STEM + dual EDS + TEM/SAED (K-ALFAA UA Hitachi HF5000, probe Cs-corrected).
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
  "@id": "ex:temTAPP-Seifert2026-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "tem protocol — Seifert2026-2",
  "schema:description": "HF5000 at K-ALFAA, UA. Gatan OneView camera used for both TEM images and SAED. Probe Cs corrector (3rd-order) present but corrector settings not stated. SAED DIFPack calibration reference not stated. This is the same facility (K-ALFAA) used by Zega2025 (Goethe-UA column). Data deposited at astromat.org per Table S1. Reported detail: ada:analyticalSubModeDefault = BF-STEM; DF-STEM; HAADF-STEM; TEM (BF-TEM); SAED; STEM-EDS mapping; ada:edsAcquisitionModeDefault = Spectrum imaging (EDS elemental maps); false-color maps.",
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
            "Bennu carbonaceous asteroid sample (OSIRIS-REx return); apatite grains in phyllosilicate-rich matrix"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/temTAPP/samplePreparationDetailsDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "samplePreparationDetailsDefault",
            "schema:name": "Sample Preparation Details",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "FEI Quanta 3D FEG FIB-SEM at JSC; stair-step milling; in situ extraction; thinned to electron transparency (≤100 nm); techniques following Holzapfel et al. 2009, Seifert et al. 2022, Zega et al. 2007"
          }
        ],
        "schema:description": "FIB lift-out (Ga+)",
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
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:instrument": [
    {
      "schema:additionalType": [
        "TEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "Hitachi",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "Hitachi HF5000",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Cold-FEG",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/Electron-Source",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "Aberration Corrector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Unknown",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/Aberration-Corrector",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Oxford Instruments X-Max N 100 TLE EDS system; dual 100 mm² windowless silicon-drift detectors",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/EDS-Detector",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "Imaging Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "BF STEM detector; DF STEM detector; SE STEM detector; Gatan OneView 4k×4k pixel CMOS camera (TEM imaging and SAED)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/Imaging-Detector",
          "schema:name": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "4D-STEM Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/4D-STEM-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EELS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/EELS-Spectrometer"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Monochromator",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Monochromator"
        }
      ],
      "ada:acceleratingVoltageDefault": "200 kV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/TEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:spectroscopicDetectorDefault": "N/A",
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "SingleCrystal (CrystalMaker Software)"
    },
    {
      "ada:toolRole": "acquisition",
      "schema:name": "Gatan DIFPack (SAED pattern measurement); SingleCrystal (simulated diffraction patterns)"
    }
  ],
  "ada:analyticalSubModeDefault": "BF-STEM",
  "ada:edsAcquisitionModeDefault": "Map",
  "ada:phaseIdentificationMethod": "SAED zone-axis patterns measured with Gatan DIFPack; compared to simulated diffraction patterns using SingleCrystal software package; confirms apatite single crystal (Ap.#1) and polycrystalline assemblage (Ap.#2)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Scanning Transmission Electron Microscopy (STEM); Energy-Dispersive X-ray Spectroscopy (EDS)"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Kuiper-Arizona Laboratory for Astromaterials Analysis (K-ALFAA), Lunar and Planetary Laboratory, University of Arizona, Tucson, AZ, USA"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM (JEOL 7600F + 7900F with Oxford EDS/EBSD/CL at JSC); EMPA (JEOL 8530 at JSC, 15 kV 20 nA 2 µm probe)",
        "schema:description": "Coordinated SEM-EMPA-TEM study of Bennu apatite; TEM provides nanoscale crystallographic and chemical characterization of FIB section from apatite cluster; SAED confirms single-crystal vs. polycrystalline nature"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:cameraLengthDefault": -9999,
  "ada:convergenceSemiAngle": -9999,
  "ada:edsCalibrationStandardDefault": "missing",
  "ada:edsQuantificationMethod": "missing",
  "ada:eelsAcquisitionModeDefault": "missing",
  "ada:eelsAcquisitionTimePerSpectrumDefault": -9999,
  "ada:eelsCollectionSemiAngle": -9999,
  "ada:eelsEnergyLossRangeDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stemDwellTimePerPixelDefault": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/TEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:temTAPP-Seifert2026-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "tem protocol \u2014 Seifert2026-2",
  "schema:description": "HF5000 at K-ALFAA, UA. Gatan OneView camera used for both TEM images and SAED. Probe Cs corrector (3rd-order) present but corrector settings not stated. SAED DIFPack calibration reference not stated. This is the same facility (K-ALFAA) used by Zega2025 (Goethe-UA column). Data deposited at astromat.org per Table S1. Reported detail: ada:analyticalSubModeDefault = BF-STEM; DF-STEM; HAADF-STEM; TEM (BF-TEM); SAED; STEM-EDS mapping; ada:edsAcquisitionModeDefault = Spectrum imaging (EDS elemental maps); false-color maps.",
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
            "Bennu carbonaceous asteroid sample (OSIRIS-REx return); apatite grains in phyllosilicate-rich matrix"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/temTAPP/samplePreparationDetailsDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "samplePreparationDetailsDefault",
            "schema:name": "Sample Preparation Details",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "FEI Quanta 3D FEG FIB-SEM at JSC; stair-step milling; in situ extraction; thinned to electron transparency (\u2264100 nm); techniques following Holzapfel et al. 2009, Seifert et al. 2022, Zega et al. 2007"
          }
        ],
        "schema:description": "FIB lift-out (Ga+)",
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
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:instrument": [
    {
      "schema:additionalType": [
        "TEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "Hitachi",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "Hitachi HF5000",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Cold-FEG",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/Electron-Source",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "Aberration Corrector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Unknown",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/Aberration-Corrector",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Oxford Instruments X-Max N 100 TLE EDS system; dual 100 mm\u00b2 windowless silicon-drift detectors",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/EDS-Detector",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "Imaging Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "BF STEM detector; DF STEM detector; SE STEM detector; Gatan OneView 4k\u00d74k pixel CMOS camera (TEM imaging and SAED)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/Imaging-Detector",
          "schema:name": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "4D-STEM Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/4D-STEM-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EELS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/EELS-Spectrometer"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Monochromator",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Monochromator"
        }
      ],
      "ada:acceleratingVoltageDefault": "200 kV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/TEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:spectroscopicDetectorDefault": "N/A",
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "SingleCrystal (CrystalMaker Software)"
    },
    {
      "ada:toolRole": "acquisition",
      "schema:name": "Gatan DIFPack (SAED pattern measurement); SingleCrystal (simulated diffraction patterns)"
    }
  ],
  "ada:analyticalSubModeDefault": "BF-STEM",
  "ada:edsAcquisitionModeDefault": "Map",
  "ada:phaseIdentificationMethod": "SAED zone-axis patterns measured with Gatan DIFPack; compared to simulated diffraction patterns using SingleCrystal software package; confirms apatite single crystal (Ap.#1) and polycrystalline assemblage (Ap.#2)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Scanning Transmission Electron Microscopy (STEM); Energy-Dispersive X-ray Spectroscopy (EDS)"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Kuiper-Arizona Laboratory for Astromaterials Analysis (K-ALFAA), Lunar and Planetary Laboratory, University of Arizona, Tucson, AZ, USA"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM (JEOL 7600F + 7900F with Oxford EDS/EBSD/CL at JSC); EMPA (JEOL 8530 at JSC, 15 kV 20 nA 2 \u00b5m probe)",
        "schema:description": "Coordinated SEM-EMPA-TEM study of Bennu apatite; TEM provides nanoscale crystallographic and chemical characterization of FIB section from apatite cluster; SAED confirms single-crystal vs. polycrystalline nature"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:cameraLengthDefault": -9999,
  "ada:convergenceSemiAngle": -9999,
  "ada:edsCalibrationStandardDefault": "missing",
  "ada:edsQuantificationMethod": "missing",
  "ada:eelsAcquisitionModeDefault": "missing",
  "ada:eelsAcquisitionTimePerSpectrumDefault": -9999,
  "ada:eelsCollectionSemiAngle": -9999,
  "ada:eelsEnergyLossRangeDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stemDwellTimePerPixelDefault": -9999,
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

ex:temTAPP-Seifert2026-2 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/temTAPP/samplePreparationDetailsDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "FIB lift-out (Ga+)" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "HF5000 at K-ALFAA, UA. Gatan OneView camera used for both TEM images and SAED. Probe Cs corrector (3rd-order) present but corrector settings not stated. SAED DIFPack calibration reference not stated. This is the same facility (K-ALFAA) used by Zega2025 (Goethe-UA column). Data deposited at astromat.org per Table S1. Reported detail: ada:analyticalSubModeDefault = BF-STEM; DF-STEM; HAADF-STEM; TEM (BF-TEM); SAED; STEM-EDS mapping; ada:edsAcquisitionModeDefault = Spectrum imaging (EDS elemental maps); false-color maps." ;
    schema1:instrument <https://example.org/instrument/TEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Kuiper-Arizona Laboratory for Astromaterials Analysis (K-ALFAA), Lunar and Planetary Laboratory, University of Arizona, Tucson, AZ, USA" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Scanning Transmission Electron Microscopy (STEM); Energy-Dispersive X-ray Spectroscopy (EDS)" ] ;
    schema1:name "tem protocol — Seifert2026-2" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Bennu carbonaceous asteroid sample (OSIRIS-REx return); apatite grains in phyllosilicate-rich matrix" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "Coordinated SEM-EMPA-TEM study of Bennu apatite; TEM provides nanoscale crystallographic and chemical characterization of FIB section from apatite cluster; SAED confirms single-crystal vs. polycrystalline nature" ;
                    schema1:name "SEM (JEOL 7600F + 7900F with Oxford EDS/EBSD/CL at JSC); EMPA (JEOL 8530 at JSC, 15 kV 20 nA 2 µm probe)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalSubModeDefault "BF-STEM" ;
    ada:cameraLengthDefault -9999 ;
    ada:convergenceSemiAngle -9999 ;
    ada:edsAcquisitionModeDefault "Map" ;
    ada:edsCalibrationStandardDefault "missing" ;
    ada:edsQuantificationMethod "missing" ;
    ada:eelsAcquisitionModeDefault "missing" ;
    ada:eelsAcquisitionTimePerSpectrumDefault -9999 ;
    ada:eelsCollectionSemiAngle -9999 ;
    ada:eelsEnergyLossRangeDefault "missing" ;
    ada:phaseIdentificationMethod "SAED zone-axis patterns measured with Gatan DIFPack; compared to simulated diffraction patterns using SingleCrystal software package; confirms apatite single crystal (Ap.#1) and polycrystalline assemblage (Ap.#2)" ;
    ada:samplingUnit "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:spectroscopicDetectorDefault "N/A" ;
    ada:stemDwellTimePerPixelDefault -9999 ;
    bios:computationalTool [ schema1:name "Gatan DIFPack (SAED pattern measurement); SingleCrystal (simulated diffraction patterns)" ;
            ada:toolRole "acquisition" ],
        [ schema1:name "SingleCrystal (CrystalMaker Software)" ;
            ada:toolRole "dataReduction" ] .

<https://ada.astromat.org/metadata/parameter/temTAPP/samplePreparationDetailsDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "FEI Quanta 3D FEG FIB-SEM at JSC; stair-step milling; in situ extraction; thinned to electron transparency (≤100 nm); techniques following Holzapfel et al. 2009, Seifert et al. 2022, Zega et al. 2007" ;
    schema1:name "Sample Preparation Details" ;
    schema1:valueName "samplePreparationDetailsDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://example.org/instrument/TEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "TEM" ;
    schema1:hasPart <https://example.org/instrument/TEM/part/4D-STEM-Detector>,
        <https://example.org/instrument/TEM/part/Aberration-Corrector>,
        <https://example.org/instrument/TEM/part/EDS-Detector>,
        <https://example.org/instrument/TEM/part/EELS-Spectrometer>,
        <https://example.org/instrument/TEM/part/Electron-Source>,
        <https://example.org/instrument/TEM/part/Imaging-Detector>,
        <https://example.org/instrument/TEM/part/Monochromator> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Hitachi" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Hitachi HF5000" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "200 kV" .

<https://example.org/instrument/TEM/part/4D-STEM-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "4D-STEM Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Aberration-Corrector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Aberration Corrector" ;
    schema1:description "Unknown" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:description "Oxford Instruments X-Max N 100 TLE EDS system; dual 100 mm² windowless silicon-drift detectors" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/EELS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EELS Spectrometer" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "Cold-FEG" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Imaging-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Imaging Detector" ;
    schema1:description "BF STEM detector; DF STEM detector; SE STEM detector; Gatan OneView 4k×4k pixel CMOS camera (TEM imaging and SAED)" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Monochromator> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Monochromator" ;
    schema1:name "missing" .


```


### temTAPP example Cymes2023
temTAPP instance derived from Cymes2023 | Apollo 17 soil 71501 pyroxene (1pyx + 2pyx) | BF/EFTEM + SAED + HRTEM (NRL JEOL JEM-2200FS).
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
  "@id": "ex:temTAPP-Cymes2023",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "tem protocol — Cymes2023",
  "schema:description": "JEOL JEM-2200FS at NRL with in-column Omega energy filter; Gatan OneView camera; 200 keV. EFTEM Ca M-edge mapping (35 eV loss, 10-eV slit) used to distinguish Ca-rich augite from Ca-poor pigeonite lamellae in exsolved grain \"2pyx\". SAED simulated with SingleCrystal (CrystalMaker Software); [1-11] zone axis of pigeonite (P2₁/c) and augite (C2/c) confirmed. HRTEM + inverse FFT (spot-pass filter) for lattice deformation visualization. FIB section stored under N₂ and baked 140°C/8h under vacuum before TEM. Coordinated with Nion UltraSTEM200-X (same FIB section). Pt-welded to Cu TEM half-grid after initial in situ thinning. Reported detail: ada:analyticalSubModeDefault = BF-TEM; EFTEM (Ca M-edge, 35 eV loss, 10-eV slit); SAED; HRTEM.",
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
            "Apollo 17 soil 71501 (<45 µm fraction); pyroxene grains \"1pyx\" (unexsolved augite) and \"2pyx\" (exsolved pigeonite-augite intergrowth); one FIB section analyzed on two instruments"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/temTAPP/samplePreparationDetailsDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "samplePreparationDetailsDefault",
            "schema:name": "Sample Preparation Details",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "FEI Helios G3 Dual Beam FIB-SEM at NRL; ~80 nm amorphous C coating applied to grain before FIB; 1–2 µm e-beam amorphous C protection strip; initial in situ thinning to ~1–2 µm, then Pt-welded to Cu TEM half-grid; thinned to ~80–100 nm; stored under N₂; baked 140°C for 8 h under vacuum before TEM"
          }
        ],
        "schema:description": "FIB lift-out (Ga+)",
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
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/temTAPP/imageProcessingMethodsAppliedDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "imageProcessingMethodsAppliedDefault",
            "schema:name": "Image Processing Methods Applied",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Inverse FFT with spot-pass filter for HRTEM images"
          }
        ],
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
  "schema:instrument": [
    {
      "schema:additionalType": [
        "TEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "JEOL JEM-2200FS",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "EELS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "JEOL in-column Omega energy filter (EFTEM mode; 10-eV slit; used for Ca M-edge mapping at 35 eV energy loss)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/EELS-Spectrometer",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "Imaging Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "BF TEM detector; Gatan OneView CMOS camera (TEM imaging, SAED, HRTEM)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/Imaging-Detector",
          "schema:name": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "4D-STEM Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/4D-STEM-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Aberration Corrector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Aberration-Corrector"
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
          "@id": "ex:instrument/TEM/part/EDS-Detector"
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
          "@id": "ex:instrument/TEM/part/Electron-Source"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Monochromator",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Monochromator"
        }
      ],
      "ada:acceleratingVoltageDefault": "200 keV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/TEM",
      "schema:name": "example instrumentName"
    }
  ],
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "SingleCrystal (CrystalMaker Software, Ltd., Oxford, UK)"
    }
  ],
  "ada:analyticalSubModeDefault": "BF-TEM",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/temTAPP/eftemEnergyWindowDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "eftemEnergyWindowDefault",
      "schema:name": "EFTEM Energy Window",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "10 eV (Ca M-edge EFTEM centered at 35 eV energy loss)"
    },
    {
      "@id": "ada:parameter/temTAPP/selectedAreaApertureSizeDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "selectedAreaApertureSizeDefault",
      "schema:name": "Selected-Area Aperture Size",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "100 nm (SAED aperture)"
    }
  ],
  "ada:phaseIdentificationMethod": "SAED zone-axis patterns; simulated SAED patterns using SingleCrystal (CrystalMaker Software); HRTEM lattice fringe imaging + FFT; inverse FFT with spot-pass filter (lattice deformation visualization)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Transmission Electron Microscopy (TEM); Energy-Filtered TEM (EFTEM); Selected Area Electron Diffraction (SAED); High-Resolution TEM (HRTEM)"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Naval Research Laboratory, Washington, D.C., USA"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "FIB (FEI Helios G3 Dual Beam at NRL); HAADF-STEM + Dual EELS + EDS (Nion UltraSTEM200-X at NRL; coordinated with JEOL JEM-2200FS)",
        "schema:description": "Petrographic and crystallographic characterization of exsolved lunar pyroxene (Apollo 17 soil); phase ID by SAED + simulation; Ca distribution by EFTEM; HRTEM lattice imaging; coordinated with EELS on Nion UltraSTEM200-X"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:cameraLengthDefault": -9999,
  "ada:convergenceSemiAngle": -9999,
  "ada:edsAcquisitionModeDefault": "missing",
  "ada:edsCalibrationStandardDefault": "missing",
  "ada:edsQuantificationMethod": "missing",
  "ada:eelsAcquisitionModeDefault": "missing",
  "ada:eelsAcquisitionTimePerSpectrumDefault": -9999,
  "ada:eelsCollectionSemiAngle": -9999,
  "ada:eelsEnergyLossRangeDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:spectroscopicDetectorDefault": "missing",
  "ada:stemDwellTimePerPixelDefault": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/TEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:temTAPP-Cymes2023",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "tem protocol \u2014 Cymes2023",
  "schema:description": "JEOL JEM-2200FS at NRL with in-column Omega energy filter; Gatan OneView camera; 200 keV. EFTEM Ca M-edge mapping (35 eV loss, 10-eV slit) used to distinguish Ca-rich augite from Ca-poor pigeonite lamellae in exsolved grain \"2pyx\". SAED simulated with SingleCrystal (CrystalMaker Software); [1-11] zone axis of pigeonite (P2\u2081/c) and augite (C2/c) confirmed. HRTEM + inverse FFT (spot-pass filter) for lattice deformation visualization. FIB section stored under N\u2082 and baked 140\u00b0C/8h under vacuum before TEM. Coordinated with Nion UltraSTEM200-X (same FIB section). Pt-welded to Cu TEM half-grid after initial in situ thinning. Reported detail: ada:analyticalSubModeDefault = BF-TEM; EFTEM (Ca M-edge, 35 eV loss, 10-eV slit); SAED; HRTEM.",
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
            "Apollo 17 soil 71501 (<45 \u00b5m fraction); pyroxene grains \"1pyx\" (unexsolved augite) and \"2pyx\" (exsolved pigeonite-augite intergrowth); one FIB section analyzed on two instruments"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/temTAPP/samplePreparationDetailsDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "samplePreparationDetailsDefault",
            "schema:name": "Sample Preparation Details",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "FEI Helios G3 Dual Beam FIB-SEM at NRL; ~80 nm amorphous C coating applied to grain before FIB; 1\u20132 \u00b5m e-beam amorphous C protection strip; initial in situ thinning to ~1\u20132 \u00b5m, then Pt-welded to Cu TEM half-grid; thinned to ~80\u2013100 nm; stored under N\u2082; baked 140\u00b0C for 8 h under vacuum before TEM"
          }
        ],
        "schema:description": "FIB lift-out (Ga+)",
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
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/temTAPP/imageProcessingMethodsAppliedDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "imageProcessingMethodsAppliedDefault",
            "schema:name": "Image Processing Methods Applied",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Inverse FFT with spot-pass filter for HRTEM images"
          }
        ],
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
  "schema:instrument": [
    {
      "schema:additionalType": [
        "TEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "JEOL JEM-2200FS",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "EELS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "JEOL in-column Omega energy filter (EFTEM mode; 10-eV slit; used for Ca M-edge mapping at 35 eV energy loss)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/EELS-Spectrometer",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "Imaging Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "BF TEM detector; Gatan OneView CMOS camera (TEM imaging, SAED, HRTEM)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/Imaging-Detector",
          "schema:name": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "4D-STEM Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/4D-STEM-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Aberration Corrector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Aberration-Corrector"
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
          "@id": "ex:instrument/TEM/part/EDS-Detector"
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
          "@id": "ex:instrument/TEM/part/Electron-Source"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Monochromator",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Monochromator"
        }
      ],
      "ada:acceleratingVoltageDefault": "200 keV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/TEM",
      "schema:name": "example instrumentName"
    }
  ],
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "SingleCrystal (CrystalMaker Software, Ltd., Oxford, UK)"
    }
  ],
  "ada:analyticalSubModeDefault": "BF-TEM",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/temTAPP/eftemEnergyWindowDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "eftemEnergyWindowDefault",
      "schema:name": "EFTEM Energy Window",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "10 eV (Ca M-edge EFTEM centered at 35 eV energy loss)"
    },
    {
      "@id": "ada:parameter/temTAPP/selectedAreaApertureSizeDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "selectedAreaApertureSizeDefault",
      "schema:name": "Selected-Area Aperture Size",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "100 nm (SAED aperture)"
    }
  ],
  "ada:phaseIdentificationMethod": "SAED zone-axis patterns; simulated SAED patterns using SingleCrystal (CrystalMaker Software); HRTEM lattice fringe imaging + FFT; inverse FFT with spot-pass filter (lattice deformation visualization)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Transmission Electron Microscopy (TEM); Energy-Filtered TEM (EFTEM); Selected Area Electron Diffraction (SAED); High-Resolution TEM (HRTEM)"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Naval Research Laboratory, Washington, D.C., USA"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "FIB (FEI Helios G3 Dual Beam at NRL); HAADF-STEM + Dual EELS + EDS (Nion UltraSTEM200-X at NRL; coordinated with JEOL JEM-2200FS)",
        "schema:description": "Petrographic and crystallographic characterization of exsolved lunar pyroxene (Apollo 17 soil); phase ID by SAED + simulation; Ca distribution by EFTEM; HRTEM lattice imaging; coordinated with EELS on Nion UltraSTEM200-X"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:cameraLengthDefault": -9999,
  "ada:convergenceSemiAngle": -9999,
  "ada:edsAcquisitionModeDefault": "missing",
  "ada:edsCalibrationStandardDefault": "missing",
  "ada:edsQuantificationMethod": "missing",
  "ada:eelsAcquisitionModeDefault": "missing",
  "ada:eelsAcquisitionTimePerSpectrumDefault": -9999,
  "ada:eelsCollectionSemiAngle": -9999,
  "ada:eelsEnergyLossRangeDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:spectroscopicDetectorDefault": "missing",
  "ada:stemDwellTimePerPixelDefault": -9999,
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

ex:temTAPP-Cymes2023 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/temTAPP/imageProcessingMethodsAppliedDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/temTAPP/samplePreparationDetailsDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "FIB lift-out (Ga+)" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/temTAPP/eftemEnergyWindowDefault>,
        <https://ada.astromat.org/metadata/parameter/temTAPP/selectedAreaApertureSizeDefault> ;
    schema1:datePublished "missing" ;
    schema1:description "JEOL JEM-2200FS at NRL with in-column Omega energy filter; Gatan OneView camera; 200 keV. EFTEM Ca M-edge mapping (35 eV loss, 10-eV slit) used to distinguish Ca-rich augite from Ca-poor pigeonite lamellae in exsolved grain \"2pyx\". SAED simulated with SingleCrystal (CrystalMaker Software); [1-11] zone axis of pigeonite (P2₁/c) and augite (C2/c) confirmed. HRTEM + inverse FFT (spot-pass filter) for lattice deformation visualization. FIB section stored under N₂ and baked 140°C/8h under vacuum before TEM. Coordinated with Nion UltraSTEM200-X (same FIB section). Pt-welded to Cu TEM half-grid after initial in situ thinning. Reported detail: ada:analyticalSubModeDefault = BF-TEM; EFTEM (Ca M-edge, 35 eV loss, 10-eV slit); SAED; HRTEM." ;
    schema1:instrument <https://example.org/instrument/TEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Naval Research Laboratory, Washington, D.C., USA" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Transmission Electron Microscopy (TEM); Energy-Filtered TEM (EFTEM); Selected Area Electron Diffraction (SAED); High-Resolution TEM (HRTEM)" ] ;
    schema1:name "tem protocol — Cymes2023" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Apollo 17 soil 71501 (<45 µm fraction); pyroxene grains \"1pyx\" (unexsolved augite) and \"2pyx\" (exsolved pigeonite-augite intergrowth); one FIB section analyzed on two instruments" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "Petrographic and crystallographic characterization of exsolved lunar pyroxene (Apollo 17 soil); phase ID by SAED + simulation; Ca distribution by EFTEM; HRTEM lattice imaging; coordinated with EELS on Nion UltraSTEM200-X" ;
                    schema1:name "FIB (FEI Helios G3 Dual Beam at NRL); HAADF-STEM + Dual EELS + EDS (Nion UltraSTEM200-X at NRL; coordinated with JEOL JEM-2200FS)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalSubModeDefault "BF-TEM" ;
    ada:cameraLengthDefault -9999 ;
    ada:convergenceSemiAngle -9999 ;
    ada:edsAcquisitionModeDefault "missing" ;
    ada:edsCalibrationStandardDefault "missing" ;
    ada:edsQuantificationMethod "missing" ;
    ada:eelsAcquisitionModeDefault "missing" ;
    ada:eelsAcquisitionTimePerSpectrumDefault -9999 ;
    ada:eelsCollectionSemiAngle -9999 ;
    ada:eelsEnergyLossRangeDefault "missing" ;
    ada:phaseIdentificationMethod "SAED zone-axis patterns; simulated SAED patterns using SingleCrystal (CrystalMaker Software); HRTEM lattice fringe imaging + FFT; inverse FFT with spot-pass filter (lattice deformation visualization)" ;
    ada:samplingUnit "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:spectroscopicDetectorDefault "missing" ;
    ada:stemDwellTimePerPixelDefault -9999 ;
    bios:computationalTool [ schema1:name "SingleCrystal (CrystalMaker Software, Ltd., Oxford, UK)" ;
            ada:toolRole "dataReduction" ] .

<https://ada.astromat.org/metadata/parameter/temTAPP/eftemEnergyWindowDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "10 eV (Ca M-edge EFTEM centered at 35 eV energy loss)" ;
    schema1:name "EFTEM Energy Window" ;
    schema1:valueName "eftemEnergyWindowDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/temTAPP/imageProcessingMethodsAppliedDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Inverse FFT with spot-pass filter for HRTEM images" ;
    schema1:name "Image Processing Methods Applied" ;
    schema1:valueName "imageProcessingMethodsAppliedDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/temTAPP/samplePreparationDetailsDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "FEI Helios G3 Dual Beam FIB-SEM at NRL; ~80 nm amorphous C coating applied to grain before FIB; 1–2 µm e-beam amorphous C protection strip; initial in situ thinning to ~1–2 µm, then Pt-welded to Cu TEM half-grid; thinned to ~80–100 nm; stored under N₂; baked 140°C for 8 h under vacuum before TEM" ;
    schema1:name "Sample Preparation Details" ;
    schema1:valueName "samplePreparationDetailsDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/temTAPP/selectedAreaApertureSizeDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "100 nm (SAED aperture)" ;
    schema1:name "Selected-Area Aperture Size" ;
    schema1:valueName "selectedAreaApertureSizeDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://example.org/instrument/TEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "TEM" ;
    schema1:hasPart <https://example.org/instrument/TEM/part/4D-STEM-Detector>,
        <https://example.org/instrument/TEM/part/Aberration-Corrector>,
        <https://example.org/instrument/TEM/part/EDS-Detector>,
        <https://example.org/instrument/TEM/part/EELS-Spectrometer>,
        <https://example.org/instrument/TEM/part/Electron-Source>,
        <https://example.org/instrument/TEM/part/Imaging-Detector>,
        <https://example.org/instrument/TEM/part/Monochromator> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "JEOL" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "JEOL JEM-2200FS" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "200 keV" .

<https://example.org/instrument/TEM/part/4D-STEM-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "4D-STEM Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Aberration-Corrector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Aberration Corrector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/EELS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EELS Spectrometer" ;
    schema1:description "JEOL in-column Omega energy filter (EFTEM mode; 10-eV slit; used for Ca M-edge mapping at 35 eV energy loss)" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Imaging-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Imaging Detector" ;
    schema1:description "BF TEM detector; Gatan OneView CMOS camera (TEM imaging, SAED, HRTEM)" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Monochromator> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Monochromator" ;
    schema1:name "missing" .


```


### temTAPP example Cymes2023-2
temTAPP instance derived from Cymes2023 | Apollo 17 soil 71501 pyroxene (1pyx + 2pyx) | HAADF-STEM + Dual EELS + EDS (NRL Nion UltraSTEM200-X).
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
  "@id": "ex:temTAPP-Cymes2023-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "tem protocol — Cymes2023-2",
  "schema:description": "Nion UltraSTEM200-X at NRL; dedicated aberration-corrected STEM; cold-FEG; 0.1 nm probe diameter; 40 pA; 200 keV. Gatan Enfinium ER Dual EELS (simultaneous low-loss + core-loss spectrum imaging). Bruker X-Flash windowless SDD EDS (0.7 sr). EELS Fe³⁺/ΣFe quantified by integral I(L3)/I(L2) ratio → Van Aken & Liebscher (2002) universal calibration curve. Oxidation state maps by MLLS fitting with 2 reference spectra; Fe⁰+Fe²⁺ not separated by MLLS (overlapping L3 peaks); Fe⁰ identified by anti-correlation with O K-edge. EDS: Cliff-Lorimer; detector-specific k-factors; 60% O assumed; no absorption correction. Coordinated with JEOL JEM-2200FS (same FIB section). EELS + EDS acquisition details in supplementary Fig. S1. Data deposited at Zenodo: 10.5281/zenodo.7439174. Reported detail: ada:analyticalSubModeDefault = HAADF-STEM; STEM-EELS spectrum imaging; STEM-EDS spectrum imaging; ada:edsQuantificationMethod = Cliff-Lorimer method with detector-specific k-factors; no absorption correction (sample thin); pyroxene compositions calculated with assumed O stoichiometry of 60%.",
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
            "Apollo 17 soil 71501 (<45 µm fraction); pyroxene grains \"1pyx\" (unexsolved augite) and \"2pyx\" (exsolved pigeonite-augite intergrowth); one FIB section analyzed on two instruments"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/temTAPP/samplePreparationDetailsDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "samplePreparationDetailsDefault",
            "schema:name": "Sample Preparation Details",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "FEI Helios G3 Dual Beam FIB-SEM at NRL; ~80 nm amorphous C coating applied to grain before FIB; 1–2 µm e-beam amorphous C protection strip; initial in situ thinning to ~1–2 µm, then Pt-welded to Cu TEM half-grid; thinned to ~80–100 nm; stored under N₂; baked 140°C for 8 h under vacuum before TEM"
          }
        ],
        "schema:description": "FIB lift-out (Ga+)",
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
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:instrument": [
    {
      "schema:additionalType": [
        "TEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "Nion",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "Nion UltraSTEM200-X",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Cold-FEG",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/Electron-Source",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "Aberration Corrector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Unknown",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/Aberration-Corrector",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Bruker X-Flash windowless silicon-drift detector (SDD); 0.7 sr solid angle",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/EDS-Detector",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "EELS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Gatan Enfinium ER Dual EELS spectrometer (simultaneous low-loss and core-loss)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/EELS-Spectrometer",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "Imaging Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "HAADF-STEM detector (DigiScan)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/Imaging-Detector",
          "schema:name": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "4D-STEM Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/4D-STEM-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Monochromator",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Monochromator"
        }
      ],
      "ada:acceleratingVoltageDefault": "200 keV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/TEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:spectroscopicDetectorDefault": "N/A",
  "ada:analyticalSubModeDefault": "ADF",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/temTAPP/stemProbeDiameterDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "stemProbeDiameterDefault",
      "schema:name": "STEM Probe Diameter",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 0.1,
      "schema:description": "0.1 nm"
    },
    {
      "@id": "ada:parameter/temTAPP/stemProbeCurrentDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "stemProbeCurrentDefault",
      "schema:name": "STEM Probe Current",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 40,
      "schema:description": "40 pA"
    },
    {
      "@id": "ada:parameter/temTAPP/eelsEnergyDispersion",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/temTAPP/eelsEnergyDispersion"
        }
      ],
      "schema:name": "EELS Energy Dispersion",
      "schema:value": 2,
      "schema:unitText": "example value",
      "schema:description": "Double-arctan continuum removal (for Fe L2,3 white-line integration)"
    },
    {
      "@id": "ada:parameter/temTAPP/eelsEnergyCalibrationDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "eelsEnergyCalibrationDefault",
      "schema:name": "EELS Energy Calibration",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "EELS reference standards collected on same microscope and spectrometer: FeNi metal (Fe⁰); wüstite (FeO) powder (Fe²⁺); synthetic Fe³⁺-bearing glass (Fe³⁺); magnetite Fe₃O₄ (mixed Fe²⁺/Fe³⁺) — Burgess & Stroud (2018b)"
    },
    {
      "@id": "ada:parameter/temTAPP/eelsChemicalStateDeterminationMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "eelsChemicalStateDeterminationMethodDefault",
      "schema:name": "EELS Chemical State Determination Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Integral white-line intensity ratio I(L3)/I(L2) → Van Aken & Liebscher (2002) universal calibration curve for Fe³⁺/ΣFe; MLLS fitting of Fe L2,3 ELNES with two reference spectra for oxidation state maps"
    }
  ],
  "ada:edsAcquisitionModeDefault": "N/A",
  "ada:edsQuantificationMethod": "Cliff-Lorimer (k-factor)",
  "ada:eelsAcquisitionModeDefault": "N/A",
  "ada:eelsEdgesDefault": [
    "Fe L2,3 edge (700–735 eV); O K-edge (528–550 eV)"
  ],
  "ada:eelsCollectionSemiAngle": "Power-law background removal",
  "ada:eelsAcquisitionTimePerSpectrumDefault": "Fe (L2,3); O (K)",
  "ada:eelsEnergyLossRangeDefault": "Fe (L2,3); O (K)",
  "ada:phaseIdentificationMethod": "EELS oxidation state mapping by MLLS fitting; HAADF-STEM + EDS chemical mapping; Fe⁰ identified by anti-correlation with O K-edge and lattice fringe measurement in HR images",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Scanning Transmission Electron Microscopy (STEM); Electron Energy Loss Spectroscopy (EELS); Energy-Dispersive X-ray Spectroscopy (EDS); STEM-EELS Fe oxidation state mapping"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Naval Research Laboratory, Washington, D.C., USA"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "FIB (FEI Helios G3 Dual Beam at NRL); BF/EFTEM/SAED/HRTEM (JEOL JEM-2200FS at NRL; coordinated with Nion UltraSTEM200-X)",
        "schema:description": "Fe oxidation state mapping and Fe³⁺/ΣFe quantification in exsolved lunar pyroxene (Apollo 17 soil) using STEM-EELS; MLLS and integral white-line ratio methods; coordinated HAADF-STEM + EDS for compositional mapping"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:cameraLengthDefault": -9999,
  "ada:convergenceSemiAngle": -9999,
  "ada:edsCalibrationStandardDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stemDwellTimePerPixelDefault": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/TEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:temTAPP-Cymes2023-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "tem protocol \u2014 Cymes2023-2",
  "schema:description": "Nion UltraSTEM200-X at NRL; dedicated aberration-corrected STEM; cold-FEG; 0.1 nm probe diameter; 40 pA; 200 keV. Gatan Enfinium ER Dual EELS (simultaneous low-loss + core-loss spectrum imaging). Bruker X-Flash windowless SDD EDS (0.7 sr). EELS Fe\u00b3\u207a/\u03a3Fe quantified by integral I(L3)/I(L2) ratio \u2192 Van Aken & Liebscher (2002) universal calibration curve. Oxidation state maps by MLLS fitting with 2 reference spectra; Fe\u2070+Fe\u00b2\u207a not separated by MLLS (overlapping L3 peaks); Fe\u2070 identified by anti-correlation with O K-edge. EDS: Cliff-Lorimer; detector-specific k-factors; 60% O assumed; no absorption correction. Coordinated with JEOL JEM-2200FS (same FIB section). EELS + EDS acquisition details in supplementary Fig. S1. Data deposited at Zenodo: 10.5281/zenodo.7439174. Reported detail: ada:analyticalSubModeDefault = HAADF-STEM; STEM-EELS spectrum imaging; STEM-EDS spectrum imaging; ada:edsQuantificationMethod = Cliff-Lorimer method with detector-specific k-factors; no absorption correction (sample thin); pyroxene compositions calculated with assumed O stoichiometry of 60%.",
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
            "Apollo 17 soil 71501 (<45 \u00b5m fraction); pyroxene grains \"1pyx\" (unexsolved augite) and \"2pyx\" (exsolved pigeonite-augite intergrowth); one FIB section analyzed on two instruments"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/temTAPP/samplePreparationDetailsDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "samplePreparationDetailsDefault",
            "schema:name": "Sample Preparation Details",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "FEI Helios G3 Dual Beam FIB-SEM at NRL; ~80 nm amorphous C coating applied to grain before FIB; 1\u20132 \u00b5m e-beam amorphous C protection strip; initial in situ thinning to ~1\u20132 \u00b5m, then Pt-welded to Cu TEM half-grid; thinned to ~80\u2013100 nm; stored under N\u2082; baked 140\u00b0C for 8 h under vacuum before TEM"
          }
        ],
        "schema:description": "FIB lift-out (Ga+)",
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
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:instrument": [
    {
      "schema:additionalType": [
        "TEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "Nion",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "Nion UltraSTEM200-X",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Cold-FEG",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/Electron-Source",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "Aberration Corrector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Unknown",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/Aberration-Corrector",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Bruker X-Flash windowless silicon-drift detector (SDD); 0.7 sr solid angle",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/EDS-Detector",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "EELS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Gatan Enfinium ER Dual EELS spectrometer (simultaneous low-loss and core-loss)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/EELS-Spectrometer",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "Imaging Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "HAADF-STEM detector (DigiScan)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/Imaging-Detector",
          "schema:name": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "4D-STEM Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/4D-STEM-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Monochromator",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Monochromator"
        }
      ],
      "ada:acceleratingVoltageDefault": "200 keV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/TEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:spectroscopicDetectorDefault": "N/A",
  "ada:analyticalSubModeDefault": "ADF",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/temTAPP/stemProbeDiameterDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "stemProbeDiameterDefault",
      "schema:name": "STEM Probe Diameter",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 0.1,
      "schema:description": "0.1 nm"
    },
    {
      "@id": "ada:parameter/temTAPP/stemProbeCurrentDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "stemProbeCurrentDefault",
      "schema:name": "STEM Probe Current",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 40,
      "schema:description": "40 pA"
    },
    {
      "@id": "ada:parameter/temTAPP/eelsEnergyDispersion",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/temTAPP/eelsEnergyDispersion"
        }
      ],
      "schema:name": "EELS Energy Dispersion",
      "schema:value": 2,
      "schema:unitText": "example value",
      "schema:description": "Double-arctan continuum removal (for Fe L2,3 white-line integration)"
    },
    {
      "@id": "ada:parameter/temTAPP/eelsEnergyCalibrationDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "eelsEnergyCalibrationDefault",
      "schema:name": "EELS Energy Calibration",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "EELS reference standards collected on same microscope and spectrometer: FeNi metal (Fe\u2070); w\u00fcstite (FeO) powder (Fe\u00b2\u207a); synthetic Fe\u00b3\u207a-bearing glass (Fe\u00b3\u207a); magnetite Fe\u2083O\u2084 (mixed Fe\u00b2\u207a/Fe\u00b3\u207a) \u2014 Burgess & Stroud (2018b)"
    },
    {
      "@id": "ada:parameter/temTAPP/eelsChemicalStateDeterminationMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "eelsChemicalStateDeterminationMethodDefault",
      "schema:name": "EELS Chemical State Determination Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Integral white-line intensity ratio I(L3)/I(L2) \u2192 Van Aken & Liebscher (2002) universal calibration curve for Fe\u00b3\u207a/\u03a3Fe; MLLS fitting of Fe L2,3 ELNES with two reference spectra for oxidation state maps"
    }
  ],
  "ada:edsAcquisitionModeDefault": "N/A",
  "ada:edsQuantificationMethod": "Cliff-Lorimer (k-factor)",
  "ada:eelsAcquisitionModeDefault": "N/A",
  "ada:eelsEdgesDefault": [
    "Fe L2,3 edge (700\u2013735 eV); O K-edge (528\u2013550 eV)"
  ],
  "ada:eelsCollectionSemiAngle": "Power-law background removal",
  "ada:eelsAcquisitionTimePerSpectrumDefault": "Fe (L2,3); O (K)",
  "ada:eelsEnergyLossRangeDefault": "Fe (L2,3); O (K)",
  "ada:phaseIdentificationMethod": "EELS oxidation state mapping by MLLS fitting; HAADF-STEM + EDS chemical mapping; Fe\u2070 identified by anti-correlation with O K-edge and lattice fringe measurement in HR images",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Scanning Transmission Electron Microscopy (STEM); Electron Energy Loss Spectroscopy (EELS); Energy-Dispersive X-ray Spectroscopy (EDS); STEM-EELS Fe oxidation state mapping"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Naval Research Laboratory, Washington, D.C., USA"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "FIB (FEI Helios G3 Dual Beam at NRL); BF/EFTEM/SAED/HRTEM (JEOL JEM-2200FS at NRL; coordinated with Nion UltraSTEM200-X)",
        "schema:description": "Fe oxidation state mapping and Fe\u00b3\u207a/\u03a3Fe quantification in exsolved lunar pyroxene (Apollo 17 soil) using STEM-EELS; MLLS and integral white-line ratio methods; coordinated HAADF-STEM + EDS for compositional mapping"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:cameraLengthDefault": -9999,
  "ada:convergenceSemiAngle": -9999,
  "ada:edsCalibrationStandardDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stemDwellTimePerPixelDefault": -9999,
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

ex:temTAPP-Cymes2023-2 a cdi:Activity,
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
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/temTAPP/samplePreparationDetailsDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "FIB lift-out (Ga+)" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/temTAPP/eelsChemicalStateDeterminationMethodDefault>,
        <https://ada.astromat.org/metadata/parameter/temTAPP/eelsEnergyCalibrationDefault>,
        <https://ada.astromat.org/metadata/parameter/temTAPP/eelsEnergyDispersion>,
        <https://ada.astromat.org/metadata/parameter/temTAPP/stemProbeCurrentDefault>,
        <https://ada.astromat.org/metadata/parameter/temTAPP/stemProbeDiameterDefault> ;
    schema1:datePublished "missing" ;
    schema1:description "Nion UltraSTEM200-X at NRL; dedicated aberration-corrected STEM; cold-FEG; 0.1 nm probe diameter; 40 pA; 200 keV. Gatan Enfinium ER Dual EELS (simultaneous low-loss + core-loss spectrum imaging). Bruker X-Flash windowless SDD EDS (0.7 sr). EELS Fe³⁺/ΣFe quantified by integral I(L3)/I(L2) ratio → Van Aken & Liebscher (2002) universal calibration curve. Oxidation state maps by MLLS fitting with 2 reference spectra; Fe⁰+Fe²⁺ not separated by MLLS (overlapping L3 peaks); Fe⁰ identified by anti-correlation with O K-edge. EDS: Cliff-Lorimer; detector-specific k-factors; 60% O assumed; no absorption correction. Coordinated with JEOL JEM-2200FS (same FIB section). EELS + EDS acquisition details in supplementary Fig. S1. Data deposited at Zenodo: 10.5281/zenodo.7439174. Reported detail: ada:analyticalSubModeDefault = HAADF-STEM; STEM-EELS spectrum imaging; STEM-EDS spectrum imaging; ada:edsQuantificationMethod = Cliff-Lorimer method with detector-specific k-factors; no absorption correction (sample thin); pyroxene compositions calculated with assumed O stoichiometry of 60%." ;
    schema1:instrument <https://example.org/instrument/TEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Naval Research Laboratory, Washington, D.C., USA" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Scanning Transmission Electron Microscopy (STEM); Electron Energy Loss Spectroscopy (EELS); Energy-Dispersive X-ray Spectroscopy (EDS); STEM-EELS Fe oxidation state mapping" ] ;
    schema1:name "tem protocol — Cymes2023-2" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Apollo 17 soil 71501 (<45 µm fraction); pyroxene grains \"1pyx\" (unexsolved augite) and \"2pyx\" (exsolved pigeonite-augite intergrowth); one FIB section analyzed on two instruments" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "Fe oxidation state mapping and Fe³⁺/ΣFe quantification in exsolved lunar pyroxene (Apollo 17 soil) using STEM-EELS; MLLS and integral white-line ratio methods; coordinated HAADF-STEM + EDS for compositional mapping" ;
                    schema1:name "FIB (FEI Helios G3 Dual Beam at NRL); BF/EFTEM/SAED/HRTEM (JEOL JEM-2200FS at NRL; coordinated with Nion UltraSTEM200-X)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalSubModeDefault "ADF" ;
    ada:cameraLengthDefault -9999 ;
    ada:convergenceSemiAngle -9999 ;
    ada:edsAcquisitionModeDefault "N/A" ;
    ada:edsCalibrationStandardDefault "missing" ;
    ada:edsQuantificationMethod "Cliff-Lorimer (k-factor)" ;
    ada:eelsAcquisitionModeDefault "N/A" ;
    ada:eelsAcquisitionTimePerSpectrumDefault "Fe (L2,3); O (K)" ;
    ada:eelsCollectionSemiAngle "Power-law background removal" ;
    ada:eelsEdgesDefault "Fe L2,3 edge (700–735 eV); O K-edge (528–550 eV)" ;
    ada:eelsEnergyLossRangeDefault "Fe (L2,3); O (K)" ;
    ada:phaseIdentificationMethod "EELS oxidation state mapping by MLLS fitting; HAADF-STEM + EDS chemical mapping; Fe⁰ identified by anti-correlation with O K-edge and lattice fringe measurement in HR images" ;
    ada:samplingUnit "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:spectroscopicDetectorDefault "N/A" ;
    ada:stemDwellTimePerPixelDefault -9999 .

<https://ada.astromat.org/metadata/parameter/temTAPP/eelsChemicalStateDeterminationMethodDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Integral white-line intensity ratio I(L3)/I(L2) → Van Aken & Liebscher (2002) universal calibration curve for Fe³⁺/ΣFe; MLLS fitting of Fe L2,3 ELNES with two reference spectra for oxidation state maps" ;
    schema1:name "EELS Chemical State Determination Method" ;
    schema1:valueName "eelsChemicalStateDeterminationMethodDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/temTAPP/eelsEnergyCalibrationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "EELS reference standards collected on same microscope and spectrometer: FeNi metal (Fe⁰); wüstite (FeO) powder (Fe²⁺); synthetic Fe³⁺-bearing glass (Fe³⁺); magnetite Fe₃O₄ (mixed Fe²⁺/Fe³⁺) — Burgess & Stroud (2018b)" ;
    schema1:name "EELS Energy Calibration" ;
    schema1:valueName "eelsEnergyCalibrationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/temTAPP/samplePreparationDetailsDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "FEI Helios G3 Dual Beam FIB-SEM at NRL; ~80 nm amorphous C coating applied to grain before FIB; 1–2 µm e-beam amorphous C protection strip; initial in situ thinning to ~1–2 µm, then Pt-welded to Cu TEM half-grid; thinned to ~80–100 nm; stored under N₂; baked 140°C for 8 h under vacuum before TEM" ;
    schema1:name "Sample Preparation Details" ;
    schema1:valueName "samplePreparationDetailsDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/temTAPP/stemProbeCurrentDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 40 ;
    schema1:description "40 pA" ;
    schema1:name "STEM Probe Current" ;
    schema1:valueName "stemProbeCurrentDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/temTAPP/stemProbeDiameterDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1e-01 ;
    schema1:description "0.1 nm" ;
    schema1:name "STEM Probe Diameter" ;
    schema1:valueName "stemProbeDiameterDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://example.org/instrument/TEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "TEM" ;
    schema1:hasPart <https://example.org/instrument/TEM/part/4D-STEM-Detector>,
        <https://example.org/instrument/TEM/part/Aberration-Corrector>,
        <https://example.org/instrument/TEM/part/EDS-Detector>,
        <https://example.org/instrument/TEM/part/EELS-Spectrometer>,
        <https://example.org/instrument/TEM/part/Electron-Source>,
        <https://example.org/instrument/TEM/part/Imaging-Detector>,
        <https://example.org/instrument/TEM/part/Monochromator> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Nion" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Nion UltraSTEM200-X" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "200 keV" .

<https://example.org/instrument/TEM/part/4D-STEM-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "4D-STEM Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Aberration-Corrector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Aberration Corrector" ;
    schema1:description "Unknown" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:description "Bruker X-Flash windowless silicon-drift detector (SDD); 0.7 sr solid angle" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/EELS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EELS Spectrometer" ;
    schema1:description "Gatan Enfinium ER Dual EELS spectrometer (simultaneous low-loss and core-loss)" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "Cold-FEG" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Imaging-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Imaging Detector" ;
    schema1:description "HAADF-STEM detector (DigiScan)" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Monochromator> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Monochromator" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/parameter/temTAPP/eelsEnergyDispersion> a schema1:PropertyValue ;
    schema1:description "Double-arctan continuum removal (for Fe L2,3 white-line integration)" ;
    schema1:name "EELS Energy Dispersion" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/temTAPP/eelsEnergyDispersion> ;
    schema1:unitText "example value" ;
    schema1:value 2 .


```


### temTAPP example Mo2022
temTAPP instance derived from Mo2022 | Chang'E-5 lunar soil CE5C0400YJFM00505 | HAADF-STEM + EDS (SINANO CAS FEI Talos F200X).
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
  "@id": "ex:temTAPP-Mo2022",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "tem protocol — Mo2022",
  "schema:description": "FEI Talos F200X at SINANO CAS, Suzhou; 200 kV; FE-STEM. HAADF-STEM + EDS for Fe distribution mapping in np-Fe0, glass matrix, olivine. Phase identification by FFT of DF image lattice fringes (olivine d-spacings confirmed). Sample CE5C0400YJFM00505 allocated by China National Space Administration; stored and mounted in Ar-filled glovebox at IGCAS CAS; Au-coated. FIB foils prepared by Wirth method at IGCAS CAS; <100 nm. Coordinated with Hitachi HF5000 (EELS at Shanghai Institute of Ceramics CAS) and PHI 700/710 Auger nanoprobe (at Tsinghua University). Reported detail: ada:analyticalSubModeDefault = HAADF-STEM; STEM-EDS mapping; BF-TEM (FFT lattice fringe analysis); ada:edsAcquisitionModeDefault = EDS chemical mapping (Fe distribution).",
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
            "Chang'E-5 lunar soil grain CE5C0400YJFM00505 (two grains selected); <50 µm; dispersed on Al double-sided tape in Ar-filled glovebox; coated with gold layer to prevent charging"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/temTAPP/samplePreparationDetailsDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "samplePreparationDetailsDefault",
            "schema:name": "Sample Preparation Details",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "FEI Scios Dual-beam FIB-SEM at Institute of Geochemistry, CAS (IGCAS), Guiyang; Wirth method (Wirth, 2009 Chem. Geol.); ultrathin foils <100 nm; characterized in sequence: FE-STEM → Auger nanoprobe → TEM-EELS; FIB foils cleaned with 1 keV Ar+ beam (PHI 710) before Auger and EELS analysis"
          }
        ],
        "schema:description": "FIB lift-out (Ga+)",
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
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:instrument": [
    {
      "schema:additionalType": [
        "TEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "Unknown",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "FEI Talos F200X",
        "@type": [
          "schema:ProductModel"
        ]
      },
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
          "@id": "ex:instrument/TEM/part/Electron-Source",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "Imaging Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "HAADF-STEM detector; DF TEM detector",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/Imaging-Detector",
          "schema:name": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "4D-STEM Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/4D-STEM-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Aberration Corrector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Aberration-Corrector"
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
          "@id": "ex:instrument/TEM/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EELS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/EELS-Spectrometer"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Monochromator",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Monochromator"
        }
      ],
      "ada:acceleratingVoltageDefault": "200 kV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/TEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:spectroscopicDetectorDefault": "N/A",
  "ada:analyticalSubModeDefault": "BF-TEM",
  "ada:edsAcquisitionModeDefault": "Map",
  "ada:phaseIdentificationMethod": "FFT of DF image lattice fringes for phase ID (olivine d-spacings); EDS composition maps",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Scanning Transmission Electron Microscopy (STEM); Energy-Dispersive X-ray Spectroscopy (EDS)"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Suzhou Institute of Nano-tech and Nano-bionics (SINANO), Chinese Academy of Sciences, Suzhou, China"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "FIB-SEM (FEI Scios Dual-beam at IGCAS CAS); Auger electron spectroscopy (PHI 700/710 scanning Auger nanoprobe at Tsinghua University); TEM-EELS (Hitachi HF5000 at Shanghai Institute of Ceramics CAS; coordinated)",
        "schema:description": "Nanoscale characterization of Fe-bearing phases in Chang'E-5 lunar soil; HAADF-STEM + EDS for phase morphology and composition mapping; coordinated with Auger (surface Fe valence) and EELS (bulk Fe valence)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:cameraLengthDefault": -9999,
  "ada:convergenceSemiAngle": -9999,
  "ada:edsCalibrationStandardDefault": "missing",
  "ada:edsQuantificationMethod": "missing",
  "ada:eelsAcquisitionModeDefault": "missing",
  "ada:eelsAcquisitionTimePerSpectrumDefault": -9999,
  "ada:eelsCollectionSemiAngle": -9999,
  "ada:eelsEnergyLossRangeDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stemDwellTimePerPixelDefault": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/TEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:temTAPP-Mo2022",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "tem protocol \u2014 Mo2022",
  "schema:description": "FEI Talos F200X at SINANO CAS, Suzhou; 200 kV; FE-STEM. HAADF-STEM + EDS for Fe distribution mapping in np-Fe0, glass matrix, olivine. Phase identification by FFT of DF image lattice fringes (olivine d-spacings confirmed). Sample CE5C0400YJFM00505 allocated by China National Space Administration; stored and mounted in Ar-filled glovebox at IGCAS CAS; Au-coated. FIB foils prepared by Wirth method at IGCAS CAS; <100 nm. Coordinated with Hitachi HF5000 (EELS at Shanghai Institute of Ceramics CAS) and PHI 700/710 Auger nanoprobe (at Tsinghua University). Reported detail: ada:analyticalSubModeDefault = HAADF-STEM; STEM-EDS mapping; BF-TEM (FFT lattice fringe analysis); ada:edsAcquisitionModeDefault = EDS chemical mapping (Fe distribution).",
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
            "Chang'E-5 lunar soil grain CE5C0400YJFM00505 (two grains selected); <50 \u00b5m; dispersed on Al double-sided tape in Ar-filled glovebox; coated with gold layer to prevent charging"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/temTAPP/samplePreparationDetailsDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "samplePreparationDetailsDefault",
            "schema:name": "Sample Preparation Details",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "FEI Scios Dual-beam FIB-SEM at Institute of Geochemistry, CAS (IGCAS), Guiyang; Wirth method (Wirth, 2009 Chem. Geol.); ultrathin foils <100 nm; characterized in sequence: FE-STEM \u2192 Auger nanoprobe \u2192 TEM-EELS; FIB foils cleaned with 1 keV Ar+ beam (PHI 710) before Auger and EELS analysis"
          }
        ],
        "schema:description": "FIB lift-out (Ga+)",
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
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:instrument": [
    {
      "schema:additionalType": [
        "TEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "Unknown",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "FEI Talos F200X",
        "@type": [
          "schema:ProductModel"
        ]
      },
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
          "@id": "ex:instrument/TEM/part/Electron-Source",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "Imaging Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "HAADF-STEM detector; DF TEM detector",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/Imaging-Detector",
          "schema:name": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "4D-STEM Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/4D-STEM-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Aberration Corrector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Aberration-Corrector"
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
          "@id": "ex:instrument/TEM/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EELS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/EELS-Spectrometer"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Monochromator",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Monochromator"
        }
      ],
      "ada:acceleratingVoltageDefault": "200 kV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/TEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:spectroscopicDetectorDefault": "N/A",
  "ada:analyticalSubModeDefault": "BF-TEM",
  "ada:edsAcquisitionModeDefault": "Map",
  "ada:phaseIdentificationMethod": "FFT of DF image lattice fringes for phase ID (olivine d-spacings); EDS composition maps",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Scanning Transmission Electron Microscopy (STEM); Energy-Dispersive X-ray Spectroscopy (EDS)"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Suzhou Institute of Nano-tech and Nano-bionics (SINANO), Chinese Academy of Sciences, Suzhou, China"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "FIB-SEM (FEI Scios Dual-beam at IGCAS CAS); Auger electron spectroscopy (PHI 700/710 scanning Auger nanoprobe at Tsinghua University); TEM-EELS (Hitachi HF5000 at Shanghai Institute of Ceramics CAS; coordinated)",
        "schema:description": "Nanoscale characterization of Fe-bearing phases in Chang'E-5 lunar soil; HAADF-STEM + EDS for phase morphology and composition mapping; coordinated with Auger (surface Fe valence) and EELS (bulk Fe valence)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:cameraLengthDefault": -9999,
  "ada:convergenceSemiAngle": -9999,
  "ada:edsCalibrationStandardDefault": "missing",
  "ada:edsQuantificationMethod": "missing",
  "ada:eelsAcquisitionModeDefault": "missing",
  "ada:eelsAcquisitionTimePerSpectrumDefault": -9999,
  "ada:eelsCollectionSemiAngle": -9999,
  "ada:eelsEnergyLossRangeDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stemDwellTimePerPixelDefault": -9999,
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

ex:temTAPP-Mo2022 a cdi:Activity,
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
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/temTAPP/samplePreparationDetailsDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "FIB lift-out (Ga+)" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "FEI Talos F200X at SINANO CAS, Suzhou; 200 kV; FE-STEM. HAADF-STEM + EDS for Fe distribution mapping in np-Fe0, glass matrix, olivine. Phase identification by FFT of DF image lattice fringes (olivine d-spacings confirmed). Sample CE5C0400YJFM00505 allocated by China National Space Administration; stored and mounted in Ar-filled glovebox at IGCAS CAS; Au-coated. FIB foils prepared by Wirth method at IGCAS CAS; <100 nm. Coordinated with Hitachi HF5000 (EELS at Shanghai Institute of Ceramics CAS) and PHI 700/710 Auger nanoprobe (at Tsinghua University). Reported detail: ada:analyticalSubModeDefault = HAADF-STEM; STEM-EDS mapping; BF-TEM (FFT lattice fringe analysis); ada:edsAcquisitionModeDefault = EDS chemical mapping (Fe distribution)." ;
    schema1:instrument <https://example.org/instrument/TEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Suzhou Institute of Nano-tech and Nano-bionics (SINANO), Chinese Academy of Sciences, Suzhou, China" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Scanning Transmission Electron Microscopy (STEM); Energy-Dispersive X-ray Spectroscopy (EDS)" ] ;
    schema1:name "tem protocol — Mo2022" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Chang'E-5 lunar soil grain CE5C0400YJFM00505 (two grains selected); <50 µm; dispersed on Al double-sided tape in Ar-filled glovebox; coated with gold layer to prevent charging" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "Nanoscale characterization of Fe-bearing phases in Chang'E-5 lunar soil; HAADF-STEM + EDS for phase morphology and composition mapping; coordinated with Auger (surface Fe valence) and EELS (bulk Fe valence)" ;
                    schema1:name "FIB-SEM (FEI Scios Dual-beam at IGCAS CAS); Auger electron spectroscopy (PHI 700/710 scanning Auger nanoprobe at Tsinghua University); TEM-EELS (Hitachi HF5000 at Shanghai Institute of Ceramics CAS; coordinated)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalSubModeDefault "BF-TEM" ;
    ada:cameraLengthDefault -9999 ;
    ada:convergenceSemiAngle -9999 ;
    ada:edsAcquisitionModeDefault "Map" ;
    ada:edsCalibrationStandardDefault "missing" ;
    ada:edsQuantificationMethod "missing" ;
    ada:eelsAcquisitionModeDefault "missing" ;
    ada:eelsAcquisitionTimePerSpectrumDefault -9999 ;
    ada:eelsCollectionSemiAngle -9999 ;
    ada:eelsEnergyLossRangeDefault "missing" ;
    ada:phaseIdentificationMethod "FFT of DF image lattice fringes for phase ID (olivine d-spacings); EDS composition maps" ;
    ada:samplingUnit "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:spectroscopicDetectorDefault "N/A" ;
    ada:stemDwellTimePerPixelDefault -9999 .

<https://ada.astromat.org/metadata/parameter/temTAPP/samplePreparationDetailsDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "FEI Scios Dual-beam FIB-SEM at Institute of Geochemistry, CAS (IGCAS), Guiyang; Wirth method (Wirth, 2009 Chem. Geol.); ultrathin foils <100 nm; characterized in sequence: FE-STEM → Auger nanoprobe → TEM-EELS; FIB foils cleaned with 1 keV Ar+ beam (PHI 710) before Auger and EELS analysis" ;
    schema1:name "Sample Preparation Details" ;
    schema1:valueName "samplePreparationDetailsDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://example.org/instrument/TEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "TEM" ;
    schema1:hasPart <https://example.org/instrument/TEM/part/4D-STEM-Detector>,
        <https://example.org/instrument/TEM/part/Aberration-Corrector>,
        <https://example.org/instrument/TEM/part/EDS-Detector>,
        <https://example.org/instrument/TEM/part/EELS-Spectrometer>,
        <https://example.org/instrument/TEM/part/Electron-Source>,
        <https://example.org/instrument/TEM/part/Imaging-Detector>,
        <https://example.org/instrument/TEM/part/Monochromator> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Unknown" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "FEI Talos F200X" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "200 kV" .

<https://example.org/instrument/TEM/part/4D-STEM-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "4D-STEM Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Aberration-Corrector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Aberration Corrector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/EELS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EELS Spectrometer" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "Unknown" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Imaging-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Imaging Detector" ;
    schema1:description "HAADF-STEM detector; DF TEM detector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Monochromator> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Monochromator" ;
    schema1:name "missing" .


```


### temTAPP example Mo2022-2
temTAPP instance derived from Mo2022 | Chang'E-5 lunar soil CE5C0400YJFM00505 | TEM-EELS (Shanghai Institute of Ceramics CAS Hitachi HF5000).
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
  "@id": "ex:temTAPP-Mo2022-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "tem protocol — Mo2022-2",
  "schema:description": "Hitachi HF5000 at Shanghai Institute of Ceramics CAS; 200 kV; 100 pA; Gatan GIF Quantum ER System Model 965 parallel EELS spectrometer. Energy resolution: 0.5–0.7 eV FWHM at ZLP. Fe L3,2 edge: L3 peak positions 707.7 eV (Fe⁰), 707.2 eV (Fe²⁺), 709.0 eV (Fe³⁺). EELS acquired in DualEELS mode; 10 s point analysis, 18 s line scan. Reference standards: Fe metal + troilite (L6 ordinary chondrite GRV051874) for Fe⁰/Fe²⁺; terrestrial hematite for Fe³⁺; wüstite and hematite from Yao et al. 2018 (AES refs). ZLP aligned before spectral comparison. Background and continuum removal methods not stated. Valence state ID is qualitative (peak position + lineshape). Coordinated with FEI Talos F200X (EDS at SINANO) and PHI 700/710 Auger nanoprobe. Reported detail: ada:analyticalSubModeDefault = HAADF-STEM; TEM-EELS point analysis; TEM-EELS line scan; ada:eelsAcquisitionModeDefault = Point analysis and line scan EELS.",
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
            "Chang'E-5 lunar soil grain CE5C0400YJFM00505 (two grains selected); <50 µm; dispersed on Al double-sided tape in Ar-filled glovebox; coated with gold layer to prevent charging"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/temTAPP/samplePreparationDetailsDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "samplePreparationDetailsDefault",
            "schema:name": "Sample Preparation Details",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "FEI Scios Dual-beam FIB-SEM at Institute of Geochemistry, CAS (IGCAS), Guiyang; Wirth method (Wirth, 2009 Chem. Geol.); ultrathin foils <100 nm; characterized in sequence: FE-STEM → Auger nanoprobe → TEM-EELS; FIB foils cleaned with 1 keV Ar+ beam (PHI 710) before Auger and EELS analysis"
          }
        ],
        "schema:description": "FIB lift-out (Ga+)",
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
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:instrument": [
    {
      "schema:additionalType": [
        "TEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "Hitachi",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "Hitachi HF5000",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "EELS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Gatan GIF Quantum ER System Model 965 parallel EELS spectrometer",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/EELS-Spectrometer",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "Imaging Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "HAADF-STEM detector",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/Imaging-Detector",
          "schema:name": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "4D-STEM Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/4D-STEM-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Aberration Corrector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Aberration-Corrector"
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
          "@id": "ex:instrument/TEM/part/EDS-Detector"
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
          "@id": "ex:instrument/TEM/part/Electron-Source"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Monochromator",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Monochromator"
        }
      ],
      "ada:acceleratingVoltageDefault": "200 kV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/TEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:spectroscopicDetectorDefault": "N/A",
  "ada:analyticalSubModeDefault": "ADF",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/temTAPP/stemProbeCurrentDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "stemProbeCurrentDefault",
      "schema:name": "STEM Probe Current",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 100,
      "schema:description": "100 pA"
    },
    {
      "@id": "ada:parameter/temTAPP/eelsEnergyResolution",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/temTAPP/eelsEnergyResolution"
        }
      ],
      "schema:name": "EELS Energy Resolution",
      "schema:value": 0.5,
      "schema:unitText": "example value",
      "schema:description": "0.5–0.7"
    },
    {
      "@id": "ada:parameter/temTAPP/eelsChemicalStateDeterminationMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "eelsChemicalStateDeterminationMethodDefault",
      "schema:name": "EELS Chemical State Determination Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Peak position and lineshape comparison to reference standards (qualitative Fe valence state determination: Fe⁰, Fe²⁺, Fe³⁺)"
    }
  ],
  "ada:eelsAcquisitionModeDefault": "Line scan",
  "ada:eelsEdgesDefault": [
    "Fe L3,2 edge (~707–709 eV; L3 peak at 707.7 eV for Fe⁰, 707.2 eV for Fe²⁺, 709.0 eV for Fe³⁺)"
  ],
  "ada:eelsAcquisitionTimePerSpectrumDefault": "Fe (L3,2)",
  "ada:eelsEnergyLossRangeDefault": "Fe (L3,2)",
  "ada:phaseIdentificationMethod": "EELS peak position and lineshape comparison to reference spectra; qualitative valence state ID (np-Fe0 = metallic; matrix = Fe³⁺; olivine = Fe²⁺)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Transmission Electron Microscopy (TEM); Electron Energy Loss Spectroscopy (EELS); TEM-EELS iron valence state analysis"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Shanghai Institute of Ceramics, Chinese Academy of Sciences, Shanghai, China"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "FIB-SEM (FEI Scios Dual-beam at IGCAS CAS); HAADF-STEM + EDS (FEI Talos F200X at SINANO CAS; coordinated); Auger electron spectroscopy (PHI 700/710 at Tsinghua University)",
        "schema:description": "In situ Fe valence state analysis in Chang'E-5 lunar soil by TEM-EELS; Fe L3,2 edge peak position and lineshape comparison to reference standards (Fe⁰, Fe²⁺, Fe³⁺); point analysis and line scan"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:cameraLengthDefault": -9999,
  "ada:convergenceSemiAngle": -9999,
  "ada:edsAcquisitionModeDefault": "missing",
  "ada:edsCalibrationStandardDefault": "missing",
  "ada:edsQuantificationMethod": "missing",
  "ada:eelsCollectionSemiAngle": -9999,
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stemDwellTimePerPixelDefault": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/TEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:temTAPP-Mo2022-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "tem protocol \u2014 Mo2022-2",
  "schema:description": "Hitachi HF5000 at Shanghai Institute of Ceramics CAS; 200 kV; 100 pA; Gatan GIF Quantum ER System Model 965 parallel EELS spectrometer. Energy resolution: 0.5\u20130.7 eV FWHM at ZLP. Fe L3,2 edge: L3 peak positions 707.7 eV (Fe\u2070), 707.2 eV (Fe\u00b2\u207a), 709.0 eV (Fe\u00b3\u207a). EELS acquired in DualEELS mode; 10 s point analysis, 18 s line scan. Reference standards: Fe metal + troilite (L6 ordinary chondrite GRV051874) for Fe\u2070/Fe\u00b2\u207a; terrestrial hematite for Fe\u00b3\u207a; w\u00fcstite and hematite from Yao et al. 2018 (AES refs). ZLP aligned before spectral comparison. Background and continuum removal methods not stated. Valence state ID is qualitative (peak position + lineshape). Coordinated with FEI Talos F200X (EDS at SINANO) and PHI 700/710 Auger nanoprobe. Reported detail: ada:analyticalSubModeDefault = HAADF-STEM; TEM-EELS point analysis; TEM-EELS line scan; ada:eelsAcquisitionModeDefault = Point analysis and line scan EELS.",
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
            "Chang'E-5 lunar soil grain CE5C0400YJFM00505 (two grains selected); <50 \u00b5m; dispersed on Al double-sided tape in Ar-filled glovebox; coated with gold layer to prevent charging"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/temTAPP/samplePreparationDetailsDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "samplePreparationDetailsDefault",
            "schema:name": "Sample Preparation Details",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "FEI Scios Dual-beam FIB-SEM at Institute of Geochemistry, CAS (IGCAS), Guiyang; Wirth method (Wirth, 2009 Chem. Geol.); ultrathin foils <100 nm; characterized in sequence: FE-STEM \u2192 Auger nanoprobe \u2192 TEM-EELS; FIB foils cleaned with 1 keV Ar+ beam (PHI 710) before Auger and EELS analysis"
          }
        ],
        "schema:description": "FIB lift-out (Ga+)",
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
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:instrument": [
    {
      "schema:additionalType": [
        "TEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "Hitachi",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "Hitachi HF5000",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "EELS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Gatan GIF Quantum ER System Model 965 parallel EELS spectrometer",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/EELS-Spectrometer",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "Imaging Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "HAADF-STEM detector",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/TEM/part/Imaging-Detector",
          "schema:name": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "4D-STEM Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/4D-STEM-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Aberration Corrector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Aberration-Corrector"
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
          "@id": "ex:instrument/TEM/part/EDS-Detector"
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
          "@id": "ex:instrument/TEM/part/Electron-Source"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Monochromator",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/TEM/part/Monochromator"
        }
      ],
      "ada:acceleratingVoltageDefault": "200 kV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/TEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:spectroscopicDetectorDefault": "N/A",
  "ada:analyticalSubModeDefault": "ADF",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/temTAPP/stemProbeCurrentDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "stemProbeCurrentDefault",
      "schema:name": "STEM Probe Current",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 100,
      "schema:description": "100 pA"
    },
    {
      "@id": "ada:parameter/temTAPP/eelsEnergyResolution",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/temTAPP/eelsEnergyResolution"
        }
      ],
      "schema:name": "EELS Energy Resolution",
      "schema:value": 0.5,
      "schema:unitText": "example value",
      "schema:description": "0.5\u20130.7"
    },
    {
      "@id": "ada:parameter/temTAPP/eelsChemicalStateDeterminationMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "eelsChemicalStateDeterminationMethodDefault",
      "schema:name": "EELS Chemical State Determination Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Peak position and lineshape comparison to reference standards (qualitative Fe valence state determination: Fe\u2070, Fe\u00b2\u207a, Fe\u00b3\u207a)"
    }
  ],
  "ada:eelsAcquisitionModeDefault": "Line scan",
  "ada:eelsEdgesDefault": [
    "Fe L3,2 edge (~707\u2013709 eV; L3 peak at 707.7 eV for Fe\u2070, 707.2 eV for Fe\u00b2\u207a, 709.0 eV for Fe\u00b3\u207a)"
  ],
  "ada:eelsAcquisitionTimePerSpectrumDefault": "Fe (L3,2)",
  "ada:eelsEnergyLossRangeDefault": "Fe (L3,2)",
  "ada:phaseIdentificationMethod": "EELS peak position and lineshape comparison to reference spectra; qualitative valence state ID (np-Fe0 = metallic; matrix = Fe\u00b3\u207a; olivine = Fe\u00b2\u207a)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Transmission Electron Microscopy (TEM); Electron Energy Loss Spectroscopy (EELS); TEM-EELS iron valence state analysis"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Shanghai Institute of Ceramics, Chinese Academy of Sciences, Shanghai, China"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "FIB-SEM (FEI Scios Dual-beam at IGCAS CAS); HAADF-STEM + EDS (FEI Talos F200X at SINANO CAS; coordinated); Auger electron spectroscopy (PHI 700/710 at Tsinghua University)",
        "schema:description": "In situ Fe valence state analysis in Chang'E-5 lunar soil by TEM-EELS; Fe L3,2 edge peak position and lineshape comparison to reference standards (Fe\u2070, Fe\u00b2\u207a, Fe\u00b3\u207a); point analysis and line scan"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:cameraLengthDefault": -9999,
  "ada:convergenceSemiAngle": -9999,
  "ada:edsAcquisitionModeDefault": "missing",
  "ada:edsCalibrationStandardDefault": "missing",
  "ada:edsQuantificationMethod": "missing",
  "ada:eelsCollectionSemiAngle": -9999,
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:stemDwellTimePerPixelDefault": -9999,
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

ex:temTAPP-Mo2022-2 a cdi:Activity,
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
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/temTAPP/samplePreparationDetailsDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "FIB lift-out (Ga+)" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/temTAPP/eelsChemicalStateDeterminationMethodDefault>,
        <https://ada.astromat.org/metadata/parameter/temTAPP/eelsEnergyResolution>,
        <https://ada.astromat.org/metadata/parameter/temTAPP/stemProbeCurrentDefault> ;
    schema1:datePublished "missing" ;
    schema1:description "Hitachi HF5000 at Shanghai Institute of Ceramics CAS; 200 kV; 100 pA; Gatan GIF Quantum ER System Model 965 parallel EELS spectrometer. Energy resolution: 0.5–0.7 eV FWHM at ZLP. Fe L3,2 edge: L3 peak positions 707.7 eV (Fe⁰), 707.2 eV (Fe²⁺), 709.0 eV (Fe³⁺). EELS acquired in DualEELS mode; 10 s point analysis, 18 s line scan. Reference standards: Fe metal + troilite (L6 ordinary chondrite GRV051874) for Fe⁰/Fe²⁺; terrestrial hematite for Fe³⁺; wüstite and hematite from Yao et al. 2018 (AES refs). ZLP aligned before spectral comparison. Background and continuum removal methods not stated. Valence state ID is qualitative (peak position + lineshape). Coordinated with FEI Talos F200X (EDS at SINANO) and PHI 700/710 Auger nanoprobe. Reported detail: ada:analyticalSubModeDefault = HAADF-STEM; TEM-EELS point analysis; TEM-EELS line scan; ada:eelsAcquisitionModeDefault = Point analysis and line scan EELS." ;
    schema1:instrument <https://example.org/instrument/TEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Shanghai Institute of Ceramics, Chinese Academy of Sciences, Shanghai, China" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Transmission Electron Microscopy (TEM); Electron Energy Loss Spectroscopy (EELS); TEM-EELS iron valence state analysis" ] ;
    schema1:name "tem protocol — Mo2022-2" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Chang'E-5 lunar soil grain CE5C0400YJFM00505 (two grains selected); <50 µm; dispersed on Al double-sided tape in Ar-filled glovebox; coated with gold layer to prevent charging" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "In situ Fe valence state analysis in Chang'E-5 lunar soil by TEM-EELS; Fe L3,2 edge peak position and lineshape comparison to reference standards (Fe⁰, Fe²⁺, Fe³⁺); point analysis and line scan" ;
                    schema1:name "FIB-SEM (FEI Scios Dual-beam at IGCAS CAS); HAADF-STEM + EDS (FEI Talos F200X at SINANO CAS; coordinated); Auger electron spectroscopy (PHI 700/710 at Tsinghua University)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalSubModeDefault "ADF" ;
    ada:cameraLengthDefault -9999 ;
    ada:convergenceSemiAngle -9999 ;
    ada:edsAcquisitionModeDefault "missing" ;
    ada:edsCalibrationStandardDefault "missing" ;
    ada:edsQuantificationMethod "missing" ;
    ada:eelsAcquisitionModeDefault "Line scan" ;
    ada:eelsAcquisitionTimePerSpectrumDefault "Fe (L3,2)" ;
    ada:eelsCollectionSemiAngle -9999 ;
    ada:eelsEdgesDefault "Fe L3,2 edge (~707–709 eV; L3 peak at 707.7 eV for Fe⁰, 707.2 eV for Fe²⁺, 709.0 eV for Fe³⁺)" ;
    ada:eelsEnergyLossRangeDefault "Fe (L3,2)" ;
    ada:phaseIdentificationMethod "EELS peak position and lineshape comparison to reference spectra; qualitative valence state ID (np-Fe0 = metallic; matrix = Fe³⁺; olivine = Fe²⁺)" ;
    ada:samplingUnit "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:spectroscopicDetectorDefault "N/A" ;
    ada:stemDwellTimePerPixelDefault -9999 .

<https://ada.astromat.org/metadata/parameter/temTAPP/eelsChemicalStateDeterminationMethodDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Peak position and lineshape comparison to reference standards (qualitative Fe valence state determination: Fe⁰, Fe²⁺, Fe³⁺)" ;
    schema1:name "EELS Chemical State Determination Method" ;
    schema1:valueName "eelsChemicalStateDeterminationMethodDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/temTAPP/samplePreparationDetailsDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "FEI Scios Dual-beam FIB-SEM at Institute of Geochemistry, CAS (IGCAS), Guiyang; Wirth method (Wirth, 2009 Chem. Geol.); ultrathin foils <100 nm; characterized in sequence: FE-STEM → Auger nanoprobe → TEM-EELS; FIB foils cleaned with 1 keV Ar+ beam (PHI 710) before Auger and EELS analysis" ;
    schema1:name "Sample Preparation Details" ;
    schema1:valueName "samplePreparationDetailsDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/temTAPP/stemProbeCurrentDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 100 ;
    schema1:description "100 pA" ;
    schema1:name "STEM Probe Current" ;
    schema1:valueName "stemProbeCurrentDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://example.org/instrument/TEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "TEM" ;
    schema1:hasPart <https://example.org/instrument/TEM/part/4D-STEM-Detector>,
        <https://example.org/instrument/TEM/part/Aberration-Corrector>,
        <https://example.org/instrument/TEM/part/EDS-Detector>,
        <https://example.org/instrument/TEM/part/EELS-Spectrometer>,
        <https://example.org/instrument/TEM/part/Electron-Source>,
        <https://example.org/instrument/TEM/part/Imaging-Detector>,
        <https://example.org/instrument/TEM/part/Monochromator> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Hitachi" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Hitachi HF5000" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "200 kV" .

<https://example.org/instrument/TEM/part/4D-STEM-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "4D-STEM Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Aberration-Corrector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Aberration Corrector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/EELS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EELS Spectrometer" ;
    schema1:description "Gatan GIF Quantum ER System Model 965 parallel EELS spectrometer" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Imaging-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Imaging Detector" ;
    schema1:description "HAADF-STEM detector" ;
    schema1:name "missing" .

<https://example.org/instrument/TEM/part/Monochromator> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Monochromator" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/parameter/temTAPP/eelsEnergyResolution> a schema1:PropertyValue ;
    schema1:description "0.5–0.7" ;
    schema1:name "EELS Energy Resolution" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/temTAPP/eelsEnergyResolution> ;
    schema1:unitText "example value" ;
    schema1:value 5e-01 .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: TEM Technique-Aligned Protocol Profile (temTAPP)
description: 'Transmission electron microscopy (TEM/STEM, incl. EDS/EELS) extension
  of the base TAPP definition. Basic protocol-tier fields are required top-level ada:
  properties; Advanced protocol-tier fields are schema:additionalProperty[] entries;
  an ada:analyteTemplate carries per-element columns. Generated from tapp/Current
  TAPPs/TEM_TAPP_v48.csv by tools/build_tapp.py.'
allOf:
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/calibrationFactor/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/analyte/schema.yaml#/$defs/ProcedureIdentification
- type: object
  properties:
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
                              - Organic matter
                              - Amorphous phase
                              - Nanoparticle
                              - N/A
                              - None
                              - missing
                            - type: string
                            readOnly: true
                allOf:
                - contains:
                    properties:
                      schema:name:
                        const: Target Material
                    required:
                    - schema:name
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
                    const: Sample preparation
                required:
                - schema:name
              then:
                properties:
                  schema:additionalProperty:
                    type: array
                    items:
                      title: Sample Preparation Details
                      description: "Detailed description of section preparation conditions:
                        FIB milling voltages and currents; final thinning conditions
                        and target foil thickness; protective coating type and deposition
                        method (e.g., e-beam vs. ion-beam Pt or C strip \u2014 e-beam
                        deposition causes less surface damage); any post-FIB surface
                        cleanup (e.g., low-energy Ar+ ion polishing in a Fischione
                        NanoMill, final 0.5\u20132 kV Ga+ thinning); sample transfer
                        and storage environment (ambient air, dry N\u2082 atmosphere,
                        vacuum transfer holder, glovebox); plasma cleaning before
                        loading. Includes session-specific observations and deviations
                        from the procedure standard. Includes preparation artifacts
                        noted (Ga implantation, amorphization, curtaining)."
                      type: object
                      properties:
                        '@id':
                          const: ada:parameter/temTAPP/samplePreparationDetailsDefault
                        '@type':
                          const:
                          - schema:PropertyValueSpecification
                        schema:valueName:
                          const: samplePreparationDetailsDefault
                        schema:name:
                          const: Sample Preparation Details
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
                    allOf:
                    - contains:
                        title: Sample Preparation Details
                        description: "Detailed description of section preparation
                          conditions: FIB milling voltages and currents; final thinning
                          conditions and target foil thickness; protective coating
                          type and deposition method (e.g., e-beam vs. ion-beam Pt
                          or C strip \u2014 e-beam deposition causes less surface
                          damage); any post-FIB surface cleanup (e.g., low-energy
                          Ar+ ion polishing in a Fischione NanoMill, final 0.5\u20132
                          kV Ga+ thinning); sample transfer and storage environment
                          (ambient air, dry N\u2082 atmosphere, vacuum transfer holder,
                          glovebox); plasma cleaning before loading. Includes session-specific
                          observations and deviations from the procedure standard.
                          Includes preparation artifacts noted (Ga implantation, amorphization,
                          curtaining)."
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/temTAPP/samplePreparationDetailsDefault
                          '@type':
                            const:
                            - schema:PropertyValueSpecification
                          schema:valueName:
                            const: samplePreparationDetailsDefault
                          schema:name:
                            const: Sample Preparation Details
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
                      - title: EELS Plural Scattering Correction
                        description: Method applied to correct for multiple inelastic
                          scattering events (plural scattering) that broaden edge
                          fine structure. Record 'N/A' where EELS is not listed in
                          Spectroscopic Detector(s).
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/temTAPP/eelsPluralScatteringCorrectionDefault
                          '@type':
                            const:
                            - schema:PropertyValueSpecification
                          schema:valueName:
                            const: eelsPluralScatteringCorrectionDefault
                          schema:name:
                            const: EELS Plural Scattering Correction
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
                      - title: Image Processing Methods Applied
                        description: Image processing steps applied to TEM or STEM
                          images during or after acquisition. Non-linear processing
                          steps that could affect quantitative interpretation should
                          be documented explicitly.
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/temTAPP/imageProcessingMethodsAppliedDefault
                          '@type':
                            const:
                            - schema:PropertyValueSpecification
                          schema:valueName:
                            const: imageProcessingMethodsAppliedDefault
                          schema:name:
                            const: Image Processing Methods Applied
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
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/aggregation/schema.yaml#/$defs/Param_Procedure_analysisInclusionAndRejectionCriteria
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Procedure_constantsReferenceValues
                    allOf:
                    - contains:
                        title: EELS Plural Scattering Correction
                        description: Method applied to correct for multiple inelastic
                          scattering events (plural scattering) that broaden edge
                          fine structure. Record 'N/A' where EELS is not listed in
                          Spectroscopic Detector(s).
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/temTAPP/eelsPluralScatteringCorrectionDefault
                          '@type':
                            const:
                            - schema:PropertyValueSpecification
                          schema:valueName:
                            const: eelsPluralScatteringCorrectionDefault
                          schema:name:
                            const: EELS Plural Scattering Correction
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
                        title: Image Processing Methods Applied
                        description: Image processing steps applied to TEM or STEM
                          images during or after acquisition. Non-linear processing
                          steps that could affect quantitative interpretation should
                          be documented explicitly.
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/temTAPP/imageProcessingMethodsAppliedDefault
                          '@type':
                            const:
                            - schema:PropertyValueSpecification
                          schema:valueName:
                            const: imageProcessingMethodsAppliedDefault
                          schema:name:
                            const: Image Processing Methods Applied
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
    schema:instrument:
      type: array
      items:
        type: object
        allOf:
        - if:
            properties:
              schema:additionalType:
                contains:
                  const: TEM
                schema:inDefinedTermSet: ada:vocab/instrumentType
            required:
            - schema:additionalType
          then:
            properties:
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
                    - ThermoFisher Scientific (FEI)
                    - Hitachi
                    - Nion
                    - Zeiss
                    - Unknown
                    - N/A
                    - None
                    - missing
                    readOnly: true
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
              schema:hasPart:
                type: array
                items:
                  type: object
                  allOf:
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
                  - if:
                      properties:
                        schema:additionalType:
                          contains:
                            const: Aberration Corrector
                          schema:inDefinedTermSet: ada:vocab/instrumentComponentType
                      required:
                      - schema:additionalType
                    then:
                      properties:
                        schema:description:
                          description: Type of aberration corrector installed and
                            active.
                          anyOf:
                          - type: string
                            enum:
                            - None
                            - Probe Cs-corrected (STEM)
                            - Image Cs-corrected (TEM)
                            - Both probe and image corrected
                            - Cs-corrected (type unknown)
                            - Unknown
                            - N/A
                            - None
                            - missing
                            readOnly: true
                          - type: array
                            items:
                              type: string
                              enum:
                              - None
                              - Probe Cs-corrected (STEM)
                              - Image Cs-corrected (TEM)
                              - Both probe and image corrected
                              - Cs-corrected (type unknown)
                              - Unknown
                              - N/A
                              - None
                              - missing
                              readOnly: true
                  - if:
                      properties:
                        schema:additionalType:
                          contains:
                            const: Monochromator
                          schema:inDefinedTermSet: ada:vocab/instrumentComponentType
                      required:
                      - schema:additionalType
                    then:
                      properties:
                        schema:description:
                          description: Whether a monochromator is installed and was
                            active during this procedure. Record 'N/A' where EELS
                            is not listed in Spectroscopic Detector(s) and EFTEM is
                            not listed in Analytical Sub-mode.
                          anyOf:
                          - type: string
                            enum:
                            - "Yes \u2014 active"
                            - "Yes \u2014 not used"
                            - 'No'
                            - Unknown
                            - N/A
                            - None
                            - missing
                            readOnly: true
                          - type: array
                            items:
                              type: string
                              enum:
                              - "Yes \u2014 active"
                              - "Yes \u2014 not used"
                              - 'No'
                              - Unknown
                              - N/A
                              - None
                              - missing
                              readOnly: true
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
                            const: EELS Spectrometer
                          schema:inDefinedTermSet: ada:vocab/instrumentComponentType
                      required:
                      - schema:additionalType
                    then:
                      properties:
                        schema:description:
                          description: EELS spectrometer manufacturer, model, and
                            key capabilities including post-column GIF model and energy
                            resolution. Record 'N/A' where EELS is not listed in Spectroscopic
                            Detector(s).
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
                            const: Imaging Detector
                          schema:inDefinedTermSet: ada:vocab/instrumentComponentType
                      required:
                      - schema:additionalType
                    then:
                      properties:
                        schema:description:
                          description: List of detectors available and used under
                            this procedure for STEM imaging and TEM/SAED/CBED diffraction
                            recording. Include HAADF/ABF/BF detector geometries and
                            TEM/diffraction camera model.
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
                            const: 4D-STEM Detector
                          schema:inDefinedTermSet: ada:vocab/instrumentComponentType
                      required:
                      - schema:additionalType
                    then:
                      properties:
                        schema:description:
                          description: Direct electron detector used for 4D-STEM data
                            acquisition, recording a full diffraction pattern at each
                            probe position. If a GIF is used as the mounting platform
                            (enabling energy-filtered 4D-STEM), specify this. Record
                            'N/A' where 4D-STEM is not listed in Analytical Sub-mode.
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
                - contains:
                    properties:
                      schema:additionalType:
                        contains:
                          const: Aberration Corrector
                        schema:inDefinedTermSet: ada:vocab/instrumentComponentType
                    required:
                    - schema:additionalType
                - contains:
                    properties:
                      schema:additionalType:
                        contains:
                          const: EDS Detector
                        schema:inDefinedTermSet: ada:vocab/instrumentComponentType
                    required:
                    - schema:additionalType
              ada:acceleratingVoltageDefault:
                description: Electron beam accelerating voltage in kilovolts (kV).
                  Justify any deviation from the standard operating voltage.
                anyOf:
                - type: number
                - type: string
              schema:additionalProperty:
                type: array
                items:
                  title: TEM Objective Aperture
                  description: Objective aperture diameter used to select the imaging
                    beam condition in TEM mode.
                  type: object
                  properties:
                    '@id':
                      const: ada:parameter/temTAPP/temObjectiveApertureDefault
                    '@type':
                      const:
                      - schema:PropertyValueSpecification
                    schema:valueName:
                      const: temObjectiveApertureDefault
                    schema:name:
                      const: TEM Objective Aperture
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
                allOf:
                - contains:
                    title: TEM Objective Aperture
                    description: Objective aperture diameter used to select the imaging
                      beam condition in TEM mode.
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/temTAPP/temObjectiveApertureDefault
                      '@type':
                        const:
                        - schema:PropertyValueSpecification
                      schema:valueName:
                        const: temObjectiveApertureDefault
                      schema:name:
                        const: TEM Objective Aperture
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
      allOf:
      - contains:
          properties:
            schema:additionalType:
              contains:
                const: TEM
              schema:inDefinedTermSet: ada:vocab/instrumentType
          required:
          - schema:additionalType
    schema:additionalProperty:
      type: array
      items:
        anyOf:
        - title: Sample Holder
          description: Type of specimen holder used.
          type: object
          properties:
            '@id':
              const: ada:parameter/temTAPP/sampleHolderDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: sampleHolderDefault
            schema:name:
              const: Sample Holder
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
        - title: EFTEM Energy Window
          description: 'Energy window(s) used for EFTEM elemental mapping: center
            energy, width, and acquisition method (three-window or jump-ratio). Record
            ''N/A'' where EFTEM is not listed in Analytical Sub-mode.'
          type: object
          properties:
            '@id':
              const: ada:parameter/temTAPP/eftemEnergyWindowDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: eftemEnergyWindowDefault
            schema:name:
              const: EFTEM Energy Window
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
        - title: HAADF Collection Angles
          description: Inner and outer collection angles of the HAADF detector in
            milliradians (mrad). Inner angle can be derived from camera length and
            detector geometry.
          type: object
          properties:
            '@id':
              const: ada:parameter/temTAPP/haadfCollectionAnglesDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: haadfCollectionAnglesDefault
            schema:name:
              const: HAADF Collection Angles
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
        - title: STEM Probe Diameter
          description: 'Nominal or measured diameter of the focused electron probe
            at the sample, reported in nm. Related to, but distinct from, Convergence
            Semi-Angle: the two quantities are connected via aberration coefficients,
            defocus, and probe current, which are not always published. Report whichever
            is known; if both are known, report both fields. Also governs STEM-EDS
            and STEM-EELS acquisition where those detectors are used.'
          type: object
          properties:
            '@id':
              const: ada:parameter/temTAPP/stemProbeDiameterDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: stemProbeDiameterDefault
            schema:name:
              const: STEM Probe Diameter
            ada:dataType:
              const: number
            ada:fieldScope:
              const: session
            schema:readonlyValue:
              const: false
            ada:tier:
              const: R
            schema:unitText:
              const: nm
          required:
          - '@id'
          - '@type'
          - schema:valueName
          - schema:name
          - ada:dataType
          - ada:fieldScope
        - title: STEM Probe Current
          description: Probe current in picoamperes (pA) or nanoamperes (nA). Also
            governs STEM-EDS and STEM-EELS acquisition where those detectors are used.
          type: object
          properties:
            '@id':
              const: ada:parameter/temTAPP/stemProbeCurrentDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: stemProbeCurrentDefault
            schema:name:
              const: STEM Probe Current
            ada:dataType:
              const: number
            ada:fieldScope:
              const: session
            schema:readonlyValue:
              const: false
            ada:tier:
              const: R
            schema:unitText:
              const: pA or nA
          required:
          - '@id'
          - '@type'
          - schema:valueName
          - schema:name
          - ada:dataType
          - ada:fieldScope
        - title: STEM Scan Dimensions
          description: "Number of pixels in the STEM scan frame (X \xD7 Y pixels).
            Also governs STEM-EDS and STEM-EELS acquisition where those detectors
            are used."
          type: object
          properties:
            '@id':
              const: ada:parameter/temTAPP/stemScanDimensionsDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: stemScanDimensionsDefault
            schema:name:
              const: STEM Scan Dimensions
            ada:dataType:
              const: number
            ada:fieldScope:
              const: session
            schema:readonlyValue:
              const: false
            ada:tier:
              const: R
            schema:unitText:
              const: pixels x pixels
          required:
          - '@id'
          - '@type'
          - schema:valueName
          - schema:name
          - ada:dataType
          - ada:fieldScope
        - title: STEM Frame Averaging
          description: Number of frames averaged (with drift correction if applicable)
            to produce the final STEM image. Also governs STEM-EDS and STEM-EELS acquisition
            where those detectors are used.
          type: object
          properties:
            '@id':
              const: ada:parameter/temTAPP/stemFrameAveragingDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: stemFrameAveragingDefault
            schema:name:
              const: STEM Frame Averaging
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
        - title: Selected-Area Aperture Size
          description: Diameter of the selected-area aperture used in SAED mode, defining
            the specimen region that contributes to the diffraction pattern.
          type: object
          properties:
            '@id':
              const: ada:parameter/temTAPP/selectedAreaApertureSizeDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: selectedAreaApertureSizeDefault
            schema:name:
              const: Selected-Area Aperture Size
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
        - title: Precession Angle
          description: Precession semi-angle in degrees for precession electron diffraction
            (PED). Not applicable to SAED, CBED, or standard 4D-STEM. Record 'N/A'
            where Precession ED is not listed in Analytical Sub-mode.
          type: object
          properties:
            '@id':
              const: ada:parameter/temTAPP/precessionAngleDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: precessionAngleDefault
            schema:name:
              const: Precession Angle
            ada:dataType:
              const: number
            ada:fieldScope:
              const: session
            schema:readonlyValue:
              const: false
            ada:tier:
              const: R
            schema:unitText:
              const: degrees
          required:
          - '@id'
          - '@type'
          - schema:valueName
          - schema:name
          - ada:dataType
          - ada:fieldScope
        - title: 4D-STEM Scan Grid and Area
          description: "Number of probe positions in the 4D-STEM dataset (scan pixels
            \xD7 scan pixels) and the physical area covered. Probe step size is the
            physical area divided by scan pixel count. Record 'N/A' where 4D-STEM
            is not listed in Analytical Sub-mode."
          type: object
          properties:
            '@id':
              const: ada:parameter/temTAPP/stemScanGridAndArea4DDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: stemScanGridAndArea4DDefault
            schema:name:
              const: 4D-STEM Scan Grid and Area
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
        - title: 4D-STEM Dwell Time per Probe Position
          description: Time spent acquiring each diffraction pattern in the 4D-STEM
            dataset in milliseconds. Record 'N/A' where 4D-STEM is not listed in Analytical
            Sub-mode.
          type: object
          properties:
            '@id':
              const: ada:parameter/temTAPP/stemDwellTimePerProbePosition4DDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: stemDwellTimePerProbePosition4DDefault
            schema:name:
              const: 4D-STEM Dwell Time per Probe Position
            ada:dataType:
              const: number
            ada:fieldScope:
              const: session
            schema:readonlyValue:
              const: false
            ada:tier:
              const: R
            schema:unitText:
              const: ms
          required:
          - '@id'
          - '@type'
          - schema:valueName
          - schema:name
          - ada:dataType
          - ada:fieldScope
        - title: Diffraction Camera Length Calibration Method
          description: Method used to calibrate the camera length constant and convert
            pixel distances in diffraction patterns to d-spacings or reciprocal lattice
            vectors.
          type: object
          properties:
            '@id':
              const: ada:parameter/temTAPP/diffractionCameraLengthCalibrationMethodDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: diffractionCameraLengthCalibrationMethodDefault
            schema:name:
              const: Diffraction Camera Length Calibration Method
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
        - title: EDS Live Time per Point or Pixel
          description: EDS spectral acquisition live time per analysis point (point/line
            mode) or per pixel (spectrum image) in seconds. Also referred to as "EDS
            Acquisition Time" in EPMA and some SEM-EDS contexts, where the per-pixel
            distinction is less relevant. Record 'N/A' where EDS is not listed in
            Spectroscopic Detector(s).
          type: object
          properties:
            '@id':
              const: ada:parameter/temTAPP/edsLiveTimePerPointOrPixelDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: edsLiveTimePerPointOrPixelDefault
            schema:name:
              const: EDS Live Time per Point or Pixel
            ada:dataType:
              const: number
            ada:fieldScope:
              const: session
            schema:readonlyValue:
              const: false
            ada:tier:
              const: R
            schema:unitText:
              const: s
          required:
          - '@id'
          - '@type'
          - schema:valueName
          - schema:name
          - ada:dataType
          - ada:fieldScope
        - title: EDS Energy Range
          description: Energy range of EDS spectrum acquisition in keV. Record 'N/A'
            where EDS is not listed in Spectroscopic Detector(s).
          type: object
          properties:
            '@id':
              const: ada:parameter/temTAPP/edsEnergyRangeDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: edsEnergyRangeDefault
            schema:name:
              const: EDS Energy Range
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
        - title: EELS Energy Dispersion
          description: Energy dispersion of the EELS spectrometer in eV per channel.
            Record 'N/A' where EELS is not listed in Spectroscopic Detector(s).
          type: object
          properties:
            '@id':
              const: ada:parameter/temTAPP/eelsEnergyDispersion
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/temTAPP/eelsEnergyDispersion
            schema:name:
              const: EELS Energy Dispersion
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
        - title: EELS Energy Resolution
          description: Full-width at half-maximum (FWHM) of the zero-loss peak in
            eV, measured at operating conditions. Record 'N/A' where EELS is not listed
            in Spectroscopic Detector(s).
          type: object
          properties:
            '@id':
              const: ada:parameter/temTAPP/eelsEnergyResolution
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/temTAPP/eelsEnergyResolution
            schema:name:
              const: EELS Energy Resolution
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
        - title: 4D-STEM Orientation Mapping Method
          description: Algorithm, software module, and reference crystal structure
            database used for automated crystal orientation mapping (ACOM) from 4D-STEM
            datasets. Record 'N/A' where 4D-STEM is not listed in Analytical Sub-mode.
          type: object
          properties:
            '@id':
              const: ada:parameter/temTAPP/stemOrientationMappingMethod4D
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/temTAPP/stemOrientationMappingMethod4D
            schema:name:
              const: 4D-STEM Orientation Mapping Method
            schema:value:
              type: string
          required:
          - '@id'
          - '@type'
          - schema:propertyID
          - schema:name
          - schema:value
          readOnly: true
        - title: EDS Spectral Processing Type
          description: Method used to process EDS spectra and extract net peak intensities
            from raw spectral data. Applied before quantification (EDS Quantification
            Method). Common approaches include background fitting and subtraction
            followed by peak integration, and filter fit or Gaussian deconvolution
            for overlapping peaks. Record 'N/A' where EDS is not listed in Spectroscopic
            Detector(s).
          type: object
          properties:
            '@id':
              const: ada:parameter/temTAPP/edsSpectralProcessingType
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/temTAPP/edsSpectralProcessingType
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
        - title: Specimen Thickness Determination Method
          description: Method used to estimate TEM foil thickness.
          type: object
          properties:
            '@id':
              const: ada:parameter/temTAPP/specimenThicknessDeterminationMethodDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: specimenThicknessDeterminationMethodDefault
            schema:name:
              const: Specimen Thickness Determination Method
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
        - title: EELS Energy Calibration
          description: Method and reference used to calibrate the EELS energy axis.
            Record 'N/A' where EELS is not listed in Spectroscopic Detector(s).
          type: object
          properties:
            '@id':
              const: ada:parameter/temTAPP/eelsEnergyCalibrationDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: eelsEnergyCalibrationDefault
            schema:name:
              const: EELS Energy Calibration
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
        - title: Diffraction Calibration Reference
          description: "Reference material or internal standard used to calibrate
            the electron diffraction camera constant (camera length \xD7 electron
            wavelength), enabling conversion of pixel distances to d-spacings."
          type: object
          properties:
            '@id':
              const: ada:parameter/temTAPP/diffractionCalibrationReferenceDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: diffractionCalibrationReferenceDefault
            schema:name:
              const: Diffraction Calibration Reference
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
        - title: EDS Detection Limit
          description: Estimated detection limits by EDS under this procedure's conditions,
            one per reported concentration variable (one per analyte, these being
            the same set). Record 'N/A' where EDS is not listed in Spectroscopic Detector(s).
          type: object
          properties:
            '@id':
              const: ada:parameter/temTAPP/edsDetectionLimitDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: edsDetectionLimitDefault
            schema:name:
              const: EDS Detection Limit
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
        - title: EDS Counting Statistics / Accumulation Criterion
          description: Quality criterion used to determine when sufficient EDS signal
            has been accumulated for a given pixel or point, in lieu of or in addition
            to a fixed live time. Expressed as a target relative uncertainty on major-element
            peak counts achieved by accumulating successive scan frames (e.g., "1%
            counting statistics on major elements"; ">10% counting statistics"). Distinct
            from EDS Live Time per Point or Pixel, which records a fixed-duration
            setting. Record 'N/A' where EDS is not listed in Spectroscopic Detector(s).
          type: object
          properties:
            '@id':
              const: ada:parameter/temTAPP/edsCountingStatisticsAccumulationCriterionDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: edsCountingStatisticsAccumulationCriterionDefault
            schema:name:
              const: EDS Counting Statistics / Accumulation Criterion
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
        - title: EELS Chemical State Determination Method
          description: Method used to determine the chemical or oxidation state of
            an element from the fine structure of its ionization edge (ELNES), together
            with the reference data or calibration the determination relies on. Name
            the method family and cite the calibration curve or reference spectra
            used. Record 'N/A' where no chemical-state determination is made.
          type: object
          properties:
            '@id':
              const: ada:parameter/temTAPP/eelsChemicalStateDeterminationMethodDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: eelsChemicalStateDeterminationMethodDefault
            schema:name:
              const: EELS Chemical State Determination Method
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
      allOf:
      - contains:
          title: Sample Holder
          description: Type of specimen holder used.
          type: object
          properties:
            '@id':
              const: ada:parameter/temTAPP/sampleHolderDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: sampleHolderDefault
            schema:name:
              const: Sample Holder
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
          title: EFTEM Energy Window
          description: 'Energy window(s) used for EFTEM elemental mapping: center
            energy, width, and acquisition method (three-window or jump-ratio). Record
            ''N/A'' where EFTEM is not listed in Analytical Sub-mode.'
          type: object
          properties:
            '@id':
              const: ada:parameter/temTAPP/eftemEnergyWindowDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: eftemEnergyWindowDefault
            schema:name:
              const: EFTEM Energy Window
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
          title: HAADF Collection Angles
          description: Inner and outer collection angles of the HAADF detector in
            milliradians (mrad). Inner angle can be derived from camera length and
            detector geometry.
          type: object
          properties:
            '@id':
              const: ada:parameter/temTAPP/haadfCollectionAnglesDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: haadfCollectionAnglesDefault
            schema:name:
              const: HAADF Collection Angles
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
          title: STEM Probe Diameter
          description: 'Nominal or measured diameter of the focused electron probe
            at the sample, reported in nm. Related to, but distinct from, Convergence
            Semi-Angle: the two quantities are connected via aberration coefficients,
            defocus, and probe current, which are not always published. Report whichever
            is known; if both are known, report both fields. Also governs STEM-EDS
            and STEM-EELS acquisition where those detectors are used.'
          type: object
          properties:
            '@id':
              const: ada:parameter/temTAPP/stemProbeDiameterDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: stemProbeDiameterDefault
            schema:name:
              const: STEM Probe Diameter
            ada:dataType:
              const: number
            ada:fieldScope:
              const: session
            schema:readonlyValue:
              const: false
            ada:tier:
              const: R
            schema:unitText:
              const: nm
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
          title: STEM Probe Current
          description: Probe current in picoamperes (pA) or nanoamperes (nA). Also
            governs STEM-EDS and STEM-EELS acquisition where those detectors are used.
          type: object
          properties:
            '@id':
              const: ada:parameter/temTAPP/stemProbeCurrentDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: stemProbeCurrentDefault
            schema:name:
              const: STEM Probe Current
            ada:dataType:
              const: number
            ada:fieldScope:
              const: session
            schema:readonlyValue:
              const: false
            ada:tier:
              const: R
            schema:unitText:
              const: pA or nA
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
          title: STEM Scan Dimensions
          description: "Number of pixels in the STEM scan frame (X \xD7 Y pixels).
            Also governs STEM-EDS and STEM-EELS acquisition where those detectors
            are used."
          type: object
          properties:
            '@id':
              const: ada:parameter/temTAPP/stemScanDimensionsDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: stemScanDimensionsDefault
            schema:name:
              const: STEM Scan Dimensions
            ada:dataType:
              const: number
            ada:fieldScope:
              const: session
            schema:readonlyValue:
              const: false
            ada:tier:
              const: R
            schema:unitText:
              const: pixels x pixels
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
          title: STEM Frame Averaging
          description: Number of frames averaged (with drift correction if applicable)
            to produce the final STEM image. Also governs STEM-EDS and STEM-EELS acquisition
            where those detectors are used.
          type: object
          properties:
            '@id':
              const: ada:parameter/temTAPP/stemFrameAveragingDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: stemFrameAveragingDefault
            schema:name:
              const: STEM Frame Averaging
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
          title: Selected-Area Aperture Size
          description: Diameter of the selected-area aperture used in SAED mode, defining
            the specimen region that contributes to the diffraction pattern.
          type: object
          properties:
            '@id':
              const: ada:parameter/temTAPP/selectedAreaApertureSizeDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: selectedAreaApertureSizeDefault
            schema:name:
              const: Selected-Area Aperture Size
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
          title: Precession Angle
          description: Precession semi-angle in degrees for precession electron diffraction
            (PED). Not applicable to SAED, CBED, or standard 4D-STEM. Record 'N/A'
            where Precession ED is not listed in Analytical Sub-mode.
          type: object
          properties:
            '@id':
              const: ada:parameter/temTAPP/precessionAngleDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: precessionAngleDefault
            schema:name:
              const: Precession Angle
            ada:dataType:
              const: number
            ada:fieldScope:
              const: session
            schema:readonlyValue:
              const: false
            ada:tier:
              const: R
            schema:unitText:
              const: degrees
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
          title: 4D-STEM Scan Grid and Area
          description: "Number of probe positions in the 4D-STEM dataset (scan pixels
            \xD7 scan pixels) and the physical area covered. Probe step size is the
            physical area divided by scan pixel count. Record 'N/A' where 4D-STEM
            is not listed in Analytical Sub-mode."
          type: object
          properties:
            '@id':
              const: ada:parameter/temTAPP/stemScanGridAndArea4DDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: stemScanGridAndArea4DDefault
            schema:name:
              const: 4D-STEM Scan Grid and Area
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
          title: 4D-STEM Dwell Time per Probe Position
          description: Time spent acquiring each diffraction pattern in the 4D-STEM
            dataset in milliseconds. Record 'N/A' where 4D-STEM is not listed in Analytical
            Sub-mode.
          type: object
          properties:
            '@id':
              const: ada:parameter/temTAPP/stemDwellTimePerProbePosition4DDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: stemDwellTimePerProbePosition4DDefault
            schema:name:
              const: 4D-STEM Dwell Time per Probe Position
            ada:dataType:
              const: number
            ada:fieldScope:
              const: session
            schema:readonlyValue:
              const: false
            ada:tier:
              const: R
            schema:unitText:
              const: ms
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
          title: Diffraction Camera Length Calibration Method
          description: Method used to calibrate the camera length constant and convert
            pixel distances in diffraction patterns to d-spacings or reciprocal lattice
            vectors.
          type: object
          properties:
            '@id':
              const: ada:parameter/temTAPP/diffractionCameraLengthCalibrationMethodDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: diffractionCameraLengthCalibrationMethodDefault
            schema:name:
              const: Diffraction Camera Length Calibration Method
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
          title: EDS Live Time per Point or Pixel
          description: EDS spectral acquisition live time per analysis point (point/line
            mode) or per pixel (spectrum image) in seconds. Also referred to as "EDS
            Acquisition Time" in EPMA and some SEM-EDS contexts, where the per-pixel
            distinction is less relevant. Record 'N/A' where EDS is not listed in
            Spectroscopic Detector(s).
          type: object
          properties:
            '@id':
              const: ada:parameter/temTAPP/edsLiveTimePerPointOrPixelDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: edsLiveTimePerPointOrPixelDefault
            schema:name:
              const: EDS Live Time per Point or Pixel
            ada:dataType:
              const: number
            ada:fieldScope:
              const: session
            schema:readonlyValue:
              const: false
            ada:tier:
              const: R
            schema:unitText:
              const: s
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
          title: EDS Energy Range
          description: Energy range of EDS spectrum acquisition in keV. Record 'N/A'
            where EDS is not listed in Spectroscopic Detector(s).
          type: object
          properties:
            '@id':
              const: ada:parameter/temTAPP/edsEnergyRangeDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: edsEnergyRangeDefault
            schema:name:
              const: EDS Energy Range
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
          title: EELS Energy Dispersion
          description: Energy dispersion of the EELS spectrometer in eV per channel.
            Record 'N/A' where EELS is not listed in Spectroscopic Detector(s).
          type: object
          properties:
            '@id':
              const: ada:parameter/temTAPP/eelsEnergyDispersion
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/temTAPP/eelsEnergyDispersion
            schema:name:
              const: EELS Energy Dispersion
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
          title: EELS Energy Resolution
          description: Full-width at half-maximum (FWHM) of the zero-loss peak in
            eV, measured at operating conditions. Record 'N/A' where EELS is not listed
            in Spectroscopic Detector(s).
          type: object
          properties:
            '@id':
              const: ada:parameter/temTAPP/eelsEnergyResolution
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/temTAPP/eelsEnergyResolution
            schema:name:
              const: EELS Energy Resolution
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
          title: 4D-STEM Orientation Mapping Method
          description: Algorithm, software module, and reference crystal structure
            database used for automated crystal orientation mapping (ACOM) from 4D-STEM
            datasets. Record 'N/A' where 4D-STEM is not listed in Analytical Sub-mode.
          type: object
          properties:
            '@id':
              const: ada:parameter/temTAPP/stemOrientationMappingMethod4D
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/temTAPP/stemOrientationMappingMethod4D
            schema:name:
              const: 4D-STEM Orientation Mapping Method
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
          title: EDS Spectral Processing Type
          description: Method used to process EDS spectra and extract net peak intensities
            from raw spectral data. Applied before quantification (EDS Quantification
            Method). Common approaches include background fitting and subtraction
            followed by peak integration, and filter fit or Gaussian deconvolution
            for overlapping peaks. Record 'N/A' where EDS is not listed in Spectroscopic
            Detector(s).
          type: object
          properties:
            '@id':
              const: ada:parameter/temTAPP/edsSpectralProcessingType
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/temTAPP/edsSpectralProcessingType
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
          title: Specimen Thickness Determination Method
          description: Method used to estimate TEM foil thickness.
          type: object
          properties:
            '@id':
              const: ada:parameter/temTAPP/specimenThicknessDeterminationMethodDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: specimenThicknessDeterminationMethodDefault
            schema:name:
              const: Specimen Thickness Determination Method
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
          title: EELS Energy Calibration
          description: Method and reference used to calibrate the EELS energy axis.
            Record 'N/A' where EELS is not listed in Spectroscopic Detector(s).
          type: object
          properties:
            '@id':
              const: ada:parameter/temTAPP/eelsEnergyCalibrationDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: eelsEnergyCalibrationDefault
            schema:name:
              const: EELS Energy Calibration
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
          title: Diffraction Calibration Reference
          description: "Reference material or internal standard used to calibrate
            the electron diffraction camera constant (camera length \xD7 electron
            wavelength), enabling conversion of pixel distances to d-spacings."
          type: object
          properties:
            '@id':
              const: ada:parameter/temTAPP/diffractionCalibrationReferenceDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: diffractionCalibrationReferenceDefault
            schema:name:
              const: Diffraction Calibration Reference
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
          title: EDS Detection Limit
          description: Estimated detection limits by EDS under this procedure's conditions,
            one per reported concentration variable (one per analyte, these being
            the same set). Record 'N/A' where EDS is not listed in Spectroscopic Detector(s).
          type: object
          properties:
            '@id':
              const: ada:parameter/temTAPP/edsDetectionLimitDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: edsDetectionLimitDefault
            schema:name:
              const: EDS Detection Limit
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
          title: EDS Counting Statistics / Accumulation Criterion
          description: Quality criterion used to determine when sufficient EDS signal
            has been accumulated for a given pixel or point, in lieu of or in addition
            to a fixed live time. Expressed as a target relative uncertainty on major-element
            peak counts achieved by accumulating successive scan frames (e.g., "1%
            counting statistics on major elements"; ">10% counting statistics"). Distinct
            from EDS Live Time per Point or Pixel, which records a fixed-duration
            setting. Record 'N/A' where EDS is not listed in Spectroscopic Detector(s).
          type: object
          properties:
            '@id':
              const: ada:parameter/temTAPP/edsCountingStatisticsAccumulationCriterionDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: edsCountingStatisticsAccumulationCriterionDefault
            schema:name:
              const: EDS Counting Statistics / Accumulation Criterion
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
          title: EELS Chemical State Determination Method
          description: Method used to determine the chemical or oxidation state of
            an element from the fine structure of its ionization edge (ELNES), together
            with the reference data or calibration the determination relies on. Name
            the method family and cite the calibration curve or reference spectra
            used. Record 'N/A' where no chemical-state determination is made.
          type: object
          properties:
            '@id':
              const: ada:parameter/temTAPP/eelsChemicalStateDeterminationMethodDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: eelsChemicalStateDeterminationMethodDefault
            schema:name:
              const: EELS Chemical State Determination Method
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
    ada:spectroscopicDetectorDefault:
      description: Spectroscopic detectors present and used under this procedure.
        EDS and EELS parameter fields in Group 4 apply only when the corresponding
        detector is listed here.
      type: string
      enum:
      - EDS only
      - EELS only
      - EDS and EELS
      - EELS and EFTEM
      - EDS and EELS and EFTEM
      - None
      - N/A
      - missing
    bios:computationalTool:
      type: array
      items:
        type: object
        allOf:
        - if:
            properties:
              ada:toolRole:
                const: dataReduction
            required:
            - ada:toolRole
          then:
            properties:
              schema:name:
                description: Software used to simulate electron diffraction patterns
                  for comparison with experimental SAED patterns during phase identification
                  (e.g., SingleCrystal, CrystalMaker, JEMS, DIFPACK). Complements
                  the Acquisition Software field, which covers data collection; simulation
                  software is used at the interpretation and data processing step.
                anyOf:
                - type: string
                - type: array
                  items:
                    type: string
        required:
        - ada:toolRole
    ada:analyticalSubModeDefault:
      description: Sub-mode(s) of imaging or diffraction performed under this procedure.
        Multiple values apply when the procedure covers more than one sub-mode within
        a given analytical mode.
      anyOf:
      - type: string
        enum:
        - BF-TEM
        - DF-TEM
        - HRTEM
        - EFTEM (TEM Imaging); HAADF
        - ABF
        - BF-STEM
        - ADF
        - MAADF (STEM Imaging); SAED
        - CBED
        - Nanobeam diffraction
        - Precession ED
        - 4D-STEM (Electron Diffraction)
        - N/A
        - None
        - missing
      - type: string
    ada:convergenceSemiAngle:
      description: Semi-angle of the converged electron probe in milliradians.
      anyOf:
      - type: number
      - type: string
      readOnly: true
    ada:stemDwellTimePerPixelDefault:
      description: Time spent acquiring signal at each pixel during STEM scanning
        in milliseconds. For dose-sensitive materials, minimize dwell and compensate
        with frame averaging. Also governs STEM-EDS and STEM-EELS acquisition where
        those detectors are used. For 4D-STEM dwell time see '4D-STEM Dwell Time per
        Probe Position'.
      anyOf:
      - type: number
      - type: string
    ada:cameraLengthDefault:
      description: "Nominal camera length in millimeters used for diffraction pattern
        acquisition. Must be calibrated to convert pixel distances to d-spacings.
        Calibration to absolute d-spacings is required \u2014 see 'Diffraction Calibration
        Reference'."
      anyOf:
      - type: number
      - type: string
    ada:edsAcquisitionModeDefault:
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
      - Simultaneous EDS+EELS
      - N/A
      - None
      - missing
    ada:edsQuantificationMethod:
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
        - Cliff-Lorimer (k-factor)
        - "\u03B6-factor (zeta-factor)"
        - Absorption-corrected Cliff-Lorimer
        - N/A
        - None
        - missing
      - type: string
      readOnly: true
    ada:eelsAcquisitionModeDefault:
      description: Mode of EELS data acquisition. Record 'N/A' where EELS is not listed
        in Spectroscopic Detector(s).
      type: string
      enum:
      - Point spectrum
      - Line scan
      - Spectrum image (SI)
      - Dual-EELS (simultaneous low- and high-loss)
      - Simultaneous EDS+EELS
      - N/A
      - None
      - missing
    ada:eelsEdgesDefault:
      type: array
      items:
        description: 'Ionization edge(s) acquired by EELS, specified by element symbol
          and edge label (e.g., Fe L2,3; O K). Provides the EELS-specific counterpart
          to the Analyte field: while Analyte lists elements, EELS Edges documents
          which ionization edges were used and their approximate energy loss positions.
          The edge list may be narrowed at analysis time. Record ''N/A'' where EELS
          is not listed in Spectroscopic Detector(s).'
        type: string
    ada:eelsCollectionSemiAngle:
      description: Semi-angle of the EELS spectrometer entrance aperture in milliradians.
        Record 'N/A' where EELS is not listed in Spectroscopic Detector(s).
      anyOf:
      - type: number
      - type: string
      readOnly: true
    ada:eelsAcquisitionTimePerSpectrumDefault:
      description: Exposure time per individual EELS spectrum (or per pixel for spectrum
        images) in seconds. Record 'N/A' where EELS is not listed in Spectroscopic
        Detector(s).
      anyOf:
      - type: number
      - type: string
    ada:eelsEnergyLossRangeDefault:
      description: Energy loss range acquired, defined by onset energy and width in
        eV. The target range covers the registered analyte edges; the actual range
        acquired may differ. Record 'N/A' where EELS is not listed in Spectroscopic
        Detector(s).
      type: string
    ada:phaseIdentificationMethod:
      description: Method used to identify crystalline phases from electron diffraction
        patterns or d-spacings, whether from SAED patterns, spot diffraction, or diffraction
        data extracted from 4D-STEM datasets.
      type: string
      readOnly: true
    ada:channelTemplate:
      type: object
      properties:
        ada:channelColumns:
          type: array
          items:
            anyOf:
            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/ChannelIdentifierColumn
            - title: EELS Background Subtraction Method
              description: Method used to subtract the background beneath the ionization
                edge of interest to extract the net edge signal. Record 'N/A' where
                EELS is not listed in Spectroscopic Detector(s).
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/temTAPP/eelsBackgroundSubtractionMethod
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: eelsBackgroundSubtractionMethod
                schema:name:
                  const: EELS Background Subtraction Method
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
            - title: EELS Detection Limit
              description: Estimated detection limit or minimum detectable concentration
                for target edges under this procedure. Record 'N/A' where EELS is
                not listed in Spectroscopic Detector(s).
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/temTAPP/eelsDetectionLimit
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: eelsDetectionLimit
                schema:name:
                  const: EELS Detection Limit
                ada:dataType:
                  const: number
                schema:readonlyValue:
                  const: false
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
          allOf:
          - contains:
              title: EELS Background Subtraction Method
              description: Method used to subtract the background beneath the ionization
                edge of interest to extract the net edge signal. Record 'N/A' where
                EELS is not listed in Spectroscopic Detector(s).
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/temTAPP/eelsBackgroundSubtractionMethod
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: eelsBackgroundSubtractionMethod
                schema:name:
                  const: EELS Background Subtraction Method
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
              title: EELS Detection Limit
              description: Estimated detection limit or minimum detectable concentration
                for target edges under this procedure. Record 'N/A' where EELS is
                not listed in Spectroscopic Detector(s).
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/temTAPP/eelsDetectionLimit
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: eelsDetectionLimit
                schema:name:
                  const: EELS Detection Limit
                ada:dataType:
                  const: number
                schema:readonlyValue:
                  const: false
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
    ada:edsCalibrationStandardDefault:
      description: Reference material(s) used to validate EDS quantification or determine
        experimental k-factors or zeta-factors. Record 'N/A' where EDS is not listed
        in Spectroscopic Detector(s).
      type: string
    schema:variableMeasured:
      type: array
      items:
        anyOf:
        - title: Dataset variable
          description: A measured variable of this dataset that is not one of the
            procedure's declared reported properties. schema:variableMeasured carries
            the dataset's actual variables; the reported-property branches above are
            permitted members of it, not the whole of it.
          type: object
          required:
          - '@type'
          properties:
            '@type':
              type: array
              contains:
                enum:
                - cdi:InstanceVariable
                - schema:PropertyValue
        - title: EDS Detection Limit
          description: Estimated detection limits by EDS under this procedure's conditions,
            one per reported concentration variable (one per analyte, these being
            the same set). Record 'N/A' where EDS is not listed in Spectroscopic Detector(s).
          type: object
          properties:
            '@id':
              const: ada:parameter/temTAPP/edsDetectionLimitDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: edsDetectionLimitDefault
            schema:name:
              const: EDS Detection Limit
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
          title: EDS Detection Limit
          description: Estimated detection limits by EDS under this procedure's conditions,
            one per reported concentration variable (one per analyte, these being
            the same set). Record 'N/A' where EDS is not listed in Spectroscopic Detector(s).
          type: object
          properties:
            '@id':
              const: ada:parameter/temTAPP/edsDetectionLimitDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: edsDetectionLimitDefault
            schema:name:
              const: EDS Detection Limit
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
    ada:analyticalMode:
      type: array
      items:
        type: string
        enum:
        - TEM Imaging
        - STEM Imaging
        - Electron Diffraction
  required:
  - ada:spectroscopicDetectorDefault
  - ada:analyticalSubModeDefault
  - ada:convergenceSemiAngle
  - ada:stemDwellTimePerPixelDefault
  - ada:cameraLengthDefault
  - ada:edsAcquisitionModeDefault
  - ada:edsQuantificationMethod
  - ada:eelsAcquisitionModeDefault
  - ada:eelsCollectionSemiAngle
  - ada:eelsAcquisitionTimePerSpectrumDefault
  - ada:eelsEnergyLossRangeDefault
  - ada:phaseIdentificationMethod
  - ada:edsCalibrationStandardDefault

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/TEM/tapp/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/TEM/tapp/schema.yaml)


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
    "wd": "https://www.wikidata.org/entity/",
    "nxs": "https://manual.nexusformat.org/classes/",
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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/TEM/tapp/context.jsonld)

## Sources

* [TEM_TAPP_v7.xlsx (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/TEM/tapp`

