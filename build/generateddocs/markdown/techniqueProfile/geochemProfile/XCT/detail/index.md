
# Lab-XCT Analysis Detail (Schema)

`ogch.techniqueProfile.geochemProfile.XCT.detail` *v0.1*

Laboratory X-ray computed tomography analysis-specific detail properties. Discriminates on ada:componentType (XCTVolume, XCTProjectionImageSet, XCTSegmentationVolume, XCTRenderedVideo, XCTQuantitativeTabular), carries analysis-level required properties (analyst, dates, sample, VOI) and per-dataset schema:additionalProperty values referencing the labxctTAPP parameterValues registry.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### detail example Eckley2024
detail instance derived from Eckley 2024 (JSC Scan Record) Bennu particle Single-volume Nikon XTH 320 NASA JSC X-FaCT.
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
  "@id": "ex:labxctTAPP-detail-Eckley2024",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "prov:used": [
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "Nikon CTPro3D v5.4",
              "@type": [
                "schema:SoftwareApplication"
              ]
            }
          ]
        },
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "XCT",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/labxctTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 110,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "110 kV"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/tubeCurrent",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/tubeCurrent"
                    }
                  ],
                  "schema:name": "Tube Current",
                  "schema:value": 27,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "27 µA"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/xRayPreFilter",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/xRayPreFilter"
                    }
                  ],
                  "schema:name": "X-ray Pre-filter",
                  "schema:value": "0.25 mm aluminum"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/voxelSize",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/voxelSize"
                    }
                  ],
                  "schema:name": "Voxel Size",
                  "schema:value": 6.0,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "6.00 µm"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:labxctTAPP-detail-Eckley2024/instrument/XCT"
            }
          ]
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/labxctTAPP/xRayPower",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/xRayPower"
            }
          ],
          "schema:name": "X-ray Power",
          "schema:value": 3.0,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "3.0 W"
        },
        {
          "@id": "ada:parameter/labxctTAPP/sourceToObjectDistance",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/sourceToObjectDistance"
            }
          ],
          "schema:name": "Source-to-Object Distance (SOD)",
          "schema:value": 20.39,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "20.39 mm"
        },
        {
          "@id": "ada:parameter/labxctTAPP/sourceToDetectorDistance",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/sourceToDetectorDistance"
            }
          ],
          "schema:name": "Source-to-Detector Distance (SDD)",
          "schema:value": 679.51,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "679.51 mm"
        },
        {
          "@id": "ada:parameter/labxctTAPP/numberOfProjections",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/numberOfProjections"
            }
          ],
          "schema:name": "Number of Projections",
          "schema:value": 4000
        },
        {
          "@id": "ada:parameter/labxctTAPP/exposureTimePerProjection",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/exposureTimePerProjection"
            }
          ],
          "schema:name": "Exposure Time per Projection",
          "schema:value": 4.0,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "4.00 s"
        },
        {
          "@id": "ada:parameter/labxctTAPP/framesAveragedPerProjection",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/framesAveragedPerProjection"
            }
          ],
          "schema:name": "Frames Averaged per Projection",
          "schema:value": 1,
          "schema:description": "1 frame"
        },
        {
          "@id": "ada:parameter/labxctTAPP/detectorBinning",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/detectorBinning"
            }
          ],
          "schema:name": "Detector Binning",
          "schema:value": "1×1 (no binning)"
        },
        {
          "@id": "ada:parameter/labxctTAPP/rotationMode",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/rotationMode"
            }
          ],
          "schema:name": "Rotation Mode",
          "schema:value": "Continuous rotation"
        },
        {
          "@id": "ada:parameter/labxctTAPP/beamHardeningCorrectionParameter",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/beamHardeningCorrectionParameter"
            }
          ],
          "schema:name": "Beam Hardening Correction Parameter",
          "schema:value": "Preset 4"
        },
        {
          "@id": "ada:parameter/labxctTAPP/outputBitDepth",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/outputBitDepth"
            }
          ],
          "schema:name": "Output Bit Depth",
          "schema:value": "16-bit (full grayscale range)"
        }
      ],
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Data processing",
            "schema:additionalProperty": [
              {
                "@id": "ada:parameter/labxctTAPP/flatFieldCorrection",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/labxctTAPP/flatFieldCorrection"
                  }
                ],
                "schema:name": "Flat Field Correction",
                "schema:value": "Flux normalization: no"
              }
            ],
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          }
        ]
      },
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "NASA JSC Astromaterials X-FaCT Lab"
      },
      "schema:startTime": "2024-10-29",
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:name": "OREX-800099-0"
        }
      ],
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier"
    }
  ],
  "schema:distribution": [
    {
      "schema:encodingFormat": [
        "TIFF (16-bit, 928 slices)"
      ]
    }
  ],
  "schema:contributor": [
    {
      "schema:roleName": "analyst",
      "schema:contributor": {
        "schema:name": "Scott Eckley"
      }
    }
  ],
  "ada:analyticalMode": [
    "Single-volume"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "Scott Eckley",
  "ada:analysisStartDate": "2024-10-29",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleDimensions": "missing",
  "ada:sampleName": "OREX-800099-0",
  "ada:samplingUnitName": "Sample name only — the scan record's \"Sample name: OREX-800099-0\", \"Sample type: Asteroid Bennu particle\" (p.1); one whole-particle scan",
  "ada:voiApplied": "missing"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XCT/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:labxctTAPP-detail-Eckley2024",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "prov:used": [
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "Nikon CTPro3D v5.4",
              "@type": [
                "schema:SoftwareApplication"
              ]
            }
          ]
        },
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "XCT",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/labxctTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 110,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "110 kV"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/tubeCurrent",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/tubeCurrent"
                    }
                  ],
                  "schema:name": "Tube Current",
                  "schema:value": 27,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "27 \u00b5A"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/xRayPreFilter",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/xRayPreFilter"
                    }
                  ],
                  "schema:name": "X-ray Pre-filter",
                  "schema:value": "0.25 mm aluminum"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/voxelSize",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/voxelSize"
                    }
                  ],
                  "schema:name": "Voxel Size",
                  "schema:value": 6.0,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "6.00 \u00b5m"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:labxctTAPP-detail-Eckley2024/instrument/XCT"
            }
          ]
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/labxctTAPP/xRayPower",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/xRayPower"
            }
          ],
          "schema:name": "X-ray Power",
          "schema:value": 3.0,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "3.0 W"
        },
        {
          "@id": "ada:parameter/labxctTAPP/sourceToObjectDistance",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/sourceToObjectDistance"
            }
          ],
          "schema:name": "Source-to-Object Distance (SOD)",
          "schema:value": 20.39,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "20.39 mm"
        },
        {
          "@id": "ada:parameter/labxctTAPP/sourceToDetectorDistance",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/sourceToDetectorDistance"
            }
          ],
          "schema:name": "Source-to-Detector Distance (SDD)",
          "schema:value": 679.51,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "679.51 mm"
        },
        {
          "@id": "ada:parameter/labxctTAPP/numberOfProjections",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/numberOfProjections"
            }
          ],
          "schema:name": "Number of Projections",
          "schema:value": 4000
        },
        {
          "@id": "ada:parameter/labxctTAPP/exposureTimePerProjection",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/exposureTimePerProjection"
            }
          ],
          "schema:name": "Exposure Time per Projection",
          "schema:value": 4.0,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "4.00 s"
        },
        {
          "@id": "ada:parameter/labxctTAPP/framesAveragedPerProjection",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/framesAveragedPerProjection"
            }
          ],
          "schema:name": "Frames Averaged per Projection",
          "schema:value": 1,
          "schema:description": "1 frame"
        },
        {
          "@id": "ada:parameter/labxctTAPP/detectorBinning",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/detectorBinning"
            }
          ],
          "schema:name": "Detector Binning",
          "schema:value": "1\u00d71 (no binning)"
        },
        {
          "@id": "ada:parameter/labxctTAPP/rotationMode",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/rotationMode"
            }
          ],
          "schema:name": "Rotation Mode",
          "schema:value": "Continuous rotation"
        },
        {
          "@id": "ada:parameter/labxctTAPP/beamHardeningCorrectionParameter",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/beamHardeningCorrectionParameter"
            }
          ],
          "schema:name": "Beam Hardening Correction Parameter",
          "schema:value": "Preset 4"
        },
        {
          "@id": "ada:parameter/labxctTAPP/outputBitDepth",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/outputBitDepth"
            }
          ],
          "schema:name": "Output Bit Depth",
          "schema:value": "16-bit (full grayscale range)"
        }
      ],
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Data processing",
            "schema:additionalProperty": [
              {
                "@id": "ada:parameter/labxctTAPP/flatFieldCorrection",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/labxctTAPP/flatFieldCorrection"
                  }
                ],
                "schema:name": "Flat Field Correction",
                "schema:value": "Flux normalization: no"
              }
            ],
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          }
        ]
      },
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "NASA JSC Astromaterials X-FaCT Lab"
      },
      "schema:startTime": "2024-10-29",
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:name": "OREX-800099-0"
        }
      ],
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier"
    }
  ],
  "schema:distribution": [
    {
      "schema:encodingFormat": [
        "TIFF (16-bit, 928 slices)"
      ]
    }
  ],
  "schema:contributor": [
    {
      "schema:roleName": "analyst",
      "schema:contributor": {
        "schema:name": "Scott Eckley"
      }
    }
  ],
  "ada:analyticalMode": [
    "Single-volume"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "Scott Eckley",
  "ada:analysisStartDate": "2024-10-29",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleDimensions": "missing",
  "ada:sampleName": "OREX-800099-0",
  "ada:samplingUnitName": "Sample name only \u2014 the scan record's \"Sample name: OREX-800099-0\", \"Sample type: Asteroid Bennu particle\" (p.1); one whole-particle scan",
  "ada:voiApplied": "missing"
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

ex:labxctTAPP-detail-Eckley2024 a schema1:Dataset,
        schema1:Product ;
    schema1:contributor [ schema1:contributor [ schema1:name "Scott Eckley" ] ;
            schema1:roleName "analyst" ] ;
    schema1:distribution [ schema1:encodingFormat "TIFF (16-bit, 928 slices)" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/flatFieldCorrection> ;
                            schema1:name "Data processing" ;
                            schema1:position 1 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/beamHardeningCorrectionParameter>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/detectorBinning>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/exposureTimePerProjection>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/framesAveragedPerProjection>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/numberOfProjections>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/outputBitDepth>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/rotationMode>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/sourceToDetectorDistance>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/sourceToObjectDistance>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayPower> ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "NASA JSC Astromaterials X-FaCT Lab" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:name "OREX-800099-0" ] ;
            schema1:startTime "2024-10-29" ;
            prov:used [ schema1:instrument <https://example.org/labxctTAPP-detail-Eckley2024/instrument/XCT> ],
                [ bios:computationalTool [ a schema1:SoftwareApplication ;
                            schema1:name "Nikon CTPro3D v5.4" ;
                            ada:toolRole "dataReduction" ] ] ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "2024-10-29" ;
    ada:analyst "Scott Eckley" ;
    ada:analyticalMode "Single-volume" ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:sampleDimensions "missing" ;
    ada:sampleName "OREX-800099-0" ;
    ada:samplingUnitName "Sample name only — the scan record's \"Sample name: OREX-800099-0\", \"Sample type: Asteroid Bennu particle\" (p.1); one whole-particle scan" ;
    ada:sessionIdentifier "missing" ;
    ada:voiApplied "missing" .

<https://example.org/labxctTAPP-detail-Eckley2024/instrument/XCT> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/tubeCurrent>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/voxelSize>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayPreFilter> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "XCT" ;
    schema1:name "no value available: schema:name" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:description "110 kV" ;
    schema1:name "Accelerating Voltage" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/acceleratingVoltage> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 110 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/beamHardeningCorrectionParameter> a schema1:PropertyValue ;
    schema1:name "Beam Hardening Correction Parameter" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/beamHardeningCorrectionParameter> ;
    schema1:value "Preset 4" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/detectorBinning> a schema1:PropertyValue ;
    schema1:name "Detector Binning" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/detectorBinning> ;
    schema1:value "1×1 (no binning)" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/exposureTimePerProjection> a schema1:PropertyValue ;
    schema1:description "4.00 s" ;
    schema1:name "Exposure Time per Projection" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/exposureTimePerProjection> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 4e+00 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/flatFieldCorrection> a schema1:PropertyValue ;
    schema1:name "Flat Field Correction" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/flatFieldCorrection> ;
    schema1:value "Flux normalization: no" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/framesAveragedPerProjection> a schema1:PropertyValue ;
    schema1:description "1 frame" ;
    schema1:name "Frames Averaged per Projection" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/framesAveragedPerProjection> ;
    schema1:value 1 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/numberOfProjections> a schema1:PropertyValue ;
    schema1:name "Number of Projections" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/numberOfProjections> ;
    schema1:value 4000 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/outputBitDepth> a schema1:PropertyValue ;
    schema1:name "Output Bit Depth" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/outputBitDepth> ;
    schema1:value "16-bit (full grayscale range)" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/rotationMode> a schema1:PropertyValue ;
    schema1:name "Rotation Mode" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/rotationMode> ;
    schema1:value "Continuous rotation" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/sourceToDetectorDistance> a schema1:PropertyValue ;
    schema1:description "679.51 mm" ;
    schema1:name "Source-to-Detector Distance (SDD)" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/sourceToDetectorDistance> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 6.7951e+02 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/sourceToObjectDistance> a schema1:PropertyValue ;
    schema1:description "20.39 mm" ;
    schema1:name "Source-to-Object Distance (SOD)" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/sourceToObjectDistance> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 2.039e+01 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/tubeCurrent> a schema1:PropertyValue ;
    schema1:description "27 µA" ;
    schema1:name "Tube Current" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/tubeCurrent> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 27 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/voxelSize> a schema1:PropertyValue ;
    schema1:description "6.00 µm" ;
    schema1:name "Voxel Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/voxelSize> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 6e+00 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayPower> a schema1:PropertyValue ;
    schema1:description "3.0 W" ;
    schema1:name "X-ray Power" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayPower> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 3e+00 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayPreFilter> a schema1:PropertyValue ;
    schema1:name "X-ray Pre-filter" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayPreFilter> ;
    schema1:value "0.25 mm aluminum" .


```


### detail example Genge2025
detail instance derived from Genge et al. 2025 (Nat. Commun.) Ryugu particle (A0180) Single-volume Zeiss Versa Not stated.
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
  "@id": "ex:labxctTAPP-detail-Genge2025",
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
              "@id": "ada:parameter/labxctTAPP/sampleDimensions",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/labxctTAPP/sampleDimensions"
                }
              ],
              "schema:name": "Sample Dimensions (L × W × H)",
              "schema:value": "1.592 × 0.756 × 0.985 mm"
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
              "schema:value": "Optical microscopy — morphological inspection of the sample exterior through the container window with the CLOXS digital optical microscope system on automated digital sample stages at JAXA/ISAS, before the sample was decanted for nano-XCT"
            }
          ],
          "schema:name": "A0180 (A0180-A and A0180-B)"
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/labxctTAPP/sampleMountingMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/sampleMountingMethod"
            }
          ],
          "schema:name": "Sample Mounting Method",
          "schema:value": "Mounted in pipette tips"
        },
        {
          "@id": "ada:parameter/labxctTAPP/rotationRange",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/rotationRange"
            }
          ],
          "schema:name": "Rotation Range",
          "schema:value": 360,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "360°"
        },
        {
          "@id": "ada:parameter/labxctTAPP/numberOfProjections",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/numberOfProjections"
            }
          ],
          "schema:name": "Number of Projections",
          "schema:value": 2401
        },
        {
          "@id": "ada:parameter/labxctTAPP/exposureTimePerProjection",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/exposureTimePerProjection"
            }
          ],
          "schema:name": "Exposure Time per Projection",
          "schema:value": 33,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "33 s (A0180-A); 28 s (A0180-B)"
        },
        {
          "@id": "ada:parameter/labxctTAPP/detectorBinning",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/detectorBinning"
            }
          ],
          "schema:name": "Detector Binning",
          "schema:value": "No binning"
        },
        {
          "@id": "ada:parameter/labxctTAPP/segmentationMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/segmentationMethod"
            }
          ],
          "schema:name": "Segmentation Method",
          "schema:value": "ImageJ threshold-based; TANGO plugin for 3D object detection"
        },
        {
          "@id": "ada:parameter/labxctTAPP/phaseIdentificationMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/phaseIdentificationMethod"
            }
          ],
          "schema:name": "Phase Identification Method",
          "schema:value": "Sulphide rims of SSOs identified by bright contrast; silicate glass by contrast relative to matrix"
        },
        {
          "@id": "ada:parameter/labxctTAPP/outputBitDepth",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/outputBitDepth"
            }
          ],
          "schema:name": "Output Bit Depth",
          "schema:value": "16-bit (CCD pixel depth)"
        },
        {
          "@id": "ada:parameter/labxctTAPP/partialVolumeEffectCriteria",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/partialVolumeEffectCriteria"
            }
          ],
          "schema:name": "Partial Volume Effect Criteria",
          "schema:value": "SSOs ≥ 5.4 µm identified (implicit: features ≥ voxel size = 0.625 µm); sulphide rims ≥ 1 voxel required for detection"
        }
      ],
      "prov:used": [
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "ImageJ + TANGO plugin (Ollion et al. 2013)",
              "@type": [
                "schema:SoftwareApplication"
              ]
            }
          ]
        },
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "XCT",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/labxctTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 90,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "90 kV"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/tubeCurrent",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/tubeCurrent"
                    }
                  ],
                  "schema:name": "Tube Current",
                  "schema:value": 89,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "89 µA"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/xRayPreFilter",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/xRayPreFilter"
                    }
                  ],
                  "schema:name": "X-ray Pre-filter",
                  "schema:value": "Inbuilt LE4 filter (beam hardening reduction)"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/voxelSize",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/voxelSize"
                    }
                  ],
                  "schema:name": "Voxel Size",
                  "schema:value": 0.625,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "0.625 µm (A0180-A); 0.672 µm (A0180-B)"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:labxctTAPP-detail-Genge2025/instrument/XCT"
            }
          ]
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Not stated"
      },
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Bulk specimen or fragment — \"The sample was decanted for Nano-XCT. During the mounting process the sample split into two along fractures (parts A and B)\" (p.7); resin embedding and polishing followed XCT (\"After nano-XCT analysis the sample was embedded in a Specifix resin\", p.7)",
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
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/labxctTAPP/effectiveSpatialResolution",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/effectiveSpatialResolution"
        }
      ],
      "schema:name": "Effective Spatial Resolution (PSF/MTF)",
      "schema:value": "N — the paper's \"spatial resolutions (in voxels)\" are the voxel sizes (0.625 / 0.672 µm); no effective (PSF/MTF) resolution reported"
    },
    {
      "@id": "ada:parameter/labxctTAPP/voiApplied",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/voiApplied"
        }
      ],
      "schema:name": "VOI Applied",
      "schema:value": "Full scan volume"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Cross-Validation Outcome",
      "dqv:value": "61 SSOs by polished SEM sections vs. 108 by XCT; discrepancy attributed to disruption by polishing; XCT detects more SSOs"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM (post-XCT polished sections)",
        "schema:description": "Serial polished sections cut post-XCT; SEM imaging"
      }
    }
  ],
  "ada:analyticalMode": [
    "Single-volume"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "A0180 (A0180-A and A0180-B)",
  "ada:samplingUnitName": "Labelled: scans \"A0180-A and A0180-B\" of Ryugu sample A0180 (p.7)"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XCT/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:labxctTAPP-detail-Genge2025",
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
              "@id": "ada:parameter/labxctTAPP/sampleDimensions",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/labxctTAPP/sampleDimensions"
                }
              ],
              "schema:name": "Sample Dimensions (L \u00d7 W \u00d7 H)",
              "schema:value": "1.592 \u00d7 0.756 \u00d7 0.985 mm"
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
              "schema:value": "Optical microscopy \u2014 morphological inspection of the sample exterior through the container window with the CLOXS digital optical microscope system on automated digital sample stages at JAXA/ISAS, before the sample was decanted for nano-XCT"
            }
          ],
          "schema:name": "A0180 (A0180-A and A0180-B)"
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/labxctTAPP/sampleMountingMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/sampleMountingMethod"
            }
          ],
          "schema:name": "Sample Mounting Method",
          "schema:value": "Mounted in pipette tips"
        },
        {
          "@id": "ada:parameter/labxctTAPP/rotationRange",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/rotationRange"
            }
          ],
          "schema:name": "Rotation Range",
          "schema:value": 360,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "360\u00b0"
        },
        {
          "@id": "ada:parameter/labxctTAPP/numberOfProjections",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/numberOfProjections"
            }
          ],
          "schema:name": "Number of Projections",
          "schema:value": 2401
        },
        {
          "@id": "ada:parameter/labxctTAPP/exposureTimePerProjection",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/exposureTimePerProjection"
            }
          ],
          "schema:name": "Exposure Time per Projection",
          "schema:value": 33,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "33 s (A0180-A); 28 s (A0180-B)"
        },
        {
          "@id": "ada:parameter/labxctTAPP/detectorBinning",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/detectorBinning"
            }
          ],
          "schema:name": "Detector Binning",
          "schema:value": "No binning"
        },
        {
          "@id": "ada:parameter/labxctTAPP/segmentationMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/segmentationMethod"
            }
          ],
          "schema:name": "Segmentation Method",
          "schema:value": "ImageJ threshold-based; TANGO plugin for 3D object detection"
        },
        {
          "@id": "ada:parameter/labxctTAPP/phaseIdentificationMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/phaseIdentificationMethod"
            }
          ],
          "schema:name": "Phase Identification Method",
          "schema:value": "Sulphide rims of SSOs identified by bright contrast; silicate glass by contrast relative to matrix"
        },
        {
          "@id": "ada:parameter/labxctTAPP/outputBitDepth",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/outputBitDepth"
            }
          ],
          "schema:name": "Output Bit Depth",
          "schema:value": "16-bit (CCD pixel depth)"
        },
        {
          "@id": "ada:parameter/labxctTAPP/partialVolumeEffectCriteria",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/partialVolumeEffectCriteria"
            }
          ],
          "schema:name": "Partial Volume Effect Criteria",
          "schema:value": "SSOs \u2265 5.4 \u00b5m identified (implicit: features \u2265 voxel size = 0.625 \u00b5m); sulphide rims \u2265 1 voxel required for detection"
        }
      ],
      "prov:used": [
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "ImageJ + TANGO plugin (Ollion et al. 2013)",
              "@type": [
                "schema:SoftwareApplication"
              ]
            }
          ]
        },
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "XCT",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/labxctTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 90,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "90 kV"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/tubeCurrent",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/tubeCurrent"
                    }
                  ],
                  "schema:name": "Tube Current",
                  "schema:value": 89,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "89 \u00b5A"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/xRayPreFilter",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/xRayPreFilter"
                    }
                  ],
                  "schema:name": "X-ray Pre-filter",
                  "schema:value": "Inbuilt LE4 filter (beam hardening reduction)"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/voxelSize",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/voxelSize"
                    }
                  ],
                  "schema:name": "Voxel Size",
                  "schema:value": 0.625,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "0.625 \u00b5m (A0180-A); 0.672 \u00b5m (A0180-B)"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:labxctTAPP-detail-Genge2025/instrument/XCT"
            }
          ]
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Not stated"
      },
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Bulk specimen or fragment \u2014 \"The sample was decanted for Nano-XCT. During the mounting process the sample split into two along fractures (parts A and B)\" (p.7); resin embedding and polishing followed XCT (\"After nano-XCT analysis the sample was embedded in a Specifix resin\", p.7)",
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
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/labxctTAPP/effectiveSpatialResolution",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/effectiveSpatialResolution"
        }
      ],
      "schema:name": "Effective Spatial Resolution (PSF/MTF)",
      "schema:value": "N \u2014 the paper's \"spatial resolutions (in voxels)\" are the voxel sizes (0.625 / 0.672 \u00b5m); no effective (PSF/MTF) resolution reported"
    },
    {
      "@id": "ada:parameter/labxctTAPP/voiApplied",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/voiApplied"
        }
      ],
      "schema:name": "VOI Applied",
      "schema:value": "Full scan volume"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Cross-Validation Outcome",
      "dqv:value": "61 SSOs by polished SEM sections vs. 108 by XCT; discrepancy attributed to disruption by polishing; XCT detects more SSOs"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM (post-XCT polished sections)",
        "schema:description": "Serial polished sections cut post-XCT; SEM imaging"
      }
    }
  ],
  "ada:analyticalMode": [
    "Single-volume"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "A0180 (A0180-A and A0180-B)",
  "ada:samplingUnitName": "Labelled: scans \"A0180-A and A0180-B\" of Ryugu sample A0180 (p.7)"
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

ex:labxctTAPP-detail-Genge2025 a schema1:Dataset,
        schema1:Product ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/voiApplied> ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "Serial polished sections cut post-XCT; SEM imaging" ;
                    schema1:name "SEM (post-XCT polished sections)" ] ] ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Cross-Validation Outcome" ;
            dqv:value "61 SSOs by polished SEM sections vs. 108 by XCT; discrepancy attributed to disruption by polishing; XCT detects more SSOs" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Bulk specimen or fragment — \"The sample was decanted for Nano-XCT. During the mounting process the sample split into two along fractures (parts A and B)\" (p.7); resin embedding and polishing followed XCT (\"After nano-XCT analysis the sample was embedded in a Specifix resin\", p.7)" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/detectorBinning>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/exposureTimePerProjection>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/numberOfProjections>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/outputBitDepth>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/partialVolumeEffectCriteria>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/phaseIdentificationMethod>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/rotationRange>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleMountingMethod>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationMethod> ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Not stated" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleDimensions>,
                        <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
                    schema1:name "A0180 (A0180-A and A0180-B)" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ bios:computationalTool [ a schema1:SoftwareApplication ;
                            schema1:name "ImageJ + TANGO plugin (Ollion et al. 2013)" ;
                            ada:toolRole "dataReduction" ] ],
                [ schema1:instrument <https://example.org/labxctTAPP-detail-Genge2025/instrument/XCT> ] ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalMode "Single-volume" ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:sampleName "A0180 (A0180-A and A0180-B)" ;
    ada:samplingUnitName "Labelled: scans \"A0180-A and A0180-B\" of Ryugu sample A0180 (p.7)" ;
    ada:sessionIdentifier "missing" .

<https://example.org/labxctTAPP-detail-Genge2025/instrument/XCT> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/tubeCurrent>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/voxelSize>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayPreFilter> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "XCT" ;
    schema1:name "no value available: schema:name" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:description "90 kV" ;
    schema1:name "Accelerating Voltage" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/acceleratingVoltage> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 90 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/detectorBinning> a schema1:PropertyValue ;
    schema1:name "Detector Binning" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/detectorBinning> ;
    schema1:value "No binning" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> a schema1:PropertyValue ;
    schema1:name "Effective Spatial Resolution (PSF/MTF)" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> ;
    schema1:value "N — the paper's \"spatial resolutions (in voxels)\" are the voxel sizes (0.625 / 0.672 µm); no effective (PSF/MTF) resolution reported" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/exposureTimePerProjection> a schema1:PropertyValue ;
    schema1:description "33 s (A0180-A); 28 s (A0180-B)" ;
    schema1:name "Exposure Time per Projection" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/exposureTimePerProjection> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 33 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/numberOfProjections> a schema1:PropertyValue ;
    schema1:name "Number of Projections" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/numberOfProjections> ;
    schema1:value 2401 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/outputBitDepth> a schema1:PropertyValue ;
    schema1:name "Output Bit Depth" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/outputBitDepth> ;
    schema1:value "16-bit (CCD pixel depth)" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/partialVolumeEffectCriteria> a schema1:PropertyValue ;
    schema1:name "Partial Volume Effect Criteria" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/partialVolumeEffectCriteria> ;
    schema1:value "SSOs ≥ 5.4 µm identified (implicit: features ≥ voxel size = 0.625 µm); sulphide rims ≥ 1 voxel required for detection" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/phaseIdentificationMethod> a schema1:PropertyValue ;
    schema1:name "Phase Identification Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/phaseIdentificationMethod> ;
    schema1:value "Sulphide rims of SSOs identified by bright contrast; silicate glass by contrast relative to matrix" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/rotationRange> a schema1:PropertyValue ;
    schema1:description "360°" ;
    schema1:name "Rotation Range" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/rotationRange> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 360 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleDimensions> a schema1:PropertyValue ;
    schema1:name "Sample Dimensions (L × W × H)" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleDimensions> ;
    schema1:value "1.592 × 0.756 × 0.985 mm" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleMountingMethod> a schema1:PropertyValue ;
    schema1:name "Sample Mounting Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleMountingMethod> ;
    schema1:value "Mounted in pipette tips" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationMethod> a schema1:PropertyValue ;
    schema1:name "Segmentation Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationMethod> ;
    schema1:value "ImageJ threshold-based; TANGO plugin for 3D object detection" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/tubeCurrent> a schema1:PropertyValue ;
    schema1:description "89 µA" ;
    schema1:name "Tube Current" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/tubeCurrent> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 89 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/voiApplied> a schema1:PropertyValue ;
    schema1:name "VOI Applied" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/voiApplied> ;
    schema1:value "Full scan volume" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/voxelSize> a schema1:PropertyValue ;
    schema1:description "0.625 µm (A0180-A); 0.672 µm (A0180-B)" ;
    schema1:name "Voxel Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/voxelSize> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 6.25e-01 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayPreFilter> a schema1:PropertyValue ;
    schema1:name "X-ray Pre-filter" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayPreFilter> ;
    schema1:value "Inbuilt LE4 filter (beam hardening reduction)" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "Optical microscopy — morphological inspection of the sample exterior through the container window with the CLOXS digital optical microscope system on automated digital sample stages at JAXA/ISAS, before the sample was decanted for nano-XCT" .


```


### detail example Neuman2025
detail instance derived from Neuman et al. 2025 / Shearer et al. 2024 (JGR / Space Sci. Rev.) Apollo 17 core 73002 Multi-volume stitching NSI custom, UTCT.
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
  "@id": "ex:labxctTAPP-detail-Neuman2025",
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
              "@id": "ada:parameter/labxctTAPP/sampleDimensions",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/labxctTAPP/sampleDimensions"
                }
              ],
              "schema:name": "Sample Dimensions (L × W × H)",
              "schema:value": "~35 cm length core"
            }
          ],
          "schema:name": "Apollo 17 core 73002"
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/labxctTAPP/sampleMountingMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/sampleMountingMethod"
            }
          ],
          "schema:name": "Sample Mounting Method",
          "schema:value": "Plexiglass tube (vertical); triple-sealed Teflon bag"
        },
        {
          "@id": "ada:parameter/labxctTAPP/rotationMode",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/rotationMode"
            }
          ],
          "schema:name": "Rotation Mode",
          "schema:value": "Continuous rotation (each Subpix sub-acquisition)"
        },
        {
          "@id": "ada:parameter/labxctTAPP/ringArtifactCorrectionMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/ringArtifactCorrectionMethod"
            }
          ],
          "schema:name": "Ring Artifact Correction Method",
          "schema:value": "Post-reconstruction ring corrections applied"
        }
      ],
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "XCT",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/labxctTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 180,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "180 kV"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/tubeCurrent",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/tubeCurrent"
                    }
                  ],
                  "schema:name": "Tube Current",
                  "schema:value": 0.18,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "0.18 mA (180 µA)"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/xRayPreFilter",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/xRayPreFilter"
                    }
                  ],
                  "schema:name": "X-ray Pre-filter",
                  "schema:value": "0.72 mm Al"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:labxctTAPP-detail-Neuman2025/instrument/XCT"
            }
          ]
        }
      ],
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Data processing",
            "schema:additionalProperty": [
              {
                "@id": "ada:parameter/labxctTAPP/subVolumeStitchingAndRegistrationMethod",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/labxctTAPP/subVolumeStitchingAndRegistrationMethod"
                  }
                ],
                "schema:name": "Sub-volume Stitching and Registration Method",
                "schema:value": "Digital stitching (method not named); post-reconstruction ring and distortion corrections applied"
              }
            ],
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Sample preparation",
            "schema:description": "Bulk specimen or fragment — drive tube scanned unopened: \"Prior to opening and processing, Apollo drive tubes 73001 and 73002 were transported to the UTCT Facility\" (Shearer et al. 2024, p.27); \"NASA curators removed the stainless-steel outer sleeve of 73002 and triple sealed the aluminum inner sleeve in teflon\" (Neuman et al. 2025, p.4)",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          }
        ]
      },
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "UTCT Facility, U. Texas"
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Ring Artifact Severity and Correction Outcome",
      "dqv:value": "Post-reconstruction ring corrections applied; severity not documented"
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/labxctTAPP/numberOfSubVolumes",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/numberOfSubVolumes"
        }
      ],
      "schema:name": "Number of Sub-volumes",
      "schema:value": 6,
      "schema:description": "6 volumes"
    },
    {
      "@id": "ada:parameter/labxctTAPP/voiApplied",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/voiApplied"
        }
      ],
      "schema:name": "VOI Applied",
      "schema:value": "Full core length per sub-volume"
    },
    {
      "@id": "ada:parameter/labxctTAPP/subVolumeOverlap",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/subVolumeOverlap"
        }
      ],
      "schema:name": "Sub-volume Overlap",
      "schema:value": 380,
      "schema:description": "~380 slices per sub-volume overlap"
    }
  ],
  "ada:analyticalMode": [
    "Multi-volume stitching"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Apollo 17 core 73002",
  "ada:samplingUnitName": "Sample name only — core 73002, \"A series of six volumes was acquired\" and stitched \"to create a continuous data set for each core\" (Neuman et al. 2025, p.4); the volumes are counted, not labelled"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XCT/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:labxctTAPP-detail-Neuman2025",
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
              "@id": "ada:parameter/labxctTAPP/sampleDimensions",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/labxctTAPP/sampleDimensions"
                }
              ],
              "schema:name": "Sample Dimensions (L \u00d7 W \u00d7 H)",
              "schema:value": "~35 cm length core"
            }
          ],
          "schema:name": "Apollo 17 core 73002"
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/labxctTAPP/sampleMountingMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/sampleMountingMethod"
            }
          ],
          "schema:name": "Sample Mounting Method",
          "schema:value": "Plexiglass tube (vertical); triple-sealed Teflon bag"
        },
        {
          "@id": "ada:parameter/labxctTAPP/rotationMode",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/rotationMode"
            }
          ],
          "schema:name": "Rotation Mode",
          "schema:value": "Continuous rotation (each Subpix sub-acquisition)"
        },
        {
          "@id": "ada:parameter/labxctTAPP/ringArtifactCorrectionMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/ringArtifactCorrectionMethod"
            }
          ],
          "schema:name": "Ring Artifact Correction Method",
          "schema:value": "Post-reconstruction ring corrections applied"
        }
      ],
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "XCT",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/labxctTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 180,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "180 kV"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/tubeCurrent",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/tubeCurrent"
                    }
                  ],
                  "schema:name": "Tube Current",
                  "schema:value": 0.18,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "0.18 mA (180 \u00b5A)"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/xRayPreFilter",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/xRayPreFilter"
                    }
                  ],
                  "schema:name": "X-ray Pre-filter",
                  "schema:value": "0.72 mm Al"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:labxctTAPP-detail-Neuman2025/instrument/XCT"
            }
          ]
        }
      ],
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Data processing",
            "schema:additionalProperty": [
              {
                "@id": "ada:parameter/labxctTAPP/subVolumeStitchingAndRegistrationMethod",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/labxctTAPP/subVolumeStitchingAndRegistrationMethod"
                  }
                ],
                "schema:name": "Sub-volume Stitching and Registration Method",
                "schema:value": "Digital stitching (method not named); post-reconstruction ring and distortion corrections applied"
              }
            ],
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Sample preparation",
            "schema:description": "Bulk specimen or fragment \u2014 drive tube scanned unopened: \"Prior to opening and processing, Apollo drive tubes 73001 and 73002 were transported to the UTCT Facility\" (Shearer et al. 2024, p.27); \"NASA curators removed the stainless-steel outer sleeve of 73002 and triple sealed the aluminum inner sleeve in teflon\" (Neuman et al. 2025, p.4)",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          }
        ]
      },
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "UTCT Facility, U. Texas"
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Ring Artifact Severity and Correction Outcome",
      "dqv:value": "Post-reconstruction ring corrections applied; severity not documented"
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/labxctTAPP/numberOfSubVolumes",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/numberOfSubVolumes"
        }
      ],
      "schema:name": "Number of Sub-volumes",
      "schema:value": 6,
      "schema:description": "6 volumes"
    },
    {
      "@id": "ada:parameter/labxctTAPP/voiApplied",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/voiApplied"
        }
      ],
      "schema:name": "VOI Applied",
      "schema:value": "Full core length per sub-volume"
    },
    {
      "@id": "ada:parameter/labxctTAPP/subVolumeOverlap",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/subVolumeOverlap"
        }
      ],
      "schema:name": "Sub-volume Overlap",
      "schema:value": 380,
      "schema:description": "~380 slices per sub-volume overlap"
    }
  ],
  "ada:analyticalMode": [
    "Multi-volume stitching"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Apollo 17 core 73002",
  "ada:samplingUnitName": "Sample name only \u2014 core 73002, \"A series of six volumes was acquired\" and stitched \"to create a continuous data set for each core\" (Neuman et al. 2025, p.4); the volumes are counted, not labelled"
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

ex:labxctTAPP-detail-Neuman2025 a schema1:Dataset,
        schema1:Product ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/numberOfSubVolumes>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/subVolumeOverlap>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/voiApplied> ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Ring Artifact Severity and Correction Outcome" ;
            dqv:value "Post-reconstruction ring corrections applied; severity not documented" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Bulk specimen or fragment — drive tube scanned unopened: \"Prior to opening and processing, Apollo drive tubes 73001 and 73002 were transported to the UTCT Facility\" (Shearer et al. 2024, p.27); \"NASA curators removed the stainless-steel outer sleeve of 73002 and triple sealed the aluminum inner sleeve in teflon\" (Neuman et al. 2025, p.4)" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 2 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/subVolumeStitchingAndRegistrationMethod> ;
                            schema1:name "Data processing" ;
                            schema1:position 1 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/ringArtifactCorrectionMethod>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/rotationMode>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleMountingMethod> ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "UTCT Facility, U. Texas" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleDimensions> ;
                    schema1:name "Apollo 17 core 73002" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ schema1:instrument <https://example.org/labxctTAPP-detail-Neuman2025/instrument/XCT> ] ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalMode "Multi-volume stitching" ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:sampleName "Apollo 17 core 73002" ;
    ada:samplingUnitName "Sample name only — core 73002, \"A series of six volumes was acquired\" and stitched \"to create a continuous data set for each core\" (Neuman et al. 2025, p.4); the volumes are counted, not labelled" ;
    ada:sessionIdentifier "missing" .

<https://example.org/labxctTAPP-detail-Neuman2025/instrument/XCT> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/tubeCurrent>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayPreFilter> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "XCT" ;
    schema1:name "no value available: schema:name" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:description "180 kV" ;
    schema1:name "Accelerating Voltage" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/acceleratingVoltage> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 180 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/numberOfSubVolumes> a schema1:PropertyValue ;
    schema1:description "6 volumes" ;
    schema1:name "Number of Sub-volumes" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/numberOfSubVolumes> ;
    schema1:value 6 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/ringArtifactCorrectionMethod> a schema1:PropertyValue ;
    schema1:name "Ring Artifact Correction Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/ringArtifactCorrectionMethod> ;
    schema1:value "Post-reconstruction ring corrections applied" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/rotationMode> a schema1:PropertyValue ;
    schema1:name "Rotation Mode" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/rotationMode> ;
    schema1:value "Continuous rotation (each Subpix sub-acquisition)" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleDimensions> a schema1:PropertyValue ;
    schema1:name "Sample Dimensions (L × W × H)" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleDimensions> ;
    schema1:value "~35 cm length core" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleMountingMethod> a schema1:PropertyValue ;
    schema1:name "Sample Mounting Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleMountingMethod> ;
    schema1:value "Plexiglass tube (vertical); triple-sealed Teflon bag" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/subVolumeOverlap> a schema1:PropertyValue ;
    schema1:description "~380 slices per sub-volume overlap" ;
    schema1:name "Sub-volume Overlap" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/subVolumeOverlap> ;
    schema1:value 380 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/subVolumeStitchingAndRegistrationMethod> a schema1:PropertyValue ;
    schema1:name "Sub-volume Stitching and Registration Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/subVolumeStitchingAndRegistrationMethod> ;
    schema1:value "Digital stitching (method not named); post-reconstruction ring and distortion corrections applied" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/tubeCurrent> a schema1:PropertyValue ;
    schema1:description "0.18 mA (180 µA)" ;
    schema1:name "Tube Current" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/tubeCurrent> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1.8e-01 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/voiApplied> a schema1:PropertyValue ;
    schema1:name "VOI Applied" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/voiApplied> ;
    schema1:value "Full core length per sub-volume" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayPreFilter> a schema1:PropertyValue ;
    schema1:name "X-ray Pre-filter" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayPreFilter> ;
    schema1:value "0.72 mm Al" .


```


### detail example Neuman2025-2
detail instance derived from Neuman et al. 2025 (JGR Planets) Apollo 17 core 73001 Multi-volume stitching NSI custom, UTCT.
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
  "@id": "ex:labxctTAPP-detail-Neuman2025-2",
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
              "@id": "ada:parameter/labxctTAPP/sampleDimensions",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/labxctTAPP/sampleDimensions"
                }
              ],
              "schema:name": "Sample Dimensions (L × W × H)",
              "schema:value": "~35 cm length core"
            }
          ],
          "schema:name": "Apollo 17 core 73001"
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/labxctTAPP/sampleMountingMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/sampleMountingMethod"
            }
          ],
          "schema:name": "Sample Mounting Method",
          "schema:value": "Custom PVC tube; core left in its stainless-steel outer sleeve — \"It was thus decided to leave the core in its stainless steel outer sleeve for scanning. The core was positioned for scanning in a custom PVC tube mount\" (Neuman et al. 2025, pp.4–5)"
        },
        {
          "@id": "ada:parameter/labxctTAPP/rotationMode",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/rotationMode"
            }
          ],
          "schema:name": "Rotation Mode",
          "schema:value": "Non-continuous rotation (to avoid rotational mismatch of continuous mode)"
        },
        {
          "@id": "ada:parameter/labxctTAPP/ringArtifactCorrectionMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/ringArtifactCorrectionMethod"
            }
          ],
          "schema:name": "Ring Artifact Correction Method",
          "schema:value": "Post-reconstruction ring corrections applied"
        }
      ],
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "XCT",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/labxctTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 190,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "190 kV"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/xRayPreFilter",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/xRayPreFilter"
                    }
                  ],
                  "schema:name": "X-ray Pre-filter",
                  "schema:value": "None (steel sleeve acts as effective filter)"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:labxctTAPP-detail-Neuman2025-2/instrument/XCT"
            }
          ]
        }
      ],
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Data processing",
            "schema:additionalProperty": [
              {
                "@id": "ada:parameter/labxctTAPP/subVolumeStitchingAndRegistrationMethod",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/labxctTAPP/subVolumeStitchingAndRegistrationMethod"
                  }
                ],
                "schema:name": "Sub-volume Stitching and Registration Method",
                "schema:value": "Digital stitching; manual realignment of raw projection images for rotational misalignment (up to 0.35°); additional cone-beam, BH, and scattering corrections applied"
              }
            ],
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Sample preparation",
            "schema:description": "Bulk specimen or fragment — drive tube scanned unopened; \"It was thus decided to leave the core in its stainless steel outer sleeve for scanning\" (pp.4–5)",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          }
        ]
      },
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "UTCT Facility, U. Texas"
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Beam Hardening Artifact Assessment",
      "dqv:value": "BH artifact from steel sleeve: uneven brightness and scattering; asymmetric + symmetric corrections applied"
    },
    {
      "dqv:isMeasurementOf": "Ring Artifact Severity and Correction Outcome",
      "dqv:value": "Post-reconstruction ring corrections applied; severity not documented"
    },
    {
      "dqv:isMeasurementOf": "Metal Streak Artifact Assessment",
      "dqv:value": "Steel outer sleeve caused secondary BH and scattering artifact resulting in uneven brightness; corrected with asymmetric + symmetric corrections"
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/labxctTAPP/numberOfSubVolumes",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/numberOfSubVolumes"
        }
      ],
      "schema:name": "Number of Sub-volumes",
      "schema:value": 9,
      "schema:description": "9 volumes"
    },
    {
      "@id": "ada:parameter/labxctTAPP/voiApplied",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/voiApplied"
        }
      ],
      "schema:name": "VOI Applied",
      "schema:value": "Full core length per sub-volume"
    }
  ],
  "ada:analyticalMode": [
    "Multi-volume stitching"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Apollo 17 core 73001",
  "ada:samplingUnitName": "Sample name only — core 73001, \"A series of nine scan volumes was acquired along the length of the core\" (p.5); the volumes are counted, not labelled"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XCT/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:labxctTAPP-detail-Neuman2025-2",
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
              "@id": "ada:parameter/labxctTAPP/sampleDimensions",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/labxctTAPP/sampleDimensions"
                }
              ],
              "schema:name": "Sample Dimensions (L \u00d7 W \u00d7 H)",
              "schema:value": "~35 cm length core"
            }
          ],
          "schema:name": "Apollo 17 core 73001"
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/labxctTAPP/sampleMountingMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/sampleMountingMethod"
            }
          ],
          "schema:name": "Sample Mounting Method",
          "schema:value": "Custom PVC tube; core left in its stainless-steel outer sleeve \u2014 \"It was thus decided to leave the core in its stainless steel outer sleeve for scanning. The core was positioned for scanning in a custom PVC tube mount\" (Neuman et al. 2025, pp.4\u20135)"
        },
        {
          "@id": "ada:parameter/labxctTAPP/rotationMode",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/rotationMode"
            }
          ],
          "schema:name": "Rotation Mode",
          "schema:value": "Non-continuous rotation (to avoid rotational mismatch of continuous mode)"
        },
        {
          "@id": "ada:parameter/labxctTAPP/ringArtifactCorrectionMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/ringArtifactCorrectionMethod"
            }
          ],
          "schema:name": "Ring Artifact Correction Method",
          "schema:value": "Post-reconstruction ring corrections applied"
        }
      ],
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "XCT",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/labxctTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 190,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "190 kV"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/xRayPreFilter",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/xRayPreFilter"
                    }
                  ],
                  "schema:name": "X-ray Pre-filter",
                  "schema:value": "None (steel sleeve acts as effective filter)"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:labxctTAPP-detail-Neuman2025-2/instrument/XCT"
            }
          ]
        }
      ],
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Data processing",
            "schema:additionalProperty": [
              {
                "@id": "ada:parameter/labxctTAPP/subVolumeStitchingAndRegistrationMethod",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/labxctTAPP/subVolumeStitchingAndRegistrationMethod"
                  }
                ],
                "schema:name": "Sub-volume Stitching and Registration Method",
                "schema:value": "Digital stitching; manual realignment of raw projection images for rotational misalignment (up to 0.35\u00b0); additional cone-beam, BH, and scattering corrections applied"
              }
            ],
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Sample preparation",
            "schema:description": "Bulk specimen or fragment \u2014 drive tube scanned unopened; \"It was thus decided to leave the core in its stainless steel outer sleeve for scanning\" (pp.4\u20135)",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          }
        ]
      },
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "UTCT Facility, U. Texas"
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Beam Hardening Artifact Assessment",
      "dqv:value": "BH artifact from steel sleeve: uneven brightness and scattering; asymmetric + symmetric corrections applied"
    },
    {
      "dqv:isMeasurementOf": "Ring Artifact Severity and Correction Outcome",
      "dqv:value": "Post-reconstruction ring corrections applied; severity not documented"
    },
    {
      "dqv:isMeasurementOf": "Metal Streak Artifact Assessment",
      "dqv:value": "Steel outer sleeve caused secondary BH and scattering artifact resulting in uneven brightness; corrected with asymmetric + symmetric corrections"
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/labxctTAPP/numberOfSubVolumes",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/numberOfSubVolumes"
        }
      ],
      "schema:name": "Number of Sub-volumes",
      "schema:value": 9,
      "schema:description": "9 volumes"
    },
    {
      "@id": "ada:parameter/labxctTAPP/voiApplied",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/voiApplied"
        }
      ],
      "schema:name": "VOI Applied",
      "schema:value": "Full core length per sub-volume"
    }
  ],
  "ada:analyticalMode": [
    "Multi-volume stitching"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Apollo 17 core 73001",
  "ada:samplingUnitName": "Sample name only \u2014 core 73001, \"A series of nine scan volumes was acquired along the length of the core\" (p.5); the volumes are counted, not labelled"
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

ex:labxctTAPP-detail-Neuman2025-2 a schema1:Dataset,
        schema1:Product ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/numberOfSubVolumes>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/voiApplied> ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Metal Streak Artifact Assessment" ;
            dqv:value "Steel outer sleeve caused secondary BH and scattering artifact resulting in uneven brightness; corrected with asymmetric + symmetric corrections" ],
        [ dqv:isMeasurementOf "Ring Artifact Severity and Correction Outcome" ;
            dqv:value "Post-reconstruction ring corrections applied; severity not documented" ],
        [ dqv:isMeasurementOf "Beam Hardening Artifact Assessment" ;
            dqv:value "BH artifact from steel sleeve: uneven brightness and scattering; asymmetric + symmetric corrections applied" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Bulk specimen or fragment — drive tube scanned unopened; \"It was thus decided to leave the core in its stainless steel outer sleeve for scanning\" (pp.4–5)" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 2 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/subVolumeStitchingAndRegistrationMethod> ;
                            schema1:name "Data processing" ;
                            schema1:position 1 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/ringArtifactCorrectionMethod>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/rotationMode>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleMountingMethod> ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "UTCT Facility, U. Texas" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleDimensions> ;
                    schema1:name "Apollo 17 core 73001" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ schema1:instrument <https://example.org/labxctTAPP-detail-Neuman2025-2/instrument/XCT> ] ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalMode "Multi-volume stitching" ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:sampleName "Apollo 17 core 73001" ;
    ada:samplingUnitName "Sample name only — core 73001, \"A series of nine scan volumes was acquired along the length of the core\" (p.5); the volumes are counted, not labelled" ;
    ada:sessionIdentifier "missing" .

<https://example.org/labxctTAPP-detail-Neuman2025-2/instrument/XCT> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayPreFilter> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "XCT" ;
    schema1:name "no value available: schema:name" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:description "190 kV" ;
    schema1:name "Accelerating Voltage" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/acceleratingVoltage> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 190 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/numberOfSubVolumes> a schema1:PropertyValue ;
    schema1:description "9 volumes" ;
    schema1:name "Number of Sub-volumes" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/numberOfSubVolumes> ;
    schema1:value 9 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/ringArtifactCorrectionMethod> a schema1:PropertyValue ;
    schema1:name "Ring Artifact Correction Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/ringArtifactCorrectionMethod> ;
    schema1:value "Post-reconstruction ring corrections applied" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/rotationMode> a schema1:PropertyValue ;
    schema1:name "Rotation Mode" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/rotationMode> ;
    schema1:value "Non-continuous rotation (to avoid rotational mismatch of continuous mode)" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleDimensions> a schema1:PropertyValue ;
    schema1:name "Sample Dimensions (L × W × H)" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleDimensions> ;
    schema1:value "~35 cm length core" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleMountingMethod> a schema1:PropertyValue ;
    schema1:name "Sample Mounting Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleMountingMethod> ;
    schema1:value "Custom PVC tube; core left in its stainless-steel outer sleeve — \"It was thus decided to leave the core in its stainless steel outer sleeve for scanning. The core was positioned for scanning in a custom PVC tube mount\" (Neuman et al. 2025, pp.4–5)" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/subVolumeStitchingAndRegistrationMethod> a schema1:PropertyValue ;
    schema1:name "Sub-volume Stitching and Registration Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/subVolumeStitchingAndRegistrationMethod> ;
    schema1:value "Digital stitching; manual realignment of raw projection images for rotational misalignment (up to 0.35°); additional cone-beam, BH, and scattering corrections applied" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/voiApplied> a schema1:PropertyValue ;
    schema1:name "VOI Applied" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/voiApplied> ;
    schema1:value "Full core length per sub-volume" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayPreFilter> a schema1:PropertyValue ;
    schema1:name "X-ray Pre-filter" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayPreFilter> ;
    schema1:value "None (steel sleeve acts as effective filter)" .


```


### detail example Shearer2024
detail instance derived from Shearer et al. 2024 (Space Sci. Rev.) Apollo 17 73001 CSVC Single-volume Nikon XTH 320 NASA JSC.
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
  "@id": "ex:labxctTAPP-detail-Shearer2024",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/labxctTAPP/sampleMountingMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/sampleMountingMethod"
            }
          ],
          "schema:name": "Sample Mounting Method",
          "schema:value": "Sealed container (the unopened 73001 CSVC); stage holder N — \"Before piercing and gas extraction of the 73001 CSVC, an XCT scan of the bottom portion was collected\" (p.26); Fig. 7 shows the core \"still within the CSVC\" (p.27)"
        }
      ],
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "XCT",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/labxctTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 215,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "215 kV"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/tubeCurrent",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/tubeCurrent"
                    }
                  ],
                  "schema:name": "Tube Current",
                  "schema:value": 179,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "179 mA (possibly typo for µA per source)"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/voxelSize",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/voxelSize"
                    }
                  ],
                  "schema:name": "Voxel Size",
                  "schema:value": 38.49,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "38.49 µm voxel edge"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:labxctTAPP-detail-Shearer2024/instrument/XCT"
            }
          ]
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "NASA JSC Astromaterials X-FaCT Lab"
      },
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:name": "73001 CSVC"
        }
      ],
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Bulk specimen or fragment — core scanned inside the unopened 73001 CSVC: \"Before piercing and gas extraction of the 73001 CSVC, an XCT scan of the bottom portion was collected\" (p.26); Fig. 7 shows the core \"still within the CSVC\" (p.27)",
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
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/labxctTAPP/effectiveSpatialResolution",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/effectiveSpatialResolution"
        }
      ],
      "schema:name": "Effective Spatial Resolution (PSF/MTF)",
      "schema:value": "N — voxel size only (38.49 µm); no effective resolution reported. The paper's \"spatial resolution of 60 µm\" is the multispectral core imager, not this XCT scan"
    }
  ],
  "ada:analyticalMode": [
    "Single-volume"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleDimensions": "missing",
  "ada:sampleName": "73001 CSVC",
  "ada:samplingUnitName": "Sample name only — the 73001 CSVC; scans are identified by position and stage (\"the bottom portion of 73001 still within the CSVC before (b) and after (c) piercing\", \"the top portion\", Fig. 7, p.27), not labelled",
  "ada:voiApplied": "missing"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XCT/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:labxctTAPP-detail-Shearer2024",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/labxctTAPP/sampleMountingMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/sampleMountingMethod"
            }
          ],
          "schema:name": "Sample Mounting Method",
          "schema:value": "Sealed container (the unopened 73001 CSVC); stage holder N \u2014 \"Before piercing and gas extraction of the 73001 CSVC, an XCT scan of the bottom portion was collected\" (p.26); Fig. 7 shows the core \"still within the CSVC\" (p.27)"
        }
      ],
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "XCT",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/labxctTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 215,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "215 kV"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/tubeCurrent",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/tubeCurrent"
                    }
                  ],
                  "schema:name": "Tube Current",
                  "schema:value": 179,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "179 mA (possibly typo for \u00b5A per source)"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/voxelSize",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/voxelSize"
                    }
                  ],
                  "schema:name": "Voxel Size",
                  "schema:value": 38.49,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "38.49 \u00b5m voxel edge"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:labxctTAPP-detail-Shearer2024/instrument/XCT"
            }
          ]
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "NASA JSC Astromaterials X-FaCT Lab"
      },
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:name": "73001 CSVC"
        }
      ],
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Bulk specimen or fragment \u2014 core scanned inside the unopened 73001 CSVC: \"Before piercing and gas extraction of the 73001 CSVC, an XCT scan of the bottom portion was collected\" (p.26); Fig. 7 shows the core \"still within the CSVC\" (p.27)",
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
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/labxctTAPP/effectiveSpatialResolution",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/effectiveSpatialResolution"
        }
      ],
      "schema:name": "Effective Spatial Resolution (PSF/MTF)",
      "schema:value": "N \u2014 voxel size only (38.49 \u00b5m); no effective resolution reported. The paper's \"spatial resolution of 60 \u00b5m\" is the multispectral core imager, not this XCT scan"
    }
  ],
  "ada:analyticalMode": [
    "Single-volume"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleDimensions": "missing",
  "ada:sampleName": "73001 CSVC",
  "ada:samplingUnitName": "Sample name only \u2014 the 73001 CSVC; scans are identified by position and stage (\"the bottom portion of 73001 still within the CSVC before (b) and after (c) piercing\", \"the top portion\", Fig. 7, p.27), not labelled",
  "ada:voiApplied": "missing"
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

ex:labxctTAPP-detail-Shearer2024 a schema1:Dataset,
        schema1:Product ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Bulk specimen or fragment — core scanned inside the unopened 73001 CSVC: \"Before piercing and gas extraction of the 73001 CSVC, an XCT scan of the bottom portion was collected\" (p.26); Fig. 7 shows the core \"still within the CSVC\" (p.27)" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleMountingMethod> ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "NASA JSC Astromaterials X-FaCT Lab" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:name "73001 CSVC" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ schema1:instrument <https://example.org/labxctTAPP-detail-Shearer2024/instrument/XCT> ] ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalMode "Single-volume" ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:sampleDimensions "missing" ;
    ada:sampleName "73001 CSVC" ;
    ada:samplingUnitName "Sample name only — the 73001 CSVC; scans are identified by position and stage (\"the bottom portion of 73001 still within the CSVC before (b) and after (c) piercing\", \"the top portion\", Fig. 7, p.27), not labelled" ;
    ada:sessionIdentifier "missing" ;
    ada:voiApplied "missing" .

<https://example.org/labxctTAPP-detail-Shearer2024/instrument/XCT> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/tubeCurrent>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/voxelSize> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "XCT" ;
    schema1:name "no value available: schema:name" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:description "215 kV" ;
    schema1:name "Accelerating Voltage" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/acceleratingVoltage> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 215 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> a schema1:PropertyValue ;
    schema1:name "Effective Spatial Resolution (PSF/MTF)" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> ;
    schema1:value "N — voxel size only (38.49 µm); no effective resolution reported. The paper's \"spatial resolution of 60 µm\" is the multispectral core imager, not this XCT scan" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleMountingMethod> a schema1:PropertyValue ;
    schema1:name "Sample Mounting Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleMountingMethod> ;
    schema1:value "Sealed container (the unopened 73001 CSVC); stage holder N — \"Before piercing and gas extraction of the 73001 CSVC, an XCT scan of the bottom portion was collected\" (p.26); Fig. 7 shows the core \"still within the CSVC\" (p.27)" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/tubeCurrent> a schema1:PropertyValue ;
    schema1:description "179 mA (possibly typo for µA per source)" ;
    schema1:name "Tube Current" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/tubeCurrent> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 179 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/voxelSize> a schema1:PropertyValue ;
    schema1:description "38.49 µm voxel edge" ;
    schema1:name "Voxel Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/voxelSize> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 3.849e+01 .


```


### detail example Shearer2024-2
detail instance derived from Shearer et al. 2024 (Space Sci. Rev.) Apollo 17 particles Single-volume Nikon XTH 320 NASA JSC X-FaCT.
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
  "@id": "ex:labxctTAPP-detail-Shearer2024-2",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/labxctTAPP/sampleMountingMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/sampleMountingMethod"
            }
          ],
          "schema:name": "Sample Mounting Method",
          "schema:value": "Triple-bagged in Teflon, wrapped in cylinder, placed in 1-cm plastic straw"
        },
        {
          "@id": "ada:parameter/labxctTAPP/xRayPower",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/xRayPower"
            }
          ],
          "schema:name": "X-ray Power",
          "schema:value": 3.0,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "3.0 W"
        }
      ],
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "XCT",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/labxctTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 90,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "90 kV (typical; optimized per sample)"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/xRayPreFilter",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/xRayPreFilter"
                    }
                  ],
                  "schema:name": "X-ray Pre-filter",
                  "schema:value": "0.1–0.25 mm Al (Bennu PE protocol range stated)"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/voxelSize",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/voxelSize"
                    }
                  ],
                  "schema:name": "Voxel Size",
                  "schema:value": 2.8,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "2.8–20.6 µm (optimized per sample)"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:labxctTAPP-detail-Shearer2024-2/instrument/XCT"
            }
          ]
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "NASA JSC Astromaterials X-FaCT Lab"
      },
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:name": "Multiple particles from 73001 and 73002"
        }
      ],
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Bulk specimen or fragment (as received) — extracted particles >4 mm \"are individually bagged and XCT scanned for classification and characterization without destructive chipping, sectioning, or dust removal\" (p.26)",
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
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/labxctTAPP/effectiveSpatialResolution",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/effectiveSpatialResolution"
        }
      ],
      "schema:name": "Effective Spatial Resolution (PSF/MTF)",
      "schema:value": "N — voxel size only (2.8–20.6 µm); no effective resolution reported. The paper's \"spatial resolution of 60 µm\" is the multispectral core imager, not this XCT scan"
    }
  ],
  "ada:analyticalMode": [
    "Single-volume"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleDimensions": "missing",
  "ada:sampleName": "Multiple particles from 73001 and 73002",
  "ada:samplingUnitName": "Sample name only — \"132 particles were scanned from 73002 ... and 220 particles from 73001\" (p.28), each \"individually bagged\"; the particles are counted and shown by lithology (Fig. 8, p.28), not labelled",
  "ada:voiApplied": "missing"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XCT/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:labxctTAPP-detail-Shearer2024-2",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/labxctTAPP/sampleMountingMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/sampleMountingMethod"
            }
          ],
          "schema:name": "Sample Mounting Method",
          "schema:value": "Triple-bagged in Teflon, wrapped in cylinder, placed in 1-cm plastic straw"
        },
        {
          "@id": "ada:parameter/labxctTAPP/xRayPower",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/xRayPower"
            }
          ],
          "schema:name": "X-ray Power",
          "schema:value": 3.0,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "3.0 W"
        }
      ],
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "XCT",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/labxctTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 90,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "90 kV (typical; optimized per sample)"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/xRayPreFilter",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/xRayPreFilter"
                    }
                  ],
                  "schema:name": "X-ray Pre-filter",
                  "schema:value": "0.1\u20130.25 mm Al (Bennu PE protocol range stated)"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/voxelSize",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/voxelSize"
                    }
                  ],
                  "schema:name": "Voxel Size",
                  "schema:value": 2.8,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "2.8\u201320.6 \u00b5m (optimized per sample)"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:labxctTAPP-detail-Shearer2024-2/instrument/XCT"
            }
          ]
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "NASA JSC Astromaterials X-FaCT Lab"
      },
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:name": "Multiple particles from 73001 and 73002"
        }
      ],
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Bulk specimen or fragment (as received) \u2014 extracted particles >4 mm \"are individually bagged and XCT scanned for classification and characterization without destructive chipping, sectioning, or dust removal\" (p.26)",
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
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/labxctTAPP/effectiveSpatialResolution",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/effectiveSpatialResolution"
        }
      ],
      "schema:name": "Effective Spatial Resolution (PSF/MTF)",
      "schema:value": "N \u2014 voxel size only (2.8\u201320.6 \u00b5m); no effective resolution reported. The paper's \"spatial resolution of 60 \u00b5m\" is the multispectral core imager, not this XCT scan"
    }
  ],
  "ada:analyticalMode": [
    "Single-volume"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleDimensions": "missing",
  "ada:sampleName": "Multiple particles from 73001 and 73002",
  "ada:samplingUnitName": "Sample name only \u2014 \"132 particles were scanned from 73002 ... and 220 particles from 73001\" (p.28), each \"individually bagged\"; the particles are counted and shown by lithology (Fig. 8, p.28), not labelled",
  "ada:voiApplied": "missing"
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

ex:labxctTAPP-detail-Shearer2024-2 a schema1:Dataset,
        schema1:Product ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Bulk specimen or fragment (as received) — extracted particles >4 mm \"are individually bagged and XCT scanned for classification and characterization without destructive chipping, sectioning, or dust removal\" (p.26)" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleMountingMethod>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayPower> ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "NASA JSC Astromaterials X-FaCT Lab" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:name "Multiple particles from 73001 and 73002" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ schema1:instrument <https://example.org/labxctTAPP-detail-Shearer2024-2/instrument/XCT> ] ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalMode "Single-volume" ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:sampleDimensions "missing" ;
    ada:sampleName "Multiple particles from 73001 and 73002" ;
    ada:samplingUnitName "Sample name only — \"132 particles were scanned from 73002 ... and 220 particles from 73001\" (p.28), each \"individually bagged\"; the particles are counted and shown by lithology (Fig. 8, p.28), not labelled" ;
    ada:sessionIdentifier "missing" ;
    ada:voiApplied "missing" .

<https://example.org/labxctTAPP-detail-Shearer2024-2/instrument/XCT> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/voxelSize>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayPreFilter> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "XCT" ;
    schema1:name "no value available: schema:name" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:description "90 kV (typical; optimized per sample)" ;
    schema1:name "Accelerating Voltage" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/acceleratingVoltage> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 90 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> a schema1:PropertyValue ;
    schema1:name "Effective Spatial Resolution (PSF/MTF)" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> ;
    schema1:value "N — voxel size only (2.8–20.6 µm); no effective resolution reported. The paper's \"spatial resolution of 60 µm\" is the multispectral core imager, not this XCT scan" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleMountingMethod> a schema1:PropertyValue ;
    schema1:name "Sample Mounting Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleMountingMethod> ;
    schema1:value "Triple-bagged in Teflon, wrapped in cylinder, placed in 1-cm plastic straw" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/voxelSize> a schema1:PropertyValue ;
    schema1:description "2.8–20.6 µm (optimized per sample)" ;
    schema1:name "Voxel Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/voxelSize> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 2.8e+00 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayPower> a schema1:PropertyValue ;
    schema1:description "3.0 W" ;
    schema1:name "X-ray Power" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayPower> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 3e+00 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayPreFilter> a schema1:PropertyValue ;
    schema1:name "X-ray Pre-filter" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayPreFilter> ;
    schema1:value "0.1–0.25 mm Al (Bennu PE protocol range stated)" .


```


### detail example Tomkinson2015
detail instance derived from Tomkinson et al. 2015 (MAPS) NWA 5790 nakhlite Single-volume Nikon Metris XTH 225 U. Manchester.
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
  "@id": "ex:labxctTAPP-detail-Tomkinson2015",
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
              "@id": "ada:parameter/labxctTAPP/sampleDimensions",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/labxctTAPP/sampleDimensions"
                }
              ],
              "schema:name": "Sample Dimensions (L × W × H)",
              "schema:value": "~1.1 × 1.2 × 0.8 cm"
            },
            {
              "@id": "ada:parameter/labxctTAPP/sampleMass",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/labxctTAPP/sampleMass"
                }
              ],
              "schema:name": "Sample Mass",
              "schema:value": 2.7,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "2.7 g"
            }
          ],
          "schema:name": "NWA 5790"
        }
      ],
      "prov:used": [
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "Avizo™",
              "@type": [
                "schema:SoftwareApplication"
              ]
            }
          ]
        },
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "XCT",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/labxctTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 120,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "120 keV (reported in paper as 'accelerating voltage of 120 keV'; likely typo for 120 kV)"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/voxelSize",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/voxelSize"
                    }
                  ],
                  "schema:name": "Voxel Size",
                  "schema:value": 10.3,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "10.3 × 10.3 × 10.3 µm³"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:labxctTAPP-detail-Tomkinson2015/instrument/XCT"
            }
          ]
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/labxctTAPP/numberOfProjections",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/numberOfProjections"
            }
          ],
          "schema:name": "Number of Projections",
          "schema:value": 3143
        },
        {
          "@id": "ada:parameter/labxctTAPP/exposureTimePerProjection",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/exposureTimePerProjection"
            }
          ],
          "schema:name": "Exposure Time per Projection",
          "schema:value": 20,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "20 s"
        },
        {
          "@id": "ada:parameter/labxctTAPP/segmentationMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/segmentationMethod"
            }
          ],
          "schema:name": "Segmentation Method",
          "schema:value": "Manual segmentation of 2D slices; grayscale threshold applied to 3D volume"
        },
        {
          "@id": "ada:parameter/labxctTAPP/segmentationThresholdValuesOrCriteria",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/segmentationThresholdValuesOrCriteria"
            }
          ],
          "schema:name": "Segmentation Threshold Values or Criteria",
          "schema:value": "Thresholds not given numerically; SEM images used to define phases; errors from threshold + subvoxel variability generally <5% for grains >125 voxels"
        },
        {
          "@id": "ada:parameter/labxctTAPP/phaseIdentificationMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/phaseIdentificationMethod"
            }
          ],
          "schema:name": "Phase Identification Method",
          "schema:value": "Phases: augite, mesostasis, olivine, titanomagnetite, pore space — identified by grayscale correlated to linear attenuation coefficients; verified with SEM"
        },
        {
          "@id": "ada:parameter/labxctTAPP/partialVolumeEffectCriteria",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/partialVolumeEffectCriteria"
            }
          ],
          "schema:name": "Partial Volume Effect Criteria",
          "schema:value": "Errors from threshold + PVE generally <5% for grains >125 voxels; features smaller than ~3 voxels unreliable"
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Manchester X-ray Imaging Facility, U. Manchester"
      },
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Bulk specimen or fragment — \"a single 2.7 g chip\" (p.3), characterised \"Prior to destructive sampling\" (p.3); \"The entire 2.7 g chip was scanned by XCT\" (p.6)",
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
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/labxctTAPP/effectiveSpatialResolution",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/effectiveSpatialResolution"
        }
      ],
      "schema:name": "Effective Spatial Resolution (PSF/MTF)",
      "schema:value": "N — the paper states \"a resolution of 10.3 x 10.3 x 10.3 µm³ per voxel\", i.e. the voxel size; no effective resolution reported"
    },
    {
      "@id": "ada:parameter/labxctTAPP/voiApplied",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/voiApplied"
        }
      ],
      "schema:name": "VOI Applied",
      "schema:value": "Entire chip volume (~250 thin-section equivalents); six interspaced 2D slices at ~1 mm spacing for modal mineralogy"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Beam Hardening Artifact Assessment",
      "dqv:value": "High noise in central portion of sample attributed to BH; augite/mesostasis difficult to distinguish in central region"
    },
    {
      "dqv:isMeasurementOf": "Cross-Validation Outcome",
      "dqv:value": "BSE contrast differences between phases comparable to XCT attenuation contrast; XCT lower spatial resolution"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM-BSE (qualitative comparison)",
        "schema:description": "BSE images compared with XCT attenuation contrast"
      }
    }
  ],
  "ada:analyticalMode": [
    "Single-volume"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "NWA 5790",
  "ada:samplingUnitName": "Labelled: 2-D slices of the one scanned volume — \"XCT slice 500\" to \"XCT slice 1000\" (Table 1, p.2) — of \"a single 2.7 g chip\" of NWA 5790 (p.3)"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XCT/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:labxctTAPP-detail-Tomkinson2015",
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
              "@id": "ada:parameter/labxctTAPP/sampleDimensions",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/labxctTAPP/sampleDimensions"
                }
              ],
              "schema:name": "Sample Dimensions (L \u00d7 W \u00d7 H)",
              "schema:value": "~1.1 \u00d7 1.2 \u00d7 0.8 cm"
            },
            {
              "@id": "ada:parameter/labxctTAPP/sampleMass",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/labxctTAPP/sampleMass"
                }
              ],
              "schema:name": "Sample Mass",
              "schema:value": 2.7,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "2.7 g"
            }
          ],
          "schema:name": "NWA 5790"
        }
      ],
      "prov:used": [
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "Avizo\u2122",
              "@type": [
                "schema:SoftwareApplication"
              ]
            }
          ]
        },
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "XCT",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/labxctTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 120,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "120 keV (reported in paper as 'accelerating voltage of 120 keV'; likely typo for 120 kV)"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/voxelSize",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/voxelSize"
                    }
                  ],
                  "schema:name": "Voxel Size",
                  "schema:value": 10.3,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "10.3 \u00d7 10.3 \u00d7 10.3 \u00b5m\u00b3"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:labxctTAPP-detail-Tomkinson2015/instrument/XCT"
            }
          ]
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/labxctTAPP/numberOfProjections",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/numberOfProjections"
            }
          ],
          "schema:name": "Number of Projections",
          "schema:value": 3143
        },
        {
          "@id": "ada:parameter/labxctTAPP/exposureTimePerProjection",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/exposureTimePerProjection"
            }
          ],
          "schema:name": "Exposure Time per Projection",
          "schema:value": 20,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "20 s"
        },
        {
          "@id": "ada:parameter/labxctTAPP/segmentationMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/segmentationMethod"
            }
          ],
          "schema:name": "Segmentation Method",
          "schema:value": "Manual segmentation of 2D slices; grayscale threshold applied to 3D volume"
        },
        {
          "@id": "ada:parameter/labxctTAPP/segmentationThresholdValuesOrCriteria",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/segmentationThresholdValuesOrCriteria"
            }
          ],
          "schema:name": "Segmentation Threshold Values or Criteria",
          "schema:value": "Thresholds not given numerically; SEM images used to define phases; errors from threshold + subvoxel variability generally <5% for grains >125 voxels"
        },
        {
          "@id": "ada:parameter/labxctTAPP/phaseIdentificationMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/phaseIdentificationMethod"
            }
          ],
          "schema:name": "Phase Identification Method",
          "schema:value": "Phases: augite, mesostasis, olivine, titanomagnetite, pore space \u2014 identified by grayscale correlated to linear attenuation coefficients; verified with SEM"
        },
        {
          "@id": "ada:parameter/labxctTAPP/partialVolumeEffectCriteria",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/partialVolumeEffectCriteria"
            }
          ],
          "schema:name": "Partial Volume Effect Criteria",
          "schema:value": "Errors from threshold + PVE generally <5% for grains >125 voxels; features smaller than ~3 voxels unreliable"
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Manchester X-ray Imaging Facility, U. Manchester"
      },
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Bulk specimen or fragment \u2014 \"a single 2.7 g chip\" (p.3), characterised \"Prior to destructive sampling\" (p.3); \"The entire 2.7 g chip was scanned by XCT\" (p.6)",
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
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/labxctTAPP/effectiveSpatialResolution",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/effectiveSpatialResolution"
        }
      ],
      "schema:name": "Effective Spatial Resolution (PSF/MTF)",
      "schema:value": "N \u2014 the paper states \"a resolution of 10.3 x 10.3 x 10.3 \u00b5m\u00b3 per voxel\", i.e. the voxel size; no effective resolution reported"
    },
    {
      "@id": "ada:parameter/labxctTAPP/voiApplied",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/voiApplied"
        }
      ],
      "schema:name": "VOI Applied",
      "schema:value": "Entire chip volume (~250 thin-section equivalents); six interspaced 2D slices at ~1 mm spacing for modal mineralogy"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Beam Hardening Artifact Assessment",
      "dqv:value": "High noise in central portion of sample attributed to BH; augite/mesostasis difficult to distinguish in central region"
    },
    {
      "dqv:isMeasurementOf": "Cross-Validation Outcome",
      "dqv:value": "BSE contrast differences between phases comparable to XCT attenuation contrast; XCT lower spatial resolution"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM-BSE (qualitative comparison)",
        "schema:description": "BSE images compared with XCT attenuation contrast"
      }
    }
  ],
  "ada:analyticalMode": [
    "Single-volume"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "NWA 5790",
  "ada:samplingUnitName": "Labelled: 2-D slices of the one scanned volume \u2014 \"XCT slice 500\" to \"XCT slice 1000\" (Table 1, p.2) \u2014 of \"a single 2.7 g chip\" of NWA 5790 (p.3)"
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

ex:labxctTAPP-detail-Tomkinson2015 a schema1:Dataset,
        schema1:Product ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/voiApplied> ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "BSE images compared with XCT attenuation contrast" ;
                    schema1:name "SEM-BSE (qualitative comparison)" ] ] ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Cross-Validation Outcome" ;
            dqv:value "BSE contrast differences between phases comparable to XCT attenuation contrast; XCT lower spatial resolution" ],
        [ dqv:isMeasurementOf "Beam Hardening Artifact Assessment" ;
            dqv:value "High noise in central portion of sample attributed to BH; augite/mesostasis difficult to distinguish in central region" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Bulk specimen or fragment — \"a single 2.7 g chip\" (p.3), characterised \"Prior to destructive sampling\" (p.3); \"The entire 2.7 g chip was scanned by XCT\" (p.6)" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/exposureTimePerProjection>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/numberOfProjections>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/partialVolumeEffectCriteria>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/phaseIdentificationMethod>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationMethod>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationThresholdValuesOrCriteria> ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Manchester X-ray Imaging Facility, U. Manchester" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleDimensions>,
                        <https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleMass> ;
                    schema1:name "NWA 5790" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ schema1:instrument <https://example.org/labxctTAPP-detail-Tomkinson2015/instrument/XCT> ],
                [ bios:computationalTool [ a schema1:SoftwareApplication ;
                            schema1:name "Avizo™" ;
                            ada:toolRole "dataReduction" ] ] ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalMode "Single-volume" ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:sampleName "NWA 5790" ;
    ada:samplingUnitName "Labelled: 2-D slices of the one scanned volume — \"XCT slice 500\" to \"XCT slice 1000\" (Table 1, p.2) — of \"a single 2.7 g chip\" of NWA 5790 (p.3)" ;
    ada:sessionIdentifier "missing" .

<https://example.org/labxctTAPP-detail-Tomkinson2015/instrument/XCT> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/voxelSize> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "XCT" ;
    schema1:name "no value available: schema:name" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:description "120 keV (reported in paper as 'accelerating voltage of 120 keV'; likely typo for 120 kV)" ;
    schema1:name "Accelerating Voltage" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/acceleratingVoltage> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 120 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> a schema1:PropertyValue ;
    schema1:name "Effective Spatial Resolution (PSF/MTF)" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> ;
    schema1:value "N — the paper states \"a resolution of 10.3 x 10.3 x 10.3 µm³ per voxel\", i.e. the voxel size; no effective resolution reported" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/exposureTimePerProjection> a schema1:PropertyValue ;
    schema1:description "20 s" ;
    schema1:name "Exposure Time per Projection" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/exposureTimePerProjection> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 20 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/numberOfProjections> a schema1:PropertyValue ;
    schema1:name "Number of Projections" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/numberOfProjections> ;
    schema1:value 3143 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/partialVolumeEffectCriteria> a schema1:PropertyValue ;
    schema1:name "Partial Volume Effect Criteria" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/partialVolumeEffectCriteria> ;
    schema1:value "Errors from threshold + PVE generally <5% for grains >125 voxels; features smaller than ~3 voxels unreliable" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/phaseIdentificationMethod> a schema1:PropertyValue ;
    schema1:name "Phase Identification Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/phaseIdentificationMethod> ;
    schema1:value "Phases: augite, mesostasis, olivine, titanomagnetite, pore space — identified by grayscale correlated to linear attenuation coefficients; verified with SEM" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleDimensions> a schema1:PropertyValue ;
    schema1:name "Sample Dimensions (L × W × H)" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleDimensions> ;
    schema1:value "~1.1 × 1.2 × 0.8 cm" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleMass> a schema1:PropertyValue ;
    schema1:description "2.7 g" ;
    schema1:name "Sample Mass" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleMass> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 2.7e+00 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationMethod> a schema1:PropertyValue ;
    schema1:name "Segmentation Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationMethod> ;
    schema1:value "Manual segmentation of 2D slices; grayscale threshold applied to 3D volume" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationThresholdValuesOrCriteria> a schema1:PropertyValue ;
    schema1:name "Segmentation Threshold Values or Criteria" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationThresholdValuesOrCriteria> ;
    schema1:value "Thresholds not given numerically; SEM images used to define phases; errors from threshold + subvoxel variability generally <5% for grains >125 voxels" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/voiApplied> a schema1:PropertyValue ;
    schema1:name "VOI Applied" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/voiApplied> ;
    schema1:value "Entire chip volume (~250 thin-section equivalents); six interspaced 2D slices at ~1 mm spacing for modal mineralogy" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/voxelSize> a schema1:PropertyValue ;
    schema1:description "10.3 × 10.3 × 10.3 µm³" ;
    schema1:name "Voxel Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/voxelSize> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1.03e+01 .


```


### detail example Glavin2023
detail instance derived from Glavin et al. 2023 (MAPS) Murchison CM2 Single-volume Nikon XTH 320 NASA JSC X-FaCT.
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
  "@id": "ex:labxctTAPP-detail-Glavin2023",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/labxctTAPP/sampleMountingMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/sampleMountingMethod"
            }
          ],
          "schema:name": "Sample Mounting Method",
          "schema:value": "Glass vial placed in scanner"
        },
        {
          "@id": "ada:parameter/labxctTAPP/sourceToObjectDistance",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/sourceToObjectDistance"
            }
          ],
          "schema:name": "Source-to-Object Distance (SOD)",
          "schema:value": 39.22,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "39.22 mm"
        },
        {
          "@id": "ada:parameter/labxctTAPP/sourceToDetectorDistance",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/sourceToDetectorDistance"
            }
          ],
          "schema:name": "Source-to-Detector Distance (SDD)",
          "schema:value": 679.51,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "679.51 mm"
        },
        {
          "@id": "ada:parameter/labxctTAPP/rotationRange",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/rotationRange"
            }
          ],
          "schema:name": "Rotation Range",
          "schema:value": 360,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "360° (continuous)"
        },
        {
          "@id": "ada:parameter/labxctTAPP/numberOfProjections",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/numberOfProjections"
            }
          ],
          "schema:name": "Number of Projections",
          "schema:value": 3141
        },
        {
          "@id": "ada:parameter/labxctTAPP/rotationStepSize",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/rotationStepSize"
            }
          ],
          "schema:name": "Rotation Step Size",
          "schema:value": 0.115,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "0.115°"
        },
        {
          "@id": "ada:parameter/labxctTAPP/exposureTimePerProjection",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/exposureTimePerProjection"
            }
          ],
          "schema:name": "Exposure Time per Projection",
          "schema:value": 1.0,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "1.00 s per frame"
        },
        {
          "@id": "ada:parameter/labxctTAPP/framesAveragedPerProjection",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/framesAveragedPerProjection"
            }
          ],
          "schema:name": "Frames Averaged per Projection",
          "schema:value": 8,
          "schema:description": "8 frames averaged per projection"
        },
        {
          "@id": "ada:parameter/labxctTAPP/rotationMode",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/rotationMode"
            }
          ],
          "schema:name": "Rotation Mode",
          "schema:value": "Continuous 360° rotation"
        }
      ],
      "prov:used": [
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "Nikon CTAgentPro v5.4 (FBP algorithm)",
              "@type": [
                "schema:SoftwareApplication"
              ]
            }
          ]
        },
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "XCT",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/labxctTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 160,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "160 keV (paper reports as X-ray photon energy; equivalent to 160 kV tube voltage)"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/tubeCurrent",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/tubeCurrent"
                    }
                  ],
                  "schema:name": "Tube Current",
                  "schema:value": 38,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "38 µA"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/xRayPreFilter",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/xRayPreFilter"
                    }
                  ],
                  "schema:name": "X-ray Pre-filter",
                  "schema:value": "None (intentionally unfiltered; worst-case dose experiment)"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/voxelSize",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/voxelSize"
                    }
                  ],
                  "schema:name": "Voxel Size",
                  "schema:value": 11.54,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "11.54 µm (cubic voxel edge)"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:labxctTAPP-detail-Glavin2023/instrument/XCT"
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
              "@id": "ada:parameter/labxctTAPP/sampleMass",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/labxctTAPP/sampleMass"
                }
              ],
              "schema:name": "Sample Mass",
              "schema:value": 4.643,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "4.6430 g (Murchison B in vial)"
            }
          ],
          "schema:name": "Murchison B (USNM 5453,1)"
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "NASA JSC Astromaterials X-FaCT Lab"
      },
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Powder or crushed split — chips \"lightly crushed by hand\", then \"further ground down by hand with a pestle until no visible fragments could be observed\", vortex mixed 3 min and \"split into two approximately equal mass portions\" (p.3); Murchison B (4.6430 g) was scanned",
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
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "schema:distribution": [
    {
      "schema:encodingFormat": [
        "TIFF (continuous series of 2D TIFF images)"
      ]
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/labxctTAPP/effectiveSpatialResolution",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/effectiveSpatialResolution"
        }
      ],
      "schema:name": "Effective Spatial Resolution (PSF/MTF)",
      "schema:value": "~30 µm — stated as \"resolution limits of ~30 µm (around 3x the voxel size)\" against an 11.54 µm voxel. Rule-of-thumb estimate; no PSF or MTF measurement"
    },
    {
      "@id": "ada:parameter/labxctTAPP/voiApplied",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/voiApplied"
        }
      ],
      "schema:name": "VOI Applied",
      "schema:value": "Full vial volume (2000 × 2000 × 2000 voxels)"
    }
  ],
  "schema:contributor": [
    {
      "schema:roleName": "analyst",
      "schema:contributor": {
        "schema:name": "Scott A. Eckley"
      }
    }
  ],
  "ada:analyticalMode": [
    "Single-volume"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "Scott A. Eckley",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleDimensions": "missing",
  "ada:sampleName": "Murchison B (USNM 5453,1)",
  "ada:samplingUnitName": "Labelled: the split \"Murchison B (mass = 4.6430 g)\", scanned in its sealed vial; its counterpart \"Murchison A\" was the unscanned control (p.3)"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XCT/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:labxctTAPP-detail-Glavin2023",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/labxctTAPP/sampleMountingMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/sampleMountingMethod"
            }
          ],
          "schema:name": "Sample Mounting Method",
          "schema:value": "Glass vial placed in scanner"
        },
        {
          "@id": "ada:parameter/labxctTAPP/sourceToObjectDistance",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/sourceToObjectDistance"
            }
          ],
          "schema:name": "Source-to-Object Distance (SOD)",
          "schema:value": 39.22,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "39.22 mm"
        },
        {
          "@id": "ada:parameter/labxctTAPP/sourceToDetectorDistance",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/sourceToDetectorDistance"
            }
          ],
          "schema:name": "Source-to-Detector Distance (SDD)",
          "schema:value": 679.51,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "679.51 mm"
        },
        {
          "@id": "ada:parameter/labxctTAPP/rotationRange",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/rotationRange"
            }
          ],
          "schema:name": "Rotation Range",
          "schema:value": 360,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "360\u00b0 (continuous)"
        },
        {
          "@id": "ada:parameter/labxctTAPP/numberOfProjections",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/numberOfProjections"
            }
          ],
          "schema:name": "Number of Projections",
          "schema:value": 3141
        },
        {
          "@id": "ada:parameter/labxctTAPP/rotationStepSize",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/rotationStepSize"
            }
          ],
          "schema:name": "Rotation Step Size",
          "schema:value": 0.115,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "0.115\u00b0"
        },
        {
          "@id": "ada:parameter/labxctTAPP/exposureTimePerProjection",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/exposureTimePerProjection"
            }
          ],
          "schema:name": "Exposure Time per Projection",
          "schema:value": 1.0,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "1.00 s per frame"
        },
        {
          "@id": "ada:parameter/labxctTAPP/framesAveragedPerProjection",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/framesAveragedPerProjection"
            }
          ],
          "schema:name": "Frames Averaged per Projection",
          "schema:value": 8,
          "schema:description": "8 frames averaged per projection"
        },
        {
          "@id": "ada:parameter/labxctTAPP/rotationMode",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/rotationMode"
            }
          ],
          "schema:name": "Rotation Mode",
          "schema:value": "Continuous 360\u00b0 rotation"
        }
      ],
      "prov:used": [
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "Nikon CTAgentPro v5.4 (FBP algorithm)",
              "@type": [
                "schema:SoftwareApplication"
              ]
            }
          ]
        },
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "XCT",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/labxctTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 160,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "160 keV (paper reports as X-ray photon energy; equivalent to 160 kV tube voltage)"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/tubeCurrent",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/tubeCurrent"
                    }
                  ],
                  "schema:name": "Tube Current",
                  "schema:value": 38,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "38 \u00b5A"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/xRayPreFilter",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/xRayPreFilter"
                    }
                  ],
                  "schema:name": "X-ray Pre-filter",
                  "schema:value": "None (intentionally unfiltered; worst-case dose experiment)"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/voxelSize",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/voxelSize"
                    }
                  ],
                  "schema:name": "Voxel Size",
                  "schema:value": 11.54,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "11.54 \u00b5m (cubic voxel edge)"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:labxctTAPP-detail-Glavin2023/instrument/XCT"
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
              "@id": "ada:parameter/labxctTAPP/sampleMass",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/labxctTAPP/sampleMass"
                }
              ],
              "schema:name": "Sample Mass",
              "schema:value": 4.643,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "4.6430 g (Murchison B in vial)"
            }
          ],
          "schema:name": "Murchison B (USNM 5453,1)"
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "NASA JSC Astromaterials X-FaCT Lab"
      },
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Powder or crushed split \u2014 chips \"lightly crushed by hand\", then \"further ground down by hand with a pestle until no visible fragments could be observed\", vortex mixed 3 min and \"split into two approximately equal mass portions\" (p.3); Murchison B (4.6430 g) was scanned",
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
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "schema:distribution": [
    {
      "schema:encodingFormat": [
        "TIFF (continuous series of 2D TIFF images)"
      ]
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/labxctTAPP/effectiveSpatialResolution",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/effectiveSpatialResolution"
        }
      ],
      "schema:name": "Effective Spatial Resolution (PSF/MTF)",
      "schema:value": "~30 \u00b5m \u2014 stated as \"resolution limits of ~30 \u00b5m (around 3x the voxel size)\" against an 11.54 \u00b5m voxel. Rule-of-thumb estimate; no PSF or MTF measurement"
    },
    {
      "@id": "ada:parameter/labxctTAPP/voiApplied",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/voiApplied"
        }
      ],
      "schema:name": "VOI Applied",
      "schema:value": "Full vial volume (2000 \u00d7 2000 \u00d7 2000 voxels)"
    }
  ],
  "schema:contributor": [
    {
      "schema:roleName": "analyst",
      "schema:contributor": {
        "schema:name": "Scott A. Eckley"
      }
    }
  ],
  "ada:analyticalMode": [
    "Single-volume"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "Scott A. Eckley",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleDimensions": "missing",
  "ada:sampleName": "Murchison B (USNM 5453,1)",
  "ada:samplingUnitName": "Labelled: the split \"Murchison B (mass = 4.6430 g)\", scanned in its sealed vial; its counterpart \"Murchison A\" was the unscanned control (p.3)"
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

ex:labxctTAPP-detail-Glavin2023 a schema1:Dataset,
        schema1:Product ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/voiApplied> ;
    schema1:contributor [ schema1:contributor [ schema1:name "Scott A. Eckley" ] ;
            schema1:roleName "analyst" ] ;
    schema1:distribution [ schema1:encodingFormat "TIFF (continuous series of 2D TIFF images)" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Powder or crushed split — chips \"lightly crushed by hand\", then \"further ground down by hand with a pestle until no visible fragments could be observed\", vortex mixed 3 min and \"split into two approximately equal mass portions\" (p.3); Murchison B (4.6430 g) was scanned" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/exposureTimePerProjection>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/framesAveragedPerProjection>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/numberOfProjections>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/rotationMode>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/rotationRange>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/rotationStepSize>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleMountingMethod>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/sourceToDetectorDistance>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/sourceToObjectDistance> ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "NASA JSC Astromaterials X-FaCT Lab" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleMass> ;
                    schema1:name "Murchison B (USNM 5453,1)" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ bios:computationalTool [ a schema1:SoftwareApplication ;
                            schema1:name "Nikon CTAgentPro v5.4 (FBP algorithm)" ;
                            ada:toolRole "dataReduction" ] ],
                [ schema1:instrument <https://example.org/labxctTAPP-detail-Glavin2023/instrument/XCT> ] ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "Scott A. Eckley" ;
    ada:analyticalMode "Single-volume" ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:sampleDimensions "missing" ;
    ada:sampleName "Murchison B (USNM 5453,1)" ;
    ada:samplingUnitName "Labelled: the split \"Murchison B (mass = 4.6430 g)\", scanned in its sealed vial; its counterpart \"Murchison A\" was the unscanned control (p.3)" ;
    ada:sessionIdentifier "missing" .

<https://example.org/labxctTAPP-detail-Glavin2023/instrument/XCT> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/tubeCurrent>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/voxelSize>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayPreFilter> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "XCT" ;
    schema1:name "no value available: schema:name" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:description "160 keV (paper reports as X-ray photon energy; equivalent to 160 kV tube voltage)" ;
    schema1:name "Accelerating Voltage" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/acceleratingVoltage> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 160 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> a schema1:PropertyValue ;
    schema1:name "Effective Spatial Resolution (PSF/MTF)" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> ;
    schema1:value "~30 µm — stated as \"resolution limits of ~30 µm (around 3x the voxel size)\" against an 11.54 µm voxel. Rule-of-thumb estimate; no PSF or MTF measurement" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/exposureTimePerProjection> a schema1:PropertyValue ;
    schema1:description "1.00 s per frame" ;
    schema1:name "Exposure Time per Projection" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/exposureTimePerProjection> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1e+00 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/framesAveragedPerProjection> a schema1:PropertyValue ;
    schema1:description "8 frames averaged per projection" ;
    schema1:name "Frames Averaged per Projection" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/framesAveragedPerProjection> ;
    schema1:value 8 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/numberOfProjections> a schema1:PropertyValue ;
    schema1:name "Number of Projections" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/numberOfProjections> ;
    schema1:value 3141 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/rotationMode> a schema1:PropertyValue ;
    schema1:name "Rotation Mode" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/rotationMode> ;
    schema1:value "Continuous 360° rotation" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/rotationRange> a schema1:PropertyValue ;
    schema1:description "360° (continuous)" ;
    schema1:name "Rotation Range" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/rotationRange> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 360 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/rotationStepSize> a schema1:PropertyValue ;
    schema1:description "0.115°" ;
    schema1:name "Rotation Step Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/rotationStepSize> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1.15e-01 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleMass> a schema1:PropertyValue ;
    schema1:description "4.6430 g (Murchison B in vial)" ;
    schema1:name "Sample Mass" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleMass> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 4.643e+00 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleMountingMethod> a schema1:PropertyValue ;
    schema1:name "Sample Mounting Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleMountingMethod> ;
    schema1:value "Glass vial placed in scanner" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/sourceToDetectorDistance> a schema1:PropertyValue ;
    schema1:description "679.51 mm" ;
    schema1:name "Source-to-Detector Distance (SDD)" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/sourceToDetectorDistance> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 6.7951e+02 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/sourceToObjectDistance> a schema1:PropertyValue ;
    schema1:description "39.22 mm" ;
    schema1:name "Source-to-Object Distance (SOD)" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/sourceToObjectDistance> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 3.922e+01 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/tubeCurrent> a schema1:PropertyValue ;
    schema1:description "38 µA" ;
    schema1:name "Tube Current" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/tubeCurrent> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 38 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/voiApplied> a schema1:PropertyValue ;
    schema1:name "VOI Applied" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/voiApplied> ;
    schema1:value "Full vial volume (2000 × 2000 × 2000 voxels)" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/voxelSize> a schema1:PropertyValue ;
    schema1:description "11.54 µm (cubic voxel edge)" ;
    schema1:name "Voxel Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/voxelSize> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1.154e+01 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayPreFilter> a schema1:PropertyValue ;
    schema1:name "X-ray Pre-filter" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayPreFilter> ;
    schema1:value "None (intentionally unfiltered; worst-case dose experiment)" .


```


### detail example Dias2019
detail instance derived from Nascimento-Dias et al. 2019 (Appl. Radiat. Isot.) NWA 8277 + NWA 6963 Single-volume Bruker Skyscan 1173.
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
  "@id": "ex:labxctTAPP-detail-Dias2019",
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
              "@id": "ada:parameter/labxctTAPP/sampleDimensions",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/labxctTAPP/sampleDimensions"
                }
              ],
              "schema:name": "Sample Dimensions (L × W × H)",
              "schema:value": "~4 mm fragments"
            }
          ],
          "schema:name": "NWA 8277; NWA 6963"
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/labxctTAPP/sampleMountingMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/sampleMountingMethod"
            }
          ],
          "schema:name": "Sample Mounting Method",
          "schema:value": "Polystyrene support"
        },
        {
          "@id": "ada:parameter/labxctTAPP/rotationRange",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/rotationRange"
            }
          ],
          "schema:name": "Rotation Range",
          "schema:value": 360,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "360°"
        },
        {
          "@id": "ada:parameter/labxctTAPP/rotationStepSize",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/rotationStepSize"
            }
          ],
          "schema:name": "Rotation Step Size",
          "schema:value": 0.4,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "0.4°/step"
        },
        {
          "@id": "ada:parameter/labxctTAPP/segmentationMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/segmentationMethod"
            }
          ],
          "schema:name": "Segmentation Method",
          "schema:value": "Adaptive (mean) thresholding"
        },
        {
          "@id": "ada:parameter/labxctTAPP/segmentationThresholdValuesOrCriteria",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/segmentationThresholdValuesOrCriteria"
            }
          ],
          "schema:name": "Segmentation Threshold Values or Criteria",
          "schema:value": "Adaptive mean threshold; total analyzed VOI for NWA 8277 = 5.39 mm³"
        },
        {
          "@id": "ada:parameter/labxctTAPP/phaseIdentificationMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/phaseIdentificationMethod"
            }
          ],
          "schema:name": "Phase Identification Method",
          "schema:value": "Three density regions: high, medium, low density; porosity separate"
        }
      ],
      "prov:used": [
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "DataViewer; CTVox; CTAn (Bruker proprietary suite)",
              "@type": [
                "schema:SoftwareApplication"
              ]
            }
          ]
        },
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "XCT",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/labxctTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 50,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "50 kV"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/tubeCurrent",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/tubeCurrent"
                    }
                  ],
                  "schema:name": "Tube Current",
                  "schema:value": 160,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "160 µA"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/xRayPreFilter",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/xRayPreFilter"
                    }
                  ],
                  "schema:name": "X-ray Pre-filter",
                  "schema:value": "1.0 mm aluminum"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/voxelSize",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/voxelSize"
                    }
                  ],
                  "schema:name": "Voxel Size",
                  "schema:value": 5.34,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "5.34 µm"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:labxctTAPP-detail-Dias2019/instrument/XCT"
            }
          ]
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Nuclear Instrumentation Lab, COPPE, UFRJ, Brazil"
      },
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Bulk specimen or fragment — \"fragments of about 4 mm of both meteorites were analyzed through X-ray micro-CT\" (p.5)",
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
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/labxctTAPP/effectiveSpatialResolution",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/effectiveSpatialResolution"
        }
      ],
      "schema:name": "Effective Spatial Resolution (PSF/MTF)",
      "schema:value": "N — voxel size only (5.34 µm); the paper describes resolution only generically (\"of the order of microns\")"
    },
    {
      "@id": "ada:parameter/labxctTAPP/voiApplied",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/voiApplied"
        }
      ],
      "schema:name": "VOI Applied",
      "schema:value": "5.39 mm³ total analyzed volume (NWA 8277)"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Cross-Validation Outcome",
      "dqv:value": "Micro-XRF structural observations consistent with meteorite classification"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Micro-XRF (same samples)",
        "schema:description": "Micro-XRF performed on same meteorite fragments after XCT"
      }
    }
  ],
  "ada:analyticalMode": [
    "Single-volume"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "NWA 8277; NWA 6963",
  "ada:samplingUnitName": "Sample name only — \"fragments of about 4 mm of both meteorites\", NWA 8277 and NWA 6963 (p.5); not otherwise labelled"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XCT/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:labxctTAPP-detail-Dias2019",
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
              "@id": "ada:parameter/labxctTAPP/sampleDimensions",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/labxctTAPP/sampleDimensions"
                }
              ],
              "schema:name": "Sample Dimensions (L \u00d7 W \u00d7 H)",
              "schema:value": "~4 mm fragments"
            }
          ],
          "schema:name": "NWA 8277; NWA 6963"
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/labxctTAPP/sampleMountingMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/sampleMountingMethod"
            }
          ],
          "schema:name": "Sample Mounting Method",
          "schema:value": "Polystyrene support"
        },
        {
          "@id": "ada:parameter/labxctTAPP/rotationRange",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/rotationRange"
            }
          ],
          "schema:name": "Rotation Range",
          "schema:value": 360,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "360\u00b0"
        },
        {
          "@id": "ada:parameter/labxctTAPP/rotationStepSize",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/rotationStepSize"
            }
          ],
          "schema:name": "Rotation Step Size",
          "schema:value": 0.4,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "0.4\u00b0/step"
        },
        {
          "@id": "ada:parameter/labxctTAPP/segmentationMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/segmentationMethod"
            }
          ],
          "schema:name": "Segmentation Method",
          "schema:value": "Adaptive (mean) thresholding"
        },
        {
          "@id": "ada:parameter/labxctTAPP/segmentationThresholdValuesOrCriteria",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/segmentationThresholdValuesOrCriteria"
            }
          ],
          "schema:name": "Segmentation Threshold Values or Criteria",
          "schema:value": "Adaptive mean threshold; total analyzed VOI for NWA 8277 = 5.39 mm\u00b3"
        },
        {
          "@id": "ada:parameter/labxctTAPP/phaseIdentificationMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/phaseIdentificationMethod"
            }
          ],
          "schema:name": "Phase Identification Method",
          "schema:value": "Three density regions: high, medium, low density; porosity separate"
        }
      ],
      "prov:used": [
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "DataViewer; CTVox; CTAn (Bruker proprietary suite)",
              "@type": [
                "schema:SoftwareApplication"
              ]
            }
          ]
        },
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "XCT",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/labxctTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 50,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "50 kV"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/tubeCurrent",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/tubeCurrent"
                    }
                  ],
                  "schema:name": "Tube Current",
                  "schema:value": 160,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "160 \u00b5A"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/xRayPreFilter",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/xRayPreFilter"
                    }
                  ],
                  "schema:name": "X-ray Pre-filter",
                  "schema:value": "1.0 mm aluminum"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/voxelSize",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/voxelSize"
                    }
                  ],
                  "schema:name": "Voxel Size",
                  "schema:value": 5.34,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "5.34 \u00b5m"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:labxctTAPP-detail-Dias2019/instrument/XCT"
            }
          ]
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Nuclear Instrumentation Lab, COPPE, UFRJ, Brazil"
      },
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Bulk specimen or fragment \u2014 \"fragments of about 4 mm of both meteorites were analyzed through X-ray micro-CT\" (p.5)",
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
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/labxctTAPP/effectiveSpatialResolution",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/effectiveSpatialResolution"
        }
      ],
      "schema:name": "Effective Spatial Resolution (PSF/MTF)",
      "schema:value": "N \u2014 voxel size only (5.34 \u00b5m); the paper describes resolution only generically (\"of the order of microns\")"
    },
    {
      "@id": "ada:parameter/labxctTAPP/voiApplied",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/voiApplied"
        }
      ],
      "schema:name": "VOI Applied",
      "schema:value": "5.39 mm\u00b3 total analyzed volume (NWA 8277)"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Cross-Validation Outcome",
      "dqv:value": "Micro-XRF structural observations consistent with meteorite classification"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Micro-XRF (same samples)",
        "schema:description": "Micro-XRF performed on same meteorite fragments after XCT"
      }
    }
  ],
  "ada:analyticalMode": [
    "Single-volume"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "NWA 8277; NWA 6963",
  "ada:samplingUnitName": "Sample name only \u2014 \"fragments of about 4 mm of both meteorites\", NWA 8277 and NWA 6963 (p.5); not otherwise labelled"
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

ex:labxctTAPP-detail-Dias2019 a schema1:Dataset,
        schema1:Product ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/voiApplied> ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "Micro-XRF performed on same meteorite fragments after XCT" ;
                    schema1:name "Micro-XRF (same samples)" ] ] ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Cross-Validation Outcome" ;
            dqv:value "Micro-XRF structural observations consistent with meteorite classification" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Bulk specimen or fragment — \"fragments of about 4 mm of both meteorites were analyzed through X-ray micro-CT\" (p.5)" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/phaseIdentificationMethod>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/rotationRange>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/rotationStepSize>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleMountingMethod>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationMethod>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationThresholdValuesOrCriteria> ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Nuclear Instrumentation Lab, COPPE, UFRJ, Brazil" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleDimensions> ;
                    schema1:name "NWA 8277; NWA 6963" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ bios:computationalTool [ a schema1:SoftwareApplication ;
                            schema1:name "DataViewer; CTVox; CTAn (Bruker proprietary suite)" ;
                            ada:toolRole "dataReduction" ] ],
                [ schema1:instrument <https://example.org/labxctTAPP-detail-Dias2019/instrument/XCT> ] ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalMode "Single-volume" ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:sampleName "NWA 8277; NWA 6963" ;
    ada:samplingUnitName "Sample name only — \"fragments of about 4 mm of both meteorites\", NWA 8277 and NWA 6963 (p.5); not otherwise labelled" ;
    ada:sessionIdentifier "missing" .

<https://example.org/labxctTAPP-detail-Dias2019/instrument/XCT> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/tubeCurrent>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/voxelSize>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayPreFilter> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "XCT" ;
    schema1:name "no value available: schema:name" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:description "50 kV" ;
    schema1:name "Accelerating Voltage" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/acceleratingVoltage> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 50 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> a schema1:PropertyValue ;
    schema1:name "Effective Spatial Resolution (PSF/MTF)" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> ;
    schema1:value "N — voxel size only (5.34 µm); the paper describes resolution only generically (\"of the order of microns\")" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/phaseIdentificationMethod> a schema1:PropertyValue ;
    schema1:name "Phase Identification Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/phaseIdentificationMethod> ;
    schema1:value "Three density regions: high, medium, low density; porosity separate" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/rotationRange> a schema1:PropertyValue ;
    schema1:description "360°" ;
    schema1:name "Rotation Range" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/rotationRange> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 360 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/rotationStepSize> a schema1:PropertyValue ;
    schema1:description "0.4°/step" ;
    schema1:name "Rotation Step Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/rotationStepSize> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 4e-01 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleDimensions> a schema1:PropertyValue ;
    schema1:name "Sample Dimensions (L × W × H)" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleDimensions> ;
    schema1:value "~4 mm fragments" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleMountingMethod> a schema1:PropertyValue ;
    schema1:name "Sample Mounting Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleMountingMethod> ;
    schema1:value "Polystyrene support" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationMethod> a schema1:PropertyValue ;
    schema1:name "Segmentation Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationMethod> ;
    schema1:value "Adaptive (mean) thresholding" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationThresholdValuesOrCriteria> a schema1:PropertyValue ;
    schema1:name "Segmentation Threshold Values or Criteria" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationThresholdValuesOrCriteria> ;
    schema1:value "Adaptive mean threshold; total analyzed VOI for NWA 8277 = 5.39 mm³" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/tubeCurrent> a schema1:PropertyValue ;
    schema1:description "160 µA" ;
    schema1:name "Tube Current" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/tubeCurrent> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 160 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/voiApplied> a schema1:PropertyValue ;
    schema1:name "VOI Applied" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/voiApplied> ;
    schema1:value "5.39 mm³ total analyzed volume (NWA 8277)" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/voxelSize> a schema1:PropertyValue ;
    schema1:description "5.34 µm" ;
    schema1:name "Voxel Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/voxelSize> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 5.34e+00 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayPreFilter> a schema1:PropertyValue ;
    schema1:name "X-ray Pre-filter" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayPreFilter> ;
    schema1:value "1.0 mm aluminum" .


```


### detail example Richard2019
detail instance derived from Richard et al. 2019 (Chem. Geol.) Olivine (melt incl.) Single-volume Zeiss Xradia 510 Versa UNAM Mexico.
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
  "@id": "ex:labxctTAPP-detail-Richard2019",
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
              "@id": "ada:parameter/labxctTAPP/sampleDimensions",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/labxctTAPP/sampleDimensions"
                }
              ],
              "schema:name": "Sample Dimensions (L × W × H)",
              "schema:value": "~1 mm olivine"
            }
          ],
          "schema:name": "Sample A (olivine)"
        }
      ],
      "prov:used": [
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "ImageJ; Avizo 9.2",
              "@type": [
                "schema:SoftwareApplication"
              ]
            }
          ]
        },
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "XCT",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/labxctTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 30,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "30 kV"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/voxelSize",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/voxelSize"
                    }
                  ],
                  "schema:name": "Voxel Size",
                  "schema:value": 2.06,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "2.06 µm/px"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:labxctTAPP-detail-Richard2019/instrument/XCT"
            }
          ]
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/labxctTAPP/numberOfProjections",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/numberOfProjections"
            }
          ],
          "schema:name": "Number of Projections",
          "schema:value": 1601
        },
        {
          "@id": "ada:parameter/labxctTAPP/exposureTimePerProjection",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/exposureTimePerProjection"
            }
          ],
          "schema:name": "Exposure Time per Projection",
          "schema:value": 8,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "8 s"
        },
        {
          "@id": "ada:parameter/labxctTAPP/framesAveragedPerProjection",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/framesAveragedPerProjection"
            }
          ],
          "schema:name": "Frames Averaged per Projection",
          "schema:value": 200,
          "schema:description": "~200 reference (blank) images taken; number of frames averaged per projection N"
        },
        {
          "@id": "ada:parameter/labxctTAPP/segmentationMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/segmentationMethod"
            }
          ],
          "schema:name": "Segmentation Method",
          "schema:value": "Grayscale threshold range selection (ImageJ)"
        },
        {
          "@id": "ada:parameter/labxctTAPP/segmentationThresholdValuesOrCriteria",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/segmentationThresholdValuesOrCriteria"
            }
          ],
          "schema:name": "Segmentation Threshold Values or Criteria",
          "schema:value": "Threshold range selected to include all voxels of one phase while excluding adjacent phases; specific values N"
        },
        {
          "@id": "ada:parameter/labxctTAPP/phaseIdentificationMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/phaseIdentificationMethod"
            }
          ],
          "schema:name": "Phase Identification Method",
          "schema:value": "Phase identified by grayscale contrast (vapor vs. silicate/mineral)"
        },
        {
          "@id": "ada:parameter/labxctTAPP/outputBitDepth",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/outputBitDepth"
            }
          ],
          "schema:name": "Output Bit Depth",
          "schema:value": "32-bit (ZEISS XRM output)"
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Lab. de Microtomografía de Rayos X, UNAM, Mexico"
      },
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Separated grain or crystal — \"a single olivine phenocryst (1.0 mm large) separated from Sample A\" (p.2); epoxy mounting \"carried out after HRXCT analysis\" (Fig. 1, p.4)",
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
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/labxctTAPP/effectiveSpatialResolution",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/effectiveSpatialResolution"
        }
      ],
      "schema:name": "Effective Spatial Resolution (PSF/MTF)",
      "schema:value": "N — the paper's \"spatial resolution of 2.06 µm/px (8.7 µm³/vx)\" is the voxel size; no effective resolution reported"
    },
    {
      "@id": "ada:parameter/labxctTAPP/voiApplied",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/voiApplied"
        }
      ],
      "schema:name": "VOI Applied",
      "schema:value": "Full scan volume"
    }
  ],
  "ada:analyticalMode": [
    "Single-volume"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Sample A (olivine)",
  "ada:samplingUnitName": "Labelled: \"a single olivine phenocryst (1.0 mm large) separated from Sample A\" (p.2), hosting one silicate melt inclusion (Fig. 1, p.4)"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XCT/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:labxctTAPP-detail-Richard2019",
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
              "@id": "ada:parameter/labxctTAPP/sampleDimensions",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/labxctTAPP/sampleDimensions"
                }
              ],
              "schema:name": "Sample Dimensions (L \u00d7 W \u00d7 H)",
              "schema:value": "~1 mm olivine"
            }
          ],
          "schema:name": "Sample A (olivine)"
        }
      ],
      "prov:used": [
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "ImageJ; Avizo 9.2",
              "@type": [
                "schema:SoftwareApplication"
              ]
            }
          ]
        },
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "XCT",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/labxctTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 30,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "30 kV"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/voxelSize",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/voxelSize"
                    }
                  ],
                  "schema:name": "Voxel Size",
                  "schema:value": 2.06,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "2.06 \u00b5m/px"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:labxctTAPP-detail-Richard2019/instrument/XCT"
            }
          ]
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/labxctTAPP/numberOfProjections",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/numberOfProjections"
            }
          ],
          "schema:name": "Number of Projections",
          "schema:value": 1601
        },
        {
          "@id": "ada:parameter/labxctTAPP/exposureTimePerProjection",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/exposureTimePerProjection"
            }
          ],
          "schema:name": "Exposure Time per Projection",
          "schema:value": 8,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "8 s"
        },
        {
          "@id": "ada:parameter/labxctTAPP/framesAveragedPerProjection",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/framesAveragedPerProjection"
            }
          ],
          "schema:name": "Frames Averaged per Projection",
          "schema:value": 200,
          "schema:description": "~200 reference (blank) images taken; number of frames averaged per projection N"
        },
        {
          "@id": "ada:parameter/labxctTAPP/segmentationMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/segmentationMethod"
            }
          ],
          "schema:name": "Segmentation Method",
          "schema:value": "Grayscale threshold range selection (ImageJ)"
        },
        {
          "@id": "ada:parameter/labxctTAPP/segmentationThresholdValuesOrCriteria",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/segmentationThresholdValuesOrCriteria"
            }
          ],
          "schema:name": "Segmentation Threshold Values or Criteria",
          "schema:value": "Threshold range selected to include all voxels of one phase while excluding adjacent phases; specific values N"
        },
        {
          "@id": "ada:parameter/labxctTAPP/phaseIdentificationMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/phaseIdentificationMethod"
            }
          ],
          "schema:name": "Phase Identification Method",
          "schema:value": "Phase identified by grayscale contrast (vapor vs. silicate/mineral)"
        },
        {
          "@id": "ada:parameter/labxctTAPP/outputBitDepth",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/outputBitDepth"
            }
          ],
          "schema:name": "Output Bit Depth",
          "schema:value": "32-bit (ZEISS XRM output)"
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Lab. de Microtomograf\u00eda de Rayos X, UNAM, Mexico"
      },
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Separated grain or crystal \u2014 \"a single olivine phenocryst (1.0 mm large) separated from Sample A\" (p.2); epoxy mounting \"carried out after HRXCT analysis\" (Fig. 1, p.4)",
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
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/labxctTAPP/effectiveSpatialResolution",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/effectiveSpatialResolution"
        }
      ],
      "schema:name": "Effective Spatial Resolution (PSF/MTF)",
      "schema:value": "N \u2014 the paper's \"spatial resolution of 2.06 \u00b5m/px (8.7 \u00b5m\u00b3/vx)\" is the voxel size; no effective resolution reported"
    },
    {
      "@id": "ada:parameter/labxctTAPP/voiApplied",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/voiApplied"
        }
      ],
      "schema:name": "VOI Applied",
      "schema:value": "Full scan volume"
    }
  ],
  "ada:analyticalMode": [
    "Single-volume"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Sample A (olivine)",
  "ada:samplingUnitName": "Labelled: \"a single olivine phenocryst (1.0 mm large) separated from Sample A\" (p.2), hosting one silicate melt inclusion (Fig. 1, p.4)"
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

ex:labxctTAPP-detail-Richard2019 a schema1:Dataset,
        schema1:Product ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/voiApplied> ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Separated grain or crystal — \"a single olivine phenocryst (1.0 mm large) separated from Sample A\" (p.2); epoxy mounting \"carried out after HRXCT analysis\" (Fig. 1, p.4)" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/exposureTimePerProjection>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/framesAveragedPerProjection>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/numberOfProjections>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/outputBitDepth>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/phaseIdentificationMethod>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationMethod>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationThresholdValuesOrCriteria> ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Lab. de Microtomografía de Rayos X, UNAM, Mexico" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleDimensions> ;
                    schema1:name "Sample A (olivine)" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ bios:computationalTool [ a schema1:SoftwareApplication ;
                            schema1:name "ImageJ; Avizo 9.2" ;
                            ada:toolRole "dataReduction" ] ],
                [ schema1:instrument <https://example.org/labxctTAPP-detail-Richard2019/instrument/XCT> ] ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalMode "Single-volume" ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:sampleName "Sample A (olivine)" ;
    ada:samplingUnitName "Labelled: \"a single olivine phenocryst (1.0 mm large) separated from Sample A\" (p.2), hosting one silicate melt inclusion (Fig. 1, p.4)" ;
    ada:sessionIdentifier "missing" .

<https://example.org/labxctTAPP-detail-Richard2019/instrument/XCT> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/voxelSize> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "XCT" ;
    schema1:name "no value available: schema:name" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:description "30 kV" ;
    schema1:name "Accelerating Voltage" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/acceleratingVoltage> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 30 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> a schema1:PropertyValue ;
    schema1:name "Effective Spatial Resolution (PSF/MTF)" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> ;
    schema1:value "N — the paper's \"spatial resolution of 2.06 µm/px (8.7 µm³/vx)\" is the voxel size; no effective resolution reported" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/exposureTimePerProjection> a schema1:PropertyValue ;
    schema1:description "8 s" ;
    schema1:name "Exposure Time per Projection" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/exposureTimePerProjection> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 8 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/framesAveragedPerProjection> a schema1:PropertyValue ;
    schema1:description "~200 reference (blank) images taken; number of frames averaged per projection N" ;
    schema1:name "Frames Averaged per Projection" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/framesAveragedPerProjection> ;
    schema1:value 200 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/numberOfProjections> a schema1:PropertyValue ;
    schema1:name "Number of Projections" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/numberOfProjections> ;
    schema1:value 1601 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/outputBitDepth> a schema1:PropertyValue ;
    schema1:name "Output Bit Depth" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/outputBitDepth> ;
    schema1:value "32-bit (ZEISS XRM output)" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/phaseIdentificationMethod> a schema1:PropertyValue ;
    schema1:name "Phase Identification Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/phaseIdentificationMethod> ;
    schema1:value "Phase identified by grayscale contrast (vapor vs. silicate/mineral)" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleDimensions> a schema1:PropertyValue ;
    schema1:name "Sample Dimensions (L × W × H)" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleDimensions> ;
    schema1:value "~1 mm olivine" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationMethod> a schema1:PropertyValue ;
    schema1:name "Segmentation Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationMethod> ;
    schema1:value "Grayscale threshold range selection (ImageJ)" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationThresholdValuesOrCriteria> a schema1:PropertyValue ;
    schema1:name "Segmentation Threshold Values or Criteria" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationThresholdValuesOrCriteria> ;
    schema1:value "Threshold range selected to include all voxels of one phase while excluding adjacent phases; specific values N" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/voiApplied> a schema1:PropertyValue ;
    schema1:name "VOI Applied" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/voiApplied> ;
    schema1:value "Full scan volume" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/voxelSize> a schema1:PropertyValue ;
    schema1:description "2.06 µm/px" ;
    schema1:name "Voxel Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/voxelSize> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 2.06e+00 .


```


### detail example Richard2019-2
detail instance derived from Richard et al. 2019 (Chem. Geol.) Synthetic quartz (fluid incl.) Whole sample (low-res) Nikon XTH 320/225 U. Strathclyde.
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
  "@id": "ex:labxctTAPP-detail-Richard2019-2",
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
              "@id": "ada:parameter/labxctTAPP/sampleDimensions",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/labxctTAPP/sampleDimensions"
                }
              ],
              "schema:name": "Sample Dimensions (L × W × H)",
              "schema:value": "3 × 5 × 2 cm"
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
              "schema:value": "Optical photography of the sample showing the fluid inclusion array, with inclusions numbered for correspondence with the HRXCT reconstruction (Fig. 2)"
            }
          ],
          "schema:name": "Sample B (synthetic quartz)"
        }
      ],
      "prov:used": [
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "Avizo 9.2.0",
              "@type": [
                "schema:SoftwareApplication"
              ]
            }
          ]
        },
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "XCT",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/labxctTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 160,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "160 kV"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/tubeCurrent",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/tubeCurrent"
                    }
                  ],
                  "schema:name": "Tube Current",
                  "schema:value": 71,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "71 µA (Ag target)"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/xRayPreFilter",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/xRayPreFilter"
                    }
                  ],
                  "schema:name": "X-ray Pre-filter",
                  "schema:value": "None (conditions did not require filtering)"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/voxelSize",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/voxelSize"
                    }
                  ],
                  "schema:name": "Voxel Size",
                  "schema:value": 25,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "25 µm"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:labxctTAPP-detail-Richard2019-2/instrument/XCT"
            }
          ]
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/labxctTAPP/xRayPower",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/xRayPower"
            }
          ],
          "schema:name": "X-ray Power",
          "schema:value": 11.4,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "11.4 W"
        },
        {
          "@id": "ada:parameter/labxctTAPP/numberOfProjections",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/numberOfProjections"
            }
          ],
          "schema:name": "Number of Projections",
          "schema:value": 3141
        },
        {
          "@id": "ada:parameter/labxctTAPP/exposureTimePerProjection",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/exposureTimePerProjection"
            }
          ],
          "schema:name": "Exposure Time per Projection",
          "schema:value": 0.708,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "0.708 s"
        },
        {
          "@id": "ada:parameter/labxctTAPP/framesAveragedPerProjection",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/framesAveragedPerProjection"
            }
          ],
          "schema:name": "Frames Averaged per Projection",
          "schema:value": 1,
          "schema:description": "1 frame per projection"
        },
        {
          "@id": "ada:parameter/labxctTAPP/segmentationMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/segmentationMethod"
            }
          ],
          "schema:name": "Segmentation Method",
          "schema:value": "Manual grayscale threshold"
        },
        {
          "@id": "ada:parameter/labxctTAPP/segmentationThresholdValuesOrCriteria",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/segmentationThresholdValuesOrCriteria"
            }
          ],
          "schema:name": "Segmentation Threshold Values or Criteria",
          "schema:value": "Manual threshold: vapor = darker, liquid = brighter pixels; specific values N"
        },
        {
          "@id": "ada:parameter/labxctTAPP/phaseIdentificationMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/phaseIdentificationMethod"
            }
          ],
          "schema:name": "Phase Identification Method",
          "schema:value": "Phase identified by grayscale contrast (vapor darker, liquid brighter)"
        },
        {
          "@id": "ada:parameter/labxctTAPP/totalScanDuration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/totalScanDuration"
            }
          ],
          "schema:name": "Total Scan Duration",
          "schema:value": "37 min"
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "U. Strathclyde, Glasgow, UK"
      },
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Bulk specimen or fragment (as received) — Sample B, a 3 × 5 × 2 cm synthetic quartz monocrystal: \"No sectioning was carried out prior to HRXCT scanning\" (p.2)",
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
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/labxctTAPP/effectiveSpatialResolution",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/effectiveSpatialResolution"
        }
      ],
      "schema:name": "Effective Spatial Resolution (PSF/MTF)",
      "schema:value": "N — the paper's \"spatial resolution\" figures are given in µm/px with voxel volumes, i.e. the voxel size (25 µm); no effective resolution reported"
    },
    {
      "@id": "ada:parameter/labxctTAPP/voiApplied",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/voiApplied"
        }
      ],
      "schema:name": "VOI Applied",
      "schema:value": "Full scan volume"
    }
  ],
  "ada:analyticalMode": [
    "Single-volume"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Sample B (synthetic quartz)",
  "ada:samplingUnitName": "Labelled: \"Sample B was scanned both entirely and on a 1.4 × 1.4 × 1.4 mm region of interest\" (p.2) — this column is the whole-sample scan; its inclusions are numbered (\"#3\", Fig. 2, p.5)"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XCT/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:labxctTAPP-detail-Richard2019-2",
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
              "@id": "ada:parameter/labxctTAPP/sampleDimensions",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/labxctTAPP/sampleDimensions"
                }
              ],
              "schema:name": "Sample Dimensions (L \u00d7 W \u00d7 H)",
              "schema:value": "3 \u00d7 5 \u00d7 2 cm"
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
              "schema:value": "Optical photography of the sample showing the fluid inclusion array, with inclusions numbered for correspondence with the HRXCT reconstruction (Fig. 2)"
            }
          ],
          "schema:name": "Sample B (synthetic quartz)"
        }
      ],
      "prov:used": [
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "Avizo 9.2.0",
              "@type": [
                "schema:SoftwareApplication"
              ]
            }
          ]
        },
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "XCT",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/labxctTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 160,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "160 kV"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/tubeCurrent",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/tubeCurrent"
                    }
                  ],
                  "schema:name": "Tube Current",
                  "schema:value": 71,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "71 \u00b5A (Ag target)"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/xRayPreFilter",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/xRayPreFilter"
                    }
                  ],
                  "schema:name": "X-ray Pre-filter",
                  "schema:value": "None (conditions did not require filtering)"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/voxelSize",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/voxelSize"
                    }
                  ],
                  "schema:name": "Voxel Size",
                  "schema:value": 25,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "25 \u00b5m"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:labxctTAPP-detail-Richard2019-2/instrument/XCT"
            }
          ]
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/labxctTAPP/xRayPower",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/xRayPower"
            }
          ],
          "schema:name": "X-ray Power",
          "schema:value": 11.4,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "11.4 W"
        },
        {
          "@id": "ada:parameter/labxctTAPP/numberOfProjections",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/numberOfProjections"
            }
          ],
          "schema:name": "Number of Projections",
          "schema:value": 3141
        },
        {
          "@id": "ada:parameter/labxctTAPP/exposureTimePerProjection",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/exposureTimePerProjection"
            }
          ],
          "schema:name": "Exposure Time per Projection",
          "schema:value": 0.708,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "0.708 s"
        },
        {
          "@id": "ada:parameter/labxctTAPP/framesAveragedPerProjection",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/framesAveragedPerProjection"
            }
          ],
          "schema:name": "Frames Averaged per Projection",
          "schema:value": 1,
          "schema:description": "1 frame per projection"
        },
        {
          "@id": "ada:parameter/labxctTAPP/segmentationMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/segmentationMethod"
            }
          ],
          "schema:name": "Segmentation Method",
          "schema:value": "Manual grayscale threshold"
        },
        {
          "@id": "ada:parameter/labxctTAPP/segmentationThresholdValuesOrCriteria",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/segmentationThresholdValuesOrCriteria"
            }
          ],
          "schema:name": "Segmentation Threshold Values or Criteria",
          "schema:value": "Manual threshold: vapor = darker, liquid = brighter pixels; specific values N"
        },
        {
          "@id": "ada:parameter/labxctTAPP/phaseIdentificationMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/phaseIdentificationMethod"
            }
          ],
          "schema:name": "Phase Identification Method",
          "schema:value": "Phase identified by grayscale contrast (vapor darker, liquid brighter)"
        },
        {
          "@id": "ada:parameter/labxctTAPP/totalScanDuration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/totalScanDuration"
            }
          ],
          "schema:name": "Total Scan Duration",
          "schema:value": "37 min"
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "U. Strathclyde, Glasgow, UK"
      },
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Bulk specimen or fragment (as received) \u2014 Sample B, a 3 \u00d7 5 \u00d7 2 cm synthetic quartz monocrystal: \"No sectioning was carried out prior to HRXCT scanning\" (p.2)",
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
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/labxctTAPP/effectiveSpatialResolution",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/effectiveSpatialResolution"
        }
      ],
      "schema:name": "Effective Spatial Resolution (PSF/MTF)",
      "schema:value": "N \u2014 the paper's \"spatial resolution\" figures are given in \u00b5m/px with voxel volumes, i.e. the voxel size (25 \u00b5m); no effective resolution reported"
    },
    {
      "@id": "ada:parameter/labxctTAPP/voiApplied",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/voiApplied"
        }
      ],
      "schema:name": "VOI Applied",
      "schema:value": "Full scan volume"
    }
  ],
  "ada:analyticalMode": [
    "Single-volume"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Sample B (synthetic quartz)",
  "ada:samplingUnitName": "Labelled: \"Sample B was scanned both entirely and on a 1.4 \u00d7 1.4 \u00d7 1.4 mm region of interest\" (p.2) \u2014 this column is the whole-sample scan; its inclusions are numbered (\"#3\", Fig. 2, p.5)"
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

ex:labxctTAPP-detail-Richard2019-2 a schema1:Dataset,
        schema1:Product ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/voiApplied> ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Bulk specimen or fragment (as received) — Sample B, a 3 × 5 × 2 cm synthetic quartz monocrystal: \"No sectioning was carried out prior to HRXCT scanning\" (p.2)" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/exposureTimePerProjection>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/framesAveragedPerProjection>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/numberOfProjections>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/phaseIdentificationMethod>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationMethod>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationThresholdValuesOrCriteria>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/totalScanDuration>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayPower> ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "U. Strathclyde, Glasgow, UK" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleDimensions>,
                        <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
                    schema1:name "Sample B (synthetic quartz)" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ bios:computationalTool [ a schema1:SoftwareApplication ;
                            schema1:name "Avizo 9.2.0" ;
                            ada:toolRole "dataReduction" ] ],
                [ schema1:instrument <https://example.org/labxctTAPP-detail-Richard2019-2/instrument/XCT> ] ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalMode "Single-volume" ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:sampleName "Sample B (synthetic quartz)" ;
    ada:samplingUnitName "Labelled: \"Sample B was scanned both entirely and on a 1.4 × 1.4 × 1.4 mm region of interest\" (p.2) — this column is the whole-sample scan; its inclusions are numbered (\"#3\", Fig. 2, p.5)" ;
    ada:sessionIdentifier "missing" .

<https://example.org/labxctTAPP-detail-Richard2019-2/instrument/XCT> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/tubeCurrent>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/voxelSize>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayPreFilter> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "XCT" ;
    schema1:name "no value available: schema:name" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:description "160 kV" ;
    schema1:name "Accelerating Voltage" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/acceleratingVoltage> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 160 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> a schema1:PropertyValue ;
    schema1:name "Effective Spatial Resolution (PSF/MTF)" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> ;
    schema1:value "N — the paper's \"spatial resolution\" figures are given in µm/px with voxel volumes, i.e. the voxel size (25 µm); no effective resolution reported" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/exposureTimePerProjection> a schema1:PropertyValue ;
    schema1:description "0.708 s" ;
    schema1:name "Exposure Time per Projection" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/exposureTimePerProjection> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 7.08e-01 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/framesAveragedPerProjection> a schema1:PropertyValue ;
    schema1:description "1 frame per projection" ;
    schema1:name "Frames Averaged per Projection" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/framesAveragedPerProjection> ;
    schema1:value 1 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/numberOfProjections> a schema1:PropertyValue ;
    schema1:name "Number of Projections" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/numberOfProjections> ;
    schema1:value 3141 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/phaseIdentificationMethod> a schema1:PropertyValue ;
    schema1:name "Phase Identification Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/phaseIdentificationMethod> ;
    schema1:value "Phase identified by grayscale contrast (vapor darker, liquid brighter)" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleDimensions> a schema1:PropertyValue ;
    schema1:name "Sample Dimensions (L × W × H)" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleDimensions> ;
    schema1:value "3 × 5 × 2 cm" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationMethod> a schema1:PropertyValue ;
    schema1:name "Segmentation Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationMethod> ;
    schema1:value "Manual grayscale threshold" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationThresholdValuesOrCriteria> a schema1:PropertyValue ;
    schema1:name "Segmentation Threshold Values or Criteria" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationThresholdValuesOrCriteria> ;
    schema1:value "Manual threshold: vapor = darker, liquid = brighter pixels; specific values N" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/totalScanDuration> a schema1:PropertyValue ;
    schema1:name "Total Scan Duration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/totalScanDuration> ;
    schema1:value "37 min" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/tubeCurrent> a schema1:PropertyValue ;
    schema1:description "71 µA (Ag target)" ;
    schema1:name "Tube Current" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/tubeCurrent> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 71 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/voiApplied> a schema1:PropertyValue ;
    schema1:name "VOI Applied" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/voiApplied> ;
    schema1:value "Full scan volume" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/voxelSize> a schema1:PropertyValue ;
    schema1:description "25 µm" ;
    schema1:name "Voxel Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/voxelSize> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 25 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayPower> a schema1:PropertyValue ;
    schema1:description "11.4 W" ;
    schema1:name "X-ray Power" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayPower> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1.14e+01 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayPreFilter> a schema1:PropertyValue ;
    schema1:name "X-ray Pre-filter" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayPreFilter> ;
    schema1:value "None (conditions did not require filtering)" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "Optical photography of the sample showing the fluid inclusion array, with inclusions numbered for correspondence with the HRXCT reconstruction (Fig. 2)" .


```


### detail example Richard2019-3
detail instance derived from Richard et al. 2019 (Chem. Geol.) Synthetic quartz (fluid incl.) ROI scan (high-res) Nikon XTH 320/225 U. Strathclyde.
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
  "@id": "ex:labxctTAPP-detail-Richard2019-3",
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
              "@id": "ada:parameter/labxctTAPP/sampleDimensions",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/labxctTAPP/sampleDimensions"
                }
              ],
              "schema:name": "Sample Dimensions (L × W × H)",
              "schema:value": "3 × 5 × 2 cm"
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
              "schema:value": "Optical photography identifying the fluid inclusion array; inclusion #3 targeted for the high-resolution region-of-interest scan (Fig. 2)"
            }
          ],
          "schema:name": "Sample B (synthetic quartz)"
        }
      ],
      "prov:used": [
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "Avizo 9.2.0",
              "@type": [
                "schema:SoftwareApplication"
              ]
            }
          ]
        },
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "XCT",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/labxctTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 160,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "160 kV"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/tubeCurrent",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/tubeCurrent"
                    }
                  ],
                  "schema:name": "Tube Current",
                  "schema:value": 46,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "46 µA (Ag target)"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/xRayPreFilter",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/xRayPreFilter"
                    }
                  ],
                  "schema:name": "X-ray Pre-filter",
                  "schema:value": "None (conditions did not require filtering)"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/voxelSize",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/voxelSize"
                    }
                  ],
                  "schema:name": "Voxel Size",
                  "schema:value": 7.7,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "7.7 µm"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:labxctTAPP-detail-Richard2019-3/instrument/XCT"
            }
          ]
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/labxctTAPP/xRayPower",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/xRayPower"
            }
          ],
          "schema:name": "X-ray Power",
          "schema:value": 7.4,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "7.4 W"
        },
        {
          "@id": "ada:parameter/labxctTAPP/numberOfProjections",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/numberOfProjections"
            }
          ],
          "schema:name": "Number of Projections",
          "schema:value": 3141
        },
        {
          "@id": "ada:parameter/labxctTAPP/exposureTimePerProjection",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/exposureTimePerProjection"
            }
          ],
          "schema:name": "Exposure Time per Projection",
          "schema:value": 1.415,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "1.415 s"
        },
        {
          "@id": "ada:parameter/labxctTAPP/framesAveragedPerProjection",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/framesAveragedPerProjection"
            }
          ],
          "schema:name": "Frames Averaged per Projection",
          "schema:value": 1,
          "schema:description": "1 frame per projection"
        },
        {
          "@id": "ada:parameter/labxctTAPP/segmentationMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/segmentationMethod"
            }
          ],
          "schema:name": "Segmentation Method",
          "schema:value": "Manual grayscale threshold"
        },
        {
          "@id": "ada:parameter/labxctTAPP/segmentationThresholdValuesOrCriteria",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/segmentationThresholdValuesOrCriteria"
            }
          ],
          "schema:name": "Segmentation Threshold Values or Criteria",
          "schema:value": "Manual threshold: vapor = darker, liquid = brighter pixels; specific values N"
        },
        {
          "@id": "ada:parameter/labxctTAPP/phaseIdentificationMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/phaseIdentificationMethod"
            }
          ],
          "schema:name": "Phase Identification Method",
          "schema:value": "Phase identified by grayscale contrast (vapor darker, liquid brighter)"
        },
        {
          "@id": "ada:parameter/labxctTAPP/totalScanDuration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/totalScanDuration"
            }
          ],
          "schema:name": "Total Scan Duration",
          "schema:value": "75 min"
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "U. Strathclyde, Glasgow, UK"
      },
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Bulk specimen or fragment (as received) — Sample B, a 3 × 5 × 2 cm synthetic quartz monocrystal: \"No sectioning was carried out prior to HRXCT scanning\" (p.2)",
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
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/labxctTAPP/effectiveSpatialResolution",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/effectiveSpatialResolution"
        }
      ],
      "schema:name": "Effective Spatial Resolution (PSF/MTF)",
      "schema:value": "N — the paper's \"spatial resolution\" figures are given in µm/px with voxel volumes, i.e. the voxel size (7.7 µm); no effective resolution reported"
    },
    {
      "@id": "ada:parameter/labxctTAPP/voiApplied",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/voiApplied"
        }
      ],
      "schema:name": "VOI Applied",
      "schema:value": "Full scan volume"
    }
  ],
  "ada:analyticalMode": [
    "Single-volume"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Sample B (synthetic quartz)",
  "ada:samplingUnitName": "Labelled: the region-of-interest scan of Sample B, \"shown in Fig. 2 (fluid inclusion #3)\" (Table 1 note, p.3)"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XCT/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:labxctTAPP-detail-Richard2019-3",
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
              "@id": "ada:parameter/labxctTAPP/sampleDimensions",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/labxctTAPP/sampleDimensions"
                }
              ],
              "schema:name": "Sample Dimensions (L \u00d7 W \u00d7 H)",
              "schema:value": "3 \u00d7 5 \u00d7 2 cm"
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
              "schema:value": "Optical photography identifying the fluid inclusion array; inclusion #3 targeted for the high-resolution region-of-interest scan (Fig. 2)"
            }
          ],
          "schema:name": "Sample B (synthetic quartz)"
        }
      ],
      "prov:used": [
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "Avizo 9.2.0",
              "@type": [
                "schema:SoftwareApplication"
              ]
            }
          ]
        },
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "XCT",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/labxctTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 160,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "160 kV"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/tubeCurrent",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/tubeCurrent"
                    }
                  ],
                  "schema:name": "Tube Current",
                  "schema:value": 46,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "46 \u00b5A (Ag target)"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/xRayPreFilter",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/xRayPreFilter"
                    }
                  ],
                  "schema:name": "X-ray Pre-filter",
                  "schema:value": "None (conditions did not require filtering)"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/voxelSize",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/voxelSize"
                    }
                  ],
                  "schema:name": "Voxel Size",
                  "schema:value": 7.7,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "7.7 \u00b5m"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:labxctTAPP-detail-Richard2019-3/instrument/XCT"
            }
          ]
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/labxctTAPP/xRayPower",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/xRayPower"
            }
          ],
          "schema:name": "X-ray Power",
          "schema:value": 7.4,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "7.4 W"
        },
        {
          "@id": "ada:parameter/labxctTAPP/numberOfProjections",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/numberOfProjections"
            }
          ],
          "schema:name": "Number of Projections",
          "schema:value": 3141
        },
        {
          "@id": "ada:parameter/labxctTAPP/exposureTimePerProjection",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/exposureTimePerProjection"
            }
          ],
          "schema:name": "Exposure Time per Projection",
          "schema:value": 1.415,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "1.415 s"
        },
        {
          "@id": "ada:parameter/labxctTAPP/framesAveragedPerProjection",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/framesAveragedPerProjection"
            }
          ],
          "schema:name": "Frames Averaged per Projection",
          "schema:value": 1,
          "schema:description": "1 frame per projection"
        },
        {
          "@id": "ada:parameter/labxctTAPP/segmentationMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/segmentationMethod"
            }
          ],
          "schema:name": "Segmentation Method",
          "schema:value": "Manual grayscale threshold"
        },
        {
          "@id": "ada:parameter/labxctTAPP/segmentationThresholdValuesOrCriteria",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/segmentationThresholdValuesOrCriteria"
            }
          ],
          "schema:name": "Segmentation Threshold Values or Criteria",
          "schema:value": "Manual threshold: vapor = darker, liquid = brighter pixels; specific values N"
        },
        {
          "@id": "ada:parameter/labxctTAPP/phaseIdentificationMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/phaseIdentificationMethod"
            }
          ],
          "schema:name": "Phase Identification Method",
          "schema:value": "Phase identified by grayscale contrast (vapor darker, liquid brighter)"
        },
        {
          "@id": "ada:parameter/labxctTAPP/totalScanDuration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/totalScanDuration"
            }
          ],
          "schema:name": "Total Scan Duration",
          "schema:value": "75 min"
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "U. Strathclyde, Glasgow, UK"
      },
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Bulk specimen or fragment (as received) \u2014 Sample B, a 3 \u00d7 5 \u00d7 2 cm synthetic quartz monocrystal: \"No sectioning was carried out prior to HRXCT scanning\" (p.2)",
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
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/labxctTAPP/effectiveSpatialResolution",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/effectiveSpatialResolution"
        }
      ],
      "schema:name": "Effective Spatial Resolution (PSF/MTF)",
      "schema:value": "N \u2014 the paper's \"spatial resolution\" figures are given in \u00b5m/px with voxel volumes, i.e. the voxel size (7.7 \u00b5m); no effective resolution reported"
    },
    {
      "@id": "ada:parameter/labxctTAPP/voiApplied",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/voiApplied"
        }
      ],
      "schema:name": "VOI Applied",
      "schema:value": "Full scan volume"
    }
  ],
  "ada:analyticalMode": [
    "Single-volume"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Sample B (synthetic quartz)",
  "ada:samplingUnitName": "Labelled: the region-of-interest scan of Sample B, \"shown in Fig. 2 (fluid inclusion #3)\" (Table 1 note, p.3)"
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

ex:labxctTAPP-detail-Richard2019-3 a schema1:Dataset,
        schema1:Product ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/voiApplied> ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Bulk specimen or fragment (as received) — Sample B, a 3 × 5 × 2 cm synthetic quartz monocrystal: \"No sectioning was carried out prior to HRXCT scanning\" (p.2)" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/exposureTimePerProjection>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/framesAveragedPerProjection>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/numberOfProjections>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/phaseIdentificationMethod>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationMethod>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationThresholdValuesOrCriteria>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/totalScanDuration>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayPower> ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "U. Strathclyde, Glasgow, UK" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleDimensions>,
                        <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
                    schema1:name "Sample B (synthetic quartz)" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ schema1:instrument <https://example.org/labxctTAPP-detail-Richard2019-3/instrument/XCT> ],
                [ bios:computationalTool [ a schema1:SoftwareApplication ;
                            schema1:name "Avizo 9.2.0" ;
                            ada:toolRole "dataReduction" ] ] ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalMode "Single-volume" ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:sampleName "Sample B (synthetic quartz)" ;
    ada:samplingUnitName "Labelled: the region-of-interest scan of Sample B, \"shown in Fig. 2 (fluid inclusion #3)\" (Table 1 note, p.3)" ;
    ada:sessionIdentifier "missing" .

<https://example.org/labxctTAPP-detail-Richard2019-3/instrument/XCT> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/tubeCurrent>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/voxelSize>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayPreFilter> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "XCT" ;
    schema1:name "no value available: schema:name" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:description "160 kV" ;
    schema1:name "Accelerating Voltage" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/acceleratingVoltage> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 160 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> a schema1:PropertyValue ;
    schema1:name "Effective Spatial Resolution (PSF/MTF)" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> ;
    schema1:value "N — the paper's \"spatial resolution\" figures are given in µm/px with voxel volumes, i.e. the voxel size (7.7 µm); no effective resolution reported" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/exposureTimePerProjection> a schema1:PropertyValue ;
    schema1:description "1.415 s" ;
    schema1:name "Exposure Time per Projection" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/exposureTimePerProjection> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1.415e+00 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/framesAveragedPerProjection> a schema1:PropertyValue ;
    schema1:description "1 frame per projection" ;
    schema1:name "Frames Averaged per Projection" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/framesAveragedPerProjection> ;
    schema1:value 1 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/numberOfProjections> a schema1:PropertyValue ;
    schema1:name "Number of Projections" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/numberOfProjections> ;
    schema1:value 3141 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/phaseIdentificationMethod> a schema1:PropertyValue ;
    schema1:name "Phase Identification Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/phaseIdentificationMethod> ;
    schema1:value "Phase identified by grayscale contrast (vapor darker, liquid brighter)" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleDimensions> a schema1:PropertyValue ;
    schema1:name "Sample Dimensions (L × W × H)" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleDimensions> ;
    schema1:value "3 × 5 × 2 cm" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationMethod> a schema1:PropertyValue ;
    schema1:name "Segmentation Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationMethod> ;
    schema1:value "Manual grayscale threshold" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationThresholdValuesOrCriteria> a schema1:PropertyValue ;
    schema1:name "Segmentation Threshold Values or Criteria" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationThresholdValuesOrCriteria> ;
    schema1:value "Manual threshold: vapor = darker, liquid = brighter pixels; specific values N" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/totalScanDuration> a schema1:PropertyValue ;
    schema1:name "Total Scan Duration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/totalScanDuration> ;
    schema1:value "75 min" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/tubeCurrent> a schema1:PropertyValue ;
    schema1:description "46 µA (Ag target)" ;
    schema1:name "Tube Current" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/tubeCurrent> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 46 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/voiApplied> a schema1:PropertyValue ;
    schema1:name "VOI Applied" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/voiApplied> ;
    schema1:value "Full scan volume" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/voxelSize> a schema1:PropertyValue ;
    schema1:description "7.7 µm" ;
    schema1:name "Voxel Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/voxelSize> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 7.7e+00 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayPower> a schema1:PropertyValue ;
    schema1:description "7.4 W" ;
    schema1:name "X-ray Power" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayPower> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 7.4e+00 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayPreFilter> a schema1:PropertyValue ;
    schema1:name "X-ray Pre-filter" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayPreFilter> ;
    schema1:value "None (conditions did not require filtering)" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "Optical photography identifying the fluid inclusion array; inclusion #3 targeted for the high-resolution region-of-interest scan (Fig. 2)" .


```


### detail example Richard2019-4
detail instance derived from Richard et al. 2019 (Chem. Geol.) Fluid incl. minerals (C-I) Single-volume Phoenix Nanotom S U. Lorraine.
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
  "@id": "ex:labxctTAPP-detail-Richard2019-4",
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
              "@id": "ada:parameter/labxctTAPP/sampleDimensions",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/labxctTAPP/sampleDimensions"
                }
              ],
              "schema:name": "Sample Dimensions (L × W × H)",
              "schema:value": "Varies: 0.3×0.4 to 11×11×7 mm"
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
              "schema:value": "Optical microscopy under UV illumination, used to identify hydrocarbon-bearing phases within the inclusions (Fig. 9)"
            }
          ],
          "schema:name": "Samples C–I (various)"
        }
      ],
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "XCT",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/labxctTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 90,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "90–115 kV (varies by sample)"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/tubeCurrent",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/tubeCurrent"
                    }
                  ],
                  "schema:name": "Tube Current",
                  "schema:value": 65,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "65–115 µA (varies by sample)"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/voxelSize",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/voxelSize"
                    }
                  ],
                  "schema:name": "Voxel Size",
                  "schema:value": 0.77,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "0.77–3.5 µm (varies by sample)"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:labxctTAPP-detail-Richard2019-4/instrument/XCT"
            }
          ]
        },
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "Avizo 9.2.0",
              "@type": [
                "schema:SoftwareApplication"
              ]
            }
          ]
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/labxctTAPP/sourceToObjectDistance",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/sourceToObjectDistance"
            }
          ],
          "schema:name": "Source-to-Object Distance (SOD)",
          "schema:value": 6,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "6–55 mm (varies by sample)"
        },
        {
          "@id": "ada:parameter/labxctTAPP/numberOfProjections",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/numberOfProjections"
            }
          ],
          "schema:name": "Number of Projections",
          "schema:value": 1200,
          "schema:description": "1200–2000 (varies by sample)"
        },
        {
          "@id": "ada:parameter/labxctTAPP/exposureTimePerProjection",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/exposureTimePerProjection"
            }
          ],
          "schema:name": "Exposure Time per Projection",
          "schema:value": 750,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "750–1250 ms (varies by sample)"
        },
        {
          "@id": "ada:parameter/labxctTAPP/framesAveragedPerProjection",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/framesAveragedPerProjection"
            }
          ],
          "schema:name": "Frames Averaged per Projection",
          "schema:value": 3,
          "schema:description": "3–6 (varies by sample)"
        },
        {
          "@id": "ada:parameter/labxctTAPP/ringArtifactCorrectionMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/ringArtifactCorrectionMethod"
            }
          ],
          "schema:name": "Ring Artifact Correction Method",
          "schema:value": "Software ring artifact correction filter applied during analysis"
        },
        {
          "@id": "ada:parameter/labxctTAPP/segmentationMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/segmentationMethod"
            }
          ],
          "schema:name": "Segmentation Method",
          "schema:value": "Manual grayscale threshold per phase"
        },
        {
          "@id": "ada:parameter/labxctTAPP/segmentationThresholdValuesOrCriteria",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/segmentationThresholdValuesOrCriteria"
            }
          ],
          "schema:name": "Segmentation Threshold Values or Criteria",
          "schema:value": "Manual threshold per phase; specific values N"
        },
        {
          "@id": "ada:parameter/labxctTAPP/phaseIdentificationMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/phaseIdentificationMethod"
            }
          ],
          "schema:name": "Phase Identification Method",
          "schema:value": "Phases by grayscale contrast; minerals by differential attenuation"
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Université de Lorraine, France"
      },
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Polished section or chip; Bulk specimen or fragment (as received) — varies by sample. C: quartz lamella \"doubly polished to reach a 0.4 mm thickness for optical microscopy and HRXCT analyses\" (p.2). D, E: \"No sectioning was carried out prior to HRXCT scanning\", each scanned entirely (p.6). F: \"a chip (3×4×0.2 mm) of a doubly polished thick section\" (p.6). G, H: \"chips (5×5×0.5 mm) of doubly polished thick sections\" (p.6). I: \"a chip (3×4×0.15 mm) of a doubly polished thick section\" (p.7)",
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
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/labxctTAPP/effectiveSpatialResolution",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/effectiveSpatialResolution"
        }
      ],
      "schema:name": "Effective Spatial Resolution (PSF/MTF)",
      "schema:value": "N — the paper's \"spatial resolution\" figures are given in µm/px with voxel volumes, i.e. the voxel size (0.77–3.5 µm); no effective resolution reported"
    },
    {
      "@id": "ada:parameter/labxctTAPP/voiApplied",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/voiApplied"
        }
      ],
      "schema:name": "VOI Applied",
      "schema:value": "Full scan volume per sample"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Ring Artifact Severity and Correction Outcome",
      "dqv:value": "Software ring artifact correction applied; outcome not documented"
    },
    {
      "dqv:isMeasurementOf": "Cross-Validation Outcome",
      "dqv:value": "Sample I: CLSM gives φ_vap = 10±2%; XCT gives 9.8% — compatible"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Confocal laser scanning microscopy (Sample I)",
        "schema:description": "CLSM performed on same inclusion for volumetric cross-validation"
      }
    }
  ],
  "ada:analyticalMode": [
    "Single-volume"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Samples C–I (various)",
  "ada:samplingUnitName": "Labelled: \"Sample #\" C, D, E, F, G, H and I, each scanned on the Phoenix Nanotom S (Table 1, p.3)"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XCT/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:labxctTAPP-detail-Richard2019-4",
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
              "@id": "ada:parameter/labxctTAPP/sampleDimensions",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/labxctTAPP/sampleDimensions"
                }
              ],
              "schema:name": "Sample Dimensions (L \u00d7 W \u00d7 H)",
              "schema:value": "Varies: 0.3\u00d70.4 to 11\u00d711\u00d77 mm"
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
              "schema:value": "Optical microscopy under UV illumination, used to identify hydrocarbon-bearing phases within the inclusions (Fig. 9)"
            }
          ],
          "schema:name": "Samples C\u2013I (various)"
        }
      ],
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "XCT",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/labxctTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 90,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "90\u2013115 kV (varies by sample)"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/tubeCurrent",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/tubeCurrent"
                    }
                  ],
                  "schema:name": "Tube Current",
                  "schema:value": 65,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "65\u2013115 \u00b5A (varies by sample)"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/voxelSize",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/voxelSize"
                    }
                  ],
                  "schema:name": "Voxel Size",
                  "schema:value": 0.77,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "0.77\u20133.5 \u00b5m (varies by sample)"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:labxctTAPP-detail-Richard2019-4/instrument/XCT"
            }
          ]
        },
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "Avizo 9.2.0",
              "@type": [
                "schema:SoftwareApplication"
              ]
            }
          ]
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/labxctTAPP/sourceToObjectDistance",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/sourceToObjectDistance"
            }
          ],
          "schema:name": "Source-to-Object Distance (SOD)",
          "schema:value": 6,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "6\u201355 mm (varies by sample)"
        },
        {
          "@id": "ada:parameter/labxctTAPP/numberOfProjections",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/numberOfProjections"
            }
          ],
          "schema:name": "Number of Projections",
          "schema:value": 1200,
          "schema:description": "1200\u20132000 (varies by sample)"
        },
        {
          "@id": "ada:parameter/labxctTAPP/exposureTimePerProjection",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/exposureTimePerProjection"
            }
          ],
          "schema:name": "Exposure Time per Projection",
          "schema:value": 750,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "750\u20131250 ms (varies by sample)"
        },
        {
          "@id": "ada:parameter/labxctTAPP/framesAveragedPerProjection",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/framesAveragedPerProjection"
            }
          ],
          "schema:name": "Frames Averaged per Projection",
          "schema:value": 3,
          "schema:description": "3\u20136 (varies by sample)"
        },
        {
          "@id": "ada:parameter/labxctTAPP/ringArtifactCorrectionMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/ringArtifactCorrectionMethod"
            }
          ],
          "schema:name": "Ring Artifact Correction Method",
          "schema:value": "Software ring artifact correction filter applied during analysis"
        },
        {
          "@id": "ada:parameter/labxctTAPP/segmentationMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/segmentationMethod"
            }
          ],
          "schema:name": "Segmentation Method",
          "schema:value": "Manual grayscale threshold per phase"
        },
        {
          "@id": "ada:parameter/labxctTAPP/segmentationThresholdValuesOrCriteria",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/segmentationThresholdValuesOrCriteria"
            }
          ],
          "schema:name": "Segmentation Threshold Values or Criteria",
          "schema:value": "Manual threshold per phase; specific values N"
        },
        {
          "@id": "ada:parameter/labxctTAPP/phaseIdentificationMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/phaseIdentificationMethod"
            }
          ],
          "schema:name": "Phase Identification Method",
          "schema:value": "Phases by grayscale contrast; minerals by differential attenuation"
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Universit\u00e9 de Lorraine, France"
      },
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Polished section or chip; Bulk specimen or fragment (as received) \u2014 varies by sample. C: quartz lamella \"doubly polished to reach a 0.4 mm thickness for optical microscopy and HRXCT analyses\" (p.2). D, E: \"No sectioning was carried out prior to HRXCT scanning\", each scanned entirely (p.6). F: \"a chip (3\u00d74\u00d70.2 mm) of a doubly polished thick section\" (p.6). G, H: \"chips (5\u00d75\u00d70.5 mm) of doubly polished thick sections\" (p.6). I: \"a chip (3\u00d74\u00d70.15 mm) of a doubly polished thick section\" (p.7)",
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
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/labxctTAPP/effectiveSpatialResolution",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/effectiveSpatialResolution"
        }
      ],
      "schema:name": "Effective Spatial Resolution (PSF/MTF)",
      "schema:value": "N \u2014 the paper's \"spatial resolution\" figures are given in \u00b5m/px with voxel volumes, i.e. the voxel size (0.77\u20133.5 \u00b5m); no effective resolution reported"
    },
    {
      "@id": "ada:parameter/labxctTAPP/voiApplied",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/voiApplied"
        }
      ],
      "schema:name": "VOI Applied",
      "schema:value": "Full scan volume per sample"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Ring Artifact Severity and Correction Outcome",
      "dqv:value": "Software ring artifact correction applied; outcome not documented"
    },
    {
      "dqv:isMeasurementOf": "Cross-Validation Outcome",
      "dqv:value": "Sample I: CLSM gives \u03c6_vap = 10\u00b12%; XCT gives 9.8% \u2014 compatible"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Confocal laser scanning microscopy (Sample I)",
        "schema:description": "CLSM performed on same inclusion for volumetric cross-validation"
      }
    }
  ],
  "ada:analyticalMode": [
    "Single-volume"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Samples C\u2013I (various)",
  "ada:samplingUnitName": "Labelled: \"Sample #\" C, D, E, F, G, H and I, each scanned on the Phoenix Nanotom S (Table 1, p.3)"
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

ex:labxctTAPP-detail-Richard2019-4 a schema1:Dataset,
        schema1:Product ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/voiApplied> ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "CLSM performed on same inclusion for volumetric cross-validation" ;
                    schema1:name "Confocal laser scanning microscopy (Sample I)" ] ] ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Cross-Validation Outcome" ;
            dqv:value "Sample I: CLSM gives φ_vap = 10±2%; XCT gives 9.8% — compatible" ],
        [ dqv:isMeasurementOf "Ring Artifact Severity and Correction Outcome" ;
            dqv:value "Software ring artifact correction applied; outcome not documented" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Polished section or chip; Bulk specimen or fragment (as received) — varies by sample. C: quartz lamella \"doubly polished to reach a 0.4 mm thickness for optical microscopy and HRXCT analyses\" (p.2). D, E: \"No sectioning was carried out prior to HRXCT scanning\", each scanned entirely (p.6). F: \"a chip (3×4×0.2 mm) of a doubly polished thick section\" (p.6). G, H: \"chips (5×5×0.5 mm) of doubly polished thick sections\" (p.6). I: \"a chip (3×4×0.15 mm) of a doubly polished thick section\" (p.7)" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/exposureTimePerProjection>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/framesAveragedPerProjection>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/numberOfProjections>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/phaseIdentificationMethod>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/ringArtifactCorrectionMethod>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationMethod>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationThresholdValuesOrCriteria>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/sourceToObjectDistance> ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Université de Lorraine, France" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleDimensions>,
                        <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
                    schema1:name "Samples C–I (various)" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ schema1:instrument <https://example.org/labxctTAPP-detail-Richard2019-4/instrument/XCT> ],
                [ bios:computationalTool [ a schema1:SoftwareApplication ;
                            schema1:name "Avizo 9.2.0" ;
                            ada:toolRole "dataReduction" ] ] ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalMode "Single-volume" ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:sampleName "Samples C–I (various)" ;
    ada:samplingUnitName "Labelled: \"Sample #\" C, D, E, F, G, H and I, each scanned on the Phoenix Nanotom S (Table 1, p.3)" ;
    ada:sessionIdentifier "missing" .

<https://example.org/labxctTAPP-detail-Richard2019-4/instrument/XCT> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/tubeCurrent>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/voxelSize> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "XCT" ;
    schema1:name "no value available: schema:name" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:description "90–115 kV (varies by sample)" ;
    schema1:name "Accelerating Voltage" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/acceleratingVoltage> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 90 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> a schema1:PropertyValue ;
    schema1:name "Effective Spatial Resolution (PSF/MTF)" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> ;
    schema1:value "N — the paper's \"spatial resolution\" figures are given in µm/px with voxel volumes, i.e. the voxel size (0.77–3.5 µm); no effective resolution reported" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/exposureTimePerProjection> a schema1:PropertyValue ;
    schema1:description "750–1250 ms (varies by sample)" ;
    schema1:name "Exposure Time per Projection" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/exposureTimePerProjection> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 750 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/framesAveragedPerProjection> a schema1:PropertyValue ;
    schema1:description "3–6 (varies by sample)" ;
    schema1:name "Frames Averaged per Projection" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/framesAveragedPerProjection> ;
    schema1:value 3 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/numberOfProjections> a schema1:PropertyValue ;
    schema1:description "1200–2000 (varies by sample)" ;
    schema1:name "Number of Projections" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/numberOfProjections> ;
    schema1:value 1200 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/phaseIdentificationMethod> a schema1:PropertyValue ;
    schema1:name "Phase Identification Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/phaseIdentificationMethod> ;
    schema1:value "Phases by grayscale contrast; minerals by differential attenuation" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/ringArtifactCorrectionMethod> a schema1:PropertyValue ;
    schema1:name "Ring Artifact Correction Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/ringArtifactCorrectionMethod> ;
    schema1:value "Software ring artifact correction filter applied during analysis" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleDimensions> a schema1:PropertyValue ;
    schema1:name "Sample Dimensions (L × W × H)" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleDimensions> ;
    schema1:value "Varies: 0.3×0.4 to 11×11×7 mm" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationMethod> a schema1:PropertyValue ;
    schema1:name "Segmentation Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationMethod> ;
    schema1:value "Manual grayscale threshold per phase" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationThresholdValuesOrCriteria> a schema1:PropertyValue ;
    schema1:name "Segmentation Threshold Values or Criteria" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationThresholdValuesOrCriteria> ;
    schema1:value "Manual threshold per phase; specific values N" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/sourceToObjectDistance> a schema1:PropertyValue ;
    schema1:description "6–55 mm (varies by sample)" ;
    schema1:name "Source-to-Object Distance (SOD)" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/sourceToObjectDistance> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 6 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/tubeCurrent> a schema1:PropertyValue ;
    schema1:description "65–115 µA (varies by sample)" ;
    schema1:name "Tube Current" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/tubeCurrent> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 65 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/voiApplied> a schema1:PropertyValue ;
    schema1:name "VOI Applied" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/voiApplied> ;
    schema1:value "Full scan volume per sample" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/voxelSize> a schema1:PropertyValue ;
    schema1:description "0.77–3.5 µm (varies by sample)" ;
    schema1:name "Voxel Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/voxelSize> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 7.7e-01 .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "Optical microscopy under UV illumination, used to identify hydrocarbon-bearing phases within the inclusions (Fig. 9)" .


```


### detail example Tait2014
detail instance derived from Tait 2014 (Thesis) Watson 012 H7 chondrite Single-volume XRADIA XRM500 CSIRO Kensington.
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
  "@id": "ex:labxctTAPP-detail-Tait2014",
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
              "@id": "ada:parameter/labxctTAPP/sampleDimensions",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/labxctTAPP/sampleDimensions"
                }
              ],
              "schema:name": "Sample Dimensions (L × W × H)",
              "schema:value": "8 mm diameter core"
            }
          ],
          "schema:name": "Watson 012"
        }
      ],
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "XCT",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/labxctTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 70,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "70 kV"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/tubeCurrent",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/tubeCurrent"
                    }
                  ],
                  "schema:name": "Tube Current",
                  "schema:value": 86,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "86 µA"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/voxelSize",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/voxelSize"
                    }
                  ],
                  "schema:name": "Voxel Size",
                  "schema:value": 1.923,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "1.923 µm"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:labxctTAPP-detail-Tait2014/instrument/XCT"
            }
          ]
        },
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "AvizoFire 8.0; Matlab; Drishti 2.0",
              "@type": [
                "schema:SoftwareApplication"
              ]
            }
          ]
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/labxctTAPP/xRayPower",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/xRayPower"
            }
          ],
          "schema:name": "X-ray Power",
          "schema:value": 7,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "7 W"
        },
        {
          "@id": "ada:parameter/labxctTAPP/rotationRange",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/rotationRange"
            }
          ],
          "schema:name": "Rotation Range",
          "schema:value": 360,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "360°"
        },
        {
          "@id": "ada:parameter/labxctTAPP/numberOfProjections",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/numberOfProjections"
            }
          ],
          "schema:name": "Number of Projections",
          "schema:value": 2000
        },
        {
          "@id": "ada:parameter/labxctTAPP/segmentationMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/segmentationMethod"
            }
          ],
          "schema:name": "Segmentation Method",
          "schema:value": "Dedicated workflow (Godel 2013) modified for plagioclase network segmentation"
        },
        {
          "@id": "ada:parameter/labxctTAPP/segmentationThresholdValuesOrCriteria",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/segmentationThresholdValuesOrCriteria"
            }
          ],
          "schema:name": "Segmentation Threshold Values or Criteria",
          "schema:value": "Dedicated workflow; specific threshold values N"
        },
        {
          "@id": "ada:parameter/labxctTAPP/phaseIdentificationMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/phaseIdentificationMethod"
            }
          ],
          "schema:name": "Phase Identification Method",
          "schema:value": "Plagioclase targeted; olivine + pyroxene not separately resolved; troilite/oxyhydroxide indistinguishable"
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "CSIRO, Kensington, Western Australia"
      },
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Core or trimmed billet — \"An 8 mm diameter core was drilled from the Watson 012 sample and then scanned\" (p.9)",
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
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/labxctTAPP/effectiveSpatialResolution",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/effectiveSpatialResolution"
        }
      ],
      "schema:name": "Effective Spatial Resolution (PSF/MTF)",
      "schema:value": "N — voxel size only (1.923 µm); no spatial resolution reported"
    },
    {
      "@id": "ada:parameter/labxctTAPP/voiApplied",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/voiApplied"
        }
      ],
      "schema:name": "VOI Applied",
      "schema:value": "Full 8 mm core volume"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Cross-Validation Outcome",
      "dqv:value": "XCT qualitatively compared with thin sections and EBSD; cm-scale plagioclase confirmed"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Optical microscopy; EBSD",
        "schema:description": "XCT qualitatively compared with thin sections and EBSD"
      }
    }
  ],
  "ada:analyticalMode": [
    "Single-volume"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Watson 012",
  "ada:samplingUnitName": "Sample name only — \"An 8 mm diameter core was drilled from the Watson 012 sample and then scanned\" (p.9); not otherwise labelled"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XCT/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:labxctTAPP-detail-Tait2014",
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
              "@id": "ada:parameter/labxctTAPP/sampleDimensions",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/labxctTAPP/sampleDimensions"
                }
              ],
              "schema:name": "Sample Dimensions (L \u00d7 W \u00d7 H)",
              "schema:value": "8 mm diameter core"
            }
          ],
          "schema:name": "Watson 012"
        }
      ],
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "XCT",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/labxctTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 70,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "70 kV"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/tubeCurrent",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/tubeCurrent"
                    }
                  ],
                  "schema:name": "Tube Current",
                  "schema:value": 86,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "86 \u00b5A"
                },
                {
                  "@id": "ada:parameter/labxctTAPP/voxelSize",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/labxctTAPP/voxelSize"
                    }
                  ],
                  "schema:name": "Voxel Size",
                  "schema:value": 1.923,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "1.923 \u00b5m"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:labxctTAPP-detail-Tait2014/instrument/XCT"
            }
          ]
        },
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "AvizoFire 8.0; Matlab; Drishti 2.0",
              "@type": [
                "schema:SoftwareApplication"
              ]
            }
          ]
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/labxctTAPP/xRayPower",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/xRayPower"
            }
          ],
          "schema:name": "X-ray Power",
          "schema:value": 7,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "7 W"
        },
        {
          "@id": "ada:parameter/labxctTAPP/rotationRange",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/rotationRange"
            }
          ],
          "schema:name": "Rotation Range",
          "schema:value": 360,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "360\u00b0"
        },
        {
          "@id": "ada:parameter/labxctTAPP/numberOfProjections",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/numberOfProjections"
            }
          ],
          "schema:name": "Number of Projections",
          "schema:value": 2000
        },
        {
          "@id": "ada:parameter/labxctTAPP/segmentationMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/segmentationMethod"
            }
          ],
          "schema:name": "Segmentation Method",
          "schema:value": "Dedicated workflow (Godel 2013) modified for plagioclase network segmentation"
        },
        {
          "@id": "ada:parameter/labxctTAPP/segmentationThresholdValuesOrCriteria",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/segmentationThresholdValuesOrCriteria"
            }
          ],
          "schema:name": "Segmentation Threshold Values or Criteria",
          "schema:value": "Dedicated workflow; specific threshold values N"
        },
        {
          "@id": "ada:parameter/labxctTAPP/phaseIdentificationMethod",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/labxctTAPP/phaseIdentificationMethod"
            }
          ],
          "schema:name": "Phase Identification Method",
          "schema:value": "Plagioclase targeted; olivine + pyroxene not separately resolved; troilite/oxyhydroxide indistinguishable"
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "CSIRO, Kensington, Western Australia"
      },
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "Core or trimmed billet \u2014 \"An 8 mm diameter core was drilled from the Watson 012 sample and then scanned\" (p.9)",
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
      "schema:startTime": "no value available: schema:startTime"
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/labxctTAPP/effectiveSpatialResolution",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/effectiveSpatialResolution"
        }
      ],
      "schema:name": "Effective Spatial Resolution (PSF/MTF)",
      "schema:value": "N \u2014 voxel size only (1.923 \u00b5m); no spatial resolution reported"
    },
    {
      "@id": "ada:parameter/labxctTAPP/voiApplied",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/voiApplied"
        }
      ],
      "schema:name": "VOI Applied",
      "schema:value": "Full 8 mm core volume"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Cross-Validation Outcome",
      "dqv:value": "XCT qualitatively compared with thin sections and EBSD; cm-scale plagioclase confirmed"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Optical microscopy; EBSD",
        "schema:description": "XCT qualitatively compared with thin sections and EBSD"
      }
    }
  ],
  "ada:analyticalMode": [
    "Single-volume"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Watson 012",
  "ada:samplingUnitName": "Sample name only \u2014 \"An 8 mm diameter core was drilled from the Watson 012 sample and then scanned\" (p.9); not otherwise labelled"
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

ex:labxctTAPP-detail-Tait2014 a schema1:Dataset,
        schema1:Product ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/voiApplied> ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "XCT qualitatively compared with thin sections and EBSD" ;
                    schema1:name "Optical microscopy; EBSD" ] ] ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Cross-Validation Outcome" ;
            dqv:value "XCT qualitatively compared with thin sections and EBSD; cm-scale plagioclase confirmed" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Core or trimmed billet — \"An 8 mm diameter core was drilled from the Watson 012 sample and then scanned\" (p.9)" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/numberOfProjections>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/phaseIdentificationMethod>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/rotationRange>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationMethod>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationThresholdValuesOrCriteria>,
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayPower> ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "CSIRO, Kensington, Western Australia" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleDimensions> ;
                    schema1:name "Watson 012" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ bios:computationalTool [ a schema1:SoftwareApplication ;
                            schema1:name "AvizoFire 8.0; Matlab; Drishti 2.0" ;
                            ada:toolRole "dataReduction" ] ],
                [ schema1:instrument <https://example.org/labxctTAPP-detail-Tait2014/instrument/XCT> ] ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalMode "Single-volume" ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:sampleName "Watson 012" ;
    ada:samplingUnitName "Sample name only — \"An 8 mm diameter core was drilled from the Watson 012 sample and then scanned\" (p.9); not otherwise labelled" ;
    ada:sessionIdentifier "missing" .

<https://example.org/labxctTAPP-detail-Tait2014/instrument/XCT> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/tubeCurrent>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/voxelSize> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "XCT" ;
    schema1:name "no value available: schema:name" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:description "70 kV" ;
    schema1:name "Accelerating Voltage" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/acceleratingVoltage> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 70 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> a schema1:PropertyValue ;
    schema1:name "Effective Spatial Resolution (PSF/MTF)" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> ;
    schema1:value "N — voxel size only (1.923 µm); no spatial resolution reported" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/numberOfProjections> a schema1:PropertyValue ;
    schema1:name "Number of Projections" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/numberOfProjections> ;
    schema1:value 2000 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/phaseIdentificationMethod> a schema1:PropertyValue ;
    schema1:name "Phase Identification Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/phaseIdentificationMethod> ;
    schema1:value "Plagioclase targeted; olivine + pyroxene not separately resolved; troilite/oxyhydroxide indistinguishable" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/rotationRange> a schema1:PropertyValue ;
    schema1:description "360°" ;
    schema1:name "Rotation Range" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/rotationRange> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 360 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleDimensions> a schema1:PropertyValue ;
    schema1:name "Sample Dimensions (L × W × H)" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleDimensions> ;
    schema1:value "8 mm diameter core" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationMethod> a schema1:PropertyValue ;
    schema1:name "Segmentation Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationMethod> ;
    schema1:value "Dedicated workflow (Godel 2013) modified for plagioclase network segmentation" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationThresholdValuesOrCriteria> a schema1:PropertyValue ;
    schema1:name "Segmentation Threshold Values or Criteria" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationThresholdValuesOrCriteria> ;
    schema1:value "Dedicated workflow; specific threshold values N" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/tubeCurrent> a schema1:PropertyValue ;
    schema1:description "86 µA" ;
    schema1:name "Tube Current" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/tubeCurrent> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 86 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/voiApplied> a schema1:PropertyValue ;
    schema1:name "VOI Applied" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/voiApplied> ;
    schema1:value "Full 8 mm core volume" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/voxelSize> a schema1:PropertyValue ;
    schema1:description "1.923 µm" ;
    schema1:name "Voxel Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/voxelSize> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1.923e+00 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayPower> a schema1:PropertyValue ;
    schema1:description "7 W" ;
    schema1:name "X-ray Power" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayPower> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 7 .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Lab-XCT Analysis Detail
description: Detail block for Lab-XCT hasPart items. Discriminates on ada:componentType,
  carries analysis-level required properties and an @id reference to a registered
  labxctTAPP definition, and per-dataset schema:additionalProperty entries constrained
  via $refs to the parameterValues registry plus a catch-all. Generated by tools/build_tapp.py.
allOf:
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/AnalysisIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/calibrationFactor/schema.yaml#/$defs/AnalysisIdentification
- type: object
  properties:
    prov:wasGeneratedBy:
      type: array
      items:
        type: object
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
                        anyOf:
                        - title: "Sample Dimensions (L \xD7 W \xD7 H)"
                          description: "Physical dimensions of the sample in mm, reported
                            as length \xD7 width \xD7 height (or equivalent three
                            orthogonal measurements)."
                          type: object
                          properties:
                            '@id':
                              const: ada:parameter/labxctTAPP/sampleDimensions
                            '@type':
                              const:
                              - schema:PropertyValue
                            schema:propertyID:
                              const:
                              - '@id': ada:parameter/labxctTAPP/sampleDimensions
                            schema:name:
                              const: "Sample Dimensions (L \xD7 W \xD7 H)"
                            schema:value:
                              type: string
                          required:
                          - '@id'
                          - '@type'
                          - schema:propertyID
                          - schema:name
                          - schema:value
                        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Analysis_preAnalysisImagingAndScreening
                        - title: Sample Mass
                          description: Mass of the sample in grams, recorded for curatorial
                            tracking of precious or limited materials.
                          type: object
                          properties:
                            '@id':
                              const: ada:parameter/labxctTAPP/sampleMass
                            '@type':
                              const:
                              - schema:PropertyValue
                            schema:propertyID:
                              const:
                              - '@id': ada:parameter/labxctTAPP/sampleMass
                            schema:name:
                              const: Sample Mass
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
                          title: "Sample Dimensions (L \xD7 W \xD7 H)"
                          description: "Physical dimensions of the sample in mm, reported
                            as length \xD7 width \xD7 height (or equivalent three
                            orthogonal measurements)."
                          type: object
                          properties:
                            '@id':
                              const: ada:parameter/labxctTAPP/sampleDimensions
                            '@type':
                              const:
                              - schema:PropertyValue
                            schema:propertyID:
                              const:
                              - '@id': ada:parameter/labxctTAPP/sampleDimensions
                            schema:name:
                              const: "Sample Dimensions (L \xD7 W \xD7 H)"
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
                          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Analysis_preAnalysisImagingAndScreening
                        minContains: 0
                        maxContains: 1
                      - contains:
                          title: Sample Mass
                          description: Mass of the sample in grams, recorded for curatorial
                            tracking of precious or limited materials.
                          type: object
                          properties:
                            '@id':
                              const: ada:parameter/labxctTAPP/sampleMass
                            '@type':
                              const:
                              - schema:PropertyValue
                            schema:propertyID:
                              const:
                              - '@id': ada:parameter/labxctTAPP/sampleMass
                            schema:name:
                              const: Sample Mass
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
          schema:additionalProperty:
            type: array
            items:
              anyOf:
              - title: Sample Mounting Method
                description: "Method used to mount or hold the sample on the instrument
                  rotation stage. Mounting material should transmit X-rays at the
                  selected voltage without dominating beam attenuation. Report the
                  holder CLASS from the list and name the specific vessel or material
                  alongside it \u2014 'Tube or vial \u2014 1 cm plastic straw', not
                  'Tube or vial'. Where the sample is sealed or bagged inside a further
                  holder for contamination control, record both layers. Report any
                  adhesive, support material and alignment aids used."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/labxctTAPP/sampleMountingMethod
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/labxctTAPP/sampleMountingMethod
                  schema:name:
                    const: Sample Mounting Method
                  schema:value:
                    type: string
                  schema:inDefinedTermSet:
                    const:
                      '@id': ada:vocab/sample-mounting-method
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              - title: X-ray Power
                description: "X-ray tube power in watts (W). Derivable as voltage
                  (kV) \xD7 current (mA) = kV \xD7 \xB5A / 1000. If power was varied
                  across samples within the session, report the full range applied
                  (e.g., 7\u201313 W)."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/labxctTAPP/xRayPower
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/labxctTAPP/xRayPower
                  schema:name:
                    const: X-ray Power
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
              - title: Source-to-Object Distance (SOD)
                description: Distance from the X-ray source focal spot to the centre
                  of the sample rotation axis, in mm.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/labxctTAPP/sourceToObjectDistance
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/labxctTAPP/sourceToObjectDistance
                  schema:name:
                    const: Source-to-Object Distance (SOD)
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
              - title: Source-to-Detector Distance (SDD)
                description: "Distance from the X-ray source focal spot to the detector
                  surface, in mm. Voxel size \u2248 detector pixel size / M (before
                  binning; divide additionally by optical objective for Versa-class
                  systems)."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/labxctTAPP/sourceToDetectorDistance
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/labxctTAPP/sourceToDetectorDistance
                  schema:name:
                    const: Source-to-Detector Distance (SDD)
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
              - title: Rotation Range
                description: Total angular range over which projection images are
                  acquired, in degrees.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/labxctTAPP/rotationRange
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/labxctTAPP/rotationRange
                  schema:name:
                    const: Rotation Range
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
              - title: Number of Projections
                description: Total number of equally-spaced projection images acquired
                  over the full rotation range. For Mode B (multi-volume stitching),
                  this is the number per sub-volume.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/labxctTAPP/numberOfProjections
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/labxctTAPP/numberOfProjections
                  schema:name:
                    const: Number of Projections
                  schema:value:
                    anyOf:
                    - type: number
                    - type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              - title: Rotation Step Size
                description: Angular increment between successive projection images,
                  in degrees. Equal to Rotation Range divided by Number of Projections
                  when both are reported; however, some sources report step size as
                  the primary rotation parameter without stating the total number
                  of projections explicitly.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/labxctTAPP/rotationStepSize
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/labxctTAPP/rotationStepSize
                  schema:name:
                    const: Rotation Step Size
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
              - title: Exposure Time per Projection
                description: "Duration of X-ray exposure for each individual projection
                  image frame, in seconds. Adjustment is warranted for samples that
                  are unusually dense or unusually transparent. If the exposure time
                  was varied across samples within the same procedure or session,
                  report the full range applied (e.g., 0.5\u20132 s)."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/labxctTAPP/exposureTimePerProjection
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/labxctTAPP/exposureTimePerProjection
                  schema:name:
                    const: Exposure Time per Projection
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
              - title: Frames Averaged per Projection
                description: "Number of individual detector frames acquired and averaged
                  to produce each saved projection image. The effective exposure per
                  projection = exposure time per frame \xD7 frames averaged."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/labxctTAPP/framesAveragedPerProjection
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/labxctTAPP/framesAveragedPerProjection
                  schema:name:
                    const: Frames Averaged per Projection
                  schema:value:
                    anyOf:
                    - type: number
                    - type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              - title: Detector Binning
                description: "Detector pixel binning factor applied during acquisition.
                  Binning combines adjacent pixels (e.g., 2\xD72 combines 4 pixels
                  into one)."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/labxctTAPP/detectorBinning
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/labxctTAPP/detectorBinning
                  schema:name:
                    const: Detector Binning
                  schema:value:
                    type: string
                  schema:inDefinedTermSet:
                    const:
                      '@id': ada:vocab/detector-binning
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              - title: Rotation Mode
                description: Whether projection images are acquired during continuous
                  sample rotation (faster; may introduce slight motion blur at high
                  rotation speeds) or at discrete step positions with the stage stationary
                  during each exposure (stop-and-shoot; eliminates motion blur).
                type: object
                properties:
                  '@id':
                    const: ada:parameter/labxctTAPP/rotationMode
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/labxctTAPP/rotationMode
                  schema:name:
                    const: Rotation Mode
                  schema:value:
                    type: string
                  schema:inDefinedTermSet:
                    const:
                      '@id': ada:vocab/rotation-mode
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Analysis_samplingUnitSelectionCriteria
              - title: Reconstruction Convolution Filter
                description: Convolution (apodization) filter kernel applied during
                  back-projection reconstruction.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/labxctTAPP/reconstructionConvolutionFilter
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/labxctTAPP/reconstructionConvolutionFilter
                  schema:name:
                    const: Reconstruction Convolution Filter
                  schema:value:
                    type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              - title: Beam Hardening Correction Parameter
                description: Numerical value or setting applied in the software beam
                  hardening correction algorithm for this specific analysis. Companion
                  to Beam Hardening Correction Method.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/labxctTAPP/beamHardeningCorrectionParameter
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/labxctTAPP/beamHardeningCorrectionParameter
                  schema:name:
                    const: Beam Hardening Correction Parameter
                  schema:value:
                    type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              - title: Ring Artifact Correction Method
                description: Procedure specification for how ring artifacts are handled.
                  Whether correction was applied and its outcome are recorded separately
                  in Group 6.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/labxctTAPP/ringArtifactCorrectionMethod
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/labxctTAPP/ringArtifactCorrectionMethod
                  schema:name:
                    const: Ring Artifact Correction Method
                  schema:value:
                    type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              - title: CT Number Calibration
                description: Whether the raw CT grayscale values have been calibrated
                  to physically meaningful units using reference materials.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/labxctTAPP/ctNumberCalibration
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/labxctTAPP/ctNumberCalibration
                  schema:name:
                    const: CT Number Calibration
                  schema:value:
                    type: string
                  schema:inDefinedTermSet:
                    const:
                      '@id': ada:vocab/ct-number-calibration
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
                    const: ada:parameter/labxctTAPP/segmentationMethod
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/labxctTAPP/segmentationMethod
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
              - title: Segmentation Threshold Values or Criteria
                description: "Specific CT number range(s) or quantitative criteria
                  used to define each segmented phase or feature. For LAC-calibrated
                  datasets, report values in cm\u207B\xB9."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/labxctTAPP/segmentationThresholdValuesOrCriteria
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/labxctTAPP/segmentationThresholdValuesOrCriteria
                  schema:name:
                    const: Segmentation Threshold Values or Criteria
                  schema:value:
                    type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              - title: Phase Identification Method
                description: Method used to assign reconstructed CT number ranges
                  to specific mineral phases or material types. Approaches include
                  comparison to calculated linear attenuation coefficients (LAC),
                  cross-validation with independent analytical techniques, or empirical
                  calibration.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/labxctTAPP/phaseIdentificationMethod
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/labxctTAPP/phaseIdentificationMethod
                  schema:name:
                    const: Phase Identification Method
                  schema:value:
                    type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              - title: VOI Selection Criteria
                description: Rules specifying how the Volume of Interest (VOI) is
                  to be defined for quantitative analysis. Common criteria exclude
                  cone-beam artifact zones at sample edges, beam hardening halos near
                  dense inclusions, and sample holder signal. The actual VOI applied
                  in a specific analysis is recorded separately at analysis level.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/labxctTAPP/voiSelectionCriteria
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/labxctTAPP/voiSelectionCriteria
                  schema:name:
                    const: VOI Selection Criteria
                  schema:value:
                    type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              - title: Output Bit Depth
                description: Bit depth of the reconstructed 3D volume (number of bits
                  used to encode each voxel's grayscale value). Common values are
                  8-bit (256 gray levels), 16-bit (65,536 gray levels), or 32-bit
                  floating point. A required output bit depth may be specified if
                  downstream analysis workflows depend on a consistent grayscale range.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/labxctTAPP/outputBitDepth
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/labxctTAPP/outputBitDepth
                  schema:name:
                    const: Output Bit Depth
                  schema:value:
                    type: string
                  schema:inDefinedTermSet:
                    const:
                      '@id': ada:vocab/output-bit-depth
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              - title: Total Scan Duration
                description: Total elapsed time for the complete XCT acquisition,
                  from the start of the first projection to the end of the last. For
                  multi-volume acquisitions, this is the combined scan time across
                  all sub-volumes (not including setup or reconstruction time).
                type: object
                properties:
                  '@id':
                    const: ada:parameter/labxctTAPP/totalScanDuration
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/labxctTAPP/totalScanDuration
                  schema:name:
                    const: Total Scan Duration
                  schema:value:
                    type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              - title: Partial Volume Effect Criteria
                description: "Specification of how partial volume effects (PVE) are
                  managed in quantitative analysis. PVE correction can be implemented
                  via PSF-based deconvolution tools such as Blob3D. Record the minimum
                  feature size criterion adopted for the procedure (in voxels or \xB5m),
                  the basis for it, the treatment of boundary voxels in modal abundance
                  or size distribution calculations, and whether PVE correction is
                  required or optional. State whether the criterion follows the Withers
                  et al. (2021) convention \u2014 a feature must span at least 3 voxels
                  to be positively identified and at least 10 for reliable shape and
                  volume characterisation \u2014 or is SNR-limited, PVE-limited or
                  analyst-defined."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/labxctTAPP/partialVolumeEffectCriteria
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/labxctTAPP/partialVolumeEffectCriteria
                  schema:name:
                    const: Partial Volume Effect Criteria
                  schema:value:
                    type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              - title: Cross-Validation Procedure Requirement
                description: Specification of what independent analytical validation
                  is required to confirm CT segmentation results, phase identification,
                  or quantitative measurements. Common approaches include BSE imaging,
                  SEM-EDS or EPMA modal analysis, He pycnometry for bulk porosity,
                  and Raman or SIMS phase mapping. Record the required validation
                  method(s) and the sampling fraction (e.g., every sample, one per
                  session, or a representative subset).
                type: object
                properties:
                  '@id':
                    const: ada:parameter/labxctTAPP/crossValidationProcedureRequirement
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/labxctTAPP/crossValidationProcedureRequirement
                  schema:name:
                    const: Cross-Validation Procedure Requirement
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
                title: Sample Mounting Method
                description: "Method used to mount or hold the sample on the instrument
                  rotation stage. Mounting material should transmit X-rays at the
                  selected voltage without dominating beam attenuation. Report the
                  holder CLASS from the list and name the specific vessel or material
                  alongside it \u2014 'Tube or vial \u2014 1 cm plastic straw', not
                  'Tube or vial'. Where the sample is sealed or bagged inside a further
                  holder for contamination control, record both layers. Report any
                  adhesive, support material and alignment aids used."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/labxctTAPP/sampleMountingMethod
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/labxctTAPP/sampleMountingMethod
                  schema:name:
                    const: Sample Mounting Method
                  schema:value:
                    type: string
                  schema:inDefinedTermSet:
                    const:
                      '@id': ada:vocab/sample-mounting-method
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              minContains: 0
              maxContains: 1
            - contains:
                title: X-ray Power
                description: "X-ray tube power in watts (W). Derivable as voltage
                  (kV) \xD7 current (mA) = kV \xD7 \xB5A / 1000. If power was varied
                  across samples within the session, report the full range applied
                  (e.g., 7\u201313 W)."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/labxctTAPP/xRayPower
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/labxctTAPP/xRayPower
                  schema:name:
                    const: X-ray Power
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
                title: Source-to-Object Distance (SOD)
                description: Distance from the X-ray source focal spot to the centre
                  of the sample rotation axis, in mm.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/labxctTAPP/sourceToObjectDistance
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/labxctTAPP/sourceToObjectDistance
                  schema:name:
                    const: Source-to-Object Distance (SOD)
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
                title: Source-to-Detector Distance (SDD)
                description: "Distance from the X-ray source focal spot to the detector
                  surface, in mm. Voxel size \u2248 detector pixel size / M (before
                  binning; divide additionally by optical objective for Versa-class
                  systems)."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/labxctTAPP/sourceToDetectorDistance
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/labxctTAPP/sourceToDetectorDistance
                  schema:name:
                    const: Source-to-Detector Distance (SDD)
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
                title: Rotation Range
                description: Total angular range over which projection images are
                  acquired, in degrees.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/labxctTAPP/rotationRange
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/labxctTAPP/rotationRange
                  schema:name:
                    const: Rotation Range
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
                title: Number of Projections
                description: Total number of equally-spaced projection images acquired
                  over the full rotation range. For Mode B (multi-volume stitching),
                  this is the number per sub-volume.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/labxctTAPP/numberOfProjections
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/labxctTAPP/numberOfProjections
                  schema:name:
                    const: Number of Projections
                  schema:value:
                    anyOf:
                    - type: number
                    - type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              minContains: 0
              maxContains: 1
            - contains:
                title: Rotation Step Size
                description: Angular increment between successive projection images,
                  in degrees. Equal to Rotation Range divided by Number of Projections
                  when both are reported; however, some sources report step size as
                  the primary rotation parameter without stating the total number
                  of projections explicitly.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/labxctTAPP/rotationStepSize
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/labxctTAPP/rotationStepSize
                  schema:name:
                    const: Rotation Step Size
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
                title: Exposure Time per Projection
                description: "Duration of X-ray exposure for each individual projection
                  image frame, in seconds. Adjustment is warranted for samples that
                  are unusually dense or unusually transparent. If the exposure time
                  was varied across samples within the same procedure or session,
                  report the full range applied (e.g., 0.5\u20132 s)."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/labxctTAPP/exposureTimePerProjection
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/labxctTAPP/exposureTimePerProjection
                  schema:name:
                    const: Exposure Time per Projection
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
                title: Frames Averaged per Projection
                description: "Number of individual detector frames acquired and averaged
                  to produce each saved projection image. The effective exposure per
                  projection = exposure time per frame \xD7 frames averaged."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/labxctTAPP/framesAveragedPerProjection
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/labxctTAPP/framesAveragedPerProjection
                  schema:name:
                    const: Frames Averaged per Projection
                  schema:value:
                    anyOf:
                    - type: number
                    - type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              minContains: 0
              maxContains: 1
            - contains:
                title: Detector Binning
                description: "Detector pixel binning factor applied during acquisition.
                  Binning combines adjacent pixels (e.g., 2\xD72 combines 4 pixels
                  into one)."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/labxctTAPP/detectorBinning
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/labxctTAPP/detectorBinning
                  schema:name:
                    const: Detector Binning
                  schema:value:
                    type: string
                  schema:inDefinedTermSet:
                    const:
                      '@id': ada:vocab/detector-binning
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              minContains: 0
              maxContains: 1
            - contains:
                title: Rotation Mode
                description: Whether projection images are acquired during continuous
                  sample rotation (faster; may introduce slight motion blur at high
                  rotation speeds) or at discrete step positions with the stage stationary
                  during each exposure (stop-and-shoot; eliminates motion blur).
                type: object
                properties:
                  '@id':
                    const: ada:parameter/labxctTAPP/rotationMode
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/labxctTAPP/rotationMode
                  schema:name:
                    const: Rotation Mode
                  schema:value:
                    type: string
                  schema:inDefinedTermSet:
                    const:
                      '@id': ada:vocab/rotation-mode
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Analysis_samplingUnitSelectionCriteria
              minContains: 0
              maxContains: 1
            - contains:
                title: Reconstruction Convolution Filter
                description: Convolution (apodization) filter kernel applied during
                  back-projection reconstruction.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/labxctTAPP/reconstructionConvolutionFilter
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/labxctTAPP/reconstructionConvolutionFilter
                  schema:name:
                    const: Reconstruction Convolution Filter
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
                title: Beam Hardening Correction Parameter
                description: Numerical value or setting applied in the software beam
                  hardening correction algorithm for this specific analysis. Companion
                  to Beam Hardening Correction Method.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/labxctTAPP/beamHardeningCorrectionParameter
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/labxctTAPP/beamHardeningCorrectionParameter
                  schema:name:
                    const: Beam Hardening Correction Parameter
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
                title: Ring Artifact Correction Method
                description: Procedure specification for how ring artifacts are handled.
                  Whether correction was applied and its outcome are recorded separately
                  in Group 6.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/labxctTAPP/ringArtifactCorrectionMethod
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/labxctTAPP/ringArtifactCorrectionMethod
                  schema:name:
                    const: Ring Artifact Correction Method
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
                title: CT Number Calibration
                description: Whether the raw CT grayscale values have been calibrated
                  to physically meaningful units using reference materials.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/labxctTAPP/ctNumberCalibration
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/labxctTAPP/ctNumberCalibration
                  schema:name:
                    const: CT Number Calibration
                  schema:value:
                    type: string
                  schema:inDefinedTermSet:
                    const:
                      '@id': ada:vocab/ct-number-calibration
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
                    const: ada:parameter/labxctTAPP/segmentationMethod
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/labxctTAPP/segmentationMethod
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
                title: Segmentation Threshold Values or Criteria
                description: "Specific CT number range(s) or quantitative criteria
                  used to define each segmented phase or feature. For LAC-calibrated
                  datasets, report values in cm\u207B\xB9."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/labxctTAPP/segmentationThresholdValuesOrCriteria
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/labxctTAPP/segmentationThresholdValuesOrCriteria
                  schema:name:
                    const: Segmentation Threshold Values or Criteria
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
                title: Phase Identification Method
                description: Method used to assign reconstructed CT number ranges
                  to specific mineral phases or material types. Approaches include
                  comparison to calculated linear attenuation coefficients (LAC),
                  cross-validation with independent analytical techniques, or empirical
                  calibration.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/labxctTAPP/phaseIdentificationMethod
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/labxctTAPP/phaseIdentificationMethod
                  schema:name:
                    const: Phase Identification Method
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
                title: VOI Selection Criteria
                description: Rules specifying how the Volume of Interest (VOI) is
                  to be defined for quantitative analysis. Common criteria exclude
                  cone-beam artifact zones at sample edges, beam hardening halos near
                  dense inclusions, and sample holder signal. The actual VOI applied
                  in a specific analysis is recorded separately at analysis level.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/labxctTAPP/voiSelectionCriteria
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/labxctTAPP/voiSelectionCriteria
                  schema:name:
                    const: VOI Selection Criteria
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
                title: Output Bit Depth
                description: Bit depth of the reconstructed 3D volume (number of bits
                  used to encode each voxel's grayscale value). Common values are
                  8-bit (256 gray levels), 16-bit (65,536 gray levels), or 32-bit
                  floating point. A required output bit depth may be specified if
                  downstream analysis workflows depend on a consistent grayscale range.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/labxctTAPP/outputBitDepth
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/labxctTAPP/outputBitDepth
                  schema:name:
                    const: Output Bit Depth
                  schema:value:
                    type: string
                  schema:inDefinedTermSet:
                    const:
                      '@id': ada:vocab/output-bit-depth
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              minContains: 0
              maxContains: 1
            - contains:
                title: Total Scan Duration
                description: Total elapsed time for the complete XCT acquisition,
                  from the start of the first projection to the end of the last. For
                  multi-volume acquisitions, this is the combined scan time across
                  all sub-volumes (not including setup or reconstruction time).
                type: object
                properties:
                  '@id':
                    const: ada:parameter/labxctTAPP/totalScanDuration
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/labxctTAPP/totalScanDuration
                  schema:name:
                    const: Total Scan Duration
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
                title: Partial Volume Effect Criteria
                description: "Specification of how partial volume effects (PVE) are
                  managed in quantitative analysis. PVE correction can be implemented
                  via PSF-based deconvolution tools such as Blob3D. Record the minimum
                  feature size criterion adopted for the procedure (in voxels or \xB5m),
                  the basis for it, the treatment of boundary voxels in modal abundance
                  or size distribution calculations, and whether PVE correction is
                  required or optional. State whether the criterion follows the Withers
                  et al. (2021) convention \u2014 a feature must span at least 3 voxels
                  to be positively identified and at least 10 for reliable shape and
                  volume characterisation \u2014 or is SNR-limited, PVE-limited or
                  analyst-defined."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/labxctTAPP/partialVolumeEffectCriteria
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/labxctTAPP/partialVolumeEffectCriteria
                  schema:name:
                    const: Partial Volume Effect Criteria
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
                title: Cross-Validation Procedure Requirement
                description: Specification of what independent analytical validation
                  is required to confirm CT segmentation results, phase identification,
                  or quantitative measurements. Common approaches include BSE imaging,
                  SEM-EDS or EPMA modal analysis, He pycnometry for bulk porosity,
                  and Raman or SIMS phase mapping. Record the required validation
                  method(s) and the sampling fraction (e.g., every sample, one per
                  session, or a representative subset).
                type: object
                properties:
                  '@id':
                    const: ada:parameter/labxctTAPP/crossValidationProcedureRequirement
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/labxctTAPP/crossValidationProcedureRequirement
                  schema:name:
                    const: Cross-Validation Procedure Requirement
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
          prov:used:
            type: array
            items:
              type: object
              allOf:
              - if:
                  required:
                  - bios:computationalTool
                then:
                  properties:
                    bios:computationalTool:
                      type: array
                      items:
                        allOf:
                        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/geochemBaseProfile/schema.yaml#/$defs/UsedComputationalTool
                        - type: object
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
                                  description: Software used to reconstruct 2D projection
                                    images into a 3D CT volume, including version
                                    number.
                                  anyOf:
                                  - type: string
                                  - type: array
                                    items:
                                      type: string
                              required:
                              - schema:name
                          required:
                          - ada:toolRole
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
                                    const: XCT
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
                                      description: "X-ray tube accelerating voltage
                                        in kilovolts (kV). If the voltage was varied
                                        across samples within the same procedure or
                                        session, report the full range applied (e.g.,
                                        90\u2013115 kV). Note: some sources report
                                        this parameter as 'X keV' (maximum Bremsstrahlung
                                        photon energy) rather than 'X kV' (tube voltage).
                                        For polychromatic lab XCT, these are numerically
                                        equivalent: E_max [keV] = V [kV]. Record the
                                        value as originally reported, and add a parenthetical
                                        note if the unit used is keV."
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/labxctTAPP/acceleratingVoltage
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/labxctTAPP/acceleratingVoltage
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
                                    - title: Tube Current
                                      description: "X-ray tube current in microamperes
                                        (\xB5A). If the current was varied across
                                        samples within the same procedure or session,
                                        report the full range applied (e.g., 65\u2013115
                                        \xB5A)."
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/labxctTAPP/tubeCurrent
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/labxctTAPP/tubeCurrent
                                        schema:name:
                                          const: Tube Current
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
                                    - title: X-ray Pre-filter
                                      description: Material and thickness of the beam-hardening
                                        filter placed between the X-ray source and
                                        the sample. Both filter material and thickness
                                        must be reported. Instrument-proprietary filter
                                        codes should be decoded where possible.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/labxctTAPP/xRayPreFilter
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/labxctTAPP/xRayPreFilter
                                        schema:name:
                                          const: X-ray Pre-filter
                                        schema:value:
                                          type: string
                                      required:
                                      - '@id'
                                      - '@type'
                                      - schema:propertyID
                                      - schema:name
                                      - schema:value
                                    - title: Voxel Size
                                      description: "Isotropic voxel edge length of
                                        the reconstructed 3D volume in micrometres.
                                        The target voxel size is set based on the
                                        smallest feature to be resolved (target voxel
                                        size \u2264 ~1/3 of that feature size; see
                                        the criterion recorded under Partial Volume
                                        Effect Criteria). Record the achieved voxel
                                        size as reported by the reconstruction software,
                                        which may differ slightly from the target
                                        due to final geometric calibration."
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/labxctTAPP/voxelSize
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/labxctTAPP/voxelSize
                                        schema:name:
                                          const: Voxel Size
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
                                      description: "X-ray tube accelerating voltage
                                        in kilovolts (kV). If the voltage was varied
                                        across samples within the same procedure or
                                        session, report the full range applied (e.g.,
                                        90\u2013115 kV). Note: some sources report
                                        this parameter as 'X keV' (maximum Bremsstrahlung
                                        photon energy) rather than 'X kV' (tube voltage).
                                        For polychromatic lab XCT, these are numerically
                                        equivalent: E_max [keV] = V [kV]. Record the
                                        value as originally reported, and add a parenthetical
                                        note if the unit used is keV."
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/labxctTAPP/acceleratingVoltage
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/labxctTAPP/acceleratingVoltage
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
                                      title: Tube Current
                                      description: "X-ray tube current in microamperes
                                        (\xB5A). If the current was varied across
                                        samples within the same procedure or session,
                                        report the full range applied (e.g., 65\u2013115
                                        \xB5A)."
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/labxctTAPP/tubeCurrent
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/labxctTAPP/tubeCurrent
                                        schema:name:
                                          const: Tube Current
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
                                      title: X-ray Pre-filter
                                      description: Material and thickness of the beam-hardening
                                        filter placed between the X-ray source and
                                        the sample. Both filter material and thickness
                                        must be reported. Instrument-proprietary filter
                                        codes should be decoded where possible.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/labxctTAPP/xRayPreFilter
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/labxctTAPP/xRayPreFilter
                                        schema:name:
                                          const: X-ray Pre-filter
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
                                      title: Voxel Size
                                      description: "Isotropic voxel edge length of
                                        the reconstructed 3D volume in micrometres.
                                        The target voxel size is set based on the
                                        smallest feature to be resolved (target voxel
                                        size \u2264 ~1/3 of that feature size; see
                                        the criterion recorded under Partial Volume
                                        Effect Criteria). Record the achieved voxel
                                        size as reported by the reconstruction software,
                                        which may differ slightly from the target
                                        due to final geometric calibration."
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/labxctTAPP/voxelSize
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/labxctTAPP/voxelSize
                                        schema:name:
                                          const: Voxel Size
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
                                const: XCT
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
                          const: Data processing
                      required:
                      - schema:name
                    then:
                      properties:
                        schema:additionalProperty:
                          type: array
                          items:
                            anyOf:
                            - title: Flat Field Correction
                              description: Whether dark-field (detector read with
                                X-ray source off; electronic noise baseline) and bright-field
                                (source on, no sample; gain calibration) reference
                                images are acquired and applied to normalize detector
                                response before reconstruction.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/labxctTAPP/flatFieldCorrection
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/labxctTAPP/flatFieldCorrection
                                schema:name:
                                  const: Flat Field Correction
                                schema:value:
                                  type: string
                                schema:inDefinedTermSet:
                                  const:
                                    '@id': ada:vocab/flat-field-correction
                              required:
                              - '@id'
                              - '@type'
                              - schema:propertyID
                              - schema:name
                              - schema:value
                            - title: Sub-volume Stitching and Registration Method
                              description: Method used to register adjacent sub-volume
                                datasets to each other and stitch them into a single
                                continuous 3D volume. Report the alignment strategy
                                (manual, automated, fiducial-based), the software
                                used, and any correction steps applied. Where rotational
                                mismatch has been corrected via raw projection re-alignment,
                                document it here.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/labxctTAPP/subVolumeStitchingAndRegistrationMethod
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/labxctTAPP/subVolumeStitchingAndRegistrationMethod
                                schema:name:
                                  const: Sub-volume Stitching and Registration Method
                                schema:value:
                                  type: string
                              required:
                              - '@id'
                              - '@type'
                              - schema:propertyID
                              - schema:name
                              - schema:value
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Analysis_constantsReferenceValues
                          allOf:
                          - contains:
                              title: Flat Field Correction
                              description: Whether dark-field (detector read with
                                X-ray source off; electronic noise baseline) and bright-field
                                (source on, no sample; gain calibration) reference
                                images are acquired and applied to normalize detector
                                response before reconstruction.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/labxctTAPP/flatFieldCorrection
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/labxctTAPP/flatFieldCorrection
                                schema:name:
                                  const: Flat Field Correction
                                schema:value:
                                  type: string
                                schema:inDefinedTermSet:
                                  const:
                                    '@id': ada:vocab/flat-field-correction
                              required:
                              - '@id'
                              - '@type'
                              - schema:propertyID
                              - schema:name
                              - schema:value
                            minContains: 0
                            maxContains: 1
                          - contains:
                              title: Sub-volume Stitching and Registration Method
                              description: Method used to register adjacent sub-volume
                                datasets to each other and stitch them into a single
                                continuous 3D volume. Report the alignment strategy
                                (manual, automated, fiducial-based), the software
                                used, and any correction steps applied. Where rotational
                                mismatch has been corrected via raw projection re-alignment,
                                document it here.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/labxctTAPP/subVolumeStitchingAndRegistrationMethod
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/labxctTAPP/subVolumeStitchingAndRegistrationMethod
                                schema:name:
                                  const: Sub-volume Stitching and Registration Method
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
      title: Analysis Events
    schema:distribution:
      type: array
      items:
        type: object
        properties:
          schema:encodingFormat:
            type: array
            items:
              description: File format of the reconstructed CT volume as output by
                the reconstruction software. Bit depth is recorded separately in Output
                Bit Depth.
              anyOf:
              - type: string
                enum:
                - TIFF image stack
                - VGI/VOL (VGStudio)
                - RAW volume
                - DICOM
                - N/A
                - None
                - missing
              - type: string
              schema:inDefinedTermSet: ada:vocab/output-data-format
            minItems: 1
        required:
        - schema:encodingFormat
      title: Distributions
    schema:additionalProperty:
      type: array
      items:
        anyOf:
        - title: Effective Spatial Resolution (PSF/MTF)
          description: "Effective spatial resolution of the reconstructed CT volume,
            which typically differs from (and is coarser than) the voxel size due
            to the detector point spread function (PSF), geometric unsharpness, and
            the reconstruction filter. Formal measurement uses the PSF method described
            in Ketcham & Hildebrandt (2014) or the modulation transfer function (MTF);
            resolution can also be reported per ASTM E1441-11. When formal measurement
            is unavailable, an estimate based on acquisition geometry (e.g., the Brenner-Weiss
            formula) or a stated multiple of the voxel size may be recorded. Report
            the value in \xB5m along with the method used to determine or estimate
            it. Note that most XCT papers use the bare phrase \"spatial resolution\"
            for the voxel size; record that under Voxel Size, and leave this field
            as not reported unless an effective resolution was actually determined."
          type: object
          properties:
            '@id':
              const: ada:parameter/labxctTAPP/effectiveSpatialResolution
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/labxctTAPP/effectiveSpatialResolution
            schema:name:
              const: Effective Spatial Resolution (PSF/MTF)
            schema:value:
              type: string
          required:
          - '@id'
          - '@type'
          - schema:propertyID
          - schema:name
          - schema:value
        - title: Number of Sub-volumes
          description: Total number of overlapping sub-volume scans acquired to cover
            the full sample length. Applies only to Mode B (multi-volume stitching).
          type: object
          properties:
            '@id':
              const: ada:parameter/labxctTAPP/numberOfSubVolumes
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/labxctTAPP/numberOfSubVolumes
            schema:name:
              const: Number of Sub-volumes
            schema:value:
              anyOf:
              - type: number
              - type: string
          required:
          - '@id'
          - '@type'
          - schema:propertyID
          - schema:name
          - schema:value
        - title: VOI Applied
          description: Actual Volume of Interest used, including dimensions or defining
            criteria. Companion to VOI Selection Criteria.
          type: object
          properties:
            '@id':
              const: ada:parameter/labxctTAPP/voiApplied
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/labxctTAPP/voiApplied
            schema:name:
              const: VOI Applied
            schema:value:
              type: string
          required:
          - '@id'
          - '@type'
          - schema:propertyID
          - schema:name
          - schema:value
        - title: Sub-volume Overlap
          description: Actual number of reconstructed slices overlapping between adjacent
            sub-volumes. May differ from the minimum sub-volume overlap required specified
            in the procedure (Group 4) if sample geometry or operator decisions resulted
            in greater or lesser overlap.
          type: object
          properties:
            '@id':
              const: ada:parameter/labxctTAPP/subVolumeOverlap
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/labxctTAPP/subVolumeOverlap
            schema:name:
              const: Sub-volume Overlap
            schema:value:
              anyOf:
              - type: number
              - type: string
          required:
          - '@id'
          - '@type'
          - schema:propertyID
          - schema:name
          - schema:value
      allOf:
      - contains:
          title: Effective Spatial Resolution (PSF/MTF)
          description: "Effective spatial resolution of the reconstructed CT volume,
            which typically differs from (and is coarser than) the voxel size due
            to the detector point spread function (PSF), geometric unsharpness, and
            the reconstruction filter. Formal measurement uses the PSF method described
            in Ketcham & Hildebrandt (2014) or the modulation transfer function (MTF);
            resolution can also be reported per ASTM E1441-11. When formal measurement
            is unavailable, an estimate based on acquisition geometry (e.g., the Brenner-Weiss
            formula) or a stated multiple of the voxel size may be recorded. Report
            the value in \xB5m along with the method used to determine or estimate
            it. Note that most XCT papers use the bare phrase \"spatial resolution\"
            for the voxel size; record that under Voxel Size, and leave this field
            as not reported unless an effective resolution was actually determined."
          type: object
          properties:
            '@id':
              const: ada:parameter/labxctTAPP/effectiveSpatialResolution
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/labxctTAPP/effectiveSpatialResolution
            schema:name:
              const: Effective Spatial Resolution (PSF/MTF)
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
          title: Number of Sub-volumes
          description: Total number of overlapping sub-volume scans acquired to cover
            the full sample length. Applies only to Mode B (multi-volume stitching).
          type: object
          properties:
            '@id':
              const: ada:parameter/labxctTAPP/numberOfSubVolumes
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/labxctTAPP/numberOfSubVolumes
            schema:name:
              const: Number of Sub-volumes
            schema:value:
              anyOf:
              - type: number
              - type: string
          required:
          - '@id'
          - '@type'
          - schema:propertyID
          - schema:name
          - schema:value
        minContains: 0
        maxContains: 1
      - contains:
          title: VOI Applied
          description: Actual Volume of Interest used, including dimensions or defining
            criteria. Companion to VOI Selection Criteria.
          type: object
          properties:
            '@id':
              const: ada:parameter/labxctTAPP/voiApplied
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/labxctTAPP/voiApplied
            schema:name:
              const: VOI Applied
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
          title: Sub-volume Overlap
          description: Actual number of reconstructed slices overlapping between adjacent
            sub-volumes. May differ from the minimum sub-volume overlap required specified
            in the procedure (Group 4) if sample geometry or operator decisions resulted
            in greater or lesser overlap.
          type: object
          properties:
            '@id':
              const: ada:parameter/labxctTAPP/subVolumeOverlap
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/labxctTAPP/subVolumeOverlap
            schema:name:
              const: Sub-volume Overlap
            schema:value:
              anyOf:
              - type: number
              - type: string
          required:
          - '@id'
          - '@type'
          - schema:propertyID
          - schema:name
          - schema:value
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
                const: Beam Hardening Artifact Assessment
            required:
            - dqv:isMeasurementOf
          then:
            properties:
              dqv:value:
                description: Assessment of whether residual beam hardening (cupping
                  artifact) is present in the reconstructed volume after any corrections
                  applied during reconstruction. Record whether this artifact is detectable
                  in the final dataset, what correction or mitigation was applied
                  (e.g., linearisation, pre-filtering, iterative correction), and
                  whether any residual effect influences the analysis region.
                anyOf:
                - type: string
                - type: array
                  items:
                    type: string
        - if:
            properties:
              dqv:isMeasurementOf:
                const: Ring Artifact Severity and Correction Outcome
            required:
            - dqv:isMeasurementOf
          then:
            properties:
              dqv:value:
                description: "Assessment of whether ring artifacts \u2014 concentric
                  rings centred on the rotation axis arising from differential sensitivity
                  or gain drift among detector elements \u2014 were present and whether
                  correction was effective. Note that ring correction algorithms modify
                  image intensity in narrow annular bands. Record whether rings were
                  present, whether correction was applied, and whether any residual
                  rings or correction artifacts fall within the analysis volume of
                  interest."
                anyOf:
                - type: string
                - type: array
                  items:
                    type: string
        - if:
            properties:
              dqv:isMeasurementOf:
                const: Metal Streak Artifact Assessment
            required:
            - dqv:isMeasurementOf
          then:
            properties:
              dqv:value:
                description: Assessment of whether high-density inclusions (FeNi metal,
                  platinum-group minerals, dense oxides, or other high-Z phases) produce
                  streak or starburst artifacts in the reconstructed volume. Common
                  forms include radial starburst streaks from high-Z inclusions and
                  shadowing (anomalously low CT number) in beam-shadow regions behind
                  dense phases. Record which artifact type(s) are present, their spatial
                  extent, and any exclusion zones or correction steps applied.
                anyOf:
                - type: string
                - type: array
                  items:
                    type: string
        - if:
            properties:
              dqv:isMeasurementOf:
                const: Partial Volume Effect Assessment
            required:
            - dqv:isMeasurementOf
          then:
            properties:
              dqv:value:
                description: Record of PVE severity and how it was handled. Documents
                  the minimum feature size relative to the voxel size, the fraction
                  of the feature population affected, and any PVE correction method
                  applied (e.g., PSF-based deconvolution via Blob3D).
                anyOf:
                - type: string
                - type: array
                  items:
                    type: string
        - if:
            properties:
              dqv:isMeasurementOf:
                const: Signal-to-Noise Ratio
            required:
            - dqv:isMeasurementOf
          then:
            properties:
              dqv:value:
                description: Quantitative measure of image quality in the reconstructed
                  CT volume. Typically calculated as the mean CT number divided by
                  the standard deviation of CT number in a homogeneous reference region
                  (e.g., an inclusion-free zone of the matrix). Record the measured
                  value and the region used for measurement, or note if SNR was not
                  formally measured.
                anyOf:
                - type: string
                - type: array
                  items:
                    type: string
        - if:
            properties:
              dqv:isMeasurementOf:
                const: Cross-Validation Outcome
            required:
            - dqv:isMeasurementOf
          then:
            properties:
              dqv:value:
                description: Record of what independent validation was performed and
                  its result. Report the validation method(s) used, the quantitative
                  agreement achieved (e.g., relative difference in modal abundance,
                  porosity), and any discrepancies and their likely causes. Where
                  BSE imaging is the validation method, note that BSE provides a 2D
                  section while CT provides a 3D volume.
                anyOf:
                - type: string
                - type: array
                  items:
                    type: string
      title: Quality Measurements
x-bblocks-metadata:
  itemIdentifier: ogch.techniqueProfile.geochemProfile.XCT.detail
  register: https://amds-ldeo.github.io/geochemBuildingBlocks/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-11-11'

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XCT/detail/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XCT/detail/schema.yaml)


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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XCT/detail/context.jsonld)

## Sources

* [Lab-XCT_TAPP_v8.xlsx (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/XCT/detail`

