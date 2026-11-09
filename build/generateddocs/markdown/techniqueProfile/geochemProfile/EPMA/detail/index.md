
# EPMA Instrument Detail (Schema)

`ogch.techniqueProfile.geochemProfile.EPMA.detail` *v0.1*

Electron Microprobe Analysis instrument-specific detail properties. Defines properties: @type, spectrometersUsed, signalUsed.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### detail example Ma2015
detail instance derived from Ma+2015 | Caltech GPS | WDS Point Analysis (JEOL 8200).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "ex": "https://example.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/",
    "prov": "http://www.w3.org/ns/prov#"
  },
  "@id": "ex:epmaTAPP-detail-Ma2015",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "EPMA",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/epmaTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 15,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "15 kV"
                },
                {
                  "@id": "ada:parameter/epmaTAPP/beamDiameter",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/beamDiameter"
                    }
                  ],
                  "schema:name": "Beam Diameter",
                  "schema:value": "N — 'beam in focused mode' is recorded under Beam Mode; no diameter is given",
                  "schema:unitText": "no value available: unnamed property"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:epmaTAPP-detail-Ma2015/instrument/EPMA"
            }
          ]
        },
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "acquisition",
              "schema:name": "Probe for EPMA (Probe Software, Inc.)",
              "@type": [
                "schema:SoftwareApplication"
              ]
            },
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "N — the 'CITZAF correction procedure' is recorded under Matrix Correction Method; the only software named is Probe for EPMA",
              "@type": [
                "schema:SoftwareApplication"
              ]
            }
          ]
        }
      ],
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening"
                }
              ],
              "schema:name": "Pre-Analysis Imaging and Screening",
              "schema:value": "SEM BSE imaging on a ZEISS 1550VP field-emission SEM, which locates the occurrences the probe then analyses — \"SEM BSE image showing tissintite in a shock melt pocket, in Tissint section UT2\" (Fig. 1 caption, p.2). The paper lists EPMA, SEM, EBSD, synchrotron XRD and micro-Raman as one suite (p.2) without stating the order"
            }
          ],
          "schema:name": "Tissint Mars meteorite"
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Caltech GPS Division Analytical Facility"
      },
      "schema:description": "Ma et al. 2015, Earth Planet. Sci. Lett. — tissintite discovery paper (Tissint Mars meteorite). Instrument stated as \"JEOL 8200 electron microprobe\" (no JXA prefix). WDS explicitly stated (\"WDS: 15 kV; 5 nA; beam in focused mode\"). Point analysis only; no X-ray mapping reported. Probe for EPMA stated; CITZAF correction procedure (Armstrong 1995). Full standard suite with X-ray lines given. Detection limits: K=0.02, Cr=0.05, Mn=0.06 wt% from Table 1 footnote. Caltech GPS Division Analytical Facility.",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Polished thin section; carbon coating N",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "schema:additionalProperty": [],
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:deadTime": -9999
    }
  ],
  "schema:contributor": [
    {
      "schema:roleName": "analyst",
      "schema:contributor": {
        "schema:name": "Chi Ma"
      }
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "DOE Cooperative Agreement DE-NA0001982; NSF EAR 322082; NASA NNN13D465T; NASA Cosmochemistry NNX11AG58G and NNX12AH63G; NSF EAR 1344942 and 1440005 — acknowledged author by author for the study as a whole; none is attributed to the microprobe work"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM (Carl Zeiss 1550VP FE-SEM, BSE imaging); EBSD (HKL system on ZEISS 1550VP); synchrotron XRD; micro-Raman"
      }
    }
  ],
  "ada:analyticalMode": [
    "WDS Point Analysis — 'WDS: 15 kV; 5 nA; beam in focused mode'; point analyses only"
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "SiO2, TiO2, Al2O3, FeO, MgO, CaO, Na2O, K2O, Cr2O3, MnO: one standard deviation of the mean; other: N — Table 1 note b: 'Errors given inside parentheses are one standard deviation of the mean based on all of the analyses'"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "Chi Ma",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "DOE Cooperative Agreement DE-NA0001982; NSF EAR 322082; NASA NNN13D465T; NASA Cosmochemistry NNX11AG58G and NNX12AH63G; NSF EAR 1344942 and 1440005 — acknowledged author by author for the study as a whole; none is attributed to the microprobe work",
  "ada:sampleName": "Tissint Mars meteorite",
  "ada:samplingUnitName": "Labelled at section level only: tissintite \"was identified in sections UT1, UT2 and UT3\" (p.2); Table 1 groups the point analyses by phase and setting (\"Wormy type tissintite\", \"Rimming tissintite\", \"Maskelynite away from melt pockets\" …) with counts (n = 6, 9, 17 …), not labels (p.5)",
  "ada:targetMaterialOfSamplingUnit": "each unit is named by its material: tissintite (wormy, rimming), maskelynite (three settings), pigeonite, fayalite — Table 1",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:detectionLimit": "K2O: 0.02 wt% K; Cr2O3: 0.05 wt% Cr; MnO: 0.06 wt% Mn; other: N — Table 1 footnote c, attached to the b.d. entries of the K2O, Cr2O3 and MnO rows: 'b.d. = below detection limit: 0.02 wt% K, 0.05 wt% Cr, 0.06 wt% Mn'",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    },
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EPMA/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:epmaTAPP-detail-Ma2015",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "EPMA",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/epmaTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 15,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "15 kV"
                },
                {
                  "@id": "ada:parameter/epmaTAPP/beamDiameter",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/beamDiameter"
                    }
                  ],
                  "schema:name": "Beam Diameter",
                  "schema:value": "N \u2014 'beam in focused mode' is recorded under Beam Mode; no diameter is given",
                  "schema:unitText": "no value available: unnamed property"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:epmaTAPP-detail-Ma2015/instrument/EPMA"
            }
          ]
        },
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "acquisition",
              "schema:name": "Probe for EPMA (Probe Software, Inc.)",
              "@type": [
                "schema:SoftwareApplication"
              ]
            },
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "N \u2014 the 'CITZAF correction procedure' is recorded under Matrix Correction Method; the only software named is Probe for EPMA",
              "@type": [
                "schema:SoftwareApplication"
              ]
            }
          ]
        }
      ],
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening"
                }
              ],
              "schema:name": "Pre-Analysis Imaging and Screening",
              "schema:value": "SEM BSE imaging on a ZEISS 1550VP field-emission SEM, which locates the occurrences the probe then analyses \u2014 \"SEM BSE image showing tissintite in a shock melt pocket, in Tissint section UT2\" (Fig. 1 caption, p.2). The paper lists EPMA, SEM, EBSD, synchrotron XRD and micro-Raman as one suite (p.2) without stating the order"
            }
          ],
          "schema:name": "Tissint Mars meteorite"
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Caltech GPS Division Analytical Facility"
      },
      "schema:description": "Ma et al. 2015, Earth Planet. Sci. Lett. \u2014 tissintite discovery paper (Tissint Mars meteorite). Instrument stated as \"JEOL 8200 electron microprobe\" (no JXA prefix). WDS explicitly stated (\"WDS: 15 kV; 5 nA; beam in focused mode\"). Point analysis only; no X-ray mapping reported. Probe for EPMA stated; CITZAF correction procedure (Armstrong 1995). Full standard suite with X-ray lines given. Detection limits: K=0.02, Cr=0.05, Mn=0.06 wt% from Table 1 footnote. Caltech GPS Division Analytical Facility.",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Polished thin section; carbon coating N",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "schema:additionalProperty": [],
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:deadTime": -9999
    }
  ],
  "schema:contributor": [
    {
      "schema:roleName": "analyst",
      "schema:contributor": {
        "schema:name": "Chi Ma"
      }
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "DOE Cooperative Agreement DE-NA0001982; NSF EAR 322082; NASA NNN13D465T; NASA Cosmochemistry NNX11AG58G and NNX12AH63G; NSF EAR 1344942 and 1440005 \u2014 acknowledged author by author for the study as a whole; none is attributed to the microprobe work"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM (Carl Zeiss 1550VP FE-SEM, BSE imaging); EBSD (HKL system on ZEISS 1550VP); synchrotron XRD; micro-Raman"
      }
    }
  ],
  "ada:analyticalMode": [
    "WDS Point Analysis \u2014 'WDS: 15 kV; 5 nA; beam in focused mode'; point analyses only"
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "SiO2, TiO2, Al2O3, FeO, MgO, CaO, Na2O, K2O, Cr2O3, MnO: one standard deviation of the mean; other: N \u2014 Table 1 note b: 'Errors given inside parentheses are one standard deviation of the mean based on all of the analyses'"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "Chi Ma",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "DOE Cooperative Agreement DE-NA0001982; NSF EAR 322082; NASA NNN13D465T; NASA Cosmochemistry NNX11AG58G and NNX12AH63G; NSF EAR 1344942 and 1440005 \u2014 acknowledged author by author for the study as a whole; none is attributed to the microprobe work",
  "ada:sampleName": "Tissint Mars meteorite",
  "ada:samplingUnitName": "Labelled at section level only: tissintite \"was identified in sections UT1, UT2 and UT3\" (p.2); Table 1 groups the point analyses by phase and setting (\"Wormy type tissintite\", \"Rimming tissintite\", \"Maskelynite away from melt pockets\" \u2026) with counts (n = 6, 9, 17 \u2026), not labels (p.5)",
  "ada:targetMaterialOfSamplingUnit": "each unit is named by its material: tissintite (wormy, rimming), maskelynite (three settings), pigeonite, fayalite \u2014 Table 1",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:detectionLimit": "K2O: 0.02 wt% K; Cr2O3: 0.05 wt% Cr; MnO: 0.06 wt% Mn; other: N \u2014 Table 1 footnote c, attached to the b.d. entries of the K2O, Cr2O3 and MnO rows: 'b.d. = below detection limit: 0.02 wt% K, 0.05 wt% Cr, 0.06 wt% Mn'",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix bios: <https://bioschemas.org/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix dqv: <http://www.w3.org/ns/dqv#> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:epmaTAPP-detail-Ma2015 a schema1:Dataset,
        schema1:Product ;
    schema1:contributor [ schema1:contributor [ schema1:name "Chi Ma" ] ;
            schema1:roleName "analyst" ] ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "DOE Cooperative Agreement DE-NA0001982; NSF EAR 322082; NASA NNN13D465T; NASA Cosmochemistry NNX11AG58G and NNX12AH63G; NSF EAR 1344942 and 1440005 — acknowledged author by author for the study as a whole; none is attributed to the microprobe work" ] ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "SEM (Carl Zeiss 1550VP FE-SEM, BSE imaging); EBSD (HKL system on ZEISS 1550VP); synchrotron XRD; micro-Raman" ] ] ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Analytical Accuracy" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Analytical Precision" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Goodness-of-Fit" ;
            dqv:value "SiO2, TiO2, Al2O3, FeO, MgO, CaO, Na2O, K2O, Cr2O3, MnO: one standard deviation of the mean; other: N — Table 1 note b: 'Errors given inside parentheses are one standard deviation of the mean based on all of the analyses'" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Polished thin section; carbon coating N" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ] ] ;
            schema1:description "Ma et al. 2015, Earth Planet. Sci. Lett. — tissintite discovery paper (Tissint Mars meteorite). Instrument stated as \"JEOL 8200 electron microprobe\" (no JXA prefix). WDS explicitly stated (\"WDS: 15 kV; 5 nA; beam in focused mode\"). Point analysis only; no X-ray mapping reported. Probe for EPMA stated; CITZAF correction procedure (Armstrong 1995). Full standard suite with X-ray lines given. Detection limits: K=0.02, Cr=0.05, Mn=0.06 wt% from Table 1 footnote. Caltech GPS Division Analytical Facility." ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Caltech GPS Division Analytical Facility" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
                    schema1:name "Tissint Mars meteorite" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ schema1:instrument <https://example.org/epmaTAPP-detail-Ma2015/instrument/EPMA> ],
                [ bios:computationalTool [ a schema1:SoftwareApplication ;
                            schema1:name "Probe for EPMA (Probe Software, Inc.)" ;
                            ada:toolRole "acquisition" ],
                        [ a schema1:SoftwareApplication ;
                            schema1:name "N — the 'CITZAF correction procedure' is recorded under Matrix Correction Method; the only software named is Probe for EPMA" ;
                            ada:toolRole "dataReduction" ] ] ;
            ada:combinedResults [ ] ;
            ada:deadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "Chi Ma" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "WDS Point Analysis — 'WDS: 15 kV; 5 nA; beam in focused mode'; point analyses only" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit "K2O: 0.02 wt% K; Cr2O3: 0.05 wt% Cr; MnO: 0.06 wt% Mn; other: N — Table 1 footnote c, attached to the b.d. entries of the K2O, Cr2O3 and MnO rows: 'b.d. = below detection limit: 0.02 wt% K, 0.05 wt% Cr, 0.06 wt% Mn'" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "DOE Cooperative Agreement DE-NA0001982; NSF EAR 322082; NASA NNN13D465T; NASA Cosmochemistry NNX11AG58G and NNX12AH63G; NSF EAR 1344942 and 1440005 — acknowledged author by author for the study as a whole; none is attributed to the microprobe work" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:sampleName "Tissint Mars meteorite" ;
    ada:samplingUnitName "Labelled at section level only: tissintite \"was identified in sections UT1, UT2 and UT3\" (p.2); Table 1 groups the point analyses by phase and setting (\"Wormy type tissintite\", \"Rimming tissintite\", \"Maskelynite away from melt pockets\" …) with counts (n = 6, 9, 17 …), not labels (p.5)" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "each unit is named by its material: tissintite (wormy, rimming), maskelynite (three settings), pigeonite, fayalite — Table 1" .

<https://example.org/epmaTAPP-detail-Ma2015/instrument/EPMA> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/epmaTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDiameter> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EPMA" ;
    schema1:name "no value available: schema:name" .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:description "15 kV" ;
    schema1:name "Accelerating Voltage" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/epmaTAPP/acceleratingVoltage> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 15 .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDiameter> a schema1:PropertyValue ;
    schema1:name "Beam Diameter" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDiameter> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value "N — 'beam in focused mode' is recorded under Beam Mode; no diameter is given" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "SEM BSE imaging on a ZEISS 1550VP field-emission SEM, which locates the occurrences the probe then analyses — \"SEM BSE image showing tissintite in a shock melt pocket, in Tissint section UT2\" (Fig. 1 caption, p.2). The paper lists EPMA, SEM, EBSD, synchrotron XRD and micro-Raman as one suite (p.2) without stating the order" .


```


### detail example Hu2020
detail instance derived from Hu+2020 | IGGCAS | WDS Point Analysis (JEOL JXA-8100).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "ex": "https://example.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/",
    "prov": "http://www.w3.org/ns/prov#"
  },
  "@id": "ex:epmaTAPP-detail-Hu2020",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "EPMA",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/epmaTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 15,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "15 kV"
                },
                {
                  "@id": "ada:parameter/epmaTAPP/beamDiameter",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/beamDiameter"
                    }
                  ],
                  "schema:name": "Beam Diameter",
                  "schema:value": 15,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "N — only 15 kV and 10 nA are given"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:epmaTAPP-detail-Hu2020/instrument/EPMA"
            }
          ]
        },
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "N — 'The Bence-Albee method was used' is recorded under Matrix Correction Method; no software is named",
              "@type": [
                "schema:SoftwareApplication"
              ]
            }
          ]
        }
      ],
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening"
                }
              ],
              "schema:name": "Pre-Analysis Imaging and Screening",
              "schema:value": "SEM imaging and EDS mapping on three instruments before the probe — \"Scanning electron microscopy (SEM) imaging and energy dispersive X-ray spectroscopy (EDS) mapping were conducted\" on a Nova NanoSEM 450 at IGGCAS, a SUPRA55 at NAOC and a JEOL JSM-7100F at NIPR, after which \"Quantitative analyses ... were conducted by electron probe microanalysis (EPMA) with the JEOL JXA-8100 at IGGCAS\" (p.2)"
            }
          ],
          "schema:name": "NWA 8657 shergottite"
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Institute of Geology and Geophysics, Chinese Academy of Sciences (IGGCAS), Beijing"
      },
      "schema:description": "Hu et al. 2020, Geochim. Cosmochim. Acta — coesite in NWA 8657 shergottite. JEOL JXA-8100 at IGGCAS; 15 kV, 10 nA; point analysis only; WDS or EDS not stated. Matrix correction: Bence-Albee (not PAP). Full primary standard suite stated (kaersutite, jadeite, bustamite, K-feldspar, rutile, Cr2O3). Mn Kα / Cr Kβ interference correction applied. Detection limits 0.01-0.06 wt% stated per oxide. Analytical software not stated.",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Polished thick section (NWA 8657); carbon coating N",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "schema:additionalProperty": [],
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:deadTime": -9999
    }
  ],
  "schema:contributor": [
    {
      "schema:roleName": "analyst",
      "schema:contributor": {
        "schema:name": "Sen Hu"
      }
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NSFC 41573057, 41430105 and 41973062; China Scholarship Council 201804910284; IGGCAS key research program IGGCAS-201905 — 'This study was financially supported by ...'"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM-EDS (FEI Nova NanoSEM 450); Raman spectroscopy"
      }
    },
    {
      "schema:linkRelationship": "coupledDataset",
      "schema:target": "https://doi.org/10.1016/j.gca.2020.07.021 — 'Supplementary data to this article can be found online at ...'"
    }
  ],
  "ada:analyticalMode": [
    "N — quantitative point analyses ('Quantitative analyses of maskelynite ... were conducted by electron probe microanalysis'); WDS or EDS is not stated, and the list has no value without one"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "Sen Hu",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NSFC 41573057, 41430105 and 41973062; China Scholarship Council 201804910284; IGGCAS key research program IGGCAS-201905 — 'This study was financially supported by ...'",
  "ada:sampleName": "NWA 8657 shergottite",
  "ada:samplingUnitName": "Sample name only — \"a polished thick section of the martian meteorite NWA 8657\" (p.2), not otherwise labelled; analyses are grouped by phase (\"maskelynite, melt inclusion glasses, silica glasses, coesite aggregates, and mesostasis\", p.2)",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:detectionLimit": "K2O: 0.01 wt%; SiO2, Al2O3, MgO, CaO, Na2O: 0.02 wt%; TiO2, Cr2O3: 0.03 wt%; FeO: 0.05 wt%; MnO: 0.06 wt% — p.2",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    },
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EPMA/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:epmaTAPP-detail-Hu2020",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "EPMA",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/epmaTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 15,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "15 kV"
                },
                {
                  "@id": "ada:parameter/epmaTAPP/beamDiameter",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/beamDiameter"
                    }
                  ],
                  "schema:name": "Beam Diameter",
                  "schema:value": 15,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "N \u2014 only 15 kV and 10 nA are given"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:epmaTAPP-detail-Hu2020/instrument/EPMA"
            }
          ]
        },
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "N \u2014 'The Bence-Albee method was used' is recorded under Matrix Correction Method; no software is named",
              "@type": [
                "schema:SoftwareApplication"
              ]
            }
          ]
        }
      ],
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening"
                }
              ],
              "schema:name": "Pre-Analysis Imaging and Screening",
              "schema:value": "SEM imaging and EDS mapping on three instruments before the probe \u2014 \"Scanning electron microscopy (SEM) imaging and energy dispersive X-ray spectroscopy (EDS) mapping were conducted\" on a Nova NanoSEM 450 at IGGCAS, a SUPRA55 at NAOC and a JEOL JSM-7100F at NIPR, after which \"Quantitative analyses ... were conducted by electron probe microanalysis (EPMA) with the JEOL JXA-8100 at IGGCAS\" (p.2)"
            }
          ],
          "schema:name": "NWA 8657 shergottite"
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Institute of Geology and Geophysics, Chinese Academy of Sciences (IGGCAS), Beijing"
      },
      "schema:description": "Hu et al. 2020, Geochim. Cosmochim. Acta \u2014 coesite in NWA 8657 shergottite. JEOL JXA-8100 at IGGCAS; 15 kV, 10 nA; point analysis only; WDS or EDS not stated. Matrix correction: Bence-Albee (not PAP). Full primary standard suite stated (kaersutite, jadeite, bustamite, K-feldspar, rutile, Cr2O3). Mn K\u03b1 / Cr K\u03b2 interference correction applied. Detection limits 0.01-0.06 wt% stated per oxide. Analytical software not stated.",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Polished thick section (NWA 8657); carbon coating N",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "schema:additionalProperty": [],
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:deadTime": -9999
    }
  ],
  "schema:contributor": [
    {
      "schema:roleName": "analyst",
      "schema:contributor": {
        "schema:name": "Sen Hu"
      }
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NSFC 41573057, 41430105 and 41973062; China Scholarship Council 201804910284; IGGCAS key research program IGGCAS-201905 \u2014 'This study was financially supported by ...'"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM-EDS (FEI Nova NanoSEM 450); Raman spectroscopy"
      }
    },
    {
      "schema:linkRelationship": "coupledDataset",
      "schema:target": "https://doi.org/10.1016/j.gca.2020.07.021 \u2014 'Supplementary data to this article can be found online at ...'"
    }
  ],
  "ada:analyticalMode": [
    "N \u2014 quantitative point analyses ('Quantitative analyses of maskelynite ... were conducted by electron probe microanalysis'); WDS or EDS is not stated, and the list has no value without one"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "Sen Hu",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NSFC 41573057, 41430105 and 41973062; China Scholarship Council 201804910284; IGGCAS key research program IGGCAS-201905 \u2014 'This study was financially supported by ...'",
  "ada:sampleName": "NWA 8657 shergottite",
  "ada:samplingUnitName": "Sample name only \u2014 \"a polished thick section of the martian meteorite NWA 8657\" (p.2), not otherwise labelled; analyses are grouped by phase (\"maskelynite, melt inclusion glasses, silica glasses, coesite aggregates, and mesostasis\", p.2)",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:detectionLimit": "K2O: 0.01 wt%; SiO2, Al2O3, MgO, CaO, Na2O: 0.02 wt%; TiO2, Cr2O3: 0.03 wt%; FeO: 0.05 wt%; MnO: 0.06 wt% \u2014 p.2",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999
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

ex:epmaTAPP-detail-Hu2020 a schema1:Dataset,
        schema1:Product ;
    schema1:contributor [ schema1:contributor [ schema1:name "Sen Hu" ] ;
            schema1:roleName "analyst" ] ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "NSFC 41573057, 41430105 and 41973062; China Scholarship Council 201804910284; IGGCAS key research program IGGCAS-201905 — 'This study was financially supported by ...'" ] ;
    schema1:relatedLink [ schema1:linkRelationship "coupledDataset" ;
            schema1:target "https://doi.org/10.1016/j.gca.2020.07.021 — 'Supplementary data to this article can be found online at ...'" ],
        [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "SEM-EDS (FEI Nova NanoSEM 450); Raman spectroscopy" ] ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Polished thick section (NWA 8657); carbon coating N" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ] ] ;
            schema1:description "Hu et al. 2020, Geochim. Cosmochim. Acta — coesite in NWA 8657 shergottite. JEOL JXA-8100 at IGGCAS; 15 kV, 10 nA; point analysis only; WDS or EDS not stated. Matrix correction: Bence-Albee (not PAP). Full primary standard suite stated (kaersutite, jadeite, bustamite, K-feldspar, rutile, Cr2O3). Mn Kα / Cr Kβ interference correction applied. Detection limits 0.01-0.06 wt% stated per oxide. Analytical software not stated." ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Institute of Geology and Geophysics, Chinese Academy of Sciences (IGGCAS), Beijing" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
                    schema1:name "NWA 8657 shergottite" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ bios:computationalTool [ a schema1:SoftwareApplication ;
                            schema1:name "N — 'The Bence-Albee method was used' is recorded under Matrix Correction Method; no software is named" ;
                            ada:toolRole "dataReduction" ] ],
                [ schema1:instrument <https://example.org/epmaTAPP-detail-Hu2020/instrument/EPMA> ] ;
            ada:combinedResults [ ] ;
            ada:deadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "Sen Hu" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "N — quantitative point analyses ('Quantitative analyses of maskelynite ... were conducted by electron probe microanalysis'); WDS or EDS is not stated, and the list has no value without one" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit "K2O: 0.01 wt%; SiO2, Al2O3, MgO, CaO, Na2O: 0.02 wt%; TiO2, Cr2O3: 0.03 wt%; FeO: 0.05 wt%; MnO: 0.06 wt% — p.2" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NSFC 41573057, 41430105 and 41973062; China Scholarship Council 201804910284; IGGCAS key research program IGGCAS-201905 — 'This study was financially supported by ...'" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:sampleName "NWA 8657 shergottite" ;
    ada:samplingUnitName "Sample name only — \"a polished thick section of the martian meteorite NWA 8657\" (p.2), not otherwise labelled; analyses are grouped by phase (\"maskelynite, melt inclusion glasses, silica glasses, coesite aggregates, and mesostasis\", p.2)" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" .

<https://example.org/epmaTAPP-detail-Hu2020/instrument/EPMA> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/epmaTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDiameter> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EPMA" ;
    schema1:name "no value available: schema:name" .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:description "15 kV" ;
    schema1:name "Accelerating Voltage" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/epmaTAPP/acceleratingVoltage> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 15 .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDiameter> a schema1:PropertyValue ;
    schema1:description "N — only 15 kV and 10 nA are given" ;
    schema1:name "Beam Diameter" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDiameter> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 15 .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "SEM imaging and EDS mapping on three instruments before the probe — \"Scanning electron microscopy (SEM) imaging and energy dispersive X-ray spectroscopy (EDS) mapping were conducted\" on a Nova NanoSEM 450 at IGGCAS, a SUPRA55 at NAOC and a JEOL JSM-7100F at NIPR, after which \"Quantitative analyses ... were conducted by electron probe microanalysis (EPMA) with the JEOL JXA-8100 at IGGCAS\" (p.2)" .


```


### detail example Liu2016
detail instance derived from Liu+2016_UT | Cameca SX100 | WDS Mapping (U.Tennessee).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "ex": "https://example.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/",
    "prov": "http://www.w3.org/ns/prov#"
  },
  "@id": "ex:epmaTAPP-detail-Liu2016",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "EPMA",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/epmaTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 15,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "15 kV"
                },
                {
                  "@id": "ada:parameter/epmaTAPP/beamDiameter",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/beamDiameter"
                    }
                  ],
                  "schema:name": "Beam Diameter",
                  "schema:value": 1,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "olivine, pyroxene, Fe-Ti-Cr oxides: 1–2 µm; maskelynite, phosphate, sulfide, glass: 5–10 µm — p.3"
                },
                {
                  "@id": "ada:parameter/epmaTAPP/mappingBeamCurrent",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/mappingBeamCurrent"
                    }
                  ],
                  "schema:name": "Mapping Beam Current",
                  "schema:value": 20,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "20 nA (section maps: Ca, Al, Fe, Mg Kα); 200 nA (olivine megacryst maps) — p.3"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:epmaTAPP-detail-Liu2016/instrument/EPMA"
            }
          ]
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/epmaTAPP/beamDamageMinimization",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/epmaTAPP/beamDamageMinimization"
            }
          ],
          "schema:name": "Beam Damage Minimization",
          "schema:value": "N — a defocused 5–10 µm beam at 10 nA is used for maskelynite, phosphate, sulfide and glass, but the paper gives no reason for it"
        },
        {
          "@id": "ada:parameter/epmaTAPP/stepSizePixelSize",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/epmaTAPP/stepSizePixelSize"
            }
          ],
          "schema:name": "Step Size / Pixel Size",
          "schema:value": 8,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "8-12 µm (BSE + Ca/Al/Fe/Mg Ka phase maps at UT); 2 µm (olivine megacryst Ka maps; instrument ambiguous)"
        }
      ],
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening"
                }
              ],
              "schema:name": "Pre-Analysis Imaging and Screening",
              "schema:value": "Petrographic microscopy and SEM — \"The petrography of these sections was examined using a petrographic microscope and a scanning electron microscope\" before the microprobe work (p.3)"
            }
          ],
          "schema:name": "Tissint thin sections UT1, UT2, UT3; Tata-1-C1 to C3; Tata-2-C1 to C3; Tata-3-C1 to C3; Tissint-B"
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Department of Earth and Planetary Sciences, University of Tennessee, Knoxville"
      },
      "schema:description": "Liu et al. 2016, Meteorit. Planet. Sci. — Tissint mineral chemistry. Protocol 1 of 2: University of Tennessee Cameca SX100. Same paper also uses Caltech GPS JXA-8200 (see Liu+2016_Cal column). Point analysis AND X-ray mapping performed at UT. Specific mapping: BSE + Ca/Al/Fe/Mg Ka maps (15 kV, 20 nA, step 8-12 µm). Olivine megacryst mapping (15 kV, 200 nA, step 2 µm, dwell ~0.5 s) described as \"using the EMP\" — instrument ambiguous (may be UT or Caltech instrument). Standards, matrix correction, and software not stated.",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Polished thin sections (coating type N)",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "schema:additionalProperty": [],
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:deadTime": -9999
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NASA Cosmochemistry NNX11AG58G and NNN13D465T; NSF EAR-1226270; NSF EAR-1019770 — 'We acknowledge partial support by ...'"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM (BSE imaging); petrographic microscopy; LA-ICP-MS (Agilent 7500ce, Virginia Tech)"
      }
    }
  ],
  "ada:analyticalMode": [
    "N — quantitative point analyses and elemental X-ray maps; WDS or EDS is not stated, and the list has no value without one"
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "SiO2, TiO2, Al2O3, Cr2O3, MgO, CaO, MnO, FeO, NiO, Na2O, K2O, P2O5: 1σ, one standard deviation of the average; other: N — Table 3 note b: '1σ is 1 standard deviation of the average'"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA Cosmochemistry NNX11AG58G and NNN13D465T; NSF EAR-1226270; NSF EAR-1019770 — 'We acknowledge partial support by ...'",
  "ada:sampleName": "Tissint thin sections UT1, UT2, UT3; Tata-1-C1 to C3; Tata-2-C1 to C3; Tata-3-C1 to C3; Tissint-B",
  "ada:samplingUnitName": "Labelled at section level: X-ray maps are placed by thin section, e.g. an olivine megacryst \"in Tata-2-C3\" whose \"Red box outlines the area of X-ray maps\" (Fig. 3 caption, p.7); the sections are \"UT1 to UT3\" and \"Tata-1-C1 to C3, Tata-2-C1 to C3, and Tata-3-C1 to C3\" (pp.2–3). Map areas carry no labels of their own",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:detectionLimit": "SiO2, TiO2, Al2O3, MgO, CaO: <0.03 wt%; FeO, MnO, Cr2O3, NiO, Na2O, K2O, P2O5: <0.05–0.1 wt%; other: N — 'Detection limits are typically <0.03 wt% for SiO2, TiO2, Al2O3, MgO, and CaO; <0.05–0.1 wt% for FeO, MnO, Cr2O3, NiO, Na2O, K2O, and P2O5' (p.3)",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    },
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EPMA/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:epmaTAPP-detail-Liu2016",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "EPMA",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/epmaTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 15,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "15 kV"
                },
                {
                  "@id": "ada:parameter/epmaTAPP/beamDiameter",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/beamDiameter"
                    }
                  ],
                  "schema:name": "Beam Diameter",
                  "schema:value": 1,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "olivine, pyroxene, Fe-Ti-Cr oxides: 1\u20132 \u00b5m; maskelynite, phosphate, sulfide, glass: 5\u201310 \u00b5m \u2014 p.3"
                },
                {
                  "@id": "ada:parameter/epmaTAPP/mappingBeamCurrent",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/mappingBeamCurrent"
                    }
                  ],
                  "schema:name": "Mapping Beam Current",
                  "schema:value": 20,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "20 nA (section maps: Ca, Al, Fe, Mg K\u03b1); 200 nA (olivine megacryst maps) \u2014 p.3"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:epmaTAPP-detail-Liu2016/instrument/EPMA"
            }
          ]
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/epmaTAPP/beamDamageMinimization",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/epmaTAPP/beamDamageMinimization"
            }
          ],
          "schema:name": "Beam Damage Minimization",
          "schema:value": "N \u2014 a defocused 5\u201310 \u00b5m beam at 10 nA is used for maskelynite, phosphate, sulfide and glass, but the paper gives no reason for it"
        },
        {
          "@id": "ada:parameter/epmaTAPP/stepSizePixelSize",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/epmaTAPP/stepSizePixelSize"
            }
          ],
          "schema:name": "Step Size / Pixel Size",
          "schema:value": 8,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "8-12 \u00b5m (BSE + Ca/Al/Fe/Mg Ka phase maps at UT); 2 \u00b5m (olivine megacryst Ka maps; instrument ambiguous)"
        }
      ],
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening"
                }
              ],
              "schema:name": "Pre-Analysis Imaging and Screening",
              "schema:value": "Petrographic microscopy and SEM \u2014 \"The petrography of these sections was examined using a petrographic microscope and a scanning electron microscope\" before the microprobe work (p.3)"
            }
          ],
          "schema:name": "Tissint thin sections UT1, UT2, UT3; Tata-1-C1 to C3; Tata-2-C1 to C3; Tata-3-C1 to C3; Tissint-B"
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Department of Earth and Planetary Sciences, University of Tennessee, Knoxville"
      },
      "schema:description": "Liu et al. 2016, Meteorit. Planet. Sci. \u2014 Tissint mineral chemistry. Protocol 1 of 2: University of Tennessee Cameca SX100. Same paper also uses Caltech GPS JXA-8200 (see Liu+2016_Cal column). Point analysis AND X-ray mapping performed at UT. Specific mapping: BSE + Ca/Al/Fe/Mg Ka maps (15 kV, 20 nA, step 8-12 \u00b5m). Olivine megacryst mapping (15 kV, 200 nA, step 2 \u00b5m, dwell ~0.5 s) described as \"using the EMP\" \u2014 instrument ambiguous (may be UT or Caltech instrument). Standards, matrix correction, and software not stated.",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Polished thin sections (coating type N)",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "schema:additionalProperty": [],
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:deadTime": -9999
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NASA Cosmochemistry NNX11AG58G and NNN13D465T; NSF EAR-1226270; NSF EAR-1019770 \u2014 'We acknowledge partial support by ...'"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM (BSE imaging); petrographic microscopy; LA-ICP-MS (Agilent 7500ce, Virginia Tech)"
      }
    }
  ],
  "ada:analyticalMode": [
    "N \u2014 quantitative point analyses and elemental X-ray maps; WDS or EDS is not stated, and the list has no value without one"
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "SiO2, TiO2, Al2O3, Cr2O3, MgO, CaO, MnO, FeO, NiO, Na2O, K2O, P2O5: 1\u03c3, one standard deviation of the average; other: N \u2014 Table 3 note b: '1\u03c3 is 1 standard deviation of the average'"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA Cosmochemistry NNX11AG58G and NNN13D465T; NSF EAR-1226270; NSF EAR-1019770 \u2014 'We acknowledge partial support by ...'",
  "ada:sampleName": "Tissint thin sections UT1, UT2, UT3; Tata-1-C1 to C3; Tata-2-C1 to C3; Tata-3-C1 to C3; Tissint-B",
  "ada:samplingUnitName": "Labelled at section level: X-ray maps are placed by thin section, e.g. an olivine megacryst \"in Tata-2-C3\" whose \"Red box outlines the area of X-ray maps\" (Fig. 3 caption, p.7); the sections are \"UT1 to UT3\" and \"Tata-1-C1 to C3, Tata-2-C1 to C3, and Tata-3-C1 to C3\" (pp.2\u20133). Map areas carry no labels of their own",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:detectionLimit": "SiO2, TiO2, Al2O3, MgO, CaO: <0.03 wt%; FeO, MnO, Cr2O3, NiO, Na2O, K2O, P2O5: <0.05\u20130.1 wt%; other: N \u2014 'Detection limits are typically <0.03 wt% for SiO2, TiO2, Al2O3, MgO, and CaO; <0.05\u20130.1 wt% for FeO, MnO, Cr2O3, NiO, Na2O, K2O, and P2O5' (p.3)",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix dqv: <http://www.w3.org/ns/dqv#> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:epmaTAPP-detail-Liu2016 a schema1:Dataset,
        schema1:Product ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "NASA Cosmochemistry NNX11AG58G and NNN13D465T; NSF EAR-1226270; NSF EAR-1019770 — 'We acknowledge partial support by ...'" ] ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "SEM (BSE imaging); petrographic microscopy; LA-ICP-MS (Agilent 7500ce, Virginia Tech)" ] ] ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Goodness-of-Fit" ;
            dqv:value "SiO2, TiO2, Al2O3, Cr2O3, MgO, CaO, MnO, FeO, NiO, Na2O, K2O, P2O5: 1σ, one standard deviation of the average; other: N — Table 3 note b: '1σ is 1 standard deviation of the average'" ],
        [ dqv:isMeasurementOf "Analytical Precision" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Analytical Accuracy" ;
            dqv:value "no value available: dqv:value" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Polished thin sections (coating type N)" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDamageMinimization>,
                <https://ada.astromat.org/metadata/parameter/epmaTAPP/stepSizePixelSize> ;
            schema1:description "Liu et al. 2016, Meteorit. Planet. Sci. — Tissint mineral chemistry. Protocol 1 of 2: University of Tennessee Cameca SX100. Same paper also uses Caltech GPS JXA-8200 (see Liu+2016_Cal column). Point analysis AND X-ray mapping performed at UT. Specific mapping: BSE + Ca/Al/Fe/Mg Ka maps (15 kV, 20 nA, step 8-12 µm). Olivine megacryst mapping (15 kV, 200 nA, step 2 µm, dwell ~0.5 s) described as \"using the EMP\" — instrument ambiguous (may be UT or Caltech instrument). Standards, matrix correction, and software not stated." ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Department of Earth and Planetary Sciences, University of Tennessee, Knoxville" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
                    schema1:name "Tissint thin sections UT1, UT2, UT3; Tata-1-C1 to C3; Tata-2-C1 to C3; Tata-3-C1 to C3; Tissint-B" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ schema1:instrument <https://example.org/epmaTAPP-detail-Liu2016/instrument/EPMA> ] ;
            ada:combinedResults [ ] ;
            ada:deadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "N — quantitative point analyses and elemental X-ray maps; WDS or EDS is not stated, and the list has no value without one" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit "SiO2, TiO2, Al2O3, MgO, CaO: <0.03 wt%; FeO, MnO, Cr2O3, NiO, Na2O, K2O, P2O5: <0.05–0.1 wt%; other: N — 'Detection limits are typically <0.03 wt% for SiO2, TiO2, Al2O3, MgO, and CaO; <0.05–0.1 wt% for FeO, MnO, Cr2O3, NiO, Na2O, K2O, and P2O5' (p.3)" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NASA Cosmochemistry NNX11AG58G and NNN13D465T; NSF EAR-1226270; NSF EAR-1019770 — 'We acknowledge partial support by ...'" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:sampleName "Tissint thin sections UT1, UT2, UT3; Tata-1-C1 to C3; Tata-2-C1 to C3; Tata-3-C1 to C3; Tissint-B" ;
    ada:samplingUnitName "Labelled at section level: X-ray maps are placed by thin section, e.g. an olivine megacryst \"in Tata-2-C3\" whose \"Red box outlines the area of X-ray maps\" (Fig. 3 caption, p.7); the sections are \"UT1 to UT3\" and \"Tata-1-C1 to C3, Tata-2-C1 to C3, and Tata-3-C1 to C3\" (pp.2–3). Map areas carry no labels of their own" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" .

<https://example.org/epmaTAPP-detail-Liu2016/instrument/EPMA> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/epmaTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDiameter>,
        <https://ada.astromat.org/metadata/parameter/epmaTAPP/mappingBeamCurrent> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EPMA" ;
    schema1:name "no value available: schema:name" .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:description "15 kV" ;
    schema1:name "Accelerating Voltage" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/epmaTAPP/acceleratingVoltage> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 15 .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDamageMinimization> a schema1:PropertyValue ;
    schema1:name "Beam Damage Minimization" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDamageMinimization> ;
    schema1:value "N — a defocused 5–10 µm beam at 10 nA is used for maskelynite, phosphate, sulfide and glass, but the paper gives no reason for it" .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDiameter> a schema1:PropertyValue ;
    schema1:description "olivine, pyroxene, Fe-Ti-Cr oxides: 1–2 µm; maskelynite, phosphate, sulfide, glass: 5–10 µm — p.3" ;
    schema1:name "Beam Diameter" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDiameter> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1 .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/mappingBeamCurrent> a schema1:PropertyValue ;
    schema1:description "20 nA (section maps: Ca, Al, Fe, Mg Kα); 200 nA (olivine megacryst maps) — p.3" ;
    schema1:name "Mapping Beam Current" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/epmaTAPP/mappingBeamCurrent> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 20 .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/stepSizePixelSize> a schema1:PropertyValue ;
    schema1:description "8-12 µm (BSE + Ca/Al/Fe/Mg Ka phase maps at UT); 2 µm (olivine megacryst Ka maps; instrument ambiguous)" ;
    schema1:name "Step Size / Pixel Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/epmaTAPP/stepSizePixelSize> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 8 .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "Petrographic microscopy and SEM — \"The petrography of these sections was examined using a petrographic microscope and a scanning electron microscope\" before the microprobe work (p.3)" .


```


### detail example Liu2016-2
detail instance derived from Liu+2016_Cal | JEOL JXA-8200 | WDS Point Analysis (Caltech GPS).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "ex": "https://example.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/",
    "prov": "http://www.w3.org/ns/prov#"
  },
  "@id": "ex:epmaTAPP-detail-Liu2016-2",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "EPMA",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/epmaTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 15,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "15 kV"
                },
                {
                  "@id": "ada:parameter/epmaTAPP/beamDiameter",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/beamDiameter"
                    }
                  ],
                  "schema:name": "Beam Diameter",
                  "schema:value": 1,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "olivine, pyroxene, Fe-Ti-Cr oxides: 1–2 µm; maskelynite, phosphate, sulfide, glass: 5–10 µm — p.3"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:epmaTAPP-detail-Liu2016-2/instrument/EPMA"
            }
          ]
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/epmaTAPP/beamDamageMinimization",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/epmaTAPP/beamDamageMinimization"
            }
          ],
          "schema:name": "Beam Damage Minimization",
          "schema:value": "N — a defocused 5–10 µm beam at 10 nA is used for maskelynite, phosphate, sulfide and glass, but the paper gives no reason for it"
        }
      ],
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening"
                }
              ],
              "schema:name": "Pre-Analysis Imaging and Screening",
              "schema:value": "Petrographic microscopy and SEM — \"The petrography of these sections was examined using a petrographic microscope and a scanning electron microscope\" (p.3); the same sections then went to both microprobes"
            }
          ],
          "schema:name": "Tissint thin sections UT1, UT2, UT3; Tata-1-C1 to C3; Tata-2-C1 to C3; Tata-3-C1 to C3; Tissint-B"
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Division of Geological and Planetary Sciences, Caltech"
      },
      "schema:description": "Liu et al. 2016, Meteorit. Planet. Sci. — Tissint mineral chemistry. Protocol 2 of 2: Caltech GPS Division JEOL JXA-8200. Point analysis only (no mapping attributed to Caltech instrument). Conditions stated jointly for UT and Caltech instruments. Standards, matrix correction, and software not stated for EPMA.",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Polished thin sections (coating type N)",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "schema:additionalProperty": [],
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:deadTime": -9999
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NASA Cosmochemistry NNX11AG58G and NNN13D465T; NSF EAR-1226270; NSF EAR-1019770 — 'We acknowledge partial support by ...'"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM (BSE imaging); petrographic microscopy; LA-ICP-MS (Agilent 7500ce, Virginia Tech)"
      }
    }
  ],
  "ada:analyticalMode": [
    "N — quantitative point analyses; WDS or EDS is not stated, and the list has no value without one"
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "SiO2, TiO2, Al2O3, Cr2O3, MgO, CaO, MnO, FeO, NiO, Na2O, K2O, P2O5: 1σ, one standard deviation of the average; other: N — Table 3 note b"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA Cosmochemistry NNX11AG58G and NNN13D465T; NSF EAR-1226270; NSF EAR-1019770 — 'We acknowledge partial support by ...'",
  "ada:sampleName": "Tissint thin sections UT1, UT2, UT3; Tata-1-C1 to C3; Tata-2-C1 to C3; Tata-3-C1 to C3; Tissint-B",
  "ada:samplingUnitName": "Labelled: thin sections \"UT1 to UT3\" and \"Tata-1-C1 to C3, Tata-2-C1 to C3, and Tata-3-C1 to C3\" (pp.2–3), and pyroxene grains within a section, e.g. \"T-3-C2 px1\" to \"T-3-C2 px5\" (Fig. 8, p.12); individual point analyses are not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:detectionLimit": "SiO2, TiO2, Al2O3, MgO, CaO: <0.03 wt%; FeO, MnO, Cr2O3, NiO, Na2O, K2O, P2O5: <0.05–0.1 wt%; other: N — 'Detection limits are typically <0.03 wt% for SiO2, TiO2, Al2O3, MgO, and CaO; <0.05–0.1 wt% for FeO, MnO, Cr2O3, NiO, Na2O, K2O, and P2O5' (p.3)",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    },
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EPMA/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:epmaTAPP-detail-Liu2016-2",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "EPMA",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/epmaTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 15,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "15 kV"
                },
                {
                  "@id": "ada:parameter/epmaTAPP/beamDiameter",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/beamDiameter"
                    }
                  ],
                  "schema:name": "Beam Diameter",
                  "schema:value": 1,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "olivine, pyroxene, Fe-Ti-Cr oxides: 1\u20132 \u00b5m; maskelynite, phosphate, sulfide, glass: 5\u201310 \u00b5m \u2014 p.3"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:epmaTAPP-detail-Liu2016-2/instrument/EPMA"
            }
          ]
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/epmaTAPP/beamDamageMinimization",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/epmaTAPP/beamDamageMinimization"
            }
          ],
          "schema:name": "Beam Damage Minimization",
          "schema:value": "N \u2014 a defocused 5\u201310 \u00b5m beam at 10 nA is used for maskelynite, phosphate, sulfide and glass, but the paper gives no reason for it"
        }
      ],
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening"
                }
              ],
              "schema:name": "Pre-Analysis Imaging and Screening",
              "schema:value": "Petrographic microscopy and SEM \u2014 \"The petrography of these sections was examined using a petrographic microscope and a scanning electron microscope\" (p.3); the same sections then went to both microprobes"
            }
          ],
          "schema:name": "Tissint thin sections UT1, UT2, UT3; Tata-1-C1 to C3; Tata-2-C1 to C3; Tata-3-C1 to C3; Tissint-B"
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Division of Geological and Planetary Sciences, Caltech"
      },
      "schema:description": "Liu et al. 2016, Meteorit. Planet. Sci. \u2014 Tissint mineral chemistry. Protocol 2 of 2: Caltech GPS Division JEOL JXA-8200. Point analysis only (no mapping attributed to Caltech instrument). Conditions stated jointly for UT and Caltech instruments. Standards, matrix correction, and software not stated for EPMA.",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Polished thin sections (coating type N)",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "schema:additionalProperty": [],
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:deadTime": -9999
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NASA Cosmochemistry NNX11AG58G and NNN13D465T; NSF EAR-1226270; NSF EAR-1019770 \u2014 'We acknowledge partial support by ...'"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM (BSE imaging); petrographic microscopy; LA-ICP-MS (Agilent 7500ce, Virginia Tech)"
      }
    }
  ],
  "ada:analyticalMode": [
    "N \u2014 quantitative point analyses; WDS or EDS is not stated, and the list has no value without one"
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "SiO2, TiO2, Al2O3, Cr2O3, MgO, CaO, MnO, FeO, NiO, Na2O, K2O, P2O5: 1\u03c3, one standard deviation of the average; other: N \u2014 Table 3 note b"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA Cosmochemistry NNX11AG58G and NNN13D465T; NSF EAR-1226270; NSF EAR-1019770 \u2014 'We acknowledge partial support by ...'",
  "ada:sampleName": "Tissint thin sections UT1, UT2, UT3; Tata-1-C1 to C3; Tata-2-C1 to C3; Tata-3-C1 to C3; Tissint-B",
  "ada:samplingUnitName": "Labelled: thin sections \"UT1 to UT3\" and \"Tata-1-C1 to C3, Tata-2-C1 to C3, and Tata-3-C1 to C3\" (pp.2\u20133), and pyroxene grains within a section, e.g. \"T-3-C2 px1\" to \"T-3-C2 px5\" (Fig. 8, p.12); individual point analyses are not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:detectionLimit": "SiO2, TiO2, Al2O3, MgO, CaO: <0.03 wt%; FeO, MnO, Cr2O3, NiO, Na2O, K2O, P2O5: <0.05\u20130.1 wt%; other: N \u2014 'Detection limits are typically <0.03 wt% for SiO2, TiO2, Al2O3, MgO, and CaO; <0.05\u20130.1 wt% for FeO, MnO, Cr2O3, NiO, Na2O, K2O, and P2O5' (p.3)",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix dqv: <http://www.w3.org/ns/dqv#> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:epmaTAPP-detail-Liu2016-2 a schema1:Dataset,
        schema1:Product ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "NASA Cosmochemistry NNX11AG58G and NNN13D465T; NSF EAR-1226270; NSF EAR-1019770 — 'We acknowledge partial support by ...'" ] ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "SEM (BSE imaging); petrographic microscopy; LA-ICP-MS (Agilent 7500ce, Virginia Tech)" ] ] ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Analytical Accuracy" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Goodness-of-Fit" ;
            dqv:value "SiO2, TiO2, Al2O3, Cr2O3, MgO, CaO, MnO, FeO, NiO, Na2O, K2O, P2O5: 1σ, one standard deviation of the average; other: N — Table 3 note b" ],
        [ dqv:isMeasurementOf "Analytical Precision" ;
            dqv:value "no value available: dqv:value" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Polished thin sections (coating type N)" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDamageMinimization> ;
            schema1:description "Liu et al. 2016, Meteorit. Planet. Sci. — Tissint mineral chemistry. Protocol 2 of 2: Caltech GPS Division JEOL JXA-8200. Point analysis only (no mapping attributed to Caltech instrument). Conditions stated jointly for UT and Caltech instruments. Standards, matrix correction, and software not stated for EPMA." ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Division of Geological and Planetary Sciences, Caltech" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
                    schema1:name "Tissint thin sections UT1, UT2, UT3; Tata-1-C1 to C3; Tata-2-C1 to C3; Tata-3-C1 to C3; Tissint-B" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ schema1:instrument <https://example.org/epmaTAPP-detail-Liu2016-2/instrument/EPMA> ] ;
            ada:combinedResults [ ] ;
            ada:deadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "N — quantitative point analyses; WDS or EDS is not stated, and the list has no value without one" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit "SiO2, TiO2, Al2O3, MgO, CaO: <0.03 wt%; FeO, MnO, Cr2O3, NiO, Na2O, K2O, P2O5: <0.05–0.1 wt%; other: N — 'Detection limits are typically <0.03 wt% for SiO2, TiO2, Al2O3, MgO, and CaO; <0.05–0.1 wt% for FeO, MnO, Cr2O3, NiO, Na2O, K2O, and P2O5' (p.3)" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NASA Cosmochemistry NNX11AG58G and NNN13D465T; NSF EAR-1226270; NSF EAR-1019770 — 'We acknowledge partial support by ...'" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:sampleName "Tissint thin sections UT1, UT2, UT3; Tata-1-C1 to C3; Tata-2-C1 to C3; Tata-3-C1 to C3; Tissint-B" ;
    ada:samplingUnitName "Labelled: thin sections \"UT1 to UT3\" and \"Tata-1-C1 to C3, Tata-2-C1 to C3, and Tata-3-C1 to C3\" (pp.2–3), and pyroxene grains within a section, e.g. \"T-3-C2 px1\" to \"T-3-C2 px5\" (Fig. 8, p.12); individual point analyses are not labelled" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" .

<https://example.org/epmaTAPP-detail-Liu2016-2/instrument/EPMA> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/epmaTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDiameter> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EPMA" ;
    schema1:name "no value available: schema:name" .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:description "15 kV" ;
    schema1:name "Accelerating Voltage" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/epmaTAPP/acceleratingVoltage> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 15 .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDamageMinimization> a schema1:PropertyValue ;
    schema1:name "Beam Damage Minimization" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDamageMinimization> ;
    schema1:value "N — a defocused 5–10 µm beam at 10 nA is used for maskelynite, phosphate, sulfide and glass, but the paper gives no reason for it" .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDiameter> a schema1:PropertyValue ;
    schema1:description "olivine, pyroxene, Fe-Ti-Cr oxides: 1–2 µm; maskelynite, phosphate, sulfide, glass: 5–10 µm — p.3" ;
    schema1:name "Beam Diameter" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDiameter> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1 .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "Petrographic microscopy and SEM — \"The petrography of these sections was examined using a petrographic microscope and a scanning electron microscope\" (p.3); the same sections then went to both microprobes" .


```


### detail example Ma2017
detail instance derived from Ma+2017 | JEOL 8200 | WDS Point Analysis (Caltech GPS Analytical Facility).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "ex": "https://example.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/",
    "prov": "http://www.w3.org/ns/prov#"
  },
  "@id": "ex:epmaTAPP-detail-Ma2017",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "EPMA",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/epmaTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 15,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "15 kV"
                },
                {
                  "@id": "ada:parameter/epmaTAPP/beamDiameter",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/beamDiameter"
                    }
                  ],
                  "schema:name": "Beam Diameter",
                  "schema:value": "N — 'beam in focused mode' is recorded under Beam Mode; no diameter is given",
                  "schema:unitText": "no value available: unnamed property"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:epmaTAPP-detail-Ma2017/instrument/EPMA"
            }
          ]
        },
        {
          "bios:reagent": [
            {
              "ada:reagentRole": "referenceMaterial",
              "schema:name": "feldspar standards — 'based on analysis of feldspar standards as unknowns'; not named individually",
              "@type": [
                "schema:DefinedTerm"
              ]
            }
          ]
        },
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "acquisition",
              "schema:name": "Probe for EPMA (Probe Software, Inc.)",
              "@type": [
                "schema:SoftwareApplication"
              ]
            },
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "N — the 'CITZAF correction procedure' is recorded under Matrix Correction Method; the only software named is Probe for EPMA",
              "@type": [
                "schema:SoftwareApplication"
              ]
            }
          ]
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/epmaTAPP/beamDamageMinimization",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/epmaTAPP/beamDamageMinimization"
            }
          ],
          "schema:name": "Beam Damage Minimization",
          "schema:value": "all: low beam current (5 nA) — 'Although a low beam current of 5 nA was used for the analysis, the low cation sum (0.92) for the K-site is likely due to diffusion of Na away from the electron beam' (p.3)"
        }
      ],
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening"
                }
              ],
              "schema:name": "Pre-Analysis Imaging and Screening",
              "schema:value": "SEM BSE imaging on a ZEISS 1550VP field-emission SEM — \"Backscattered electron (BSE) imaging was performed using a Carl Zeiss, LLC 1550VP field emission SEM\" (p.2), locating the three occurrences of the new mineral in the Zagami thin section (Fig. 1, p.2). The paper lists EPMA, SEM, EBSD, synchrotron XRD and micro-Raman as one suite (p.2) without stating the order"
            }
          ],
          "schema:name": "Zagami USNM 7619",
          "schema:identifier": "USNM 7619 — Smithsonian catalogue number: 'The Zagami thin section (USNM 7619)'; no IGSN"
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Division of Geological and Planetary Sciences Analytical Facility, Caltech"
      },
      "schema:description": "Ma et al. 2018, Meteorit. Planet. Sci. 53:50-61 (file dated 2017) — liebermannite (KAlSi3O8) discovery from Zagami. Instrument stated as \"JEOL 8200 electron microprobe\" (no JXA prefix in text). WDS explicitly stated (\"WDS: 15 kV, 5 nA\"). Probe for EPMA; CITZAF correction (Armstrong 1995) — NOT PAP. Full standard suite and X-ray lines stated. K-mapping by EPMA also performed (used for mineral identification) but mapping conditions (step size, dwell time, current) not stated. Na diffusion observed during analysis despite low 5 nA beam current. Detection limits stated (per-element wt% values). Analytical accuracy: 1-2% for Si, Al, Ca, Na, K (feldspar standards as unknowns). Caltech GPS Division Analytical Facility.",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Polished thin section USNM 7619 (coating type N)",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "schema:additionalProperty": [],
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:deadTime": -9999
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "feldspar standards [Si, Al, Ca, Na, K: 1–2%; other: N] — 'The accuracy is 1–2% for Si, Al, Ca, Na, and K, based on analysis of feldspar standards as unknowns' — per element, while Table 1 reports oxides"
    },
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "SiO2, TiO2, Al2O3, FeO, CaO, Na2O, K2O: one standard deviation of the mean; other: N — Table 1 note c, same wording"
    },
    {
      "dqv:isMeasurementOf": "Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "schema:contributor": [
    {
      "schema:roleName": "analyst",
      "schema:contributor": {
        "schema:name": "Chi Ma"
      }
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NNSA Stewardship Science Academic Alliances, DOE Cooperative Agreements DE-NA0001982 and DESC0005278; NASA NNX12AJ01G — 'This work was supported in part by ...'"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM (Carl Zeiss 1550VP FE-SEM, BSE imaging); EBSD; synchrotron XRD; micro-Raman"
      }
    }
  ],
  "ada:analyticalMode": [
    "WDS Point Analysis — 'WDS: 15 kV, 5 nA'; the paper also mentions 'K-mapping by EPMA', with no detector or conditions"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "Chi Ma",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NNSA Stewardship Science Academic Alliances, DOE Cooperative Agreements DE-NA0001982 and DESC0005278; NASA NNX12AJ01G — 'This work was supported in part by ...'",
  "ada:sampleName": "Zagami USNM 7619",
  "ada:samplingUnitName": "Labelled at section level only: \"The Zagami thin section (USNM 7619)\" (p.3); occurrences are identified by figure panel (\"First occurrence of liebermannite\", Fig. 1, p.2), not by label",
  "ada:targetMaterialOfSamplingUnit": "liebermannite (type, second and third occurrences); lingunite (next to type liebermannite); maskelynite (near type and near second liebermannite) — Table 1",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:detectionLimit": "Si: 0.05 wt%; Ti: 0.04 wt%; Al: 0.06 wt%; Fe: 0.06 wt%; Mg: 0.02 wt%; Ca: 0.02 wt%; Na: 0.03 wt%; K: 0.02 wt%; Cr: 0.05 wt%; Mn: 0.06 wt% — 'The detection limits (wt%) are 0.05 Si, 0.04 Ti, ...' (p.2) — stated per element, while Table 1 reports oxides",
  "ada:analyticalPrecision": "missing",
  "ada:edsDeadTime": -9999
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    },
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EPMA/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:epmaTAPP-detail-Ma2017",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "EPMA",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/epmaTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 15,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "15 kV"
                },
                {
                  "@id": "ada:parameter/epmaTAPP/beamDiameter",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/beamDiameter"
                    }
                  ],
                  "schema:name": "Beam Diameter",
                  "schema:value": "N \u2014 'beam in focused mode' is recorded under Beam Mode; no diameter is given",
                  "schema:unitText": "no value available: unnamed property"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:epmaTAPP-detail-Ma2017/instrument/EPMA"
            }
          ]
        },
        {
          "bios:reagent": [
            {
              "ada:reagentRole": "referenceMaterial",
              "schema:name": "feldspar standards \u2014 'based on analysis of feldspar standards as unknowns'; not named individually",
              "@type": [
                "schema:DefinedTerm"
              ]
            }
          ]
        },
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "acquisition",
              "schema:name": "Probe for EPMA (Probe Software, Inc.)",
              "@type": [
                "schema:SoftwareApplication"
              ]
            },
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "N \u2014 the 'CITZAF correction procedure' is recorded under Matrix Correction Method; the only software named is Probe for EPMA",
              "@type": [
                "schema:SoftwareApplication"
              ]
            }
          ]
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/epmaTAPP/beamDamageMinimization",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/epmaTAPP/beamDamageMinimization"
            }
          ],
          "schema:name": "Beam Damage Minimization",
          "schema:value": "all: low beam current (5 nA) \u2014 'Although a low beam current of 5 nA was used for the analysis, the low cation sum (0.92) for the K-site is likely due to diffusion of Na away from the electron beam' (p.3)"
        }
      ],
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening"
                }
              ],
              "schema:name": "Pre-Analysis Imaging and Screening",
              "schema:value": "SEM BSE imaging on a ZEISS 1550VP field-emission SEM \u2014 \"Backscattered electron (BSE) imaging was performed using a Carl Zeiss, LLC 1550VP field emission SEM\" (p.2), locating the three occurrences of the new mineral in the Zagami thin section (Fig. 1, p.2). The paper lists EPMA, SEM, EBSD, synchrotron XRD and micro-Raman as one suite (p.2) without stating the order"
            }
          ],
          "schema:name": "Zagami USNM 7619",
          "schema:identifier": "USNM 7619 \u2014 Smithsonian catalogue number: 'The Zagami thin section (USNM 7619)'; no IGSN"
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Division of Geological and Planetary Sciences Analytical Facility, Caltech"
      },
      "schema:description": "Ma et al. 2018, Meteorit. Planet. Sci. 53:50-61 (file dated 2017) \u2014 liebermannite (KAlSi3O8) discovery from Zagami. Instrument stated as \"JEOL 8200 electron microprobe\" (no JXA prefix in text). WDS explicitly stated (\"WDS: 15 kV, 5 nA\"). Probe for EPMA; CITZAF correction (Armstrong 1995) \u2014 NOT PAP. Full standard suite and X-ray lines stated. K-mapping by EPMA also performed (used for mineral identification) but mapping conditions (step size, dwell time, current) not stated. Na diffusion observed during analysis despite low 5 nA beam current. Detection limits stated (per-element wt% values). Analytical accuracy: 1-2% for Si, Al, Ca, Na, K (feldspar standards as unknowns). Caltech GPS Division Analytical Facility.",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Polished thin section USNM 7619 (coating type N)",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "schema:additionalProperty": [],
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:deadTime": -9999
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "feldspar standards [Si, Al, Ca, Na, K: 1\u20132%; other: N] \u2014 'The accuracy is 1\u20132% for Si, Al, Ca, Na, and K, based on analysis of feldspar standards as unknowns' \u2014 per element, while Table 1 reports oxides"
    },
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "SiO2, TiO2, Al2O3, FeO, CaO, Na2O, K2O: one standard deviation of the mean; other: N \u2014 Table 1 note c, same wording"
    },
    {
      "dqv:isMeasurementOf": "Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "schema:contributor": [
    {
      "schema:roleName": "analyst",
      "schema:contributor": {
        "schema:name": "Chi Ma"
      }
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NNSA Stewardship Science Academic Alliances, DOE Cooperative Agreements DE-NA0001982 and DESC0005278; NASA NNX12AJ01G \u2014 'This work was supported in part by ...'"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM (Carl Zeiss 1550VP FE-SEM, BSE imaging); EBSD; synchrotron XRD; micro-Raman"
      }
    }
  ],
  "ada:analyticalMode": [
    "WDS Point Analysis \u2014 'WDS: 15 kV, 5 nA'; the paper also mentions 'K-mapping by EPMA', with no detector or conditions"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "Chi Ma",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NNSA Stewardship Science Academic Alliances, DOE Cooperative Agreements DE-NA0001982 and DESC0005278; NASA NNX12AJ01G \u2014 'This work was supported in part by ...'",
  "ada:sampleName": "Zagami USNM 7619",
  "ada:samplingUnitName": "Labelled at section level only: \"The Zagami thin section (USNM 7619)\" (p.3); occurrences are identified by figure panel (\"First occurrence of liebermannite\", Fig. 1, p.2), not by label",
  "ada:targetMaterialOfSamplingUnit": "liebermannite (type, second and third occurrences); lingunite (next to type liebermannite); maskelynite (near type and near second liebermannite) \u2014 Table 1",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:detectionLimit": "Si: 0.05 wt%; Ti: 0.04 wt%; Al: 0.06 wt%; Fe: 0.06 wt%; Mg: 0.02 wt%; Ca: 0.02 wt%; Na: 0.03 wt%; K: 0.02 wt%; Cr: 0.05 wt%; Mn: 0.06 wt% \u2014 'The detection limits (wt%) are 0.05 Si, 0.04 Ti, ...' (p.2) \u2014 stated per element, while Table 1 reports oxides",
  "ada:analyticalPrecision": "missing",
  "ada:edsDeadTime": -9999
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix bios: <https://bioschemas.org/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix dqv: <http://www.w3.org/ns/dqv#> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:epmaTAPP-detail-Ma2017 a schema1:Dataset,
        schema1:Product ;
    schema1:contributor [ schema1:contributor [ schema1:name "Chi Ma" ] ;
            schema1:roleName "analyst" ] ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "NNSA Stewardship Science Academic Alliances, DOE Cooperative Agreements DE-NA0001982 and DESC0005278; NASA NNX12AJ01G — 'This work was supported in part by ...'" ] ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "SEM (Carl Zeiss 1550VP FE-SEM, BSE imaging); EBSD; synchrotron XRD; micro-Raman" ] ] ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Analytical Accuracy" ;
            dqv:value "feldspar standards [Si, Al, Ca, Na, K: 1–2%; other: N] — 'The accuracy is 1–2% for Si, Al, Ca, Na, and K, based on analysis of feldspar standards as unknowns' — per element, while Table 1 reports oxides" ],
        [ dqv:isMeasurementOf "Goodness-of-Fit" ;
            dqv:value "SiO2, TiO2, Al2O3, FeO, CaO, Na2O, K2O: one standard deviation of the mean; other: N — Table 1 note c, same wording" ],
        [ dqv:isMeasurementOf "Analytical Precision" ;
            dqv:value "no value available: dqv:value" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Polished thin section USNM 7619 (coating type N)" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDamageMinimization> ;
            schema1:description "Ma et al. 2018, Meteorit. Planet. Sci. 53:50-61 (file dated 2017) — liebermannite (KAlSi3O8) discovery from Zagami. Instrument stated as \"JEOL 8200 electron microprobe\" (no JXA prefix in text). WDS explicitly stated (\"WDS: 15 kV, 5 nA\"). Probe for EPMA; CITZAF correction (Armstrong 1995) — NOT PAP. Full standard suite and X-ray lines stated. K-mapping by EPMA also performed (used for mineral identification) but mapping conditions (step size, dwell time, current) not stated. Na diffusion observed during analysis despite low 5 nA beam current. Detection limits stated (per-element wt% values). Analytical accuracy: 1-2% for Si, Al, Ca, Na, K (feldspar standards as unknowns). Caltech GPS Division Analytical Facility." ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Division of Geological and Planetary Sciences Analytical Facility, Caltech" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
                    schema1:identifier "USNM 7619 — Smithsonian catalogue number: 'The Zagami thin section (USNM 7619)'; no IGSN" ;
                    schema1:name "Zagami USNM 7619" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "feldspar standards — 'based on analysis of feldspar standards as unknowns'; not named individually" ;
                            ada:reagentRole "referenceMaterial" ] ],
                [ schema1:instrument <https://example.org/epmaTAPP-detail-Ma2017/instrument/EPMA> ],
                [ bios:computationalTool [ a schema1:SoftwareApplication ;
                            schema1:name "Probe for EPMA (Probe Software, Inc.)" ;
                            ada:toolRole "acquisition" ],
                        [ a schema1:SoftwareApplication ;
                            schema1:name "N — the 'CITZAF correction procedure' is recorded under Matrix Correction Method; the only software named is Probe for EPMA" ;
                            ada:toolRole "dataReduction" ] ] ;
            ada:combinedResults [ ] ;
            ada:deadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "Chi Ma" ;
    ada:analyticalMode "WDS Point Analysis — 'WDS: 15 kV, 5 nA'; the paper also mentions 'K-mapping by EPMA', with no detector or conditions" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit "Si: 0.05 wt%; Ti: 0.04 wt%; Al: 0.06 wt%; Fe: 0.06 wt%; Mg: 0.02 wt%; Ca: 0.02 wt%; Na: 0.03 wt%; K: 0.02 wt%; Cr: 0.05 wt%; Mn: 0.06 wt% — 'The detection limits (wt%) are 0.05 Si, 0.04 Ti, ...' (p.2) — stated per element, while Table 1 reports oxides" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NNSA Stewardship Science Academic Alliances, DOE Cooperative Agreements DE-NA0001982 and DESC0005278; NASA NNX12AJ01G — 'This work was supported in part by ...'" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:sampleName "Zagami USNM 7619" ;
    ada:samplingUnitName "Labelled at section level only: \"The Zagami thin section (USNM 7619)\" (p.3); occurrences are identified by figure panel (\"First occurrence of liebermannite\", Fig. 1, p.2), not by label" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "liebermannite (type, second and third occurrences); lingunite (next to type liebermannite); maskelynite (near type and near second liebermannite) — Table 1" .

<https://example.org/epmaTAPP-detail-Ma2017/instrument/EPMA> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/epmaTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDiameter> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EPMA" ;
    schema1:name "no value available: schema:name" .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:description "15 kV" ;
    schema1:name "Accelerating Voltage" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/epmaTAPP/acceleratingVoltage> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 15 .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDamageMinimization> a schema1:PropertyValue ;
    schema1:name "Beam Damage Minimization" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDamageMinimization> ;
    schema1:value "all: low beam current (5 nA) — 'Although a low beam current of 5 nA was used for the analysis, the low cation sum (0.92) for the K-site is likely due to diffusion of Na away from the electron beam' (p.3)" .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDiameter> a schema1:PropertyValue ;
    schema1:name "Beam Diameter" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDiameter> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value "N — 'beam in focused mode' is recorded under Beam Mode; no diameter is given" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "SEM BSE imaging on a ZEISS 1550VP field-emission SEM — \"Backscattered electron (BSE) imaging was performed using a Carl Zeiss, LLC 1550VP field emission SEM\" (p.2), locating the three occurrences of the new mineral in the Zagami thin section (Fig. 1, p.2). The paper lists EPMA, SEM, EBSD, synchrotron XRD and micro-Raman as one suite (p.2) without stating the order" .


```


### detail example Frank2023
detail instance derived from Frank+2023 | Cameca SX100 | WDS Point Analysis (ARES JSC).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "ex": "https://example.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/",
    "prov": "http://www.w3.org/ns/prov#"
  },
  "@id": "ex:epmaTAPP-detail-Frank2023",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "EPMA",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/epmaTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 20,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "20 kV"
                },
                {
                  "@id": "ada:parameter/epmaTAPP/beamDiameter",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/beamDiameter"
                    }
                  ],
                  "schema:name": "Beam Diameter",
                  "schema:value": 1,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "all: 1 µm — p.3"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:epmaTAPP-detail-Frank2023/instrument/EPMA"
            }
          ]
        },
        {
          "bios:reagent": [
            {
              "ada:reagentRole": "referenceMaterial",
              "schema:name": "N — no EPMA secondary standard is named; San Carlos olivine standardised the SIMS oxygen-isotope measurements, and Kakanui kaersutite is a primary standard",
              "@type": [
                "schema:DefinedTerm"
              ]
            }
          ]
        }
      ],
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening"
                }
              ],
              "schema:name": "Pre-Analysis Imaging and Screening",
              "schema:value": "Petrographic microscopy and SEM — \"The CAI was characterized by petrographic microscope, scanning electron microscope, electron microprobe, and X-ray mapping before being measured for oxygen isotopes\" (p.3); the object itself had been found during an earlier survey of matrix compositions (p.3)"
            }
          ],
          "schema:name": "Ivuna CI chondrite, section MZ2"
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "ARES, NASA Johnson Space Center"
      },
      "schema:description": "Frank et al. 2023, Meteorit. Planet. Sci. 58:1495-1511 — CAI in Ivuna CI chondrite. ARES NASA JSC. Instrument stated as \"Cameca SX100 electron microprobe at ARES, Johnson Space Center\" — NOT JEOL JXA-8530F as in v2 header. Accelerating voltage 20 kV (not 15 kV). Both point analysis (20 kV, 20 nA, 1 µm focused) and X-ray mapping performed. X-ray mapping described but conditions (step size, dwell time, mapping beam mode) N. WDS not explicitly stated. Matrix correction and background correction method N. Peak counting time 10-50 s. Primary standard suite fully documented. No EPMA secondary standard is named (San Carlos olivine standardised the SIMS work). Detection limits stated per element group.",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:deadTime": -9999
    }
  ],
  "schema:contributor": [
    {
      "schema:roleName": "analyst",
      "schema:contributor": {
        "schema:name": "David R. Frank"
      }
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NASA NNX11AG78G, 13-COS13-0026, NNX14AI19G and 80NSSC18K0586; NASA Cosmochemistry and Emerging Worlds Programs — 'This work was supported by ...'"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Petrographic microscopy; SEM-BSE (JEOL 5900LV); EPMA X-ray mapping; Cameca ims1280 ion microprobe (O isotopes; 26Al-26Mg); FIB-TEM"
      }
    },
    {
      "schema:linkRelationship": "coupledDataset",
      "schema:target": "same submission — 'All data are included within the manuscript'"
    }
  ],
  "ada:analyticalMode": [
    "N — point analyses and X-ray mapping ('electron microprobe, and X-ray mapping'); WDS or EDS is not stated, and the list has no value without one"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "David R. Frank",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA NNX11AG78G, 13-COS13-0026, NNX14AI19G and 80NSSC18K0586; NASA Cosmochemistry and Emerging Worlds Programs — 'This work was supported by ...'",
  "ada:sampleName": "Ivuna CI chondrite, section MZ2",
  "ada:samplingUnitName": "Labelled at section level: the CAI \"in Ivuna section MZ2\" (p.3), in \"polished mount 'Ivuna MZ2'\" (p.14); the single CAI and its analysis points carry no labels",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:detectionLimit": "Al2O3, K2O, CaO: 0.03–0.04 wt%; Na2O, MgO, SiO2, FeO, MnO: 0.05 wt%; P2O5, SO2, TiO2, V2O3, Cr2O3, NiO: 0.06–0.09 wt% — 'typically' (p.4)",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    },
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EPMA/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:epmaTAPP-detail-Frank2023",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "EPMA",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/epmaTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 20,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "20 kV"
                },
                {
                  "@id": "ada:parameter/epmaTAPP/beamDiameter",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/beamDiameter"
                    }
                  ],
                  "schema:name": "Beam Diameter",
                  "schema:value": 1,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "all: 1 \u00b5m \u2014 p.3"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:epmaTAPP-detail-Frank2023/instrument/EPMA"
            }
          ]
        },
        {
          "bios:reagent": [
            {
              "ada:reagentRole": "referenceMaterial",
              "schema:name": "N \u2014 no EPMA secondary standard is named; San Carlos olivine standardised the SIMS oxygen-isotope measurements, and Kakanui kaersutite is a primary standard",
              "@type": [
                "schema:DefinedTerm"
              ]
            }
          ]
        }
      ],
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening"
                }
              ],
              "schema:name": "Pre-Analysis Imaging and Screening",
              "schema:value": "Petrographic microscopy and SEM \u2014 \"The CAI was characterized by petrographic microscope, scanning electron microscope, electron microprobe, and X-ray mapping before being measured for oxygen isotopes\" (p.3); the object itself had been found during an earlier survey of matrix compositions (p.3)"
            }
          ],
          "schema:name": "Ivuna CI chondrite, section MZ2"
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "ARES, NASA Johnson Space Center"
      },
      "schema:description": "Frank et al. 2023, Meteorit. Planet. Sci. 58:1495-1511 \u2014 CAI in Ivuna CI chondrite. ARES NASA JSC. Instrument stated as \"Cameca SX100 electron microprobe at ARES, Johnson Space Center\" \u2014 NOT JEOL JXA-8530F as in v2 header. Accelerating voltage 20 kV (not 15 kV). Both point analysis (20 kV, 20 nA, 1 \u00b5m focused) and X-ray mapping performed. X-ray mapping described but conditions (step size, dwell time, mapping beam mode) N. WDS not explicitly stated. Matrix correction and background correction method N. Peak counting time 10-50 s. Primary standard suite fully documented. No EPMA secondary standard is named (San Carlos olivine standardised the SIMS work). Detection limits stated per element group.",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:deadTime": -9999
    }
  ],
  "schema:contributor": [
    {
      "schema:roleName": "analyst",
      "schema:contributor": {
        "schema:name": "David R. Frank"
      }
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NASA NNX11AG78G, 13-COS13-0026, NNX14AI19G and 80NSSC18K0586; NASA Cosmochemistry and Emerging Worlds Programs \u2014 'This work was supported by ...'"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Petrographic microscopy; SEM-BSE (JEOL 5900LV); EPMA X-ray mapping; Cameca ims1280 ion microprobe (O isotopes; 26Al-26Mg); FIB-TEM"
      }
    },
    {
      "schema:linkRelationship": "coupledDataset",
      "schema:target": "same submission \u2014 'All data are included within the manuscript'"
    }
  ],
  "ada:analyticalMode": [
    "N \u2014 point analyses and X-ray mapping ('electron microprobe, and X-ray mapping'); WDS or EDS is not stated, and the list has no value without one"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "David R. Frank",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA NNX11AG78G, 13-COS13-0026, NNX14AI19G and 80NSSC18K0586; NASA Cosmochemistry and Emerging Worlds Programs \u2014 'This work was supported by ...'",
  "ada:sampleName": "Ivuna CI chondrite, section MZ2",
  "ada:samplingUnitName": "Labelled at section level: the CAI \"in Ivuna section MZ2\" (p.3), in \"polished mount 'Ivuna MZ2'\" (p.14); the single CAI and its analysis points carry no labels",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:detectionLimit": "Al2O3, K2O, CaO: 0.03\u20130.04 wt%; Na2O, MgO, SiO2, FeO, MnO: 0.05 wt%; P2O5, SO2, TiO2, V2O3, Cr2O3, NiO: 0.06\u20130.09 wt% \u2014 'typically' (p.4)",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix bios: <https://bioschemas.org/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:epmaTAPP-detail-Frank2023 a schema1:Dataset,
        schema1:Product ;
    schema1:contributor [ schema1:contributor [ schema1:name "David R. Frank" ] ;
            schema1:roleName "analyst" ] ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "NASA NNX11AG78G, 13-COS13-0026, NNX14AI19G and 80NSSC18K0586; NASA Cosmochemistry and Emerging Worlds Programs — 'This work was supported by ...'" ] ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "Petrographic microscopy; SEM-BSE (JEOL 5900LV); EPMA X-ray mapping; Cameca ims1280 ion microprobe (O isotopes; 26Al-26Mg); FIB-TEM" ] ],
        [ schema1:linkRelationship "coupledDataset" ;
            schema1:target "same submission — 'All data are included within the manuscript'" ] ;
    prov:wasGeneratedBy [ schema1:description "Frank et al. 2023, Meteorit. Planet. Sci. 58:1495-1511 — CAI in Ivuna CI chondrite. ARES NASA JSC. Instrument stated as \"Cameca SX100 electron microprobe at ARES, Johnson Space Center\" — NOT JEOL JXA-8530F as in v2 header. Accelerating voltage 20 kV (not 15 kV). Both point analysis (20 kV, 20 nA, 1 µm focused) and X-ray mapping performed. X-ray mapping described but conditions (step size, dwell time, mapping beam mode) N. WDS not explicitly stated. Matrix correction and background correction method N. Peak counting time 10-50 s. Primary standard suite fully documented. No EPMA secondary standard is named (San Carlos olivine standardised the SIMS work). Detection limits stated per element group." ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "ARES, NASA Johnson Space Center" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
                    schema1:name "Ivuna CI chondrite, section MZ2" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ schema1:instrument <https://example.org/epmaTAPP-detail-Frank2023/instrument/EPMA> ],
                [ bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "N — no EPMA secondary standard is named; San Carlos olivine standardised the SIMS oxygen-isotope measurements, and Kakanui kaersutite is a primary standard" ;
                            ada:reagentRole "referenceMaterial" ] ] ;
            ada:combinedResults [ ] ;
            ada:deadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "David R. Frank" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "N — point analyses and X-ray mapping ('electron microprobe, and X-ray mapping'); WDS or EDS is not stated, and the list has no value without one" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit "Al2O3, K2O, CaO: 0.03–0.04 wt%; Na2O, MgO, SiO2, FeO, MnO: 0.05 wt%; P2O5, SO2, TiO2, V2O3, Cr2O3, NiO: 0.06–0.09 wt% — 'typically' (p.4)" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NASA NNX11AG78G, 13-COS13-0026, NNX14AI19G and 80NSSC18K0586; NASA Cosmochemistry and Emerging Worlds Programs — 'This work was supported by ...'" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:sampleName "Ivuna CI chondrite, section MZ2" ;
    ada:samplingUnitName "Labelled at section level: the CAI \"in Ivuna section MZ2\" (p.3), in \"polished mount 'Ivuna MZ2'\" (p.14); the single CAI and its analysis points carry no labels" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" .

<https://example.org/epmaTAPP-detail-Frank2023/instrument/EPMA> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/epmaTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDiameter> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EPMA" ;
    schema1:name "no value available: schema:name" .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:description "20 kV" ;
    schema1:name "Accelerating Voltage" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/epmaTAPP/acceleratingVoltage> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 20 .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDiameter> a schema1:PropertyValue ;
    schema1:description "all: 1 µm — p.3" ;
    schema1:name "Beam Diameter" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDiameter> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1 .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "Petrographic microscopy and SEM — \"The CAI was characterized by petrographic microscope, scanning electron microscope, electron microprobe, and X-ray mapping before being measured for oxygen isotopes\" (p.3); the object itself had been found during an earlier survey of matrix compositions (p.3)" .


```


### detail example Broussard2026
detail instance derived from Broussard+2026 | JEOL JXA-8200 | WDS Mapping (WashU).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "ex": "https://example.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/",
    "prov": "http://www.w3.org/ns/prov#"
  },
  "@id": "ex:epmaTAPP-detail-Broussard2026",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "EPMA",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/epmaTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 15,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "15 kV"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:epmaTAPP-detail-Broussard2026/instrument/EPMA"
            }
          ]
        },
        {
          "bios:reagent": [
            {
              "ada:reagentRole": "referenceMaterial",
              "schema:name": "Smithsonian Microbeam standards (specific materials and values N)",
              "@type": [
                "schema:DefinedTerm"
              ]
            }
          ]
        },
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "acquisition",
              "schema:name": "Probe for EPMA microanalysis software",
              "@type": [
                "schema:SoftwareApplication"
              ]
            },
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "Probe for EPMA (CITZAF matrix correction, Armstrong 1995); CalcImage and Quantitative Microanalysis Explorer web-based tool (for stage mapping)",
              "@type": [
                "schema:SoftwareApplication"
              ]
            }
          ]
        }
      ],
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening"
                }
              ],
              "schema:name": "Pre-Analysis Imaging and Screening",
              "schema:value": "Optical microscopy of the same thin section — \"Eleven OC002 LAB24-2 fragments were mounted and dry-polished in a petrographic thin section used for optical microscopy and electron probe microanalyses\" (p.3)"
            }
          ],
          "schema:name": "OC002 LAB24-2 (10-11 fragments of Oued Chebeika 002)"
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Washington University in St. Louis"
      },
      "schema:description": "Broussard et al. 2026, Meteorit. Planet. Sci. — OC002 CI chondrite links Bennu and Ryugu. Washington University in St. Louis. Instrument stated as \"JEOL JXA-8200 electron microprobe\" — NOT JXA-8230 as in v2 header. WDS explicitly stated (\"wavelength-dispersive quantitative compositional mapping and analysis\"). CITZAF matrix correction (Armstrong 1995) — NOT PAP or XPP. MAN background for most analytes; polynomial fit for F via LDE1 crystal. Both point analysis (15 kV, 25 nA) and quantitative stage mapping performed. O by stoichiometry from cations. F is the only explicitly named analyte in methods; full list N. An EDS spectrometer is on the instrument; its use is not stated. Smithsonian Microbeam standards as secondary QC. No peak counting time, beam diameter, detection limits, or interference corrections stated.",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Fragments mounted and dry-polished in a petrographic thin section; carbon coating N",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "schema:additionalProperty": [],
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:deadTime": -9999
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NASA 80NSSC22K1689; NASA 80NSSC24K1284; McDonnell Center for the Space Sciences — 'Individual funding was provided by ...'"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Powder XRD (Rigaku MiniFlex 600); ICP-MS (Thermo Fisher iCAP Qc, WashU); K isotope MC-ICP-MS (Neptune Plus, WashU); CO2 laser-fluorination O isotope MS (U. New Mexico); AMS (PRIME Lab, Purdue)"
      }
    },
    {
      "schema:linkRelationship": "coupledDataset",
      "schema:target": "N — 'The data that support the findings of this study are available from the corresponding author upon reasonable request'"
    }
  ],
  "ada:analyticalMode": [
    "WDS Point Analysis; WDS Mapping — 'wavelength-dispersive quantitative compositional mapping and analysis'"
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "N — the carbonate means are given as '±' values ('2.0 ± 0.4 wt% Fe') without naming the statistic"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA 80NSSC22K1689; NASA 80NSSC24K1284; McDonnell Center for the Space Sciences — 'Individual funding was provided by ...'",
  "ada:sampleName": "OC002 LAB24-2 (10-11 fragments of Oued Chebeika 002)",
  "ada:samplingUnitName": "Labelled: \"OC002 LAB24-2 fragment 1\" and \"fragment 2\" (Figs 3–4, pp.6–7), and within fragment 1 \"lithic clast LC1\" (Figure S3 caption, p.17); map areas are otherwise unlabelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    },
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EPMA/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:epmaTAPP-detail-Broussard2026",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "EPMA",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/epmaTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 15,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "15 kV"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:epmaTAPP-detail-Broussard2026/instrument/EPMA"
            }
          ]
        },
        {
          "bios:reagent": [
            {
              "ada:reagentRole": "referenceMaterial",
              "schema:name": "Smithsonian Microbeam standards (specific materials and values N)",
              "@type": [
                "schema:DefinedTerm"
              ]
            }
          ]
        },
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "acquisition",
              "schema:name": "Probe for EPMA microanalysis software",
              "@type": [
                "schema:SoftwareApplication"
              ]
            },
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "Probe for EPMA (CITZAF matrix correction, Armstrong 1995); CalcImage and Quantitative Microanalysis Explorer web-based tool (for stage mapping)",
              "@type": [
                "schema:SoftwareApplication"
              ]
            }
          ]
        }
      ],
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening"
                }
              ],
              "schema:name": "Pre-Analysis Imaging and Screening",
              "schema:value": "Optical microscopy of the same thin section \u2014 \"Eleven OC002 LAB24-2 fragments were mounted and dry-polished in a petrographic thin section used for optical microscopy and electron probe microanalyses\" (p.3)"
            }
          ],
          "schema:name": "OC002 LAB24-2 (10-11 fragments of Oued Chebeika 002)"
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Washington University in St. Louis"
      },
      "schema:description": "Broussard et al. 2026, Meteorit. Planet. Sci. \u2014 OC002 CI chondrite links Bennu and Ryugu. Washington University in St. Louis. Instrument stated as \"JEOL JXA-8200 electron microprobe\" \u2014 NOT JXA-8230 as in v2 header. WDS explicitly stated (\"wavelength-dispersive quantitative compositional mapping and analysis\"). CITZAF matrix correction (Armstrong 1995) \u2014 NOT PAP or XPP. MAN background for most analytes; polynomial fit for F via LDE1 crystal. Both point analysis (15 kV, 25 nA) and quantitative stage mapping performed. O by stoichiometry from cations. F is the only explicitly named analyte in methods; full list N. An EDS spectrometer is on the instrument; its use is not stated. Smithsonian Microbeam standards as secondary QC. No peak counting time, beam diameter, detection limits, or interference corrections stated.",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Fragments mounted and dry-polished in a petrographic thin section; carbon coating N",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "schema:additionalProperty": [],
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:deadTime": -9999
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NASA 80NSSC22K1689; NASA 80NSSC24K1284; McDonnell Center for the Space Sciences \u2014 'Individual funding was provided by ...'"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Powder XRD (Rigaku MiniFlex 600); ICP-MS (Thermo Fisher iCAP Qc, WashU); K isotope MC-ICP-MS (Neptune Plus, WashU); CO2 laser-fluorination O isotope MS (U. New Mexico); AMS (PRIME Lab, Purdue)"
      }
    },
    {
      "schema:linkRelationship": "coupledDataset",
      "schema:target": "N \u2014 'The data that support the findings of this study are available from the corresponding author upon reasonable request'"
    }
  ],
  "ada:analyticalMode": [
    "WDS Point Analysis; WDS Mapping \u2014 'wavelength-dispersive quantitative compositional mapping and analysis'"
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "N \u2014 the carbonate means are given as '\u00b1' values ('2.0 \u00b1 0.4 wt% Fe') without naming the statistic"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA 80NSSC22K1689; NASA 80NSSC24K1284; McDonnell Center for the Space Sciences \u2014 'Individual funding was provided by ...'",
  "ada:sampleName": "OC002 LAB24-2 (10-11 fragments of Oued Chebeika 002)",
  "ada:samplingUnitName": "Labelled: \"OC002 LAB24-2 fragment 1\" and \"fragment 2\" (Figs 3\u20134, pp.6\u20137), and within fragment 1 \"lithic clast LC1\" (Figure S3 caption, p.17); map areas are otherwise unlabelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix bios: <https://bioschemas.org/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix dqv: <http://www.w3.org/ns/dqv#> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:epmaTAPP-detail-Broussard2026 a schema1:Dataset,
        schema1:Product ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "NASA 80NSSC22K1689; NASA 80NSSC24K1284; McDonnell Center for the Space Sciences — 'Individual funding was provided by ...'" ] ;
    schema1:relatedLink [ schema1:linkRelationship "coupledDataset" ;
            schema1:target "N — 'The data that support the findings of this study are available from the corresponding author upon reasonable request'" ],
        [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "Powder XRD (Rigaku MiniFlex 600); ICP-MS (Thermo Fisher iCAP Qc, WashU); K isotope MC-ICP-MS (Neptune Plus, WashU); CO2 laser-fluorination O isotope MS (U. New Mexico); AMS (PRIME Lab, Purdue)" ] ] ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Goodness-of-Fit" ;
            dqv:value "N — the carbonate means are given as '±' values ('2.0 ± 0.4 wt% Fe') without naming the statistic" ],
        [ dqv:isMeasurementOf "Analytical Precision" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Analytical Accuracy" ;
            dqv:value "no value available: dqv:value" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Fragments mounted and dry-polished in a petrographic thin section; carbon coating N" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ] ] ;
            schema1:description "Broussard et al. 2026, Meteorit. Planet. Sci. — OC002 CI chondrite links Bennu and Ryugu. Washington University in St. Louis. Instrument stated as \"JEOL JXA-8200 electron microprobe\" — NOT JXA-8230 as in v2 header. WDS explicitly stated (\"wavelength-dispersive quantitative compositional mapping and analysis\"). CITZAF matrix correction (Armstrong 1995) — NOT PAP or XPP. MAN background for most analytes; polynomial fit for F via LDE1 crystal. Both point analysis (15 kV, 25 nA) and quantitative stage mapping performed. O by stoichiometry from cations. F is the only explicitly named analyte in methods; full list N. An EDS spectrometer is on the instrument; its use is not stated. Smithsonian Microbeam standards as secondary QC. No peak counting time, beam diameter, detection limits, or interference corrections stated." ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Washington University in St. Louis" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
                    schema1:name "OC002 LAB24-2 (10-11 fragments of Oued Chebeika 002)" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "Smithsonian Microbeam standards (specific materials and values N)" ;
                            ada:reagentRole "referenceMaterial" ] ],
                [ schema1:instrument <https://example.org/epmaTAPP-detail-Broussard2026/instrument/EPMA> ],
                [ bios:computationalTool [ a schema1:SoftwareApplication ;
                            schema1:name "Probe for EPMA (CITZAF matrix correction, Armstrong 1995); CalcImage and Quantitative Microanalysis Explorer web-based tool (for stage mapping)" ;
                            ada:toolRole "dataReduction" ],
                        [ a schema1:SoftwareApplication ;
                            schema1:name "Probe for EPMA microanalysis software" ;
                            ada:toolRole "acquisition" ] ] ;
            ada:combinedResults [ ] ;
            ada:deadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "WDS Point Analysis; WDS Mapping — 'wavelength-dispersive quantitative compositional mapping and analysis'" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NASA 80NSSC22K1689; NASA 80NSSC24K1284; McDonnell Center for the Space Sciences — 'Individual funding was provided by ...'" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:sampleName "OC002 LAB24-2 (10-11 fragments of Oued Chebeika 002)" ;
    ada:samplingUnitName "Labelled: \"OC002 LAB24-2 fragment 1\" and \"fragment 2\" (Figs 3–4, pp.6–7), and within fragment 1 \"lithic clast LC1\" (Figure S3 caption, p.17); map areas are otherwise unlabelled" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" .

<https://example.org/epmaTAPP-detail-Broussard2026/instrument/EPMA> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/epmaTAPP/acceleratingVoltage> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EPMA" ;
    schema1:name "no value available: schema:name" .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:description "15 kV" ;
    schema1:name "Accelerating Voltage" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/epmaTAPP/acceleratingVoltage> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 15 .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "Optical microscopy of the same thin section — \"Eleven OC002 LAB24-2 fragments were mounted and dry-polished in a petrographic thin section used for optical microscopy and electron probe microanalyses\" (p.3)" .


```


### detail example Seifert2026
detail instance derived from Seifert+2026 | JEOL 8530 | WDS Point Analysis (ARES JSC).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "ex": "https://example.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/",
    "prov": "http://www.w3.org/ns/prov#"
  },
  "@id": "ex:epmaTAPP-detail-Seifert2026",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "EPMA",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/epmaTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 15,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "15 kV"
                },
                {
                  "@id": "ada:parameter/epmaTAPP/beamDiameter",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/beamDiameter"
                    }
                  ],
                  "schema:name": "Beam Diameter",
                  "schema:value": 2,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "all: 2 µm — as above"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:epmaTAPP-detail-Seifert2026/instrument/EPMA"
            }
          ]
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/epmaTAPP/beamDamageMinimization",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/epmaTAPP/beamDamageMinimization"
            }
          ],
          "schema:name": "Beam Damage Minimization",
          "schema:value": "all: Durango apatite compared at 10 μm and 3 μm spot sizes, with no significant volatile loss — 'in order to assess volatilization of halogens using our beam conditions'"
        },
        {
          "@id": "ada:parameter/epmaTAPP/halogenCorrectionOnOxygen",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/epmaTAPP/halogenCorrectionOnOxygen"
            }
          ],
          "schema:name": "Halogen Correction on Oxygen",
          "schema:value": "N — OH is 'calculated by difference based on 1–F–Cl=OH' (under Target Species Estimation Method); no oxygen-equivalent correction for F and Cl is stated"
        }
      ],
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening"
                }
              ],
              "schema:name": "Pre-Analysis Imaging and Screening",
              "schema:value": "SEM EDS mapping, then CL imaging, on the JEOL 7900F at JSC — \"Apatite grains in OREX-803079-0 and OREX-803080-0 were identified via EDS mapping and point analysis\", after which \"CL images were obtained for each apatite grain to search for zoning or internal structures not resolvable in EDS maps\", collected \"at 5 kV with beam currents ranging from 1 to 1.5 nA\" (p.2); the numbered grains (Ap. #1 …) tie the probe analyses back to those images"
            }
          ],
          "schema:name": "OREX-803079-0 and OREX-803080-0 (Bennu OSIRIS-REx samples)",
          "schema:identifier": "OREX-803079-0; OREX-803080-0 — NASA curation numbers of the mounts, not IGSN"
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "ARES, NASA Johnson Space Center"
      },
      "schema:description": "Seifert et al. 2026, Meteorit. Planet. Sci. — apatite in Bennu OSIRIS-REx samples. ARES NASA JSC. Instrument stated as \"JEOL 8530 EMPA at NASA JSC\" (no \"JXA\", no \"F\", no \"+\" suffix stated in paper). Analytical conditions: 15 kV, 20 nA, 2 µm probe size. Previous v2 values of 10/40-100 nA and 10 µm beam were WRONG — those were Durango apatite test conditions used to assess beam damage, not the actual protocol. Analytes: P, F, Cl, Ca, Mn, Fe, Na, Mg, Si, S. Apatite stoichiometry by Ketcham (2015) method (13-anion basis; OH by difference). Primary standards: SrF2, albite, olivine, quartz, apatite, barite, tugtupite, rhodonite, ilmenite. Sample preparation: fragments embedded in epoxy, dry-polished, ion-polished (one mount), carbon coated. 14 total analyses performed.",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Fragments embedded in epoxy; dry-polished with diamond powder; one mount ion-polished before carbon coating",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "schema:additionalProperty": [],
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:deadTime": -9999
    }
  ],
  "schema:contributor": [
    {
      "schema:roleName": "analyst",
      "schema:contributor": {
        "schema:name": "Logan B. Seifert"
      }
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NASA NNH09ZDA007O under contract NNM10AA11C (New Frontiers Program); NASA Postdoctoral Program — acknowledgements"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM-EDS; SIMS (Cameca ims 1280); TEM-EDS"
      }
    },
    {
      "schema:linkRelationship": "coupledDataset",
      "schema:target": "astromat.org, at the DOIs in Table S1 — 'Instrument data products that support the findings of this study will be available via astromat.org at the DOIs given in Table S1'"
    }
  ],
  "ada:analyticalMode": [
    "N — 14 quantitative point analyses; WDS or EDS is not stated, and the list has no value without one"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "Logan B. Seifert",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA NNH09ZDA007O under contract NNM10AA11C (New Frontiers Program); NASA Postdoctoral Program — acknowledgements",
  "ada:sampleName": "OREX-803079-0 and OREX-803080-0 (Bennu OSIRIS-REx samples)",
  "ada:samplingUnitName": "Labelled: apatite grains numbered within each particle — \"OREX-803166-0 … Ap. #1 Ap. #2 Ap. #3 Ap. #4\" (Table 1, p.7) — in particles \"OREX-803166-0, OREX-803169-0, and OREX-803173-0\" (p.3) from the mounts \"OREX-803079-0 and OREX-803080-0\" (p.2)",
  "ada:targetMaterialOfSamplingUnit": "Phosphate (apatite) for every grain, Ap. #1 onward — Table 1",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    },
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EPMA/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:epmaTAPP-detail-Seifert2026",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "EPMA",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/epmaTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 15,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "15 kV"
                },
                {
                  "@id": "ada:parameter/epmaTAPP/beamDiameter",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/beamDiameter"
                    }
                  ],
                  "schema:name": "Beam Diameter",
                  "schema:value": 2,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "all: 2 \u00b5m \u2014 as above"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:epmaTAPP-detail-Seifert2026/instrument/EPMA"
            }
          ]
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/epmaTAPP/beamDamageMinimization",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/epmaTAPP/beamDamageMinimization"
            }
          ],
          "schema:name": "Beam Damage Minimization",
          "schema:value": "all: Durango apatite compared at 10 \u03bcm and 3 \u03bcm spot sizes, with no significant volatile loss \u2014 'in order to assess volatilization of halogens using our beam conditions'"
        },
        {
          "@id": "ada:parameter/epmaTAPP/halogenCorrectionOnOxygen",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/epmaTAPP/halogenCorrectionOnOxygen"
            }
          ],
          "schema:name": "Halogen Correction on Oxygen",
          "schema:value": "N \u2014 OH is 'calculated by difference based on 1\u2013F\u2013Cl=OH' (under Target Species Estimation Method); no oxygen-equivalent correction for F and Cl is stated"
        }
      ],
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening"
                }
              ],
              "schema:name": "Pre-Analysis Imaging and Screening",
              "schema:value": "SEM EDS mapping, then CL imaging, on the JEOL 7900F at JSC \u2014 \"Apatite grains in OREX-803079-0 and OREX-803080-0 were identified via EDS mapping and point analysis\", after which \"CL images were obtained for each apatite grain to search for zoning or internal structures not resolvable in EDS maps\", collected \"at 5 kV with beam currents ranging from 1 to 1.5 nA\" (p.2); the numbered grains (Ap. #1 \u2026) tie the probe analyses back to those images"
            }
          ],
          "schema:name": "OREX-803079-0 and OREX-803080-0 (Bennu OSIRIS-REx samples)",
          "schema:identifier": "OREX-803079-0; OREX-803080-0 \u2014 NASA curation numbers of the mounts, not IGSN"
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "ARES, NASA Johnson Space Center"
      },
      "schema:description": "Seifert et al. 2026, Meteorit. Planet. Sci. \u2014 apatite in Bennu OSIRIS-REx samples. ARES NASA JSC. Instrument stated as \"JEOL 8530 EMPA at NASA JSC\" (no \"JXA\", no \"F\", no \"+\" suffix stated in paper). Analytical conditions: 15 kV, 20 nA, 2 \u00b5m probe size. Previous v2 values of 10/40-100 nA and 10 \u00b5m beam were WRONG \u2014 those were Durango apatite test conditions used to assess beam damage, not the actual protocol. Analytes: P, F, Cl, Ca, Mn, Fe, Na, Mg, Si, S. Apatite stoichiometry by Ketcham (2015) method (13-anion basis; OH by difference). Primary standards: SrF2, albite, olivine, quartz, apatite, barite, tugtupite, rhodonite, ilmenite. Sample preparation: fragments embedded in epoxy, dry-polished, ion-polished (one mount), carbon coated. 14 total analyses performed.",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Fragments embedded in epoxy; dry-polished with diamond powder; one mount ion-polished before carbon coating",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "schema:additionalProperty": [],
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:deadTime": -9999
    }
  ],
  "schema:contributor": [
    {
      "schema:roleName": "analyst",
      "schema:contributor": {
        "schema:name": "Logan B. Seifert"
      }
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NASA NNH09ZDA007O under contract NNM10AA11C (New Frontiers Program); NASA Postdoctoral Program \u2014 acknowledgements"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM-EDS; SIMS (Cameca ims 1280); TEM-EDS"
      }
    },
    {
      "schema:linkRelationship": "coupledDataset",
      "schema:target": "astromat.org, at the DOIs in Table S1 \u2014 'Instrument data products that support the findings of this study will be available via astromat.org at the DOIs given in Table S1'"
    }
  ],
  "ada:analyticalMode": [
    "N \u2014 14 quantitative point analyses; WDS or EDS is not stated, and the list has no value without one"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "Logan B. Seifert",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA NNH09ZDA007O under contract NNM10AA11C (New Frontiers Program); NASA Postdoctoral Program \u2014 acknowledgements",
  "ada:sampleName": "OREX-803079-0 and OREX-803080-0 (Bennu OSIRIS-REx samples)",
  "ada:samplingUnitName": "Labelled: apatite grains numbered within each particle \u2014 \"OREX-803166-0 \u2026 Ap. #1 Ap. #2 Ap. #3 Ap. #4\" (Table 1, p.7) \u2014 in particles \"OREX-803166-0, OREX-803169-0, and OREX-803173-0\" (p.3) from the mounts \"OREX-803079-0 and OREX-803080-0\" (p.2)",
  "ada:targetMaterialOfSamplingUnit": "Phosphate (apatite) for every grain, Ap. #1 onward \u2014 Table 1",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:epmaTAPP-detail-Seifert2026 a schema1:Dataset,
        schema1:Product ;
    schema1:contributor [ schema1:contributor [ schema1:name "Logan B. Seifert" ] ;
            schema1:roleName "analyst" ] ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "NASA NNH09ZDA007O under contract NNM10AA11C (New Frontiers Program); NASA Postdoctoral Program — acknowledgements" ] ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "SEM-EDS; SIMS (Cameca ims 1280); TEM-EDS" ] ],
        [ schema1:linkRelationship "coupledDataset" ;
            schema1:target "astromat.org, at the DOIs in Table S1 — 'Instrument data products that support the findings of this study will be available via astromat.org at the DOIs given in Table S1'" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Fragments embedded in epoxy; dry-polished with diamond powder; one mount ion-polished before carbon coating" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDamageMinimization>,
                <https://ada.astromat.org/metadata/parameter/epmaTAPP/halogenCorrectionOnOxygen> ;
            schema1:description "Seifert et al. 2026, Meteorit. Planet. Sci. — apatite in Bennu OSIRIS-REx samples. ARES NASA JSC. Instrument stated as \"JEOL 8530 EMPA at NASA JSC\" (no \"JXA\", no \"F\", no \"+\" suffix stated in paper). Analytical conditions: 15 kV, 20 nA, 2 µm probe size. Previous v2 values of 10/40-100 nA and 10 µm beam were WRONG — those were Durango apatite test conditions used to assess beam damage, not the actual protocol. Analytes: P, F, Cl, Ca, Mn, Fe, Na, Mg, Si, S. Apatite stoichiometry by Ketcham (2015) method (13-anion basis; OH by difference). Primary standards: SrF2, albite, olivine, quartz, apatite, barite, tugtupite, rhodonite, ilmenite. Sample preparation: fragments embedded in epoxy, dry-polished, ion-polished (one mount), carbon coated. 14 total analyses performed." ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "ARES, NASA Johnson Space Center" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
                    schema1:identifier "OREX-803079-0; OREX-803080-0 — NASA curation numbers of the mounts, not IGSN" ;
                    schema1:name "OREX-803079-0 and OREX-803080-0 (Bennu OSIRIS-REx samples)" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ schema1:instrument <https://example.org/epmaTAPP-detail-Seifert2026/instrument/EPMA> ] ;
            ada:combinedResults [ ] ;
            ada:deadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "Logan B. Seifert" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "N — 14 quantitative point analyses; WDS or EDS is not stated, and the list has no value without one" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NASA NNH09ZDA007O under contract NNM10AA11C (New Frontiers Program); NASA Postdoctoral Program — acknowledgements" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:sampleName "OREX-803079-0 and OREX-803080-0 (Bennu OSIRIS-REx samples)" ;
    ada:samplingUnitName "Labelled: apatite grains numbered within each particle — \"OREX-803166-0 … Ap. #1 Ap. #2 Ap. #3 Ap. #4\" (Table 1, p.7) — in particles \"OREX-803166-0, OREX-803169-0, and OREX-803173-0\" (p.3) from the mounts \"OREX-803079-0 and OREX-803080-0\" (p.2)" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "Phosphate (apatite) for every grain, Ap. #1 onward — Table 1" .

<https://example.org/epmaTAPP-detail-Seifert2026/instrument/EPMA> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/epmaTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDiameter> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EPMA" ;
    schema1:name "no value available: schema:name" .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:description "15 kV" ;
    schema1:name "Accelerating Voltage" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/epmaTAPP/acceleratingVoltage> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 15 .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDamageMinimization> a schema1:PropertyValue ;
    schema1:name "Beam Damage Minimization" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDamageMinimization> ;
    schema1:value "all: Durango apatite compared at 10 μm and 3 μm spot sizes, with no significant volatile loss — 'in order to assess volatilization of halogens using our beam conditions'" .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDiameter> a schema1:PropertyValue ;
    schema1:description "all: 2 µm — as above" ;
    schema1:name "Beam Diameter" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDiameter> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 2 .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/halogenCorrectionOnOxygen> a schema1:PropertyValue ;
    schema1:name "Halogen Correction on Oxygen" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/epmaTAPP/halogenCorrectionOnOxygen> ;
    schema1:value "N — OH is 'calculated by difference based on 1–F–Cl=OH' (under Target Species Estimation Method); no oxygen-equivalent correction for F and Cl is stated" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "SEM EDS mapping, then CL imaging, on the JEOL 7900F at JSC — \"Apatite grains in OREX-803079-0 and OREX-803080-0 were identified via EDS mapping and point analysis\", after which \"CL images were obtained for each apatite grain to search for zoning or internal structures not resolvable in EDS maps\", collected \"at 5 kV with beam currents ranging from 1 to 1.5 nA\" (p.2); the numbered grains (Ap. #1 …) tie the probe analyses back to those images" .


```


### detail example Pang2016
detail instance derived from Pang+2016 | JEOL JXA-8100 | WDS Point Analysis (Nanjing U.).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "ex": "https://example.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/",
    "prov": "http://www.w3.org/ns/prov#"
  },
  "@id": "ex:epmaTAPP-detail-Pang2016",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "EPMA",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/epmaTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 15,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "15 kV"
                },
                {
                  "@id": "ada:parameter/epmaTAPP/beamDiameter",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/beamDiameter"
                    }
                  ],
                  "schema:name": "Beam Diameter",
                  "schema:value": 2,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "plagioclase and its polymorphs: 2–5 µm; other: N — 'a defocused beam (2–5 μm in diameter)'"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:epmaTAPP-detail-Pang2016/instrument/EPMA"
            }
          ]
        }
      ],
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening"
                }
              ],
              "schema:name": "Pre-Analysis Imaging and Screening",
              "schema:value": "SEM petrography — \"The petrographic texture of NWA 8003 was observed using a JEOL 7000F field emission gun scanning electron microscope (FEG-SEM) at Hokkaido University\" (p.7); phase identifications also rest on Raman spectra and EBSD patterns (p.4)"
            }
          ],
          "schema:name": "NWA 8003 eucrite"
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "State Key Laboratory for Mineral Deposits Research, Nanjing University"
      },
      "schema:description": "Pang et al. 2016, Sci. Rep. 6:26063 — NWA 8003 eucrite, Nanjing University. JEOL JXA-8100 (stated as \"JEOL 8100\"). WDS explicitly stated (\"JEOL 8100 WDS\"). ZAF matrix correction (NOT \"ZAF or PAP\" as in v2; paper states ZAF). Focused beam (20 nA) for most phases; defocused 2-5 µm for plagioclase and polymorphs. Natural and synthetic mineral standards (specific names N). Detection limit better than 0.02 wt% (as stated). Analytical software not stated.",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Polished thin section; carbon coating N",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "schema:additionalProperty": [],
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:deadTime": -9999
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NSFC 41373065; State Key Laboratory for Mineral Deposits Research ZZKT-201322; Fundamental Research Funds for the Central Universities — 'This study was supported by grants from ...'"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM (BSE imaging); petrographic microscopy"
      }
    },
    {
      "schema:linkRelationship": "coupledDataset",
      "schema:target": "Supplementary Information at www.nature.com/srep — 'Supplementary information accompanies this paper at http://www.nature.com/srep'; the EPMA data are in Supplementary Tables 1–4"
    }
  ],
  "ada:analyticalMode": [
    "WDS Point Analysis — 'Electron Probe Micro-Analyzer (EPMA) with wavelength dispersive spectrometers (WDS)'"
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "N — the averages are given as '±' values ('41 ± 8 mol%') without naming the statistic"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NSFC 41373065; State Key Laboratory for Mineral Deposits Research ZZKT-201322; Fundamental Research Funds for the Central Universities — 'This study was supported by grants from ...'",
  "ada:sampleName": "NWA 8003 eucrite",
  "ada:samplingUnitName": "Sample name only — NWA 8003; grains are identified by setting (\"garnet grains within the eclogitic mineral assemblage\", p.4), and the point analyses are in \"Supplementary Table 4\" (p.4), not in the archived PDF",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:detectionLimit": "all: better than 0.02 wt% (typical) — 'Typical detection limits for oxides of most elements were better than 0.02 wt%'",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    },
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EPMA/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:epmaTAPP-detail-Pang2016",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "EPMA",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/epmaTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 15,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "15 kV"
                },
                {
                  "@id": "ada:parameter/epmaTAPP/beamDiameter",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/beamDiameter"
                    }
                  ],
                  "schema:name": "Beam Diameter",
                  "schema:value": 2,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "plagioclase and its polymorphs: 2\u20135 \u00b5m; other: N \u2014 'a defocused beam (2\u20135 \u03bcm in diameter)'"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:epmaTAPP-detail-Pang2016/instrument/EPMA"
            }
          ]
        }
      ],
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening"
                }
              ],
              "schema:name": "Pre-Analysis Imaging and Screening",
              "schema:value": "SEM petrography \u2014 \"The petrographic texture of NWA 8003 was observed using a JEOL 7000F field emission gun scanning electron microscope (FEG-SEM) at Hokkaido University\" (p.7); phase identifications also rest on Raman spectra and EBSD patterns (p.4)"
            }
          ],
          "schema:name": "NWA 8003 eucrite"
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "State Key Laboratory for Mineral Deposits Research, Nanjing University"
      },
      "schema:description": "Pang et al. 2016, Sci. Rep. 6:26063 \u2014 NWA 8003 eucrite, Nanjing University. JEOL JXA-8100 (stated as \"JEOL 8100\"). WDS explicitly stated (\"JEOL 8100 WDS\"). ZAF matrix correction (NOT \"ZAF or PAP\" as in v2; paper states ZAF). Focused beam (20 nA) for most phases; defocused 2-5 \u00b5m for plagioclase and polymorphs. Natural and synthetic mineral standards (specific names N). Detection limit better than 0.02 wt% (as stated). Analytical software not stated.",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Polished thin section; carbon coating N",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "schema:additionalProperty": [],
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:deadTime": -9999
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NSFC 41373065; State Key Laboratory for Mineral Deposits Research ZZKT-201322; Fundamental Research Funds for the Central Universities \u2014 'This study was supported by grants from ...'"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM (BSE imaging); petrographic microscopy"
      }
    },
    {
      "schema:linkRelationship": "coupledDataset",
      "schema:target": "Supplementary Information at www.nature.com/srep \u2014 'Supplementary information accompanies this paper at http://www.nature.com/srep'; the EPMA data are in Supplementary Tables 1\u20134"
    }
  ],
  "ada:analyticalMode": [
    "WDS Point Analysis \u2014 'Electron Probe Micro-Analyzer (EPMA) with wavelength dispersive spectrometers (WDS)'"
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "N \u2014 the averages are given as '\u00b1' values ('41 \u00b1 8 mol%') without naming the statistic"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NSFC 41373065; State Key Laboratory for Mineral Deposits Research ZZKT-201322; Fundamental Research Funds for the Central Universities \u2014 'This study was supported by grants from ...'",
  "ada:sampleName": "NWA 8003 eucrite",
  "ada:samplingUnitName": "Sample name only \u2014 NWA 8003; grains are identified by setting (\"garnet grains within the eclogitic mineral assemblage\", p.4), and the point analyses are in \"Supplementary Table 4\" (p.4), not in the archived PDF",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:detectionLimit": "all: better than 0.02 wt% (typical) \u2014 'Typical detection limits for oxides of most elements were better than 0.02 wt%'",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix dqv: <http://www.w3.org/ns/dqv#> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:epmaTAPP-detail-Pang2016 a schema1:Dataset,
        schema1:Product ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "NSFC 41373065; State Key Laboratory for Mineral Deposits Research ZZKT-201322; Fundamental Research Funds for the Central Universities — 'This study was supported by grants from ...'" ] ;
    schema1:relatedLink [ schema1:linkRelationship "coupledDataset" ;
            schema1:target "Supplementary Information at www.nature.com/srep — 'Supplementary information accompanies this paper at http://www.nature.com/srep'; the EPMA data are in Supplementary Tables 1–4" ],
        [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "SEM (BSE imaging); petrographic microscopy" ] ] ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Analytical Precision" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Analytical Accuracy" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Goodness-of-Fit" ;
            dqv:value "N — the averages are given as '±' values ('41 ± 8 mol%') without naming the statistic" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Polished thin section; carbon coating N" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ] ] ;
            schema1:description "Pang et al. 2016, Sci. Rep. 6:26063 — NWA 8003 eucrite, Nanjing University. JEOL JXA-8100 (stated as \"JEOL 8100\"). WDS explicitly stated (\"JEOL 8100 WDS\"). ZAF matrix correction (NOT \"ZAF or PAP\" as in v2; paper states ZAF). Focused beam (20 nA) for most phases; defocused 2-5 µm for plagioclase and polymorphs. Natural and synthetic mineral standards (specific names N). Detection limit better than 0.02 wt% (as stated). Analytical software not stated." ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "State Key Laboratory for Mineral Deposits Research, Nanjing University" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
                    schema1:name "NWA 8003 eucrite" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ schema1:instrument <https://example.org/epmaTAPP-detail-Pang2016/instrument/EPMA> ] ;
            ada:combinedResults [ ] ;
            ada:deadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "WDS Point Analysis — 'Electron Probe Micro-Analyzer (EPMA) with wavelength dispersive spectrometers (WDS)'" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit "all: better than 0.02 wt% (typical) — 'Typical detection limits for oxides of most elements were better than 0.02 wt%'" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NSFC 41373065; State Key Laboratory for Mineral Deposits Research ZZKT-201322; Fundamental Research Funds for the Central Universities — 'This study was supported by grants from ...'" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:sampleName "NWA 8003 eucrite" ;
    ada:samplingUnitName "Sample name only — NWA 8003; grains are identified by setting (\"garnet grains within the eclogitic mineral assemblage\", p.4), and the point analyses are in \"Supplementary Table 4\" (p.4), not in the archived PDF" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" .

<https://example.org/epmaTAPP-detail-Pang2016/instrument/EPMA> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/epmaTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDiameter> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EPMA" ;
    schema1:name "no value available: schema:name" .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:description "15 kV" ;
    schema1:name "Accelerating Voltage" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/epmaTAPP/acceleratingVoltage> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 15 .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDiameter> a schema1:PropertyValue ;
    schema1:description "plagioclase and its polymorphs: 2–5 µm; other: N — 'a defocused beam (2–5 μm in diameter)'" ;
    schema1:name "Beam Diameter" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDiameter> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 2 .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "SEM petrography — \"The petrographic texture of NWA 8003 was observed using a JEOL 7000F field emission gun scanning electron microscope (FEG-SEM) at Hokkaido University\" (p.7); phase identifications also rest on Raman spectra and EBSD patterns (p.4)" .


```


### detail example McCoy2025
detail instance derived from McCoy+2025_SI | JEOL 8530F+ | WDS Point Analysis (Smithsonian).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "ex": "https://example.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/",
    "prov": "http://www.w3.org/ns/prov#"
  },
  "@id": "ex:epmaTAPP-detail-McCoy2025",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "EPMA",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/epmaTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 15,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "15 kV"
                },
                {
                  "@id": "ada:parameter/epmaTAPP/beamDiameter",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/beamDiameter"
                    }
                  ],
                  "schema:name": "Beam Diameter",
                  "schema:value": 5,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "carbonate: 5 µm; magnetite, olivine: 1 µm — 'with an analytical spot size of 5 µm' (carbonates); 'Analyses were conducted at 15kV and 10nA, with an analytical spot size of 1µm' (the magnetite and olivine sentence)"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:epmaTAPP-detail-McCoy2025/instrument/EPMA"
            }
          ]
        },
        {
          "bios:reagent": [
            {
              "ada:reagentRole": "referenceMaterial",
              "schema:name": "calcite, dolomite, rhodochrosite, magnetite, San Carlos olivine, Springwater olivine — carbonates: calcite, dolomite and rhodochrosite; magnetite and olivine: magnetite, San Carlos olivine and Springwater olivine (p.7)",
              "@type": [
                "schema:DefinedTerm"
              ]
            }
          ]
        }
      ],
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening"
                }
              ],
              "schema:name": "Pre-Analysis Imaging and Screening",
              "schema:value": "SEM mapping at the Smithsonian — particles 'analysed at 15 kV and around 0.5 nA in high vacuum using a Thermo Fisher Quattro FE-SEM'; 'Maps of loose grains were investigated, then used to inform sectioning' (p.7)"
            }
          ],
          "schema:name": "Bennu OSIRIS-REx samples (OREX-8#####-###)",
          "schema:identifier": "OREX-8#####-### (NASA curatorial ID, not IGSN)"
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Smithsonian Institution, National Museum of Natural History"
      },
      "schema:description": "McCoy et al. 2025, Nature 637:320-325 — Bennu evaporites. Protocol 1 of 2: Smithsonian Institution JEOL 8530 F+ Hyperprobe (Field Emission). Ir-coated specimens mounted on Ir-coated Parafilm. Carbonate analyses: 15 kV, 10 nA, 5 µm spot; LIFL (Fe,Mn), TAPL (Mg), PETL (Ca). Magnetite and olivine analyses: 15 kV, 10 nA, 1 µm spot; their own standard suite. Both primary and secondary standard suites fully documented with USNM catalog numbers. Acquisition software and matrix correction method N. WDS not explicitly stated in text (crystal designations LIFL/TAPL/PETL confirm WDS use).",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Ir-coated specimens — 'Electron microprobe analysis was conducted on Ir-coated specimens'; the mounting for the microprobe work is not stated",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "schema:additionalProperty": [],
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:deadTime": -9999
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NASA NNH09ZDA007O under contract NNM10AA11C (New Frontiers Program) — 'This material is based on work supported by ...'; individual grants are also listed by person (80NSSC22K1692, MR/T020261/1, ST/V000675/1, 22EXPOSITO)"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM-EDS (NHM London; Smithsonian; JSC); TEM-EDS/EELS; FIB-SEM; ToF-SIMS; XRD; XANES"
      }
    },
    {
      "schema:linkRelationship": "coupledDataset",
      "schema:target": "astromat.org, at the DOIs in Extended Data Table 3 — 'Instrument data supporting the experimental results from the samples analysed in this study will be available from Astromat (astromat.org) at the DOIs listed in Extended Data Table 3'"
    }
  ],
  "ada:analyticalMode": [
    "N — point analyses with named crystals (LIFL, TAPL, PETL); WDS or EDS is not stated, and the list has no value without one"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA NNH09ZDA007O under contract NNM10AA11C (New Frontiers Program) — 'This material is based on work supported by ...'; individual grants are also listed by person (80NSSC22K1692, MR/T020261/1, ST/V000675/1, 22EXPOSITO)",
  "ada:sampleName": "Bennu OSIRIS-REx samples (OREX-8#####-###)",
  "ada:samplingUnitName": "N — the Smithsonian microprobe passage names no specimens (\"conducted on Ir-coated specimens\", p.7); the paper's OREX numbers identify figure images, not microprobe analyses",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    },
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EPMA/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:epmaTAPP-detail-McCoy2025",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "EPMA",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/epmaTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 15,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "15 kV"
                },
                {
                  "@id": "ada:parameter/epmaTAPP/beamDiameter",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/beamDiameter"
                    }
                  ],
                  "schema:name": "Beam Diameter",
                  "schema:value": 5,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "carbonate: 5 \u00b5m; magnetite, olivine: 1 \u00b5m \u2014 'with an analytical spot size of 5 \u00b5m' (carbonates); 'Analyses were conducted at 15kV and 10nA, with an analytical spot size of 1\u00b5m' (the magnetite and olivine sentence)"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:epmaTAPP-detail-McCoy2025/instrument/EPMA"
            }
          ]
        },
        {
          "bios:reagent": [
            {
              "ada:reagentRole": "referenceMaterial",
              "schema:name": "calcite, dolomite, rhodochrosite, magnetite, San Carlos olivine, Springwater olivine \u2014 carbonates: calcite, dolomite and rhodochrosite; magnetite and olivine: magnetite, San Carlos olivine and Springwater olivine (p.7)",
              "@type": [
                "schema:DefinedTerm"
              ]
            }
          ]
        }
      ],
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening"
                }
              ],
              "schema:name": "Pre-Analysis Imaging and Screening",
              "schema:value": "SEM mapping at the Smithsonian \u2014 particles 'analysed at 15 kV and around 0.5 nA in high vacuum using a Thermo Fisher Quattro FE-SEM'; 'Maps of loose grains were investigated, then used to inform sectioning' (p.7)"
            }
          ],
          "schema:name": "Bennu OSIRIS-REx samples (OREX-8#####-###)",
          "schema:identifier": "OREX-8#####-### (NASA curatorial ID, not IGSN)"
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Smithsonian Institution, National Museum of Natural History"
      },
      "schema:description": "McCoy et al. 2025, Nature 637:320-325 \u2014 Bennu evaporites. Protocol 1 of 2: Smithsonian Institution JEOL 8530 F+ Hyperprobe (Field Emission). Ir-coated specimens mounted on Ir-coated Parafilm. Carbonate analyses: 15 kV, 10 nA, 5 \u00b5m spot; LIFL (Fe,Mn), TAPL (Mg), PETL (Ca). Magnetite and olivine analyses: 15 kV, 10 nA, 1 \u00b5m spot; their own standard suite. Both primary and secondary standard suites fully documented with USNM catalog numbers. Acquisition software and matrix correction method N. WDS not explicitly stated in text (crystal designations LIFL/TAPL/PETL confirm WDS use).",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Ir-coated specimens \u2014 'Electron microprobe analysis was conducted on Ir-coated specimens'; the mounting for the microprobe work is not stated",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "schema:additionalProperty": [],
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:deadTime": -9999
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NASA NNH09ZDA007O under contract NNM10AA11C (New Frontiers Program) \u2014 'This material is based on work supported by ...'; individual grants are also listed by person (80NSSC22K1692, MR/T020261/1, ST/V000675/1, 22EXPOSITO)"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM-EDS (NHM London; Smithsonian; JSC); TEM-EDS/EELS; FIB-SEM; ToF-SIMS; XRD; XANES"
      }
    },
    {
      "schema:linkRelationship": "coupledDataset",
      "schema:target": "astromat.org, at the DOIs in Extended Data Table 3 \u2014 'Instrument data supporting the experimental results from the samples analysed in this study will be available from Astromat (astromat.org) at the DOIs listed in Extended Data Table 3'"
    }
  ],
  "ada:analyticalMode": [
    "N \u2014 point analyses with named crystals (LIFL, TAPL, PETL); WDS or EDS is not stated, and the list has no value without one"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA NNH09ZDA007O under contract NNM10AA11C (New Frontiers Program) \u2014 'This material is based on work supported by ...'; individual grants are also listed by person (80NSSC22K1692, MR/T020261/1, ST/V000675/1, 22EXPOSITO)",
  "ada:sampleName": "Bennu OSIRIS-REx samples (OREX-8#####-###)",
  "ada:samplingUnitName": "N \u2014 the Smithsonian microprobe passage names no specimens (\"conducted on Ir-coated specimens\", p.7); the paper's OREX numbers identify figure images, not microprobe analyses",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999
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

ex:epmaTAPP-detail-McCoy2025 a schema1:Dataset,
        schema1:Product ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "NASA NNH09ZDA007O under contract NNM10AA11C (New Frontiers Program) — 'This material is based on work supported by ...'; individual grants are also listed by person (80NSSC22K1692, MR/T020261/1, ST/V000675/1, 22EXPOSITO)" ] ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "SEM-EDS (NHM London; Smithsonian; JSC); TEM-EDS/EELS; FIB-SEM; ToF-SIMS; XRD; XANES" ] ],
        [ schema1:linkRelationship "coupledDataset" ;
            schema1:target "astromat.org, at the DOIs in Extended Data Table 3 — 'Instrument data supporting the experimental results from the samples analysed in this study will be available from Astromat (astromat.org) at the DOIs listed in Extended Data Table 3'" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Ir-coated specimens — 'Electron microprobe analysis was conducted on Ir-coated specimens'; the mounting for the microprobe work is not stated" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ] ] ;
            schema1:description "McCoy et al. 2025, Nature 637:320-325 — Bennu evaporites. Protocol 1 of 2: Smithsonian Institution JEOL 8530 F+ Hyperprobe (Field Emission). Ir-coated specimens mounted on Ir-coated Parafilm. Carbonate analyses: 15 kV, 10 nA, 5 µm spot; LIFL (Fe,Mn), TAPL (Mg), PETL (Ca). Magnetite and olivine analyses: 15 kV, 10 nA, 1 µm spot; their own standard suite. Both primary and secondary standard suites fully documented with USNM catalog numbers. Acquisition software and matrix correction method N. WDS not explicitly stated in text (crystal designations LIFL/TAPL/PETL confirm WDS use)." ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Smithsonian Institution, National Museum of Natural History" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
                    schema1:identifier "OREX-8#####-### (NASA curatorial ID, not IGSN)" ;
                    schema1:name "Bennu OSIRIS-REx samples (OREX-8#####-###)" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "calcite, dolomite, rhodochrosite, magnetite, San Carlos olivine, Springwater olivine — carbonates: calcite, dolomite and rhodochrosite; magnetite and olivine: magnetite, San Carlos olivine and Springwater olivine (p.7)" ;
                            ada:reagentRole "referenceMaterial" ] ],
                [ schema1:instrument <https://example.org/epmaTAPP-detail-McCoy2025/instrument/EPMA> ] ;
            ada:combinedResults [ ] ;
            ada:deadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "N — point analyses with named crystals (LIFL, TAPL, PETL); WDS or EDS is not stated, and the list has no value without one" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NASA NNH09ZDA007O under contract NNM10AA11C (New Frontiers Program) — 'This material is based on work supported by ...'; individual grants are also listed by person (80NSSC22K1692, MR/T020261/1, ST/V000675/1, 22EXPOSITO)" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:sampleName "Bennu OSIRIS-REx samples (OREX-8#####-###)" ;
    ada:samplingUnitName "N — the Smithsonian microprobe passage names no specimens (\"conducted on Ir-coated specimens\", p.7); the paper's OREX numbers identify figure images, not microprobe analyses" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" .

<https://example.org/epmaTAPP-detail-McCoy2025/instrument/EPMA> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/epmaTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDiameter> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EPMA" ;
    schema1:name "no value available: schema:name" .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:description "15 kV" ;
    schema1:name "Accelerating Voltage" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/epmaTAPP/acceleratingVoltage> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 15 .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDiameter> a schema1:PropertyValue ;
    schema1:description "carbonate: 5 µm; magnetite, olivine: 1 µm — 'with an analytical spot size of 5 µm' (carbonates); 'Analyses were conducted at 15kV and 10nA, with an analytical spot size of 1µm' (the magnetite and olivine sentence)" ;
    schema1:name "Beam Diameter" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDiameter> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 5 .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "SEM mapping at the Smithsonian — particles 'analysed at 15 kV and around 0.5 nA in high vacuum using a Thermo Fisher Quattro FE-SEM'; 'Maps of loose grains were investigated, then used to inform sectioning' (p.7)" .


```


### detail example McCoy2025-2
detail instance derived from McCoy+2025_UA | Cameca SX-100 | WDS Point Analysis (K-ALFAA U.Arizona).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "ex": "https://example.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/",
    "prov": "http://www.w3.org/ns/prov#"
  },
  "@id": "ex:epmaTAPP-detail-McCoy2025-2",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "EPMA",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/epmaTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 15,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "15 kV"
                },
                {
                  "@id": "ada:parameter/epmaTAPP/beamDiameter",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/beamDiameter"
                    }
                  ],
                  "schema:name": "Beam Diameter",
                  "schema:value": 1,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "\"Mg,Na phosphate\": 1 µm; other: N — 'using a 1-µm beam size'"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:epmaTAPP-detail-McCoy2025-2/instrument/EPMA"
            }
          ]
        }
      ],
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening"
                }
              ],
              "schema:name": "Pre-Analysis Imaging and Screening",
              "schema:value": "N — the paper describes SEM characterisation at JSC, the NHM, the Smithsonian and Curtin, not for the K-ALFAA microprobe work"
            }
          ],
          "schema:name": "Bennu OSIRIS-REx samples (OREX-8#####-###)",
          "schema:identifier": "OREX-8#####-### (NASA curatorial ID, not IGSN)"
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Kuiper-Arizona Laboratory for Astromaterials Analysis (K-ALFAA), University of Arizona"
      },
      "schema:description": "McCoy et al. 2025, Nature 637:320-325 — Bennu evaporites. Protocol 2 of 2: U. Arizona K-ALFAA Cameca SX-100. 20 nm carbon coat. WDS explicitly stated for phosphate analyses. Mg,Na phosphate analyses: 15 kV, 8 nA, 1 µm. Carbonate analyses at K-ALFAA also mentioned; conditions N. Full primary standard suite documented for phosphates and carbonates. Acquisition software and matrix correction method N.",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Polished section; 20 nm carbon coat",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "schema:additionalProperty": [],
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:deadTime": -9999
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NASA NNH09ZDA007O under contract NNM10AA11C (New Frontiers Program) — 'This material is based on work supported by ...'; individual grants are also listed by person (80NSSC22K1692, MR/T020261/1, ST/V000675/1, 22EXPOSITO)"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM-EDS (NHM London; Smithsonian; JSC); TEM-EDS/EELS; FIB-SEM; ToF-SIMS; XRD; XANES"
      }
    },
    {
      "schema:linkRelationship": "coupledDataset",
      "schema:target": "astromat.org, at the DOIs in Extended Data Table 3 — as for the Smithsonian procedure"
    }
  ],
  "ada:analyticalMode": [
    "WDS Point Analysis — 'Wavelength-dispersive X-ray spectroscopy analyses of Mg,Na phosphate'"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA NNH09ZDA007O under contract NNM10AA11C (New Frontiers Program) — 'This material is based on work supported by ...'; individual grants are also listed by person (80NSSC22K1692, MR/T020261/1, ST/V000675/1, 22EXPOSITO)",
  "ada:sampleName": "Bennu OSIRIS-REx samples (OREX-8#####-###)",
  "ada:samplingUnitName": "N — the Arizona microprobe passage names no specimen (\"the section was coated with a thin film of carbon\", p.7); the paper's OREX numbers identify figure images, not microprobe analyses",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    },
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EPMA/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:epmaTAPP-detail-McCoy2025-2",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "EPMA",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/epmaTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 15,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "15 kV"
                },
                {
                  "@id": "ada:parameter/epmaTAPP/beamDiameter",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/beamDiameter"
                    }
                  ],
                  "schema:name": "Beam Diameter",
                  "schema:value": 1,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "\"Mg,Na phosphate\": 1 \u00b5m; other: N \u2014 'using a 1-\u00b5m beam size'"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:epmaTAPP-detail-McCoy2025-2/instrument/EPMA"
            }
          ]
        }
      ],
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening"
                }
              ],
              "schema:name": "Pre-Analysis Imaging and Screening",
              "schema:value": "N \u2014 the paper describes SEM characterisation at JSC, the NHM, the Smithsonian and Curtin, not for the K-ALFAA microprobe work"
            }
          ],
          "schema:name": "Bennu OSIRIS-REx samples (OREX-8#####-###)",
          "schema:identifier": "OREX-8#####-### (NASA curatorial ID, not IGSN)"
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Kuiper-Arizona Laboratory for Astromaterials Analysis (K-ALFAA), University of Arizona"
      },
      "schema:description": "McCoy et al. 2025, Nature 637:320-325 \u2014 Bennu evaporites. Protocol 2 of 2: U. Arizona K-ALFAA Cameca SX-100. 20 nm carbon coat. WDS explicitly stated for phosphate analyses. Mg,Na phosphate analyses: 15 kV, 8 nA, 1 \u00b5m. Carbonate analyses at K-ALFAA also mentioned; conditions N. Full primary standard suite documented for phosphates and carbonates. Acquisition software and matrix correction method N.",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Polished section; 20 nm carbon coat",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "schema:additionalProperty": [],
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:deadTime": -9999
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NASA NNH09ZDA007O under contract NNM10AA11C (New Frontiers Program) \u2014 'This material is based on work supported by ...'; individual grants are also listed by person (80NSSC22K1692, MR/T020261/1, ST/V000675/1, 22EXPOSITO)"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM-EDS (NHM London; Smithsonian; JSC); TEM-EDS/EELS; FIB-SEM; ToF-SIMS; XRD; XANES"
      }
    },
    {
      "schema:linkRelationship": "coupledDataset",
      "schema:target": "astromat.org, at the DOIs in Extended Data Table 3 \u2014 as for the Smithsonian procedure"
    }
  ],
  "ada:analyticalMode": [
    "WDS Point Analysis \u2014 'Wavelength-dispersive X-ray spectroscopy analyses of Mg,Na phosphate'"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA NNH09ZDA007O under contract NNM10AA11C (New Frontiers Program) \u2014 'This material is based on work supported by ...'; individual grants are also listed by person (80NSSC22K1692, MR/T020261/1, ST/V000675/1, 22EXPOSITO)",
  "ada:sampleName": "Bennu OSIRIS-REx samples (OREX-8#####-###)",
  "ada:samplingUnitName": "N \u2014 the Arizona microprobe passage names no specimen (\"the section was coated with a thin film of carbon\", p.7); the paper's OREX numbers identify figure images, not microprobe analyses",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:epmaTAPP-detail-McCoy2025-2 a schema1:Dataset,
        schema1:Product ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "NASA NNH09ZDA007O under contract NNM10AA11C (New Frontiers Program) — 'This material is based on work supported by ...'; individual grants are also listed by person (80NSSC22K1692, MR/T020261/1, ST/V000675/1, 22EXPOSITO)" ] ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "SEM-EDS (NHM London; Smithsonian; JSC); TEM-EDS/EELS; FIB-SEM; ToF-SIMS; XRD; XANES" ] ],
        [ schema1:linkRelationship "coupledDataset" ;
            schema1:target "astromat.org, at the DOIs in Extended Data Table 3 — as for the Smithsonian procedure" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Polished section; 20 nm carbon coat" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ] ] ;
            schema1:description "McCoy et al. 2025, Nature 637:320-325 — Bennu evaporites. Protocol 2 of 2: U. Arizona K-ALFAA Cameca SX-100. 20 nm carbon coat. WDS explicitly stated for phosphate analyses. Mg,Na phosphate analyses: 15 kV, 8 nA, 1 µm. Carbonate analyses at K-ALFAA also mentioned; conditions N. Full primary standard suite documented for phosphates and carbonates. Acquisition software and matrix correction method N." ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Kuiper-Arizona Laboratory for Astromaterials Analysis (K-ALFAA), University of Arizona" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
                    schema1:identifier "OREX-8#####-### (NASA curatorial ID, not IGSN)" ;
                    schema1:name "Bennu OSIRIS-REx samples (OREX-8#####-###)" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ schema1:instrument <https://example.org/epmaTAPP-detail-McCoy2025-2/instrument/EPMA> ] ;
            ada:combinedResults [ ] ;
            ada:deadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "WDS Point Analysis — 'Wavelength-dispersive X-ray spectroscopy analyses of Mg,Na phosphate'" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NASA NNH09ZDA007O under contract NNM10AA11C (New Frontiers Program) — 'This material is based on work supported by ...'; individual grants are also listed by person (80NSSC22K1692, MR/T020261/1, ST/V000675/1, 22EXPOSITO)" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:sampleName "Bennu OSIRIS-REx samples (OREX-8#####-###)" ;
    ada:samplingUnitName "N — the Arizona microprobe passage names no specimen (\"the section was coated with a thin film of carbon\", p.7); the paper's OREX numbers identify figure images, not microprobe analyses" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" .

<https://example.org/epmaTAPP-detail-McCoy2025-2/instrument/EPMA> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/epmaTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDiameter> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EPMA" ;
    schema1:name "no value available: schema:name" .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:description "15 kV" ;
    schema1:name "Accelerating Voltage" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/epmaTAPP/acceleratingVoltage> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 15 .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDiameter> a schema1:PropertyValue ;
    schema1:description "\"Mg,Na phosphate\": 1 µm; other: N — 'using a 1-µm beam size'" ;
    schema1:name "Beam Diameter" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDiameter> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1 .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "N — the paper describes SEM characterisation at JSC, the NHM, the Smithsonian and Curtin, not for the K-ALFAA microprobe work" .


```


### detail example Zega2025
detail instance derived from Zega+2025 | Cameca SX-100 Ultra | WDS Point Analysis (K-ALFAA U.Arizona).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "ex": "https://example.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/",
    "prov": "http://www.w3.org/ns/prov#"
  },
  "@id": "ex:epmaTAPP-detail-Zega2025",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "EPMA",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/epmaTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 15,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "15 kV"
                },
                {
                  "@id": "ada:parameter/epmaTAPP/beamDiameter",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/beamDiameter"
                    }
                  ],
                  "schema:name": "Beam Diameter",
                  "schema:value": 2,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "phosphates, carbonates: 2 µm; other: N — p.9"
                },
                {
                  "@id": "ada:parameter/epmaTAPP/mappingBeamCurrent",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/mappingBeamCurrent"
                    }
                  ],
                  "schema:name": "Mapping Beam Current",
                  "schema:value": 20,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "20 nA — 'X-ray maps and BSE images were run at 15kV and 20nA'"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:epmaTAPP-detail-Zega2025/instrument/EPMA"
            }
          ]
        },
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "XMapTools (for phase maps)",
              "@type": [
                "schema:SoftwareApplication"
              ]
            }
          ]
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/epmaTAPP/beamDamageMinimization",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/epmaTAPP/beamDamageMinimization"
            }
          ],
          "schema:name": "Beam Damage Minimization",
          "schema:value": "phosphates, carbonates: 2 µm defocused beam, lower beam currents and shorter count times; other: N — 'to minimize possible beam damage effects'"
        }
      ],
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening"
                }
              ],
              "schema:name": "Pre-Analysis Imaging and Screening",
              "schema:value": "SEM imaging and EDS mapping before the probe — particles were characterized by SE and BSE imaging and by EDS mapping of \"The compositional heterogeneity of the particles\" (p.9), and the paper's Fig. 1 pairs those BSE images with the EMPA data (p.2); the Methods list SEM before electron microprobe analysis without stating an explicit order"
            }
          ],
          "schema:name": "Bennu OSIRIS-REx samples (OREX-5/8#####-###)",
          "schema:identifier": "OREX-5/8#####-### (NASA curatorial ID, not IGSN)"
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Kuiper-Arizona Laboratory for Astromaterials Analysis (K-ALFAA), University of Arizona"
      },
      "schema:description": "Zega et al. 2025, Nat. Geosci. — mineralogical evidence for hydrothermal alteration of Bennu. K-ALFAA, University of Arizona. Instrument stated as \"SX-100 Ultra electron microprobe in the K-ALFAA\". IMPORTANT: v2 had \"no protocol details reported\" — this was WRONG. The paper provides detailed EPMA conditions: X-ray maps and BSE images: 15 kV, 20 nA. Silicates/sulfides/oxides: 15 kV, 20 nA, focused, 20 s peak, 10 s on each background. Phosphates: 15 kV, 8 nA, 2 µm defocused, 20 s peak and 10 s background. Carbonates: 15 kV, 4 nA, 2 µm defocused, 10 s peak and 5 s background. Standards: \"well-characterized natural and synthetic materials\" (specific names N). Phase maps generated using XMapTools. WDS and matrix correction NOT explicitly stated in paper.",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:deadTime": -9999
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NASA NNH09ZDA007O under contract NNM10AA11C (New Frontiers Program) — 'This material is based upon work supported by ...'; the K-ALFAA facility and instrumentation support is under Funding Source for Procedure Development"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM-EDS; TEM-EDS/EELS; FIB-SEM; XRD; XANES"
      }
    }
  ],
  "ada:analyticalMode": [
    "N — quantitative point analyses and X-ray maps ('BSE images, element maps and quantitative compositional analyses'); WDS or EDS is not stated, and the list has no value without one"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA NNH09ZDA007O under contract NNM10AA11C (New Frontiers Program) — 'This material is based upon work supported by ...'; the K-ALFAA facility and instrumentation support is under Funding Source for Procedure Development",
  "ada:sampleName": "Bennu OSIRIS-REx samples (OREX-5/8#####-###)",
  "ada:samplingUnitName": "Labelled by curation number per particle: \"EMPA data from Bennu particles\" (Fig. 1) cites \"OREX-803095-0\" and \"OREX-803096-0\", and sulfide compositions \"in samples OREX-803095-0, OREX-803096-0, OREX-803066-0, OREX-803067-0 and OREX-803070-0\" (p.2); points within particles are not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    },
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EPMA/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:epmaTAPP-detail-Zega2025",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "EPMA",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/epmaTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 15,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "15 kV"
                },
                {
                  "@id": "ada:parameter/epmaTAPP/beamDiameter",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/beamDiameter"
                    }
                  ],
                  "schema:name": "Beam Diameter",
                  "schema:value": 2,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "phosphates, carbonates: 2 \u00b5m; other: N \u2014 p.9"
                },
                {
                  "@id": "ada:parameter/epmaTAPP/mappingBeamCurrent",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/mappingBeamCurrent"
                    }
                  ],
                  "schema:name": "Mapping Beam Current",
                  "schema:value": 20,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "20 nA \u2014 'X-ray maps and BSE images were run at 15kV and 20nA'"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:epmaTAPP-detail-Zega2025/instrument/EPMA"
            }
          ]
        },
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "XMapTools (for phase maps)",
              "@type": [
                "schema:SoftwareApplication"
              ]
            }
          ]
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/epmaTAPP/beamDamageMinimization",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/epmaTAPP/beamDamageMinimization"
            }
          ],
          "schema:name": "Beam Damage Minimization",
          "schema:value": "phosphates, carbonates: 2 \u00b5m defocused beam, lower beam currents and shorter count times; other: N \u2014 'to minimize possible beam damage effects'"
        }
      ],
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening"
                }
              ],
              "schema:name": "Pre-Analysis Imaging and Screening",
              "schema:value": "SEM imaging and EDS mapping before the probe \u2014 particles were characterized by SE and BSE imaging and by EDS mapping of \"The compositional heterogeneity of the particles\" (p.9), and the paper's Fig. 1 pairs those BSE images with the EMPA data (p.2); the Methods list SEM before electron microprobe analysis without stating an explicit order"
            }
          ],
          "schema:name": "Bennu OSIRIS-REx samples (OREX-5/8#####-###)",
          "schema:identifier": "OREX-5/8#####-### (NASA curatorial ID, not IGSN)"
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Kuiper-Arizona Laboratory for Astromaterials Analysis (K-ALFAA), University of Arizona"
      },
      "schema:description": "Zega et al. 2025, Nat. Geosci. \u2014 mineralogical evidence for hydrothermal alteration of Bennu. K-ALFAA, University of Arizona. Instrument stated as \"SX-100 Ultra electron microprobe in the K-ALFAA\". IMPORTANT: v2 had \"no protocol details reported\" \u2014 this was WRONG. The paper provides detailed EPMA conditions: X-ray maps and BSE images: 15 kV, 20 nA. Silicates/sulfides/oxides: 15 kV, 20 nA, focused, 20 s peak, 10 s on each background. Phosphates: 15 kV, 8 nA, 2 \u00b5m defocused, 20 s peak and 10 s background. Carbonates: 15 kV, 4 nA, 2 \u00b5m defocused, 10 s peak and 5 s background. Standards: \"well-characterized natural and synthetic materials\" (specific names N). Phase maps generated using XMapTools. WDS and matrix correction NOT explicitly stated in paper.",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:deadTime": -9999
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NASA NNH09ZDA007O under contract NNM10AA11C (New Frontiers Program) \u2014 'This material is based upon work supported by ...'; the K-ALFAA facility and instrumentation support is under Funding Source for Procedure Development"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM-EDS; TEM-EDS/EELS; FIB-SEM; XRD; XANES"
      }
    }
  ],
  "ada:analyticalMode": [
    "N \u2014 quantitative point analyses and X-ray maps ('BSE images, element maps and quantitative compositional analyses'); WDS or EDS is not stated, and the list has no value without one"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA NNH09ZDA007O under contract NNM10AA11C (New Frontiers Program) \u2014 'This material is based upon work supported by ...'; the K-ALFAA facility and instrumentation support is under Funding Source for Procedure Development",
  "ada:sampleName": "Bennu OSIRIS-REx samples (OREX-5/8#####-###)",
  "ada:samplingUnitName": "Labelled by curation number per particle: \"EMPA data from Bennu particles\" (Fig. 1) cites \"OREX-803095-0\" and \"OREX-803096-0\", and sulfide compositions \"in samples OREX-803095-0, OREX-803096-0, OREX-803066-0, OREX-803067-0 and OREX-803070-0\" (p.2); points within particles are not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix bios: <https://bioschemas.org/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:epmaTAPP-detail-Zega2025 a schema1:Dataset,
        schema1:Product ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "NASA NNH09ZDA007O under contract NNM10AA11C (New Frontiers Program) — 'This material is based upon work supported by ...'; the K-ALFAA facility and instrumentation support is under Funding Source for Procedure Development" ] ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "SEM-EDS; TEM-EDS/EELS; FIB-SEM; XRD; XANES" ] ] ;
    prov:wasGeneratedBy [ schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDamageMinimization> ;
            schema1:description "Zega et al. 2025, Nat. Geosci. — mineralogical evidence for hydrothermal alteration of Bennu. K-ALFAA, University of Arizona. Instrument stated as \"SX-100 Ultra electron microprobe in the K-ALFAA\". IMPORTANT: v2 had \"no protocol details reported\" — this was WRONG. The paper provides detailed EPMA conditions: X-ray maps and BSE images: 15 kV, 20 nA. Silicates/sulfides/oxides: 15 kV, 20 nA, focused, 20 s peak, 10 s on each background. Phosphates: 15 kV, 8 nA, 2 µm defocused, 20 s peak and 10 s background. Carbonates: 15 kV, 4 nA, 2 µm defocused, 10 s peak and 5 s background. Standards: \"well-characterized natural and synthetic materials\" (specific names N). Phase maps generated using XMapTools. WDS and matrix correction NOT explicitly stated in paper." ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Kuiper-Arizona Laboratory for Astromaterials Analysis (K-ALFAA), University of Arizona" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
                    schema1:identifier "OREX-5/8#####-### (NASA curatorial ID, not IGSN)" ;
                    schema1:name "Bennu OSIRIS-REx samples (OREX-5/8#####-###)" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ schema1:instrument <https://example.org/epmaTAPP-detail-Zega2025/instrument/EPMA> ],
                [ bios:computationalTool [ a schema1:SoftwareApplication ;
                            schema1:name "XMapTools (for phase maps)" ;
                            ada:toolRole "dataReduction" ] ] ;
            ada:combinedResults [ ] ;
            ada:deadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "N — quantitative point analyses and X-ray maps ('BSE images, element maps and quantitative compositional analyses'); WDS or EDS is not stated, and the list has no value without one" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NASA NNH09ZDA007O under contract NNM10AA11C (New Frontiers Program) — 'This material is based upon work supported by ...'; the K-ALFAA facility and instrumentation support is under Funding Source for Procedure Development" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:sampleName "Bennu OSIRIS-REx samples (OREX-5/8#####-###)" ;
    ada:samplingUnitName "Labelled by curation number per particle: \"EMPA data from Bennu particles\" (Fig. 1) cites \"OREX-803095-0\" and \"OREX-803096-0\", and sulfide compositions \"in samples OREX-803095-0, OREX-803096-0, OREX-803066-0, OREX-803067-0 and OREX-803070-0\" (p.2); points within particles are not labelled" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" .

<https://example.org/epmaTAPP-detail-Zega2025/instrument/EPMA> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/epmaTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDiameter>,
        <https://ada.astromat.org/metadata/parameter/epmaTAPP/mappingBeamCurrent> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EPMA" ;
    schema1:name "no value available: schema:name" .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:description "15 kV" ;
    schema1:name "Accelerating Voltage" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/epmaTAPP/acceleratingVoltage> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 15 .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDamageMinimization> a schema1:PropertyValue ;
    schema1:name "Beam Damage Minimization" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDamageMinimization> ;
    schema1:value "phosphates, carbonates: 2 µm defocused beam, lower beam currents and shorter count times; other: N — 'to minimize possible beam damage effects'" .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDiameter> a schema1:PropertyValue ;
    schema1:description "phosphates, carbonates: 2 µm; other: N — p.9" ;
    schema1:name "Beam Diameter" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDiameter> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 2 .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/mappingBeamCurrent> a schema1:PropertyValue ;
    schema1:description "20 nA — 'X-ray maps and BSE images were run at 15kV and 20nA'" ;
    schema1:name "Mapping Beam Current" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/epmaTAPP/mappingBeamCurrent> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 20 .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "SEM imaging and EDS mapping before the probe — particles were characterized by SE and BSE imaging and by EDS mapping of \"The compositional heterogeneity of the particles\" (p.9), and the paper's Fig. 1 pairs those BSE images with the EMPA data (p.2); the Methods list SEM before electron microprobe analysis without stating an explicit order" .


```


### detail example Barnes2025
detail instance derived from Barnes+2025 | JEOL JXA-8230 | WDS Point Analysis (CRPG Nancy).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "ex": "https://example.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/",
    "prov": "http://www.w3.org/ns/prov#"
  },
  "@id": "ex:epmaTAPP-detail-Barnes2025",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "EPMA",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/epmaTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 20,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "20 kV"
                },
                {
                  "@id": "ada:parameter/epmaTAPP/beamDiameter",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/beamDiameter"
                    }
                  ],
                  "schema:name": "Beam Diameter",
                  "schema:value": 1,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "all: 1 µm — as above"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:epmaTAPP-detail-Barnes2025/instrument/EPMA"
            }
          ]
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/epmaTAPP/beamRasterDimensions",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/epmaTAPP/beamRasterDimensions"
            }
          ],
          "schema:name": "Beam Raster Dimensions",
          "schema:value": 5,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "carbonates: 5 × 5 µm²; other: N/A — as above"
        }
      ],
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening"
                }
              ],
              "schema:name": "Pre-Analysis Imaging and Screening",
              "schema:value": "SEM imaging and multi-element EDS mapping — \"SEM observations were performed on the samples using a JEOL JSM-6510 with 3-nA primary beam at 15 kV. We also performed multi-element EDS mapping (Mg, Si, Fe, Ni, S, Na, Ca and Al) of the different grains\", after which \"Quantitative chemical analyses were performed using a JEOL JXA-8230 electron microprobe\" (p.11)"
            }
          ],
          "schema:name": "OREX-800045-103 and OREX-800045-107",
          "schema:identifier": "OREX-800045-103; OREX-800045-107 (NASA curatorial IDs, not IGSN)"
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Centre de Recherches Pétrographiques et Géochimiques (CRPG), Nancy, France"
      },
      "schema:description": "Barnes et al. 2025, Nat. Astron. — variety and origin of accreted materials in Bennu. Protocol 1 of 2: CRPG Nancy, JEOL JXA-8230. Instrument has 5 WDS spectrometers + 1 SDD EDS; per-analyte technique (WDS vs. EDS) not stated. Two analytical sessions: session 1 (no Na, K); session 2 (with Na, K). Counting times are stated as total peak + background combined: 200 ms for minor elements (Al, Ti, Ca, Mn, Cr) and 20 ms for major elements (Mg, Fe, Si). Full primary standard suite stated with element assignments. Full per-element detection limits stated. Matrix correction method not stated. Sample preparation done at Université Côte d'Azur (not at CRPG). Beam current not stated for NHM protocol; 3 nA mentioned in text is for SEM-EDS (different instrument).",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Aggregate particles (<1 mm) mounted in epoxy at Université Côte d'Azur; polished; carbon coated (thickness N)",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "schema:additionalProperty": [],
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:deadTime": -9999
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NASA NNH09ZDA007O under contract NNM10AA11C (New Frontiers Program) — acknowledged with the named authors; further grants are listed by person across many laboratories, and none is attributed to the microprobe work"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM-BSE (JEOL JSM-6510, 15 kV, 3 nA); SEM-EDS (multi-element mapping); SIMS (CAMECA IMS 1270 E7, CRPG); NanoSIMS (K-ALFAA); ICP-MS; MC-ICP-MS; noble gas MS"
      }
    }
  ],
  "ada:analyticalMode": [
    "N — quantitative point analyses on an instrument 'equipped with five wavelength-dispersive spectrometers and one silicon drift detector energy dispersive spectrometer'; which detector measured which element is not stated"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA NNH09ZDA007O under contract NNM10AA11C (New Frontiers Program) — acknowledged with the named authors; further grants are listed by person across many laboratories, and none is attributed to the microprobe work",
  "ada:sampleName": "OREX-800045-103 and OREX-800045-107",
  "ada:samplingUnitName": "Labelled at split level: \"Samples OREX-800045-103 and OREX-800045-107 ... Aggregate particles (<1 mm) were mounted in epoxy\" (p.11); particles and points are not labelled, and the data are \"compiled in Supplementary Table 14\" (p.11), not in the archived PDF",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:detectionLimit": "Mg: 0.025 wt%; Fe: 0.025 wt%; Si, K, Na: 0.05 wt%; Ca: 0.005 wt%; Al: 0.02 wt%; Ti: 0.005 wt%; Cr: 0.015 wt%; Mn: 0.008 wt%; other: N — p.11",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    },
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EPMA/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:epmaTAPP-detail-Barnes2025",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "EPMA",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/epmaTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 20,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "20 kV"
                },
                {
                  "@id": "ada:parameter/epmaTAPP/beamDiameter",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/beamDiameter"
                    }
                  ],
                  "schema:name": "Beam Diameter",
                  "schema:value": 1,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "all: 1 \u00b5m \u2014 as above"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:epmaTAPP-detail-Barnes2025/instrument/EPMA"
            }
          ]
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/epmaTAPP/beamRasterDimensions",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/epmaTAPP/beamRasterDimensions"
            }
          ],
          "schema:name": "Beam Raster Dimensions",
          "schema:value": 5,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "carbonates: 5 \u00d7 5 \u00b5m\u00b2; other: N/A \u2014 as above"
        }
      ],
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening"
                }
              ],
              "schema:name": "Pre-Analysis Imaging and Screening",
              "schema:value": "SEM imaging and multi-element EDS mapping \u2014 \"SEM observations were performed on the samples using a JEOL JSM-6510 with 3-nA primary beam at 15 kV. We also performed multi-element EDS mapping (Mg, Si, Fe, Ni, S, Na, Ca and Al) of the different grains\", after which \"Quantitative chemical analyses were performed using a JEOL JXA-8230 electron microprobe\" (p.11)"
            }
          ],
          "schema:name": "OREX-800045-103 and OREX-800045-107",
          "schema:identifier": "OREX-800045-103; OREX-800045-107 (NASA curatorial IDs, not IGSN)"
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Centre de Recherches P\u00e9trographiques et G\u00e9ochimiques (CRPG), Nancy, France"
      },
      "schema:description": "Barnes et al. 2025, Nat. Astron. \u2014 variety and origin of accreted materials in Bennu. Protocol 1 of 2: CRPG Nancy, JEOL JXA-8230. Instrument has 5 WDS spectrometers + 1 SDD EDS; per-analyte technique (WDS vs. EDS) not stated. Two analytical sessions: session 1 (no Na, K); session 2 (with Na, K). Counting times are stated as total peak + background combined: 200 ms for minor elements (Al, Ti, Ca, Mn, Cr) and 20 ms for major elements (Mg, Fe, Si). Full primary standard suite stated with element assignments. Full per-element detection limits stated. Matrix correction method not stated. Sample preparation done at Universit\u00e9 C\u00f4te d'Azur (not at CRPG). Beam current not stated for NHM protocol; 3 nA mentioned in text is for SEM-EDS (different instrument).",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Aggregate particles (<1 mm) mounted in epoxy at Universit\u00e9 C\u00f4te d'Azur; polished; carbon coated (thickness N)",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "schema:additionalProperty": [],
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:deadTime": -9999
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NASA NNH09ZDA007O under contract NNM10AA11C (New Frontiers Program) \u2014 acknowledged with the named authors; further grants are listed by person across many laboratories, and none is attributed to the microprobe work"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM-BSE (JEOL JSM-6510, 15 kV, 3 nA); SEM-EDS (multi-element mapping); SIMS (CAMECA IMS 1270 E7, CRPG); NanoSIMS (K-ALFAA); ICP-MS; MC-ICP-MS; noble gas MS"
      }
    }
  ],
  "ada:analyticalMode": [
    "N \u2014 quantitative point analyses on an instrument 'equipped with five wavelength-dispersive spectrometers and one silicon drift detector energy dispersive spectrometer'; which detector measured which element is not stated"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA NNH09ZDA007O under contract NNM10AA11C (New Frontiers Program) \u2014 acknowledged with the named authors; further grants are listed by person across many laboratories, and none is attributed to the microprobe work",
  "ada:sampleName": "OREX-800045-103 and OREX-800045-107",
  "ada:samplingUnitName": "Labelled at split level: \"Samples OREX-800045-103 and OREX-800045-107 ... Aggregate particles (<1 mm) were mounted in epoxy\" (p.11); particles and points are not labelled, and the data are \"compiled in Supplementary Table 14\" (p.11), not in the archived PDF",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:detectionLimit": "Mg: 0.025 wt%; Fe: 0.025 wt%; Si, K, Na: 0.05 wt%; Ca: 0.005 wt%; Al: 0.02 wt%; Ti: 0.005 wt%; Cr: 0.015 wt%; Mn: 0.008 wt%; other: N \u2014 p.11",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:epmaTAPP-detail-Barnes2025 a schema1:Dataset,
        schema1:Product ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "NASA NNH09ZDA007O under contract NNM10AA11C (New Frontiers Program) — acknowledged with the named authors; further grants are listed by person across many laboratories, and none is attributed to the microprobe work" ] ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "SEM-BSE (JEOL JSM-6510, 15 kV, 3 nA); SEM-EDS (multi-element mapping); SIMS (CAMECA IMS 1270 E7, CRPG); NanoSIMS (K-ALFAA); ICP-MS; MC-ICP-MS; noble gas MS" ] ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Aggregate particles (<1 mm) mounted in epoxy at Université Côte d'Azur; polished; carbon coated (thickness N)" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/epmaTAPP/beamRasterDimensions> ;
            schema1:description "Barnes et al. 2025, Nat. Astron. — variety and origin of accreted materials in Bennu. Protocol 1 of 2: CRPG Nancy, JEOL JXA-8230. Instrument has 5 WDS spectrometers + 1 SDD EDS; per-analyte technique (WDS vs. EDS) not stated. Two analytical sessions: session 1 (no Na, K); session 2 (with Na, K). Counting times are stated as total peak + background combined: 200 ms for minor elements (Al, Ti, Ca, Mn, Cr) and 20 ms for major elements (Mg, Fe, Si). Full primary standard suite stated with element assignments. Full per-element detection limits stated. Matrix correction method not stated. Sample preparation done at Université Côte d'Azur (not at CRPG). Beam current not stated for NHM protocol; 3 nA mentioned in text is for SEM-EDS (different instrument)." ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Centre de Recherches Pétrographiques et Géochimiques (CRPG), Nancy, France" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
                    schema1:identifier "OREX-800045-103; OREX-800045-107 (NASA curatorial IDs, not IGSN)" ;
                    schema1:name "OREX-800045-103 and OREX-800045-107" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ schema1:instrument <https://example.org/epmaTAPP-detail-Barnes2025/instrument/EPMA> ] ;
            ada:combinedResults [ ] ;
            ada:deadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "N — quantitative point analyses on an instrument 'equipped with five wavelength-dispersive spectrometers and one silicon drift detector energy dispersive spectrometer'; which detector measured which element is not stated" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit "Mg: 0.025 wt%; Fe: 0.025 wt%; Si, K, Na: 0.05 wt%; Ca: 0.005 wt%; Al: 0.02 wt%; Ti: 0.005 wt%; Cr: 0.015 wt%; Mn: 0.008 wt%; other: N — p.11" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NASA NNH09ZDA007O under contract NNM10AA11C (New Frontiers Program) — acknowledged with the named authors; further grants are listed by person across many laboratories, and none is attributed to the microprobe work" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:sampleName "OREX-800045-103 and OREX-800045-107" ;
    ada:samplingUnitName "Labelled at split level: \"Samples OREX-800045-103 and OREX-800045-107 ... Aggregate particles (<1 mm) were mounted in epoxy\" (p.11); particles and points are not labelled, and the data are \"compiled in Supplementary Table 14\" (p.11), not in the archived PDF" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" .

<https://example.org/epmaTAPP-detail-Barnes2025/instrument/EPMA> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/epmaTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDiameter> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EPMA" ;
    schema1:name "no value available: schema:name" .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:description "20 kV" ;
    schema1:name "Accelerating Voltage" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/epmaTAPP/acceleratingVoltage> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 20 .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDiameter> a schema1:PropertyValue ;
    schema1:description "all: 1 µm — as above" ;
    schema1:name "Beam Diameter" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDiameter> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1 .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/beamRasterDimensions> a schema1:PropertyValue ;
    schema1:description "carbonates: 5 × 5 µm²; other: N/A — as above" ;
    schema1:name "Beam Raster Dimensions" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/epmaTAPP/beamRasterDimensions> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 5 .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "SEM imaging and multi-element EDS mapping — \"SEM observations were performed on the samples using a JEOL JSM-6510 with 3-nA primary beam at 15 kV. We also performed multi-element EDS mapping (Mg, Si, Fe, Ni, S, Na, Ca and Al) of the different grains\", after which \"Quantitative chemical analyses were performed using a JEOL JXA-8230 electron microprobe\" (p.11)" .


```


### detail example Barnes2025-2
detail instance derived from Barnes+2025 | Cameca SX100 | WDS Point Analysis (NHM London).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "ex": "https://example.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/",
    "prov": "http://www.w3.org/ns/prov#"
  },
  "@id": "ex:epmaTAPP-detail-Barnes2025-2",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "EPMA",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/epmaTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 20,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "20 kV"
                },
                {
                  "@id": "ada:parameter/epmaTAPP/beamDiameter",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/beamDiameter"
                    }
                  ],
                  "schema:name": "Beam Diameter",
                  "schema:value": 1,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "all: 1 µm — as above"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:epmaTAPP-detail-Barnes2025-2/instrument/EPMA"
            }
          ]
        }
      ],
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening"
                }
              ],
              "schema:name": "Pre-Analysis Imaging and Screening",
              "schema:value": "SEM characterisation at the NHM — \"Olivine and pyroxene grains were identified and characterized at the NHM\" and \"Following characterization by SEM/EPMA, an additional carbon coat was added for a total thickness of ~30 nm\" (p.13); additional quantitative data came from a Zeiss EVO 15LS analytical SEM with an Oxford X-Max80 EDS (p.13)"
            }
          ],
          "schema:name": "OREX-501054-0 and OREX-501059-0 (particles P1, P2)",
          "schema:identifier": "OREX-501054-0; OREX-501059-0 (NASA curatorial IDs, not IGSN)"
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Natural History Museum (NHM), London, UK"
      },
      "schema:description": "Barnes et al. 2025, Nat. Astron. — variety and origin of accreted materials in Bennu. Protocol 2 of 2: NHM London, CAMECA SX100. Stated instrument: \"CAMECA SX100 electron microprobe\". Target minerals: olivine and pyroxene (anhydrous silicates). 20 kV, 1 µm focused beam. Beam current not stated for EPMA (3 nA in text refers to SEM-EDS on separate Zeiss EVO instrument). Detection limits ~250 ppm for transition metals. Standards, matrix correction, WDS spectrometer details not stated. Analyte list not given. SEM-EDS at NHM is a separate instrument (Zeiss EVO 15LS + Oxford X-Max80) calibrated at 20 kV, 3 nA. Carbon coat: initial coat for SEM/EPMA (thickness N); additional coat to ~30 nm total was for subsequent SIMS, not EPMA.",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Mounted in resin blocks; polished at NHM London; fragmented during polishing (P1, P2); initial carbon coat for SEM/EPMA (thickness N); additional coat added after for SIMS (total ~30 nm)",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "schema:additionalProperty": [],
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:deadTime": -9999
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NASA NNH09ZDA007O under contract NNM10AA11C (New Frontiers Program) — acknowledged with the named authors; further grants are listed by person across many laboratories, and none is attributed to the microprobe work"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM-EDS (Zeiss EVO 15LS + Oxford X-Max80, 20 kV, 3 nA); NanoSIMS (OU); SIMS (CAMECA ims-1280-HR, Hokkaido); laser fluorination O isotopes (OU)"
      }
    }
  ],
  "ada:analyticalMode": [
    "N — point analyses ('Analyses were performed at 20 kV, using a focused 1-μm beam'); WDS or EDS is not stated, and the list has no value without one"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA NNH09ZDA007O under contract NNM10AA11C (New Frontiers Program) — acknowledged with the named authors; further grants are listed by person across many laboratories, and none is attributed to the microprobe work",
  "ada:sampleName": "OREX-501054-0 and OREX-501059-0 (particles P1, P2)",
  "ada:samplingUnitName": "Labelled: \"The samples OREX-501054-0 and OREX-501059-0 ... fragmented into particles, identified as P1 and P2\" (p.13); the olivine and pyroxene grains within them are not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:detectionLimit": "N — 'Typical detection limits for transition metals were around 250 ppm'; the elements are not named",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    },
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EPMA/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:epmaTAPP-detail-Barnes2025-2",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "EPMA",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/epmaTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 20,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "20 kV"
                },
                {
                  "@id": "ada:parameter/epmaTAPP/beamDiameter",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/beamDiameter"
                    }
                  ],
                  "schema:name": "Beam Diameter",
                  "schema:value": 1,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "all: 1 \u00b5m \u2014 as above"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:epmaTAPP-detail-Barnes2025-2/instrument/EPMA"
            }
          ]
        }
      ],
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening"
                }
              ],
              "schema:name": "Pre-Analysis Imaging and Screening",
              "schema:value": "SEM characterisation at the NHM \u2014 \"Olivine and pyroxene grains were identified and characterized at the NHM\" and \"Following characterization by SEM/EPMA, an additional carbon coat was added for a total thickness of ~30 nm\" (p.13); additional quantitative data came from a Zeiss EVO 15LS analytical SEM with an Oxford X-Max80 EDS (p.13)"
            }
          ],
          "schema:name": "OREX-501054-0 and OREX-501059-0 (particles P1, P2)",
          "schema:identifier": "OREX-501054-0; OREX-501059-0 (NASA curatorial IDs, not IGSN)"
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Natural History Museum (NHM), London, UK"
      },
      "schema:description": "Barnes et al. 2025, Nat. Astron. \u2014 variety and origin of accreted materials in Bennu. Protocol 2 of 2: NHM London, CAMECA SX100. Stated instrument: \"CAMECA SX100 electron microprobe\". Target minerals: olivine and pyroxene (anhydrous silicates). 20 kV, 1 \u00b5m focused beam. Beam current not stated for EPMA (3 nA in text refers to SEM-EDS on separate Zeiss EVO instrument). Detection limits ~250 ppm for transition metals. Standards, matrix correction, WDS spectrometer details not stated. Analyte list not given. SEM-EDS at NHM is a separate instrument (Zeiss EVO 15LS + Oxford X-Max80) calibrated at 20 kV, 3 nA. Carbon coat: initial coat for SEM/EPMA (thickness N); additional coat to ~30 nm total was for subsequent SIMS, not EPMA.",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Mounted in resin blocks; polished at NHM London; fragmented during polishing (P1, P2); initial carbon coat for SEM/EPMA (thickness N); additional coat added after for SIMS (total ~30 nm)",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "schema:additionalProperty": [],
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:deadTime": -9999
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NASA NNH09ZDA007O under contract NNM10AA11C (New Frontiers Program) \u2014 acknowledged with the named authors; further grants are listed by person across many laboratories, and none is attributed to the microprobe work"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM-EDS (Zeiss EVO 15LS + Oxford X-Max80, 20 kV, 3 nA); NanoSIMS (OU); SIMS (CAMECA ims-1280-HR, Hokkaido); laser fluorination O isotopes (OU)"
      }
    }
  ],
  "ada:analyticalMode": [
    "N \u2014 point analyses ('Analyses were performed at 20 kV, using a focused 1-\u03bcm beam'); WDS or EDS is not stated, and the list has no value without one"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA NNH09ZDA007O under contract NNM10AA11C (New Frontiers Program) \u2014 acknowledged with the named authors; further grants are listed by person across many laboratories, and none is attributed to the microprobe work",
  "ada:sampleName": "OREX-501054-0 and OREX-501059-0 (particles P1, P2)",
  "ada:samplingUnitName": "Labelled: \"The samples OREX-501054-0 and OREX-501059-0 ... fragmented into particles, identified as P1 and P2\" (p.13); the olivine and pyroxene grains within them are not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:detectionLimit": "N \u2014 'Typical detection limits for transition metals were around 250 ppm'; the elements are not named",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:epmaTAPP-detail-Barnes2025-2 a schema1:Dataset,
        schema1:Product ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "NASA NNH09ZDA007O under contract NNM10AA11C (New Frontiers Program) — acknowledged with the named authors; further grants are listed by person across many laboratories, and none is attributed to the microprobe work" ] ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "SEM-EDS (Zeiss EVO 15LS + Oxford X-Max80, 20 kV, 3 nA); NanoSIMS (OU); SIMS (CAMECA ims-1280-HR, Hokkaido); laser fluorination O isotopes (OU)" ] ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Mounted in resin blocks; polished at NHM London; fragmented during polishing (P1, P2); initial carbon coat for SEM/EPMA (thickness N); additional coat added after for SIMS (total ~30 nm)" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ] ] ;
            schema1:description "Barnes et al. 2025, Nat. Astron. — variety and origin of accreted materials in Bennu. Protocol 2 of 2: NHM London, CAMECA SX100. Stated instrument: \"CAMECA SX100 electron microprobe\". Target minerals: olivine and pyroxene (anhydrous silicates). 20 kV, 1 µm focused beam. Beam current not stated for EPMA (3 nA in text refers to SEM-EDS on separate Zeiss EVO instrument). Detection limits ~250 ppm for transition metals. Standards, matrix correction, WDS spectrometer details not stated. Analyte list not given. SEM-EDS at NHM is a separate instrument (Zeiss EVO 15LS + Oxford X-Max80) calibrated at 20 kV, 3 nA. Carbon coat: initial coat for SEM/EPMA (thickness N); additional coat to ~30 nm total was for subsequent SIMS, not EPMA." ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Natural History Museum (NHM), London, UK" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
                    schema1:identifier "OREX-501054-0; OREX-501059-0 (NASA curatorial IDs, not IGSN)" ;
                    schema1:name "OREX-501054-0 and OREX-501059-0 (particles P1, P2)" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ schema1:instrument <https://example.org/epmaTAPP-detail-Barnes2025-2/instrument/EPMA> ] ;
            ada:combinedResults [ ] ;
            ada:deadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "N — point analyses ('Analyses were performed at 20 kV, using a focused 1-μm beam'); WDS or EDS is not stated, and the list has no value without one" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit "N — 'Typical detection limits for transition metals were around 250 ppm'; the elements are not named" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NASA NNH09ZDA007O under contract NNM10AA11C (New Frontiers Program) — acknowledged with the named authors; further grants are listed by person across many laboratories, and none is attributed to the microprobe work" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:sampleName "OREX-501054-0 and OREX-501059-0 (particles P1, P2)" ;
    ada:samplingUnitName "Labelled: \"The samples OREX-501054-0 and OREX-501059-0 ... fragmented into particles, identified as P1 and P2\" (p.13); the olivine and pyroxene grains within them are not labelled" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" .

<https://example.org/epmaTAPP-detail-Barnes2025-2/instrument/EPMA> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/epmaTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDiameter> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EPMA" ;
    schema1:name "no value available: schema:name" .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:description "20 kV" ;
    schema1:name "Accelerating Voltage" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/epmaTAPP/acceleratingVoltage> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 20 .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDiameter> a schema1:PropertyValue ;
    schema1:description "all: 1 µm — as above" ;
    schema1:name "Beam Diameter" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDiameter> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1 .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "SEM characterisation at the NHM — \"Olivine and pyroxene grains were identified and characterized at the NHM\" and \"Following characterization by SEM/EPMA, an additional carbon coat was added for a total thickness of ~30 nm\" (p.13); additional quantitative data came from a Zeiss EVO 15LS analytical SEM with an Oxford X-Max80 EDS (p.13)" .


```


### detail example Neuman2025
detail instance derived from Neuman+2025 | WashU St. Louis | WDS Mapping (JEOL JXA-8200).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "ex": "https://example.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/",
    "prov": "http://www.w3.org/ns/prov#"
  },
  "@id": "ex:epmaTAPP-detail-Neuman2025",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "EPMA",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/epmaTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 15,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "15 kV (stage maps and BSE mosaic)"
                },
                {
                  "@id": "ada:parameter/epmaTAPP/beamDiameter",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/beamDiameter"
                    }
                  ],
                  "schema:name": "Beam Diameter",
                  "schema:value": "N/A — mapping-only procedure; map beam under Mapping Beam Diameter",
                  "schema:unitText": "no value available: unnamed property"
                },
                {
                  "@id": "ada:parameter/epmaTAPP/mappingBeamCurrent",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/mappingBeamCurrent"
                    }
                  ],
                  "schema:name": "Mapping Beam Current",
                  "schema:value": 100,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "100 nA probe current (stage maps)"
                },
                {
                  "@id": "ada:parameter/epmaTAPP/mappingBeamDiameter",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/mappingBeamDiameter"
                    }
                  ],
                  "schema:name": "Mapping Beam Diameter",
                  "schema:value": 10,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "10 µm (fixed)"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:epmaTAPP-detail-Neuman2025/instrument/EPMA"
            }
          ]
        },
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "acquisition",
              "schema:name": "JEOL guide-net mapping software (BSE mosaic); N for the WDS stage maps",
              "@type": [
                "schema:SoftwareApplication"
              ]
            },
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "Probe Software CalcImage and Probe for EPMA (full Phi(rho-z) correction at each pixel); MATLAB routines generating 32-bit floating point .tiff quantitative maps; Fiji and MATLAB for stitching; ENVI input image stacks",
              "@type": [
                "schema:SoftwareApplication"
              ]
            }
          ]
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/epmaTAPP/beamRasterDimensions",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/epmaTAPP/beamRasterDimensions"
            }
          ],
          "schema:name": "Beam Raster Dimensions",
          "schema:value": "N/A — stage scan, not beam scan",
          "schema:unitText": "no value available: unnamed property"
        },
        {
          "@id": "ada:parameter/epmaTAPP/stepSizePixelSize",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/epmaTAPP/stepSizePixelSize"
            }
          ],
          "schema:name": "Step Size / Pixel Size",
          "schema:value": 9.5,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "9.5 um (stage maps); ~1.5 um per pixel (BSE mosaic)"
        }
      ],
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening"
                }
              ],
              "schema:name": "Pre-Analysis Imaging and Screening",
              "schema:value": "BSE mosaic: approximately 325 backscattered-electron images collected with the JEOL guide-net mapping software at 15 kV, 2 nA probe current and 70x magnification, stitched with the ImageJ Fiji grid-collection stitching plug-in (Donovan et al., 2021) into a 20k x 5k pixel mosaic at ~1.5 um pixel resolution"
            }
          ],
          "schema:name": "73001,6014-73001,6021"
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Washington University in St. Louis"
      },
      "schema:description": "Multi-pass WDS mapping: two passes per stage map, five elements each; 18 hr per map; 20 x 10^6 fully quantitative analyses across all slides. Recorded in the acquisition-pass proposal (2026-09-08) as the evidence that EPMA partitions the target-species domain across passes.",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Core extruded and dissected in 0.5 cm depth intervals; the remaining material impregnated with epoxy to create a continuous thin section set of the entire core; sections are 50 x 25 mm. Carbon coating N",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "schema:additionalProperty": [],
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:deadTime": -9999,
      "ada:proceduralBlankLevel": "no value available: ada:proceduralBlankLevel"
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/epmaTAPP/mapArea",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/epmaTAPP/mapArea"
        }
      ],
      "schema:name": "Map Area",
      "schema:value": 1,
      "schema:unitText": "no value available: unnamed property",
      "schema:description": "N - not stated directly (1,024 pixels at 9.5 um step corresponds to ~9.7 mm per side)"
    },
    {
      "@id": "ada:parameter/epmaTAPP/mapDimensions",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/epmaTAPP/mapDimensions"
        }
      ],
      "schema:name": "Map Dimensions",
      "schema:value": 1,
      "schema:unitText": "no value available: unnamed property",
      "schema:description": "1,024 x 1,024 pixels per stage map; five stage maps per thin section"
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NASA ANGSA program 80NSSC19K0958 — 'We thank NASA for support of the ANGSA program (Grant 80NSSC19K0958)'"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "BSE mosaic imaging (same JEOL JXA-8200); QEMSCAN (FEI QUANTA 650 FEG-SEM, Univ. Manchester); optical microscopy (Keyence VHX 7000, NASA JSC); micro-XCT (custom NSI instrument, UTCT)",
        "schema:description": "Single-element and RGB composite X-ray maps are compared with BSE and optical image mosaics (reflected light, plane polarized, crossed polars) to discriminate crystalline from glassy phases; an Al-Mg-Fe RGB composite X-ray map is used to discriminate feldspathic (red) from ferromagnesian (green and blue) phases"
      }
    },
    {
      "schema:linkRelationship": "coupledDataset",
      "schema:target": "Ogliore (2025) — 'The quantitative EPMA image data and coregistered image sets are available in Ogliore (2025)'"
    }
  ],
  "ada:analyticalMode": [
    "WDS Mapping — 'five EPMA stage maps were acquired using fixed wavelength-dispersive spectrometers (WDS)'"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA ANGSA program 80NSSC19K0958 — 'We thank NASA for support of the ANGSA program (Grant 80NSSC19K0958)'",
  "ada:sampleName": "73001,6014-73001,6021",
  "ada:samplingUnitName": "Labelled at thin-section level: \"The 73001,6014–73001,6021 samples are 50 × 25 mm continuous thin sections\" (p.6), e.g. the \"73001,6019\" X-ray map (p.11); every map pixel is an analysis, so the section — the acquisition area — is the unit named",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:detectionLimit": "all: 0.1–0.2 element wt% — 'for all elements in this map set'",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    },
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EPMA/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:epmaTAPP-detail-Neuman2025",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "EPMA",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/epmaTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 15,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "15 kV (stage maps and BSE mosaic)"
                },
                {
                  "@id": "ada:parameter/epmaTAPP/beamDiameter",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/beamDiameter"
                    }
                  ],
                  "schema:name": "Beam Diameter",
                  "schema:value": "N/A \u2014 mapping-only procedure; map beam under Mapping Beam Diameter",
                  "schema:unitText": "no value available: unnamed property"
                },
                {
                  "@id": "ada:parameter/epmaTAPP/mappingBeamCurrent",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/mappingBeamCurrent"
                    }
                  ],
                  "schema:name": "Mapping Beam Current",
                  "schema:value": 100,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "100 nA probe current (stage maps)"
                },
                {
                  "@id": "ada:parameter/epmaTAPP/mappingBeamDiameter",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/epmaTAPP/mappingBeamDiameter"
                    }
                  ],
                  "schema:name": "Mapping Beam Diameter",
                  "schema:value": 10,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "10 \u00b5m (fixed)"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:epmaTAPP-detail-Neuman2025/instrument/EPMA"
            }
          ]
        },
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "acquisition",
              "schema:name": "JEOL guide-net mapping software (BSE mosaic); N for the WDS stage maps",
              "@type": [
                "schema:SoftwareApplication"
              ]
            },
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "Probe Software CalcImage and Probe for EPMA (full Phi(rho-z) correction at each pixel); MATLAB routines generating 32-bit floating point .tiff quantitative maps; Fiji and MATLAB for stitching; ENVI input image stacks",
              "@type": [
                "schema:SoftwareApplication"
              ]
            }
          ]
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/epmaTAPP/beamRasterDimensions",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/epmaTAPP/beamRasterDimensions"
            }
          ],
          "schema:name": "Beam Raster Dimensions",
          "schema:value": "N/A \u2014 stage scan, not beam scan",
          "schema:unitText": "no value available: unnamed property"
        },
        {
          "@id": "ada:parameter/epmaTAPP/stepSizePixelSize",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/epmaTAPP/stepSizePixelSize"
            }
          ],
          "schema:name": "Step Size / Pixel Size",
          "schema:value": 9.5,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "9.5 um (stage maps); ~1.5 um per pixel (BSE mosaic)"
        }
      ],
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening"
                }
              ],
              "schema:name": "Pre-Analysis Imaging and Screening",
              "schema:value": "BSE mosaic: approximately 325 backscattered-electron images collected with the JEOL guide-net mapping software at 15 kV, 2 nA probe current and 70x magnification, stitched with the ImageJ Fiji grid-collection stitching plug-in (Donovan et al., 2021) into a 20k x 5k pixel mosaic at ~1.5 um pixel resolution"
            }
          ],
          "schema:name": "73001,6014-73001,6021"
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Washington University in St. Louis"
      },
      "schema:description": "Multi-pass WDS mapping: two passes per stage map, five elements each; 18 hr per map; 20 x 10^6 fully quantitative analyses across all slides. Recorded in the acquisition-pass proposal (2026-09-08) as the evidence that EPMA partitions the target-species domain across passes.",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Core extruded and dissected in 0.5 cm depth intervals; the remaining material impregnated with epoxy to create a continuous thin section set of the entire core; sections are 50 x 25 mm. Carbon coating N",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "schema:additionalProperty": [],
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:deadTime": -9999,
      "ada:proceduralBlankLevel": "no value available: ada:proceduralBlankLevel"
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/epmaTAPP/mapArea",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/epmaTAPP/mapArea"
        }
      ],
      "schema:name": "Map Area",
      "schema:value": 1,
      "schema:unitText": "no value available: unnamed property",
      "schema:description": "N - not stated directly (1,024 pixels at 9.5 um step corresponds to ~9.7 mm per side)"
    },
    {
      "@id": "ada:parameter/epmaTAPP/mapDimensions",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/epmaTAPP/mapDimensions"
        }
      ],
      "schema:name": "Map Dimensions",
      "schema:value": 1,
      "schema:unitText": "no value available: unnamed property",
      "schema:description": "1,024 x 1,024 pixels per stage map; five stage maps per thin section"
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NASA ANGSA program 80NSSC19K0958 \u2014 'We thank NASA for support of the ANGSA program (Grant 80NSSC19K0958)'"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "BSE mosaic imaging (same JEOL JXA-8200); QEMSCAN (FEI QUANTA 650 FEG-SEM, Univ. Manchester); optical microscopy (Keyence VHX 7000, NASA JSC); micro-XCT (custom NSI instrument, UTCT)",
        "schema:description": "Single-element and RGB composite X-ray maps are compared with BSE and optical image mosaics (reflected light, plane polarized, crossed polars) to discriminate crystalline from glassy phases; an Al-Mg-Fe RGB composite X-ray map is used to discriminate feldspathic (red) from ferromagnesian (green and blue) phases"
      }
    },
    {
      "schema:linkRelationship": "coupledDataset",
      "schema:target": "Ogliore (2025) \u2014 'The quantitative EPMA image data and coregistered image sets are available in Ogliore (2025)'"
    }
  ],
  "ada:analyticalMode": [
    "WDS Mapping \u2014 'five EPMA stage maps were acquired using fixed wavelength-dispersive spectrometers (WDS)'"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA ANGSA program 80NSSC19K0958 \u2014 'We thank NASA for support of the ANGSA program (Grant 80NSSC19K0958)'",
  "ada:sampleName": "73001,6014-73001,6021",
  "ada:samplingUnitName": "Labelled at thin-section level: \"The 73001,6014\u201373001,6021 samples are 50 \u00d7 25 mm continuous thin sections\" (p.6), e.g. the \"73001,6019\" X-ray map (p.11); every map pixel is an analysis, so the section \u2014 the acquisition area \u2014 is the unit named",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:detectionLimit": "all: 0.1\u20130.2 element wt% \u2014 'for all elements in this map set'",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999
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

ex:epmaTAPP-detail-Neuman2025 a schema1:Dataset,
        schema1:Product ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/epmaTAPP/mapArea>,
        <https://ada.astromat.org/metadata/parameter/epmaTAPP/mapDimensions> ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "NASA ANGSA program 80NSSC19K0958 — 'We thank NASA for support of the ANGSA program (Grant 80NSSC19K0958)'" ] ;
    schema1:relatedLink [ schema1:linkRelationship "coupledDataset" ;
            schema1:target "Ogliore (2025) — 'The quantitative EPMA image data and coregistered image sets are available in Ogliore (2025)'" ],
        [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "Single-element and RGB composite X-ray maps are compared with BSE and optical image mosaics (reflected light, plane polarized, crossed polars) to discriminate crystalline from glassy phases; an Al-Mg-Fe RGB composite X-ray map is used to discriminate feldspathic (red) from ferromagnesian (green and blue) phases" ;
                    schema1:name "BSE mosaic imaging (same JEOL JXA-8200); QEMSCAN (FEI QUANTA 650 FEG-SEM, Univ. Manchester); optical microscopy (Keyence VHX 7000, NASA JSC); micro-XCT (custom NSI instrument, UTCT)" ] ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Core extruded and dissected in 0.5 cm depth intervals; the remaining material impregnated with epoxy to create a continuous thin section set of the entire core; sections are 50 x 25 mm. Carbon coating N" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/epmaTAPP/beamRasterDimensions>,
                <https://ada.astromat.org/metadata/parameter/epmaTAPP/stepSizePixelSize> ;
            schema1:description "Multi-pass WDS mapping: two passes per stage map, five elements each; 18 hr per map; 20 x 10^6 fully quantitative analyses across all slides. Recorded in the acquisition-pass proposal (2026-09-08) as the evidence that EPMA partitions the target-species domain across passes." ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Washington University in St. Louis" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
                    schema1:name "73001,6014-73001,6021" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ schema1:instrument <https://example.org/epmaTAPP-detail-Neuman2025/instrument/EPMA> ],
                [ bios:computationalTool [ a schema1:SoftwareApplication ;
                            schema1:name "Probe Software CalcImage and Probe for EPMA (full Phi(rho-z) correction at each pixel); MATLAB routines generating 32-bit floating point .tiff quantitative maps; Fiji and MATLAB for stitching; ENVI input image stacks" ;
                            ada:toolRole "dataReduction" ],
                        [ a schema1:SoftwareApplication ;
                            schema1:name "JEOL guide-net mapping software (BSE mosaic); N for the WDS stage maps" ;
                            ada:toolRole "acquisition" ] ] ;
            ada:deadTime -9999 ;
            ada:proceduralBlankLevel "no value available: ada:proceduralBlankLevel" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "WDS Mapping — 'five EPMA stage maps were acquired using fixed wavelength-dispersive spectrometers (WDS)'" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit "all: 0.1–0.2 element wt% — 'for all elements in this map set'" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NASA ANGSA program 80NSSC19K0958 — 'We thank NASA for support of the ANGSA program (Grant 80NSSC19K0958)'" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "73001,6014-73001,6021" ;
    ada:samplingUnitName "Labelled at thin-section level: \"The 73001,6014–73001,6021 samples are 50 × 25 mm continuous thin sections\" (p.6), e.g. the \"73001,6019\" X-ray map (p.11); every map pixel is an analysis, so the section — the acquisition area — is the unit named" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" .

<https://example.org/epmaTAPP-detail-Neuman2025/instrument/EPMA> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/epmaTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDiameter>,
        <https://ada.astromat.org/metadata/parameter/epmaTAPP/mappingBeamCurrent>,
        <https://ada.astromat.org/metadata/parameter/epmaTAPP/mappingBeamDiameter> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EPMA" ;
    schema1:name "no value available: schema:name" .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:description "15 kV (stage maps and BSE mosaic)" ;
    schema1:name "Accelerating Voltage" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/epmaTAPP/acceleratingVoltage> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 15 .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDiameter> a schema1:PropertyValue ;
    schema1:name "Beam Diameter" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDiameter> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value "N/A — mapping-only procedure; map beam under Mapping Beam Diameter" .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/beamRasterDimensions> a schema1:PropertyValue ;
    schema1:name "Beam Raster Dimensions" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/epmaTAPP/beamRasterDimensions> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value "N/A — stage scan, not beam scan" .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/mapArea> a schema1:PropertyValue ;
    schema1:description "N - not stated directly (1,024 pixels at 9.5 um step corresponds to ~9.7 mm per side)" ;
    schema1:name "Map Area" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/epmaTAPP/mapArea> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1 .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/mapDimensions> a schema1:PropertyValue ;
    schema1:description "1,024 x 1,024 pixels per stage map; five stage maps per thin section" ;
    schema1:name "Map Dimensions" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/epmaTAPP/mapDimensions> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1 .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/mappingBeamCurrent> a schema1:PropertyValue ;
    schema1:description "100 nA probe current (stage maps)" ;
    schema1:name "Mapping Beam Current" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/epmaTAPP/mappingBeamCurrent> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 100 .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/mappingBeamDiameter> a schema1:PropertyValue ;
    schema1:description "10 µm (fixed)" ;
    schema1:name "Mapping Beam Diameter" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/epmaTAPP/mappingBeamDiameter> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 10 .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/stepSizePixelSize> a schema1:PropertyValue ;
    schema1:description "9.5 um (stage maps); ~1.5 um per pixel (BSE mosaic)" ;
    schema1:name "Step Size / Pixel Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/epmaTAPP/stepSizePixelSize> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 9.5e+00 .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "BSE mosaic: approximately 325 backscattered-electron images collected with the JEOL guide-net mapping software at 15 kV, 2 nA probe current and 70x magnification, stitched with the ImageJ Fiji grid-collection stitching plug-in (Donovan et al., 2021) into a 20k x 5k pixel mosaic at ~1.5 um pixel resolution" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: EPMA/EPMA Analysis Detail
description: Dataset-level analysis-instance detail for EPMA/EPMA, reusing CDIF/schema.org
  slots on the schema:Dataset root.
allOf:
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/AnalysisIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/calibrationFactor/schema.yaml#/$defs/AnalysisIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/aggregation/schema.yaml#/$defs/AnalysisIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/compositionQC/schema.yaml#/$defs/AnalysisIdentification
- type: object
  properties:
    prov:wasGeneratedBy:
      type: array
      items:
        type: object
        properties:
          prov:used:
            type: array
            items:
              type: object
              allOf:
              - if:
                  required:
                  - schema:instrument
                then:
                  properties:
                    schema:instrument:
                      type: array
                      items:
                        allOf:
                        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/instrument/schema.yaml
                        - type: object
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
                                schema:additionalProperty:
                                  type: array
                                  items:
                                    anyOf:
                                    - title: Accelerating Voltage
                                      description: Electron beam accelerating voltage
                                        in kilovolts (kV). Justify any deviation from
                                        the standard operating voltage.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/epmaTAPP/acceleratingVoltage
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/epmaTAPP/acceleratingVoltage
                                        schema:name:
                                          const: Accelerating Voltage
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
                                    - title: Beam Diameter
                                      description: Diameter of the electron beam in
                                        micrometers. 0 indicates a fully focused beam.
                                        Document defocused diameter when used to minimize
                                        beam damage or improve spatial averaging for
                                        beam-sensitive phases.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/epmaTAPP/beamDiameter
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/epmaTAPP/beamDiameter
                                        schema:name:
                                          const: Beam Diameter
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
                                    - title: Mapping Beam Current
                                      description: Probe current in nanoamperes (nA)
                                        used during X-ray mapping.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/epmaTAPP/mappingBeamCurrent
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/epmaTAPP/mappingBeamCurrent
                                        schema:name:
                                          const: Mapping Beam Current
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
                                    - title: Mapping Beam Diameter
                                      description: Diameter of the electron beam in
                                        micrometres during X-ray mapping. 0 indicates
                                        a fully focused beam.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/epmaTAPP/mappingBeamDiameter
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/epmaTAPP/mappingBeamDiameter
                                        schema:name:
                                          const: Mapping Beam Diameter
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
                                  allOf:
                                  - contains:
                                      title: Accelerating Voltage
                                      description: Electron beam accelerating voltage
                                        in kilovolts (kV). Justify any deviation from
                                        the standard operating voltage.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/epmaTAPP/acceleratingVoltage
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/epmaTAPP/acceleratingVoltage
                                        schema:name:
                                          const: Accelerating Voltage
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
                                    minContains: 0
                                    maxContains: 1
                                  - contains:
                                      title: Beam Diameter
                                      description: Diameter of the electron beam in
                                        micrometers. 0 indicates a fully focused beam.
                                        Document defocused diameter when used to minimize
                                        beam damage or improve spatial averaging for
                                        beam-sensitive phases.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/epmaTAPP/beamDiameter
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/epmaTAPP/beamDiameter
                                        schema:name:
                                          const: Beam Diameter
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
                                    minContains: 0
                                    maxContains: 1
                                  - contains:
                                      title: Mapping Beam Current
                                      description: Probe current in nanoamperes (nA)
                                        used during X-ray mapping.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/epmaTAPP/mappingBeamCurrent
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/epmaTAPP/mappingBeamCurrent
                                        schema:name:
                                          const: Mapping Beam Current
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
                                    minContains: 0
                                    maxContains: 1
                                  - contains:
                                      title: Mapping Beam Diameter
                                      description: Diameter of the electron beam in
                                        micrometres during X-ray mapping. 0 indicates
                                        a fully focused beam.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/epmaTAPP/mappingBeamDiameter
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/epmaTAPP/mappingBeamDiameter
                                        schema:name:
                                          const: Mapping Beam Diameter
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
                                    minContains: 0
                                    maxContains: 1
                      allOf:
                      - contains:
                          properties:
                            schema:additionalType:
                              contains:
                                const: EPMA
                              schema:inDefinedTermSet: ada:vocab/instrumentType
                          required:
                          - schema:additionalType
          schema:additionalProperty:
            type: array
            items:
              anyOf:
              - title: Beam Damage Minimization
                description: Measures taken to minimize beam damage, particularly
                  volatilization or migration of Na, K, F, and Cl in hydrous minerals,
                  glasses, feldspars, phosphates, and carbonates. Document approach,
                  beam conditions used, and phases for which it was applied.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/epmaTAPP/beamDamageMinimization
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/epmaTAPP/beamDamageMinimization
                  schema:name:
                    const: Beam Damage Minimization
                  schema:value:
                    type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              - title: Beam Raster Dimensions
                description: "Dimensions of the small area over which the beam is
                  rastered at a single analysis point, reported as width \xD7 height
                  in \xB5m. Applicable when Beam Mode = Rastered; defines the effective
                  spatial footprint of the measurement. Not applicable when mapping."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/epmaTAPP/beamRasterDimensions
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/epmaTAPP/beamRasterDimensions
                  schema:name:
                    const: Beam Raster Dimensions
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
              - title: Drift Correction
                description: Method used to monitor and correct for instrument drift
                  (beam current drift, spectrometer drift) during the analytical session.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/epmaTAPP/driftCorrection
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/epmaTAPP/driftCorrection
                  schema:name:
                    const: Drift Correction
                  schema:value:
                    type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              - title: EDS Live Time per Point or Pixel
                description: EDS spectral acquisition live time per analysis point
                  or per pixel in seconds.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/epmaTAPP/edsLiveTimePerPointOrPixel
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/epmaTAPP/edsLiveTimePerPointOrPixel
                  schema:name:
                    const: EDS Live Time per Point or Pixel
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
              - title: Halogen Correction on Oxygen
                description: Whether oxygen content was adjusted to account for halogen
                  substitution (F and/or Cl replacing OH) in halogen-bearing phases
                  such as apatite, amphibole, and mica, where oxygen is calculated
                  by stoichiometry.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/epmaTAPP/halogenCorrectionOnOxygen
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/epmaTAPP/halogenCorrectionOnOxygen
                  schema:name:
                    const: Halogen Correction on Oxygen
                  schema:value:
                    type: string
                  schema:inDefinedTermSet:
                    const:
                      '@id': ada:vocab/halogen-correction-on-oxygen
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              - title: Step Size / Pixel Size
                description: Distance between adjacent measurement points in the X-ray
                  map in micrometers, defining the spatial resolution. Report both
                  X and Y step if they differ.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/epmaTAPP/stepSizePixelSize
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/epmaTAPP/stepSizePixelSize
                  schema:name:
                    const: Step Size / Pixel Size
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
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Analysis_samplingUnitSelectionCriteria
            allOf:
            - contains:
                title: Beam Damage Minimization
                description: Measures taken to minimize beam damage, particularly
                  volatilization or migration of Na, K, F, and Cl in hydrous minerals,
                  glasses, feldspars, phosphates, and carbonates. Document approach,
                  beam conditions used, and phases for which it was applied.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/epmaTAPP/beamDamageMinimization
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/epmaTAPP/beamDamageMinimization
                  schema:name:
                    const: Beam Damage Minimization
                  schema:value:
                    type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              minContains: 0
              maxContains: 1
            - contains:
                title: Beam Raster Dimensions
                description: "Dimensions of the small area over which the beam is
                  rastered at a single analysis point, reported as width \xD7 height
                  in \xB5m. Applicable when Beam Mode = Rastered; defines the effective
                  spatial footprint of the measurement. Not applicable when mapping."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/epmaTAPP/beamRasterDimensions
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/epmaTAPP/beamRasterDimensions
                  schema:name:
                    const: Beam Raster Dimensions
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
              minContains: 0
              maxContains: 1
            - contains:
                title: Drift Correction
                description: Method used to monitor and correct for instrument drift
                  (beam current drift, spectrometer drift) during the analytical session.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/epmaTAPP/driftCorrection
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/epmaTAPP/driftCorrection
                  schema:name:
                    const: Drift Correction
                  schema:value:
                    type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              minContains: 0
              maxContains: 1
            - contains:
                title: EDS Live Time per Point or Pixel
                description: EDS spectral acquisition live time per analysis point
                  or per pixel in seconds.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/epmaTAPP/edsLiveTimePerPointOrPixel
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/epmaTAPP/edsLiveTimePerPointOrPixel
                  schema:name:
                    const: EDS Live Time per Point or Pixel
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
              minContains: 0
              maxContains: 1
            - contains:
                title: Halogen Correction on Oxygen
                description: Whether oxygen content was adjusted to account for halogen
                  substitution (F and/or Cl replacing OH) in halogen-bearing phases
                  such as apatite, amphibole, and mica, where oxygen is calculated
                  by stoichiometry.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/epmaTAPP/halogenCorrectionOnOxygen
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/epmaTAPP/halogenCorrectionOnOxygen
                  schema:name:
                    const: Halogen Correction on Oxygen
                  schema:value:
                    type: string
                  schema:inDefinedTermSet:
                    const:
                      '@id': ada:vocab/halogen-correction-on-oxygen
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              minContains: 0
              maxContains: 1
            - contains:
                title: Step Size / Pixel Size
                description: Distance between adjacent measurement points in the X-ray
                  map in micrometers, defining the spatial resolution. Report both
                  X and Y step if they differ.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/epmaTAPP/stepSizePixelSize
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/epmaTAPP/stepSizePixelSize
                  schema:name:
                    const: Step Size / Pixel Size
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
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Analysis_samplingUnitSelectionCriteria
              minContains: 0
              maxContains: 1
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
                        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Analysis_preAnalysisImagingAndScreening
                      allOf:
                      - contains:
                          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Analysis_preAnalysisImagingAndScreening
                        minContains: 0
                        maxContains: 1
          ada:deadTime:
            description: "Percent dead time reported by the EDS detector during the
              session \u2014 the fraction of total acquisition time the detector spent
              processing rather than counting. This field documents the resulting
              percentage as a session QC metric. Unlike WDS dead time (see WDS Dead
              Time Correction), no user-selectable correction algorithm is required."
            anyOf:
            - type: number
            - type: string
          ada:proceduralBlankLevel:
            description: "The measured level of the analytical blank in the session,
              and \u2014 where the reported quantity is a ratio \u2014 its composition,
              since a blank subtracted from a ratio biases the result unless its own
              composition is known. Companion to the blank correction method."
            type: string
          schema:actionProcess:
            type: object
            properties:
              schema:step:
                type: array
                items:
                  type: object
                  allOf:
                  - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/WorkflowStep
                  - if:
                      properties:
                        schema:name:
                          const: Data processing
                      required:
                      - schema:name
                    then:
                      properties:
                        schema:additionalProperty:
                          type: array
                          items:
                            $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Analysis_constantsReferenceValues
                          allOf:
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Analysis_constantsReferenceValues
                            minContains: 0
                            maxContains: 1
                allOf:
                - contains:
                    properties:
                      schema:name:
                        const: Data processing
                    required:
                    - schema:name
        required:
        - ada:deadTime
        - ada:proceduralBlankLevel
      title: Analysis Events
    dqv:hasQualityMeasurement:
      type: array
      items:
        type: object
        allOf:
        - if:
            properties:
              dqv:isMeasurementOf:
                const: Analytical Accuracy
            required:
            - dqv:isMeasurementOf
          then:
            properties:
              dqv:value:
                description: Offset between measured and accepted reference values
                  for secondary standards, expressed as percent relative bias. Include
                  reference material, reference value source, and the measured value.
                anyOf:
                - type: string
                - type: array
                  items:
                    type: string
            required:
            - dqv:value
        - if:
            properties:
              dqv:isMeasurementOf:
                const: Analytical Precision
            required:
            - dqv:isMeasurementOf
          then:
            properties:
              dqv:value:
                description: Precision of repeated measurements on the same or equivalent
                  reference material, expressed as 1-sigma relative standard deviation
                  (%). State whether the repeats were made within one session (repeatability)
                  or across sessions (intermediate precision, in ISO 5725 terms).
                  Include reference material name, number of analyses (n), and the
                  measured value.
                anyOf:
                - type: string
                - type: array
                  items:
                    type: string
            required:
            - dqv:value
      allOf:
      - contains:
          properties:
            dqv:isMeasurementOf:
              const: Analytical Accuracy
          required:
          - dqv:isMeasurementOf
      - contains:
          properties:
            dqv:isMeasurementOf:
              const: Analytical Precision
          required:
          - dqv:isMeasurementOf
      title: Quality Measurements
    schema:additionalProperty:
      type: array
      items:
        anyOf:
        - title: Map Area
          description: "Physical extent of the mapped region, given either as width
            \xD7 height in \xB5m or as a total area in \xB5m\xB2 or mm\xB2, and equal
            to (map width in pixels \xD7 step size) \xD7 (map height in pixels \xD7
            step size). Complements the map's pixel-grid dimensions by recording the
            physical scale of the mapped region."
          type: object
          properties:
            '@id':
              const: ada:parameter/epmaTAPP/mapArea
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/epmaTAPP/mapArea
            schema:name:
              const: Map Area
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
        - title: Map Dimensions
          description: Number of pixels in the X-ray map in the X and Y directions.
            Based on the area of interest and selected step size.
          type: object
          properties:
            '@id':
              const: ada:parameter/epmaTAPP/mapDimensions
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/epmaTAPP/mapDimensions
            schema:name:
              const: Map Dimensions
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
      allOf:
      - contains:
          title: Map Area
          description: "Physical extent of the mapped region, given either as width
            \xD7 height in \xB5m or as a total area in \xB5m\xB2 or mm\xB2, and equal
            to (map width in pixels \xD7 step size) \xD7 (map height in pixels \xD7
            step size). Complements the map's pixel-grid dimensions by recording the
            physical scale of the mapped region."
          type: object
          properties:
            '@id':
              const: ada:parameter/epmaTAPP/mapArea
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/epmaTAPP/mapArea
            schema:name:
              const: Map Area
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
        minContains: 0
        maxContains: 1
      - contains:
          title: Map Dimensions
          description: Number of pixels in the X-ray map in the X and Y directions.
            Based on the area of interest and selected step size.
          type: object
          properties:
            '@id':
              const: ada:parameter/epmaTAPP/mapDimensions
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/epmaTAPP/mapDimensions
            schema:name:
              const: Map Dimensions
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
        minContains: 0
        maxContains: 1
      title: Additional Properties
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
        - title: Target Material of Sampling Unit
          description: The entry in Target Material that the sampling unit belongs
            to, which links the unit to the point-analysis conditions registered for
            that material.
          type: object
          properties:
            '@id':
              const: ada:parameter/epmaTAPP/targetMaterialOfSamplingUnit
            '@type':
              const:
              - schema:PropertyValue
              - cdi:InstanceVariable
            schema:propertyID:
              const:
              - '@id': ada:parameter/epmaTAPP/targetMaterialOfSamplingUnit
            schema:name:
              const: Target Material of Sampling Unit
            schema:value:
              type: string
          required:
          - '@id'
          - '@type'
          - schema:propertyID
          - schema:name
          - schema:value
      allOf:
      - contains:
          title: Target Material of Sampling Unit
          description: The entry in Target Material that the sampling unit belongs
            to, which links the unit to the point-analysis conditions registered for
            that material.
          type: object
          properties:
            '@id':
              const: ada:parameter/epmaTAPP/targetMaterialOfSamplingUnit
            '@type':
              const:
              - schema:PropertyValue
              - cdi:InstanceVariable
            schema:propertyID:
              const:
              - '@id': ada:parameter/epmaTAPP/targetMaterialOfSamplingUnit
            schema:name:
              const: Target Material of Sampling Unit
            schema:value:
              type: string
          required:
          - '@id'
          - '@type'
          - schema:propertyID
          - schema:name
          - schema:value
        minContains: 0
        maxContains: 1
      title: Measured Variables
x-bblocks-metadata:
  itemIdentifier: ogch.techniqueProfile.geochemProfile.EPMA.detail
  register: https://amds-ldeo.github.io/geochemBuildingBlocks/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-11-09'

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EPMA/detail/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EPMA/detail/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "ada": "https://ada.astromat.org/metadata/",
    "bios": "https://bioschemas.org/",
    "prov": "http://www.w3.org/ns/prov#",
    "schema": "http://schema.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "csvw": "http://www.w3.org/ns/csvw#",
    "spdx": "http://spdx.org/rdf/terms#",
    "nxs": "https://manual.nexusformat.org/classes/",
    "dcterms": "http://purl.org/dc/terms/",
    "geosparql": "http://www.opengis.net/ont/geosparql#",
    "dqv": "http://www.w3.org/ns/dqv#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "wd": "https://www.wikidata.org/entity/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EPMA/detail/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/EPMA/detail`

