
# SEM Composition Analysis Detail (Schema)

`ogch.techniqueProfile.geochemProfile.SEM-Composition.detail` *v0.1*

Dataset-level analysis-instance detail for SEM composition (EDS/WDS), reusing CDIF/schema.org slots on the schema:Dataset root.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### detail example Genge2025
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
  "@id": "ex:semCompositionTAPP-detail-Genge2025",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
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
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "SEM",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/semCompositionTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/semCompositionTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 10,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "10 kV"
                },
                {
                  "@id": "ada:parameter/semCompositionTAPP/beamDiameter",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/semCompositionTAPP/beamDiameter"
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
              "@id": "ex:semCompositionTAPP-detail-Genge2025/instrument/SEM"
            }
          ]
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/semCompositionTAPP/beamDamageMinimization",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semCompositionTAPP/beamDamageMinimization"
            }
          ],
          "schema:name": "Beam Damage Minimization",
          "schema:value": "N — 10 kV was chosen 'to reduce the excitation volume and increase spatial resolution' (p.2), not to limit beam damage"
        }
      ],
      "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
      "ada:combinedResults": [
        {}
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "GPS Division Analytical Facility, California Institute of Technology"
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:deadTime": -9999
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semCompositionTAPP-detail-Genge2025",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
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
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "SEM",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/semCompositionTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/semCompositionTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 10,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "10 kV"
                },
                {
                  "@id": "ada:parameter/semCompositionTAPP/beamDiameter",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/semCompositionTAPP/beamDiameter"
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
              "@id": "ex:semCompositionTAPP-detail-Genge2025/instrument/SEM"
            }
          ]
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/semCompositionTAPP/beamDamageMinimization",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semCompositionTAPP/beamDamageMinimization"
            }
          ],
          "schema:name": "Beam Damage Minimization",
          "schema:value": "N \u2014 10 kV was chosen 'to reduce the excitation volume and increase spatial resolution' (p.2), not to limit beam damage"
        }
      ],
      "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
      "ada:combinedResults": [
        {}
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "GPS Division Analytical Facility, California Institute of Technology"
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:deadTime": -9999
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
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:semCompositionTAPP-detail-Genge2025 a schema1:Dataset,
        schema1:Product ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "BSE Imaging (same session, same instrument); EBSD (same instrument); EPMA (JEOL JXA-iHP200F, WDS, out of scope)" ] ] ;
    prov:wasGeneratedBy [ schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semCompositionTAPP/beamDamageMinimization> ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "GPS Division Analytical Facility, California Institute of Technology" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
                    schema1:name "no value available: schema:name" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ schema1:instrument <https://example.org/semCompositionTAPP-detail-Genge2025/instrument/SEM> ] ;
            ada:combinedResults [ ] ;
            ada:deadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "EDS Point Analysis" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Sample name only — the single particle \"micrometeorite NG-1\", analysed as \"the NG-1 section\" (p.2); regions are identified by figure panel (\"Alloy-rich regions\", Fig. 2; \"Silicate-dominated areas\", Fig. 3; pp.3–4), not labelled" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" .

<https://example.org/semCompositionTAPP-detail-Genge2025/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semCompositionTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/semCompositionTAPP/beamDiameter> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:name "no value available: schema:name" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "N — the imaging this procedure performs is its own measurement, not a screening step before it; the paper describes no prior characterisation used to locate the units" .

<https://ada.astromat.org/metadata/parameter/semCompositionTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:description "10 kV" ;
    schema1:name "Accelerating Voltage" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semCompositionTAPP/acceleratingVoltage> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 10 .

<https://ada.astromat.org/metadata/parameter/semCompositionTAPP/beamDamageMinimization> a schema1:PropertyValue ;
    schema1:name "Beam Damage Minimization" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semCompositionTAPP/beamDamageMinimization> ;
    schema1:value "N — 10 kV was chosen 'to reduce the excitation volume and increase spatial resolution' (p.2), not to limit beam damage" .

<https://ada.astromat.org/metadata/parameter/semCompositionTAPP/beamDiameter> a schema1:PropertyValue ;
    schema1:description "N — the '0.1 μm beam diameter' (p.2) is the EPMA's, not the SEM's" ;
    schema1:name "Beam Diameter" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semCompositionTAPP/beamDiameter> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1e-01 .


```


### detail example Gucsik2013
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
  "@id": "ex:semCompositionTAPP-detail-Gucsik2013",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
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
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "SEM",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/semCompositionTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/semCompositionTAPP/acceleratingVoltage"
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
              "@id": "ex:semCompositionTAPP-detail-Gucsik2013/instrument/SEM"
            }
          ]
        }
      ],
      "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
      "ada:combinedResults": [
        {}
      ],
      "schema:description": "Described as semiquantitative; BSE images also captured with this instrument at same conditions; EPMA (JEOL JXA-8900R WDS) used for quantitative analyses (out of scope)",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:deadTime": -9999
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semCompositionTAPP-detail-Gucsik2013",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
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
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "SEM",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/semCompositionTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/semCompositionTAPP/acceleratingVoltage"
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
              "@id": "ex:semCompositionTAPP-detail-Gucsik2013/instrument/SEM"
            }
          ]
        }
      ],
      "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
      "ada:combinedResults": [
        {}
      ],
      "schema:description": "Described as semiquantitative; BSE images also captured with this instrument at same conditions; EPMA (JEOL JXA-8900R WDS) used for quantitative analyses (out of scope)",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:deadTime": -9999
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
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:semCompositionTAPP-detail-Gucsik2013 a schema1:Dataset,
        schema1:Product ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "CL (same instrument); BSE Imaging (same instrument, same session); EPMA with WDS (JEOL JXA-8900R, out of scope)" ] ] ;
    prov:wasGeneratedBy [ schema1:description "Described as semiquantitative; BSE images also captured with this instrument at same conditions; EPMA (JEOL JXA-8900R WDS) used for quantitative analyses (out of scope)" ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
                    schema1:name "no value available: schema:name" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ schema1:instrument <https://example.org/semCompositionTAPP-detail-Gucsik2013/instrument/SEM> ] ;
            ada:combinedResults [ ] ;
            ada:deadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "EDS Point Analysis" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Labelled: \"seven representative grains (designated as B-1 through B-7)\" of \"a Kaba thin section\" (p.2), shown as the \"analyzed areas\" in Fig. 1 (p.2)" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" .

<https://example.org/semCompositionTAPP-detail-Gucsik2013/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semCompositionTAPP/acceleratingVoltage> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:name "no value available: schema:name" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "Optical microscope-cathodoluminescence survey — \"Following a systematic optical microscopecathodoluminescence study of a Kaba thin section, seven representative grains (designated as B-1 through B-7) were selected for further analyses\" (p.2); the grain labels tie the later measurements back to that survey (Fig. 1, p.2)" .

<https://ada.astromat.org/metadata/parameter/semCompositionTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:description "15 kV" ;
    schema1:name "Accelerating Voltage" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semCompositionTAPP/acceleratingVoltage> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 15 .


```


### detail example Izawa2010
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
  "@id": "ex:semCompositionTAPP-detail-Izawa2010",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
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
      "ada:combinedResults": [
        {}
      ],
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
      "ada:deadTime": -9999
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
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:detectionLimit": "all: 0.5 wt% — 'with a detection limit of 0.5 wt% for most elements' (p.3), a capability of the Quartz XOne system",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semCompositionTAPP-detail-Izawa2010",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
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
      "ada:combinedResults": [
        {}
      ],
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
      "ada:deadTime": -9999
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
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:detectionLimit": "all: 0.5 wt% \u2014 'with a detection limit of 0.5 wt% for most elements' (p.3), a capability of the Quartz XOne system",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:edsDeadTime": -9999
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:semCompositionTAPP-detail-Izawa2010 a schema1:Dataset,
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
            ada:deadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "EDS Mapping" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit "all: 0.5 wt% — 'with a detection limit of 0.5 wt% for most elements' (p.3), a capability of the Quartz XOne system" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Sample name only — \"the Tagish Lake sections\" (p.3), not individually labelled; the numbered points of Table 1 and Fig. 1 (e.g. \"point #1\", \"spot 34\") are μXRD spots, not SEM analyses" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "Micro X-ray diffraction reconnaissance — the paper's first stage is \"an initial, non-destructive in situ reconnaissance step using micro X-ray diffraction (mXRD) to document meteorite mineralogy and textures and to identify features of interest\", valuable as \"a 'no-touch' first-pass reconnaissance, which may identify areas for further study\"; it then gives \"point-by-point correlation of crystal structure data with other microscopic and microanalytical data\" (p.2)" .


```


### detail example Izawa2010-2
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
  "@id": "ex:semCompositionTAPP-detail-Izawa2010-2",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
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
      "ada:combinedResults": [
        {}
      ],
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
      "ada:deadTime": -9999
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semCompositionTAPP-detail-Izawa2010-2",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
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
      "ada:combinedResults": [
        {}
      ],
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
      "ada:deadTime": -9999
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
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:semCompositionTAPP-detail-Izawa2010-2 a schema1:Dataset,
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
            ada:deadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "EDS Point Analysis" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Sample name only — \"the Tagish Lake sections\" (p.3), not individually labelled; the numbered points of Table 1 and Fig. 1 (e.g. \"point #1\", \"spot 34\") are μXRD spots, not SEM analyses" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "Micro X-ray diffraction reconnaissance — the paper's first stage is \"an initial, non-destructive in situ reconnaissance step using micro X-ray diffraction (mXRD) to document meteorite mineralogy and textures and to identify features of interest\", valuable as \"a 'no-touch' first-pass reconnaissance, which may identify areas for further study\"; it then gives \"point-by-point correlation of crystal structure data with other microscopic and microanalytical data\" (p.2); this procedure is the third stage, run on features the earlier stages located" .


```


### detail example Pascucci2026
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
  "@id": "ex:semCompositionTAPP-detail-Pascucci2026",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
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
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "SEM",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/semCompositionTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/semCompositionTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 20,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "20 kV"
                },
                {
                  "@id": "ada:parameter/semCompositionTAPP/beamDiameter",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/semCompositionTAPP/beamDiameter"
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
              "@id": "ex:semCompositionTAPP-detail-Pascucci2026/instrument/SEM"
            }
          ]
        },
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "acquisition",
              "schema:name": "Oxford INCA Energy",
              "@type": [
                "schema:SoftwareApplication"
              ]
            },
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "Oxford INCA Energy (semi-quantitative phase determination from atomic proportions)",
              "@type": [
                "schema:SoftwareApplication"
              ]
            }
          ]
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/semCompositionTAPP/beamDamageMinimization",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semCompositionTAPP/beamDamageMinimization"
            }
          ],
          "schema:name": "Beam Damage Minimization",
          "schema:value": "all: SEM-EDS run only after the SPIM reflectance measurements — 'This was done only after the SPIM reflectance acquisitions to try to avoid charging effects and by also reducing thermal damage' (p.3)"
        },
        {
          "@id": "ada:parameter/semCompositionTAPP/chamberPressure",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semCompositionTAPP/chamberPressure"
            }
          ],
          "schema:name": "Chamber Pressure",
          "schema:value": "High vacuum",
          "schema:unitText": "no value available: unnamed property"
        },
        {
          "@id": "ada:parameter/semCompositionTAPP/edsLiveTimePerPointOrPixel",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semCompositionTAPP/edsLiveTimePerPointOrPixel"
            }
          ],
          "schema:name": "EDS Live Time per Point or Pixel",
          "schema:value": 30,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "30 s live time per spot analysis"
        }
      ],
      "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
      "ada:combinedResults": [
        {}
      ],
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semCompositionTAPP-detail-Pascucci2026",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
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
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "SEM",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/semCompositionTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/semCompositionTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 20,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "20 kV"
                },
                {
                  "@id": "ada:parameter/semCompositionTAPP/beamDiameter",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/semCompositionTAPP/beamDiameter"
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
              "@id": "ex:semCompositionTAPP-detail-Pascucci2026/instrument/SEM"
            }
          ]
        },
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "acquisition",
              "schema:name": "Oxford INCA Energy",
              "@type": [
                "schema:SoftwareApplication"
              ]
            },
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "Oxford INCA Energy (semi-quantitative phase determination from atomic proportions)",
              "@type": [
                "schema:SoftwareApplication"
              ]
            }
          ]
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/semCompositionTAPP/beamDamageMinimization",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semCompositionTAPP/beamDamageMinimization"
            }
          ],
          "schema:name": "Beam Damage Minimization",
          "schema:value": "all: SEM-EDS run only after the SPIM reflectance measurements \u2014 'This was done only after the SPIM reflectance acquisitions to try to avoid charging effects and by also reducing thermal damage' (p.3)"
        },
        {
          "@id": "ada:parameter/semCompositionTAPP/chamberPressure",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semCompositionTAPP/chamberPressure"
            }
          ],
          "schema:name": "Chamber Pressure",
          "schema:value": "High vacuum",
          "schema:unitText": "no value available: unnamed property"
        },
        {
          "@id": "ada:parameter/semCompositionTAPP/edsLiveTimePerPointOrPixel",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semCompositionTAPP/edsLiveTimePerPointOrPixel"
            }
          ],
          "schema:name": "EDS Live Time per Point or Pixel",
          "schema:value": 30,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "30 s live time per spot analysis"
        }
      ],
      "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
      "ada:combinedResults": [
        {}
      ],
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

ex:semCompositionTAPP-detail-Pascucci2026 a schema1:Dataset,
        schema1:Product ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "BSE Imaging (Zeiss Supra 40 FE-SEM); SE Imaging (Zeiss Supra 40 FE-SEM); EMPA-WDS (JEOL JXA-8230, separate instrument); VIS-IR spectroscopy (SPIM)" ] ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Embedded in epoxy, polished to ¼ µm level, sputtered with 30-nm-thick carbon film" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semCompositionTAPP/beamDamageMinimization>,
                <https://ada.astromat.org/metadata/parameter/semCompositionTAPP/chamberPressure>,
                <https://ada.astromat.org/metadata/parameter/semCompositionTAPP/edsLiveTimePerPointOrPixel> ;
            schema1:description "Spot analysis: 20 kV, 30 µm aperture, 30 s live time per spot, maximum process time (Oxford INCA Energy)" ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "CNR IMAA (Institute of Methodologies for Environmental Analysis), Italian National Research Council, Potenza, Italy" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
                    schema1:name "NWA 7317" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ bios:computationalTool [ a schema1:SoftwareApplication ;
                            schema1:name "Oxford INCA Energy (semi-quantitative phase determination from atomic proportions)" ;
                            ada:toolRole "dataReduction" ],
                        [ a schema1:SoftwareApplication ;
                            schema1:name "Oxford INCA Energy" ;
                            ada:toolRole "acquisition" ] ],
                [ schema1:instrument <https://example.org/semCompositionTAPP-detail-Pascucci2026/instrument/SEM> ] ;
            ada:combinedResults [ ] ;
            ada:deadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "EDS Point Analysis" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:sampleName "NWA 7317" ;
    ada:samplingUnitName "Sample name only — \"the NWA 7317 slab\" (p.3), imaged on \"almost the same portion of the VIS-IR SPIM images\" (p.4); imaged fields and analysis points are not labelled" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" .

<https://example.org/semCompositionTAPP-detail-Pascucci2026/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semCompositionTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/semCompositionTAPP/beamDiameter> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:name "no value available: schema:name" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "VIS-IR imaging spectroscopy, acquired before the section was prepared — the fragment was embedded and polished \"after the SPectral IMager (SPIM) reflectance spectroscopy imagery acquisition\" and only then carbon coated \"for further SEM-EDS and EMPA-WDS analyses\" (p.3). The SEM work is then registered to those images: \"To cover approximately the same area of the SPIM images (9.7 mm large), 10 BSE images, with four consecutive images in the same row, were acquired and mosaicked\" (p.3)" .

<https://ada.astromat.org/metadata/parameter/semCompositionTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:description "20 kV" ;
    schema1:name "Accelerating Voltage" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semCompositionTAPP/acceleratingVoltage> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 20 .

<https://ada.astromat.org/metadata/parameter/semCompositionTAPP/beamDamageMinimization> a schema1:PropertyValue ;
    schema1:name "Beam Damage Minimization" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semCompositionTAPP/beamDamageMinimization> ;
    schema1:value "all: SEM-EDS run only after the SPIM reflectance measurements — 'This was done only after the SPIM reflectance acquisitions to try to avoid charging effects and by also reducing thermal damage' (p.3)" .

<https://ada.astromat.org/metadata/parameter/semCompositionTAPP/beamDiameter> a schema1:PropertyValue ;
    schema1:description "N — a 30 μm aperture is stated (p.3), not a beam diameter" ;
    schema1:name "Beam Diameter" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semCompositionTAPP/beamDiameter> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 30 .

<https://ada.astromat.org/metadata/parameter/semCompositionTAPP/chamberPressure> a schema1:PropertyValue ;
    schema1:name "Chamber Pressure" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semCompositionTAPP/chamberPressure> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value "High vacuum" .

<https://ada.astromat.org/metadata/parameter/semCompositionTAPP/edsLiveTimePerPointOrPixel> a schema1:PropertyValue ;
    schema1:description "30 s live time per spot analysis" ;
    schema1:name "EDS Live Time per Point or Pixel" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semCompositionTAPP/edsLiveTimePerPointOrPixel> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 30 .


```


### detail example Pascucci2026-2
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
  "@id": "ex:semCompositionTAPP-detail-Pascucci2026-2",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
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
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "SEM",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/semCompositionTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/semCompositionTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 20,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "20 kV"
                },
                {
                  "@id": "ada:parameter/semCompositionTAPP/mappingBeamDiameter",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/semCompositionTAPP/mappingBeamDiameter"
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
              "@id": "ex:semCompositionTAPP-detail-Pascucci2026-2/instrument/SEM"
            }
          ]
        },
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "acquisition",
              "schema:name": "Oxford INCA Energy",
              "@type": [
                "schema:SoftwareApplication"
              ]
            },
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "Oxford INCA Energy (semi-quantitative phase determination from atomic proportions)",
              "@type": [
                "schema:SoftwareApplication"
              ]
            }
          ]
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/semCompositionTAPP/chamberPressure",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semCompositionTAPP/chamberPressure"
            }
          ],
          "schema:name": "Chamber Pressure",
          "schema:value": "High vacuum",
          "schema:unitText": "no value available: unnamed property"
        },
        {
          "@id": "ada:parameter/semCompositionTAPP/edsLiveTimePerPointOrPixel",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semCompositionTAPP/edsLiveTimePerPointOrPixel"
            }
          ],
          "schema:name": "EDS Live Time per Point or Pixel",
          "schema:value": 5,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "5 ms dwell time per pixel"
        },
        {
          "@id": "ada:parameter/semCompositionTAPP/stepSizePixelSize",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semCompositionTAPP/stepSizePixelSize"
            }
          ],
          "schema:name": "Step Size / Pixel Size",
          "schema:value": 2.5,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "2.5 µm"
        }
      ],
      "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
      "ada:combinedResults": [
        {}
      ],
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
  "ada:mapDimensions": "1024 × 768 pixels",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/semCompositionTAPP/mapArea",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/semCompositionTAPP/mapArea"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semCompositionTAPP-detail-Pascucci2026-2",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
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
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "SEM",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/semCompositionTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/semCompositionTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 20,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "20 kV"
                },
                {
                  "@id": "ada:parameter/semCompositionTAPP/mappingBeamDiameter",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/semCompositionTAPP/mappingBeamDiameter"
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
              "@id": "ex:semCompositionTAPP-detail-Pascucci2026-2/instrument/SEM"
            }
          ]
        },
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "acquisition",
              "schema:name": "Oxford INCA Energy",
              "@type": [
                "schema:SoftwareApplication"
              ]
            },
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "Oxford INCA Energy (semi-quantitative phase determination from atomic proportions)",
              "@type": [
                "schema:SoftwareApplication"
              ]
            }
          ]
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/semCompositionTAPP/chamberPressure",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semCompositionTAPP/chamberPressure"
            }
          ],
          "schema:name": "Chamber Pressure",
          "schema:value": "High vacuum",
          "schema:unitText": "no value available: unnamed property"
        },
        {
          "@id": "ada:parameter/semCompositionTAPP/edsLiveTimePerPointOrPixel",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semCompositionTAPP/edsLiveTimePerPointOrPixel"
            }
          ],
          "schema:name": "EDS Live Time per Point or Pixel",
          "schema:value": 5,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "5 ms dwell time per pixel"
        },
        {
          "@id": "ada:parameter/semCompositionTAPP/stepSizePixelSize",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semCompositionTAPP/stepSizePixelSize"
            }
          ],
          "schema:name": "Step Size / Pixel Size",
          "schema:value": 2.5,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "2.5 \u00b5m"
        }
      ],
      "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
      "ada:combinedResults": [
        {}
      ],
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
  "ada:mapDimensions": "1024 \u00d7 768 pixels",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/semCompositionTAPP/mapArea",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/semCompositionTAPP/mapArea"
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

ex:semCompositionTAPP-detail-Pascucci2026-2 a schema1:Dataset,
        schema1:Product ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semCompositionTAPP/mapArea> ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "BSE Imaging (Zeiss Supra 40 FE-SEM); SE Imaging (Zeiss Supra 40 FE-SEM); EMPA-WDS (JEOL JXA-8230, separate instrument); VIS-IR spectroscopy (SPIM)" ] ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Embedded in epoxy, polished to ¼ µm level, sputtered with 30-nm-thick carbon film" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semCompositionTAPP/chamberPressure>,
                <https://ada.astromat.org/metadata/parameter/semCompositionTAPP/edsLiveTimePerPointOrPixel>,
                <https://ada.astromat.org/metadata/parameter/semCompositionTAPP/stepSizePixelSize> ;
            schema1:description "EDS mapping: 20 kV, 60 µm aperture, 5 ms dwell per pixel, 1024×768 pixels, 2.5 µm pixel size, ~10 h total; element maps co-registered with BSE images" ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "CNR IMAA (Institute of Methodologies for Environmental Analysis), Italian National Research Council, Potenza, Italy" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
                    schema1:name "NWA 7317" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ bios:computationalTool [ a schema1:SoftwareApplication ;
                            schema1:name "Oxford INCA Energy" ;
                            ada:toolRole "acquisition" ],
                        [ a schema1:SoftwareApplication ;
                            schema1:name "Oxford INCA Energy (semi-quantitative phase determination from atomic proportions)" ;
                            ada:toolRole "dataReduction" ] ],
                [ schema1:instrument <https://example.org/semCompositionTAPP-detail-Pascucci2026-2/instrument/SEM> ] ;
            ada:combinedResults [ ] ;
            ada:deadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "EDS Mapping" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:mapDimensions "1024 × 768 pixels" ;
    ada:sampleName "NWA 7317" ;
    ada:samplingUnitName "Sample name only — \"the NWA 7317 slab\" (p.3), imaged on \"almost the same portion of the VIS-IR SPIM images\" (p.4); imaged fields and analysis points are not labelled" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" .

<https://example.org/semCompositionTAPP-detail-Pascucci2026-2/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semCompositionTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/semCompositionTAPP/mappingBeamDiameter> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:name "no value available: schema:name" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "VIS-IR imaging spectroscopy, acquired before the section was prepared — the fragment was embedded and polished \"after the SPectral IMager (SPIM) reflectance spectroscopy imagery acquisition\" and only then carbon coated \"for further SEM-EDS and EMPA-WDS analyses\" (p.3). The SEM work is then registered to those images: \"To cover approximately the same area of the SPIM images (9.7 mm large), 10 BSE images, with four consecutive images in the same row, were acquired and mosaicked\" (p.3)" .

<https://ada.astromat.org/metadata/parameter/semCompositionTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:description "20 kV" ;
    schema1:name "Accelerating Voltage" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semCompositionTAPP/acceleratingVoltage> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 20 .

<https://ada.astromat.org/metadata/parameter/semCompositionTAPP/chamberPressure> a schema1:PropertyValue ;
    schema1:name "Chamber Pressure" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semCompositionTAPP/chamberPressure> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value "High vacuum" .

<https://ada.astromat.org/metadata/parameter/semCompositionTAPP/edsLiveTimePerPointOrPixel> a schema1:PropertyValue ;
    schema1:description "5 ms dwell time per pixel" ;
    schema1:name "EDS Live Time per Point or Pixel" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semCompositionTAPP/edsLiveTimePerPointOrPixel> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 5 .

<https://ada.astromat.org/metadata/parameter/semCompositionTAPP/mapArea> a schema1:PropertyValue ;
    schema1:description "10.5 × 4.0 mm — 'The area acquired by the SEM-EDS instrument is 10.5 × 4.0 mm wide and it is composed of nine mosaicked images (magnification 138×)'" ;
    schema1:name "Map Area" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semCompositionTAPP/mapArea> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1.05e+01 .

<https://ada.astromat.org/metadata/parameter/semCompositionTAPP/mappingBeamDiameter> a schema1:PropertyValue ;
    schema1:description "N — a 60 μm aperture is stated (p.3), not a beam diameter" ;
    schema1:name "Mapping Beam Diameter" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semCompositionTAPP/mappingBeamDiameter> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 60 .

<https://ada.astromat.org/metadata/parameter/semCompositionTAPP/stepSizePixelSize> a schema1:PropertyValue ;
    schema1:description "2.5 µm" ;
    schema1:name "Step Size / Pixel Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semCompositionTAPP/stepSizePixelSize> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 2.5e+00 .


```


### detail example Zega2025
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
  "@id": "ex:semCompositionTAPP-detail-Zega2025",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
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
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "SEM",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/semCompositionTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/semCompositionTAPP/acceleratingVoltage"
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
              "@id": "ex:semCompositionTAPP-detail-Zega2025/instrument/SEM"
            }
          ]
        },
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "acquisition",
              "schema:name": "Oxford AZtec (Point & ID programme)",
              "@type": [
                "schema:SoftwareApplication"
              ]
            },
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "Oxford AZtec",
              "@type": [
                "schema:SoftwareApplication"
              ]
            }
          ]
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/semCompositionTAPP/edsLiveTimePerPointOrPixel",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semCompositionTAPP/edsLiveTimePerPointOrPixel"
            }
          ],
          "schema:name": "EDS Live Time per Point or Pixel",
          "schema:value": 20,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "20 to 200 s (per point)"
        }
      ],
      "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
      "ada:combinedResults": [
        {}
      ],
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semCompositionTAPP-detail-Zega2025",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
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
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "SEM",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/semCompositionTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/semCompositionTAPP/acceleratingVoltage"
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
              "@id": "ex:semCompositionTAPP-detail-Zega2025/instrument/SEM"
            }
          ]
        },
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "acquisition",
              "schema:name": "Oxford AZtec (Point & ID programme)",
              "@type": [
                "schema:SoftwareApplication"
              ]
            },
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "Oxford AZtec",
              "@type": [
                "schema:SoftwareApplication"
              ]
            }
          ]
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/semCompositionTAPP/edsLiveTimePerPointOrPixel",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semCompositionTAPP/edsLiveTimePerPointOrPixel"
            }
          ],
          "schema:name": "EDS Live Time per Point or Pixel",
          "schema:value": 20,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "20 to 200 s (per point)"
        }
      ],
      "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
      "ada:combinedResults": [
        {}
      ],
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

ex:semCompositionTAPP-detail-Zega2025 a schema1:Dataset,
        schema1:Product ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "NASA award NNH09ZDA007O; contract NNM10AA11C (OSIRIS-REx New Frontiers)" ] ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "BSE Imaging (JEOL 7600F, JSC); SE Imaging (JEOL 7600F, JSC); FIB-SEM TEM prep (Quanta3D600, JSC)" ] ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Attached to Al cylinder SEM mount with double-sided C tape; sputter coated with ~5 nm carbon" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semCompositionTAPP/edsLiveTimePerPointOrPixel> ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "NASA Johnson Space Center (JSC), Houston, TX, USA" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
                    schema1:name "no value available: schema:name" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ schema1:instrument <https://example.org/semCompositionTAPP-detail-Zega2025/instrument/SEM> ],
                [ bios:computationalTool [ a schema1:SoftwareApplication ;
                            schema1:name "Oxford AZtec" ;
                            ada:toolRole "dataReduction" ],
                        [ a schema1:SoftwareApplication ;
                            schema1:name "Oxford AZtec (Point & ID programme)" ;
                            ada:toolRole "acquisition" ] ] ;
            ada:combinedResults [ ] ;
            ada:deadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "EDS Point Analysis" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NASA award NNH09ZDA007O; contract NNM10AA11C (OSIRIS-REx New Frontiers)" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "N — the JSC SEM passage names no specimen (\"The particle was attached to an Al cylinder SEM mount\"; \"regions of interest\", p.9); the paper's OREX numbers identify figures, not this laboratory's analyses" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" .

<https://example.org/semCompositionTAPP-detail-Zega2025/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semCompositionTAPP/acceleratingVoltage> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:name "no value available: schema:name" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "Optical microscopy before coating — \"After initial documentation by optical microscopy, the sample was sputter coated with ~5 nm of C to assist with charge dissipation during SEM analysis\" (p.9)" .

<https://ada.astromat.org/metadata/parameter/semCompositionTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:description "15 kV" ;
    schema1:name "Accelerating Voltage" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semCompositionTAPP/acceleratingVoltage> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 15 .

<https://ada.astromat.org/metadata/parameter/semCompositionTAPP/edsLiveTimePerPointOrPixel> a schema1:PropertyValue ;
    schema1:description "20 to 200 s (per point)" ;
    schema1:name "EDS Live Time per Point or Pixel" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semCompositionTAPP/edsLiveTimePerPointOrPixel> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 20 .


```


### detail example Zega2025-2
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
  "@id": "ex:semCompositionTAPP-detail-Zega2025-2",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
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
      "ada:combinedResults": [
        {}
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "K-ALFAA (Kuiper-Arizona Laboratory for Astromaterials Analysis), University of Arizona"
      },
      "prov:used": [
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "acquisition",
              "schema:name": "Oxford Instruments Aztec Live/x-stream",
              "@type": [
                "schema:SoftwareApplication"
              ]
            },
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "Oxford Instruments Aztec",
              "@type": [
                "schema:SoftwareApplication"
              ]
            }
          ]
        }
      ],
      "schema:description": "Compositional heterogeneity assessed through EDS mapping; no specific kV, current, dwell time stated for S-4800 EDS",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Polished sections; coated with 0.1 nm carbon for charge mitigation",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semCompositionTAPP-detail-Zega2025-2",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
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
      "ada:combinedResults": [
        {}
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "K-ALFAA (Kuiper-Arizona Laboratory for Astromaterials Analysis), University of Arizona"
      },
      "prov:used": [
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "acquisition",
              "schema:name": "Oxford Instruments Aztec Live/x-stream",
              "@type": [
                "schema:SoftwareApplication"
              ]
            },
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "Oxford Instruments Aztec",
              "@type": [
                "schema:SoftwareApplication"
              ]
            }
          ]
        }
      ],
      "schema:description": "Compositional heterogeneity assessed through EDS mapping; no specific kV, current, dwell time stated for S-4800 EDS",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Polished sections; coated with 0.1 nm carbon for charge mitigation",
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

ex:semCompositionTAPP-detail-Zega2025-2 a schema1:Dataset,
        schema1:Product ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "NASA PSEF 80NSSC23K0327; NSF MRI 1531243 and 0619599" ] ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "SE/BSE Imaging (Hitachi S-4800, U Arizona); FIB-SEM TEM prep (Helios G3, U Arizona); EMPA (Cameca SX-100 Ultra, out of scope)" ] ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Polished sections; coated with 0.1 nm carbon for charge mitigation" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ] ] ;
            schema1:description "Compositional heterogeneity assessed through EDS mapping; no specific kV, current, dwell time stated for S-4800 EDS" ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "K-ALFAA (Kuiper-Arizona Laboratory for Astromaterials Analysis), University of Arizona" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
                    schema1:name "no value available: schema:name" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ bios:computationalTool [ a schema1:SoftwareApplication ;
                            schema1:name "Oxford Instruments Aztec Live/x-stream" ;
                            ada:toolRole "acquisition" ],
                        [ a schema1:SoftwareApplication ;
                            schema1:name "Oxford Instruments Aztec" ;
                            ada:toolRole "dataReduction" ] ] ;
            ada:combinedResults [ ] ;
            ada:deadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "EDS Mapping" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NASA PSEF 80NSSC23K0327; NSF MRI 1531243 and 0619599" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "N — the Arizona SEM passage names no specimen (\"Polished sections were coated with a thin layer ... of carbon\", p.9); the paper's OREX numbers identify figures, not this laboratory's analyses" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "N — the passage describes mounting and coating only (\"Polished sections were coated with a thin layer (0.1 nm) of carbon to mitigate charge build-up\", p.9); no prior imaging or screening is described" .


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
  "@id": "ex:semCompositionTAPP-detail-Barnes2025",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
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
      "ada:combinedResults": [
        {}
      ],
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
      "ada:deadTime": -9999
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semCompositionTAPP-detail-Barnes2025",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
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
      "ada:combinedResults": [
        {}
      ],
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
      "ada:deadTime": -9999
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
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:semCompositionTAPP-detail-Barnes2025 a schema1:Dataset,
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
            ada:deadTime -9999 ;
            ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalMode "EDS Mapping" ;
    ada:analyticalPrecision "missing" ;
    ada:detectionLimit -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:sampleName "OREX-501018-100" ;
    ada:samplingUnitName "Labelled: \"Bennu sample OREX-501018-100\" (Extended Data Fig. 8 caption, p.27), \"aggregate QL material pressed onto a gold (Au) foil mount\" (p.10); the presolar-grain regions are not labelled" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "NanoSIMS isotope imaging — the two grains this procedure analyses were found by raster ion imaging of the Au foil mount, each image \"256 × 256 pixels, analysed at 1,800 μs per pixel for 32 frames\", with grains counted presolar if their composition \"differed from the reference ratios by >5σ\" and the anomaly persisted across frames; \"Two O-rich presolar grains were also analysed by SEM-EDS to further constrain the phase\" (p.11)" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: SEM Composition Analysis Detail
description: Dataset-level analysis-instance detail for SEM composition (EDS/WDS),
  reusing CDIF/schema.org slots on the schema:Dataset root.
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
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Analysis_samplingUnitSelectionCriteria
              - title: Beam Raster Dimensions
                description: "Dimensions of the small area over which the beam is
                  rastered at a single analysis point, reported as width \xD7 height
                  in \xB5m. Applicable when Beam Mode = Rastered; defines the effective
                  spatial footprint of the measurement. Not applicable when mapping."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semCompositionTAPP/beamRasterDimensions
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semCompositionTAPP/beamRasterDimensions
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
              - title: Beam Damage Minimization
                description: 'Describes any measures taken to reduce electron beam
                  damage to the sample during analysis. Examples: reduced accelerating
                  voltage, lowered beam current, defocused or rastered beam, cooled
                  stage, short acquisition sequences, or rotating between multiple
                  points.'
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semCompositionTAPP/beamDamageMinimization
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semCompositionTAPP/beamDamageMinimization
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
              - title: Drift Correction
                description: 'Describes whether and how stage or beam drift was monitored
                  and corrected during the measurement session. Examples: periodic
                  stage realignment to a fiducial marker, automated beam drift correction
                  in acquisition software, or reanalysis of a reference point at regular
                  intervals.'
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semCompositionTAPP/driftCorrection
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semCompositionTAPP/driftCorrection
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
              - title: Chamber Pressure
                description: Chamber pressure and gas type during analysis. Required
                  for variable pressure (VP-SEM) and environmental SEM (ESEM) modes.
                  Report value and unit (Pa or Torr) and gas composition. Use 'None'
                  for standard high-vacuum operation.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semCompositionTAPP/chamberPressure
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semCompositionTAPP/chamberPressure
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
              - title: EDS Live Time per Point or Pixel
                description: EDS spectral acquisition live time per analysis point
                  or per pixel in seconds.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semCompositionTAPP/edsLiveTimePerPointOrPixel
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semCompositionTAPP/edsLiveTimePerPointOrPixel
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
              - title: Step Size / Pixel Size
                description: "Centre-to-centre distance between adjacent measurement
                  points (WDS mapping) or pixels (EDS mapping) in \xB5m."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semCompositionTAPP/stepSizePixelSize
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semCompositionTAPP/stepSizePixelSize
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
              - title: Halogen Correction on Oxygen
                description: Whether oxygen content was adjusted to account for halogen
                  substitution (F and/or Cl replacing OH) in halogen-bearing phases
                  such as apatite, amphibole, and mica, where oxygen is calculated
                  by stoichiometry.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semCompositionTAPP/halogenCorrectionOnOxygen
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semCompositionTAPP/halogenCorrectionOnOxygen
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
            allOf:
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Analysis_samplingUnitSelectionCriteria
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
                    const: ada:parameter/semCompositionTAPP/beamRasterDimensions
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semCompositionTAPP/beamRasterDimensions
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
                title: Beam Damage Minimization
                description: 'Describes any measures taken to reduce electron beam
                  damage to the sample during analysis. Examples: reduced accelerating
                  voltage, lowered beam current, defocused or rastered beam, cooled
                  stage, short acquisition sequences, or rotating between multiple
                  points.'
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semCompositionTAPP/beamDamageMinimization
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semCompositionTAPP/beamDamageMinimization
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
                title: Drift Correction
                description: 'Describes whether and how stage or beam drift was monitored
                  and corrected during the measurement session. Examples: periodic
                  stage realignment to a fiducial marker, automated beam drift correction
                  in acquisition software, or reanalysis of a reference point at regular
                  intervals.'
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semCompositionTAPP/driftCorrection
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semCompositionTAPP/driftCorrection
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
                title: Chamber Pressure
                description: Chamber pressure and gas type during analysis. Required
                  for variable pressure (VP-SEM) and environmental SEM (ESEM) modes.
                  Report value and unit (Pa or Torr) and gas composition. Use 'None'
                  for standard high-vacuum operation.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semCompositionTAPP/chamberPressure
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semCompositionTAPP/chamberPressure
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
                title: EDS Live Time per Point or Pixel
                description: EDS spectral acquisition live time per analysis point
                  or per pixel in seconds.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semCompositionTAPP/edsLiveTimePerPointOrPixel
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semCompositionTAPP/edsLiveTimePerPointOrPixel
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
                title: Step Size / Pixel Size
                description: "Centre-to-centre distance between adjacent measurement
                  points (WDS mapping) or pixels (EDS mapping) in \xB5m."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semCompositionTAPP/stepSizePixelSize
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semCompositionTAPP/stepSizePixelSize
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
                title: Halogen Correction on Oxygen
                description: Whether oxygen content was adjusted to account for halogen
                  substitution (F and/or Cl replacing OH) in halogen-bearing phases
                  such as apatite, amphibole, and mica, where oxygen is calculated
                  by stoichiometry.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semCompositionTAPP/halogenCorrectionOnOxygen
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semCompositionTAPP/halogenCorrectionOnOxygen
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
                                      description: Electron beam accelerating voltage
                                        in kilovolts.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/semCompositionTAPP/acceleratingVoltage
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/semCompositionTAPP/acceleratingVoltage
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
                                      description: Nominal electron beam diameter
                                        (spot size) at the sample surface for point
                                        analysis, in nanometres or micrometres, as
                                        set by the condenser aperture and working
                                        distance. The beam used for mapping is recorded
                                        under Mapping Beam Diameter.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/semCompositionTAPP/beamDiameter
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/semCompositionTAPP/beamDiameter
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
                                    - title: Working Distance
                                      description: Distance between the objective
                                        lens pole piece and the specimen surface in
                                        millimetres.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/semCompositionTAPP/workingDistance
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/semCompositionTAPP/workingDistance
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
                                    - title: Mapping Beam Current
                                      description: Probe current in nanoamperes (nA)
                                        used during X-ray mapping.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/semCompositionTAPP/mappingBeamCurrent
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/semCompositionTAPP/mappingBeamCurrent
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
                                          const: ada:parameter/semCompositionTAPP/mappingBeamDiameter
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/semCompositionTAPP/mappingBeamDiameter
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
                                        in kilovolts.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/semCompositionTAPP/acceleratingVoltage
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/semCompositionTAPP/acceleratingVoltage
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
                                      description: Nominal electron beam diameter
                                        (spot size) at the sample surface for point
                                        analysis, in nanometres or micrometres, as
                                        set by the condenser aperture and working
                                        distance. The beam used for mapping is recorded
                                        under Mapping Beam Diameter.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/semCompositionTAPP/beamDiameter
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/semCompositionTAPP/beamDiameter
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
                                      title: Working Distance
                                      description: Distance between the objective
                                        lens pole piece and the specimen surface in
                                        millimetres.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/semCompositionTAPP/workingDistance
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/semCompositionTAPP/workingDistance
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
                                  - contains:
                                      title: Mapping Beam Current
                                      description: Probe current in nanoamperes (nA)
                                        used during X-ray mapping.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/semCompositionTAPP/mappingBeamCurrent
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/semCompositionTAPP/mappingBeamCurrent
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
                                          const: ada:parameter/semCompositionTAPP/mappingBeamDiameter
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/semCompositionTAPP/mappingBeamDiameter
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
          ada:deadTime:
            description: "Percent dead time reported by the EDS detector during the
              session \u2014 the fraction of total acquisition time the detector spent
              processing rather than counting. This field documents the resulting
              percentage as a session QC metric. Unlike WDS dead time (see WDS Dead
              Time Correction), no user-selectable correction algorithm is required."
            anyOf:
            - type: number
            - type: string
        required:
        - ada:deadTime
        - ada:proceduralBlankLevel
      title: Analysis Events
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
            const: ada:parameter/semCompositionTAPP/mapArea
          '@type':
            const:
            - schema:PropertyValue
          schema:propertyID:
            const:
            - '@id': ada:parameter/semCompositionTAPP/mapArea
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
              const: ada:parameter/semCompositionTAPP/mapArea
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/semCompositionTAPP/mapArea
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
    dqv:hasQualityMeasurement:
      type: array
      items:
        type: object
        allOf:
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
      allOf:
      - contains:
          properties:
            dqv:isMeasurementOf:
              const: Analytical Precision
          required:
          - dqv:isMeasurementOf
      - contains:
          properties:
            dqv:isMeasurementOf:
              const: Analytical Accuracy
          required:
          - dqv:isMeasurementOf
      title: Quality Measurements
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
              const: ada:parameter/semCompositionTAPP/targetMaterialOfSamplingUnit
            '@type':
              const:
              - schema:PropertyValue
              - cdi:InstanceVariable
            schema:propertyID:
              const:
              - '@id': ada:parameter/semCompositionTAPP/targetMaterialOfSamplingUnit
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
              const: ada:parameter/semCompositionTAPP/targetMaterialOfSamplingUnit
            '@type':
              const:
              - schema:PropertyValue
              - cdi:InstanceVariable
            schema:propertyID:
              const:
              - '@id': ada:parameter/semCompositionTAPP/targetMaterialOfSamplingUnit
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
x-bblocks-metadata:
  itemIdentifier: ogch.techniqueProfile.geochemProfile.SEM-Composition.detail
  register: https://amds-ldeo.github.io/geochemBuildingBlocks/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-11-09'

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/detail/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/detail/schema.yaml)


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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/detail/context.jsonld)

## Sources

* [SEM_Composition_TAPP_v4.xlsx (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/SEM-Composition/detail`

