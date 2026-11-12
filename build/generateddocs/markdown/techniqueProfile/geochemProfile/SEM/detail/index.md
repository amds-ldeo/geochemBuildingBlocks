
# SEM Analysis Detail (Schema)

`ogch.techniqueProfile.geochemProfile.SEM.detail` *v0.1*

Dataset-level analysis-instance detail for SEM (superset), reusing CDIF/schema.org slots on the schema:Dataset root.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### detail example Garvie2008
detail instance derived from Garvie et al. 2008 | Tagish Lake (C2) nanoglobules | SE Imaging (FEI Nova 200 NanoLab).
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
  "@id": "ex:semTAPP-detail-Garvie2008",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:instrument": [
        {
          "schema:additionalType": [
            "SEM",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/semTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/semTAPP/acceleratingVoltage"
                }
              ],
              "schema:name": "Accelerating Voltage",
              "schema:value": 500,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "500 V; 1 kV; 5 kV"
            },
            {
              "@id": "ada:parameter/semTAPP/mappingBeamCurrent",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/semTAPP/mappingBeamCurrent"
                }
              ],
              "schema:name": "Mapping Beam Current",
              "schema:value": 70,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "70 fA (500 V); 1.4 pA (1 kV); 98 pA (5 kV)"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:semTAPP-detail-Garvie2008/instrument/SEM"
        }
      ],
      "ada:combinedResults": [
        {}
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
              "schema:value": "N — the imaging this procedure performs is its own measurement, not a screening step before it; the paper describes no prior characterisation used to locate the units"
            }
          ],
          "schema:name": "no value available: schema:name"
        }
      ],
      "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/semTAPP/workingDistance",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semTAPP/workingDistance"
            }
          ],
          "schema:name": "Working Distance",
          "schema:value": 0.5,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "0.5–5.4 mm"
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "School of Earth and Space Exploration / School of Materials, Arizona State University"
      },
      "schema:description": "Sample imaged without coating; initial ~5% beam-induced shrinkage observed upon first e-beam exposure; sample stable thereafter; focusing performed away from particles of interest to minimise beam exposure",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "HCl and HF acid dissolution residue from pristine Tagish Lake pieces; deposited on lacey C TEM grid attached to Al-SEM stub; uncoated",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          },
          {
            "schema:name": "Ion milling",
            "schema:position": 3,
            "schema:description": "no value available: schema:description",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NASA NNG06GE37G (LAJG); NASA NNG06GF08G (PRB)"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "FIB milling and TEM cross-section preparation (same instrument)"
      }
    }
  ],
  "ada:analyticalMode": [
    "SE Imaging"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA NNG06GE37G (LAJG); NASA NNG06GF08G (PRB)",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only — the Tagish Lake \"carbonaceous residue was attached to an Al-SEM stub\" (p.2); globules are identified by figure panel (\"A) Single sphere, B) three coalesced spheres, C) cluster of spheres …\", Fig. 1, p.2), not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-detail-Garvie2008",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:instrument": [
        {
          "schema:additionalType": [
            "SEM",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/semTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/semTAPP/acceleratingVoltage"
                }
              ],
              "schema:name": "Accelerating Voltage",
              "schema:value": 500,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "500 V; 1 kV; 5 kV"
            },
            {
              "@id": "ada:parameter/semTAPP/mappingBeamCurrent",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/semTAPP/mappingBeamCurrent"
                }
              ],
              "schema:name": "Mapping Beam Current",
              "schema:value": 70,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "70 fA (500 V); 1.4 pA (1 kV); 98 pA (5 kV)"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:semTAPP-detail-Garvie2008/instrument/SEM"
        }
      ],
      "ada:combinedResults": [
        {}
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
              "schema:value": "N \u2014 the imaging this procedure performs is its own measurement, not a screening step before it; the paper describes no prior characterisation used to locate the units"
            }
          ],
          "schema:name": "no value available: schema:name"
        }
      ],
      "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/semTAPP/workingDistance",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semTAPP/workingDistance"
            }
          ],
          "schema:name": "Working Distance",
          "schema:value": 0.5,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "0.5\u20135.4 mm"
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "School of Earth and Space Exploration / School of Materials, Arizona State University"
      },
      "schema:description": "Sample imaged without coating; initial ~5% beam-induced shrinkage observed upon first e-beam exposure; sample stable thereafter; focusing performed away from particles of interest to minimise beam exposure",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "HCl and HF acid dissolution residue from pristine Tagish Lake pieces; deposited on lacey C TEM grid attached to Al-SEM stub; uncoated",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          },
          {
            "schema:name": "Ion milling",
            "schema:position": 3,
            "schema:description": "no value available: schema:description",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NASA NNG06GE37G (LAJG); NASA NNG06GF08G (PRB)"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "FIB milling and TEM cross-section preparation (same instrument)"
      }
    }
  ],
  "ada:analyticalMode": [
    "SE Imaging"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA NNG06GE37G (LAJG); NASA NNG06GF08G (PRB)",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only \u2014 the Tagish Lake \"carbonaceous residue was attached to an Al-SEM stub\" (p.2); globules are identified by figure panel (\"A) Single sphere, B) three coalesced spheres, C) cluster of spheres \u2026\", Fig. 1, p.2), not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix wd: <https://www.wikidata.org/entity/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:semTAPP-detail-Garvie2008 a schema1:Dataset,
        schema1:Product ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "NASA NNG06GE37G (LAJG); NASA NNG06GF08G (PRB)" ] ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "FIB milling and TEM cross-section preparation (same instrument)" ] ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "no value available: schema:description" ;
                            schema1:name "Ion milling" ;
                            schema1:position 3 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "HCl and HF acid dissolution residue from pristine Tagish Lake pieces; deposited on lacey C TEM grid attached to Al-SEM stub; uncoated" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semTAPP/workingDistance> ;
            schema1:description "Sample imaged without coating; initial ~5% beam-induced shrinkage observed upon first e-beam exposure; sample stable thereafter; focusing performed away from particles of interest to minimise beam exposure" ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:instrument <https://example.org/semTAPP-detail-Garvie2008/instrument/SEM> ;
            schema1:location [ a schema1:Place ;
                    schema1:name "School of Earth and Space Exploration / School of Materials, Arizona State University" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
                    schema1:name "no value available: schema:name" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            ada:combinedResults [ ] ;
            ada:edsDeadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "SE Imaging" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NASA NNG06GE37G (LAJG); NASA NNG06GF08G (PRB)" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimensions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Sample name only — the Tagish Lake \"carbonaceous residue was attached to an Al-SEM stub\" (p.2); globules are identified by figure panel (\"A) Single sphere, B) three coalesced spheres, C) cluster of spheres …\", Fig. 1, p.2), not labelled" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "no value available: ada:voxelSize" .

<https://example.org/semTAPP-detail-Garvie2008/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/semTAPP/mappingBeamCurrent> ;
    schema1:additionalType wd:Q3099911,
        "SEM" ;
    schema1:name "no value available: schema:name" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "N — the imaging this procedure performs is its own measurement, not a screening step before it; the paper describes no prior characterisation used to locate the units" .

<https://ada.astromat.org/metadata/parameter/semTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:description "500 V; 1 kV; 5 kV" ;
    schema1:name "Accelerating Voltage" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/acceleratingVoltage> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 500 .

<https://ada.astromat.org/metadata/parameter/semTAPP/mappingBeamCurrent> a schema1:PropertyValue ;
    schema1:description "70 fA (500 V); 1.4 pA (1 kV); 98 pA (5 kV)" ;
    schema1:name "Mapping Beam Current" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/mappingBeamCurrent> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 70 .

<https://ada.astromat.org/metadata/parameter/semTAPP/workingDistance> a schema1:PropertyValue ;
    schema1:description "0.5–5.4 mm" ;
    schema1:name "Working Distance" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/workingDistance> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 5e-01 .


```


### detail example Garvie2008-2
detail instance derived from Garvie et al. 2008 | Tagish Lake (C2) nanoglobules | TEM Sample Preparation (FIB, FEI Nova 200 NanoLab).
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
  "@id": "ex:semTAPP-detail-Garvie2008-2",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "ada:combinedResults": [
        {}
      ],
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:additionalProperty": [
              {
                "@id": "ada:parameter/semTAPP/coarseMillingConditions",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/semTAPP/coarseMillingConditions"
                  }
                ],
                "schema:name": "Coarse Milling Conditions",
                "schema:value": "30 kV, 10 pA Ga beam"
              }
            ],
            "schema:description": "HCl and HF acid dissolution residue from pristine Tagish Lake pieces; deposited on lacey C TEM grid attached to Al-SEM stub; uncoated",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          },
          {
            "schema:name": "Ion milling",
            "schema:position": 3,
            "schema:description": "no value available: schema:description",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
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
              "schema:value": "N — the SEM imaging and the FIB sectioning are one session on one instrument, \"Images were acquired with a Nova 200 NanoLab DualBeam FIB/SEM\" (p.2); no separate prior screening step is described"
            }
          ],
          "schema:name": "no value available: schema:name"
        }
      ],
      "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/semTAPP/workingDistance",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semTAPP/workingDistance"
            }
          ],
          "schema:name": "Working Distance",
          "schema:value": 5.4,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "5.4 mm (eucentric height for electron and ion columns)"
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "School of Earth and Space Exploration / School of Materials, Arizona State University"
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NASA NNG06GE37G (LAJG); NASA NNG06GF08G (PRB)"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SE Imaging (same instrument, pre- and post-FIB milling)"
      }
    }
  ],
  "ada:analyticalMode": [
    "TEM Sample Preparation"
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "N — a sample-preparation procedure produces sections, not results to combine"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "EBSD Indexing Rate",
      "dqv:value": -9999
    },
    {
      "dqv:isMeasurementOf": "EBSD Mean Angular Deviation",
      "dqv:value": -9999
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA NNG06GE37G (LAJG); NASA NNG06GF08G (PRB)",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only — the Tagish Lake carbonaceous residue on \"an Al-SEM stub\" (p.2); the globules sectioned by FIB are not given labels in the text",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-detail-Garvie2008-2",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "ada:combinedResults": [
        {}
      ],
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:additionalProperty": [
              {
                "@id": "ada:parameter/semTAPP/coarseMillingConditions",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/semTAPP/coarseMillingConditions"
                  }
                ],
                "schema:name": "Coarse Milling Conditions",
                "schema:value": "30 kV, 10 pA Ga beam"
              }
            ],
            "schema:description": "HCl and HF acid dissolution residue from pristine Tagish Lake pieces; deposited on lacey C TEM grid attached to Al-SEM stub; uncoated",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          },
          {
            "schema:name": "Ion milling",
            "schema:position": 3,
            "schema:description": "no value available: schema:description",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
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
              "schema:value": "N \u2014 the SEM imaging and the FIB sectioning are one session on one instrument, \"Images were acquired with a Nova 200 NanoLab DualBeam FIB/SEM\" (p.2); no separate prior screening step is described"
            }
          ],
          "schema:name": "no value available: schema:name"
        }
      ],
      "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/semTAPP/workingDistance",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semTAPP/workingDistance"
            }
          ],
          "schema:name": "Working Distance",
          "schema:value": 5.4,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "5.4 mm (eucentric height for electron and ion columns)"
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "School of Earth and Space Exploration / School of Materials, Arizona State University"
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NASA NNG06GE37G (LAJG); NASA NNG06GF08G (PRB)"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SE Imaging (same instrument, pre- and post-FIB milling)"
      }
    }
  ],
  "ada:analyticalMode": [
    "TEM Sample Preparation"
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "N \u2014 a sample-preparation procedure produces sections, not results to combine"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "EBSD Indexing Rate",
      "dqv:value": -9999
    },
    {
      "dqv:isMeasurementOf": "EBSD Mean Angular Deviation",
      "dqv:value": -9999
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA NNG06GE37G (LAJG); NASA NNG06GF08G (PRB)",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only \u2014 the Tagish Lake carbonaceous residue on \"an Al-SEM stub\" (p.2); the globules sectioned by FIB are not given labels in the text",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix dqv: <http://www.w3.org/ns/dqv#> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:semTAPP-detail-Garvie2008-2 a schema1:Dataset,
        schema1:Product ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "NASA NNG06GE37G (LAJG); NASA NNG06GF08G (PRB)" ] ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "SE Imaging (same instrument, pre- and post-FIB milling)" ] ] ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "EBSD Indexing Rate" ;
            dqv:value -9999 ],
        [ dqv:isMeasurementOf "Goodness-of-Fit" ;
            dqv:value "N — a sample-preparation procedure produces sections, not results to combine" ],
        [ dqv:isMeasurementOf "Analytical Precision" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "EBSD Mean Angular Deviation" ;
            dqv:value -9999 ],
        [ dqv:isMeasurementOf "Analytical Accuracy" ;
            dqv:value "no value available: dqv:value" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semTAPP/coarseMillingConditions> ;
                            schema1:description "HCl and HF acid dissolution residue from pristine Tagish Lake pieces; deposited on lacey C TEM grid attached to Al-SEM stub; uncoated" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "no value available: schema:description" ;
                            schema1:name "Ion milling" ;
                            schema1:position 3 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semTAPP/workingDistance> ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "School of Earth and Space Exploration / School of Materials, Arizona State University" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
                    schema1:name "no value available: schema:name" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            ada:combinedResults [ ] ;
            ada:edsDeadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "TEM Sample Preparation" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NASA NNG06GE37G (LAJG); NASA NNG06GF08G (PRB)" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimensions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Sample name only — the Tagish Lake carbonaceous residue on \"an Al-SEM stub\" (p.2); the globules sectioned by FIB are not given labels in the text" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "no value available: ada:voxelSize" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "N — the SEM imaging and the FIB sectioning are one session on one instrument, \"Images were acquired with a Nova 200 NanoLab DualBeam FIB/SEM\" (p.2); no separate prior screening step is described" .

<https://ada.astromat.org/metadata/parameter/semTAPP/coarseMillingConditions> a schema1:PropertyValue ;
    schema1:name "Coarse Milling Conditions" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/coarseMillingConditions> ;
    schema1:value "30 kV, 10 pA Ga beam" .

<https://ada.astromat.org/metadata/parameter/semTAPP/workingDistance> a schema1:PropertyValue ;
    schema1:description "5.4 mm (eucentric height for electron and ion columns)" ;
    schema1:name "Working Distance" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/workingDistance> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 5.4e+00 .


```


### detail example Genge2025
detail instance derived from Genge et al. 2025 | Micrometeorite NG-1 (CV3-like) | BSE Imaging (ZEISS Sigma 1550VP, 10 kV).
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
  "@id": "ex:semTAPP-detail-Genge2025",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:instrument": [
        {
          "schema:additionalType": [
            "SEM",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/semTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/semTAPP/acceleratingVoltage"
                }
              ],
              "schema:name": "Accelerating Voltage",
              "schema:value": 10,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "10 kV"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:semTAPP-detail-Genge2025/instrument/SEM"
        }
      ],
      "ada:combinedResults": [
        {}
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
              "schema:value": "N — the imaging this procedure performs is its own measurement, not a screening step before it; the paper describes no prior characterisation used to locate the units"
            }
          ],
          "schema:name": "no value available: schema:name"
        }
      ],
      "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "GPS Division Analytical Facility, California Institute of Technology"
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "EDS (same session, same instrument); EBSD (same instrument); EPMA (JEOL JXA-iHP200F, WDS, out of scope)"
      }
    }
  ],
  "ada:analyticalMode": [
    "BSE Imaging"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only — the single particle \"micrometeorite NG-1\", analysed as \"the NG-1 section\" (p.2); regions are identified by figure panel (\"Alloy-rich regions\", Fig. 2; \"Silicate-dominated areas\", Fig. 3; pp.3–4), not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-detail-Genge2025",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:instrument": [
        {
          "schema:additionalType": [
            "SEM",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/semTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/semTAPP/acceleratingVoltage"
                }
              ],
              "schema:name": "Accelerating Voltage",
              "schema:value": 10,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "10 kV"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:semTAPP-detail-Genge2025/instrument/SEM"
        }
      ],
      "ada:combinedResults": [
        {}
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
              "schema:value": "N \u2014 the imaging this procedure performs is its own measurement, not a screening step before it; the paper describes no prior characterisation used to locate the units"
            }
          ],
          "schema:name": "no value available: schema:name"
        }
      ],
      "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "GPS Division Analytical Facility, California Institute of Technology"
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "EDS (same session, same instrument); EBSD (same instrument); EPMA (JEOL JXA-iHP200F, WDS, out of scope)"
      }
    }
  ],
  "ada:analyticalMode": [
    "BSE Imaging"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only \u2014 the single particle \"micrometeorite NG-1\", analysed as \"the NG-1 section\" (p.2); regions are identified by figure panel (\"Alloy-rich regions\", Fig. 2; \"Silicate-dominated areas\", Fig. 3; pp.3\u20134), not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix wd: <https://www.wikidata.org/entity/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:semTAPP-detail-Genge2025 a schema1:Dataset,
        schema1:Product ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "EDS (same session, same instrument); EBSD (same instrument); EPMA (JEOL JXA-iHP200F, WDS, out of scope)" ] ] ;
    prov:wasGeneratedBy [ schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:instrument <https://example.org/semTAPP-detail-Genge2025/instrument/SEM> ;
            schema1:location [ a schema1:Place ;
                    schema1:name "GPS Division Analytical Facility, California Institute of Technology" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
                    schema1:name "no value available: schema:name" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            ada:combinedResults [ ] ;
            ada:edsDeadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "BSE Imaging" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimensions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Sample name only — the single particle \"micrometeorite NG-1\", analysed as \"the NG-1 section\" (p.2); regions are identified by figure panel (\"Alloy-rich regions\", Fig. 2; \"Silicate-dominated areas\", Fig. 3; pp.3–4), not labelled" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "no value available: ada:voxelSize" .

<https://example.org/semTAPP-detail-Genge2025/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semTAPP/acceleratingVoltage> ;
    schema1:additionalType wd:Q3099911,
        "SEM" ;
    schema1:name "no value available: schema:name" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "N — the imaging this procedure performs is its own measurement, not a screening step before it; the paper describes no prior characterisation used to locate the units" .

<https://ada.astromat.org/metadata/parameter/semTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:description "10 kV" ;
    schema1:name "Accelerating Voltage" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/acceleratingVoltage> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 10 .


```


### detail example Genge2025-2
detail instance derived from Genge et al. 2025 | Micrometeorite NG-1 (CV3-like) | EDS Point Analysis (ZEISS Sigma 1550VP, 10 kV).
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
  "@id": "ex:semTAPP-detail-Genge2025-2",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:instrument": [
        {
          "schema:additionalType": [
            "SEM",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/semTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/semTAPP/acceleratingVoltage"
                }
              ],
              "schema:name": "Accelerating Voltage",
              "schema:value": 10,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "10 kV"
            },
            {
              "@id": "ada:parameter/semTAPP/beamDiameter",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/semTAPP/beamDiameter"
                }
              ],
              "schema:name": "Beam Diameter",
              "schema:value": 0.1,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "N — the '0.1 μm beam diameter' (p.2) is the EPMA's, not the SEM's"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:semTAPP-detail-Genge2025-2/instrument/SEM"
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/semTAPP/beamDamageMinimization",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semTAPP/beamDamageMinimization"
            }
          ],
          "schema:name": "Beam Damage Minimization",
          "schema:value": "N — 10 kV was chosen 'to reduce the excitation volume and increase spatial resolution' (p.2), not to limit beam damage"
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
              "schema:value": "N — the imaging this procedure performs is its own measurement, not a screening step before it; the paper describes no prior characterisation used to locate the units"
            }
          ],
          "schema:name": "no value available: schema:name"
        }
      ],
      "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "GPS Division Analytical Facility, California Institute of Technology"
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "BSE Imaging (same session, same instrument); EBSD (same instrument); EPMA (JEOL JXA-iHP200F, WDS, out of scope)"
      }
    }
  ],
  "ada:analyticalMode": [
    "EDS Point Analysis"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only — the single particle \"micrometeorite NG-1\", analysed as \"the NG-1 section\" (p.2); regions are identified by figure panel (\"Alloy-rich regions\", Fig. 2; \"Silicate-dominated areas\", Fig. 3; pp.3–4), not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-detail-Genge2025-2",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:instrument": [
        {
          "schema:additionalType": [
            "SEM",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/semTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/semTAPP/acceleratingVoltage"
                }
              ],
              "schema:name": "Accelerating Voltage",
              "schema:value": 10,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "10 kV"
            },
            {
              "@id": "ada:parameter/semTAPP/beamDiameter",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/semTAPP/beamDiameter"
                }
              ],
              "schema:name": "Beam Diameter",
              "schema:value": 0.1,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "N \u2014 the '0.1 \u03bcm beam diameter' (p.2) is the EPMA's, not the SEM's"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:semTAPP-detail-Genge2025-2/instrument/SEM"
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/semTAPP/beamDamageMinimization",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semTAPP/beamDamageMinimization"
            }
          ],
          "schema:name": "Beam Damage Minimization",
          "schema:value": "N \u2014 10 kV was chosen 'to reduce the excitation volume and increase spatial resolution' (p.2), not to limit beam damage"
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
              "schema:value": "N \u2014 the imaging this procedure performs is its own measurement, not a screening step before it; the paper describes no prior characterisation used to locate the units"
            }
          ],
          "schema:name": "no value available: schema:name"
        }
      ],
      "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "GPS Division Analytical Facility, California Institute of Technology"
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "BSE Imaging (same session, same instrument); EBSD (same instrument); EPMA (JEOL JXA-iHP200F, WDS, out of scope)"
      }
    }
  ],
  "ada:analyticalMode": [
    "EDS Point Analysis"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only \u2014 the single particle \"micrometeorite NG-1\", analysed as \"the NG-1 section\" (p.2); regions are identified by figure panel (\"Alloy-rich regions\", Fig. 2; \"Silicate-dominated areas\", Fig. 3; pp.3\u20134), not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix wd: <https://www.wikidata.org/entity/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:semTAPP-detail-Genge2025-2 a schema1:Dataset,
        schema1:Product ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "BSE Imaging (same session, same instrument); EBSD (same instrument); EPMA (JEOL JXA-iHP200F, WDS, out of scope)" ] ] ;
    prov:wasGeneratedBy [ schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semTAPP/beamDamageMinimization> ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:instrument <https://example.org/semTAPP-detail-Genge2025-2/instrument/SEM> ;
            schema1:location [ a schema1:Place ;
                    schema1:name "GPS Division Analytical Facility, California Institute of Technology" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
                    schema1:name "no value available: schema:name" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            ada:combinedResults [ ] ;
            ada:edsDeadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "EDS Point Analysis" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimensions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Sample name only — the single particle \"micrometeorite NG-1\", analysed as \"the NG-1 section\" (p.2); regions are identified by figure panel (\"Alloy-rich regions\", Fig. 2; \"Silicate-dominated areas\", Fig. 3; pp.3–4), not labelled" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "no value available: ada:voxelSize" .

<https://example.org/semTAPP-detail-Genge2025-2/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/semTAPP/beamDiameter> ;
    schema1:additionalType wd:Q3099911,
        "SEM" ;
    schema1:name "no value available: schema:name" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "N — the imaging this procedure performs is its own measurement, not a screening step before it; the paper describes no prior characterisation used to locate the units" .

<https://ada.astromat.org/metadata/parameter/semTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:description "10 kV" ;
    schema1:name "Accelerating Voltage" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/acceleratingVoltage> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 10 .

<https://ada.astromat.org/metadata/parameter/semTAPP/beamDamageMinimization> a schema1:PropertyValue ;
    schema1:name "Beam Damage Minimization" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/beamDamageMinimization> ;
    schema1:value "N — 10 kV was chosen 'to reduce the excitation volume and increase spatial resolution' (p.2), not to limit beam damage" .

<https://ada.astromat.org/metadata/parameter/semTAPP/beamDiameter> a schema1:PropertyValue ;
    schema1:description "N — the '0.1 μm beam diameter' (p.2) is the EPMA's, not the SEM's" ;
    schema1:name "Beam Diameter" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/beamDiameter> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1e-01 .


```


### detail example Genge2025-3
detail instance derived from Genge et al. 2025 | Micrometeorite NG-1 (CV3-like) | EBSD (ZEISS Sigma 1550VP, 20 kV).
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
  "@id": "ex:semTAPP-detail-Genge2025-3",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:instrument": [
        {
          "schema:additionalType": [
            "SEM",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/semTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/semTAPP/acceleratingVoltage"
                }
              ],
              "schema:name": "Accelerating Voltage",
              "schema:value": 20,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "20 kV"
            },
            {
              "@id": "ada:parameter/semTAPP/mappingBeamCurrent",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/semTAPP/mappingBeamCurrent"
                }
              ],
              "schema:name": "Mapping Beam Current",
              "schema:value": 6,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "6 nA"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:semTAPP-detail-Genge2025-3/instrument/SEM"
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/semTAPP/chamberPressure",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semTAPP/chamberPressure"
            }
          ],
          "schema:name": "Chamber Pressure",
          "schema:value": 25,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "25 Pa (variable pressure mode)"
        }
      ],
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Data processing",
            "schema:additionalProperty": [
              {
                "@id": "ada:parameter/semTAPP/crystalStructureDatabase",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/semTAPP/crystalStructureDatabase"
                  }
                ],
                "schema:name": "Crystal Structure Database",
                "schema:value": "ICSD (Inorganic Crystal Structure Database)"
              }
            ],
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Sample preparation",
            "schema:position": 2,
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          },
          {
            "schema:name": "Ion milling",
            "schema:position": 3,
            "schema:description": "no value available: schema:description",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
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
              "schema:value": "N — the imaging this procedure performs is its own measurement, not a screening step before it; the paper describes no prior characterisation used to locate the units"
            }
          ],
          "schema:name": "no value available: schema:name"
        }
      ],
      "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "GPS Division Analytical Facility, California Institute of Technology"
      },
      "schema:description": "EBSD done in variable pressure mode (25 Pa) to suppress charging on tilted sample; spatial resolution ~30 nm stated; calibrated with single-crystal silicon standard",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "BSE Imaging and EDS (same instrument); SIMS (University of Wisconsin-Madison); EPMA (out of scope)"
      }
    }
  ],
  "ada:analyticalMode": [
    "EBSD"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only — the single particle \"micrometeorite NG-1\", analysed as \"the NG-1 section\" (p.2); regions are identified by figure panel (\"Alloy-rich regions\", Fig. 2; \"Silicate-dominated areas\", Fig. 3; pp.3–4), not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-detail-Genge2025-3",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:instrument": [
        {
          "schema:additionalType": [
            "SEM",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/semTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/semTAPP/acceleratingVoltage"
                }
              ],
              "schema:name": "Accelerating Voltage",
              "schema:value": 20,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "20 kV"
            },
            {
              "@id": "ada:parameter/semTAPP/mappingBeamCurrent",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/semTAPP/mappingBeamCurrent"
                }
              ],
              "schema:name": "Mapping Beam Current",
              "schema:value": 6,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "6 nA"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:semTAPP-detail-Genge2025-3/instrument/SEM"
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/semTAPP/chamberPressure",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semTAPP/chamberPressure"
            }
          ],
          "schema:name": "Chamber Pressure",
          "schema:value": 25,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "25 Pa (variable pressure mode)"
        }
      ],
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Data processing",
            "schema:additionalProperty": [
              {
                "@id": "ada:parameter/semTAPP/crystalStructureDatabase",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/semTAPP/crystalStructureDatabase"
                  }
                ],
                "schema:name": "Crystal Structure Database",
                "schema:value": "ICSD (Inorganic Crystal Structure Database)"
              }
            ],
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Sample preparation",
            "schema:position": 2,
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          },
          {
            "schema:name": "Ion milling",
            "schema:position": 3,
            "schema:description": "no value available: schema:description",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
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
              "schema:value": "N \u2014 the imaging this procedure performs is its own measurement, not a screening step before it; the paper describes no prior characterisation used to locate the units"
            }
          ],
          "schema:name": "no value available: schema:name"
        }
      ],
      "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "GPS Division Analytical Facility, California Institute of Technology"
      },
      "schema:description": "EBSD done in variable pressure mode (25 Pa) to suppress charging on tilted sample; spatial resolution ~30 nm stated; calibrated with single-crystal silicon standard",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "BSE Imaging and EDS (same instrument); SIMS (University of Wisconsin-Madison); EPMA (out of scope)"
      }
    }
  ],
  "ada:analyticalMode": [
    "EBSD"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only \u2014 the single particle \"micrometeorite NG-1\", analysed as \"the NG-1 section\" (p.2); regions are identified by figure panel (\"Alloy-rich regions\", Fig. 2; \"Silicate-dominated areas\", Fig. 3; pp.3\u20134), not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix wd: <https://www.wikidata.org/entity/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:semTAPP-detail-Genge2025-3 a schema1:Dataset,
        schema1:Product ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "BSE Imaging and EDS (same instrument); SIMS (University of Wisconsin-Madison); EPMA (out of scope)" ] ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "no value available: schema:description" ;
                            schema1:name "Ion milling" ;
                            schema1:position 3 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semTAPP/crystalStructureDatabase> ;
                            schema1:name "Data processing" ;
                            schema1:position 1 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Sample preparation" ;
                            schema1:position 2 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semTAPP/chamberPressure> ;
            schema1:description "EBSD done in variable pressure mode (25 Pa) to suppress charging on tilted sample; spatial resolution ~30 nm stated; calibrated with single-crystal silicon standard" ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:instrument <https://example.org/semTAPP-detail-Genge2025-3/instrument/SEM> ;
            schema1:location [ a schema1:Place ;
                    schema1:name "GPS Division Analytical Facility, California Institute of Technology" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
                    schema1:name "no value available: schema:name" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            ada:combinedResults [ ] ;
            ada:edsDeadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "EBSD" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimensions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Sample name only — the single particle \"micrometeorite NG-1\", analysed as \"the NG-1 section\" (p.2); regions are identified by figure panel (\"Alloy-rich regions\", Fig. 2; \"Silicate-dominated areas\", Fig. 3; pp.3–4), not labelled" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "no value available: ada:voxelSize" .

<https://example.org/semTAPP-detail-Genge2025-3/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/semTAPP/mappingBeamCurrent> ;
    schema1:additionalType wd:Q3099911,
        "SEM" ;
    schema1:name "no value available: schema:name" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "N — the imaging this procedure performs is its own measurement, not a screening step before it; the paper describes no prior characterisation used to locate the units" .

<https://ada.astromat.org/metadata/parameter/semTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:description "20 kV" ;
    schema1:name "Accelerating Voltage" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/acceleratingVoltage> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 20 .

<https://ada.astromat.org/metadata/parameter/semTAPP/chamberPressure> a schema1:PropertyValue ;
    schema1:description "25 Pa (variable pressure mode)" ;
    schema1:name "Chamber Pressure" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/chamberPressure> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 25 .

<https://ada.astromat.org/metadata/parameter/semTAPP/crystalStructureDatabase> a schema1:PropertyValue ;
    schema1:name "Crystal Structure Database" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/crystalStructureDatabase> ;
    schema1:value "ICSD (Inorganic Crystal Structure Database)" .

<https://ada.astromat.org/metadata/parameter/semTAPP/mappingBeamCurrent> a schema1:PropertyValue ;
    schema1:description "6 nA" ;
    schema1:name "Mapping Beam Current" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/mappingBeamCurrent> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 6 .


```


### detail example Gucsik2013
detail instance derived from Gucsik et al. 2013 | Forsterite, Kaba meteorite (CV3) | CL Mapping (JEOL JSM-5410LV).
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
  "@id": "ex:semTAPP-detail-Gucsik2013",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "ada:combinedResults": [
        {}
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
              "schema:value": "Optical microscope-cathodoluminescence survey — \"Following a systematic optical microscopecathodoluminescence study of a Kaba thin section, seven representative grains (designated as B-1 through B-7) were selected for further analyses\" (p.2); the grain labels tie the later measurements back to that survey (Fig. 1, p.2)"
            }
          ],
          "schema:name": "no value available: schema:name"
        }
      ],
      "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
      "schema:description": "CL color imaging also done with separate luminoscope ELM-3R (cold cathode, 10 kV, 0.5 mA, <100 Torr) — standalone CL system, not SEM-based; spectrum deconvolution via Peak Analyzer in OriginPro 8J SR2",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "EDS and BSE Imaging (same instrument); EPMA with WDS (JEOL JXA-8900R, out of scope)"
      }
    }
  ],
  "ada:analyticalMode": [
    "CL Mapping"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Labelled: \"seven representative grains (designated as B-1 through B-7)\" of \"a Kaba thin section\" (p.2), shown as the \"analyzed areas\" in Fig. 1 (p.2)",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-detail-Gucsik2013",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "ada:combinedResults": [
        {}
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
              "schema:value": "Optical microscope-cathodoluminescence survey \u2014 \"Following a systematic optical microscopecathodoluminescence study of a Kaba thin section, seven representative grains (designated as B-1 through B-7) were selected for further analyses\" (p.2); the grain labels tie the later measurements back to that survey (Fig. 1, p.2)"
            }
          ],
          "schema:name": "no value available: schema:name"
        }
      ],
      "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
      "schema:description": "CL color imaging also done with separate luminoscope ELM-3R (cold cathode, 10 kV, 0.5 mA, <100 Torr) \u2014 standalone CL system, not SEM-based; spectrum deconvolution via Peak Analyzer in OriginPro 8J SR2",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "EDS and BSE Imaging (same instrument); EPMA with WDS (JEOL JXA-8900R, out of scope)"
      }
    }
  ],
  "ada:analyticalMode": [
    "CL Mapping"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Labelled: \"seven representative grains (designated as B-1 through B-7)\" of \"a Kaba thin section\" (p.2), shown as the \"analyzed areas\" in Fig. 1 (p.2)",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:semTAPP-detail-Gucsik2013 a schema1:Dataset,
        schema1:Product ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "EDS and BSE Imaging (same instrument); EPMA with WDS (JEOL JXA-8900R, out of scope)" ] ] ;
    prov:wasGeneratedBy [ schema1:description "CL color imaging also done with separate luminoscope ELM-3R (cold cathode, 10 kV, 0.5 mA, <100 Torr) — standalone CL system, not SEM-based; spectrum deconvolution via Peak Analyzer in OriginPro 8J SR2" ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
                    schema1:name "no value available: schema:name" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            ada:combinedResults [ ] ;
            ada:edsDeadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "CL Mapping" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimensions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Labelled: \"seven representative grains (designated as B-1 through B-7)\" of \"a Kaba thin section\" (p.2), shown as the \"analyzed areas\" in Fig. 1 (p.2)" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "no value available: ada:voxelSize" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "Optical microscope-cathodoluminescence survey — \"Following a systematic optical microscopecathodoluminescence study of a Kaba thin section, seven representative grains (designated as B-1 through B-7) were selected for further analyses\" (p.2); the grain labels tie the later measurements back to that survey (Fig. 1, p.2)" .


```


### detail example Gucsik2013-2
detail instance derived from Gucsik et al. 2013 | Forsterite, Kaba meteorite (CV3) | EDS Point Analysis (JEOL JSM-5410LV).
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
  "@id": "ex:semTAPP-detail-Gucsik2013-2",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:instrument": [
        {
          "schema:additionalType": [
            "SEM",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/semTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/semTAPP/acceleratingVoltage"
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
          "@id": "ex:semTAPP-detail-Gucsik2013-2/instrument/SEM"
        }
      ],
      "ada:combinedResults": [
        {}
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
              "schema:value": "Optical microscope-cathodoluminescence survey — \"Following a systematic optical microscopecathodoluminescence study of a Kaba thin section, seven representative grains (designated as B-1 through B-7) were selected for further analyses\" (p.2); the grain labels tie the later measurements back to that survey (Fig. 1, p.2)"
            }
          ],
          "schema:name": "no value available: schema:name"
        }
      ],
      "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
      "schema:description": "Described as semiquantitative; BSE images also captured with this instrument at same conditions; EPMA (JEOL JXA-8900R WDS) used for quantitative analyses (out of scope)",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "CL (same instrument); BSE Imaging (same instrument, same session); EPMA with WDS (JEOL JXA-8900R, out of scope)"
      }
    }
  ],
  "ada:analyticalMode": [
    "EDS Point Analysis"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Labelled: \"seven representative grains (designated as B-1 through B-7)\" of \"a Kaba thin section\" (p.2), shown as the \"analyzed areas\" in Fig. 1 (p.2)",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-detail-Gucsik2013-2",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:instrument": [
        {
          "schema:additionalType": [
            "SEM",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/semTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/semTAPP/acceleratingVoltage"
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
          "@id": "ex:semTAPP-detail-Gucsik2013-2/instrument/SEM"
        }
      ],
      "ada:combinedResults": [
        {}
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
              "schema:value": "Optical microscope-cathodoluminescence survey \u2014 \"Following a systematic optical microscopecathodoluminescence study of a Kaba thin section, seven representative grains (designated as B-1 through B-7) were selected for further analyses\" (p.2); the grain labels tie the later measurements back to that survey (Fig. 1, p.2)"
            }
          ],
          "schema:name": "no value available: schema:name"
        }
      ],
      "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
      "schema:description": "Described as semiquantitative; BSE images also captured with this instrument at same conditions; EPMA (JEOL JXA-8900R WDS) used for quantitative analyses (out of scope)",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "CL (same instrument); BSE Imaging (same instrument, same session); EPMA with WDS (JEOL JXA-8900R, out of scope)"
      }
    }
  ],
  "ada:analyticalMode": [
    "EDS Point Analysis"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Labelled: \"seven representative grains (designated as B-1 through B-7)\" of \"a Kaba thin section\" (p.2), shown as the \"analyzed areas\" in Fig. 1 (p.2)",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix wd: <https://www.wikidata.org/entity/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:semTAPP-detail-Gucsik2013-2 a schema1:Dataset,
        schema1:Product ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "CL (same instrument); BSE Imaging (same instrument, same session); EPMA with WDS (JEOL JXA-8900R, out of scope)" ] ] ;
    prov:wasGeneratedBy [ schema1:description "Described as semiquantitative; BSE images also captured with this instrument at same conditions; EPMA (JEOL JXA-8900R WDS) used for quantitative analyses (out of scope)" ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:instrument <https://example.org/semTAPP-detail-Gucsik2013-2/instrument/SEM> ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
                    schema1:name "no value available: schema:name" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            ada:combinedResults [ ] ;
            ada:edsDeadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "EDS Point Analysis" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimensions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Labelled: \"seven representative grains (designated as B-1 through B-7)\" of \"a Kaba thin section\" (p.2), shown as the \"analyzed areas\" in Fig. 1 (p.2)" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "no value available: ada:voxelSize" .

<https://example.org/semTAPP-detail-Gucsik2013-2/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semTAPP/acceleratingVoltage> ;
    schema1:additionalType wd:Q3099911,
        "SEM" ;
    schema1:name "no value available: schema:name" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "Optical microscope-cathodoluminescence survey — \"Following a systematic optical microscopecathodoluminescence study of a Kaba thin section, seven representative grains (designated as B-1 through B-7) were selected for further analyses\" (p.2); the grain labels tie the later measurements back to that survey (Fig. 1, p.2)" .

<https://ada.astromat.org/metadata/parameter/semTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:description "15 kV" ;
    schema1:name "Accelerating Voltage" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/acceleratingVoltage> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 15 .


```


### detail example Izawa2010
detail instance derived from Izawa et al. 2010 | Tagish Lake (C2) meteorite | CL Mapping (Hitachi S-2500C).
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
  "@id": "ex:semTAPP-detail-Izawa2010",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:instrument": [
        {
          "schema:additionalType": [
            "SEM",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/semTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/semTAPP/acceleratingVoltage"
                }
              ],
              "schema:name": "Accelerating Voltage",
              "schema:value": 15,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "15–20 kV"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:semTAPP-detail-Izawa2010/instrument/SEM"
        },
        {
          "ada:toolRole": "acquisition",
          "schema:name": "Gatan DigitalMicrograph (CL image assembly)",
          "@type": [
            "schema:SoftwareApplication"
          ],
          "schema:additionalType": [
            {
              "@id": "https://www.wikidata.org/entity/Q7397"
            }
          ]
        },
        {
          "ada:toolRole": "dataReduction",
          "schema:name": "Gatan DigitalMicrograph",
          "@type": [
            "schema:SoftwareApplication"
          ],
          "schema:additionalType": [
            {
              "@id": "https://www.wikidata.org/entity/Q7397"
            }
          ]
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/semTAPP/chamberPressure",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semTAPP/chamberPressure"
            }
          ],
          "schema:name": "Chamber Pressure",
          "schema:value": "High vacuum",
          "schema:unitText": "no value available: unnamed property"
        },
        {
          "@id": "ada:parameter/semTAPP/clIntegrationTime",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semTAPP/clIntegrationTime"
            }
          ],
          "schema:name": "CL Integration Time",
          "schema:value": 80,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "80–500 ms per pixel (varied based on IR luminescence duration in carbonates)"
        },
        {
          "@id": "ada:parameter/semTAPP/workingDistance",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semTAPP/workingDistance"
            }
          ],
          "schema:name": "Working Distance",
          "schema:value": 10,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "~10 mm"
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
              "schema:value": "Micro X-ray diffraction reconnaissance — the paper's first stage is \"an initial, non-destructive in situ reconnaissance step using micro X-ray diffraction (mXRD) to document meteorite mineralogy and textures and to identify features of interest\", valuable as \"a 'no-touch' first-pass reconnaissance, which may identify areas for further study\"; it then gives \"point-by-point correlation of crystal structure data with other microscopic and microanalytical data\" (p.2)"
            }
          ],
          "schema:name": "no value available: schema:name"
        }
      ],
      "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Zircon and Accessory Phase Laboratory, University of Western Ontario"
      },
      "schema:description": "Digiscan II beam controller used for CL raster; multi-channel color CL distinguishes ~4 spectral bands; beam-induced CL may persist from long-lived IR emission in carbonates",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Carbon-coated polished thin sections; high vacuum analysis",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          },
          {
            "schema:name": "Ion milling",
            "schema:position": 3,
            "schema:description": "no value available: schema:description",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM-EDX (Leo 440; Leo 1540); BSE Imaging; micro-XRD; EPMA-WDS (out of scope)"
      }
    }
  ],
  "ada:analyticalMode": [
    "CL Mapping"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only — \"polished thin sections\" of Tagish Lake (p.2), not individually labelled; the numbered points of Table 1 and Fig. 1 (e.g. \"point #1\", \"spot 34\") are μXRD spots, not SEM-CL",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-detail-Izawa2010",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:instrument": [
        {
          "schema:additionalType": [
            "SEM",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/semTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/semTAPP/acceleratingVoltage"
                }
              ],
              "schema:name": "Accelerating Voltage",
              "schema:value": 15,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "15\u201320 kV"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:semTAPP-detail-Izawa2010/instrument/SEM"
        },
        {
          "ada:toolRole": "acquisition",
          "schema:name": "Gatan DigitalMicrograph (CL image assembly)",
          "@type": [
            "schema:SoftwareApplication"
          ],
          "schema:additionalType": [
            {
              "@id": "https://www.wikidata.org/entity/Q7397"
            }
          ]
        },
        {
          "ada:toolRole": "dataReduction",
          "schema:name": "Gatan DigitalMicrograph",
          "@type": [
            "schema:SoftwareApplication"
          ],
          "schema:additionalType": [
            {
              "@id": "https://www.wikidata.org/entity/Q7397"
            }
          ]
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/semTAPP/chamberPressure",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semTAPP/chamberPressure"
            }
          ],
          "schema:name": "Chamber Pressure",
          "schema:value": "High vacuum",
          "schema:unitText": "no value available: unnamed property"
        },
        {
          "@id": "ada:parameter/semTAPP/clIntegrationTime",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semTAPP/clIntegrationTime"
            }
          ],
          "schema:name": "CL Integration Time",
          "schema:value": 80,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "80\u2013500 ms per pixel (varied based on IR luminescence duration in carbonates)"
        },
        {
          "@id": "ada:parameter/semTAPP/workingDistance",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semTAPP/workingDistance"
            }
          ],
          "schema:name": "Working Distance",
          "schema:value": 10,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "~10 mm"
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
              "schema:value": "Micro X-ray diffraction reconnaissance \u2014 the paper's first stage is \"an initial, non-destructive in situ reconnaissance step using micro X-ray diffraction (mXRD) to document meteorite mineralogy and textures and to identify features of interest\", valuable as \"a 'no-touch' first-pass reconnaissance, which may identify areas for further study\"; it then gives \"point-by-point correlation of crystal structure data with other microscopic and microanalytical data\" (p.2)"
            }
          ],
          "schema:name": "no value available: schema:name"
        }
      ],
      "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Zircon and Accessory Phase Laboratory, University of Western Ontario"
      },
      "schema:description": "Digiscan II beam controller used for CL raster; multi-channel color CL distinguishes ~4 spectral bands; beam-induced CL may persist from long-lived IR emission in carbonates",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Carbon-coated polished thin sections; high vacuum analysis",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          },
          {
            "schema:name": "Ion milling",
            "schema:position": 3,
            "schema:description": "no value available: schema:description",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM-EDX (Leo 440; Leo 1540); BSE Imaging; micro-XRD; EPMA-WDS (out of scope)"
      }
    }
  ],
  "ada:analyticalMode": [
    "CL Mapping"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only \u2014 \"polished thin sections\" of Tagish Lake (p.2), not individually labelled; the numbered points of Table 1 and Fig. 1 (e.g. \"point #1\", \"spot 34\") are \u03bcXRD spots, not SEM-CL",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix wd: <https://www.wikidata.org/entity/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:semTAPP-detail-Izawa2010 a schema1:Dataset,
        schema1:Product ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "SEM-EDX (Leo 440; Leo 1540); BSE Imaging; micro-XRD; EPMA-WDS (out of scope)" ] ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "no value available: schema:description" ;
                            schema1:name "Ion milling" ;
                            schema1:position 3 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Carbon-coated polished thin sections; high vacuum analysis" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semTAPP/chamberPressure>,
                <https://ada.astromat.org/metadata/parameter/semTAPP/clIntegrationTime>,
                <https://ada.astromat.org/metadata/parameter/semTAPP/workingDistance> ;
            schema1:description "Digiscan II beam controller used for CL raster; multi-channel color CL distinguishes ~4 spectral bands; beam-induced CL may persist from long-lived IR emission in carbonates" ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:instrument [ a schema1:SoftwareApplication ;
                    schema1:additionalType wd:Q7397 ;
                    schema1:name "Gatan DigitalMicrograph (CL image assembly)" ;
                    ada:toolRole "acquisition" ],
                [ a schema1:SoftwareApplication ;
                    schema1:additionalType wd:Q7397 ;
                    schema1:name "Gatan DigitalMicrograph" ;
                    ada:toolRole "dataReduction" ],
                <https://example.org/semTAPP-detail-Izawa2010/instrument/SEM> ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Zircon and Accessory Phase Laboratory, University of Western Ontario" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
                    schema1:name "no value available: schema:name" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            ada:combinedResults [ ] ;
            ada:edsDeadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "CL Mapping" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimensions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Sample name only — \"polished thin sections\" of Tagish Lake (p.2), not individually labelled; the numbered points of Table 1 and Fig. 1 (e.g. \"point #1\", \"spot 34\") are μXRD spots, not SEM-CL" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "no value available: ada:voxelSize" .

<https://example.org/semTAPP-detail-Izawa2010/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semTAPP/acceleratingVoltage> ;
    schema1:additionalType wd:Q3099911,
        "SEM" ;
    schema1:name "no value available: schema:name" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "Micro X-ray diffraction reconnaissance — the paper's first stage is \"an initial, non-destructive in situ reconnaissance step using micro X-ray diffraction (mXRD) to document meteorite mineralogy and textures and to identify features of interest\", valuable as \"a 'no-touch' first-pass reconnaissance, which may identify areas for further study\"; it then gives \"point-by-point correlation of crystal structure data with other microscopic and microanalytical data\" (p.2)" .

<https://ada.astromat.org/metadata/parameter/semTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:description "15–20 kV" ;
    schema1:name "Accelerating Voltage" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/acceleratingVoltage> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 15 .

<https://ada.astromat.org/metadata/parameter/semTAPP/chamberPressure> a schema1:PropertyValue ;
    schema1:name "Chamber Pressure" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/chamberPressure> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value "High vacuum" .

<https://ada.astromat.org/metadata/parameter/semTAPP/clIntegrationTime> a schema1:PropertyValue ;
    schema1:description "80–500 ms per pixel (varied based on IR luminescence duration in carbonates)" ;
    schema1:name "CL Integration Time" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/clIntegrationTime> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 80 .

<https://ada.astromat.org/metadata/parameter/semTAPP/workingDistance> a schema1:PropertyValue ;
    schema1:description "~10 mm" ;
    schema1:name "Working Distance" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/workingDistance> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 10 .


```


### detail example Izawa2010-2
detail instance derived from Izawa et al. 2010 | Tagish Lake (C2) meteorite | BSE Imaging (Leo 440).
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
  "@id": "ex:semTAPP-detail-Izawa2010-2",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "ada:combinedResults": [
        {}
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
              "schema:value": "Micro X-ray diffraction reconnaissance — the paper's first stage is \"an initial, non-destructive in situ reconnaissance step using micro X-ray diffraction (mXRD) to document meteorite mineralogy and textures and to identify features of interest\", valuable as \"a 'no-touch' first-pass reconnaissance, which may identify areas for further study\"; it then gives \"point-by-point correlation of crystal structure data with other microscopic and microanalytical data\" (p.2)"
            }
          ],
          "schema:name": "no value available: schema:name"
        }
      ],
      "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Surface Science Western"
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "EDS (same instrument); CL (Hitachi S-2500C); BSE Imaging (Leo 1540); micro-XRD; EPMA (out of scope)"
      }
    }
  ],
  "ada:analyticalMode": [
    "BSE Imaging"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only — \"the Tagish Lake sections\" (p.3), not individually labelled; the numbered points of Table 1 and Fig. 1 (e.g. \"point #1\", \"spot 34\") are μXRD spots, not SEM analyses",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-detail-Izawa2010-2",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "ada:combinedResults": [
        {}
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
              "schema:value": "Micro X-ray diffraction reconnaissance \u2014 the paper's first stage is \"an initial, non-destructive in situ reconnaissance step using micro X-ray diffraction (mXRD) to document meteorite mineralogy and textures and to identify features of interest\", valuable as \"a 'no-touch' first-pass reconnaissance, which may identify areas for further study\"; it then gives \"point-by-point correlation of crystal structure data with other microscopic and microanalytical data\" (p.2)"
            }
          ],
          "schema:name": "no value available: schema:name"
        }
      ],
      "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Surface Science Western"
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "EDS (same instrument); CL (Hitachi S-2500C); BSE Imaging (Leo 1540); micro-XRD; EPMA (out of scope)"
      }
    }
  ],
  "ada:analyticalMode": [
    "BSE Imaging"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only \u2014 \"the Tagish Lake sections\" (p.3), not individually labelled; the numbered points of Table 1 and Fig. 1 (e.g. \"point #1\", \"spot 34\") are \u03bcXRD spots, not SEM analyses",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:semTAPP-detail-Izawa2010-2 a schema1:Dataset,
        schema1:Product ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "EDS (same instrument); CL (Hitachi S-2500C); BSE Imaging (Leo 1540); micro-XRD; EPMA (out of scope)" ] ] ;
    prov:wasGeneratedBy [ schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Surface Science Western" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
                    schema1:name "no value available: schema:name" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            ada:combinedResults [ ] ;
            ada:edsDeadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "BSE Imaging" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimensions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Sample name only — \"the Tagish Lake sections\" (p.3), not individually labelled; the numbered points of Table 1 and Fig. 1 (e.g. \"point #1\", \"spot 34\") are μXRD spots, not SEM analyses" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "no value available: ada:voxelSize" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "Micro X-ray diffraction reconnaissance — the paper's first stage is \"an initial, non-destructive in situ reconnaissance step using micro X-ray diffraction (mXRD) to document meteorite mineralogy and textures and to identify features of interest\", valuable as \"a 'no-touch' first-pass reconnaissance, which may identify areas for further study\"; it then gives \"point-by-point correlation of crystal structure data with other microscopic and microanalytical data\" (p.2)" .


```


### detail example Izawa2010-3
detail instance derived from Izawa et al. 2010 | Tagish Lake (C2) meteorite | EDS Mapping (Leo 440).
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
  "@id": "ex:semTAPP-detail-Izawa2010-3",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "ada:combinedResults": [
        {}
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
              "schema:value": "Micro X-ray diffraction reconnaissance — the paper's first stage is \"an initial, non-destructive in situ reconnaissance step using micro X-ray diffraction (mXRD) to document meteorite mineralogy and textures and to identify features of interest\", valuable as \"a 'no-touch' first-pass reconnaissance, which may identify areas for further study\"; it then gives \"point-by-point correlation of crystal structure data with other microscopic and microanalytical data\" (p.2)"
            }
          ],
          "schema:name": "no value available: schema:name"
        }
      ],
      "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Surface Science Western"
      },
      "schema:description": "Full spectral imaging (Quartz XOne): all X-rays recorded per pixel, allowing post-hoc spectral analysis",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "BSE Imaging (same instrument); CL (Hitachi S-2500C); micro-XRD; EPMA (out of scope)"
      }
    }
  ],
  "ada:analyticalMode": [
    "EDS Mapping"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only — \"the Tagish Lake sections\" (p.3), not individually labelled; the numbered points of Table 1 and Fig. 1 (e.g. \"point #1\", \"spot 34\") are μXRD spots, not SEM analyses",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": "all: 0.5 wt% — 'with a detection limit of 0.5 wt% for most elements' (p.3), a capability of the Quartz XOne system",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-detail-Izawa2010-3",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "ada:combinedResults": [
        {}
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
              "schema:value": "Micro X-ray diffraction reconnaissance \u2014 the paper's first stage is \"an initial, non-destructive in situ reconnaissance step using micro X-ray diffraction (mXRD) to document meteorite mineralogy and textures and to identify features of interest\", valuable as \"a 'no-touch' first-pass reconnaissance, which may identify areas for further study\"; it then gives \"point-by-point correlation of crystal structure data with other microscopic and microanalytical data\" (p.2)"
            }
          ],
          "schema:name": "no value available: schema:name"
        }
      ],
      "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Surface Science Western"
      },
      "schema:description": "Full spectral imaging (Quartz XOne): all X-rays recorded per pixel, allowing post-hoc spectral analysis",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "BSE Imaging (same instrument); CL (Hitachi S-2500C); micro-XRD; EPMA (out of scope)"
      }
    }
  ],
  "ada:analyticalMode": [
    "EDS Mapping"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only \u2014 \"the Tagish Lake sections\" (p.3), not individually labelled; the numbered points of Table 1 and Fig. 1 (e.g. \"point #1\", \"spot 34\") are \u03bcXRD spots, not SEM analyses",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": "all: 0.5 wt% \u2014 'with a detection limit of 0.5 wt% for most elements' (p.3), a capability of the Quartz XOne system",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:semTAPP-detail-Izawa2010-3 a schema1:Dataset,
        schema1:Product ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "BSE Imaging (same instrument); CL (Hitachi S-2500C); micro-XRD; EPMA (out of scope)" ] ] ;
    prov:wasGeneratedBy [ schema1:description "Full spectral imaging (Quartz XOne): all X-rays recorded per pixel, allowing post-hoc spectral analysis" ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Surface Science Western" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
                    schema1:name "no value available: schema:name" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            ada:combinedResults [ ] ;
            ada:edsDeadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "EDS Mapping" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit "all: 0.5 wt% — 'with a detection limit of 0.5 wt% for most elements' (p.3), a capability of the Quartz XOne system" ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimensions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Sample name only — \"the Tagish Lake sections\" (p.3), not individually labelled; the numbered points of Table 1 and Fig. 1 (e.g. \"point #1\", \"spot 34\") are μXRD spots, not SEM analyses" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "no value available: ada:voxelSize" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "Micro X-ray diffraction reconnaissance — the paper's first stage is \"an initial, non-destructive in situ reconnaissance step using micro X-ray diffraction (mXRD) to document meteorite mineralogy and textures and to identify features of interest\", valuable as \"a 'no-touch' first-pass reconnaissance, which may identify areas for further study\"; it then gives \"point-by-point correlation of crystal structure data with other microscopic and microanalytical data\" (p.2)" .


```


### detail example Izawa2010-4
detail instance derived from Izawa et al. 2010 | Tagish Lake (C2) meteorite | BSE Imaging (Leo 1540 FIB/SEM CrossBeam).
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
  "@id": "ex:semTAPP-detail-Izawa2010-4",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "ada:combinedResults": [
        {}
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
              "schema:value": "Micro X-ray diffraction reconnaissance — the paper's first stage is \"an initial, non-destructive in situ reconnaissance step using micro X-ray diffraction (mXRD) to document meteorite mineralogy and textures and to identify features of interest\", valuable as \"a 'no-touch' first-pass reconnaissance, which may identify areas for further study\"; it then gives \"point-by-point correlation of crystal structure data with other microscopic and microanalytical data\" (p.2); this procedure is the third stage, run on features the earlier stages located"
            }
          ],
          "schema:name": "no value available: schema:name"
        }
      ],
      "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Nanofabrication Laboratory, University of Western Ontario"
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "EDS (same instrument); BSE Imaging (Leo 440); CL (Hitachi S-2500C); micro-XRD; EPMA (out of scope)"
      }
    }
  ],
  "ada:analyticalMode": [
    "BSE Imaging"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only — \"the Tagish Lake sections\" (p.3), not individually labelled; the numbered points of Table 1 and Fig. 1 (e.g. \"point #1\", \"spot 34\") are μXRD spots, not SEM analyses",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-detail-Izawa2010-4",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "ada:combinedResults": [
        {}
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
              "schema:value": "Micro X-ray diffraction reconnaissance \u2014 the paper's first stage is \"an initial, non-destructive in situ reconnaissance step using micro X-ray diffraction (mXRD) to document meteorite mineralogy and textures and to identify features of interest\", valuable as \"a 'no-touch' first-pass reconnaissance, which may identify areas for further study\"; it then gives \"point-by-point correlation of crystal structure data with other microscopic and microanalytical data\" (p.2); this procedure is the third stage, run on features the earlier stages located"
            }
          ],
          "schema:name": "no value available: schema:name"
        }
      ],
      "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Nanofabrication Laboratory, University of Western Ontario"
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "EDS (same instrument); BSE Imaging (Leo 440); CL (Hitachi S-2500C); micro-XRD; EPMA (out of scope)"
      }
    }
  ],
  "ada:analyticalMode": [
    "BSE Imaging"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only \u2014 \"the Tagish Lake sections\" (p.3), not individually labelled; the numbered points of Table 1 and Fig. 1 (e.g. \"point #1\", \"spot 34\") are \u03bcXRD spots, not SEM analyses",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:semTAPP-detail-Izawa2010-4 a schema1:Dataset,
        schema1:Product ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "EDS (same instrument); BSE Imaging (Leo 440); CL (Hitachi S-2500C); micro-XRD; EPMA (out of scope)" ] ] ;
    prov:wasGeneratedBy [ schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Nanofabrication Laboratory, University of Western Ontario" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
                    schema1:name "no value available: schema:name" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            ada:combinedResults [ ] ;
            ada:edsDeadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "BSE Imaging" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimensions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Sample name only — \"the Tagish Lake sections\" (p.3), not individually labelled; the numbered points of Table 1 and Fig. 1 (e.g. \"point #1\", \"spot 34\") are μXRD spots, not SEM analyses" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "no value available: ada:voxelSize" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "Micro X-ray diffraction reconnaissance — the paper's first stage is \"an initial, non-destructive in situ reconnaissance step using micro X-ray diffraction (mXRD) to document meteorite mineralogy and textures and to identify features of interest\", valuable as \"a 'no-touch' first-pass reconnaissance, which may identify areas for further study\"; it then gives \"point-by-point correlation of crystal structure data with other microscopic and microanalytical data\" (p.2); this procedure is the third stage, run on features the earlier stages located" .


```


### detail example Izawa2010-5
detail instance derived from Izawa et al. 2010 | Tagish Lake (C2) meteorite | EDS Point Analysis (Leo 1540 FIB/SEM CrossBeam).
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
  "@id": "ex:semTAPP-detail-Izawa2010-5",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "ada:combinedResults": [
        {}
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
              "schema:value": "Micro X-ray diffraction reconnaissance — the paper's first stage is \"an initial, non-destructive in situ reconnaissance step using micro X-ray diffraction (mXRD) to document meteorite mineralogy and textures and to identify features of interest\", valuable as \"a 'no-touch' first-pass reconnaissance, which may identify areas for further study\"; it then gives \"point-by-point correlation of crystal structure data with other microscopic and microanalytical data\" (p.2); this procedure is the third stage, run on features the earlier stages located"
            }
          ],
          "schema:name": "no value available: schema:name"
        }
      ],
      "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Nanofabrication Laboratory, University of Western Ontario"
      },
      "schema:description": "Additional BSE and EDX analyses also carried out with Hitachi S-4300SE/N (Texas Tech) and Hitachi SU6600 (UWO) — not captured as separate assessment columns",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "BSE Imaging (same instrument); CL (Hitachi S-2500C); micro-XRD; EPMA (out of scope)"
      }
    }
  ],
  "ada:analyticalMode": [
    "EDS Point Analysis"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only — \"the Tagish Lake sections\" (p.3), not individually labelled; the numbered points of Table 1 and Fig. 1 (e.g. \"point #1\", \"spot 34\") are μXRD spots, not SEM analyses",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-detail-Izawa2010-5",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "ada:combinedResults": [
        {}
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
              "schema:value": "Micro X-ray diffraction reconnaissance \u2014 the paper's first stage is \"an initial, non-destructive in situ reconnaissance step using micro X-ray diffraction (mXRD) to document meteorite mineralogy and textures and to identify features of interest\", valuable as \"a 'no-touch' first-pass reconnaissance, which may identify areas for further study\"; it then gives \"point-by-point correlation of crystal structure data with other microscopic and microanalytical data\" (p.2); this procedure is the third stage, run on features the earlier stages located"
            }
          ],
          "schema:name": "no value available: schema:name"
        }
      ],
      "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Nanofabrication Laboratory, University of Western Ontario"
      },
      "schema:description": "Additional BSE and EDX analyses also carried out with Hitachi S-4300SE/N (Texas Tech) and Hitachi SU6600 (UWO) \u2014 not captured as separate assessment columns",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "BSE Imaging (same instrument); CL (Hitachi S-2500C); micro-XRD; EPMA (out of scope)"
      }
    }
  ],
  "ada:analyticalMode": [
    "EDS Point Analysis"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only \u2014 \"the Tagish Lake sections\" (p.3), not individually labelled; the numbered points of Table 1 and Fig. 1 (e.g. \"point #1\", \"spot 34\") are \u03bcXRD spots, not SEM analyses",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:semTAPP-detail-Izawa2010-5 a schema1:Dataset,
        schema1:Product ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "BSE Imaging (same instrument); CL (Hitachi S-2500C); micro-XRD; EPMA (out of scope)" ] ] ;
    prov:wasGeneratedBy [ schema1:description "Additional BSE and EDX analyses also carried out with Hitachi S-4300SE/N (Texas Tech) and Hitachi SU6600 (UWO) — not captured as separate assessment columns" ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Nanofabrication Laboratory, University of Western Ontario" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
                    schema1:name "no value available: schema:name" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            ada:combinedResults [ ] ;
            ada:edsDeadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "EDS Point Analysis" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimensions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Sample name only — \"the Tagish Lake sections\" (p.3), not individually labelled; the numbered points of Table 1 and Fig. 1 (e.g. \"point #1\", \"spot 34\") are μXRD spots, not SEM analyses" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "no value available: ada:voxelSize" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "Micro X-ray diffraction reconnaissance — the paper's first stage is \"an initial, non-destructive in situ reconnaissance step using micro X-ray diffraction (mXRD) to document meteorite mineralogy and textures and to identify features of interest\", valuable as \"a 'no-touch' first-pass reconnaissance, which may identify areas for further study\"; it then gives \"point-by-point correlation of crystal structure data with other microscopic and microanalytical data\" (p.2); this procedure is the third stage, run on features the earlier stages located" .


```


### detail example Liu2017
detail instance derived from Liu et al. 2017 | High-rank coal (Qinshui basin) | 3D Tomography (Carl Zeiss Crossbeam 540).
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
  "@id": "ex:semTAPP-detail-Liu2017",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/semTAPP/segmentationMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semTAPP/segmentationMethod"
            }
          ],
          "schema:name": "Segmentation Method",
          "schema:value": "Image denoising, binarization, and segmentation; 3D model established using Avizo 7 and Multiple-point geostatistics"
        }
      ],
      "ada:combinedResults": [
        {}
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
              "schema:value": "N — X-ray micro-CT is run on the same samples (\"The scanning area of the X-ray CT scan was 2 mm in diameter and 1 mm in height ... pixel resolution was 1 µm\", p.3), but as a parallel measurement feeding the same pore-network model, not as a screening step that sites the FIB-SEM volume"
            },
            {
              "@id": "ada:parameter/semTAPP/sliceThickness",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/semTAPP/sliceThickness"
                }
              ],
              "schema:name": "Slice Thickness",
              "schema:value": 15,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "15 nm (single layer scanning thickness = 9.0 µm total / 600 slices)"
            }
          ],
          "schema:name": "no value available: schema:name"
        }
      ],
      "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:additionalProperty": [
              {
                "@id": "ada:parameter/semTAPP/protectiveCoatingDeposition",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/semTAPP/protectiveCoatingDeposition"
                  }
                ],
                "schema:name": "Protective Coating Deposition",
                "schema:value": "No coating applied; not sputtered with gold or other materials"
              }
            ],
            "schema:description": "Small coal pillars (~2 mm diameter, 2 mm height) drilled orthogonal to bedding; polished with cross section polisher to remove ~1-2 µm oxide layer; no coating applied",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          },
          {
            "schema:name": "Ion milling",
            "schema:position": 3,
            "schema:description": "no value available: schema:description",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "China University of Mining and Technology, Xuzhou, China"
      },
      "schema:instrument": [
        {
          "ada:toolRole": "dataReduction",
          "schema:name": "Avizo 7 (3D digital core software); Multiple-point geostatistics for pore network model",
          "@type": [
            "schema:SoftwareApplication"
          ],
          "schema:additionalType": [
            {
              "@id": "https://www.wikidata.org/entity/Q7397"
            }
          ]
        },
        {
          "schema:additionalType": [
            "SEM",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "SEM",
          "@id": "ex:semTAPP-detail-Liu2017/instrument/SEM"
        }
      ],
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "ada:voxelSize": "9.8 × 9.8 × 15 nm voxel size; 600 slices; 7.8 × 7.8 µm scanning area; 9.0 µm total thickness",
  "ada:imageStackDimensions": "9.8 × 9.8 × 15 nm voxel size; 600 slices; 7.8 × 7.8 µm scanning area; 9.0 µm total thickness",
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "X-ray CT (Xradia 520 Versa, Carl Zeiss)"
      }
    }
  ],
  "ada:analyticalMode": [
    "3D Tomography"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Labelled: coal samples \"#1\" (Bofang Mine) and \"#2\" (Yuwu Mine) (Table 1, p.2); the 3D pore-network model \"only focuses on the coal sample #1\" (p.8)",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-detail-Liu2017",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/semTAPP/segmentationMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semTAPP/segmentationMethod"
            }
          ],
          "schema:name": "Segmentation Method",
          "schema:value": "Image denoising, binarization, and segmentation; 3D model established using Avizo 7 and Multiple-point geostatistics"
        }
      ],
      "ada:combinedResults": [
        {}
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
              "schema:value": "N \u2014 X-ray micro-CT is run on the same samples (\"The scanning area of the X-ray CT scan was 2 mm in diameter and 1 mm in height ... pixel resolution was 1 \u00b5m\", p.3), but as a parallel measurement feeding the same pore-network model, not as a screening step that sites the FIB-SEM volume"
            },
            {
              "@id": "ada:parameter/semTAPP/sliceThickness",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/semTAPP/sliceThickness"
                }
              ],
              "schema:name": "Slice Thickness",
              "schema:value": 15,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "15 nm (single layer scanning thickness = 9.0 \u00b5m total / 600 slices)"
            }
          ],
          "schema:name": "no value available: schema:name"
        }
      ],
      "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:additionalProperty": [
              {
                "@id": "ada:parameter/semTAPP/protectiveCoatingDeposition",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/semTAPP/protectiveCoatingDeposition"
                  }
                ],
                "schema:name": "Protective Coating Deposition",
                "schema:value": "No coating applied; not sputtered with gold or other materials"
              }
            ],
            "schema:description": "Small coal pillars (~2 mm diameter, 2 mm height) drilled orthogonal to bedding; polished with cross section polisher to remove ~1-2 \u00b5m oxide layer; no coating applied",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          },
          {
            "schema:name": "Ion milling",
            "schema:position": 3,
            "schema:description": "no value available: schema:description",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "China University of Mining and Technology, Xuzhou, China"
      },
      "schema:instrument": [
        {
          "ada:toolRole": "dataReduction",
          "schema:name": "Avizo 7 (3D digital core software); Multiple-point geostatistics for pore network model",
          "@type": [
            "schema:SoftwareApplication"
          ],
          "schema:additionalType": [
            {
              "@id": "https://www.wikidata.org/entity/Q7397"
            }
          ]
        },
        {
          "schema:additionalType": [
            "SEM",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "SEM",
          "@id": "ex:semTAPP-detail-Liu2017/instrument/SEM"
        }
      ],
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "ada:voxelSize": "9.8 \u00d7 9.8 \u00d7 15 nm voxel size; 600 slices; 7.8 \u00d7 7.8 \u00b5m scanning area; 9.0 \u00b5m total thickness",
  "ada:imageStackDimensions": "9.8 \u00d7 9.8 \u00d7 15 nm voxel size; 600 slices; 7.8 \u00d7 7.8 \u00b5m scanning area; 9.0 \u00b5m total thickness",
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "X-ray CT (Xradia 520 Versa, Carl Zeiss)"
      }
    }
  ],
  "ada:analyticalMode": [
    "3D Tomography"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Labelled: coal samples \"#1\" (Bofang Mine) and \"#2\" (Yuwu Mine) (Table 1, p.2); the 3D pore-network model \"only focuses on the coal sample #1\" (p.8)",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix wd: <https://www.wikidata.org/entity/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:semTAPP-detail-Liu2017 a schema1:Dataset,
        schema1:Product ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "X-ray CT (Xradia 520 Versa, Carl Zeiss)" ] ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semTAPP/protectiveCoatingDeposition> ;
                            schema1:description "Small coal pillars (~2 mm diameter, 2 mm height) drilled orthogonal to bedding; polished with cross section polisher to remove ~1-2 µm oxide layer; no coating applied" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "no value available: schema:description" ;
                            schema1:name "Ion milling" ;
                            schema1:position 3 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semTAPP/segmentationMethod> ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:instrument [ a schema1:SoftwareApplication ;
                    schema1:additionalType wd:Q7397 ;
                    schema1:name "Avizo 7 (3D digital core software); Multiple-point geostatistics for pore network model" ;
                    ada:toolRole "dataReduction" ],
                <https://example.org/semTAPP-detail-Liu2017/instrument/SEM> ;
            schema1:location [ a schema1:Place ;
                    schema1:name "China University of Mining and Technology, Xuzhou, China" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening>,
                        <https://ada.astromat.org/metadata/parameter/semTAPP/sliceThickness> ;
                    schema1:name "no value available: schema:name" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            ada:combinedResults [ ] ;
            ada:edsDeadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "3D Tomography" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimensions "9.8 × 9.8 × 15 nm voxel size; 600 slices; 7.8 × 7.8 µm scanning area; 9.0 µm total thickness" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Labelled: coal samples \"#1\" (Bofang Mine) and \"#2\" (Yuwu Mine) (Table 1, p.2); the 3D pore-network model \"only focuses on the coal sample #1\" (p.8)" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "9.8 × 9.8 × 15 nm voxel size; 600 slices; 7.8 × 7.8 µm scanning area; 9.0 µm total thickness" .

<https://example.org/semTAPP-detail-Liu2017/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType wd:Q3099911,
        "SEM" ;
    schema1:name "SEM" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "N — X-ray micro-CT is run on the same samples (\"The scanning area of the X-ray CT scan was 2 mm in diameter and 1 mm in height ... pixel resolution was 1 µm\", p.3), but as a parallel measurement feeding the same pore-network model, not as a screening step that sites the FIB-SEM volume" .

<https://ada.astromat.org/metadata/parameter/semTAPP/protectiveCoatingDeposition> a schema1:PropertyValue ;
    schema1:name "Protective Coating Deposition" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/protectiveCoatingDeposition> ;
    schema1:value "No coating applied; not sputtered with gold or other materials" .

<https://ada.astromat.org/metadata/parameter/semTAPP/segmentationMethod> a schema1:PropertyValue ;
    schema1:name "Segmentation Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/segmentationMethod> ;
    schema1:value "Image denoising, binarization, and segmentation; 3D model established using Avizo 7 and Multiple-point geostatistics" .

<https://ada.astromat.org/metadata/parameter/semTAPP/sliceThickness> a schema1:PropertyValue ;
    schema1:description "15 nm (single layer scanning thickness = 9.0 µm total / 600 slices)" ;
    schema1:name "Slice Thickness" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/sliceThickness> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 15 .


```


### detail example Liu2017-2
detail instance derived from Liu et al. 2017 | High-rank coal (Qinshui basin) | SE Imaging (ESEM Quanta 250).
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
  "@id": "ex:semTAPP-detail-Liu2017-2",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "ada:combinedResults": [
        {}
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/semTAPP/chamberPressure",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semTAPP/chamberPressure"
            }
          ],
          "schema:name": "Chamber Pressure",
          "schema:value": "High vacuum",
          "schema:unitText": "no value available: unnamed property"
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
              "schema:value": "N — the imaging this procedure performs is its own measurement, not a screening step before it; the paper describes no prior characterisation used to locate the units"
            }
          ],
          "schema:name": "no value available: schema:name"
        }
      ],
      "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "China University of Mining and Technology, Xuzhou, China"
      },
      "schema:description": "Pore and mineral sizes >0.1 µm measured; minerals analyzed via EDS (surface energy spectrum analysis); magnification range 10³ to 10⁴",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Bulk coal polished to ~10 mm × 2-3 mm using polishing and burnishing machine; further polished with cross section polisher; thin gold coating applied by sputtering",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          },
          {
            "schema:name": "Ion milling",
            "schema:position": 3,
            "schema:description": "no value available: schema:description",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "FIB-SEM (Crossbeam 540) for 3D tomography; EDS for mineral analysis"
      }
    }
  ],
  "ada:analyticalMode": [
    "SE Imaging"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Labelled: coal samples \"#1\" (Bofang Mine) and \"#2\" (Yuwu Mine) (Table 1, p.2); imaged areas are not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-detail-Liu2017-2",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "ada:combinedResults": [
        {}
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/semTAPP/chamberPressure",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semTAPP/chamberPressure"
            }
          ],
          "schema:name": "Chamber Pressure",
          "schema:value": "High vacuum",
          "schema:unitText": "no value available: unnamed property"
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
              "schema:value": "N \u2014 the imaging this procedure performs is its own measurement, not a screening step before it; the paper describes no prior characterisation used to locate the units"
            }
          ],
          "schema:name": "no value available: schema:name"
        }
      ],
      "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "China University of Mining and Technology, Xuzhou, China"
      },
      "schema:description": "Pore and mineral sizes >0.1 \u00b5m measured; minerals analyzed via EDS (surface energy spectrum analysis); magnification range 10\u00b3 to 10\u2074",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Bulk coal polished to ~10 mm \u00d7 2-3 mm using polishing and burnishing machine; further polished with cross section polisher; thin gold coating applied by sputtering",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          },
          {
            "schema:name": "Ion milling",
            "schema:position": 3,
            "schema:description": "no value available: schema:description",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "FIB-SEM (Crossbeam 540) for 3D tomography; EDS for mineral analysis"
      }
    }
  ],
  "ada:analyticalMode": [
    "SE Imaging"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Labelled: coal samples \"#1\" (Bofang Mine) and \"#2\" (Yuwu Mine) (Table 1, p.2); imaged areas are not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:semTAPP-detail-Liu2017-2 a schema1:Dataset,
        schema1:Product ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "FIB-SEM (Crossbeam 540) for 3D tomography; EDS for mineral analysis" ] ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Bulk coal polished to ~10 mm × 2-3 mm using polishing and burnishing machine; further polished with cross section polisher; thin gold coating applied by sputtering" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "no value available: schema:description" ;
                            schema1:name "Ion milling" ;
                            schema1:position 3 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semTAPP/chamberPressure> ;
            schema1:description "Pore and mineral sizes >0.1 µm measured; minerals analyzed via EDS (surface energy spectrum analysis); magnification range 10³ to 10⁴" ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "China University of Mining and Technology, Xuzhou, China" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
                    schema1:name "no value available: schema:name" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            ada:combinedResults [ ] ;
            ada:edsDeadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "SE Imaging" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimensions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Labelled: coal samples \"#1\" (Bofang Mine) and \"#2\" (Yuwu Mine) (Table 1, p.2); imaged areas are not labelled" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "no value available: ada:voxelSize" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "N — the imaging this procedure performs is its own measurement, not a screening step before it; the paper describes no prior characterisation used to locate the units" .

<https://ada.astromat.org/metadata/parameter/semTAPP/chamberPressure> a schema1:PropertyValue ;
    schema1:name "Chamber Pressure" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/chamberPressure> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value "High vacuum" .


```


### detail example Liu2017-3
detail instance derived from Liu et al. 2017 | High-rank coal (Qinshui basin) | SE Imaging (FESEM SUPRA 55).
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
  "@id": "ex:semTAPP-detail-Liu2017-3",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "ada:combinedResults": [
        {}
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/semTAPP/chamberPressure",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semTAPP/chamberPressure"
            }
          ],
          "schema:name": "Chamber Pressure",
          "schema:value": "High vacuum",
          "schema:unitText": "no value available: unnamed property"
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
              "schema:value": "N — the imaging this procedure performs is its own measurement, not a screening step before it; the paper describes no prior characterisation used to locate the units"
            }
          ],
          "schema:name": "no value available: schema:name"
        }
      ],
      "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "China University of Mining and Technology, Xuzhou, China"
      },
      "schema:description": "Pore and mineral sizes >20 nm to <5 µm measured; EDS also used for mineral analysis; magnification range 10³ to 10⁵",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Bulk coal polished to ~10 mm × 2-3 mm using polishing and burnishing machine; further polished with cross section polisher; thin gold coating applied by sputtering",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          },
          {
            "schema:name": "Ion milling",
            "schema:position": 3,
            "schema:description": "no value available: schema:description",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "FIB-SEM (Crossbeam 540) for 3D tomography; EDS for mineral analysis"
      }
    }
  ],
  "ada:analyticalMode": [
    "SE Imaging"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Labelled: coal samples \"#1\" (Bofang Mine) and \"#2\" (Yuwu Mine) (Table 1, p.2); imaged areas are not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-detail-Liu2017-3",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "ada:combinedResults": [
        {}
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/semTAPP/chamberPressure",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semTAPP/chamberPressure"
            }
          ],
          "schema:name": "Chamber Pressure",
          "schema:value": "High vacuum",
          "schema:unitText": "no value available: unnamed property"
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
              "schema:value": "N \u2014 the imaging this procedure performs is its own measurement, not a screening step before it; the paper describes no prior characterisation used to locate the units"
            }
          ],
          "schema:name": "no value available: schema:name"
        }
      ],
      "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "China University of Mining and Technology, Xuzhou, China"
      },
      "schema:description": "Pore and mineral sizes >20 nm to <5 \u00b5m measured; EDS also used for mineral analysis; magnification range 10\u00b3 to 10\u2075",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Bulk coal polished to ~10 mm \u00d7 2-3 mm using polishing and burnishing machine; further polished with cross section polisher; thin gold coating applied by sputtering",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          },
          {
            "schema:name": "Ion milling",
            "schema:position": 3,
            "schema:description": "no value available: schema:description",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "FIB-SEM (Crossbeam 540) for 3D tomography; EDS for mineral analysis"
      }
    }
  ],
  "ada:analyticalMode": [
    "SE Imaging"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Labelled: coal samples \"#1\" (Bofang Mine) and \"#2\" (Yuwu Mine) (Table 1, p.2); imaged areas are not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:semTAPP-detail-Liu2017-3 a schema1:Dataset,
        schema1:Product ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "FIB-SEM (Crossbeam 540) for 3D tomography; EDS for mineral analysis" ] ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Bulk coal polished to ~10 mm × 2-3 mm using polishing and burnishing machine; further polished with cross section polisher; thin gold coating applied by sputtering" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "no value available: schema:description" ;
                            schema1:name "Ion milling" ;
                            schema1:position 3 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semTAPP/chamberPressure> ;
            schema1:description "Pore and mineral sizes >20 nm to <5 µm measured; EDS also used for mineral analysis; magnification range 10³ to 10⁵" ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "China University of Mining and Technology, Xuzhou, China" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
                    schema1:name "no value available: schema:name" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            ada:combinedResults [ ] ;
            ada:edsDeadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "SE Imaging" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimensions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Labelled: coal samples \"#1\" (Bofang Mine) and \"#2\" (Yuwu Mine) (Table 1, p.2); imaged areas are not labelled" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "no value available: ada:voxelSize" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "N — the imaging this procedure performs is its own measurement, not a screening step before it; the paper describes no prior characterisation used to locate the units" .

<https://ada.astromat.org/metadata/parameter/semTAPP/chamberPressure> a schema1:PropertyValue ;
    schema1:name "Chamber Pressure" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/chamberPressure> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value "High vacuum" .


```


### detail example Ma2017
detail instance derived from Ma et al. 2017 | Khatyrka CV3 chondrite (metal phases) | BSE Imaging (ZEISS 1550VP FE-SEM).
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
  "@id": "ex:semTAPP-detail-Ma2017",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "ada:combinedResults": [
        {}
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
              "schema:value": "N — the imaging this procedure performs is its own measurement, not a screening step before it; the paper describes no prior characterisation used to locate the units"
            }
          ],
          "schema:name": "Section 126A (USNM 7908)",
          "schema:identifier": "USNM 7908 (section 126A)"
        }
      ],
      "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Caltech GPS Analytical Facility, California Institute of Technology, Pasadena, CA, USA"
      },
      "schema:description": "BSE images obtained from both ZEISS 1550VP FE-SEM and JEOL 8200 electron microprobe (EPMA); quantitative EPMA on JEOL 8200 at 12 kV, 5 nA (out of scope for SEM TAPP)",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Polished thin section (section 126A prepared from Grain 126); no coating or SEM-specific preparation stated",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          },
          {
            "schema:name": "Ion milling",
            "schema:position": 3,
            "schema:description": "no value available: schema:description",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NSF EAR-0318518; NSF DMR-0080065 (supporting Caltech GPS Analytical Facility)"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "EBSD (ZEISS 1550VP FE-SEM); EPMA (JEOL 8200, separate instrument)"
      }
    }
  ],
  "ada:analyticalMode": [
    "BSE Imaging"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NSF EAR-0318518; NSF DMR-0080065 (supporting Caltech GPS Analytical Facility)",
  "ada:sampleName": "Section 126A (USNM 7908)",
  "ada:samplingUnitName": "Labelled: \"section 126A of USNM 7908\" (p.1), \"prepared from a larger Grain 126\" (p.2); the three mineral locations are \"marked by rectangles\" in Fig. 1 (p.2), not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-detail-Ma2017",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "ada:combinedResults": [
        {}
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
              "schema:value": "N \u2014 the imaging this procedure performs is its own measurement, not a screening step before it; the paper describes no prior characterisation used to locate the units"
            }
          ],
          "schema:name": "Section 126A (USNM 7908)",
          "schema:identifier": "USNM 7908 (section 126A)"
        }
      ],
      "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Caltech GPS Analytical Facility, California Institute of Technology, Pasadena, CA, USA"
      },
      "schema:description": "BSE images obtained from both ZEISS 1550VP FE-SEM and JEOL 8200 electron microprobe (EPMA); quantitative EPMA on JEOL 8200 at 12 kV, 5 nA (out of scope for SEM TAPP)",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Polished thin section (section 126A prepared from Grain 126); no coating or SEM-specific preparation stated",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          },
          {
            "schema:name": "Ion milling",
            "schema:position": 3,
            "schema:description": "no value available: schema:description",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NSF EAR-0318518; NSF DMR-0080065 (supporting Caltech GPS Analytical Facility)"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "EBSD (ZEISS 1550VP FE-SEM); EPMA (JEOL 8200, separate instrument)"
      }
    }
  ],
  "ada:analyticalMode": [
    "BSE Imaging"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NSF EAR-0318518; NSF DMR-0080065 (supporting Caltech GPS Analytical Facility)",
  "ada:sampleName": "Section 126A (USNM 7908)",
  "ada:samplingUnitName": "Labelled: \"section 126A of USNM 7908\" (p.1), \"prepared from a larger Grain 126\" (p.2); the three mineral locations are \"marked by rectangles\" in Fig. 1 (p.2), not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:semTAPP-detail-Ma2017 a schema1:Dataset,
        schema1:Product ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "NSF EAR-0318518; NSF DMR-0080065 (supporting Caltech GPS Analytical Facility)" ] ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "EBSD (ZEISS 1550VP FE-SEM); EPMA (JEOL 8200, separate instrument)" ] ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "no value available: schema:description" ;
                            schema1:name "Ion milling" ;
                            schema1:position 3 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Polished thin section (section 126A prepared from Grain 126); no coating or SEM-specific preparation stated" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ] ] ;
            schema1:description "BSE images obtained from both ZEISS 1550VP FE-SEM and JEOL 8200 electron microprobe (EPMA); quantitative EPMA on JEOL 8200 at 12 kV, 5 nA (out of scope for SEM TAPP)" ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Caltech GPS Analytical Facility, California Institute of Technology, Pasadena, CA, USA" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
                    schema1:identifier "USNM 7908 (section 126A)" ;
                    schema1:name "Section 126A (USNM 7908)" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            ada:combinedResults [ ] ;
            ada:edsDeadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "BSE Imaging" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NSF EAR-0318518; NSF DMR-0080065 (supporting Caltech GPS Analytical Facility)" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimensions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:sampleName "Section 126A (USNM 7908)" ;
    ada:samplingUnitName "Labelled: \"section 126A of USNM 7908\" (p.1), \"prepared from a larger Grain 126\" (p.2); the three mineral locations are \"marked by rectangles\" in Fig. 1 (p.2), not labelled" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "no value available: ada:voxelSize" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "N — the imaging this procedure performs is its own measurement, not a screening step before it; the paper describes no prior characterisation used to locate the units" .


```


### detail example Ma2017-2
detail instance derived from Ma et al. 2017 | Khatyrka CV3 chondrite (metal phases) | EBSD (ZEISS 1550VP FE-SEM, HKL system, 20 kV).
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
  "@id": "ex:semTAPP-detail-Ma2017-2",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "ada:combinedResults": [
        {}
      ],
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Data processing",
            "schema:additionalProperty": [
              {
                "@id": "ada:parameter/semTAPP/crystalStructureDatabase",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/semTAPP/crystalStructureDatabase"
                  }
                ],
                "schema:name": "Crystal Structure Database",
                "schema:value": "Literature crystal structures: Black et al. 1961 (Cmc21 (Al,Cu)Fe6 for kryachkoite); Zhang et al. 2005 (Pm3m AlCu for stolperite)"
              }
            ],
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Sample preparation",
            "schema:description": "Polished thin section (section 126A prepared from Grain 126); no coating or EBSD-specific preparation stated",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          },
          {
            "schema:name": "Ion milling",
            "schema:position": 3,
            "schema:description": "no value available: schema:description",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/semTAPP/ebsdPhaseList",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semTAPP/ebsdPhaseList"
            }
          ],
          "schema:name": "EBSD Phase List",
          "schema:value": "Hollisterite (C2/m FeAl3); kryachkoite (Cmc21 (Al,Cu)Fe6); stolperite (Pm3m AlCu)"
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
              "schema:value": "N — no prior screening is described; the EBSD patterns are acquired on the same instrument as the BSE imaging, \"an HKL EBSD system on the ZEISS 1550VP SEM\" (p.2)"
            }
          ],
          "schema:name": "Section 126A (USNM 7908)",
          "schema:identifier": "USNM 7908 (section 126A)"
        }
      ],
      "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Caltech GPS Analytical Facility, California Institute of Technology, Pasadena, CA, USA"
      },
      "schema:description": "EBSD performed at Caltech GPS Analytical Facility; EPMA (JEOL 8200) used for quantitative chemical analysis (out of scope for SEM TAPP)",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "EBSD Mean Angular Deviation",
      "dqv:value": "0.30°~0.45° (all three mineral phases: hollisterite, kryachkoite, stolperite)"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "EBSD Indexing Rate",
      "dqv:value": -9999
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NSF EAR-0318518; NSF DMR-0080065 (supporting Caltech GPS Analytical Facility)"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "BSE Imaging (ZEISS 1550VP FE-SEM); EPMA (JEOL 8200, separate instrument)"
      }
    }
  ],
  "ada:analyticalMode": [
    "EBSD"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NSF EAR-0318518; NSF DMR-0080065 (supporting Caltech GPS Analytical Facility)",
  "ada:sampleName": "Section 126A (USNM 7908)",
  "ada:samplingUnitName": "Labelled: \"section 126A of USNM 7908\" (p.1), \"prepared from a larger Grain 126\" (p.2); the three mineral locations are \"marked by rectangles\" in Fig. 1 (p.2), not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-detail-Ma2017-2",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "ada:combinedResults": [
        {}
      ],
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Data processing",
            "schema:additionalProperty": [
              {
                "@id": "ada:parameter/semTAPP/crystalStructureDatabase",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/semTAPP/crystalStructureDatabase"
                  }
                ],
                "schema:name": "Crystal Structure Database",
                "schema:value": "Literature crystal structures: Black et al. 1961 (Cmc21 (Al,Cu)Fe6 for kryachkoite); Zhang et al. 2005 (Pm3m AlCu for stolperite)"
              }
            ],
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Sample preparation",
            "schema:description": "Polished thin section (section 126A prepared from Grain 126); no coating or EBSD-specific preparation stated",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          },
          {
            "schema:name": "Ion milling",
            "schema:position": 3,
            "schema:description": "no value available: schema:description",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/semTAPP/ebsdPhaseList",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semTAPP/ebsdPhaseList"
            }
          ],
          "schema:name": "EBSD Phase List",
          "schema:value": "Hollisterite (C2/m FeAl3); kryachkoite (Cmc21 (Al,Cu)Fe6); stolperite (Pm3m AlCu)"
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
              "schema:value": "N \u2014 no prior screening is described; the EBSD patterns are acquired on the same instrument as the BSE imaging, \"an HKL EBSD system on the ZEISS 1550VP SEM\" (p.2)"
            }
          ],
          "schema:name": "Section 126A (USNM 7908)",
          "schema:identifier": "USNM 7908 (section 126A)"
        }
      ],
      "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Caltech GPS Analytical Facility, California Institute of Technology, Pasadena, CA, USA"
      },
      "schema:description": "EBSD performed at Caltech GPS Analytical Facility; EPMA (JEOL 8200) used for quantitative chemical analysis (out of scope for SEM TAPP)",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "EBSD Mean Angular Deviation",
      "dqv:value": "0.30\u00b0~0.45\u00b0 (all three mineral phases: hollisterite, kryachkoite, stolperite)"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "EBSD Indexing Rate",
      "dqv:value": -9999
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NSF EAR-0318518; NSF DMR-0080065 (supporting Caltech GPS Analytical Facility)"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "BSE Imaging (ZEISS 1550VP FE-SEM); EPMA (JEOL 8200, separate instrument)"
      }
    }
  ],
  "ada:analyticalMode": [
    "EBSD"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NSF EAR-0318518; NSF DMR-0080065 (supporting Caltech GPS Analytical Facility)",
  "ada:sampleName": "Section 126A (USNM 7908)",
  "ada:samplingUnitName": "Labelled: \"section 126A of USNM 7908\" (p.1), \"prepared from a larger Grain 126\" (p.2); the three mineral locations are \"marked by rectangles\" in Fig. 1 (p.2), not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix dqv: <http://www.w3.org/ns/dqv#> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:semTAPP-detail-Ma2017-2 a schema1:Dataset,
        schema1:Product ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "NSF EAR-0318518; NSF DMR-0080065 (supporting Caltech GPS Analytical Facility)" ] ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "BSE Imaging (ZEISS 1550VP FE-SEM); EPMA (JEOL 8200, separate instrument)" ] ] ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Analytical Precision" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "EBSD Mean Angular Deviation" ;
            dqv:value "0.30°~0.45° (all three mineral phases: hollisterite, kryachkoite, stolperite)" ],
        [ dqv:isMeasurementOf "EBSD Indexing Rate" ;
            dqv:value -9999 ],
        [ dqv:isMeasurementOf "Analytical Accuracy" ;
            dqv:value "no value available: dqv:value" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semTAPP/crystalStructureDatabase> ;
                            schema1:name "Data processing" ;
                            schema1:position 1 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Polished thin section (section 126A prepared from Grain 126); no coating or EBSD-specific preparation stated" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 2 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "no value available: schema:description" ;
                            schema1:name "Ion milling" ;
                            schema1:position 3 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semTAPP/ebsdPhaseList> ;
            schema1:description "EBSD performed at Caltech GPS Analytical Facility; EPMA (JEOL 8200) used for quantitative chemical analysis (out of scope for SEM TAPP)" ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Caltech GPS Analytical Facility, California Institute of Technology, Pasadena, CA, USA" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
                    schema1:identifier "USNM 7908 (section 126A)" ;
                    schema1:name "Section 126A (USNM 7908)" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            ada:combinedResults [ ] ;
            ada:edsDeadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "EBSD" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NSF EAR-0318518; NSF DMR-0080065 (supporting Caltech GPS Analytical Facility)" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimensions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:sampleName "Section 126A (USNM 7908)" ;
    ada:samplingUnitName "Labelled: \"section 126A of USNM 7908\" (p.1), \"prepared from a larger Grain 126\" (p.2); the three mineral locations are \"marked by rectangles\" in Fig. 1 (p.2), not labelled" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "no value available: ada:voxelSize" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "N — no prior screening is described; the EBSD patterns are acquired on the same instrument as the BSE imaging, \"an HKL EBSD system on the ZEISS 1550VP SEM\" (p.2)" .

<https://ada.astromat.org/metadata/parameter/semTAPP/crystalStructureDatabase> a schema1:PropertyValue ;
    schema1:name "Crystal Structure Database" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/crystalStructureDatabase> ;
    schema1:value "Literature crystal structures: Black et al. 1961 (Cmc21 (Al,Cu)Fe6 for kryachkoite); Zhang et al. 2005 (Pm3m AlCu for stolperite)" .

<https://ada.astromat.org/metadata/parameter/semTAPP/ebsdPhaseList> a schema1:PropertyValue ;
    schema1:name "EBSD Phase List" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/ebsdPhaseList> ;
    schema1:value "Hollisterite (C2/m FeAl3); kryachkoite (Cmc21 (Al,Cu)Fe6); stolperite (Pm3m AlCu)" .


```


### detail example Pascucci2026
detail instance derived from Pascucci et al. 2026 | NWA 7317 CR6 chondrite | BSE Imaging (Zeiss Supra 40 FE-SEM, 20 kV).
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
  "@id": "ex:semTAPP-detail-Pascucci2026",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:instrument": [
        {
          "schema:additionalType": [
            "SEM",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/semTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/semTAPP/acceleratingVoltage"
                }
              ],
              "schema:name": "Accelerating Voltage",
              "schema:value": 20,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "20 kV"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:semTAPP-detail-Pascucci2026/instrument/SEM"
        },
        {
          "ada:toolRole": "acquisition",
          "schema:name": "Oxford INCA Energy",
          "@type": [
            "schema:SoftwareApplication"
          ],
          "schema:additionalType": [
            {
              "@id": "https://www.wikidata.org/entity/Q7397"
            }
          ]
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/semTAPP/chamberPressure",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semTAPP/chamberPressure"
            }
          ],
          "schema:name": "Chamber Pressure",
          "schema:value": "High vacuum",
          "schema:unitText": "no value available: unnamed property"
        },
        {
          "@id": "ada:parameter/semTAPP/workingDistance",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semTAPP/workingDistance"
            }
          ],
          "schema:name": "Working Distance",
          "schema:value": 8,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "8 mm"
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
              "schema:value": "VIS-IR imaging spectroscopy, acquired before the section was prepared — the fragment was embedded and polished \"after the SPectral IMager (SPIM) reflectance spectroscopy imagery acquisition\" and only then carbon coated \"for further SEM-EDS and EMPA-WDS analyses\" (p.3). The SEM work is then registered to those images: \"To cover approximately the same area of the SPIM images (9.7 mm large), 10 BSE images, with four consecutive images in the same row, were acquired and mosaicked\" (p.3)"
            }
          ],
          "schema:name": "NWA 7317"
        }
      ],
      "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "CNR IMAA (Institute of Methodologies for Environmental Analysis), Italian National Research Council, Potenza, Italy"
      },
      "schema:description": "10 BSE images acquired at ×138 magnification and mosaicked (4 consecutive per row) to cover ~9.7 mm area matching SPIM imagery",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Embedded in epoxy, polished to ¼ µm level, sputtered with 30-nm-thick carbon film",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          },
          {
            "schema:name": "Ion milling",
            "schema:position": 3,
            "schema:description": "no value available: schema:description",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "EDS (Zeiss Supra 40 FE-SEM); SE Imaging (Zeiss Supra 40 FE-SEM); EMPA-WDS (JEOL JXA-8230, separate instrument); VIS-IR spectroscopy (SPIM)"
      }
    }
  ],
  "ada:analyticalMode": [
    "BSE Imaging"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "NWA 7317",
  "ada:samplingUnitName": "Sample name only — \"the NWA 7317 slab\" (p.3), imaged on \"almost the same portion of the VIS-IR SPIM images\" (p.4); imaged fields and analysis points are not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-detail-Pascucci2026",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:instrument": [
        {
          "schema:additionalType": [
            "SEM",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/semTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/semTAPP/acceleratingVoltage"
                }
              ],
              "schema:name": "Accelerating Voltage",
              "schema:value": 20,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "20 kV"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:semTAPP-detail-Pascucci2026/instrument/SEM"
        },
        {
          "ada:toolRole": "acquisition",
          "schema:name": "Oxford INCA Energy",
          "@type": [
            "schema:SoftwareApplication"
          ],
          "schema:additionalType": [
            {
              "@id": "https://www.wikidata.org/entity/Q7397"
            }
          ]
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/semTAPP/chamberPressure",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semTAPP/chamberPressure"
            }
          ],
          "schema:name": "Chamber Pressure",
          "schema:value": "High vacuum",
          "schema:unitText": "no value available: unnamed property"
        },
        {
          "@id": "ada:parameter/semTAPP/workingDistance",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semTAPP/workingDistance"
            }
          ],
          "schema:name": "Working Distance",
          "schema:value": 8,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "8 mm"
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
              "schema:value": "VIS-IR imaging spectroscopy, acquired before the section was prepared \u2014 the fragment was embedded and polished \"after the SPectral IMager (SPIM) reflectance spectroscopy imagery acquisition\" and only then carbon coated \"for further SEM-EDS and EMPA-WDS analyses\" (p.3). The SEM work is then registered to those images: \"To cover approximately the same area of the SPIM images (9.7 mm large), 10 BSE images, with four consecutive images in the same row, were acquired and mosaicked\" (p.3)"
            }
          ],
          "schema:name": "NWA 7317"
        }
      ],
      "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "CNR IMAA (Institute of Methodologies for Environmental Analysis), Italian National Research Council, Potenza, Italy"
      },
      "schema:description": "10 BSE images acquired at \u00d7138 magnification and mosaicked (4 consecutive per row) to cover ~9.7 mm area matching SPIM imagery",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Embedded in epoxy, polished to \u00bc \u00b5m level, sputtered with 30-nm-thick carbon film",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          },
          {
            "schema:name": "Ion milling",
            "schema:position": 3,
            "schema:description": "no value available: schema:description",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "EDS (Zeiss Supra 40 FE-SEM); SE Imaging (Zeiss Supra 40 FE-SEM); EMPA-WDS (JEOL JXA-8230, separate instrument); VIS-IR spectroscopy (SPIM)"
      }
    }
  ],
  "ada:analyticalMode": [
    "BSE Imaging"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "NWA 7317",
  "ada:samplingUnitName": "Sample name only \u2014 \"the NWA 7317 slab\" (p.3), imaged on \"almost the same portion of the VIS-IR SPIM images\" (p.4); imaged fields and analysis points are not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix wd: <https://www.wikidata.org/entity/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:semTAPP-detail-Pascucci2026 a schema1:Dataset,
        schema1:Product ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "EDS (Zeiss Supra 40 FE-SEM); SE Imaging (Zeiss Supra 40 FE-SEM); EMPA-WDS (JEOL JXA-8230, separate instrument); VIS-IR spectroscopy (SPIM)" ] ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "no value available: schema:description" ;
                            schema1:name "Ion milling" ;
                            schema1:position 3 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Embedded in epoxy, polished to ¼ µm level, sputtered with 30-nm-thick carbon film" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semTAPP/chamberPressure>,
                <https://ada.astromat.org/metadata/parameter/semTAPP/workingDistance> ;
            schema1:description "10 BSE images acquired at ×138 magnification and mosaicked (4 consecutive per row) to cover ~9.7 mm area matching SPIM imagery" ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:instrument [ a schema1:SoftwareApplication ;
                    schema1:additionalType wd:Q7397 ;
                    schema1:name "Oxford INCA Energy" ;
                    ada:toolRole "acquisition" ],
                <https://example.org/semTAPP-detail-Pascucci2026/instrument/SEM> ;
            schema1:location [ a schema1:Place ;
                    schema1:name "CNR IMAA (Institute of Methodologies for Environmental Analysis), Italian National Research Council, Potenza, Italy" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
                    schema1:name "NWA 7317" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            ada:combinedResults [ ] ;
            ada:edsDeadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "BSE Imaging" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimensions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:sampleName "NWA 7317" ;
    ada:samplingUnitName "Sample name only — \"the NWA 7317 slab\" (p.3), imaged on \"almost the same portion of the VIS-IR SPIM images\" (p.4); imaged fields and analysis points are not labelled" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "no value available: ada:voxelSize" .

<https://example.org/semTAPP-detail-Pascucci2026/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semTAPP/acceleratingVoltage> ;
    schema1:additionalType wd:Q3099911,
        "SEM" ;
    schema1:name "no value available: schema:name" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "VIS-IR imaging spectroscopy, acquired before the section was prepared — the fragment was embedded and polished \"after the SPectral IMager (SPIM) reflectance spectroscopy imagery acquisition\" and only then carbon coated \"for further SEM-EDS and EMPA-WDS analyses\" (p.3). The SEM work is then registered to those images: \"To cover approximately the same area of the SPIM images (9.7 mm large), 10 BSE images, with four consecutive images in the same row, were acquired and mosaicked\" (p.3)" .

<https://ada.astromat.org/metadata/parameter/semTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:description "20 kV" ;
    schema1:name "Accelerating Voltage" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/acceleratingVoltage> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 20 .

<https://ada.astromat.org/metadata/parameter/semTAPP/chamberPressure> a schema1:PropertyValue ;
    schema1:name "Chamber Pressure" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/chamberPressure> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value "High vacuum" .

<https://ada.astromat.org/metadata/parameter/semTAPP/workingDistance> a schema1:PropertyValue ;
    schema1:description "8 mm" ;
    schema1:name "Working Distance" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/workingDistance> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 8 .


```


### detail example Pascucci2026-2
detail instance derived from Pascucci et al. 2026 | NWA 7317 CR6 chondrite | EDS Point Analysis (Zeiss Supra 40 FE-SEM, 20 kV).
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
  "@id": "ex:semTAPP-detail-Pascucci2026-2",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:instrument": [
        {
          "schema:additionalType": [
            "SEM",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/semTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/semTAPP/acceleratingVoltage"
                }
              ],
              "schema:name": "Accelerating Voltage",
              "schema:value": 20,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "20 kV"
            },
            {
              "@id": "ada:parameter/semTAPP/beamDiameter",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/semTAPP/beamDiameter"
                }
              ],
              "schema:name": "Beam Diameter",
              "schema:value": 30,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "N — a 30 μm aperture is stated (p.3), not a beam diameter"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:semTAPP-detail-Pascucci2026-2/instrument/SEM"
        },
        {
          "ada:toolRole": "acquisition",
          "schema:name": "Oxford INCA Energy",
          "@type": [
            "schema:SoftwareApplication"
          ],
          "schema:additionalType": [
            {
              "@id": "https://www.wikidata.org/entity/Q7397"
            }
          ]
        },
        {
          "ada:toolRole": "dataReduction",
          "schema:name": "Oxford INCA Energy (semi-quantitative phase determination from atomic proportions)",
          "@type": [
            "schema:SoftwareApplication"
          ],
          "schema:additionalType": [
            {
              "@id": "https://www.wikidata.org/entity/Q7397"
            }
          ]
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/semTAPP/beamDamageMinimization",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semTAPP/beamDamageMinimization"
            }
          ],
          "schema:name": "Beam Damage Minimization",
          "schema:value": "all: SEM-EDS run only after the SPIM reflectance measurements — 'This was done only after the SPIM reflectance acquisitions to try to avoid charging effects and by also reducing thermal damage' (p.3)"
        },
        {
          "@id": "ada:parameter/semTAPP/chamberPressure",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semTAPP/chamberPressure"
            }
          ],
          "schema:name": "Chamber Pressure",
          "schema:value": "High vacuum",
          "schema:unitText": "no value available: unnamed property"
        },
        {
          "@id": "ada:parameter/semTAPP/edsLiveTimePerPointOrPixel",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semTAPP/edsLiveTimePerPointOrPixel"
            }
          ],
          "schema:name": "EDS Live Time per Point or Pixel",
          "schema:value": 30,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "30 s live time per spot analysis"
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
              "schema:value": "VIS-IR imaging spectroscopy, acquired before the section was prepared — the fragment was embedded and polished \"after the SPectral IMager (SPIM) reflectance spectroscopy imagery acquisition\" and only then carbon coated \"for further SEM-EDS and EMPA-WDS analyses\" (p.3). The SEM work is then registered to those images: \"To cover approximately the same area of the SPIM images (9.7 mm large), 10 BSE images, with four consecutive images in the same row, were acquired and mosaicked\" (p.3)"
            }
          ],
          "schema:name": "NWA 7317"
        }
      ],
      "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "CNR IMAA (Institute of Methodologies for Environmental Analysis), Italian National Research Council, Potenza, Italy"
      },
      "schema:description": "Spot analysis: 20 kV, 30 µm aperture, 30 s live time per spot, maximum process time (Oxford INCA Energy)",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Embedded in epoxy, polished to ¼ µm level, sputtered with 30-nm-thick carbon film",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          },
          {
            "schema:name": "Ion milling",
            "schema:position": 3,
            "schema:description": "no value available: schema:description",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "BSE Imaging (Zeiss Supra 40 FE-SEM); SE Imaging (Zeiss Supra 40 FE-SEM); EMPA-WDS (JEOL JXA-8230, separate instrument); VIS-IR spectroscopy (SPIM)"
      }
    }
  ],
  "ada:analyticalMode": [
    "EDS Point Analysis"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "NWA 7317",
  "ada:samplingUnitName": "Sample name only — \"the NWA 7317 slab\" (p.3), imaged on \"almost the same portion of the VIS-IR SPIM images\" (p.4); imaged fields and analysis points are not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-detail-Pascucci2026-2",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:instrument": [
        {
          "schema:additionalType": [
            "SEM",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/semTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/semTAPP/acceleratingVoltage"
                }
              ],
              "schema:name": "Accelerating Voltage",
              "schema:value": 20,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "20 kV"
            },
            {
              "@id": "ada:parameter/semTAPP/beamDiameter",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/semTAPP/beamDiameter"
                }
              ],
              "schema:name": "Beam Diameter",
              "schema:value": 30,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "N \u2014 a 30 \u03bcm aperture is stated (p.3), not a beam diameter"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:semTAPP-detail-Pascucci2026-2/instrument/SEM"
        },
        {
          "ada:toolRole": "acquisition",
          "schema:name": "Oxford INCA Energy",
          "@type": [
            "schema:SoftwareApplication"
          ],
          "schema:additionalType": [
            {
              "@id": "https://www.wikidata.org/entity/Q7397"
            }
          ]
        },
        {
          "ada:toolRole": "dataReduction",
          "schema:name": "Oxford INCA Energy (semi-quantitative phase determination from atomic proportions)",
          "@type": [
            "schema:SoftwareApplication"
          ],
          "schema:additionalType": [
            {
              "@id": "https://www.wikidata.org/entity/Q7397"
            }
          ]
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/semTAPP/beamDamageMinimization",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semTAPP/beamDamageMinimization"
            }
          ],
          "schema:name": "Beam Damage Minimization",
          "schema:value": "all: SEM-EDS run only after the SPIM reflectance measurements \u2014 'This was done only after the SPIM reflectance acquisitions to try to avoid charging effects and by also reducing thermal damage' (p.3)"
        },
        {
          "@id": "ada:parameter/semTAPP/chamberPressure",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semTAPP/chamberPressure"
            }
          ],
          "schema:name": "Chamber Pressure",
          "schema:value": "High vacuum",
          "schema:unitText": "no value available: unnamed property"
        },
        {
          "@id": "ada:parameter/semTAPP/edsLiveTimePerPointOrPixel",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semTAPP/edsLiveTimePerPointOrPixel"
            }
          ],
          "schema:name": "EDS Live Time per Point or Pixel",
          "schema:value": 30,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "30 s live time per spot analysis"
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
              "schema:value": "VIS-IR imaging spectroscopy, acquired before the section was prepared \u2014 the fragment was embedded and polished \"after the SPectral IMager (SPIM) reflectance spectroscopy imagery acquisition\" and only then carbon coated \"for further SEM-EDS and EMPA-WDS analyses\" (p.3). The SEM work is then registered to those images: \"To cover approximately the same area of the SPIM images (9.7 mm large), 10 BSE images, with four consecutive images in the same row, were acquired and mosaicked\" (p.3)"
            }
          ],
          "schema:name": "NWA 7317"
        }
      ],
      "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "CNR IMAA (Institute of Methodologies for Environmental Analysis), Italian National Research Council, Potenza, Italy"
      },
      "schema:description": "Spot analysis: 20 kV, 30 \u00b5m aperture, 30 s live time per spot, maximum process time (Oxford INCA Energy)",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Embedded in epoxy, polished to \u00bc \u00b5m level, sputtered with 30-nm-thick carbon film",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          },
          {
            "schema:name": "Ion milling",
            "schema:position": 3,
            "schema:description": "no value available: schema:description",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "BSE Imaging (Zeiss Supra 40 FE-SEM); SE Imaging (Zeiss Supra 40 FE-SEM); EMPA-WDS (JEOL JXA-8230, separate instrument); VIS-IR spectroscopy (SPIM)"
      }
    }
  ],
  "ada:analyticalMode": [
    "EDS Point Analysis"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "NWA 7317",
  "ada:samplingUnitName": "Sample name only \u2014 \"the NWA 7317 slab\" (p.3), imaged on \"almost the same portion of the VIS-IR SPIM images\" (p.4); imaged fields and analysis points are not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix wd: <https://www.wikidata.org/entity/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:semTAPP-detail-Pascucci2026-2 a schema1:Dataset,
        schema1:Product ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "BSE Imaging (Zeiss Supra 40 FE-SEM); SE Imaging (Zeiss Supra 40 FE-SEM); EMPA-WDS (JEOL JXA-8230, separate instrument); VIS-IR spectroscopy (SPIM)" ] ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Embedded in epoxy, polished to ¼ µm level, sputtered with 30-nm-thick carbon film" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "no value available: schema:description" ;
                            schema1:name "Ion milling" ;
                            schema1:position 3 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semTAPP/beamDamageMinimization>,
                <https://ada.astromat.org/metadata/parameter/semTAPP/chamberPressure>,
                <https://ada.astromat.org/metadata/parameter/semTAPP/edsLiveTimePerPointOrPixel> ;
            schema1:description "Spot analysis: 20 kV, 30 µm aperture, 30 s live time per spot, maximum process time (Oxford INCA Energy)" ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:instrument [ a schema1:SoftwareApplication ;
                    schema1:additionalType wd:Q7397 ;
                    schema1:name "Oxford INCA Energy" ;
                    ada:toolRole "acquisition" ],
                [ a schema1:SoftwareApplication ;
                    schema1:additionalType wd:Q7397 ;
                    schema1:name "Oxford INCA Energy (semi-quantitative phase determination from atomic proportions)" ;
                    ada:toolRole "dataReduction" ],
                <https://example.org/semTAPP-detail-Pascucci2026-2/instrument/SEM> ;
            schema1:location [ a schema1:Place ;
                    schema1:name "CNR IMAA (Institute of Methodologies for Environmental Analysis), Italian National Research Council, Potenza, Italy" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
                    schema1:name "NWA 7317" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            ada:combinedResults [ ] ;
            ada:edsDeadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "EDS Point Analysis" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimensions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:sampleName "NWA 7317" ;
    ada:samplingUnitName "Sample name only — \"the NWA 7317 slab\" (p.3), imaged on \"almost the same portion of the VIS-IR SPIM images\" (p.4); imaged fields and analysis points are not labelled" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "no value available: ada:voxelSize" .

<https://example.org/semTAPP-detail-Pascucci2026-2/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/semTAPP/beamDiameter> ;
    schema1:additionalType wd:Q3099911,
        "SEM" ;
    schema1:name "no value available: schema:name" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "VIS-IR imaging spectroscopy, acquired before the section was prepared — the fragment was embedded and polished \"after the SPectral IMager (SPIM) reflectance spectroscopy imagery acquisition\" and only then carbon coated \"for further SEM-EDS and EMPA-WDS analyses\" (p.3). The SEM work is then registered to those images: \"To cover approximately the same area of the SPIM images (9.7 mm large), 10 BSE images, with four consecutive images in the same row, were acquired and mosaicked\" (p.3)" .

<https://ada.astromat.org/metadata/parameter/semTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:description "20 kV" ;
    schema1:name "Accelerating Voltage" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/acceleratingVoltage> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 20 .

<https://ada.astromat.org/metadata/parameter/semTAPP/beamDamageMinimization> a schema1:PropertyValue ;
    schema1:name "Beam Damage Minimization" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/beamDamageMinimization> ;
    schema1:value "all: SEM-EDS run only after the SPIM reflectance measurements — 'This was done only after the SPIM reflectance acquisitions to try to avoid charging effects and by also reducing thermal damage' (p.3)" .

<https://ada.astromat.org/metadata/parameter/semTAPP/beamDiameter> a schema1:PropertyValue ;
    schema1:description "N — a 30 μm aperture is stated (p.3), not a beam diameter" ;
    schema1:name "Beam Diameter" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/beamDiameter> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 30 .

<https://ada.astromat.org/metadata/parameter/semTAPP/chamberPressure> a schema1:PropertyValue ;
    schema1:name "Chamber Pressure" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/chamberPressure> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value "High vacuum" .

<https://ada.astromat.org/metadata/parameter/semTAPP/edsLiveTimePerPointOrPixel> a schema1:PropertyValue ;
    schema1:description "30 s live time per spot analysis" ;
    schema1:name "EDS Live Time per Point or Pixel" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/edsLiveTimePerPointOrPixel> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 30 .


```


### detail example Pascucci2026-3
detail instance derived from Pascucci et al. 2026 | NWA 7317 CR6 chondrite | EDS Mapping (Zeiss Supra 40 FE-SEM, 20 kV).
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
  "@id": "ex:semTAPP-detail-Pascucci2026-3",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:instrument": [
        {
          "schema:additionalType": [
            "SEM",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/semTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/semTAPP/acceleratingVoltage"
                }
              ],
              "schema:name": "Accelerating Voltage",
              "schema:value": 20,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "20 kV"
            },
            {
              "@id": "ada:parameter/semTAPP/mappingBeamDiameter",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/semTAPP/mappingBeamDiameter"
                }
              ],
              "schema:name": "Mapping Beam Diameter",
              "schema:value": 60,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "N — a 60 μm aperture is stated (p.3), not a beam diameter"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:semTAPP-detail-Pascucci2026-3/instrument/SEM"
        },
        {
          "ada:toolRole": "acquisition",
          "schema:name": "Oxford INCA Energy",
          "@type": [
            "schema:SoftwareApplication"
          ],
          "schema:additionalType": [
            {
              "@id": "https://www.wikidata.org/entity/Q7397"
            }
          ]
        },
        {
          "ada:toolRole": "dataReduction",
          "schema:name": "Oxford INCA Energy (semi-quantitative phase determination from atomic proportions)",
          "@type": [
            "schema:SoftwareApplication"
          ],
          "schema:additionalType": [
            {
              "@id": "https://www.wikidata.org/entity/Q7397"
            }
          ]
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/semTAPP/chamberPressure",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semTAPP/chamberPressure"
            }
          ],
          "schema:name": "Chamber Pressure",
          "schema:value": "High vacuum",
          "schema:unitText": "no value available: unnamed property"
        },
        {
          "@id": "ada:parameter/semTAPP/edsLiveTimePerPointOrPixel",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semTAPP/edsLiveTimePerPointOrPixel"
            }
          ],
          "schema:name": "EDS Live Time per Point or Pixel",
          "schema:value": 5,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "5 ms dwell time per pixel"
        },
        {
          "@id": "ada:parameter/semTAPP/stepSizePixelSize",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semTAPP/stepSizePixelSize"
            }
          ],
          "schema:name": "Step Size / Pixel Size",
          "schema:value": 2.5,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "2.5 µm"
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
              "schema:value": "VIS-IR imaging spectroscopy, acquired before the section was prepared — the fragment was embedded and polished \"after the SPectral IMager (SPIM) reflectance spectroscopy imagery acquisition\" and only then carbon coated \"for further SEM-EDS and EMPA-WDS analyses\" (p.3). The SEM work is then registered to those images: \"To cover approximately the same area of the SPIM images (9.7 mm large), 10 BSE images, with four consecutive images in the same row, were acquired and mosaicked\" (p.3)"
            }
          ],
          "schema:name": "NWA 7317"
        }
      ],
      "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "CNR IMAA (Institute of Methodologies for Environmental Analysis), Italian National Research Council, Potenza, Italy"
      },
      "schema:description": "EDS mapping: 20 kV, 60 µm aperture, 5 ms dwell per pixel, 1024×768 pixels, 2.5 µm pixel size, ~10 h total; element maps co-registered with BSE images",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Embedded in epoxy, polished to ¼ µm level, sputtered with 30-nm-thick carbon film",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          },
          {
            "schema:name": "Ion milling",
            "schema:position": 3,
            "schema:description": "no value available: schema:description",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "ada:mapDimensions": "1024 × 768 pixels",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/semTAPP/mapArea",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/semTAPP/mapArea"
        }
      ],
      "schema:name": "Map Area",
      "schema:value": 10.5,
      "schema:unitText": "no value available: unnamed property",
      "schema:description": "10.5 × 4.0 mm — 'The area acquired by the SEM-EDS instrument is 10.5 × 4.0 mm wide and it is composed of nine mosaicked images (magnification 138×)'"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "BSE Imaging (Zeiss Supra 40 FE-SEM); SE Imaging (Zeiss Supra 40 FE-SEM); EMPA-WDS (JEOL JXA-8230, separate instrument); VIS-IR spectroscopy (SPIM)"
      }
    }
  ],
  "ada:analyticalMode": [
    "EDS Mapping"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "NWA 7317",
  "ada:samplingUnitName": "Sample name only — \"the NWA 7317 slab\" (p.3), imaged on \"almost the same portion of the VIS-IR SPIM images\" (p.4); imaged fields and analysis points are not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-detail-Pascucci2026-3",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:instrument": [
        {
          "schema:additionalType": [
            "SEM",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/semTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/semTAPP/acceleratingVoltage"
                }
              ],
              "schema:name": "Accelerating Voltage",
              "schema:value": 20,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "20 kV"
            },
            {
              "@id": "ada:parameter/semTAPP/mappingBeamDiameter",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/semTAPP/mappingBeamDiameter"
                }
              ],
              "schema:name": "Mapping Beam Diameter",
              "schema:value": 60,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "N \u2014 a 60 \u03bcm aperture is stated (p.3), not a beam diameter"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:semTAPP-detail-Pascucci2026-3/instrument/SEM"
        },
        {
          "ada:toolRole": "acquisition",
          "schema:name": "Oxford INCA Energy",
          "@type": [
            "schema:SoftwareApplication"
          ],
          "schema:additionalType": [
            {
              "@id": "https://www.wikidata.org/entity/Q7397"
            }
          ]
        },
        {
          "ada:toolRole": "dataReduction",
          "schema:name": "Oxford INCA Energy (semi-quantitative phase determination from atomic proportions)",
          "@type": [
            "schema:SoftwareApplication"
          ],
          "schema:additionalType": [
            {
              "@id": "https://www.wikidata.org/entity/Q7397"
            }
          ]
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/semTAPP/chamberPressure",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semTAPP/chamberPressure"
            }
          ],
          "schema:name": "Chamber Pressure",
          "schema:value": "High vacuum",
          "schema:unitText": "no value available: unnamed property"
        },
        {
          "@id": "ada:parameter/semTAPP/edsLiveTimePerPointOrPixel",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semTAPP/edsLiveTimePerPointOrPixel"
            }
          ],
          "schema:name": "EDS Live Time per Point or Pixel",
          "schema:value": 5,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "5 ms dwell time per pixel"
        },
        {
          "@id": "ada:parameter/semTAPP/stepSizePixelSize",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semTAPP/stepSizePixelSize"
            }
          ],
          "schema:name": "Step Size / Pixel Size",
          "schema:value": 2.5,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "2.5 \u00b5m"
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
              "schema:value": "VIS-IR imaging spectroscopy, acquired before the section was prepared \u2014 the fragment was embedded and polished \"after the SPectral IMager (SPIM) reflectance spectroscopy imagery acquisition\" and only then carbon coated \"for further SEM-EDS and EMPA-WDS analyses\" (p.3). The SEM work is then registered to those images: \"To cover approximately the same area of the SPIM images (9.7 mm large), 10 BSE images, with four consecutive images in the same row, were acquired and mosaicked\" (p.3)"
            }
          ],
          "schema:name": "NWA 7317"
        }
      ],
      "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "CNR IMAA (Institute of Methodologies for Environmental Analysis), Italian National Research Council, Potenza, Italy"
      },
      "schema:description": "EDS mapping: 20 kV, 60 \u00b5m aperture, 5 ms dwell per pixel, 1024\u00d7768 pixels, 2.5 \u00b5m pixel size, ~10 h total; element maps co-registered with BSE images",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Embedded in epoxy, polished to \u00bc \u00b5m level, sputtered with 30-nm-thick carbon film",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          },
          {
            "schema:name": "Ion milling",
            "schema:position": 3,
            "schema:description": "no value available: schema:description",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "ada:mapDimensions": "1024 \u00d7 768 pixels",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/semTAPP/mapArea",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/semTAPP/mapArea"
        }
      ],
      "schema:name": "Map Area",
      "schema:value": 10.5,
      "schema:unitText": "no value available: unnamed property",
      "schema:description": "10.5 \u00d7 4.0 mm \u2014 'The area acquired by the SEM-EDS instrument is 10.5 \u00d7 4.0 mm wide and it is composed of nine mosaicked images (magnification 138\u00d7)'"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "BSE Imaging (Zeiss Supra 40 FE-SEM); SE Imaging (Zeiss Supra 40 FE-SEM); EMPA-WDS (JEOL JXA-8230, separate instrument); VIS-IR spectroscopy (SPIM)"
      }
    }
  ],
  "ada:analyticalMode": [
    "EDS Mapping"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "NWA 7317",
  "ada:samplingUnitName": "Sample name only \u2014 \"the NWA 7317 slab\" (p.3), imaged on \"almost the same portion of the VIS-IR SPIM images\" (p.4); imaged fields and analysis points are not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix wd: <https://www.wikidata.org/entity/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:semTAPP-detail-Pascucci2026-3 a schema1:Dataset,
        schema1:Product ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semTAPP/mapArea> ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "BSE Imaging (Zeiss Supra 40 FE-SEM); SE Imaging (Zeiss Supra 40 FE-SEM); EMPA-WDS (JEOL JXA-8230, separate instrument); VIS-IR spectroscopy (SPIM)" ] ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Embedded in epoxy, polished to ¼ µm level, sputtered with 30-nm-thick carbon film" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "no value available: schema:description" ;
                            schema1:name "Ion milling" ;
                            schema1:position 3 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semTAPP/chamberPressure>,
                <https://ada.astromat.org/metadata/parameter/semTAPP/edsLiveTimePerPointOrPixel>,
                <https://ada.astromat.org/metadata/parameter/semTAPP/stepSizePixelSize> ;
            schema1:description "EDS mapping: 20 kV, 60 µm aperture, 5 ms dwell per pixel, 1024×768 pixels, 2.5 µm pixel size, ~10 h total; element maps co-registered with BSE images" ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:instrument [ a schema1:SoftwareApplication ;
                    schema1:additionalType wd:Q7397 ;
                    schema1:name "Oxford INCA Energy (semi-quantitative phase determination from atomic proportions)" ;
                    ada:toolRole "dataReduction" ],
                [ a schema1:SoftwareApplication ;
                    schema1:additionalType wd:Q7397 ;
                    schema1:name "Oxford INCA Energy" ;
                    ada:toolRole "acquisition" ],
                <https://example.org/semTAPP-detail-Pascucci2026-3/instrument/SEM> ;
            schema1:location [ a schema1:Place ;
                    schema1:name "CNR IMAA (Institute of Methodologies for Environmental Analysis), Italian National Research Council, Potenza, Italy" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
                    schema1:name "NWA 7317" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            ada:combinedResults [ ] ;
            ada:edsDeadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "EDS Mapping" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimensions "missing" ;
    ada:mapDimensions "1024 × 768 pixels" ;
    ada:sampleName "NWA 7317" ;
    ada:samplingUnitName "Sample name only — \"the NWA 7317 slab\" (p.3), imaged on \"almost the same portion of the VIS-IR SPIM images\" (p.4); imaged fields and analysis points are not labelled" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "no value available: ada:voxelSize" .

<https://example.org/semTAPP-detail-Pascucci2026-3/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/semTAPP/mappingBeamDiameter> ;
    schema1:additionalType wd:Q3099911,
        "SEM" ;
    schema1:name "no value available: schema:name" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "VIS-IR imaging spectroscopy, acquired before the section was prepared — the fragment was embedded and polished \"after the SPectral IMager (SPIM) reflectance spectroscopy imagery acquisition\" and only then carbon coated \"for further SEM-EDS and EMPA-WDS analyses\" (p.3). The SEM work is then registered to those images: \"To cover approximately the same area of the SPIM images (9.7 mm large), 10 BSE images, with four consecutive images in the same row, were acquired and mosaicked\" (p.3)" .

<https://ada.astromat.org/metadata/parameter/semTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:description "20 kV" ;
    schema1:name "Accelerating Voltage" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/acceleratingVoltage> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 20 .

<https://ada.astromat.org/metadata/parameter/semTAPP/chamberPressure> a schema1:PropertyValue ;
    schema1:name "Chamber Pressure" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/chamberPressure> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value "High vacuum" .

<https://ada.astromat.org/metadata/parameter/semTAPP/edsLiveTimePerPointOrPixel> a schema1:PropertyValue ;
    schema1:description "5 ms dwell time per pixel" ;
    schema1:name "EDS Live Time per Point or Pixel" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/edsLiveTimePerPointOrPixel> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 5 .

<https://ada.astromat.org/metadata/parameter/semTAPP/mapArea> a schema1:PropertyValue ;
    schema1:description "10.5 × 4.0 mm — 'The area acquired by the SEM-EDS instrument is 10.5 × 4.0 mm wide and it is composed of nine mosaicked images (magnification 138×)'" ;
    schema1:name "Map Area" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/mapArea> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1.05e+01 .

<https://ada.astromat.org/metadata/parameter/semTAPP/mappingBeamDiameter> a schema1:PropertyValue ;
    schema1:description "N — a 60 μm aperture is stated (p.3), not a beam diameter" ;
    schema1:name "Mapping Beam Diameter" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/mappingBeamDiameter> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 60 .

<https://ada.astromat.org/metadata/parameter/semTAPP/stepSizePixelSize> a schema1:PropertyValue ;
    schema1:description "2.5 µm" ;
    schema1:name "Step Size / Pixel Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/stepSizePixelSize> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 2.5e+00 .


```


### detail example Pascucci2026-4
detail instance derived from Pascucci et al. 2026 | NWA 7317 CR6 chondrite | SE Imaging (Zeiss Supra 40 FE-SEM).
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
  "@id": "ex:semTAPP-detail-Pascucci2026-4",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "ada:combinedResults": [
        {}
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
              "schema:value": "VIS-IR imaging spectroscopy, acquired before the section was prepared — the fragment was embedded and polished \"after the SPectral IMager (SPIM) reflectance spectroscopy imagery acquisition\" and only then carbon coated \"for further SEM-EDS and EMPA-WDS analyses\" (p.3). The SEM work is then registered to those images: \"To cover approximately the same area of the SPIM images (9.7 mm large), 10 BSE images, with four consecutive images in the same row, were acquired and mosaicked\" (p.3)"
            }
          ],
          "schema:name": "NWA 7317"
        }
      ],
      "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "CNR IMAA (Institute of Methodologies for Environmental Analysis), Italian National Research Council, Potenza, Italy"
      },
      "schema:description": "SE imaging used for topographic examination; instrument capability: up to ×200,000 magnification, 5 nm resolution; SE acquired before EDS to minimize charging effects",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Embedded in epoxy, polished to ¼ µm level, sputtered with 30-nm-thick carbon film",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          },
          {
            "schema:name": "Ion milling",
            "schema:position": 3,
            "schema:description": "no value available: schema:description",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "BSE Imaging (Zeiss Supra 40 FE-SEM); EDS (Zeiss Supra 40 FE-SEM); EMPA-WDS (JEOL JXA-8230, separate instrument); VIS-IR spectroscopy (SPIM)"
      }
    }
  ],
  "ada:analyticalMode": [
    "SE Imaging"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "NWA 7317",
  "ada:samplingUnitName": "Sample name only — \"the NWA 7317 slab\" (p.3), imaged on \"almost the same portion of the VIS-IR SPIM images\" (p.4); imaged fields and analysis points are not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-detail-Pascucci2026-4",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "ada:combinedResults": [
        {}
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
              "schema:value": "VIS-IR imaging spectroscopy, acquired before the section was prepared \u2014 the fragment was embedded and polished \"after the SPectral IMager (SPIM) reflectance spectroscopy imagery acquisition\" and only then carbon coated \"for further SEM-EDS and EMPA-WDS analyses\" (p.3). The SEM work is then registered to those images: \"To cover approximately the same area of the SPIM images (9.7 mm large), 10 BSE images, with four consecutive images in the same row, were acquired and mosaicked\" (p.3)"
            }
          ],
          "schema:name": "NWA 7317"
        }
      ],
      "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "CNR IMAA (Institute of Methodologies for Environmental Analysis), Italian National Research Council, Potenza, Italy"
      },
      "schema:description": "SE imaging used for topographic examination; instrument capability: up to \u00d7200,000 magnification, 5 nm resolution; SE acquired before EDS to minimize charging effects",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Embedded in epoxy, polished to \u00bc \u00b5m level, sputtered with 30-nm-thick carbon film",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          },
          {
            "schema:name": "Ion milling",
            "schema:position": 3,
            "schema:description": "no value available: schema:description",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "BSE Imaging (Zeiss Supra 40 FE-SEM); EDS (Zeiss Supra 40 FE-SEM); EMPA-WDS (JEOL JXA-8230, separate instrument); VIS-IR spectroscopy (SPIM)"
      }
    }
  ],
  "ada:analyticalMode": [
    "SE Imaging"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "NWA 7317",
  "ada:samplingUnitName": "Sample name only \u2014 \"the NWA 7317 slab\" (p.3), imaged on \"almost the same portion of the VIS-IR SPIM images\" (p.4); imaged fields and analysis points are not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:semTAPP-detail-Pascucci2026-4 a schema1:Dataset,
        schema1:Product ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "BSE Imaging (Zeiss Supra 40 FE-SEM); EDS (Zeiss Supra 40 FE-SEM); EMPA-WDS (JEOL JXA-8230, separate instrument); VIS-IR spectroscopy (SPIM)" ] ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "no value available: schema:description" ;
                            schema1:name "Ion milling" ;
                            schema1:position 3 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Embedded in epoxy, polished to ¼ µm level, sputtered with 30-nm-thick carbon film" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ] ] ;
            schema1:description "SE imaging used for topographic examination; instrument capability: up to ×200,000 magnification, 5 nm resolution; SE acquired before EDS to minimize charging effects" ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "CNR IMAA (Institute of Methodologies for Environmental Analysis), Italian National Research Council, Potenza, Italy" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
                    schema1:name "NWA 7317" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            ada:combinedResults [ ] ;
            ada:edsDeadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "SE Imaging" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimensions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:sampleName "NWA 7317" ;
    ada:samplingUnitName "Sample name only — \"the NWA 7317 slab\" (p.3), imaged on \"almost the same portion of the VIS-IR SPIM images\" (p.4); imaged fields and analysis points are not labelled" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "no value available: ada:voxelSize" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "VIS-IR imaging spectroscopy, acquired before the section was prepared — the fragment was embedded and polished \"after the SPectral IMager (SPIM) reflectance spectroscopy imagery acquisition\" and only then carbon coated \"for further SEM-EDS and EMPA-WDS analyses\" (p.3). The SEM work is then registered to those images: \"To cover approximately the same area of the SPIM images (9.7 mm large), 10 BSE images, with four consecutive images in the same row, were acquired and mosaicked\" (p.3)" .


```


### detail example Zhou2017
detail instance derived from Zhou et al. 2017 | Coal (SC + HBC, Junggar Basin) | 3D Tomography (FEI Helios NanoLab 650).
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
  "@id": "ex:semTAPP-detail-Zhou2017",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/semTAPP/imageRegistration3D",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semTAPP/imageRegistration3D"
            }
          ],
          "schema:name": "3D Image Registration",
          "schema:value": "Fiji/ImageJ StackReg and TurboReg plugins used for slice realignment"
        },
        {
          "@id": "ada:parameter/semTAPP/segmentationMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semTAPP/segmentationMethod"
            }
          ],
          "schema:name": "Segmentation Method",
          "schema:value": "Semi-automatic porosity segmentation by grayscale thresholding; pore volume reconstruction using FEI Avizo Fire 8.1.1; connected component analysis for pore network extraction (PNE)"
        },
        {
          "@id": "ada:parameter/semTAPP/workingDistance",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semTAPP/workingDistance"
            }
          ],
          "schema:name": "Working Distance",
          "schema:value": 4,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "4 mm"
        }
      ],
      "schema:instrument": [
        {
          "schema:additionalType": [
            "SEM",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/semTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/semTAPP/acceleratingVoltage"
                }
              ],
              "schema:name": "Accelerating Voltage",
              "schema:value": 2,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "2 kV (SEM imaging)"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:semTAPP-detail-Zhou2017/instrument/SEM"
        },
        {
          "ada:toolRole": "dataReduction",
          "schema:name": "Fiji/ImageJ (StackReg/TurboReg for slice alignment; VolumeJ for volume rendering); Adobe Photoshop CS6 (image enhancement); FEI Avizo Fire 8.1.1 (pore volume reconstruction and segmentation)",
          "@type": [
            "schema:SoftwareApplication"
          ],
          "schema:additionalType": [
            {
              "@id": "https://www.wikidata.org/entity/Q7397"
            }
          ]
        }
      ],
      "ada:combinedResults": [
        {}
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
              "schema:value": "N — the preparation is mechanical and chemical only (\"polished with dry emery paper and then ground by argon ion\", p.3); no imaging or screening precedes the tomography"
            }
          ],
          "schema:name": "SC; HBC"
        }
      ],
      "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "China University of Geosciences, Beijing, China"
      },
      "schema:description": "Stage tilt 52° between electron and ion columns; SEM range 20V–30kV and FIB range 500V–30kV (system specs); destriping filter xStripes.jar applied; deconvolves y-axis by y/sin(52°) for pixel scale correction",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Cuboidal samples (~0.5×1×1 cm) polished with dry emery paper and argon ion polishing; high-pressure freezing and freeze-drying; glued onto sample holder",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          },
          {
            "schema:name": "Ion milling",
            "schema:position": 3,
            "schema:description": "no value available: schema:description",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "ada:voxelSize": "14.8×14.8 nm pixel size (XY); ~800 total slices; sub-volumes: SC=5.609×3.08×5.446 µm; HBC=4.679×3.2×4.24 µm; SEM image resolution 2.5 nm",
  "ada:imageStackDimensions": "14.8×14.8 nm pixel size (XY); ~800 total slices; sub-volumes: SC=5.609×3.08×5.446 µm; HBC=4.679×3.2×4.24 µm; SEM image resolution 2.5 nm",
  "ada:analyticalMode": [
    "3D Tomography"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "SC; HBC",
  "ada:samplingUnitName": "Sample name only — \"subbituminous coal (SC) and high-volatile bituminous coal (HBC)\" (p.1), one FIB-SEM volume each; the numbered images (e.g. \"1st\", \"300th\" of sample SC, p.2) are slices, not units",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-detail-Zhou2017",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/semTAPP/imageRegistration3D",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semTAPP/imageRegistration3D"
            }
          ],
          "schema:name": "3D Image Registration",
          "schema:value": "Fiji/ImageJ StackReg and TurboReg plugins used for slice realignment"
        },
        {
          "@id": "ada:parameter/semTAPP/segmentationMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semTAPP/segmentationMethod"
            }
          ],
          "schema:name": "Segmentation Method",
          "schema:value": "Semi-automatic porosity segmentation by grayscale thresholding; pore volume reconstruction using FEI Avizo Fire 8.1.1; connected component analysis for pore network extraction (PNE)"
        },
        {
          "@id": "ada:parameter/semTAPP/workingDistance",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semTAPP/workingDistance"
            }
          ],
          "schema:name": "Working Distance",
          "schema:value": 4,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "4 mm"
        }
      ],
      "schema:instrument": [
        {
          "schema:additionalType": [
            "SEM",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/semTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/semTAPP/acceleratingVoltage"
                }
              ],
              "schema:name": "Accelerating Voltage",
              "schema:value": 2,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "2 kV (SEM imaging)"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:semTAPP-detail-Zhou2017/instrument/SEM"
        },
        {
          "ada:toolRole": "dataReduction",
          "schema:name": "Fiji/ImageJ (StackReg/TurboReg for slice alignment; VolumeJ for volume rendering); Adobe Photoshop CS6 (image enhancement); FEI Avizo Fire 8.1.1 (pore volume reconstruction and segmentation)",
          "@type": [
            "schema:SoftwareApplication"
          ],
          "schema:additionalType": [
            {
              "@id": "https://www.wikidata.org/entity/Q7397"
            }
          ]
        }
      ],
      "ada:combinedResults": [
        {}
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
              "schema:value": "N \u2014 the preparation is mechanical and chemical only (\"polished with dry emery paper and then ground by argon ion\", p.3); no imaging or screening precedes the tomography"
            }
          ],
          "schema:name": "SC; HBC"
        }
      ],
      "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "China University of Geosciences, Beijing, China"
      },
      "schema:description": "Stage tilt 52\u00b0 between electron and ion columns; SEM range 20V\u201330kV and FIB range 500V\u201330kV (system specs); destriping filter xStripes.jar applied; deconvolves y-axis by y/sin(52\u00b0) for pixel scale correction",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Cuboidal samples (~0.5\u00d71\u00d71 cm) polished with dry emery paper and argon ion polishing; high-pressure freezing and freeze-drying; glued onto sample holder",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          },
          {
            "schema:name": "Ion milling",
            "schema:position": 3,
            "schema:description": "no value available: schema:description",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "ada:voxelSize": "14.8\u00d714.8 nm pixel size (XY); ~800 total slices; sub-volumes: SC=5.609\u00d73.08\u00d75.446 \u00b5m; HBC=4.679\u00d73.2\u00d74.24 \u00b5m; SEM image resolution 2.5 nm",
  "ada:imageStackDimensions": "14.8\u00d714.8 nm pixel size (XY); ~800 total slices; sub-volumes: SC=5.609\u00d73.08\u00d75.446 \u00b5m; HBC=4.679\u00d73.2\u00d74.24 \u00b5m; SEM image resolution 2.5 nm",
  "ada:analyticalMode": [
    "3D Tomography"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "SC; HBC",
  "ada:samplingUnitName": "Sample name only \u2014 \"subbituminous coal (SC) and high-volatile bituminous coal (HBC)\" (p.1), one FIB-SEM volume each; the numbered images (e.g. \"1st\", \"300th\" of sample SC, p.2) are slices, not units",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix wd: <https://www.wikidata.org/entity/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:semTAPP-detail-Zhou2017 a schema1:Dataset,
        schema1:Product ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Cuboidal samples (~0.5×1×1 cm) polished with dry emery paper and argon ion polishing; high-pressure freezing and freeze-drying; glued onto sample holder" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "no value available: schema:description" ;
                            schema1:name "Ion milling" ;
                            schema1:position 3 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semTAPP/imageRegistration3D>,
                <https://ada.astromat.org/metadata/parameter/semTAPP/segmentationMethod>,
                <https://ada.astromat.org/metadata/parameter/semTAPP/workingDistance> ;
            schema1:description "Stage tilt 52° between electron and ion columns; SEM range 20V–30kV and FIB range 500V–30kV (system specs); destriping filter xStripes.jar applied; deconvolves y-axis by y/sin(52°) for pixel scale correction" ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:instrument [ a schema1:SoftwareApplication ;
                    schema1:additionalType wd:Q7397 ;
                    schema1:name "Fiji/ImageJ (StackReg/TurboReg for slice alignment; VolumeJ for volume rendering); Adobe Photoshop CS6 (image enhancement); FEI Avizo Fire 8.1.1 (pore volume reconstruction and segmentation)" ;
                    ada:toolRole "dataReduction" ],
                <https://example.org/semTAPP-detail-Zhou2017/instrument/SEM> ;
            schema1:location [ a schema1:Place ;
                    schema1:name "China University of Geosciences, Beijing, China" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
                    schema1:name "SC; HBC" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            ada:combinedResults [ ] ;
            ada:edsDeadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "3D Tomography" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimensions "14.8×14.8 nm pixel size (XY); ~800 total slices; sub-volumes: SC=5.609×3.08×5.446 µm; HBC=4.679×3.2×4.24 µm; SEM image resolution 2.5 nm" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:sampleName "SC; HBC" ;
    ada:samplingUnitName "Sample name only — \"subbituminous coal (SC) and high-volatile bituminous coal (HBC)\" (p.1), one FIB-SEM volume each; the numbered images (e.g. \"1st\", \"300th\" of sample SC, p.2) are slices, not units" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "14.8×14.8 nm pixel size (XY); ~800 total slices; sub-volumes: SC=5.609×3.08×5.446 µm; HBC=4.679×3.2×4.24 µm; SEM image resolution 2.5 nm" .

<https://example.org/semTAPP-detail-Zhou2017/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semTAPP/acceleratingVoltage> ;
    schema1:additionalType wd:Q3099911,
        "SEM" ;
    schema1:name "no value available: schema:name" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "N — the preparation is mechanical and chemical only (\"polished with dry emery paper and then ground by argon ion\", p.3); no imaging or screening precedes the tomography" .

<https://ada.astromat.org/metadata/parameter/semTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:description "2 kV (SEM imaging)" ;
    schema1:name "Accelerating Voltage" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/acceleratingVoltage> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 2 .

<https://ada.astromat.org/metadata/parameter/semTAPP/imageRegistration3D> a schema1:PropertyValue ;
    schema1:name "3D Image Registration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/imageRegistration3D> ;
    schema1:value "Fiji/ImageJ StackReg and TurboReg plugins used for slice realignment" .

<https://ada.astromat.org/metadata/parameter/semTAPP/segmentationMethod> a schema1:PropertyValue ;
    schema1:name "Segmentation Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/segmentationMethod> ;
    schema1:value "Semi-automatic porosity segmentation by grayscale thresholding; pore volume reconstruction using FEI Avizo Fire 8.1.1; connected component analysis for pore network extraction (PNE)" .

<https://ada.astromat.org/metadata/parameter/semTAPP/workingDistance> a schema1:PropertyValue ;
    schema1:description "4 mm" ;
    schema1:name "Working Distance" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/workingDistance> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 4 .


```


### detail example Zega2025
detail instance derived from Zega et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | BSE Imaging (JEOL 7600F, NASA JSC, 15 kV).
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
  "@id": "ex:semTAPP-detail-Zega2025",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:instrument": [
        {
          "schema:additionalType": [
            "SEM",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/semTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/semTAPP/acceleratingVoltage"
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
          "@id": "ex:semTAPP-detail-Zega2025/instrument/SEM"
        },
        {
          "ada:toolRole": "acquisition",
          "schema:name": "Oxford AZtec (Point & ID programme)",
          "@type": [
            "schema:SoftwareApplication"
          ],
          "schema:additionalType": [
            {
              "@id": "https://www.wikidata.org/entity/Q7397"
            }
          ]
        }
      ],
      "ada:combinedResults": [
        {}
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
              "schema:value": "Optical microscopy before coating — \"After initial documentation by optical microscopy, the sample was sputter coated with ~5 nm of C to assist with charge dissipation during SEM analysis\" (p.9)"
            }
          ],
          "schema:name": "no value available: schema:name"
        }
      ],
      "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "NASA Johnson Space Center (JSC), Houston, TX, USA"
      },
      "schema:description": "SE and BSE imaging; EDS point spectra; Oxford AZtec system; EDS detector: Oxford Instruments Ultim Max SDD 170 mm²",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Attached to Al cylinder SEM mount with double-sided C tape; sputter coated with ~5 nm carbon",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          },
          {
            "schema:name": "Ion milling",
            "schema:position": 3,
            "schema:description": "no value available: schema:description",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NASA award NNH09ZDA007O; contract NNM10AA11C (OSIRIS-REx New Frontiers)"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "EDS (JEOL 7600F, JSC); SE Imaging (JEOL 7600F, JSC); FIB-SEM TEM prep (Quanta3D600, JSC)"
      }
    }
  ],
  "ada:analyticalMode": [
    "BSE Imaging"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA award NNH09ZDA007O; contract NNM10AA11C (OSIRIS-REx New Frontiers)",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "N — the JSC SEM passage names no specimen (\"The particle was attached to an Al cylinder SEM mount\"; \"regions of interest\", p.9); the paper's OREX numbers identify figures, not this laboratory's analyses",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-detail-Zega2025",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:instrument": [
        {
          "schema:additionalType": [
            "SEM",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/semTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/semTAPP/acceleratingVoltage"
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
          "@id": "ex:semTAPP-detail-Zega2025/instrument/SEM"
        },
        {
          "ada:toolRole": "acquisition",
          "schema:name": "Oxford AZtec (Point & ID programme)",
          "@type": [
            "schema:SoftwareApplication"
          ],
          "schema:additionalType": [
            {
              "@id": "https://www.wikidata.org/entity/Q7397"
            }
          ]
        }
      ],
      "ada:combinedResults": [
        {}
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
              "schema:value": "Optical microscopy before coating \u2014 \"After initial documentation by optical microscopy, the sample was sputter coated with ~5 nm of C to assist with charge dissipation during SEM analysis\" (p.9)"
            }
          ],
          "schema:name": "no value available: schema:name"
        }
      ],
      "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "NASA Johnson Space Center (JSC), Houston, TX, USA"
      },
      "schema:description": "SE and BSE imaging; EDS point spectra; Oxford AZtec system; EDS detector: Oxford Instruments Ultim Max SDD 170 mm\u00b2",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Attached to Al cylinder SEM mount with double-sided C tape; sputter coated with ~5 nm carbon",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          },
          {
            "schema:name": "Ion milling",
            "schema:position": 3,
            "schema:description": "no value available: schema:description",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NASA award NNH09ZDA007O; contract NNM10AA11C (OSIRIS-REx New Frontiers)"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "EDS (JEOL 7600F, JSC); SE Imaging (JEOL 7600F, JSC); FIB-SEM TEM prep (Quanta3D600, JSC)"
      }
    }
  ],
  "ada:analyticalMode": [
    "BSE Imaging"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA award NNH09ZDA007O; contract NNM10AA11C (OSIRIS-REx New Frontiers)",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "N \u2014 the JSC SEM passage names no specimen (\"The particle was attached to an Al cylinder SEM mount\"; \"regions of interest\", p.9); the paper's OREX numbers identify figures, not this laboratory's analyses",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix wd: <https://www.wikidata.org/entity/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:semTAPP-detail-Zega2025 a schema1:Dataset,
        schema1:Product ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "NASA award NNH09ZDA007O; contract NNM10AA11C (OSIRIS-REx New Frontiers)" ] ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "EDS (JEOL 7600F, JSC); SE Imaging (JEOL 7600F, JSC); FIB-SEM TEM prep (Quanta3D600, JSC)" ] ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Attached to Al cylinder SEM mount with double-sided C tape; sputter coated with ~5 nm carbon" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "no value available: schema:description" ;
                            schema1:name "Ion milling" ;
                            schema1:position 3 ] ] ;
            schema1:description "SE and BSE imaging; EDS point spectra; Oxford AZtec system; EDS detector: Oxford Instruments Ultim Max SDD 170 mm²" ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:instrument [ a schema1:SoftwareApplication ;
                    schema1:additionalType wd:Q7397 ;
                    schema1:name "Oxford AZtec (Point & ID programme)" ;
                    ada:toolRole "acquisition" ],
                <https://example.org/semTAPP-detail-Zega2025/instrument/SEM> ;
            schema1:location [ a schema1:Place ;
                    schema1:name "NASA Johnson Space Center (JSC), Houston, TX, USA" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
                    schema1:name "no value available: schema:name" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            ada:combinedResults [ ] ;
            ada:edsDeadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "BSE Imaging" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NASA award NNH09ZDA007O; contract NNM10AA11C (OSIRIS-REx New Frontiers)" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimensions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "N — the JSC SEM passage names no specimen (\"The particle was attached to an Al cylinder SEM mount\"; \"regions of interest\", p.9); the paper's OREX numbers identify figures, not this laboratory's analyses" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "no value available: ada:voxelSize" .

<https://example.org/semTAPP-detail-Zega2025/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semTAPP/acceleratingVoltage> ;
    schema1:additionalType wd:Q3099911,
        "SEM" ;
    schema1:name "no value available: schema:name" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "Optical microscopy before coating — \"After initial documentation by optical microscopy, the sample was sputter coated with ~5 nm of C to assist with charge dissipation during SEM analysis\" (p.9)" .

<https://ada.astromat.org/metadata/parameter/semTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:description "15 kV" ;
    schema1:name "Accelerating Voltage" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/acceleratingVoltage> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 15 .


```


### detail example Zega2025-2
detail instance derived from Zega et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | EDS Point Analysis (JEOL 7600F, NASA JSC, 15 kV).
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
  "@id": "ex:semTAPP-detail-Zega2025-2",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:instrument": [
        {
          "schema:additionalType": [
            "SEM",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/semTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/semTAPP/acceleratingVoltage"
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
          "@id": "ex:semTAPP-detail-Zega2025-2/instrument/SEM"
        },
        {
          "ada:toolRole": "acquisition",
          "schema:name": "Oxford AZtec (Point & ID programme)",
          "@type": [
            "schema:SoftwareApplication"
          ],
          "schema:additionalType": [
            {
              "@id": "https://www.wikidata.org/entity/Q7397"
            }
          ]
        },
        {
          "ada:toolRole": "dataReduction",
          "schema:name": "Oxford AZtec",
          "@type": [
            "schema:SoftwareApplication"
          ],
          "schema:additionalType": [
            {
              "@id": "https://www.wikidata.org/entity/Q7397"
            }
          ]
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/semTAPP/edsLiveTimePerPointOrPixel",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semTAPP/edsLiveTimePerPointOrPixel"
            }
          ],
          "schema:name": "EDS Live Time per Point or Pixel",
          "schema:value": 20,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "20 to 200 s (per point)"
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
              "schema:value": "Optical microscopy before coating — \"After initial documentation by optical microscopy, the sample was sputter coated with ~5 nm of C to assist with charge dissipation during SEM analysis\" (p.9)"
            }
          ],
          "schema:name": "no value available: schema:name"
        }
      ],
      "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "NASA Johnson Space Center (JSC), Houston, TX, USA"
      },
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Attached to Al cylinder SEM mount with double-sided C tape; sputter coated with ~5 nm carbon",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          },
          {
            "schema:name": "Ion milling",
            "schema:position": 3,
            "schema:description": "no value available: schema:description",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NASA award NNH09ZDA007O; contract NNM10AA11C (OSIRIS-REx New Frontiers)"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "BSE Imaging (JEOL 7600F, JSC); SE Imaging (JEOL 7600F, JSC); FIB-SEM TEM prep (Quanta3D600, JSC)"
      }
    }
  ],
  "ada:analyticalMode": [
    "EDS Point Analysis"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA award NNH09ZDA007O; contract NNM10AA11C (OSIRIS-REx New Frontiers)",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "N — the JSC SEM passage names no specimen (\"The particle was attached to an Al cylinder SEM mount\"; \"regions of interest\", p.9); the paper's OREX numbers identify figures, not this laboratory's analyses",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-detail-Zega2025-2",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:instrument": [
        {
          "schema:additionalType": [
            "SEM",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/semTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/semTAPP/acceleratingVoltage"
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
          "@id": "ex:semTAPP-detail-Zega2025-2/instrument/SEM"
        },
        {
          "ada:toolRole": "acquisition",
          "schema:name": "Oxford AZtec (Point & ID programme)",
          "@type": [
            "schema:SoftwareApplication"
          ],
          "schema:additionalType": [
            {
              "@id": "https://www.wikidata.org/entity/Q7397"
            }
          ]
        },
        {
          "ada:toolRole": "dataReduction",
          "schema:name": "Oxford AZtec",
          "@type": [
            "schema:SoftwareApplication"
          ],
          "schema:additionalType": [
            {
              "@id": "https://www.wikidata.org/entity/Q7397"
            }
          ]
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/semTAPP/edsLiveTimePerPointOrPixel",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semTAPP/edsLiveTimePerPointOrPixel"
            }
          ],
          "schema:name": "EDS Live Time per Point or Pixel",
          "schema:value": 20,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "20 to 200 s (per point)"
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
              "schema:value": "Optical microscopy before coating \u2014 \"After initial documentation by optical microscopy, the sample was sputter coated with ~5 nm of C to assist with charge dissipation during SEM analysis\" (p.9)"
            }
          ],
          "schema:name": "no value available: schema:name"
        }
      ],
      "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "NASA Johnson Space Center (JSC), Houston, TX, USA"
      },
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Attached to Al cylinder SEM mount with double-sided C tape; sputter coated with ~5 nm carbon",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          },
          {
            "schema:name": "Ion milling",
            "schema:position": 3,
            "schema:description": "no value available: schema:description",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NASA award NNH09ZDA007O; contract NNM10AA11C (OSIRIS-REx New Frontiers)"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "BSE Imaging (JEOL 7600F, JSC); SE Imaging (JEOL 7600F, JSC); FIB-SEM TEM prep (Quanta3D600, JSC)"
      }
    }
  ],
  "ada:analyticalMode": [
    "EDS Point Analysis"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA award NNH09ZDA007O; contract NNM10AA11C (OSIRIS-REx New Frontiers)",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "N \u2014 the JSC SEM passage names no specimen (\"The particle was attached to an Al cylinder SEM mount\"; \"regions of interest\", p.9); the paper's OREX numbers identify figures, not this laboratory's analyses",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix wd: <https://www.wikidata.org/entity/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:semTAPP-detail-Zega2025-2 a schema1:Dataset,
        schema1:Product ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "NASA award NNH09ZDA007O; contract NNM10AA11C (OSIRIS-REx New Frontiers)" ] ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "BSE Imaging (JEOL 7600F, JSC); SE Imaging (JEOL 7600F, JSC); FIB-SEM TEM prep (Quanta3D600, JSC)" ] ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "no value available: schema:description" ;
                            schema1:name "Ion milling" ;
                            schema1:position 3 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Attached to Al cylinder SEM mount with double-sided C tape; sputter coated with ~5 nm carbon" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semTAPP/edsLiveTimePerPointOrPixel> ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:instrument [ a schema1:SoftwareApplication ;
                    schema1:additionalType wd:Q7397 ;
                    schema1:name "Oxford AZtec" ;
                    ada:toolRole "dataReduction" ],
                [ a schema1:SoftwareApplication ;
                    schema1:additionalType wd:Q7397 ;
                    schema1:name "Oxford AZtec (Point & ID programme)" ;
                    ada:toolRole "acquisition" ],
                <https://example.org/semTAPP-detail-Zega2025-2/instrument/SEM> ;
            schema1:location [ a schema1:Place ;
                    schema1:name "NASA Johnson Space Center (JSC), Houston, TX, USA" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
                    schema1:name "no value available: schema:name" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            ada:combinedResults [ ] ;
            ada:edsDeadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "EDS Point Analysis" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NASA award NNH09ZDA007O; contract NNM10AA11C (OSIRIS-REx New Frontiers)" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimensions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "N — the JSC SEM passage names no specimen (\"The particle was attached to an Al cylinder SEM mount\"; \"regions of interest\", p.9); the paper's OREX numbers identify figures, not this laboratory's analyses" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "no value available: ada:voxelSize" .

<https://example.org/semTAPP-detail-Zega2025-2/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semTAPP/acceleratingVoltage> ;
    schema1:additionalType wd:Q3099911,
        "SEM" ;
    schema1:name "no value available: schema:name" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "Optical microscopy before coating — \"After initial documentation by optical microscopy, the sample was sputter coated with ~5 nm of C to assist with charge dissipation during SEM analysis\" (p.9)" .

<https://ada.astromat.org/metadata/parameter/semTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:description "15 kV" ;
    schema1:name "Accelerating Voltage" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/acceleratingVoltage> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 15 .

<https://ada.astromat.org/metadata/parameter/semTAPP/edsLiveTimePerPointOrPixel> a schema1:PropertyValue ;
    schema1:description "20 to 200 s (per point)" ;
    schema1:name "EDS Live Time per Point or Pixel" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/edsLiveTimePerPointOrPixel> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 20 .


```


### detail example Zega2025-3
detail instance derived from Zega et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | SE Imaging (Hitachi S-4800, U Arizona).
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
  "@id": "ex:semTAPP-detail-Zega2025-3",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "ada:combinedResults": [
        {}
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
              "schema:value": "N — the passage describes mounting and coating only (\"Polished sections were coated with a thin layer (0.1 nm) of carbon to mitigate charge build-up\", p.9); no prior imaging or screening is described"
            }
          ],
          "schema:name": "no value available: schema:name"
        }
      ],
      "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "K-ALFAA (Kuiper-Arizona Laboratory for Astromaterials Analysis), University of Arizona"
      },
      "schema:description": "Cold FEG; system range 0.5-30 keV; SE and BSE imaging detectors; also equipped with Oxford Instruments Aztec Live/x-stream/Ultimax 170 SDD EDS; specific operating voltage not stated",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Polished sections; coated with 0.1 nm carbon for charge mitigation",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          },
          {
            "schema:name": "Ion milling",
            "schema:position": 3,
            "schema:description": "no value available: schema:description",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NASA PSEF 80NSSC23K0327; NSF MRI 1531243 and 0619599"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "BSE Imaging (Hitachi S-4800, U Arizona); EDS (Hitachi S-4800, U Arizona); FIB-SEM TEM prep (Helios G3, U Arizona); EMPA (Cameca SX-100 Ultra, out of scope)"
      }
    }
  ],
  "ada:analyticalMode": [
    "SE Imaging"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA PSEF 80NSSC23K0327; NSF MRI 1531243 and 0619599",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "N — the Arizona SEM passage names no specimen (\"Polished sections were coated with a thin layer ... of carbon\", p.9); the paper's OREX numbers identify figures, not this laboratory's analyses",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-detail-Zega2025-3",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "ada:combinedResults": [
        {}
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
              "schema:value": "N \u2014 the passage describes mounting and coating only (\"Polished sections were coated with a thin layer (0.1 nm) of carbon to mitigate charge build-up\", p.9); no prior imaging or screening is described"
            }
          ],
          "schema:name": "no value available: schema:name"
        }
      ],
      "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "K-ALFAA (Kuiper-Arizona Laboratory for Astromaterials Analysis), University of Arizona"
      },
      "schema:description": "Cold FEG; system range 0.5-30 keV; SE and BSE imaging detectors; also equipped with Oxford Instruments Aztec Live/x-stream/Ultimax 170 SDD EDS; specific operating voltage not stated",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Polished sections; coated with 0.1 nm carbon for charge mitigation",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          },
          {
            "schema:name": "Ion milling",
            "schema:position": 3,
            "schema:description": "no value available: schema:description",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NASA PSEF 80NSSC23K0327; NSF MRI 1531243 and 0619599"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "BSE Imaging (Hitachi S-4800, U Arizona); EDS (Hitachi S-4800, U Arizona); FIB-SEM TEM prep (Helios G3, U Arizona); EMPA (Cameca SX-100 Ultra, out of scope)"
      }
    }
  ],
  "ada:analyticalMode": [
    "SE Imaging"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA PSEF 80NSSC23K0327; NSF MRI 1531243 and 0619599",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "N \u2014 the Arizona SEM passage names no specimen (\"Polished sections were coated with a thin layer ... of carbon\", p.9); the paper's OREX numbers identify figures, not this laboratory's analyses",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:semTAPP-detail-Zega2025-3 a schema1:Dataset,
        schema1:Product ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "NASA PSEF 80NSSC23K0327; NSF MRI 1531243 and 0619599" ] ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "BSE Imaging (Hitachi S-4800, U Arizona); EDS (Hitachi S-4800, U Arizona); FIB-SEM TEM prep (Helios G3, U Arizona); EMPA (Cameca SX-100 Ultra, out of scope)" ] ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Polished sections; coated with 0.1 nm carbon for charge mitigation" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "no value available: schema:description" ;
                            schema1:name "Ion milling" ;
                            schema1:position 3 ] ] ;
            schema1:description "Cold FEG; system range 0.5-30 keV; SE and BSE imaging detectors; also equipped with Oxford Instruments Aztec Live/x-stream/Ultimax 170 SDD EDS; specific operating voltage not stated" ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "K-ALFAA (Kuiper-Arizona Laboratory for Astromaterials Analysis), University of Arizona" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
                    schema1:name "no value available: schema:name" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            ada:combinedResults [ ] ;
            ada:edsDeadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "SE Imaging" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NASA PSEF 80NSSC23K0327; NSF MRI 1531243 and 0619599" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimensions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "N — the Arizona SEM passage names no specimen (\"Polished sections were coated with a thin layer ... of carbon\", p.9); the paper's OREX numbers identify figures, not this laboratory's analyses" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "no value available: ada:voxelSize" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "N — the passage describes mounting and coating only (\"Polished sections were coated with a thin layer (0.1 nm) of carbon to mitigate charge build-up\", p.9); no prior imaging or screening is described" .


```


### detail example Zega2025-4
detail instance derived from Zega et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | BSE Imaging (Hitachi S-4800, U Arizona).
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
  "@id": "ex:semTAPP-detail-Zega2025-4",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "ada:combinedResults": [
        {}
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
              "schema:value": "N — the passage describes mounting and coating only (\"Polished sections were coated with a thin layer (0.1 nm) of carbon to mitigate charge build-up\", p.9); no prior imaging or screening is described"
            }
          ],
          "schema:name": "no value available: schema:name"
        }
      ],
      "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "K-ALFAA (Kuiper-Arizona Laboratory for Astromaterials Analysis), University of Arizona"
      },
      "schema:description": "Cold FEG; system range 0.5-30 keV; SE and BSE imaging; EDS mapping; specific operating voltage not stated",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Polished sections; coated with 0.1 nm carbon for charge mitigation",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          },
          {
            "schema:name": "Ion milling",
            "schema:position": 3,
            "schema:description": "no value available: schema:description",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NASA PSEF 80NSSC23K0327; NSF MRI 1531243 and 0619599"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SE Imaging (Hitachi S-4800, U Arizona); EDS (Hitachi S-4800, U Arizona); FIB-SEM TEM prep (Helios G3, U Arizona); EMPA (Cameca SX-100 Ultra, out of scope)"
      }
    }
  ],
  "ada:analyticalMode": [
    "BSE Imaging"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA PSEF 80NSSC23K0327; NSF MRI 1531243 and 0619599",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "N — the Arizona SEM passage names no specimen (\"Polished sections were coated with a thin layer ... of carbon\", p.9); the paper's OREX numbers identify figures, not this laboratory's analyses",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-detail-Zega2025-4",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "ada:combinedResults": [
        {}
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
              "schema:value": "N \u2014 the passage describes mounting and coating only (\"Polished sections were coated with a thin layer (0.1 nm) of carbon to mitigate charge build-up\", p.9); no prior imaging or screening is described"
            }
          ],
          "schema:name": "no value available: schema:name"
        }
      ],
      "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "K-ALFAA (Kuiper-Arizona Laboratory for Astromaterials Analysis), University of Arizona"
      },
      "schema:description": "Cold FEG; system range 0.5-30 keV; SE and BSE imaging; EDS mapping; specific operating voltage not stated",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Polished sections; coated with 0.1 nm carbon for charge mitigation",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          },
          {
            "schema:name": "Ion milling",
            "schema:position": 3,
            "schema:description": "no value available: schema:description",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NASA PSEF 80NSSC23K0327; NSF MRI 1531243 and 0619599"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SE Imaging (Hitachi S-4800, U Arizona); EDS (Hitachi S-4800, U Arizona); FIB-SEM TEM prep (Helios G3, U Arizona); EMPA (Cameca SX-100 Ultra, out of scope)"
      }
    }
  ],
  "ada:analyticalMode": [
    "BSE Imaging"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA PSEF 80NSSC23K0327; NSF MRI 1531243 and 0619599",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "N \u2014 the Arizona SEM passage names no specimen (\"Polished sections were coated with a thin layer ... of carbon\", p.9); the paper's OREX numbers identify figures, not this laboratory's analyses",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:semTAPP-detail-Zega2025-4 a schema1:Dataset,
        schema1:Product ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "NASA PSEF 80NSSC23K0327; NSF MRI 1531243 and 0619599" ] ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "SE Imaging (Hitachi S-4800, U Arizona); EDS (Hitachi S-4800, U Arizona); FIB-SEM TEM prep (Helios G3, U Arizona); EMPA (Cameca SX-100 Ultra, out of scope)" ] ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "no value available: schema:description" ;
                            schema1:name "Ion milling" ;
                            schema1:position 3 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Polished sections; coated with 0.1 nm carbon for charge mitigation" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ] ] ;
            schema1:description "Cold FEG; system range 0.5-30 keV; SE and BSE imaging; EDS mapping; specific operating voltage not stated" ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "K-ALFAA (Kuiper-Arizona Laboratory for Astromaterials Analysis), University of Arizona" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
                    schema1:name "no value available: schema:name" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            ada:combinedResults [ ] ;
            ada:edsDeadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "BSE Imaging" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NASA PSEF 80NSSC23K0327; NSF MRI 1531243 and 0619599" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimensions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "N — the Arizona SEM passage names no specimen (\"Polished sections were coated with a thin layer ... of carbon\", p.9); the paper's OREX numbers identify figures, not this laboratory's analyses" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "no value available: ada:voxelSize" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "N — the passage describes mounting and coating only (\"Polished sections were coated with a thin layer (0.1 nm) of carbon to mitigate charge build-up\", p.9); no prior imaging or screening is described" .


```


### detail example Zega2025-5
detail instance derived from Zega et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | EDS Mapping (Hitachi S-4800, U Arizona).
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
  "@id": "ex:semTAPP-detail-Zega2025-5",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "ada:combinedResults": [
        {}
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
              "schema:value": "N — the passage describes mounting and coating only (\"Polished sections were coated with a thin layer (0.1 nm) of carbon to mitigate charge build-up\", p.9); no prior imaging or screening is described"
            }
          ],
          "schema:name": "no value available: schema:name"
        }
      ],
      "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "K-ALFAA (Kuiper-Arizona Laboratory for Astromaterials Analysis), University of Arizona"
      },
      "schema:instrument": [
        {
          "ada:toolRole": "acquisition",
          "schema:name": "Oxford Instruments Aztec Live/x-stream",
          "@type": [
            "schema:SoftwareApplication"
          ],
          "schema:additionalType": [
            {
              "@id": "https://www.wikidata.org/entity/Q7397"
            }
          ]
        },
        {
          "ada:toolRole": "dataReduction",
          "schema:name": "Oxford Instruments Aztec",
          "@type": [
            "schema:SoftwareApplication"
          ],
          "schema:additionalType": [
            {
              "@id": "https://www.wikidata.org/entity/Q7397"
            }
          ]
        },
        {
          "schema:additionalType": [
            "SEM",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "SEM",
          "@id": "ex:semTAPP-detail-Zega2025-5/instrument/SEM"
        }
      ],
      "schema:description": "Compositional heterogeneity assessed through EDS mapping; no specific kV, current, dwell time stated for S-4800 EDS",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Polished sections; coated with 0.1 nm carbon for charge mitigation",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          },
          {
            "schema:name": "Ion milling",
            "schema:position": 3,
            "schema:description": "no value available: schema:description",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NASA PSEF 80NSSC23K0327; NSF MRI 1531243 and 0619599"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SE/BSE Imaging (Hitachi S-4800, U Arizona); FIB-SEM TEM prep (Helios G3, U Arizona); EMPA (Cameca SX-100 Ultra, out of scope)"
      }
    }
  ],
  "ada:analyticalMode": [
    "EDS Mapping"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA PSEF 80NSSC23K0327; NSF MRI 1531243 and 0619599",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "N — the Arizona SEM passage names no specimen (\"Polished sections were coated with a thin layer ... of carbon\", p.9); the paper's OREX numbers identify figures, not this laboratory's analyses",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-detail-Zega2025-5",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "ada:combinedResults": [
        {}
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
              "schema:value": "N \u2014 the passage describes mounting and coating only (\"Polished sections were coated with a thin layer (0.1 nm) of carbon to mitigate charge build-up\", p.9); no prior imaging or screening is described"
            }
          ],
          "schema:name": "no value available: schema:name"
        }
      ],
      "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "K-ALFAA (Kuiper-Arizona Laboratory for Astromaterials Analysis), University of Arizona"
      },
      "schema:instrument": [
        {
          "ada:toolRole": "acquisition",
          "schema:name": "Oxford Instruments Aztec Live/x-stream",
          "@type": [
            "schema:SoftwareApplication"
          ],
          "schema:additionalType": [
            {
              "@id": "https://www.wikidata.org/entity/Q7397"
            }
          ]
        },
        {
          "ada:toolRole": "dataReduction",
          "schema:name": "Oxford Instruments Aztec",
          "@type": [
            "schema:SoftwareApplication"
          ],
          "schema:additionalType": [
            {
              "@id": "https://www.wikidata.org/entity/Q7397"
            }
          ]
        },
        {
          "schema:additionalType": [
            "SEM",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "SEM",
          "@id": "ex:semTAPP-detail-Zega2025-5/instrument/SEM"
        }
      ],
      "schema:description": "Compositional heterogeneity assessed through EDS mapping; no specific kV, current, dwell time stated for S-4800 EDS",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Polished sections; coated with 0.1 nm carbon for charge mitigation",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          },
          {
            "schema:name": "Ion milling",
            "schema:position": 3,
            "schema:description": "no value available: schema:description",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NASA PSEF 80NSSC23K0327; NSF MRI 1531243 and 0619599"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SE/BSE Imaging (Hitachi S-4800, U Arizona); FIB-SEM TEM prep (Helios G3, U Arizona); EMPA (Cameca SX-100 Ultra, out of scope)"
      }
    }
  ],
  "ada:analyticalMode": [
    "EDS Mapping"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA PSEF 80NSSC23K0327; NSF MRI 1531243 and 0619599",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "N \u2014 the Arizona SEM passage names no specimen (\"Polished sections were coated with a thin layer ... of carbon\", p.9); the paper's OREX numbers identify figures, not this laboratory's analyses",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix wd: <https://www.wikidata.org/entity/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:semTAPP-detail-Zega2025-5 a schema1:Dataset,
        schema1:Product ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "NASA PSEF 80NSSC23K0327; NSF MRI 1531243 and 0619599" ] ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "SE/BSE Imaging (Hitachi S-4800, U Arizona); FIB-SEM TEM prep (Helios G3, U Arizona); EMPA (Cameca SX-100 Ultra, out of scope)" ] ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "no value available: schema:description" ;
                            schema1:name "Ion milling" ;
                            schema1:position 3 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Polished sections; coated with 0.1 nm carbon for charge mitigation" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ] ] ;
            schema1:description "Compositional heterogeneity assessed through EDS mapping; no specific kV, current, dwell time stated for S-4800 EDS" ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:instrument [ a schema1:SoftwareApplication ;
                    schema1:additionalType wd:Q7397 ;
                    schema1:name "Oxford Instruments Aztec Live/x-stream" ;
                    ada:toolRole "acquisition" ],
                [ a schema1:SoftwareApplication ;
                    schema1:additionalType wd:Q7397 ;
                    schema1:name "Oxford Instruments Aztec" ;
                    ada:toolRole "dataReduction" ],
                <https://example.org/semTAPP-detail-Zega2025-5/instrument/SEM> ;
            schema1:location [ a schema1:Place ;
                    schema1:name "K-ALFAA (Kuiper-Arizona Laboratory for Astromaterials Analysis), University of Arizona" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
                    schema1:name "no value available: schema:name" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            ada:combinedResults [ ] ;
            ada:edsDeadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "EDS Mapping" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NASA PSEF 80NSSC23K0327; NSF MRI 1531243 and 0619599" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimensions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "N — the Arizona SEM passage names no specimen (\"Polished sections were coated with a thin layer ... of carbon\", p.9); the paper's OREX numbers identify figures, not this laboratory's analyses" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "no value available: ada:voxelSize" .

<https://example.org/semTAPP-detail-Zega2025-5/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType wd:Q3099911,
        "SEM" ;
    schema1:name "SEM" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "N — the passage describes mounting and coating only (\"Polished sections were coated with a thin layer (0.1 nm) of carbon to mitigate charge build-up\", p.9); no prior imaging or screening is described" .


```


### detail example Zega2025-6
detail instance derived from Zega et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | TEM Sample Preparation (Helios G3, U Arizona).
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
  "@id": "ex:semTAPP-detail-Zega2025-6",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:instrument": [
        {
          "schema:additionalType": [
            "SEM",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/semTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/semTAPP/acceleratingVoltage"
                }
              ],
              "schema:name": "Accelerating Voltage",
              "schema:value": 30,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "30 keV (FIB milling and thinning)"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:semTAPP-detail-Zega2025-6/instrument/SEM"
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:additionalProperty": [
              {
                "@id": "ada:parameter/semTAPP/coarseMillingConditions",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/semTAPP/coarseMillingConditions"
                  }
                ],
                "schema:name": "Coarse Milling Conditions",
                "schema:value": "Standard stair step; 30 keV, currents 2.5 to 0.8 nA"
              },
              {
                "@id": "ada:parameter/semTAPP/protectiveCoatingDeposition",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/semTAPP/protectiveCoatingDeposition"
                  }
                ],
                "schema:name": "Protective Coating Deposition",
                "schema:value": "12-µm wide × 4-µm tall carbon capping layer deposited on matrix areas"
              }
            ],
            "schema:description": "Sections extracted from fine-grained matrix areas in polished sections; BSE and SE images acquired before and after sectioning",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          },
          {
            "schema:name": "Ion milling",
            "schema:position": 3,
            "schema:description": "no value available: schema:description",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
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
              "schema:value": "SEM imaging and EDS mapping of the same particles, reported immediately before the FIB work in the Methods — SE and BSE images on the Hitachi S-4800 and EDS mapping of \"The compositional heterogeneity of the particles\" (p.9); the paper does not state explicitly that the sections were sited from those images"
            }
          ],
          "schema:name": "no value available: schema:name"
        }
      ],
      "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "K-ALFAA (Kuiper-Arizona Laboratory for Astromaterials Analysis), University of Arizona"
      },
      "schema:description": "Sections thinned to electron transparency; BSE/SE images acquired before and after sectioning; methods follow refs. 72-75",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NASA PSEF 80NSSC23K0327; NASA Planetary Major Equipment NNX12AL47G; NSF MRI 0619599"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "TEM analysis (HF5000 STEM, U Arizona); BSE/SE Imaging (Hitachi S-4800, U Arizona)"
      }
    }
  ],
  "ada:analyticalMode": [
    "TEM Sample Preparation"
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "N — a sample-preparation procedure produces sections, not results to combine"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "EBSD Indexing Rate",
      "dqv:value": -9999
    },
    {
      "dqv:isMeasurementOf": "EBSD Mean Angular Deviation",
      "dqv:value": -9999
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA PSEF 80NSSC23K0327; NASA Planetary Major Equipment NNX12AL47G; NSF MRI 0619599",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "N — \"All sections were extracted from varied regions of matrix within the particles\" (p.9), none named; the paper labels FIB sections (e.g. OREX-803095-100, OREX-501005-100, OREX-803031-101; Figs 2–4) without attributing them to a laboratory",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-detail-Zega2025-6",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:instrument": [
        {
          "schema:additionalType": [
            "SEM",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/semTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/semTAPP/acceleratingVoltage"
                }
              ],
              "schema:name": "Accelerating Voltage",
              "schema:value": 30,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "30 keV (FIB milling and thinning)"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:semTAPP-detail-Zega2025-6/instrument/SEM"
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:additionalProperty": [
              {
                "@id": "ada:parameter/semTAPP/coarseMillingConditions",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/semTAPP/coarseMillingConditions"
                  }
                ],
                "schema:name": "Coarse Milling Conditions",
                "schema:value": "Standard stair step; 30 keV, currents 2.5 to 0.8 nA"
              },
              {
                "@id": "ada:parameter/semTAPP/protectiveCoatingDeposition",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/semTAPP/protectiveCoatingDeposition"
                  }
                ],
                "schema:name": "Protective Coating Deposition",
                "schema:value": "12-\u00b5m wide \u00d7 4-\u00b5m tall carbon capping layer deposited on matrix areas"
              }
            ],
            "schema:description": "Sections extracted from fine-grained matrix areas in polished sections; BSE and SE images acquired before and after sectioning",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          },
          {
            "schema:name": "Ion milling",
            "schema:position": 3,
            "schema:description": "no value available: schema:description",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
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
              "schema:value": "SEM imaging and EDS mapping of the same particles, reported immediately before the FIB work in the Methods \u2014 SE and BSE images on the Hitachi S-4800 and EDS mapping of \"The compositional heterogeneity of the particles\" (p.9); the paper does not state explicitly that the sections were sited from those images"
            }
          ],
          "schema:name": "no value available: schema:name"
        }
      ],
      "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "K-ALFAA (Kuiper-Arizona Laboratory for Astromaterials Analysis), University of Arizona"
      },
      "schema:description": "Sections thinned to electron transparency; BSE/SE images acquired before and after sectioning; methods follow refs. 72-75",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NASA PSEF 80NSSC23K0327; NASA Planetary Major Equipment NNX12AL47G; NSF MRI 0619599"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "TEM analysis (HF5000 STEM, U Arizona); BSE/SE Imaging (Hitachi S-4800, U Arizona)"
      }
    }
  ],
  "ada:analyticalMode": [
    "TEM Sample Preparation"
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "N \u2014 a sample-preparation procedure produces sections, not results to combine"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "EBSD Indexing Rate",
      "dqv:value": -9999
    },
    {
      "dqv:isMeasurementOf": "EBSD Mean Angular Deviation",
      "dqv:value": -9999
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA PSEF 80NSSC23K0327; NASA Planetary Major Equipment NNX12AL47G; NSF MRI 0619599",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "N \u2014 \"All sections were extracted from varied regions of matrix within the particles\" (p.9), none named; the paper labels FIB sections (e.g. OREX-803095-100, OREX-501005-100, OREX-803031-101; Figs 2\u20134) without attributing them to a laboratory",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix dqv: <http://www.w3.org/ns/dqv#> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix wd: <https://www.wikidata.org/entity/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:semTAPP-detail-Zega2025-6 a schema1:Dataset,
        schema1:Product ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "NASA PSEF 80NSSC23K0327; NASA Planetary Major Equipment NNX12AL47G; NSF MRI 0619599" ] ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "TEM analysis (HF5000 STEM, U Arizona); BSE/SE Imaging (Hitachi S-4800, U Arizona)" ] ] ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Analytical Precision" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Goodness-of-Fit" ;
            dqv:value "N — a sample-preparation procedure produces sections, not results to combine" ],
        [ dqv:isMeasurementOf "Analytical Accuracy" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "EBSD Mean Angular Deviation" ;
            dqv:value -9999 ],
        [ dqv:isMeasurementOf "EBSD Indexing Rate" ;
            dqv:value -9999 ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "no value available: schema:description" ;
                            schema1:name "Ion milling" ;
                            schema1:position 3 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semTAPP/coarseMillingConditions>,
                                <https://ada.astromat.org/metadata/parameter/semTAPP/protectiveCoatingDeposition> ;
                            schema1:description "Sections extracted from fine-grained matrix areas in polished sections; BSE and SE images acquired before and after sectioning" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ] ] ;
            schema1:description "Sections thinned to electron transparency; BSE/SE images acquired before and after sectioning; methods follow refs. 72-75" ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:instrument <https://example.org/semTAPP-detail-Zega2025-6/instrument/SEM> ;
            schema1:location [ a schema1:Place ;
                    schema1:name "K-ALFAA (Kuiper-Arizona Laboratory for Astromaterials Analysis), University of Arizona" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
                    schema1:name "no value available: schema:name" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            ada:combinedResults [ ] ;
            ada:edsDeadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "TEM Sample Preparation" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NASA PSEF 80NSSC23K0327; NASA Planetary Major Equipment NNX12AL47G; NSF MRI 0619599" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimensions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "N — \"All sections were extracted from varied regions of matrix within the particles\" (p.9), none named; the paper labels FIB sections (e.g. OREX-803095-100, OREX-501005-100, OREX-803031-101; Figs 2–4) without attributing them to a laboratory" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "no value available: ada:voxelSize" .

<https://example.org/semTAPP-detail-Zega2025-6/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semTAPP/acceleratingVoltage> ;
    schema1:additionalType wd:Q3099911,
        "SEM" ;
    schema1:name "no value available: schema:name" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "SEM imaging and EDS mapping of the same particles, reported immediately before the FIB work in the Methods — SE and BSE images on the Hitachi S-4800 and EDS mapping of \"The compositional heterogeneity of the particles\" (p.9); the paper does not state explicitly that the sections were sited from those images" .

<https://ada.astromat.org/metadata/parameter/semTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:description "30 keV (FIB milling and thinning)" ;
    schema1:name "Accelerating Voltage" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/acceleratingVoltage> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 30 .

<https://ada.astromat.org/metadata/parameter/semTAPP/coarseMillingConditions> a schema1:PropertyValue ;
    schema1:name "Coarse Milling Conditions" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/coarseMillingConditions> ;
    schema1:value "Standard stair step; 30 keV, currents 2.5 to 0.8 nA" .

<https://ada.astromat.org/metadata/parameter/semTAPP/protectiveCoatingDeposition> a schema1:PropertyValue ;
    schema1:name "Protective Coating Deposition" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/protectiveCoatingDeposition> ;
    schema1:value "12-µm wide × 4-µm tall carbon capping layer deposited on matrix areas" .


```


### detail example Zega2025-7
detail instance derived from Zega et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | TEM Sample Preparation (Helios G4 UX, UC Berkeley).
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
  "@id": "ex:semTAPP-detail-Zega2025-7",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:instrument": [
        {
          "schema:additionalType": [
            "SEM",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/semTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/semTAPP/acceleratingVoltage"
                }
              ],
              "schema:name": "Accelerating Voltage",
              "schema:value": 16,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "16 to 30 keV (coarse milling); down to 1 keV (polishing)"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:semTAPP-detail-Zega2025-7/instrument/SEM"
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:additionalProperty": [
              {
                "@id": "ada:parameter/semTAPP/coarseMillingConditions",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/semTAPP/coarseMillingConditions"
                  }
                ],
                "schema:name": "Coarse Milling Conditions",
                "schema:value": "Ga+ ion beam at 16–30 keV (coarse milling)"
              },
              {
                "@id": "ada:parameter/semTAPP/finePolishingConditions",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/semTAPP/finePolishingConditions"
                  }
                ],
                "schema:name": "Fine Polishing Conditions",
                "schema:value": "Various voltages down to 1 keV (polishing)"
              }
            ],
            "schema:description": "Particles placed on PELCO carbon conductive tabs on Al SEM round; no protective coating stated",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          },
          {
            "schema:name": "Ion milling",
            "schema:position": 3,
            "schema:description": "no value available: schema:description",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/semTAPP/foilThickness",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/semTAPP/foilThickness"
                }
              ],
              "schema:name": "Foil Thickness",
              "schema:value": 100,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "<100 to 600 nm (variable, depending on targeted experiment)"
            },
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
              "schema:value": "N — the passage states only that \"Bennu particles were placed on PELCO carbon conductive tabs\" (p.9); no prior imaging or screening is described for this laboratory"
            }
          ],
          "schema:name": "no value available: schema:name"
        }
      ],
      "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Molecular Foundry, Lawrence Berkeley National Laboratory (UC Berkeley)"
      },
      "schema:description": "Thicker sections (<100 nm) for TEM; sections up to 600 nm for Fe-L XANES and tomography",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "US DOE contract DE-AC02-05CH11231 (Advanced Light Source / Molecular Foundry)"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Synchrotron XANES (ALS, Berkeley); TEM analysis"
      }
    }
  ],
  "ada:analyticalMode": [
    "TEM Sample Preparation"
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "N — a sample-preparation procedure produces sections, not results to combine"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "EBSD Indexing Rate",
      "dqv:value": -9999
    },
    {
      "dqv:isMeasurementOf": "EBSD Mean Angular Deviation",
      "dqv:value": -9999
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "US DOE contract DE-AC02-05CH11231 (Advanced Light Source / Molecular Foundry)",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "N — \"Bennu particles were placed on PELCO carbon conductive tabs\" (p.9), none named; the paper labels FIB sections (e.g. OREX-803095-100, OREX-501005-100, OREX-803031-101; Figs 2–4) without attributing them to a laboratory",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-detail-Zega2025-7",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:instrument": [
        {
          "schema:additionalType": [
            "SEM",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/semTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/semTAPP/acceleratingVoltage"
                }
              ],
              "schema:name": "Accelerating Voltage",
              "schema:value": 16,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "16 to 30 keV (coarse milling); down to 1 keV (polishing)"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:semTAPP-detail-Zega2025-7/instrument/SEM"
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:additionalProperty": [
              {
                "@id": "ada:parameter/semTAPP/coarseMillingConditions",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/semTAPP/coarseMillingConditions"
                  }
                ],
                "schema:name": "Coarse Milling Conditions",
                "schema:value": "Ga+ ion beam at 16\u201330 keV (coarse milling)"
              },
              {
                "@id": "ada:parameter/semTAPP/finePolishingConditions",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/semTAPP/finePolishingConditions"
                  }
                ],
                "schema:name": "Fine Polishing Conditions",
                "schema:value": "Various voltages down to 1 keV (polishing)"
              }
            ],
            "schema:description": "Particles placed on PELCO carbon conductive tabs on Al SEM round; no protective coating stated",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          },
          {
            "schema:name": "Ion milling",
            "schema:position": 3,
            "schema:description": "no value available: schema:description",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/semTAPP/foilThickness",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/semTAPP/foilThickness"
                }
              ],
              "schema:name": "Foil Thickness",
              "schema:value": 100,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "<100 to 600 nm (variable, depending on targeted experiment)"
            },
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
              "schema:value": "N \u2014 the passage states only that \"Bennu particles were placed on PELCO carbon conductive tabs\" (p.9); no prior imaging or screening is described for this laboratory"
            }
          ],
          "schema:name": "no value available: schema:name"
        }
      ],
      "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Molecular Foundry, Lawrence Berkeley National Laboratory (UC Berkeley)"
      },
      "schema:description": "Thicker sections (<100 nm) for TEM; sections up to 600 nm for Fe-L XANES and tomography",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "US DOE contract DE-AC02-05CH11231 (Advanced Light Source / Molecular Foundry)"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Synchrotron XANES (ALS, Berkeley); TEM analysis"
      }
    }
  ],
  "ada:analyticalMode": [
    "TEM Sample Preparation"
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "N \u2014 a sample-preparation procedure produces sections, not results to combine"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "EBSD Indexing Rate",
      "dqv:value": -9999
    },
    {
      "dqv:isMeasurementOf": "EBSD Mean Angular Deviation",
      "dqv:value": -9999
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "US DOE contract DE-AC02-05CH11231 (Advanced Light Source / Molecular Foundry)",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "N \u2014 \"Bennu particles were placed on PELCO carbon conductive tabs\" (p.9), none named; the paper labels FIB sections (e.g. OREX-803095-100, OREX-501005-100, OREX-803031-101; Figs 2\u20134) without attributing them to a laboratory",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix dqv: <http://www.w3.org/ns/dqv#> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix wd: <https://www.wikidata.org/entity/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:semTAPP-detail-Zega2025-7 a schema1:Dataset,
        schema1:Product ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "US DOE contract DE-AC02-05CH11231 (Advanced Light Source / Molecular Foundry)" ] ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "Synchrotron XANES (ALS, Berkeley); TEM analysis" ] ] ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "EBSD Indexing Rate" ;
            dqv:value -9999 ],
        [ dqv:isMeasurementOf "EBSD Mean Angular Deviation" ;
            dqv:value -9999 ],
        [ dqv:isMeasurementOf "Analytical Accuracy" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Goodness-of-Fit" ;
            dqv:value "N — a sample-preparation procedure produces sections, not results to combine" ],
        [ dqv:isMeasurementOf "Analytical Precision" ;
            dqv:value "no value available: dqv:value" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semTAPP/coarseMillingConditions>,
                                <https://ada.astromat.org/metadata/parameter/semTAPP/finePolishingConditions> ;
                            schema1:description "Particles placed on PELCO carbon conductive tabs on Al SEM round; no protective coating stated" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "no value available: schema:description" ;
                            schema1:name "Ion milling" ;
                            schema1:position 3 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ] ] ;
            schema1:description "Thicker sections (<100 nm) for TEM; sections up to 600 nm for Fe-L XANES and tomography" ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:instrument <https://example.org/semTAPP-detail-Zega2025-7/instrument/SEM> ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Molecular Foundry, Lawrence Berkeley National Laboratory (UC Berkeley)" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening>,
                        <https://ada.astromat.org/metadata/parameter/semTAPP/foilThickness> ;
                    schema1:name "no value available: schema:name" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            ada:combinedResults [ ] ;
            ada:edsDeadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "TEM Sample Preparation" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "US DOE contract DE-AC02-05CH11231 (Advanced Light Source / Molecular Foundry)" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimensions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "N — \"Bennu particles were placed on PELCO carbon conductive tabs\" (p.9), none named; the paper labels FIB sections (e.g. OREX-803095-100, OREX-501005-100, OREX-803031-101; Figs 2–4) without attributing them to a laboratory" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "no value available: ada:voxelSize" .

<https://example.org/semTAPP-detail-Zega2025-7/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semTAPP/acceleratingVoltage> ;
    schema1:additionalType wd:Q3099911,
        "SEM" ;
    schema1:name "no value available: schema:name" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "N — the passage states only that \"Bennu particles were placed on PELCO carbon conductive tabs\" (p.9); no prior imaging or screening is described for this laboratory" .

<https://ada.astromat.org/metadata/parameter/semTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:description "16 to 30 keV (coarse milling); down to 1 keV (polishing)" ;
    schema1:name "Accelerating Voltage" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/acceleratingVoltage> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 16 .

<https://ada.astromat.org/metadata/parameter/semTAPP/coarseMillingConditions> a schema1:PropertyValue ;
    schema1:name "Coarse Milling Conditions" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/coarseMillingConditions> ;
    schema1:value "Ga+ ion beam at 16–30 keV (coarse milling)" .

<https://ada.astromat.org/metadata/parameter/semTAPP/finePolishingConditions> a schema1:PropertyValue ;
    schema1:name "Fine Polishing Conditions" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/finePolishingConditions> ;
    schema1:value "Various voltages down to 1 keV (polishing)" .

<https://ada.astromat.org/metadata/parameter/semTAPP/foilThickness> a schema1:PropertyValue ;
    schema1:description "<100 to 600 nm (variable, depending on targeted experiment)" ;
    schema1:name "Foil Thickness" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/foilThickness> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 100 .


```


### detail example Zega2025-8
detail instance derived from Zega et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | TEM Sample Preparation (Quanta3D600, NASA JSC).
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
  "@id": "ex:semTAPP-detail-Zega2025-8",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:instrument": [
        {
          "schema:additionalType": [
            "SEM",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/semTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/semTAPP/acceleratingVoltage"
                }
              ],
              "schema:name": "Accelerating Voltage",
              "schema:value": 30,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "30 kV (initial milling); 16 kV (intermediate); 5 kV (final thinning)"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:semTAPP-detail-Zega2025-8/instrument/SEM"
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:additionalProperty": [
              {
                "@id": "ada:parameter/semTAPP/coarseMillingConditions",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/semTAPP/coarseMillingConditions"
                  }
                ],
                "schema:name": "Coarse Milling Conditions",
                "schema:value": "Ga+ ion beam at 30 kV (initial milling); 16 kV (intermediate)"
              },
              {
                "@id": "ada:parameter/semTAPP/finePolishingConditions",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/semTAPP/finePolishingConditions"
                  }
                ],
                "schema:name": "Fine Polishing Conditions",
                "schema:value": "Ga+ ion beam at 5 kV (final thinning) until ~100 nm thick"
              },
              {
                "@id": "ada:parameter/semTAPP/protectiveCoatingDeposition",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/semTAPP/protectiveCoatingDeposition"
                  }
                ],
                "schema:name": "Protective Coating Deposition",
                "schema:value": "Electron-beam deposited carbon (~0.5–1 µm); followed by ion beam-deposited carbon (~2–3 µm capping layer)"
              }
            ],
            "schema:description": "Particles dispersed on conductive carbon dots on Al SEM pin mounts",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          },
          {
            "schema:name": "Ion milling",
            "schema:position": 3,
            "schema:description": "no value available: schema:description",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/semTAPP/foilThickness",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/semTAPP/foilThickness"
                }
              ],
              "schema:name": "Foil Thickness",
              "schema:value": 100,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "~100 nm"
            },
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
              "schema:value": "N — the passage states only that \"FIB sections were prepared from particles dispersed on conductive carbon dots on Al SEM pin mounts\" (p.10); no prior imaging or screening is described for this laboratory"
            }
          ],
          "schema:name": "no value available: schema:name"
        }
      ],
      "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "NASA Johnson Space Center (JSC), Houston, TX, USA"
      },
      "schema:description": "Multi-step milling: e-beam C deposition then FIB C capping, 30 kV → 16 kV → 5 kV; Pt weld to Cu half grids",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NASA award NNH09ZDA007O; contract NNM10AA11C (OSIRIS-REx New Frontiers)"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "TEM analysis (NASA JSC); BSE/SE Imaging (JEOL 7600F, JSC)"
      }
    }
  ],
  "ada:analyticalMode": [
    "TEM Sample Preparation"
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "N — a sample-preparation procedure produces sections, not results to combine"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "EBSD Indexing Rate",
      "dqv:value": -9999
    },
    {
      "dqv:isMeasurementOf": "EBSD Mean Angular Deviation",
      "dqv:value": -9999
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA award NNH09ZDA007O; contract NNM10AA11C (OSIRIS-REx New Frontiers)",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "N — \"FIB sections were prepared from particles dispersed on conductive carbon dots on Al SEM pin mounts\" (p.10), none named; the paper labels FIB sections (e.g. OREX-803095-100, OREX-501005-100, OREX-803031-101; Figs 2–4) without attributing them to a laboratory",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-detail-Zega2025-8",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:instrument": [
        {
          "schema:additionalType": [
            "SEM",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/semTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/semTAPP/acceleratingVoltage"
                }
              ],
              "schema:name": "Accelerating Voltage",
              "schema:value": 30,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "30 kV (initial milling); 16 kV (intermediate); 5 kV (final thinning)"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:semTAPP-detail-Zega2025-8/instrument/SEM"
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:additionalProperty": [
              {
                "@id": "ada:parameter/semTAPP/coarseMillingConditions",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/semTAPP/coarseMillingConditions"
                  }
                ],
                "schema:name": "Coarse Milling Conditions",
                "schema:value": "Ga+ ion beam at 30 kV (initial milling); 16 kV (intermediate)"
              },
              {
                "@id": "ada:parameter/semTAPP/finePolishingConditions",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/semTAPP/finePolishingConditions"
                  }
                ],
                "schema:name": "Fine Polishing Conditions",
                "schema:value": "Ga+ ion beam at 5 kV (final thinning) until ~100 nm thick"
              },
              {
                "@id": "ada:parameter/semTAPP/protectiveCoatingDeposition",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/semTAPP/protectiveCoatingDeposition"
                  }
                ],
                "schema:name": "Protective Coating Deposition",
                "schema:value": "Electron-beam deposited carbon (~0.5\u20131 \u00b5m); followed by ion beam-deposited carbon (~2\u20133 \u00b5m capping layer)"
              }
            ],
            "schema:description": "Particles dispersed on conductive carbon dots on Al SEM pin mounts",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          },
          {
            "schema:name": "Ion milling",
            "schema:position": 3,
            "schema:description": "no value available: schema:description",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/semTAPP/foilThickness",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/semTAPP/foilThickness"
                }
              ],
              "schema:name": "Foil Thickness",
              "schema:value": 100,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "~100 nm"
            },
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
              "schema:value": "N \u2014 the passage states only that \"FIB sections were prepared from particles dispersed on conductive carbon dots on Al SEM pin mounts\" (p.10); no prior imaging or screening is described for this laboratory"
            }
          ],
          "schema:name": "no value available: schema:name"
        }
      ],
      "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "NASA Johnson Space Center (JSC), Houston, TX, USA"
      },
      "schema:description": "Multi-step milling: e-beam C deposition then FIB C capping, 30 kV \u2192 16 kV \u2192 5 kV; Pt weld to Cu half grids",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NASA award NNH09ZDA007O; contract NNM10AA11C (OSIRIS-REx New Frontiers)"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "TEM analysis (NASA JSC); BSE/SE Imaging (JEOL 7600F, JSC)"
      }
    }
  ],
  "ada:analyticalMode": [
    "TEM Sample Preparation"
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "N \u2014 a sample-preparation procedure produces sections, not results to combine"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "EBSD Indexing Rate",
      "dqv:value": -9999
    },
    {
      "dqv:isMeasurementOf": "EBSD Mean Angular Deviation",
      "dqv:value": -9999
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA award NNH09ZDA007O; contract NNM10AA11C (OSIRIS-REx New Frontiers)",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "N \u2014 \"FIB sections were prepared from particles dispersed on conductive carbon dots on Al SEM pin mounts\" (p.10), none named; the paper labels FIB sections (e.g. OREX-803095-100, OREX-501005-100, OREX-803031-101; Figs 2\u20134) without attributing them to a laboratory",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix dqv: <http://www.w3.org/ns/dqv#> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix wd: <https://www.wikidata.org/entity/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:semTAPP-detail-Zega2025-8 a schema1:Dataset,
        schema1:Product ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "NASA award NNH09ZDA007O; contract NNM10AA11C (OSIRIS-REx New Frontiers)" ] ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "TEM analysis (NASA JSC); BSE/SE Imaging (JEOL 7600F, JSC)" ] ] ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Analytical Precision" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Analytical Accuracy" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Goodness-of-Fit" ;
            dqv:value "N — a sample-preparation procedure produces sections, not results to combine" ],
        [ dqv:isMeasurementOf "EBSD Mean Angular Deviation" ;
            dqv:value -9999 ],
        [ dqv:isMeasurementOf "EBSD Indexing Rate" ;
            dqv:value -9999 ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "no value available: schema:description" ;
                            schema1:name "Ion milling" ;
                            schema1:position 3 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semTAPP/coarseMillingConditions>,
                                <https://ada.astromat.org/metadata/parameter/semTAPP/finePolishingConditions>,
                                <https://ada.astromat.org/metadata/parameter/semTAPP/protectiveCoatingDeposition> ;
                            schema1:description "Particles dispersed on conductive carbon dots on Al SEM pin mounts" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ] ] ;
            schema1:description "Multi-step milling: e-beam C deposition then FIB C capping, 30 kV → 16 kV → 5 kV; Pt weld to Cu half grids" ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:instrument <https://example.org/semTAPP-detail-Zega2025-8/instrument/SEM> ;
            schema1:location [ a schema1:Place ;
                    schema1:name "NASA Johnson Space Center (JSC), Houston, TX, USA" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening>,
                        <https://ada.astromat.org/metadata/parameter/semTAPP/foilThickness> ;
                    schema1:name "no value available: schema:name" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            ada:combinedResults [ ] ;
            ada:edsDeadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "TEM Sample Preparation" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NASA award NNH09ZDA007O; contract NNM10AA11C (OSIRIS-REx New Frontiers)" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimensions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "N — \"FIB sections were prepared from particles dispersed on conductive carbon dots on Al SEM pin mounts\" (p.10), none named; the paper labels FIB sections (e.g. OREX-803095-100, OREX-501005-100, OREX-803031-101; Figs 2–4) without attributing them to a laboratory" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "no value available: ada:voxelSize" .

<https://example.org/semTAPP-detail-Zega2025-8/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semTAPP/acceleratingVoltage> ;
    schema1:additionalType wd:Q3099911,
        "SEM" ;
    schema1:name "no value available: schema:name" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "N — the passage states only that \"FIB sections were prepared from particles dispersed on conductive carbon dots on Al SEM pin mounts\" (p.10); no prior imaging or screening is described for this laboratory" .

<https://ada.astromat.org/metadata/parameter/semTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:description "30 kV (initial milling); 16 kV (intermediate); 5 kV (final thinning)" ;
    schema1:name "Accelerating Voltage" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/acceleratingVoltage> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 30 .

<https://ada.astromat.org/metadata/parameter/semTAPP/coarseMillingConditions> a schema1:PropertyValue ;
    schema1:name "Coarse Milling Conditions" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/coarseMillingConditions> ;
    schema1:value "Ga+ ion beam at 30 kV (initial milling); 16 kV (intermediate)" .

<https://ada.astromat.org/metadata/parameter/semTAPP/finePolishingConditions> a schema1:PropertyValue ;
    schema1:name "Fine Polishing Conditions" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/finePolishingConditions> ;
    schema1:value "Ga+ ion beam at 5 kV (final thinning) until ~100 nm thick" .

<https://ada.astromat.org/metadata/parameter/semTAPP/foilThickness> a schema1:PropertyValue ;
    schema1:description "~100 nm" ;
    schema1:name "Foil Thickness" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/foilThickness> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 100 .

<https://ada.astromat.org/metadata/parameter/semTAPP/protectiveCoatingDeposition> a schema1:PropertyValue ;
    schema1:name "Protective Coating Deposition" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/protectiveCoatingDeposition> ;
    schema1:value "Electron-beam deposited carbon (~0.5–1 µm); followed by ion beam-deposited carbon (~2–3 µm capping layer)" .


```


### detail example Zega2025-9
detail instance derived from Zega et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | CL Mapping (JEOL JSM-7000F, Universite Cote d'Azur, 5 keV).
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
  "@id": "ex:semTAPP-detail-Zega2025-9",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:instrument": [
        {
          "schema:additionalType": [
            "SEM",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/semTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/semTAPP/acceleratingVoltage"
                }
              ],
              "schema:name": "Accelerating Voltage",
              "schema:value": 5,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "5 keV"
            },
            {
              "@id": "ada:parameter/semTAPP/mappingBeamCurrent",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/semTAPP/mappingBeamCurrent"
                }
              ],
              "schema:name": "Mapping Beam Current",
              "schema:value": 1,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "1 to 4 nA"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:semTAPP-detail-Zega2025-9/instrument/SEM"
        }
      ],
      "ada:combinedResults": [
        {}
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
              "schema:value": "N — the cathodoluminescence passage describes the instrument and beam conditions only (p.9)"
            }
          ],
          "schema:name": "no value available: schema:name"
        }
      ],
      "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Université Côte d'Azur / Observatoire de la Côte d'Azur, Valbonne, France"
      },
      "schema:description": "CL emitting volume at 5 keV: up to 230 nm depth, 200 nm sideways (assuming 100-nm graphite coating); recording below focal plane for magnifications <×500 to minimize hotspot effect",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Polished thin sections; ~100 nm graphite coating (as stated in CL emitting volume calculation)",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          },
          {
            "schema:name": "Ion milling",
            "schema:position": 3,
            "schema:description": "no value available: schema:description",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "BSE/EDS (JEOL 7600F, JSC); SE/BSE/EDS (Hitachi S-4800, U Arizona)"
      }
    }
  ],
  "ada:analyticalMode": [
    "CL Mapping"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "N — the cathodoluminescence passage names no specimen (p.9)",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-detail-Zega2025-9",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:instrument": [
        {
          "schema:additionalType": [
            "SEM",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/semTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/semTAPP/acceleratingVoltage"
                }
              ],
              "schema:name": "Accelerating Voltage",
              "schema:value": 5,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "5 keV"
            },
            {
              "@id": "ada:parameter/semTAPP/mappingBeamCurrent",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/semTAPP/mappingBeamCurrent"
                }
              ],
              "schema:name": "Mapping Beam Current",
              "schema:value": 1,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "1 to 4 nA"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:semTAPP-detail-Zega2025-9/instrument/SEM"
        }
      ],
      "ada:combinedResults": [
        {}
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
              "schema:value": "N \u2014 the cathodoluminescence passage describes the instrument and beam conditions only (p.9)"
            }
          ],
          "schema:name": "no value available: schema:name"
        }
      ],
      "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Universit\u00e9 C\u00f4te d'Azur / Observatoire de la C\u00f4te d'Azur, Valbonne, France"
      },
      "schema:description": "CL emitting volume at 5 keV: up to 230 nm depth, 200 nm sideways (assuming 100-nm graphite coating); recording below focal plane for magnifications <\u00d7500 to minimize hotspot effect",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Polished thin sections; ~100 nm graphite coating (as stated in CL emitting volume calculation)",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:position": 2,
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          },
          {
            "schema:name": "Ion milling",
            "schema:position": 3,
            "schema:description": "no value available: schema:description",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ]
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "BSE/EDS (JEOL 7600F, JSC); SE/BSE/EDS (Hitachi S-4800, U Arizona)"
      }
    }
  ],
  "ada:analyticalMode": [
    "CL Mapping"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "N \u2014 the cathodoluminescence passage names no specimen (p.9)",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix wd: <https://www.wikidata.org/entity/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:semTAPP-detail-Zega2025-9 a schema1:Dataset,
        schema1:Product ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "BSE/EDS (JEOL 7600F, JSC); SE/BSE/EDS (Hitachi S-4800, U Arizona)" ] ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "no value available: schema:description" ;
                            schema1:name "Ion milling" ;
                            schema1:position 3 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ],
                        [ a schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Polished thin sections; ~100 nm graphite coating (as stated in CL emitting volume calculation)" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ] ] ;
            schema1:description "CL emitting volume at 5 keV: up to 230 nm depth, 200 nm sideways (assuming 100-nm graphite coating); recording below focal plane for magnifications <×500 to minimize hotspot effect" ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:instrument <https://example.org/semTAPP-detail-Zega2025-9/instrument/SEM> ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Université Côte d'Azur / Observatoire de la Côte d'Azur, Valbonne, France" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
                    schema1:name "no value available: schema:name" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            ada:combinedResults [ ] ;
            ada:edsDeadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "CL Mapping" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimensions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "N — the cathodoluminescence passage names no specimen (p.9)" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "no value available: ada:voxelSize" .

<https://example.org/semTAPP-detail-Zega2025-9/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/semTAPP/mappingBeamCurrent> ;
    schema1:additionalType wd:Q3099911,
        "SEM" ;
    schema1:name "no value available: schema:name" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "N — the cathodoluminescence passage describes the instrument and beam conditions only (p.9)" .

<https://ada.astromat.org/metadata/parameter/semTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:description "5 keV" ;
    schema1:name "Accelerating Voltage" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/acceleratingVoltage> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 5 .

<https://ada.astromat.org/metadata/parameter/semTAPP/mappingBeamCurrent> a schema1:PropertyValue ;
    schema1:description "1 to 4 nA" ;
    schema1:name "Mapping Beam Current" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/mappingBeamCurrent> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1 .


```


### detail example Barnes2025
detail instance derived from Barnes et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | EDS Mapping (JEOL 7600F, NASA JSC, 15 kV).
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
  "@id": "ex:semTAPP-detail-Barnes2025",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "ada:combinedResults": [
        {}
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
              "schema:value": "NanoSIMS isotope imaging — the two grains this procedure analyses were found by raster ion imaging of the Au foil mount, each image \"256 × 256 pixels, analysed at 1,800 μs per pixel for 32 frames\", with grains counted presolar if their composition \"differed from the reference ratios by >5σ\" and the anomaly persisted across frames; \"Two O-rich presolar grains were also analysed by SEM-EDS to further constrain the phase\" (p.11)"
            }
          ],
          "schema:name": "OREX-501018-100"
        }
      ],
      "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Astromaterials Research and Exploration Science Division (ARES), NASA Johnson Space Center, Houston, TX, USA"
      },
      "schema:description": "SEM-EDS (referred to as SEM-EDX in Extended Data Fig. 8) used to confirm phase identifications of two O-rich presolar grains identified by NanoSIMS isotope mapping: one grain confirmed as ferromagnesian silicate; one confirmed as Al,Mg-bearing oxide (Barnes et al. 2025, p.2 and Extended Data Fig. 8 caption). No instrument name, accelerating voltage, beam current, or sample preparation specifics stated for the JSC SEM-EDS step in this paper.",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "NanoSIMS isotope mapping (CAMECA NanoSIMS 50L, NASA JSC); presolar grains identified by NanoSIMS then confirmed by SEM-EDS phase characterisation"
      }
    }
  ],
  "ada:analyticalMode": [
    "EDS Mapping"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "OREX-501018-100",
  "ada:samplingUnitName": "Labelled: \"Bennu sample OREX-501018-100\" (Extended Data Fig. 8 caption, p.27), \"aggregate QL material pressed onto a gold (Au) foil mount\" (p.10); the presolar-grain regions are not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-detail-Barnes2025",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "ada:combinedResults": [
        {}
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
              "schema:value": "NanoSIMS isotope imaging \u2014 the two grains this procedure analyses were found by raster ion imaging of the Au foil mount, each image \"256 \u00d7 256 pixels, analysed at 1,800 \u03bcs per pixel for 32 frames\", with grains counted presolar if their composition \"differed from the reference ratios by >5\u03c3\" and the anomaly persisted across frames; \"Two O-rich presolar grains were also analysed by SEM-EDS to further constrain the phase\" (p.11)"
            }
          ],
          "schema:name": "OREX-501018-100"
        }
      ],
      "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Astromaterials Research and Exploration Science Division (ARES), NASA Johnson Space Center, Houston, TX, USA"
      },
      "schema:description": "SEM-EDS (referred to as SEM-EDX in Extended Data Fig. 8) used to confirm phase identifications of two O-rich presolar grains identified by NanoSIMS isotope mapping: one grain confirmed as ferromagnesian silicate; one confirmed as Al,Mg-bearing oxide (Barnes et al. 2025, p.2 and Extended Data Fig. 8 caption). No instrument name, accelerating voltage, beam current, or sample preparation specifics stated for the JSC SEM-EDS step in this paper.",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:edsDeadTime": -9999
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "NanoSIMS isotope mapping (CAMECA NanoSIMS 50L, NASA JSC); presolar grains identified by NanoSIMS then confirmed by SEM-EDS phase characterisation"
      }
    }
  ],
  "ada:analyticalMode": [
    "EDS Mapping"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "OREX-501018-100",
  "ada:samplingUnitName": "Labelled: \"Bennu sample OREX-501018-100\" (Extended Data Fig. 8 caption, p.27), \"aggregate QL material pressed onto a gold (Au) foil mount\" (p.10); the presolar-grain regions are not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimensions": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:voxelSize": "no value available: ada:voxelSize"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:semTAPP-detail-Barnes2025 a schema1:Dataset,
        schema1:Product ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "NanoSIMS isotope mapping (CAMECA NanoSIMS 50L, NASA JSC); presolar grains identified by NanoSIMS then confirmed by SEM-EDS phase characterisation" ] ] ;
    prov:wasGeneratedBy [ schema1:description "SEM-EDS (referred to as SEM-EDX in Extended Data Fig. 8) used to confirm phase identifications of two O-rich presolar grains identified by NanoSIMS isotope mapping: one grain confirmed as ferromagnesian silicate; one confirmed as Al,Mg-bearing oxide (Barnes et al. 2025, p.2 and Extended Data Fig. 8 caption). No instrument name, accelerating voltage, beam current, or sample preparation specifics stated for the JSC SEM-EDS step in this paper." ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Astromaterials Research and Exploration Science Division (ARES), NASA Johnson Space Center, Houston, TX, USA" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
                    schema1:name "OREX-501018-100" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            ada:combinedResults [ ] ;
            ada:edsDeadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "EDS Mapping" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimensions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:sampleName "OREX-501018-100" ;
    ada:samplingUnitName "Labelled: \"Bennu sample OREX-501018-100\" (Extended Data Fig. 8 caption, p.27), \"aggregate QL material pressed onto a gold (Au) foil mount\" (p.10); the presolar-grain regions are not labelled" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "no value available: ada:voxelSize" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "NanoSIMS isotope imaging — the two grains this procedure analyses were found by raster ion imaging of the Au foil mount, each image \"256 × 256 pixels, analysed at 1,800 μs per pixel for 32 frames\", with grains counted presolar if their composition \"differed from the reference ratios by >5σ\" and the anomaly persisted across frames; \"Two O-rich presolar grains were also analysed by SEM-EDS to further constrain the phase\" (p.11)" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: SEM Analysis Detail
description: Dataset-level analysis-instance detail for SEM (superset), reusing CDIF/schema.org
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
          schema:additionalProperty:
            type: array
            items:
              anyOf:
              - title: 3D Image Registration
                description: Method used to align consecutive SEM image slices in
                  the 3D stack to correct for drift, vibration, and curtaining artifacts.
                  Include software used.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/imageRegistration3D
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/imageRegistration3D
                  schema:name:
                    const: 3D Image Registration
                  schema:value:
                    type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              - title: Segmentation Method
                description: Method and software used to separate distinct phases
                  or features in the reconstructed 3D volume, turning the grayscale
                  volume into labelled regions.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/segmentationMethod
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/segmentationMethod
                  schema:name:
                    const: Segmentation Method
                  schema:value:
                    type: string
                  schema:inDefinedTermSet:
                    const:
                      '@id': ada:vocab/segmentation-method
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              - title: Beam Damage Minimization
                description: 'Describes any measures taken to reduce electron beam
                  damage to the sample during analysis. Examples: reduced accelerating
                  voltage, lowered beam current, defocused or rastered beam, cooled
                  stage, short acquisition sequences, or rotating between multiple
                  points.'
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/beamDamageMinimization
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/beamDamageMinimization
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
                    const: ada:parameter/semTAPP/beamRasterDimensions
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/beamRasterDimensions
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
              - title: Chamber Pressure
                description: Chamber pressure and gas type during analysis. Required
                  for variable pressure (VP-SEM) and environmental SEM (ESEM) modes.
                  Report value and unit (Pa or Torr) and gas composition. Use 'None'
                  for standard high-vacuum operation.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/chamberPressure
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/chamberPressure
                  schema:name:
                    const: Chamber Pressure
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
              - title: CL Integration Time
                description: Acquisition time per pixel (hyperspectral map mode) or
                  per spectrum (spectral point mode), in ms or s.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/clIntegrationTime
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/clIntegrationTime
                  schema:name:
                    const: CL Integration Time
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
              - title: CL Wavelength Calibration Reference
                description: Reference light source or standard material used to calibrate
                  the wavelength axis of the CL spectrometer. Required for quantitative
                  spectral CL and hyperspectral mapping.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/clWavelengthCalibrationReference
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/clWavelengthCalibrationReference
                  schema:name:
                    const: CL Wavelength Calibration Reference
                  schema:value:
                    type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              - title: Drift Correction
                description: 'Describes whether and how stage or beam drift was monitored
                  and corrected during the measurement session. Examples: periodic
                  stage realignment to a fiducial marker, automated beam drift correction
                  in acquisition software, or reanalysis of a reference point at regular
                  intervals.'
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/driftCorrection
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/driftCorrection
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
              - title: EBSD Frame Time
                description: Acquisition time per EBSD diffraction pattern frame in
                  milliseconds.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/ebsdFrameTime
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/ebsdFrameTime
                  schema:name:
                    const: EBSD Frame Time
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
              - title: EBSD Phase List
                description: Mineral phases included in the EBSD reference pattern
                  library for this procedure. Phases may be added for specific sample
                  compositions beyond the expected suite for the target material.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/ebsdPhaseList
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/ebsdPhaseList
                  schema:name:
                    const: EBSD Phase List
                  schema:value:
                    type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              - title: EBSD Step Size
                description: "Distance between adjacent EBSD measurement points in
                  the map in nm or \xB5m. Must be smaller than the smallest grain
                  of interest."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/ebsdStepSize
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/ebsdStepSize
                  schema:name:
                    const: EBSD Step Size
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
              - title: EDS Live Time per Point or Pixel
                description: EDS spectral acquisition live time per analysis point
                  or per pixel in seconds.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/edsLiveTimePerPointOrPixel
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/edsLiveTimePerPointOrPixel
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
                    const: ada:parameter/semTAPP/halogenCorrectionOnOxygen
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/halogenCorrectionOnOxygen
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
              - title: Image Pixel Size
                description: "Physical size of each image pixel at the sample surface,
                  in nm or \xB5m. For large-area mosaic imaging, report the pixel
                  size of individual tiles and the number and arrangement of tiles."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/imagePixelSize
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/imagePixelSize
                  schema:name:
                    const: Image Pixel Size
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
              - title: Step Size / Pixel Size
                description: "Centre-to-centre distance between adjacent measurement
                  points (WDS mapping) or pixels (EDS mapping) in \xB5m."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/stepSizePixelSize
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/stepSizePixelSize
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
              - title: Working Distance
                description: Distance between the objective lens pole piece and the
                  specimen surface in millimetres.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/workingDistance
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/workingDistance
                  schema:name:
                    const: Working Distance
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
                title: 3D Image Registration
                description: Method used to align consecutive SEM image slices in
                  the 3D stack to correct for drift, vibration, and curtaining artifacts.
                  Include software used.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/imageRegistration3D
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/imageRegistration3D
                  schema:name:
                    const: 3D Image Registration
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
                title: Segmentation Method
                description: Method and software used to separate distinct phases
                  or features in the reconstructed 3D volume, turning the grayscale
                  volume into labelled regions.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/segmentationMethod
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/segmentationMethod
                  schema:name:
                    const: Segmentation Method
                  schema:value:
                    type: string
                  schema:inDefinedTermSet:
                    const:
                      '@id': ada:vocab/segmentation-method
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              minContains: 0
              maxContains: 1
            - contains:
                title: Beam Damage Minimization
                description: 'Describes any measures taken to reduce electron beam
                  damage to the sample during analysis. Examples: reduced accelerating
                  voltage, lowered beam current, defocused or rastered beam, cooled
                  stage, short acquisition sequences, or rotating between multiple
                  points.'
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/beamDamageMinimization
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/beamDamageMinimization
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
                    const: ada:parameter/semTAPP/beamRasterDimensions
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/beamRasterDimensions
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
                title: Chamber Pressure
                description: Chamber pressure and gas type during analysis. Required
                  for variable pressure (VP-SEM) and environmental SEM (ESEM) modes.
                  Report value and unit (Pa or Torr) and gas composition. Use 'None'
                  for standard high-vacuum operation.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/chamberPressure
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/chamberPressure
                  schema:name:
                    const: Chamber Pressure
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
                title: CL Integration Time
                description: Acquisition time per pixel (hyperspectral map mode) or
                  per spectrum (spectral point mode), in ms or s.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/clIntegrationTime
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/clIntegrationTime
                  schema:name:
                    const: CL Integration Time
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
                title: CL Wavelength Calibration Reference
                description: Reference light source or standard material used to calibrate
                  the wavelength axis of the CL spectrometer. Required for quantitative
                  spectral CL and hyperspectral mapping.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/clWavelengthCalibrationReference
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/clWavelengthCalibrationReference
                  schema:name:
                    const: CL Wavelength Calibration Reference
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
                title: Drift Correction
                description: 'Describes whether and how stage or beam drift was monitored
                  and corrected during the measurement session. Examples: periodic
                  stage realignment to a fiducial marker, automated beam drift correction
                  in acquisition software, or reanalysis of a reference point at regular
                  intervals.'
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/driftCorrection
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/driftCorrection
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
                title: EBSD Frame Time
                description: Acquisition time per EBSD diffraction pattern frame in
                  milliseconds.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/ebsdFrameTime
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/ebsdFrameTime
                  schema:name:
                    const: EBSD Frame Time
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
                title: EBSD Phase List
                description: Mineral phases included in the EBSD reference pattern
                  library for this procedure. Phases may be added for specific sample
                  compositions beyond the expected suite for the target material.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/ebsdPhaseList
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/ebsdPhaseList
                  schema:name:
                    const: EBSD Phase List
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
                title: EBSD Step Size
                description: "Distance between adjacent EBSD measurement points in
                  the map in nm or \xB5m. Must be smaller than the smallest grain
                  of interest."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/ebsdStepSize
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/ebsdStepSize
                  schema:name:
                    const: EBSD Step Size
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
                title: EDS Live Time per Point or Pixel
                description: EDS spectral acquisition live time per analysis point
                  or per pixel in seconds.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/edsLiveTimePerPointOrPixel
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/edsLiveTimePerPointOrPixel
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
                    const: ada:parameter/semTAPP/halogenCorrectionOnOxygen
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/halogenCorrectionOnOxygen
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
                title: Image Pixel Size
                description: "Physical size of each image pixel at the sample surface,
                  in nm or \xB5m. For large-area mosaic imaging, report the pixel
                  size of individual tiles and the number and arrangement of tiles."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/imagePixelSize
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/imagePixelSize
                  schema:name:
                    const: Image Pixel Size
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
                title: Step Size / Pixel Size
                description: "Centre-to-centre distance between adjacent measurement
                  points (WDS mapping) or pixels (EDS mapping) in \xB5m."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/stepSizePixelSize
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/stepSizePixelSize
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
            - contains:
                title: Working Distance
                description: Distance between the objective lens pole piece and the
                  specimen surface in millimetres.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/workingDistance
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/workingDistance
                  schema:name:
                    const: Working Distance
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
          schema:instrument:
            type: array
            items:
              type: object
              allOf:
              - if:
                  $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/KindInstrument
                then:
                  $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/instrument/schema.yaml
              - if:
                  $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/KindSoftware
                then:
                  $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/geochemBaseProfile/schema.yaml#/$defs/UsedComputationalTool
              - if:
                  $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/KindReagent
                then:
                  $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/geochemBaseProfile/schema.yaml#/$defs/UsedReagent
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
                    schema:additionalProperty:
                      type: array
                      items:
                        anyOf:
                        - title: Accelerating Voltage
                          description: Electron beam accelerating voltage in kilovolts.
                          type: object
                          properties:
                            '@id':
                              const: ada:parameter/semTAPP/acceleratingVoltage
                            '@type':
                              const:
                              - schema:PropertyValue
                            schema:propertyID:
                              const:
                              - '@id': ada:parameter/semTAPP/acceleratingVoltage
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
                          description: Nominal electron beam diameter (spot size)
                            at the sample surface for point analysis, in nanometres
                            or micrometres, as set by the condenser aperture and working
                            distance. The beam used for mapping is recorded under
                            Mapping Beam Diameter.
                          type: object
                          properties:
                            '@id':
                              const: ada:parameter/semTAPP/beamDiameter
                            '@type':
                              const:
                              - schema:PropertyValue
                            schema:propertyID:
                              const:
                              - '@id': ada:parameter/semTAPP/beamDiameter
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
                          description: 'Electron beam probe current used while the
                            beam scans an area: an X-ray or CL map, an EBSD map, or
                            an SE or BSE image, including images taken during FIB-SEM
                            work. For sub-nA values use decimal notation (e.g., 0.4
                            nA). Ion-beam currents used for milling belong in the
                            milling condition fields.'
                          type: object
                          properties:
                            '@id':
                              const: ada:parameter/semTAPP/mappingBeamCurrent
                            '@type':
                              const:
                              - schema:PropertyValue
                            schema:propertyID:
                              const:
                              - '@id': ada:parameter/semTAPP/mappingBeamCurrent
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
                          description: Diameter of the electron beam in micrometres
                            during X-ray mapping. 0 indicates a fully focused beam.
                          type: object
                          properties:
                            '@id':
                              const: ada:parameter/semTAPP/mappingBeamDiameter
                            '@type':
                              const:
                              - schema:PropertyValue
                            schema:propertyID:
                              const:
                              - '@id': ada:parameter/semTAPP/mappingBeamDiameter
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
                          description: Electron beam accelerating voltage in kilovolts.
                          type: object
                          properties:
                            '@id':
                              const: ada:parameter/semTAPP/acceleratingVoltage
                            '@type':
                              const:
                              - schema:PropertyValue
                            schema:propertyID:
                              const:
                              - '@id': ada:parameter/semTAPP/acceleratingVoltage
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
                          description: Nominal electron beam diameter (spot size)
                            at the sample surface for point analysis, in nanometres
                            or micrometres, as set by the condenser aperture and working
                            distance. The beam used for mapping is recorded under
                            Mapping Beam Diameter.
                          type: object
                          properties:
                            '@id':
                              const: ada:parameter/semTAPP/beamDiameter
                            '@type':
                              const:
                              - schema:PropertyValue
                            schema:propertyID:
                              const:
                              - '@id': ada:parameter/semTAPP/beamDiameter
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
                          description: 'Electron beam probe current used while the
                            beam scans an area: an X-ray or CL map, an EBSD map, or
                            an SE or BSE image, including images taken during FIB-SEM
                            work. For sub-nA values use decimal notation (e.g., 0.4
                            nA). Ion-beam currents used for milling belong in the
                            milling condition fields.'
                          type: object
                          properties:
                            '@id':
                              const: ada:parameter/semTAPP/mappingBeamCurrent
                            '@type':
                              const:
                              - schema:PropertyValue
                            schema:propertyID:
                              const:
                              - '@id': ada:parameter/semTAPP/mappingBeamCurrent
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
                          description: Diameter of the electron beam in micrometres
                            during X-ray mapping. 0 indicates a fully focused beam.
                          type: object
                          properties:
                            '@id':
                              const: ada:parameter/semTAPP/mappingBeamDiameter
                            '@type':
                              const:
                              - schema:PropertyValue
                            schema:propertyID:
                              const:
                              - '@id': ada:parameter/semTAPP/mappingBeamDiameter
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
                      const: SEM
                    schema:inDefinedTermSet: ada:vocab/instrumentType
                required:
                - schema:additionalType
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
                          const: Sample preparation
                      required:
                      - schema:name
                    then:
                      properties:
                        schema:additionalProperty:
                          type: array
                          items:
                            anyOf:
                            - title: Coarse Milling Conditions
                              description: 'Ion beam voltage and current used for
                                bulk material removal during FIB milling. For TEM
                                specimen preparation: bulk trenching to isolate the
                                lamella and intermediate thinning. For 3D tomography:
                                face preparation and initial slice removal.'
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/semTAPP/coarseMillingConditions
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/semTAPP/coarseMillingConditions
                                schema:name:
                                  const: Coarse Milling Conditions
                                schema:value:
                                  type: string
                              required:
                              - '@id'
                              - '@type'
                              - schema:propertyID
                              - schema:name
                              - schema:value
                            - title: Fine Polishing Conditions
                              description: Ion beam voltage and current for final
                                thinning and surface polishing of the TEM lamella.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/semTAPP/finePolishingConditions
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/semTAPP/finePolishingConditions
                                schema:name:
                                  const: Fine Polishing Conditions
                                schema:value:
                                  type: string
                              required:
                              - '@id'
                              - '@type'
                              - schema:propertyID
                              - schema:name
                              - schema:value
                            - title: Protective Coating Deposition
                              description: 'Type and deposition conditions of the
                                protective coating applied to the sample surface before
                                FIB milling. E-beam deposition should be applied as
                                the initial layer. Typical coatings: platinum (Pt)
                                or carbon (C). State material, deposition method,
                                beam conditions, and approximate thickness.'
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/semTAPP/protectiveCoatingDeposition
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/semTAPP/protectiveCoatingDeposition
                                schema:name:
                                  const: Protective Coating Deposition
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
                              title: Coarse Milling Conditions
                              description: 'Ion beam voltage and current used for
                                bulk material removal during FIB milling. For TEM
                                specimen preparation: bulk trenching to isolate the
                                lamella and intermediate thinning. For 3D tomography:
                                face preparation and initial slice removal.'
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/semTAPP/coarseMillingConditions
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/semTAPP/coarseMillingConditions
                                schema:name:
                                  const: Coarse Milling Conditions
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
                              title: Fine Polishing Conditions
                              description: Ion beam voltage and current for final
                                thinning and surface polishing of the TEM lamella.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/semTAPP/finePolishingConditions
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/semTAPP/finePolishingConditions
                                schema:name:
                                  const: Fine Polishing Conditions
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
                              title: Protective Coating Deposition
                              description: 'Type and deposition conditions of the
                                protective coating applied to the sample surface before
                                FIB milling. E-beam deposition should be applied as
                                the initial layer. Typical coatings: platinum (Pt)
                                or carbon (C). State material, deposition method,
                                beam conditions, and approximate thickness.'
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/semTAPP/protectiveCoatingDeposition
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/semTAPP/protectiveCoatingDeposition
                                schema:name:
                                  const: Protective Coating Deposition
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
                            anyOf:
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Analysis_constantsReferenceValues
                            - title: Crystal Structure Database
                              description: Crystal structure database used for EBSD
                                phase identification and Kikuchi pattern simulation.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/semTAPP/crystalStructureDatabase
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/semTAPP/crystalStructureDatabase
                                schema:name:
                                  const: Crystal Structure Database
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
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Analysis_constantsReferenceValues
                            minContains: 0
                            maxContains: 1
                          - contains:
                              title: Crystal Structure Database
                              description: Crystal structure database used for EBSD
                                phase identification and Kikuchi pattern simulation.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/semTAPP/crystalStructureDatabase
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/semTAPP/crystalStructureDatabase
                                schema:name:
                                  const: Crystal Structure Database
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
                  - if:
                      properties:
                        schema:name:
                          const: Ion milling
                      required:
                      - schema:name
                    then:
                      properties:
                        schema:description:
                          description: Ion beam voltage and current used to mill each
                            slice during FIB-SEM serial sectioning.
                          anyOf:
                          - type: string
                          - type: array
                            items:
                              type: string
                      required:
                      - schema:description
                allOf:
                - contains:
                    properties:
                      schema:name:
                        const: Sample preparation
                    required:
                    - schema:name
                - contains:
                    properties:
                      schema:name:
                        const: Data processing
                    required:
                    - schema:name
                - contains:
                    properties:
                      schema:name:
                        const: Ion milling
                    required:
                    - schema:name
          ada:edsDeadTime:
            description: "Percent dead time reported by the EDS detector during the
              session \u2014 the fraction of total acquisition time the detector spent
              processing rather than counting. This field documents the resulting
              percentage as a session QC metric. Unlike WDS dead time (see WDS Dead
              Time Correction), no user-selectable correction algorithm is required."
            anyOf:
            - type: number
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
                        anyOf:
                        - title: Foil Thickness
                          description: Target thickness of the electron-transparent
                            TEM lamella after final FIB polishing, in nanometres.
                            Actual thickness may differ from target.
                          type: object
                          properties:
                            '@id':
                              const: ada:parameter/semTAPP/foilThickness
                            '@type':
                              const:
                              - schema:PropertyValue
                            schema:propertyID:
                              const:
                              - '@id': ada:parameter/semTAPP/foilThickness
                            schema:name:
                              const: Foil Thickness
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
                        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Analysis_preAnalysisImagingAndScreening
                        - title: Slice Thickness
                          description: Thickness of each FIB-milled slice during serial
                            sectioning in nanometres.
                          type: object
                          properties:
                            '@id':
                              const: ada:parameter/semTAPP/sliceThickness
                            '@type':
                              const:
                              - schema:PropertyValue
                            schema:propertyID:
                              const:
                              - '@id': ada:parameter/semTAPP/sliceThickness
                            schema:name:
                              const: Slice Thickness
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
                          title: Foil Thickness
                          description: Target thickness of the electron-transparent
                            TEM lamella after final FIB polishing, in nanometres.
                            Actual thickness may differ from target.
                          type: object
                          properties:
                            '@id':
                              const: ada:parameter/semTAPP/foilThickness
                            '@type':
                              const:
                              - schema:PropertyValue
                            schema:propertyID:
                              const:
                              - '@id': ada:parameter/semTAPP/foilThickness
                            schema:name:
                              const: Foil Thickness
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
                          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Analysis_preAnalysisImagingAndScreening
                        minContains: 0
                        maxContains: 1
                      - contains:
                          title: Slice Thickness
                          description: Thickness of each FIB-milled slice during serial
                            sectioning in nanometres.
                          type: object
                          properties:
                            '@id':
                              const: ada:parameter/semTAPP/sliceThickness
                            '@type':
                              const:
                              - schema:PropertyValue
                            schema:propertyID:
                              const:
                              - '@id': ada:parameter/semTAPP/sliceThickness
                            schema:name:
                              const: Slice Thickness
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
                  '@type':
                    contains:
                      const: https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample
                required:
                - '@type'
          ada:proceduralBlankLevel:
            description: "The measured level of the analytical blank in the session,
              and \u2014 where the reported quantity is a ratio \u2014 its composition,
              since a blank subtracted from a ratio biases the result unless its own
              composition is known. Companion to the blank correction method."
            type: string
        required:
        - ada:edsDeadTime
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
        - if:
            properties:
              dqv:isMeasurementOf:
                const: EBSD Indexing Rate
            required:
            - dqv:isMeasurementOf
          then:
            properties:
              dqv:value:
                description: Fraction of EBSD map points successfully indexed, expressed
                  as a percentage of total map points.
                anyOf:
                - type: number
                - type: string
            required:
            - dqv:value
        - if:
            properties:
              dqv:isMeasurementOf:
                const: EBSD Mean Angular Deviation
            required:
            - dqv:isMeasurementOf
          then:
            properties:
              dqv:value:
                description: Mean angular deviation (MAD) of the EBSD pattern indexing
                  solution in degrees. MAD quantifies the misfit between experimental
                  Kikuchi band positions and the best-fit crystal orientation.
                anyOf:
                - type: number
                - type: string
            required:
            - dqv:value
        - if:
            properties:
              dqv:isMeasurementOf:
                const: EBSD Pattern Quality Threshold
            required:
            - dqv:isMeasurementOf
          then:
            properties:
              dqv:value:
                description: Minimum pattern quality or confidence index threshold
                  applied during EBSD data processing to exclude unreliably indexed
                  points from orientation maps. Include metric name and threshold
                  value.
                anyOf:
                - type: string
                - type: array
                  items:
                    type: string
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
      - contains:
          properties:
            dqv:isMeasurementOf:
              const: EBSD Indexing Rate
          required:
          - dqv:isMeasurementOf
      - contains:
          properties:
            dqv:isMeasurementOf:
              const: EBSD Mean Angular Deviation
          required:
          - dqv:isMeasurementOf
      title: Quality Measurements
    ada:mapDimensions:
      description: Number of pixels in the EDS map in the X and Y directions. Based
        on the area of interest and selected pixel size.
      anyOf:
      - type: number
      - type: string
    schema:additionalProperty:
      type: array
      items:
        title: Map Area
        description: "Physical extent of the mapped region, given either as width
          \xD7 height in \xB5m or as a total area in \xB5m\xB2 or mm\xB2, and equal
          to (map width in pixels \xD7 step size) \xD7 (map height in pixels \xD7
          step size). Complements the map's pixel-grid dimensions by recording the
          physical scale of the mapped region."
        type: object
        properties:
          '@id':
            const: ada:parameter/semTAPP/mapArea
          '@type':
            const:
            - schema:PropertyValue
          schema:propertyID:
            const:
            - '@id': ada:parameter/semTAPP/mapArea
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
              const: ada:parameter/semTAPP/mapArea
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/semTAPP/mapArea
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
      title: Additional Properties
    ada:voxelSize:
      description: X, Y, Z dimensions of the reconstructed 3D voxel in nanometres
        (X-Y pixel size from SEM image calibration; Z from slice thickness), and the
        total number of slices in the stack.
      type: string
    ada:imageStackDimensions:
      description: X, Y, Z dimensions of the reconstructed 3D voxel in nanometres
        (X-Y pixel size from SEM image calibration; Z from slice thickness), and the
        total number of slices in the stack.
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
        - title: Target Material of Sampling Unit
          description: The entry in Target Material that the sampling unit belongs
            to, which links the unit to the point-analysis conditions registered for
            that material.
          type: object
          properties:
            '@id':
              const: ada:parameter/semTAPP/targetMaterialOfSamplingUnit
            '@type':
              const:
              - schema:PropertyValue
              - cdi:InstanceVariable
            schema:propertyID:
              const:
              - '@id': ada:parameter/semTAPP/targetMaterialOfSamplingUnit
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
              const: ada:parameter/semTAPP/targetMaterialOfSamplingUnit
            '@type':
              const:
              - schema:PropertyValue
              - cdi:InstanceVariable
            schema:propertyID:
              const:
              - '@id': ada:parameter/semTAPP/targetMaterialOfSamplingUnit
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
  required:
  - ada:mapDimensions
  - ada:voxelSize
  - ada:imageStackDimensions
x-bblocks-metadata:
  itemIdentifier: ogch.techniqueProfile.geochemProfile.SEM.detail
  register: https://amds-ldeo.github.io/geochemBuildingBlocks/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-11-11'

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "ada": "https://ada.astromat.org/metadata/",
    "prov": "http://www.w3.org/ns/prov#",
    "schema": "http://schema.org/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "wd": "https://www.wikidata.org/entity/",
    "nxs": "https://manual.nexusformat.org/classes/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "csvw": "http://www.w3.org/ns/csvw#",
    "bios": "https://bioschemas.org/",
    "spdx": "http://spdx.org/rdf/terms#",
    "dcterms": "http://purl.org/dc/terms/",
    "geosparql": "http://www.opengis.net/ont/geosparql#",
    "dqv": "http://www.w3.org/ns/dqv#",
    "dcat": "http://www.w3.org/ns/dcat#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld)

## Sources

* [SEM_TAPP_v4.xlsx (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/SEM/detail`

