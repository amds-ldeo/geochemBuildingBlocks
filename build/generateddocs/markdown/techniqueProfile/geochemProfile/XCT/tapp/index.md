
# Lab-XCT Technique-Aligned Protocol Profile (labxctTAPP) (Schema)

`ogch.techniqueProfile.geochemProfile.XCT.tapp` *v0.1*

Laboratory X-ray computed tomography (polychromatic cone-beam) extension of the base TAPP definition. Adds XCT protocol-level acquisition/processing defaults as top-level ada: properties and an ada:methodParameters vocabulary of session-adjustable parameter templates. XCT has no per-element analyte axis, so no analyteTemplate is defined. Vocabularies and parameter templates ship as separate files under vocab/ and parameterTemplates/.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### labxctTAPP example Eckley2024
labxctTAPP instance derived from Eckley 2024 (JSC Scan Record) Bennu particle Single-volume Nikon XTH 320 NASA JSC X-FaCT.
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
  "@id": "ex:labxctTAPP-Eckley2024",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "labxct protocol — Eckley2024",
  "schema:description": "labxctTAPP instance derived from Eckley 2024 (JSC Scan Record) Bennu particle Single-volume Nikon XTH 320 NASA JSC X-FaCT (publication column of Lab-XCT_TAPP_v37.csv).",
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
            "C-type asteroid particle (Bennu, OSIRIS-REx)"
          ]
        }
      ]
    }
  ],
  "ada:targetFeature": "Internal structure; mineralogy (reconnaissance scan)",
  "ada:xRaySourceConfiguration": "180 kV transmission source",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/labxctTAPP/xRayTubeAnodeMaterial",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/xRayTubeAnodeMaterial"
        }
      ],
      "schema:name": "X-ray Tube Anode Material",
      "schema:value": "Tungsten"
    },
    {
      "@id": "ada:parameter/labxctTAPP/xRayPowerDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "xRayPowerDefault",
      "schema:name": "X-ray Power",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 3.0,
      "schema:description": "3.0 W"
    },
    {
      "@id": "ada:parameter/labxctTAPP/sourceToObjectDistanceDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "sourceToObjectDistanceDefault",
      "schema:name": "Source-to-Object Distance (SOD)",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 20.39,
      "schema:description": "20.39 mm"
    },
    {
      "@id": "ada:parameter/labxctTAPP/sourceToDetectorDistanceDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "sourceToDetectorDistanceDefault",
      "schema:name": "Source-to-Detector Distance (SDD)",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 679.51,
      "schema:description": "679.51 mm"
    },
    {
      "@id": "ada:parameter/labxctTAPP/framesAveragedPerProjectionDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "framesAveragedPerProjectionDefault",
      "schema:name": "Frames Averaged per Projection",
      "ada:dataType": "integer",
      "ada:fieldScope": "session",
      "schema:defaultValue": 1,
      "schema:description": "1 frame"
    },
    {
      "@id": "ada:parameter/labxctTAPP/detectorBinningDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "detectorBinningDefault",
      "schema:name": "Detector Binning",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "1×1 (no binning)"
    },
    {
      "@id": "ada:parameter/labxctTAPP/beamHardeningCorrectionParameterDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "beamHardeningCorrectionParameterDefault",
      "schema:name": "Beam Hardening Correction Parameter",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Preset 4"
    },
    {
      "@id": "ada:parameter/labxctTAPP/outputBitDepthDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "outputBitDepthDefault",
      "schema:name": "Output Bit Depth",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "16-bit (full grayscale range)"
    }
  ],
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Nikon CTPro3D v5.4"
    }
  ],
  "schema:instrument": [
    {
      "schema:additionalType": [
        "XCT",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "110 kV",
      "ada:tubeCurrentDefault": "27 µA",
      "ada:xRayPreFilterDefault": "0.25 mm aluminum",
      "ada:voxelSizeDefault": "6.00 µm",
      "schema:manufacturer": {
        "schema:name": "Nikon",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "Nikon XT H 320",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/XCT",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:numberOfProjectionsDefault": "4000",
  "ada:exposureTimePerProjectionDefault": "4.00 s",
  "schema:actionProcess": {
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
        "schema:position": 1
      },
      {
        "schema:name": "Data reduction",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/labxctTAPP/flatFieldCorrectionDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "flatFieldCorrectionDefault",
            "schema:name": "Flat Field Correction",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Flux normalization: no"
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
  "ada:rotationModeDefault": "Continuous rotation",
  "ada:beamHardeningCorrectionMethod": "Hardware filter (0.25 mm Al) + software BHC preset",
  "ada:outputDataFormatDefault": "TIFF (16-bit, 928 slices)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Lab XCT"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "NASA JSC Astromaterials X-FaCT Lab"
  },
  "ada:samplingUnit": "Whole sample (single allocated Bennu particle; 928 slices)",
  "ada:analyticalMode": [
    "Single-volume"
  ],
  "ada:applicableSampleDimensionRange": "missing",
  "ada:detectorType": "missing",
  "ada:minimumSubVolumeOverlap": -9999,
  "ada:reconstructionAlgorithm": "missing",
  "ada:rotationRangeDefault": -9999,
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:segmentationMethodDefault": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XCT/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:labxctTAPP-Eckley2024",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "labxct protocol \u2014 Eckley2024",
  "schema:description": "labxctTAPP instance derived from Eckley 2024 (JSC Scan Record) Bennu particle Single-volume Nikon XTH 320 NASA JSC X-FaCT (publication column of Lab-XCT_TAPP_v37.csv).",
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
            "C-type asteroid particle (Bennu, OSIRIS-REx)"
          ]
        }
      ]
    }
  ],
  "ada:targetFeature": "Internal structure; mineralogy (reconnaissance scan)",
  "ada:xRaySourceConfiguration": "180 kV transmission source",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/labxctTAPP/xRayTubeAnodeMaterial",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/xRayTubeAnodeMaterial"
        }
      ],
      "schema:name": "X-ray Tube Anode Material",
      "schema:value": "Tungsten"
    },
    {
      "@id": "ada:parameter/labxctTAPP/xRayPowerDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "xRayPowerDefault",
      "schema:name": "X-ray Power",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 3.0,
      "schema:description": "3.0 W"
    },
    {
      "@id": "ada:parameter/labxctTAPP/sourceToObjectDistanceDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "sourceToObjectDistanceDefault",
      "schema:name": "Source-to-Object Distance (SOD)",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 20.39,
      "schema:description": "20.39 mm"
    },
    {
      "@id": "ada:parameter/labxctTAPP/sourceToDetectorDistanceDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "sourceToDetectorDistanceDefault",
      "schema:name": "Source-to-Detector Distance (SDD)",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 679.51,
      "schema:description": "679.51 mm"
    },
    {
      "@id": "ada:parameter/labxctTAPP/framesAveragedPerProjectionDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "framesAveragedPerProjectionDefault",
      "schema:name": "Frames Averaged per Projection",
      "ada:dataType": "integer",
      "ada:fieldScope": "session",
      "schema:defaultValue": 1,
      "schema:description": "1 frame"
    },
    {
      "@id": "ada:parameter/labxctTAPP/detectorBinningDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "detectorBinningDefault",
      "schema:name": "Detector Binning",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "1\u00d71 (no binning)"
    },
    {
      "@id": "ada:parameter/labxctTAPP/beamHardeningCorrectionParameterDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "beamHardeningCorrectionParameterDefault",
      "schema:name": "Beam Hardening Correction Parameter",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Preset 4"
    },
    {
      "@id": "ada:parameter/labxctTAPP/outputBitDepthDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "outputBitDepthDefault",
      "schema:name": "Output Bit Depth",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "16-bit (full grayscale range)"
    }
  ],
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Nikon CTPro3D v5.4"
    }
  ],
  "schema:instrument": [
    {
      "schema:additionalType": [
        "XCT",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "110 kV",
      "ada:tubeCurrentDefault": "27 \u00b5A",
      "ada:xRayPreFilterDefault": "0.25 mm aluminum",
      "ada:voxelSizeDefault": "6.00 \u00b5m",
      "schema:manufacturer": {
        "schema:name": "Nikon",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "Nikon XT H 320",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/XCT",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:numberOfProjectionsDefault": "4000",
  "ada:exposureTimePerProjectionDefault": "4.00 s",
  "schema:actionProcess": {
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
        "schema:position": 1
      },
      {
        "schema:name": "Data reduction",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/labxctTAPP/flatFieldCorrectionDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "flatFieldCorrectionDefault",
            "schema:name": "Flat Field Correction",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Flux normalization: no"
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
  "ada:rotationModeDefault": "Continuous rotation",
  "ada:beamHardeningCorrectionMethod": "Hardware filter (0.25 mm Al) + software BHC preset",
  "ada:outputDataFormatDefault": "TIFF (16-bit, 928 slices)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Lab XCT"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "NASA JSC Astromaterials X-FaCT Lab"
  },
  "ada:samplingUnit": "Whole sample (single allocated Bennu particle; 928 slices)",
  "ada:analyticalMode": [
    "Single-volume"
  ],
  "ada:applicableSampleDimensionRange": "missing",
  "ada:detectorType": "missing",
  "ada:minimumSubVolumeOverlap": -9999,
  "ada:reconstructionAlgorithm": "missing",
  "ada:rotationRangeDefault": -9999,
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:segmentationMethodDefault": "missing",
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

ex:labxctTAPP-Eckley2024 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/flatFieldCorrectionDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/beamHardeningCorrectionParameterDefault>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/detectorBinningDefault>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/framesAveragedPerProjectionDefault>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/outputBitDepthDefault>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/sourceToDetectorDistanceDefault>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/sourceToObjectDistanceDefault>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayPowerDefault>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayTubeAnodeMaterial> ;
    schema1:datePublished "missing" ;
    schema1:description "labxctTAPP instance derived from Eckley 2024 (JSC Scan Record) Bennu particle Single-volume Nikon XTH 320 NASA JSC X-FaCT (publication column of Lab-XCT_TAPP_v37.csv)." ;
    schema1:instrument <https://example.org/instrument/XCT> ;
    schema1:location [ a schema1:Place ;
            schema1:name "NASA JSC Astromaterials X-FaCT Lab" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Lab XCT" ] ;
    schema1:name "labxct protocol — Eckley2024" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "C-type asteroid particle (Bennu, OSIRIS-REx)" ] ] ;
    ada:analyticalMode "Single-volume" ;
    ada:applicableSampleDimensionRange "missing" ;
    ada:beamHardeningCorrectionMethod "Hardware filter (0.25 mm Al) + software BHC preset" ;
    ada:detectorType "missing" ;
    ada:exposureTimePerProjectionDefault "4.00 s" ;
    ada:minimumSubVolumeOverlap -9999 ;
    ada:numberOfProjectionsDefault "4000" ;
    ada:outputDataFormatDefault "TIFF (16-bit, 928 slices)" ;
    ada:reconstructionAlgorithm "missing" ;
    ada:rotationModeDefault "Continuous rotation" ;
    ada:rotationRangeDefault -9999 ;
    ada:samplingUnit "Whole sample (single allocated Bennu particle; 928 slices)" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:segmentationMethodDefault "missing" ;
    ada:targetFeature "Internal structure; mineralogy (reconnaissance scan)" ;
    ada:xRaySourceConfiguration "180 kV transmission source" ;
    bios:computationalTool [ schema1:name "Nikon CTPro3D v5.4" ;
            ada:toolRole "dataReduction" ] .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/beamHardeningCorrectionParameterDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Preset 4" ;
    schema1:name "Beam Hardening Correction Parameter" ;
    schema1:valueName "beamHardeningCorrectionParameterDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/detectorBinningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "1×1 (no binning)" ;
    schema1:name "Detector Binning" ;
    schema1:valueName "detectorBinningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/flatFieldCorrectionDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Flux normalization: no" ;
    schema1:name "Flat Field Correction" ;
    schema1:valueName "flatFieldCorrectionDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/framesAveragedPerProjectionDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:description "1 frame" ;
    schema1:name "Frames Averaged per Projection" ;
    schema1:valueName "framesAveragedPerProjectionDefault" ;
    ada:dataType "integer" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/outputBitDepthDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "16-bit (full grayscale range)" ;
    schema1:name "Output Bit Depth" ;
    schema1:valueName "outputBitDepthDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/sourceToDetectorDistanceDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 6.7951e+02 ;
    schema1:description "679.51 mm" ;
    schema1:name "Source-to-Detector Distance (SDD)" ;
    schema1:valueName "sourceToDetectorDistanceDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/sourceToObjectDistanceDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 2.039e+01 ;
    schema1:description "20.39 mm" ;
    schema1:name "Source-to-Object Distance (SOD)" ;
    schema1:valueName "sourceToObjectDistanceDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayPowerDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 3e+00 ;
    schema1:description "3.0 W" ;
    schema1:name "X-ray Power" ;
    schema1:valueName "xRayPowerDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://example.org/instrument/XCT> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "XCT" ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Nikon" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Nikon XT H 320" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "110 kV" ;
    ada:tubeCurrentDefault "27 µA" ;
    ada:voxelSizeDefault "6.00 µm" ;
    ada:xRayPreFilterDefault "0.25 mm aluminum" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayTubeAnodeMaterial> a schema1:PropertyValue ;
    schema1:name "X-ray Tube Anode Material" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayTubeAnodeMaterial> ;
    schema1:value "Tungsten" .


```


### labxctTAPP example Genge2025
labxctTAPP instance derived from Genge et al. 2025 (Nat. Commun.) Ryugu particle (A0180) Single-volume Zeiss Versa Not stated.
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
  "@id": "ex:labxctTAPP-Genge2025",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "labxct protocol — Genge2025",
  "schema:description": "labxctTAPP instance derived from Genge et al. 2025 (Nat. Commun.) Ryugu particle (A0180) Single-volume Zeiss Versa Not stated (publication column of Lab-XCT_TAPP_v37.csv).",
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
            "C-type asteroid particle (Ryugu, Hayabusa2)"
          ]
        },
        {
          "@id": "ada:parameter/labxctTAPP/sampleDimensionsDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleDimensionsDefault",
          "schema:name": "Sample Dimensions (L × W × H)",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "1.592 × 0.756 × 0.985 mm"
        },
        {
          "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "preAnalysisImagingAndScreeningDefault",
          "schema:name": "Pre-Analysis Imaging and Screening",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Optical microscopy — morphological inspection of the sample exterior through the container window with the CLOXS digital optical microscope system on automated digital sample stages at JAXA/ISAS, before the sample was decanted for nano-XCT"
        }
      ]
    }
  ],
  "ada:targetFeature": "Microchondrules (SSOs); 3D volume fraction",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/labxctTAPP/sampleMountingMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "sampleMountingMethodDefault",
      "schema:name": "Sample Mounting Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Mounted in pipette tips"
    },
    {
      "@id": "ada:parameter/labxctTAPP/xRayTubeAnodeMaterial",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/xRayTubeAnodeMaterial"
        }
      ],
      "schema:name": "X-ray Tube Anode Material",
      "schema:value": "Tungsten"
    },
    {
      "@id": "ada:parameter/labxctTAPP/detectorArraySize",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/detectorArraySize"
        }
      ],
      "schema:name": "Detector Array Size",
      "schema:value": "2000 × 2000 pixels"
    },
    {
      "@id": "ada:parameter/labxctTAPP/opticalObjective",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/opticalObjective"
        }
      ],
      "schema:name": "Optical Objective",
      "schema:value": "4× objective lens"
    },
    {
      "@id": "ada:parameter/labxctTAPP/detectorBinningDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "detectorBinningDefault",
      "schema:name": "Detector Binning",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "No binning"
    },
    {
      "@id": "ada:parameter/labxctTAPP/phaseIdentificationMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "phaseIdentificationMethodDefault",
      "schema:name": "Phase Identification Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Sulphide rims of SSOs identified by bright contrast; silicate glass by contrast relative to matrix"
    },
    {
      "@id": "ada:parameter/labxctTAPP/outputBitDepthDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "outputBitDepthDefault",
      "schema:name": "Output Bit Depth",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "16-bit (CCD pixel depth)"
    },
    {
      "@id": "ada:parameter/labxctTAPP/partialVolumeEffectCriteriaDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "partialVolumeEffectCriteriaDefault",
      "schema:name": "Partial Volume Effect Criteria",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "SSOs ≥ 5.4 µm identified (implicit: features ≥ voxel size = 0.625 µm); sulphide rims ≥ 1 voxel required for detection"
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Decanted for XCT; sample split along fractures during mounting into pipette tips. Post-XCT: embedded in Specifix resin, polished with 0.1 µm Al₂O₃.",
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
  "ada:detectorType": "2000 × 2000 CCD plane (16-bit)",
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "ImageJ + TANGO plugin (Ollion et al. 2013)"
    }
  ],
  "schema:instrument": [
    {
      "schema:additionalType": [
        "XCT",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "90 kV",
      "ada:tubeCurrentDefault": "89 µA",
      "ada:xRayPreFilterDefault": "Inbuilt LE4 filter (beam hardening reduction)",
      "ada:voxelSizeDefault": "0.625 µm (A0180-A); 0.672 µm (A0180-B)",
      "schema:manufacturer": {
        "schema:name": "Zeiss",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "Zeiss Versa (model not specified)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/XCT",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:rotationRangeDefault": "360°",
  "ada:numberOfProjectionsDefault": "2401",
  "ada:exposureTimePerProjectionDefault": "33 s (A0180-A); 28 s (A0180-B)",
  "ada:beamHardeningCorrectionMethod": "Hardware filter (LE4 inbuilt)",
  "ada:segmentationMethodDefault": "ImageJ threshold-based; TANGO plugin for 3D object detection",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Lab XCT (nano-CT)"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Not stated"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM (post-XCT polished sections)",
        "schema:description": "Serial polished sections cut post-XCT; SEM imaging"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnit": "Sub-volume > Grain (sub-samples A0180-A and A0180-B; size and shape factor reported per microchondrule / sulphide-silicate object)",
  "ada:analyticalMode": [
    "Single-volume"
  ],
  "ada:reportedProperties": [
    "Microchondrule / sulphide-silicate object diameter (um) and shape factor; object abundance; particle volume"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method"
    }
  ],
  "ada:applicableSampleDimensionRange": "missing",
  "ada:minimumSubVolumeOverlap": -9999,
  "ada:outputDataFormatDefault": "missing",
  "ada:reconstructionAlgorithm": "missing",
  "ada:rotationModeDefault": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:xRaySourceConfiguration": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XCT/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:labxctTAPP-Genge2025",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "labxct protocol \u2014 Genge2025",
  "schema:description": "labxctTAPP instance derived from Genge et al. 2025 (Nat. Commun.) Ryugu particle (A0180) Single-volume Zeiss Versa Not stated (publication column of Lab-XCT_TAPP_v37.csv).",
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
            "C-type asteroid particle (Ryugu, Hayabusa2)"
          ]
        },
        {
          "@id": "ada:parameter/labxctTAPP/sampleDimensionsDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleDimensionsDefault",
          "schema:name": "Sample Dimensions (L \u00d7 W \u00d7 H)",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "1.592 \u00d7 0.756 \u00d7 0.985 mm"
        },
        {
          "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "preAnalysisImagingAndScreeningDefault",
          "schema:name": "Pre-Analysis Imaging and Screening",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Optical microscopy \u2014 morphological inspection of the sample exterior through the container window with the CLOXS digital optical microscope system on automated digital sample stages at JAXA/ISAS, before the sample was decanted for nano-XCT"
        }
      ]
    }
  ],
  "ada:targetFeature": "Microchondrules (SSOs); 3D volume fraction",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/labxctTAPP/sampleMountingMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "sampleMountingMethodDefault",
      "schema:name": "Sample Mounting Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Mounted in pipette tips"
    },
    {
      "@id": "ada:parameter/labxctTAPP/xRayTubeAnodeMaterial",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/xRayTubeAnodeMaterial"
        }
      ],
      "schema:name": "X-ray Tube Anode Material",
      "schema:value": "Tungsten"
    },
    {
      "@id": "ada:parameter/labxctTAPP/detectorArraySize",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/detectorArraySize"
        }
      ],
      "schema:name": "Detector Array Size",
      "schema:value": "2000 \u00d7 2000 pixels"
    },
    {
      "@id": "ada:parameter/labxctTAPP/opticalObjective",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/opticalObjective"
        }
      ],
      "schema:name": "Optical Objective",
      "schema:value": "4\u00d7 objective lens"
    },
    {
      "@id": "ada:parameter/labxctTAPP/detectorBinningDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "detectorBinningDefault",
      "schema:name": "Detector Binning",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "No binning"
    },
    {
      "@id": "ada:parameter/labxctTAPP/phaseIdentificationMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "phaseIdentificationMethodDefault",
      "schema:name": "Phase Identification Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Sulphide rims of SSOs identified by bright contrast; silicate glass by contrast relative to matrix"
    },
    {
      "@id": "ada:parameter/labxctTAPP/outputBitDepthDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "outputBitDepthDefault",
      "schema:name": "Output Bit Depth",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "16-bit (CCD pixel depth)"
    },
    {
      "@id": "ada:parameter/labxctTAPP/partialVolumeEffectCriteriaDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "partialVolumeEffectCriteriaDefault",
      "schema:name": "Partial Volume Effect Criteria",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "SSOs \u2265 5.4 \u00b5m identified (implicit: features \u2265 voxel size = 0.625 \u00b5m); sulphide rims \u2265 1 voxel required for detection"
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Decanted for XCT; sample split along fractures during mounting into pipette tips. Post-XCT: embedded in Specifix resin, polished with 0.1 \u00b5m Al\u2082O\u2083.",
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
  "ada:detectorType": "2000 \u00d7 2000 CCD plane (16-bit)",
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "ImageJ + TANGO plugin (Ollion et al. 2013)"
    }
  ],
  "schema:instrument": [
    {
      "schema:additionalType": [
        "XCT",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "90 kV",
      "ada:tubeCurrentDefault": "89 \u00b5A",
      "ada:xRayPreFilterDefault": "Inbuilt LE4 filter (beam hardening reduction)",
      "ada:voxelSizeDefault": "0.625 \u00b5m (A0180-A); 0.672 \u00b5m (A0180-B)",
      "schema:manufacturer": {
        "schema:name": "Zeiss",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "Zeiss Versa (model not specified)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/XCT",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:rotationRangeDefault": "360\u00b0",
  "ada:numberOfProjectionsDefault": "2401",
  "ada:exposureTimePerProjectionDefault": "33 s (A0180-A); 28 s (A0180-B)",
  "ada:beamHardeningCorrectionMethod": "Hardware filter (LE4 inbuilt)",
  "ada:segmentationMethodDefault": "ImageJ threshold-based; TANGO plugin for 3D object detection",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Lab XCT (nano-CT)"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Not stated"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM (post-XCT polished sections)",
        "schema:description": "Serial polished sections cut post-XCT; SEM imaging"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnit": "Sub-volume > Grain (sub-samples A0180-A and A0180-B; size and shape factor reported per microchondrule / sulphide-silicate object)",
  "ada:analyticalMode": [
    "Single-volume"
  ],
  "ada:reportedProperties": [
    "Microchondrule / sulphide-silicate object diameter (um) and shape factor; object abundance; particle volume"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method"
    }
  ],
  "ada:applicableSampleDimensionRange": "missing",
  "ada:minimumSubVolumeOverlap": -9999,
  "ada:outputDataFormatDefault": "missing",
  "ada:reconstructionAlgorithm": "missing",
  "ada:rotationModeDefault": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:xRaySourceConfiguration": "missing",
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

ex:labxctTAPP-Genge2025 a cdi:Activity,
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
                    schema1:description "Decanted for XCT; sample split along fractures during mounting into pipette tips. Post-XCT: embedded in Specifix resin, polished with 0.1 µm Al₂O₃." ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/detectorArraySize>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/detectorBinningDefault>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/opticalObjective>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/outputBitDepthDefault>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/partialVolumeEffectCriteriaDefault>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/phaseIdentificationMethodDefault>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleMountingMethodDefault>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayTubeAnodeMaterial> ;
    schema1:datePublished "missing" ;
    schema1:description "labxctTAPP instance derived from Genge et al. 2025 (Nat. Commun.) Ryugu particle (A0180) Single-volume Zeiss Versa Not stated (publication column of Lab-XCT_TAPP_v37.csv)." ;
    schema1:instrument <https://example.org/instrument/XCT> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Not stated" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Lab XCT (nano-CT)" ] ;
    schema1:name "labxct protocol — Genge2025" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "C-type asteroid particle (Ryugu, Hayabusa2)" ],
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleDimensionsDefault>,
                <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "Serial polished sections cut post-XCT; SEM imaging" ;
                    schema1:name "SEM (post-XCT polished sections)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    schema1:variableMeasured [ schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analyticalMode "Single-volume" ;
    ada:applicableSampleDimensionRange "missing" ;
    ada:beamHardeningCorrectionMethod "Hardware filter (LE4 inbuilt)" ;
    ada:detectorType "2000 × 2000 CCD plane (16-bit)" ;
    ada:exposureTimePerProjectionDefault "33 s (A0180-A); 28 s (A0180-B)" ;
    ada:minimumSubVolumeOverlap -9999 ;
    ada:numberOfProjectionsDefault "2401" ;
    ada:outputDataFormatDefault "missing" ;
    ada:reconstructionAlgorithm "missing" ;
    ada:reportedProperties "Microchondrule / sulphide-silicate object diameter (um) and shape factor; object abundance; particle volume" ;
    ada:rotationModeDefault "missing" ;
    ada:rotationRangeDefault "360°" ;
    ada:samplingUnit "Sub-volume > Grain (sub-samples A0180-A and A0180-B; size and shape factor reported per microchondrule / sulphide-silicate object)" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:segmentationMethodDefault "ImageJ threshold-based; TANGO plugin for 3D object detection" ;
    ada:targetFeature "Microchondrules (SSOs); 3D volume fraction" ;
    ada:xRaySourceConfiguration "missing" ;
    bios:computationalTool [ schema1:name "ImageJ + TANGO plugin (Ollion et al. 2013)" ;
            ada:toolRole "dataReduction" ] .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/detectorBinningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "No binning" ;
    schema1:name "Detector Binning" ;
    schema1:valueName "detectorBinningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/outputBitDepthDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "16-bit (CCD pixel depth)" ;
    schema1:name "Output Bit Depth" ;
    schema1:valueName "outputBitDepthDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/partialVolumeEffectCriteriaDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "SSOs ≥ 5.4 µm identified (implicit: features ≥ voxel size = 0.625 µm); sulphide rims ≥ 1 voxel required for detection" ;
    schema1:name "Partial Volume Effect Criteria" ;
    schema1:valueName "partialVolumeEffectCriteriaDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/phaseIdentificationMethodDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Sulphide rims of SSOs identified by bright contrast; silicate glass by contrast relative to matrix" ;
    schema1:name "Phase Identification Method" ;
    schema1:valueName "phaseIdentificationMethodDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleDimensionsDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "1.592 × 0.756 × 0.985 mm" ;
    schema1:name "Sample Dimensions (L × W × H)" ;
    schema1:valueName "sampleDimensionsDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleMountingMethodDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Mounted in pipette tips" ;
    schema1:name "Sample Mounting Method" ;
    schema1:valueName "sampleMountingMethodDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Optical microscopy — morphological inspection of the sample exterior through the container window with the CLOXS digital optical microscope system on automated digital sample stages at JAXA/ISAS, before the sample was decanted for nano-XCT" ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:valueName "preAnalysisImagingAndScreeningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://example.org/instrument/XCT> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "XCT" ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Zeiss" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Zeiss Versa (model not specified)" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "90 kV" ;
    ada:tubeCurrentDefault "89 µA" ;
    ada:voxelSizeDefault "0.625 µm (A0180-A); 0.672 µm (A0180-B)" ;
    ada:xRayPreFilterDefault "Inbuilt LE4 filter (beam hardening reduction)" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/detectorArraySize> a schema1:PropertyValue ;
    schema1:name "Detector Array Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/detectorArraySize> ;
    schema1:value "2000 × 2000 pixels" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/opticalObjective> a schema1:PropertyValue ;
    schema1:name "Optical Objective" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/opticalObjective> ;
    schema1:value "4× objective lens" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayTubeAnodeMaterial> a schema1:PropertyValue ;
    schema1:name "X-ray Tube Anode Material" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayTubeAnodeMaterial> ;
    schema1:value "Tungsten" .


```


### labxctTAPP example Neuman2025
labxctTAPP instance derived from Neuman et al. 2025 / Shearer et al. 2024 (JGR / Space Sci. Rev.) Apollo 17 core 73002 Multi-volume stitching NSI custom, UTCT.
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
  "@id": "ex:labxctTAPP-Neuman2025",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "labxct protocol — Neuman2025",
  "schema:description": "labxctTAPP instance derived from Neuman et al. 2025 / Shearer et al. 2024 (JGR / Space Sci. Rev.) Apollo 17 core 73002 Multi-volume stitching NSI custom, UTCT (publication column of Lab-XCT_TAPP_v37.csv). Reported detail: ada:rotationModeDefault = Continuous rotation (each Subpix sub-acquisition).",
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
            "Lunar regolith (Apollo 17 drive-tube core)"
          ]
        },
        {
          "@id": "ada:parameter/labxctTAPP/sampleDimensionsDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleDimensionsDefault",
          "schema:name": "Sample Dimensions (L × W × H)",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "~35 cm length core"
        }
      ]
    }
  ],
  "ada:targetFeature": "Voids, lithic clasts, stratigraphic layers in core",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/labxctTAPP/sampleMountingMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "sampleMountingMethodDefault",
      "schema:name": "Sample Mounting Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Plexiglass tube (vertical); triple-sealed Teflon bag"
    },
    {
      "@id": "ada:parameter/labxctTAPP/detectorArraySize",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/detectorArraySize"
        }
      ],
      "schema:name": "Detector Array Size",
      "schema:value": "2048 × 2048 (physical); 4096 × 4096 (effective, NSI Subpix)"
    },
    {
      "@id": "ada:parameter/labxctTAPP/ringArtifactCorrectionMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "ringArtifactCorrectionMethodDefault",
      "schema:name": "Ring Artifact Correction Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Post-reconstruction ring corrections applied"
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Al inner sleeve triple-sealed in Teflon; stainless-steel outer sleeve removed prior to scan",
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
            "@id": "ada:parameter/labxctTAPP/subVolumeStitchingAndRegistrationMethodDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "subVolumeStitchingAndRegistrationMethodDefault",
            "schema:name": "Sub-volume Stitching and Registration Method",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Digital stitching (method not named); post-reconstruction ring and distortion corrections applied"
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
  "ada:xRaySourceConfiguration": "Feinfocus FXE 225.48 microfocal source",
  "ada:detectorType": "2048 × 2048 Perkin Elmer flat panel (4096 × 4096 effective via Subpix)",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "XCT",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "180 kV",
      "ada:tubeCurrentDefault": "0.18 mA (180 µA)",
      "ada:xRayPreFilterDefault": "0.72 mm Al",
      "schema:manufacturer": {
        "schema:name": "North Star Imaging",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "Custom NSI instrument (North Star Imaging) at UTCT",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/XCT",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:rotationModeDefault": "Continuous rotation",
  "ada:minimumSubVolumeOverlap": "~380 slices overlap between sub-volumes",
  "ada:beamHardeningCorrectionMethod": "Software BHC applied during reconstruction",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Lab XCT"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "UTCT Facility, U. Texas"
  },
  "ada:samplingUnit": "Whole sample (six overlapping cone-beam volumes stitched into one continuous dataset per core; the sub-volumes are an acquisition unit, not a reporting unit)",
  "ada:analyticalMode": [
    "Multi-volume stitching"
  ],
  "ada:applicableSampleDimensionRange": "missing",
  "ada:exposureTimePerProjectionDefault": -9999,
  "ada:numberOfProjectionsDefault": -9999,
  "ada:outputDataFormatDefault": "missing",
  "ada:reconstructionAlgorithm": "missing",
  "ada:rotationRangeDefault": -9999,
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:segmentationMethodDefault": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XCT/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:labxctTAPP-Neuman2025",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "labxct protocol \u2014 Neuman2025",
  "schema:description": "labxctTAPP instance derived from Neuman et al. 2025 / Shearer et al. 2024 (JGR / Space Sci. Rev.) Apollo 17 core 73002 Multi-volume stitching NSI custom, UTCT (publication column of Lab-XCT_TAPP_v37.csv). Reported detail: ada:rotationModeDefault = Continuous rotation (each Subpix sub-acquisition).",
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
            "Lunar regolith (Apollo 17 drive-tube core)"
          ]
        },
        {
          "@id": "ada:parameter/labxctTAPP/sampleDimensionsDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleDimensionsDefault",
          "schema:name": "Sample Dimensions (L \u00d7 W \u00d7 H)",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "~35 cm length core"
        }
      ]
    }
  ],
  "ada:targetFeature": "Voids, lithic clasts, stratigraphic layers in core",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/labxctTAPP/sampleMountingMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "sampleMountingMethodDefault",
      "schema:name": "Sample Mounting Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Plexiglass tube (vertical); triple-sealed Teflon bag"
    },
    {
      "@id": "ada:parameter/labxctTAPP/detectorArraySize",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/detectorArraySize"
        }
      ],
      "schema:name": "Detector Array Size",
      "schema:value": "2048 \u00d7 2048 (physical); 4096 \u00d7 4096 (effective, NSI Subpix)"
    },
    {
      "@id": "ada:parameter/labxctTAPP/ringArtifactCorrectionMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "ringArtifactCorrectionMethodDefault",
      "schema:name": "Ring Artifact Correction Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Post-reconstruction ring corrections applied"
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Al inner sleeve triple-sealed in Teflon; stainless-steel outer sleeve removed prior to scan",
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
            "@id": "ada:parameter/labxctTAPP/subVolumeStitchingAndRegistrationMethodDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "subVolumeStitchingAndRegistrationMethodDefault",
            "schema:name": "Sub-volume Stitching and Registration Method",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Digital stitching (method not named); post-reconstruction ring and distortion corrections applied"
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
  "ada:xRaySourceConfiguration": "Feinfocus FXE 225.48 microfocal source",
  "ada:detectorType": "2048 \u00d7 2048 Perkin Elmer flat panel (4096 \u00d7 4096 effective via Subpix)",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "XCT",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "180 kV",
      "ada:tubeCurrentDefault": "0.18 mA (180 \u00b5A)",
      "ada:xRayPreFilterDefault": "0.72 mm Al",
      "schema:manufacturer": {
        "schema:name": "North Star Imaging",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "Custom NSI instrument (North Star Imaging) at UTCT",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/XCT",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:rotationModeDefault": "Continuous rotation",
  "ada:minimumSubVolumeOverlap": "~380 slices overlap between sub-volumes",
  "ada:beamHardeningCorrectionMethod": "Software BHC applied during reconstruction",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Lab XCT"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "UTCT Facility, U. Texas"
  },
  "ada:samplingUnit": "Whole sample (six overlapping cone-beam volumes stitched into one continuous dataset per core; the sub-volumes are an acquisition unit, not a reporting unit)",
  "ada:analyticalMode": [
    "Multi-volume stitching"
  ],
  "ada:applicableSampleDimensionRange": "missing",
  "ada:exposureTimePerProjectionDefault": -9999,
  "ada:numberOfProjectionsDefault": -9999,
  "ada:outputDataFormatDefault": "missing",
  "ada:reconstructionAlgorithm": "missing",
  "ada:rotationRangeDefault": -9999,
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:segmentationMethodDefault": "missing",
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

ex:labxctTAPP-Neuman2025 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Al inner sleeve triple-sealed in Teflon; stainless-steel outer sleeve removed prior to scan" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/subVolumeStitchingAndRegistrationMethodDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/detectorArraySize>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/ringArtifactCorrectionMethodDefault>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleMountingMethodDefault> ;
    schema1:datePublished "missing" ;
    schema1:description "labxctTAPP instance derived from Neuman et al. 2025 / Shearer et al. 2024 (JGR / Space Sci. Rev.) Apollo 17 core 73002 Multi-volume stitching NSI custom, UTCT (publication column of Lab-XCT_TAPP_v37.csv). Reported detail: ada:rotationModeDefault = Continuous rotation (each Subpix sub-acquisition)." ;
    schema1:instrument <https://example.org/instrument/XCT> ;
    schema1:location [ a schema1:Place ;
            schema1:name "UTCT Facility, U. Texas" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Lab XCT" ] ;
    schema1:name "labxct protocol — Neuman2025" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Lunar regolith (Apollo 17 drive-tube core)" ],
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleDimensionsDefault> ] ;
    ada:analyticalMode "Multi-volume stitching" ;
    ada:applicableSampleDimensionRange "missing" ;
    ada:beamHardeningCorrectionMethod "Software BHC applied during reconstruction" ;
    ada:detectorType "2048 × 2048 Perkin Elmer flat panel (4096 × 4096 effective via Subpix)" ;
    ada:exposureTimePerProjectionDefault -9999 ;
    ada:minimumSubVolumeOverlap "~380 slices overlap between sub-volumes" ;
    ada:numberOfProjectionsDefault -9999 ;
    ada:outputDataFormatDefault "missing" ;
    ada:reconstructionAlgorithm "missing" ;
    ada:rotationModeDefault "Continuous rotation" ;
    ada:rotationRangeDefault -9999 ;
    ada:samplingUnit "Whole sample (six overlapping cone-beam volumes stitched into one continuous dataset per core; the sub-volumes are an acquisition unit, not a reporting unit)" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:segmentationMethodDefault "missing" ;
    ada:targetFeature "Voids, lithic clasts, stratigraphic layers in core" ;
    ada:xRaySourceConfiguration "Feinfocus FXE 225.48 microfocal source" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/ringArtifactCorrectionMethodDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Post-reconstruction ring corrections applied" ;
    schema1:name "Ring Artifact Correction Method" ;
    schema1:valueName "ringArtifactCorrectionMethodDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleDimensionsDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "~35 cm length core" ;
    schema1:name "Sample Dimensions (L × W × H)" ;
    schema1:valueName "sampleDimensionsDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleMountingMethodDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Plexiglass tube (vertical); triple-sealed Teflon bag" ;
    schema1:name "Sample Mounting Method" ;
    schema1:valueName "sampleMountingMethodDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/subVolumeStitchingAndRegistrationMethodDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Digital stitching (method not named); post-reconstruction ring and distortion corrections applied" ;
    schema1:name "Sub-volume Stitching and Registration Method" ;
    schema1:valueName "subVolumeStitchingAndRegistrationMethodDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://example.org/instrument/XCT> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "XCT" ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "North Star Imaging" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Custom NSI instrument (North Star Imaging) at UTCT" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "180 kV" ;
    ada:tubeCurrentDefault "0.18 mA (180 µA)" ;
    ada:xRayPreFilterDefault "0.72 mm Al" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/detectorArraySize> a schema1:PropertyValue ;
    schema1:name "Detector Array Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/detectorArraySize> ;
    schema1:value "2048 × 2048 (physical); 4096 × 4096 (effective, NSI Subpix)" .


```


### labxctTAPP example Neuman2025-2
labxctTAPP instance derived from Neuman et al. 2025 (JGR Planets) Apollo 17 core 73001 Multi-volume stitching NSI custom, UTCT.
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
  "@id": "ex:labxctTAPP-Neuman2025-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "labxct protocol — Neuman2025-2",
  "schema:description": "labxctTAPP instance derived from Neuman et al. 2025 (JGR Planets) Apollo 17 core 73001 Multi-volume stitching NSI custom, UTCT (publication column of Lab-XCT_TAPP_v37.csv). Reported detail: ada:rotationModeDefault = Non-continuous rotation (to avoid rotational mismatch of continuous mode).",
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
            "Lunar regolith (Apollo 17 drive-tube core, steel sleeve)"
          ]
        },
        {
          "@id": "ada:parameter/labxctTAPP/sampleDimensionsDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleDimensionsDefault",
          "schema:name": "Sample Dimensions (L × W × H)",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "~35 cm length core"
        }
      ]
    }
  ],
  "ada:targetFeature": "Voids, lithic clasts, stratigraphic layers in core (steel-sleeved)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/labxctTAPP/sampleMountingMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "sampleMountingMethodDefault",
      "schema:name": "Sample Mounting Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Custom PVC tube"
    },
    {
      "@id": "ada:parameter/labxctTAPP/detectorArraySize",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/detectorArraySize"
        }
      ],
      "schema:name": "Detector Array Size",
      "schema:value": "2048 × 2048 (physical); 4096 × 4096 (effective, NSI Subpix)"
    },
    {
      "@id": "ada:parameter/labxctTAPP/ringArtifactCorrectionMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "ringArtifactCorrectionMethodDefault",
      "schema:name": "Ring Artifact Correction Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Post-reconstruction ring corrections applied"
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Steel outer sleeve retained for scan",
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
            "@id": "ada:parameter/labxctTAPP/subVolumeStitchingAndRegistrationMethodDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "subVolumeStitchingAndRegistrationMethodDefault",
            "schema:name": "Sub-volume Stitching and Registration Method",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Digital stitching; manual realignment of raw projection images for rotational misalignment (up to 0.35°); additional cone-beam, BH, and scattering corrections applied"
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
  "ada:xRaySourceConfiguration": "Feinfocus FXE 225.48 microfocal source",
  "ada:detectorType": "2048 × 2048 Perkin Elmer flat panel (4096 × 4096 effective via Subpix)",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "XCT",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "190 kV",
      "ada:xRayPreFilterDefault": "None (steel sleeve acts as effective filter)",
      "schema:manufacturer": {
        "schema:name": "North Star Imaging",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "Custom NSI instrument (North Star Imaging) at UTCT",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/XCT",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:rotationModeDefault": "Continuous rotation",
  "ada:beamHardeningCorrectionMethod": "Software BHC (same factor as 73002 re-used)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Lab XCT"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "UTCT Facility, U. Texas"
  },
  "ada:samplingUnit": "Whole sample (six overlapping cone-beam volumes stitched into one continuous dataset per core; the sub-volumes are an acquisition unit, not a reporting unit)",
  "ada:analyticalMode": [
    "Multi-volume stitching"
  ],
  "ada:applicableSampleDimensionRange": "missing",
  "ada:exposureTimePerProjectionDefault": -9999,
  "ada:minimumSubVolumeOverlap": -9999,
  "ada:numberOfProjectionsDefault": -9999,
  "ada:outputDataFormatDefault": "missing",
  "ada:reconstructionAlgorithm": "missing",
  "ada:rotationRangeDefault": -9999,
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:segmentationMethodDefault": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XCT/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:labxctTAPP-Neuman2025-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "labxct protocol \u2014 Neuman2025-2",
  "schema:description": "labxctTAPP instance derived from Neuman et al. 2025 (JGR Planets) Apollo 17 core 73001 Multi-volume stitching NSI custom, UTCT (publication column of Lab-XCT_TAPP_v37.csv). Reported detail: ada:rotationModeDefault = Non-continuous rotation (to avoid rotational mismatch of continuous mode).",
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
            "Lunar regolith (Apollo 17 drive-tube core, steel sleeve)"
          ]
        },
        {
          "@id": "ada:parameter/labxctTAPP/sampleDimensionsDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleDimensionsDefault",
          "schema:name": "Sample Dimensions (L \u00d7 W \u00d7 H)",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "~35 cm length core"
        }
      ]
    }
  ],
  "ada:targetFeature": "Voids, lithic clasts, stratigraphic layers in core (steel-sleeved)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/labxctTAPP/sampleMountingMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "sampleMountingMethodDefault",
      "schema:name": "Sample Mounting Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Custom PVC tube"
    },
    {
      "@id": "ada:parameter/labxctTAPP/detectorArraySize",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/detectorArraySize"
        }
      ],
      "schema:name": "Detector Array Size",
      "schema:value": "2048 \u00d7 2048 (physical); 4096 \u00d7 4096 (effective, NSI Subpix)"
    },
    {
      "@id": "ada:parameter/labxctTAPP/ringArtifactCorrectionMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "ringArtifactCorrectionMethodDefault",
      "schema:name": "Ring Artifact Correction Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Post-reconstruction ring corrections applied"
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Steel outer sleeve retained for scan",
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
            "@id": "ada:parameter/labxctTAPP/subVolumeStitchingAndRegistrationMethodDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "subVolumeStitchingAndRegistrationMethodDefault",
            "schema:name": "Sub-volume Stitching and Registration Method",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Digital stitching; manual realignment of raw projection images for rotational misalignment (up to 0.35\u00b0); additional cone-beam, BH, and scattering corrections applied"
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
  "ada:xRaySourceConfiguration": "Feinfocus FXE 225.48 microfocal source",
  "ada:detectorType": "2048 \u00d7 2048 Perkin Elmer flat panel (4096 \u00d7 4096 effective via Subpix)",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "XCT",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "190 kV",
      "ada:xRayPreFilterDefault": "None (steel sleeve acts as effective filter)",
      "schema:manufacturer": {
        "schema:name": "North Star Imaging",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "Custom NSI instrument (North Star Imaging) at UTCT",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/XCT",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:rotationModeDefault": "Continuous rotation",
  "ada:beamHardeningCorrectionMethod": "Software BHC (same factor as 73002 re-used)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Lab XCT"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "UTCT Facility, U. Texas"
  },
  "ada:samplingUnit": "Whole sample (six overlapping cone-beam volumes stitched into one continuous dataset per core; the sub-volumes are an acquisition unit, not a reporting unit)",
  "ada:analyticalMode": [
    "Multi-volume stitching"
  ],
  "ada:applicableSampleDimensionRange": "missing",
  "ada:exposureTimePerProjectionDefault": -9999,
  "ada:minimumSubVolumeOverlap": -9999,
  "ada:numberOfProjectionsDefault": -9999,
  "ada:outputDataFormatDefault": "missing",
  "ada:reconstructionAlgorithm": "missing",
  "ada:rotationRangeDefault": -9999,
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:segmentationMethodDefault": "missing",
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

ex:labxctTAPP-Neuman2025-2 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Steel outer sleeve retained for scan" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/subVolumeStitchingAndRegistrationMethodDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/detectorArraySize>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/ringArtifactCorrectionMethodDefault>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleMountingMethodDefault> ;
    schema1:datePublished "missing" ;
    schema1:description "labxctTAPP instance derived from Neuman et al. 2025 (JGR Planets) Apollo 17 core 73001 Multi-volume stitching NSI custom, UTCT (publication column of Lab-XCT_TAPP_v37.csv). Reported detail: ada:rotationModeDefault = Non-continuous rotation (to avoid rotational mismatch of continuous mode)." ;
    schema1:instrument <https://example.org/instrument/XCT> ;
    schema1:location [ a schema1:Place ;
            schema1:name "UTCT Facility, U. Texas" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Lab XCT" ] ;
    schema1:name "labxct protocol — Neuman2025-2" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Lunar regolith (Apollo 17 drive-tube core, steel sleeve)" ],
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleDimensionsDefault> ] ;
    ada:analyticalMode "Multi-volume stitching" ;
    ada:applicableSampleDimensionRange "missing" ;
    ada:beamHardeningCorrectionMethod "Software BHC (same factor as 73002 re-used)" ;
    ada:detectorType "2048 × 2048 Perkin Elmer flat panel (4096 × 4096 effective via Subpix)" ;
    ada:exposureTimePerProjectionDefault -9999 ;
    ada:minimumSubVolumeOverlap -9999 ;
    ada:numberOfProjectionsDefault -9999 ;
    ada:outputDataFormatDefault "missing" ;
    ada:reconstructionAlgorithm "missing" ;
    ada:rotationModeDefault "Continuous rotation" ;
    ada:rotationRangeDefault -9999 ;
    ada:samplingUnit "Whole sample (six overlapping cone-beam volumes stitched into one continuous dataset per core; the sub-volumes are an acquisition unit, not a reporting unit)" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:segmentationMethodDefault "missing" ;
    ada:targetFeature "Voids, lithic clasts, stratigraphic layers in core (steel-sleeved)" ;
    ada:xRaySourceConfiguration "Feinfocus FXE 225.48 microfocal source" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/ringArtifactCorrectionMethodDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Post-reconstruction ring corrections applied" ;
    schema1:name "Ring Artifact Correction Method" ;
    schema1:valueName "ringArtifactCorrectionMethodDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleDimensionsDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "~35 cm length core" ;
    schema1:name "Sample Dimensions (L × W × H)" ;
    schema1:valueName "sampleDimensionsDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleMountingMethodDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Custom PVC tube" ;
    schema1:name "Sample Mounting Method" ;
    schema1:valueName "sampleMountingMethodDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/subVolumeStitchingAndRegistrationMethodDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Digital stitching; manual realignment of raw projection images for rotational misalignment (up to 0.35°); additional cone-beam, BH, and scattering corrections applied" ;
    schema1:name "Sub-volume Stitching and Registration Method" ;
    schema1:valueName "subVolumeStitchingAndRegistrationMethodDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://example.org/instrument/XCT> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "XCT" ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "North Star Imaging" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Custom NSI instrument (North Star Imaging) at UTCT" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "190 kV" ;
    ada:xRayPreFilterDefault "None (steel sleeve acts as effective filter)" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/detectorArraySize> a schema1:PropertyValue ;
    schema1:name "Detector Array Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/detectorArraySize> ;
    schema1:value "2048 × 2048 (physical); 4096 × 4096 (effective, NSI Subpix)" .


```


### labxctTAPP example Shearer2024
labxctTAPP instance derived from Shearer et al. 2024 (Space Sci. Rev.) Apollo 17 73001 CSVC Single-volume Nikon XTH 320 NASA JSC.
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
  "@id": "ex:labxctTAPP-Shearer2024",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "labxct protocol — Shearer2024",
  "schema:description": "labxctTAPP instance derived from Shearer et al. 2024 (Space Sci. Rev.) Apollo 17 73001 CSVC Single-volume Nikon XTH 320 NASA JSC (publication column of Lab-XCT_TAPP_v37.csv).",
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
            "Lunar regolith (Apollo 17 drive-tube CSVC)"
          ]
        }
      ]
    }
  ],
  "ada:targetFeature": "Internal structure of core vacuum seal container",
  "ada:xRaySourceConfiguration": "225 kV multi-metal reflection target source",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "XCT",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "215 kV",
      "ada:tubeCurrentDefault": "179 mA (possibly typo for µA per source)",
      "ada:voxelSizeDefault": "38.49 µm voxel edge",
      "schema:manufacturer": {
        "schema:name": "Nikon",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "Nikon XTH 320",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/XCT",
      "schema:name": "example instrumentName"
    }
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Lab XCT"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "NASA JSC Astromaterials X-FaCT Lab"
  },
  "ada:samplingUnit": "Whole sample (the 73001 CSVC container assembly)",
  "ada:analyticalMode": [
    "Single-volume"
  ],
  "ada:reportedProperties": [
    "Space between the bottom tip of the CSVC and the Teflon cap; Teflon cap location and integrity (nominal)"
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
    ]
  },
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method"
    }
  ],
  "ada:applicableSampleDimensionRange": "missing",
  "ada:beamHardeningCorrectionMethod": "missing",
  "ada:detectorType": "missing",
  "ada:exposureTimePerProjectionDefault": -9999,
  "ada:minimumSubVolumeOverlap": -9999,
  "ada:numberOfProjectionsDefault": -9999,
  "ada:outputDataFormatDefault": "missing",
  "ada:reconstructionAlgorithm": "missing",
  "ada:rotationModeDefault": "missing",
  "ada:rotationRangeDefault": -9999,
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:segmentationMethodDefault": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XCT/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:labxctTAPP-Shearer2024",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "labxct protocol \u2014 Shearer2024",
  "schema:description": "labxctTAPP instance derived from Shearer et al. 2024 (Space Sci. Rev.) Apollo 17 73001 CSVC Single-volume Nikon XTH 320 NASA JSC (publication column of Lab-XCT_TAPP_v37.csv).",
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
            "Lunar regolith (Apollo 17 drive-tube CSVC)"
          ]
        }
      ]
    }
  ],
  "ada:targetFeature": "Internal structure of core vacuum seal container",
  "ada:xRaySourceConfiguration": "225 kV multi-metal reflection target source",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "XCT",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "215 kV",
      "ada:tubeCurrentDefault": "179 mA (possibly typo for \u00b5A per source)",
      "ada:voxelSizeDefault": "38.49 \u00b5m voxel edge",
      "schema:manufacturer": {
        "schema:name": "Nikon",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "Nikon XTH 320",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/XCT",
      "schema:name": "example instrumentName"
    }
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Lab XCT"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "NASA JSC Astromaterials X-FaCT Lab"
  },
  "ada:samplingUnit": "Whole sample (the 73001 CSVC container assembly)",
  "ada:analyticalMode": [
    "Single-volume"
  ],
  "ada:reportedProperties": [
    "Space between the bottom tip of the CSVC and the Teflon cap; Teflon cap location and integrity (nominal)"
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
    ]
  },
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method"
    }
  ],
  "ada:applicableSampleDimensionRange": "missing",
  "ada:beamHardeningCorrectionMethod": "missing",
  "ada:detectorType": "missing",
  "ada:exposureTimePerProjectionDefault": -9999,
  "ada:minimumSubVolumeOverlap": -9999,
  "ada:numberOfProjectionsDefault": -9999,
  "ada:outputDataFormatDefault": "missing",
  "ada:reconstructionAlgorithm": "missing",
  "ada:rotationModeDefault": "missing",
  "ada:rotationRangeDefault": -9999,
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:segmentationMethodDefault": "missing",
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

ex:labxctTAPP-Shearer2024 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "labxctTAPP instance derived from Shearer et al. 2024 (Space Sci. Rev.) Apollo 17 73001 CSVC Single-volume Nikon XTH 320 NASA JSC (publication column of Lab-XCT_TAPP_v37.csv)." ;
    schema1:instrument <https://example.org/instrument/XCT> ;
    schema1:location [ a schema1:Place ;
            schema1:name "NASA JSC Astromaterials X-FaCT Lab" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Lab XCT" ] ;
    schema1:name "labxct protocol — Shearer2024" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Lunar regolith (Apollo 17 drive-tube CSVC)" ] ] ;
    schema1:variableMeasured [ schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analyticalMode "Single-volume" ;
    ada:applicableSampleDimensionRange "missing" ;
    ada:beamHardeningCorrectionMethod "missing" ;
    ada:detectorType "missing" ;
    ada:exposureTimePerProjectionDefault -9999 ;
    ada:minimumSubVolumeOverlap -9999 ;
    ada:numberOfProjectionsDefault -9999 ;
    ada:outputDataFormatDefault "missing" ;
    ada:reconstructionAlgorithm "missing" ;
    ada:reportedProperties "Space between the bottom tip of the CSVC and the Teflon cap; Teflon cap location and integrity (nominal)" ;
    ada:rotationModeDefault "missing" ;
    ada:rotationRangeDefault -9999 ;
    ada:samplingUnit "Whole sample (the 73001 CSVC container assembly)" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:segmentationMethodDefault "missing" ;
    ada:targetFeature "Internal structure of core vacuum seal container" ;
    ada:xRaySourceConfiguration "225 kV multi-metal reflection target source" .

<https://example.org/instrument/XCT> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "XCT" ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Nikon" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Nikon XTH 320" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "215 kV" ;
    ada:tubeCurrentDefault "179 mA (possibly typo for µA per source)" ;
    ada:voxelSizeDefault "38.49 µm voxel edge" .


```


### labxctTAPP example Shearer2024-2
labxctTAPP instance derived from Shearer et al. 2024 (Space Sci. Rev.) Apollo 17 particles Single-volume Nikon XTH 320 NASA JSC X-FaCT.
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
  "@id": "ex:labxctTAPP-Shearer2024-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "labxct protocol — Shearer2024-2",
  "schema:description": "labxctTAPP instance derived from Shearer et al. 2024 (Space Sci. Rev.) Apollo 17 particles Single-volume Nikon XTH 320 NASA JSC X-FaCT (publication column of Lab-XCT_TAPP_v37.csv).",
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
            "Lunar regolith particles (Apollo 17 core)"
          ]
        }
      ]
    }
  ],
  "ada:targetFeature": "Individual particle internal structure",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/labxctTAPP/sampleMountingMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "sampleMountingMethodDefault",
      "schema:name": "Sample Mounting Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Triple-bagged in Teflon, wrapped in cylinder, placed in 1-cm plastic straw"
    },
    {
      "@id": "ada:parameter/labxctTAPP/xRayTubeAnodeMaterial",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/xRayTubeAnodeMaterial"
        }
      ],
      "schema:name": "X-ray Tube Anode Material",
      "schema:value": "Tungsten"
    },
    {
      "@id": "ada:parameter/labxctTAPP/xRayPowerDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "xRayPowerDefault",
      "schema:name": "X-ray Power",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 3.0,
      "schema:description": "3.0 W"
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Triple-bagged (Teflon) per ANGSA curation protocol",
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
  "ada:xRaySourceConfiguration": "180 kV nano-focus transmission target source",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "XCT",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "90 kV (typical; optimized per sample)",
      "ada:xRayPreFilterDefault": "0.1–0.25 mm Al (Bennu PE protocol range stated)",
      "ada:voxelSizeDefault": "2.8–20.6 µm (optimized per sample)",
      "schema:manufacturer": {
        "schema:name": "Nikon",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "Nikon XTH 320",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/XCT",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:samplingUnitSelectionCriteriaDefault": "Particles >4 mm extracted during dissection are individually bagged and XCT scanned for classification and characterization, without destructive chipping, sectioning or dust removal",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Lab XCT"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "NASA JSC Astromaterials X-FaCT Lab"
  },
  "ada:samplingUnit": "Grain (individual extracted particles >4 mm, each individually bagged and scanned)",
  "ada:analyticalMode": [
    "Single-volume"
  ],
  "ada:applicableSampleDimensionRange": "missing",
  "ada:beamHardeningCorrectionMethod": "missing",
  "ada:detectorType": "missing",
  "ada:exposureTimePerProjectionDefault": -9999,
  "ada:minimumSubVolumeOverlap": -9999,
  "ada:numberOfProjectionsDefault": -9999,
  "ada:outputDataFormatDefault": "missing",
  "ada:reconstructionAlgorithm": "missing",
  "ada:rotationModeDefault": "missing",
  "ada:rotationRangeDefault": -9999,
  "ada:segmentationMethodDefault": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XCT/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:labxctTAPP-Shearer2024-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "labxct protocol \u2014 Shearer2024-2",
  "schema:description": "labxctTAPP instance derived from Shearer et al. 2024 (Space Sci. Rev.) Apollo 17 particles Single-volume Nikon XTH 320 NASA JSC X-FaCT (publication column of Lab-XCT_TAPP_v37.csv).",
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
            "Lunar regolith particles (Apollo 17 core)"
          ]
        }
      ]
    }
  ],
  "ada:targetFeature": "Individual particle internal structure",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/labxctTAPP/sampleMountingMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "sampleMountingMethodDefault",
      "schema:name": "Sample Mounting Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Triple-bagged in Teflon, wrapped in cylinder, placed in 1-cm plastic straw"
    },
    {
      "@id": "ada:parameter/labxctTAPP/xRayTubeAnodeMaterial",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/xRayTubeAnodeMaterial"
        }
      ],
      "schema:name": "X-ray Tube Anode Material",
      "schema:value": "Tungsten"
    },
    {
      "@id": "ada:parameter/labxctTAPP/xRayPowerDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "xRayPowerDefault",
      "schema:name": "X-ray Power",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 3.0,
      "schema:description": "3.0 W"
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Triple-bagged (Teflon) per ANGSA curation protocol",
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
  "ada:xRaySourceConfiguration": "180 kV nano-focus transmission target source",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "XCT",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "90 kV (typical; optimized per sample)",
      "ada:xRayPreFilterDefault": "0.1\u20130.25 mm Al (Bennu PE protocol range stated)",
      "ada:voxelSizeDefault": "2.8\u201320.6 \u00b5m (optimized per sample)",
      "schema:manufacturer": {
        "schema:name": "Nikon",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "Nikon XTH 320",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/XCT",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:samplingUnitSelectionCriteriaDefault": "Particles >4 mm extracted during dissection are individually bagged and XCT scanned for classification and characterization, without destructive chipping, sectioning or dust removal",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Lab XCT"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "NASA JSC Astromaterials X-FaCT Lab"
  },
  "ada:samplingUnit": "Grain (individual extracted particles >4 mm, each individually bagged and scanned)",
  "ada:analyticalMode": [
    "Single-volume"
  ],
  "ada:applicableSampleDimensionRange": "missing",
  "ada:beamHardeningCorrectionMethod": "missing",
  "ada:detectorType": "missing",
  "ada:exposureTimePerProjectionDefault": -9999,
  "ada:minimumSubVolumeOverlap": -9999,
  "ada:numberOfProjectionsDefault": -9999,
  "ada:outputDataFormatDefault": "missing",
  "ada:reconstructionAlgorithm": "missing",
  "ada:rotationModeDefault": "missing",
  "ada:rotationRangeDefault": -9999,
  "ada:segmentationMethodDefault": "missing",
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

ex:labxctTAPP-Shearer2024-2 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Triple-bagged (Teflon) per ANGSA curation protocol" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleMountingMethodDefault>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayPowerDefault>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayTubeAnodeMaterial> ;
    schema1:datePublished "missing" ;
    schema1:description "labxctTAPP instance derived from Shearer et al. 2024 (Space Sci. Rev.) Apollo 17 particles Single-volume Nikon XTH 320 NASA JSC X-FaCT (publication column of Lab-XCT_TAPP_v37.csv)." ;
    schema1:instrument <https://example.org/instrument/XCT> ;
    schema1:location [ a schema1:Place ;
            schema1:name "NASA JSC Astromaterials X-FaCT Lab" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Lab XCT" ] ;
    schema1:name "labxct protocol — Shearer2024-2" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Lunar regolith particles (Apollo 17 core)" ] ] ;
    ada:analyticalMode "Single-volume" ;
    ada:applicableSampleDimensionRange "missing" ;
    ada:beamHardeningCorrectionMethod "missing" ;
    ada:detectorType "missing" ;
    ada:exposureTimePerProjectionDefault -9999 ;
    ada:minimumSubVolumeOverlap -9999 ;
    ada:numberOfProjectionsDefault -9999 ;
    ada:outputDataFormatDefault "missing" ;
    ada:reconstructionAlgorithm "missing" ;
    ada:rotationModeDefault "missing" ;
    ada:rotationRangeDefault -9999 ;
    ada:samplingUnit "Grain (individual extracted particles >4 mm, each individually bagged and scanned)" ;
    ada:samplingUnitSelectionCriteriaDefault "Particles >4 mm extracted during dissection are individually bagged and XCT scanned for classification and characterization, without destructive chipping, sectioning or dust removal" ;
    ada:segmentationMethodDefault "missing" ;
    ada:targetFeature "Individual particle internal structure" ;
    ada:xRaySourceConfiguration "180 kV nano-focus transmission target source" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleMountingMethodDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Triple-bagged in Teflon, wrapped in cylinder, placed in 1-cm plastic straw" ;
    schema1:name "Sample Mounting Method" ;
    schema1:valueName "sampleMountingMethodDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayPowerDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 3e+00 ;
    schema1:description "3.0 W" ;
    schema1:name "X-ray Power" ;
    schema1:valueName "xRayPowerDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://example.org/instrument/XCT> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "XCT" ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Nikon" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Nikon XTH 320" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "90 kV (typical; optimized per sample)" ;
    ada:voxelSizeDefault "2.8–20.6 µm (optimized per sample)" ;
    ada:xRayPreFilterDefault "0.1–0.25 mm Al (Bennu PE protocol range stated)" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayTubeAnodeMaterial> a schema1:PropertyValue ;
    schema1:name "X-ray Tube Anode Material" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayTubeAnodeMaterial> ;
    schema1:value "Tungsten" .


```


### labxctTAPP example Tomkinson2015
labxctTAPP instance derived from Tomkinson et al. 2015 (MAPS) NWA 5790 nakhlite Single-volume Nikon Metris XTH 225 U. Manchester.
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
  "@id": "ex:labxctTAPP-Tomkinson2015",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "labxct protocol — Tomkinson2015",
  "schema:description": "labxctTAPP instance derived from Tomkinson et al. 2015 (MAPS) NWA 5790 nakhlite Single-volume Nikon Metris XTH 225 U. Manchester (publication column of Lab-XCT_TAPP_v37.csv).",
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
            "Martian meteorite (nakhlite, NWA 5790)"
          ]
        },
        {
          "@id": "ada:parameter/labxctTAPP/sampleDimensionsDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleDimensionsDefault",
          "schema:name": "Sample Dimensions (L × W × H)",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "~1.1 × 1.2 × 0.8 cm"
        }
      ]
    }
  ],
  "ada:targetFeature": "Modal mineralogy (vol%); secondary minerals",
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "None; chip used as received",
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
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/labxctTAPP/xRayTubeAnodeMaterial",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/xRayTubeAnodeMaterial"
        }
      ],
      "schema:name": "X-ray Tube Anode Material",
      "schema:value": "Copper"
    },
    {
      "@id": "ada:parameter/labxctTAPP/segmentationThresholdValuesOrCriteriaDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "segmentationThresholdValuesOrCriteriaDefault",
      "schema:name": "Segmentation Threshold Values or Criteria",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Thresholds not given numerically; SEM images used to define phases; errors from threshold + subvoxel variability generally <5% for grains >125 voxels"
    },
    {
      "@id": "ada:parameter/labxctTAPP/phaseIdentificationMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "phaseIdentificationMethodDefault",
      "schema:name": "Phase Identification Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Phases: augite, mesostasis, olivine, titanomagnetite, pore space — identified by grayscale correlated to linear attenuation coefficients; verified with SEM"
    },
    {
      "@id": "ada:parameter/labxctTAPP/partialVolumeEffectCriteriaDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "partialVolumeEffectCriteriaDefault",
      "schema:name": "Partial Volume Effect Criteria",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Errors from threshold + PVE generally <5% for grains >125 voxels; features smaller than ~3 voxels unreliable"
    }
  ],
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Avizo™"
    }
  ],
  "schema:instrument": [
    {
      "schema:additionalType": [
        "XCT",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "120 keV (reported in paper as 'accelerating voltage of 120 keV'; likely typo for 120 kV)",
      "ada:voxelSizeDefault": "10.3 × 10.3 × 10.3 µm³",
      "schema:manufacturer": {
        "schema:name": "Nikon",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "Nikon Metris XTH 225",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/XCT",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:numberOfProjectionsDefault": "3143",
  "ada:exposureTimePerProjectionDefault": "20 s",
  "ada:samplingUnitSelectionCriteriaDefault": "Single 2.7 g chip (~1.1 x 1.2 x 0.8 cm) taken from the outer part of one stone, selected because it provides a profile from the weathered exterior to the fresh interior; six 2-D slices at ~1 mm spacing extracted for modal analysis",
  "ada:reconstructionAlgorithm": "Filtered back projection (Nikon proprietary)",
  "ada:segmentationMethodDefault": "Manual segmentation of 2D slices; grayscale threshold applied to 3D volume",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Lab XCT"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Manchester X-ray Imaging Facility, U. Manchester"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM-BSE (qualitative comparison)",
        "schema:description": "BSE images compared with XCT attenuation contrast"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnit": "Sub-volume (modal mineralogy reported for six 2-D XCT slices at ~1 mm spacing and for the entire chip volume)",
  "ada:analyticalMode": [
    "Single-volume"
  ],
  "ada:reportedProperties": [
    "Modal mineralogy (vol%) for augite, mesostasis, olivine and titanomagnetite; slice area (mm2)"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method"
    }
  ],
  "ada:applicableSampleDimensionRange": "missing",
  "ada:beamHardeningCorrectionMethod": "missing",
  "ada:detectorType": "missing",
  "ada:minimumSubVolumeOverlap": -9999,
  "ada:outputDataFormatDefault": "missing",
  "ada:rotationModeDefault": "missing",
  "ada:rotationRangeDefault": -9999,
  "ada:xRaySourceConfiguration": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XCT/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:labxctTAPP-Tomkinson2015",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "labxct protocol \u2014 Tomkinson2015",
  "schema:description": "labxctTAPP instance derived from Tomkinson et al. 2015 (MAPS) NWA 5790 nakhlite Single-volume Nikon Metris XTH 225 U. Manchester (publication column of Lab-XCT_TAPP_v37.csv).",
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
            "Martian meteorite (nakhlite, NWA 5790)"
          ]
        },
        {
          "@id": "ada:parameter/labxctTAPP/sampleDimensionsDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleDimensionsDefault",
          "schema:name": "Sample Dimensions (L \u00d7 W \u00d7 H)",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "~1.1 \u00d7 1.2 \u00d7 0.8 cm"
        }
      ]
    }
  ],
  "ada:targetFeature": "Modal mineralogy (vol%); secondary minerals",
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "None; chip used as received",
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
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/labxctTAPP/xRayTubeAnodeMaterial",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/xRayTubeAnodeMaterial"
        }
      ],
      "schema:name": "X-ray Tube Anode Material",
      "schema:value": "Copper"
    },
    {
      "@id": "ada:parameter/labxctTAPP/segmentationThresholdValuesOrCriteriaDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "segmentationThresholdValuesOrCriteriaDefault",
      "schema:name": "Segmentation Threshold Values or Criteria",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Thresholds not given numerically; SEM images used to define phases; errors from threshold + subvoxel variability generally <5% for grains >125 voxels"
    },
    {
      "@id": "ada:parameter/labxctTAPP/phaseIdentificationMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "phaseIdentificationMethodDefault",
      "schema:name": "Phase Identification Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Phases: augite, mesostasis, olivine, titanomagnetite, pore space \u2014 identified by grayscale correlated to linear attenuation coefficients; verified with SEM"
    },
    {
      "@id": "ada:parameter/labxctTAPP/partialVolumeEffectCriteriaDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "partialVolumeEffectCriteriaDefault",
      "schema:name": "Partial Volume Effect Criteria",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Errors from threshold + PVE generally <5% for grains >125 voxels; features smaller than ~3 voxels unreliable"
    }
  ],
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Avizo\u2122"
    }
  ],
  "schema:instrument": [
    {
      "schema:additionalType": [
        "XCT",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "120 keV (reported in paper as 'accelerating voltage of 120 keV'; likely typo for 120 kV)",
      "ada:voxelSizeDefault": "10.3 \u00d7 10.3 \u00d7 10.3 \u00b5m\u00b3",
      "schema:manufacturer": {
        "schema:name": "Nikon",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "Nikon Metris XTH 225",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/XCT",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:numberOfProjectionsDefault": "3143",
  "ada:exposureTimePerProjectionDefault": "20 s",
  "ada:samplingUnitSelectionCriteriaDefault": "Single 2.7 g chip (~1.1 x 1.2 x 0.8 cm) taken from the outer part of one stone, selected because it provides a profile from the weathered exterior to the fresh interior; six 2-D slices at ~1 mm spacing extracted for modal analysis",
  "ada:reconstructionAlgorithm": "Filtered back projection (Nikon proprietary)",
  "ada:segmentationMethodDefault": "Manual segmentation of 2D slices; grayscale threshold applied to 3D volume",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Lab XCT"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Manchester X-ray Imaging Facility, U. Manchester"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM-BSE (qualitative comparison)",
        "schema:description": "BSE images compared with XCT attenuation contrast"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnit": "Sub-volume (modal mineralogy reported for six 2-D XCT slices at ~1 mm spacing and for the entire chip volume)",
  "ada:analyticalMode": [
    "Single-volume"
  ],
  "ada:reportedProperties": [
    "Modal mineralogy (vol%) for augite, mesostasis, olivine and titanomagnetite; slice area (mm2)"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method"
    }
  ],
  "ada:applicableSampleDimensionRange": "missing",
  "ada:beamHardeningCorrectionMethod": "missing",
  "ada:detectorType": "missing",
  "ada:minimumSubVolumeOverlap": -9999,
  "ada:outputDataFormatDefault": "missing",
  "ada:rotationModeDefault": "missing",
  "ada:rotationRangeDefault": -9999,
  "ada:xRaySourceConfiguration": "missing",
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

ex:labxctTAPP-Tomkinson2015 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "None; chip used as received" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/partialVolumeEffectCriteriaDefault>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/phaseIdentificationMethodDefault>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationThresholdValuesOrCriteriaDefault>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayTubeAnodeMaterial> ;
    schema1:datePublished "missing" ;
    schema1:description "labxctTAPP instance derived from Tomkinson et al. 2015 (MAPS) NWA 5790 nakhlite Single-volume Nikon Metris XTH 225 U. Manchester (publication column of Lab-XCT_TAPP_v37.csv)." ;
    schema1:instrument <https://example.org/instrument/XCT> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Manchester X-ray Imaging Facility, U. Manchester" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Lab XCT" ] ;
    schema1:name "labxct protocol — Tomkinson2015" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Martian meteorite (nakhlite, NWA 5790)" ],
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleDimensionsDefault> ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "BSE images compared with XCT attenuation contrast" ;
                    schema1:name "SEM-BSE (qualitative comparison)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    schema1:variableMeasured [ schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analyticalMode "Single-volume" ;
    ada:applicableSampleDimensionRange "missing" ;
    ada:beamHardeningCorrectionMethod "missing" ;
    ada:detectorType "missing" ;
    ada:exposureTimePerProjectionDefault "20 s" ;
    ada:minimumSubVolumeOverlap -9999 ;
    ada:numberOfProjectionsDefault "3143" ;
    ada:outputDataFormatDefault "missing" ;
    ada:reconstructionAlgorithm "Filtered back projection (Nikon proprietary)" ;
    ada:reportedProperties "Modal mineralogy (vol%) for augite, mesostasis, olivine and titanomagnetite; slice area (mm2)" ;
    ada:rotationModeDefault "missing" ;
    ada:rotationRangeDefault -9999 ;
    ada:samplingUnit "Sub-volume (modal mineralogy reported for six 2-D XCT slices at ~1 mm spacing and for the entire chip volume)" ;
    ada:samplingUnitSelectionCriteriaDefault "Single 2.7 g chip (~1.1 x 1.2 x 0.8 cm) taken from the outer part of one stone, selected because it provides a profile from the weathered exterior to the fresh interior; six 2-D slices at ~1 mm spacing extracted for modal analysis" ;
    ada:segmentationMethodDefault "Manual segmentation of 2D slices; grayscale threshold applied to 3D volume" ;
    ada:targetFeature "Modal mineralogy (vol%); secondary minerals" ;
    ada:xRaySourceConfiguration "missing" ;
    bios:computationalTool [ schema1:name "Avizo™" ;
            ada:toolRole "dataReduction" ] .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/partialVolumeEffectCriteriaDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Errors from threshold + PVE generally <5% for grains >125 voxels; features smaller than ~3 voxels unreliable" ;
    schema1:name "Partial Volume Effect Criteria" ;
    schema1:valueName "partialVolumeEffectCriteriaDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/phaseIdentificationMethodDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Phases: augite, mesostasis, olivine, titanomagnetite, pore space — identified by grayscale correlated to linear attenuation coefficients; verified with SEM" ;
    schema1:name "Phase Identification Method" ;
    schema1:valueName "phaseIdentificationMethodDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleDimensionsDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "~1.1 × 1.2 × 0.8 cm" ;
    schema1:name "Sample Dimensions (L × W × H)" ;
    schema1:valueName "sampleDimensionsDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationThresholdValuesOrCriteriaDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Thresholds not given numerically; SEM images used to define phases; errors from threshold + subvoxel variability generally <5% for grains >125 voxels" ;
    schema1:name "Segmentation Threshold Values or Criteria" ;
    schema1:valueName "segmentationThresholdValuesOrCriteriaDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://example.org/instrument/XCT> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "XCT" ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Nikon" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Nikon Metris XTH 225" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "120 keV (reported in paper as 'accelerating voltage of 120 keV'; likely typo for 120 kV)" ;
    ada:voxelSizeDefault "10.3 × 10.3 × 10.3 µm³" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayTubeAnodeMaterial> a schema1:PropertyValue ;
    schema1:name "X-ray Tube Anode Material" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayTubeAnodeMaterial> ;
    schema1:value "Copper" .


```


### labxctTAPP example Glavin2023
labxctTAPP instance derived from Glavin et al. 2023 (MAPS) Murchison CM2 Single-volume Nikon XTH 320 NASA JSC X-FaCT.
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
  "@id": "ex:labxctTAPP-Glavin2023",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "labxct protocol — Glavin2023",
  "schema:description": "labxctTAPP instance derived from Glavin et al. 2023 (MAPS) Murchison CM2 Single-volume Nikon XTH 320 NASA JSC X-FaCT (publication column of Lab-XCT_TAPP_v37.csv).",
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
            "CM2 carbonaceous chondrite (Murchison)"
          ]
        }
      ]
    }
  ],
  "ada:targetFeature": "Radiation dose assessment (not mineralogy)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/labxctTAPP/sampleMountingMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "sampleMountingMethodDefault",
      "schema:name": "Sample Mounting Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Glass vial placed in scanner"
    },
    {
      "@id": "ada:parameter/labxctTAPP/xRayTubeAnodeMaterial",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/xRayTubeAnodeMaterial"
        }
      ],
      "schema:name": "X-ray Tube Anode Material",
      "schema:value": "Tungsten"
    },
    {
      "@id": "ada:parameter/labxctTAPP/detectorArraySize",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/detectorArraySize"
        }
      ],
      "schema:name": "Detector Array Size",
      "schema:value": "2000 × 2000 pixels"
    },
    {
      "@id": "ada:parameter/labxctTAPP/sourceToObjectDistanceDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "sourceToObjectDistanceDefault",
      "schema:name": "Source-to-Object Distance (SOD)",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 39.22,
      "schema:description": "39.22 mm"
    },
    {
      "@id": "ada:parameter/labxctTAPP/sourceToDetectorDistanceDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "sourceToDetectorDistanceDefault",
      "schema:name": "Source-to-Detector Distance (SDD)",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 679.51,
      "schema:description": "679.51 mm"
    },
    {
      "@id": "ada:parameter/labxctTAPP/rotationStepSizeDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "rotationStepSizeDefault",
      "schema:name": "Rotation Step Size",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 0.115,
      "schema:description": "0.115°"
    },
    {
      "@id": "ada:parameter/labxctTAPP/framesAveragedPerProjectionDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "framesAveragedPerProjectionDefault",
      "schema:name": "Frames Averaged per Projection",
      "ada:dataType": "integer",
      "ada:fieldScope": "session",
      "schema:defaultValue": 8,
      "schema:description": "8 frames averaged per projection"
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Chips (~10.3 g) crushed with mortar and pestle; vortex mixed 3 min; split into two ~4.6 g portions",
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
  "ada:xRaySourceConfiguration": "180 kV nano-focus tungsten transmission source (~1 µm spot size)",
  "ada:detectorType": "2000 × 2000 pixel Perkin Elmer flat panel CCD",
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Nikon CTAgentPro v5.4 (FBP algorithm)"
    }
  ],
  "schema:instrument": [
    {
      "schema:additionalType": [
        "XCT",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "160 keV (paper reports as X-ray photon energy; equivalent to 160 kV tube voltage)",
      "ada:tubeCurrentDefault": "38 µA",
      "ada:xRayPreFilterDefault": "None (intentionally unfiltered; worst-case dose experiment)",
      "ada:voxelSizeDefault": "11.54 µm (cubic voxel edge)",
      "schema:manufacturer": {
        "schema:name": "Nikon",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "Nikon XTH 320",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/XCT",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:rotationRangeDefault": "360° (continuous)",
  "ada:numberOfProjectionsDefault": "3141",
  "ada:exposureTimePerProjectionDefault": "1.00 s per frame",
  "ada:rotationModeDefault": "N/A",
  "ada:reconstructionAlgorithm": "Filtered back projection (FBP)",
  "ada:beamHardeningCorrectionMethod": "None (intentionally unfiltered; no software BHC mentioned)",
  "ada:outputDataFormatDefault": "TIFF (continuous series of 2D TIFF images)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Lab XCT"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "NASA JSC Astromaterials X-FaCT Lab"
  },
  "ada:samplingUnit": "Aliquot (~1 g crushed Murchison B in a glass vial)",
  "ada:analyticalMode": [
    "Single-volume"
  ],
  "ada:reportedProperties": [
    "Absorbed x-ray dose (~180 Gy, the maximum a Bennu sample would receive during an XCT imaging experiment)"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method"
    }
  ],
  "ada:applicableSampleDimensionRange": "missing",
  "ada:minimumSubVolumeOverlap": -9999,
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:segmentationMethodDefault": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XCT/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:labxctTAPP-Glavin2023",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "labxct protocol \u2014 Glavin2023",
  "schema:description": "labxctTAPP instance derived from Glavin et al. 2023 (MAPS) Murchison CM2 Single-volume Nikon XTH 320 NASA JSC X-FaCT (publication column of Lab-XCT_TAPP_v37.csv).",
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
            "CM2 carbonaceous chondrite (Murchison)"
          ]
        }
      ]
    }
  ],
  "ada:targetFeature": "Radiation dose assessment (not mineralogy)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/labxctTAPP/sampleMountingMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "sampleMountingMethodDefault",
      "schema:name": "Sample Mounting Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Glass vial placed in scanner"
    },
    {
      "@id": "ada:parameter/labxctTAPP/xRayTubeAnodeMaterial",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/xRayTubeAnodeMaterial"
        }
      ],
      "schema:name": "X-ray Tube Anode Material",
      "schema:value": "Tungsten"
    },
    {
      "@id": "ada:parameter/labxctTAPP/detectorArraySize",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/detectorArraySize"
        }
      ],
      "schema:name": "Detector Array Size",
      "schema:value": "2000 \u00d7 2000 pixels"
    },
    {
      "@id": "ada:parameter/labxctTAPP/sourceToObjectDistanceDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "sourceToObjectDistanceDefault",
      "schema:name": "Source-to-Object Distance (SOD)",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 39.22,
      "schema:description": "39.22 mm"
    },
    {
      "@id": "ada:parameter/labxctTAPP/sourceToDetectorDistanceDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "sourceToDetectorDistanceDefault",
      "schema:name": "Source-to-Detector Distance (SDD)",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 679.51,
      "schema:description": "679.51 mm"
    },
    {
      "@id": "ada:parameter/labxctTAPP/rotationStepSizeDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "rotationStepSizeDefault",
      "schema:name": "Rotation Step Size",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 0.115,
      "schema:description": "0.115\u00b0"
    },
    {
      "@id": "ada:parameter/labxctTAPP/framesAveragedPerProjectionDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "framesAveragedPerProjectionDefault",
      "schema:name": "Frames Averaged per Projection",
      "ada:dataType": "integer",
      "ada:fieldScope": "session",
      "schema:defaultValue": 8,
      "schema:description": "8 frames averaged per projection"
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Chips (~10.3 g) crushed with mortar and pestle; vortex mixed 3 min; split into two ~4.6 g portions",
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
  "ada:xRaySourceConfiguration": "180 kV nano-focus tungsten transmission source (~1 \u00b5m spot size)",
  "ada:detectorType": "2000 \u00d7 2000 pixel Perkin Elmer flat panel CCD",
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Nikon CTAgentPro v5.4 (FBP algorithm)"
    }
  ],
  "schema:instrument": [
    {
      "schema:additionalType": [
        "XCT",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "160 keV (paper reports as X-ray photon energy; equivalent to 160 kV tube voltage)",
      "ada:tubeCurrentDefault": "38 \u00b5A",
      "ada:xRayPreFilterDefault": "None (intentionally unfiltered; worst-case dose experiment)",
      "ada:voxelSizeDefault": "11.54 \u00b5m (cubic voxel edge)",
      "schema:manufacturer": {
        "schema:name": "Nikon",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "Nikon XTH 320",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/XCT",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:rotationRangeDefault": "360\u00b0 (continuous)",
  "ada:numberOfProjectionsDefault": "3141",
  "ada:exposureTimePerProjectionDefault": "1.00 s per frame",
  "ada:rotationModeDefault": "N/A",
  "ada:reconstructionAlgorithm": "Filtered back projection (FBP)",
  "ada:beamHardeningCorrectionMethod": "None (intentionally unfiltered; no software BHC mentioned)",
  "ada:outputDataFormatDefault": "TIFF (continuous series of 2D TIFF images)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Lab XCT"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "NASA JSC Astromaterials X-FaCT Lab"
  },
  "ada:samplingUnit": "Aliquot (~1 g crushed Murchison B in a glass vial)",
  "ada:analyticalMode": [
    "Single-volume"
  ],
  "ada:reportedProperties": [
    "Absorbed x-ray dose (~180 Gy, the maximum a Bennu sample would receive during an XCT imaging experiment)"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method"
    }
  ],
  "ada:applicableSampleDimensionRange": "missing",
  "ada:minimumSubVolumeOverlap": -9999,
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:segmentationMethodDefault": "missing",
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

ex:labxctTAPP-Glavin2023 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Chips (~10.3 g) crushed with mortar and pestle; vortex mixed 3 min; split into two ~4.6 g portions" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/detectorArraySize>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/framesAveragedPerProjectionDefault>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/rotationStepSizeDefault>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleMountingMethodDefault>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/sourceToDetectorDistanceDefault>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/sourceToObjectDistanceDefault>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayTubeAnodeMaterial> ;
    schema1:datePublished "missing" ;
    schema1:description "labxctTAPP instance derived from Glavin et al. 2023 (MAPS) Murchison CM2 Single-volume Nikon XTH 320 NASA JSC X-FaCT (publication column of Lab-XCT_TAPP_v37.csv)." ;
    schema1:instrument <https://example.org/instrument/XCT> ;
    schema1:location [ a schema1:Place ;
            schema1:name "NASA JSC Astromaterials X-FaCT Lab" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Lab XCT" ] ;
    schema1:name "labxct protocol — Glavin2023" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "CM2 carbonaceous chondrite (Murchison)" ] ] ;
    schema1:variableMeasured [ schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analyticalMode "Single-volume" ;
    ada:applicableSampleDimensionRange "missing" ;
    ada:beamHardeningCorrectionMethod "None (intentionally unfiltered; no software BHC mentioned)" ;
    ada:detectorType "2000 × 2000 pixel Perkin Elmer flat panel CCD" ;
    ada:exposureTimePerProjectionDefault "1.00 s per frame" ;
    ada:minimumSubVolumeOverlap -9999 ;
    ada:numberOfProjectionsDefault "3141" ;
    ada:outputDataFormatDefault "TIFF (continuous series of 2D TIFF images)" ;
    ada:reconstructionAlgorithm "Filtered back projection (FBP)" ;
    ada:reportedProperties "Absorbed x-ray dose (~180 Gy, the maximum a Bennu sample would receive during an XCT imaging experiment)" ;
    ada:rotationModeDefault "N/A" ;
    ada:rotationRangeDefault "360° (continuous)" ;
    ada:samplingUnit "Aliquot (~1 g crushed Murchison B in a glass vial)" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:segmentationMethodDefault "missing" ;
    ada:targetFeature "Radiation dose assessment (not mineralogy)" ;
    ada:xRaySourceConfiguration "180 kV nano-focus tungsten transmission source (~1 µm spot size)" ;
    bios:computationalTool [ schema1:name "Nikon CTAgentPro v5.4 (FBP algorithm)" ;
            ada:toolRole "dataReduction" ] .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/framesAveragedPerProjectionDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 8 ;
    schema1:description "8 frames averaged per projection" ;
    schema1:name "Frames Averaged per Projection" ;
    schema1:valueName "framesAveragedPerProjectionDefault" ;
    ada:dataType "integer" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/rotationStepSizeDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1.15e-01 ;
    schema1:description "0.115°" ;
    schema1:name "Rotation Step Size" ;
    schema1:valueName "rotationStepSizeDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleMountingMethodDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Glass vial placed in scanner" ;
    schema1:name "Sample Mounting Method" ;
    schema1:valueName "sampleMountingMethodDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/sourceToDetectorDistanceDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 6.7951e+02 ;
    schema1:description "679.51 mm" ;
    schema1:name "Source-to-Detector Distance (SDD)" ;
    schema1:valueName "sourceToDetectorDistanceDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/sourceToObjectDistanceDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 3.922e+01 ;
    schema1:description "39.22 mm" ;
    schema1:name "Source-to-Object Distance (SOD)" ;
    schema1:valueName "sourceToObjectDistanceDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://example.org/instrument/XCT> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "XCT" ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Nikon" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Nikon XTH 320" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "160 keV (paper reports as X-ray photon energy; equivalent to 160 kV tube voltage)" ;
    ada:tubeCurrentDefault "38 µA" ;
    ada:voxelSizeDefault "11.54 µm (cubic voxel edge)" ;
    ada:xRayPreFilterDefault "None (intentionally unfiltered; worst-case dose experiment)" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/detectorArraySize> a schema1:PropertyValue ;
    schema1:name "Detector Array Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/detectorArraySize> ;
    schema1:value "2000 × 2000 pixels" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayTubeAnodeMaterial> a schema1:PropertyValue ;
    schema1:name "X-ray Tube Anode Material" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayTubeAnodeMaterial> ;
    schema1:value "Tungsten" .


```


### labxctTAPP example Dias2019
labxctTAPP instance derived from Nascimento-Dias et al. 2019 (Appl. Radiat. Isot.) NWA 8277 + NWA 6963 Single-volume Bruker Skyscan 1173.
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
  "@id": "ex:labxctTAPP-Dias2019",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "labxct protocol — Dias2019",
  "schema:description": "labxctTAPP instance derived from Nascimento-Dias et al. 2019 (Appl. Radiat. Isot.) NWA 8277 + NWA 6963 Single-volume Bruker Skyscan 1173 (publication column of Lab-XCT_TAPP_v37.csv).",
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
            "Lunar meteorite (NWA 8277); Martian meteorite (NWA 6963)"
          ]
        },
        {
          "@id": "ada:parameter/labxctTAPP/sampleDimensionsDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleDimensionsDefault",
          "schema:name": "Sample Dimensions (L × W × H)",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "~4 mm fragments"
        }
      ]
    }
  ],
  "ada:targetFeature": "Internal structure; porosity; density contrast",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/labxctTAPP/sampleMountingMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "sampleMountingMethodDefault",
      "schema:name": "Sample Mounting Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Polystyrene support"
    },
    {
      "@id": "ada:parameter/labxctTAPP/detectorArraySize",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/detectorArraySize"
        }
      ],
      "schema:name": "Detector Array Size",
      "schema:value": "2240 × 2240 pixels"
    },
    {
      "@id": "ada:parameter/labxctTAPP/rotationStepSizeDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "rotationStepSizeDefault",
      "schema:name": "Rotation Step Size",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 0.4,
      "schema:description": "0.4°/step"
    },
    {
      "@id": "ada:parameter/labxctTAPP/segmentationThresholdValuesOrCriteriaDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "segmentationThresholdValuesOrCriteriaDefault",
      "schema:name": "Segmentation Threshold Values or Criteria",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Adaptive mean threshold; total analyzed VOI for NWA 8277 = 5.39 mm³"
    },
    {
      "@id": "ada:parameter/labxctTAPP/phaseIdentificationMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "phaseIdentificationMethodDefault",
      "schema:name": "Phase Identification Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Three density regions: high, medium, low density; porosity separate"
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "None stated (fragments purchased from IMCA member)",
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
  "ada:detectorType": "Flat panel detector (2240 × 2240 pixels)",
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "DataViewer; CTVox; CTAn (Bruker proprietary suite)"
    }
  ],
  "schema:instrument": [
    {
      "schema:additionalType": [
        "XCT",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "50 kV",
      "ada:tubeCurrentDefault": "160 µA",
      "ada:xRayPreFilterDefault": "1.0 mm aluminum",
      "ada:voxelSizeDefault": "5.34 µm",
      "schema:manufacturer": {
        "schema:name": "Bruker",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "Bruker/Skyscan 1173",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/XCT",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:rotationRangeDefault": "360°",
  "ada:beamHardeningCorrectionMethod": "Hardware filter (1.0 mm Al); software BHC in NRecon not mentioned",
  "ada:segmentationMethodDefault": "Adaptive (mean) thresholding",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Lab XCT"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Nuclear Instrumentation Lab, COPPE, UFRJ, Brazil"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Micro-XRF (same samples)",
        "schema:description": "Micro-XRF performed on same meteorite fragments after XCT"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnit": "Whole sample (one scan per meteorite specimen: NWA 8277, NWA 6963)",
  "ada:analyticalMode": [
    "Single-volume"
  ],
  "ada:reportedProperties": [
    "Density and porosity; proportions, volume, size, shape and spatial distribution of internal structure"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method"
    }
  ],
  "ada:applicableSampleDimensionRange": "missing",
  "ada:exposureTimePerProjectionDefault": -9999,
  "ada:minimumSubVolumeOverlap": -9999,
  "ada:numberOfProjectionsDefault": -9999,
  "ada:outputDataFormatDefault": "missing",
  "ada:reconstructionAlgorithm": "missing",
  "ada:rotationModeDefault": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:xRaySourceConfiguration": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XCT/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:labxctTAPP-Dias2019",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "labxct protocol \u2014 Dias2019",
  "schema:description": "labxctTAPP instance derived from Nascimento-Dias et al. 2019 (Appl. Radiat. Isot.) NWA 8277 + NWA 6963 Single-volume Bruker Skyscan 1173 (publication column of Lab-XCT_TAPP_v37.csv).",
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
            "Lunar meteorite (NWA 8277); Martian meteorite (NWA 6963)"
          ]
        },
        {
          "@id": "ada:parameter/labxctTAPP/sampleDimensionsDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleDimensionsDefault",
          "schema:name": "Sample Dimensions (L \u00d7 W \u00d7 H)",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "~4 mm fragments"
        }
      ]
    }
  ],
  "ada:targetFeature": "Internal structure; porosity; density contrast",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/labxctTAPP/sampleMountingMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "sampleMountingMethodDefault",
      "schema:name": "Sample Mounting Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Polystyrene support"
    },
    {
      "@id": "ada:parameter/labxctTAPP/detectorArraySize",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/detectorArraySize"
        }
      ],
      "schema:name": "Detector Array Size",
      "schema:value": "2240 \u00d7 2240 pixels"
    },
    {
      "@id": "ada:parameter/labxctTAPP/rotationStepSizeDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "rotationStepSizeDefault",
      "schema:name": "Rotation Step Size",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 0.4,
      "schema:description": "0.4\u00b0/step"
    },
    {
      "@id": "ada:parameter/labxctTAPP/segmentationThresholdValuesOrCriteriaDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "segmentationThresholdValuesOrCriteriaDefault",
      "schema:name": "Segmentation Threshold Values or Criteria",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Adaptive mean threshold; total analyzed VOI for NWA 8277 = 5.39 mm\u00b3"
    },
    {
      "@id": "ada:parameter/labxctTAPP/phaseIdentificationMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "phaseIdentificationMethodDefault",
      "schema:name": "Phase Identification Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Three density regions: high, medium, low density; porosity separate"
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "None stated (fragments purchased from IMCA member)",
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
  "ada:detectorType": "Flat panel detector (2240 \u00d7 2240 pixels)",
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "DataViewer; CTVox; CTAn (Bruker proprietary suite)"
    }
  ],
  "schema:instrument": [
    {
      "schema:additionalType": [
        "XCT",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "50 kV",
      "ada:tubeCurrentDefault": "160 \u00b5A",
      "ada:xRayPreFilterDefault": "1.0 mm aluminum",
      "ada:voxelSizeDefault": "5.34 \u00b5m",
      "schema:manufacturer": {
        "schema:name": "Bruker",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "Bruker/Skyscan 1173",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/XCT",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:rotationRangeDefault": "360\u00b0",
  "ada:beamHardeningCorrectionMethod": "Hardware filter (1.0 mm Al); software BHC in NRecon not mentioned",
  "ada:segmentationMethodDefault": "Adaptive (mean) thresholding",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Lab XCT"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Nuclear Instrumentation Lab, COPPE, UFRJ, Brazil"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Micro-XRF (same samples)",
        "schema:description": "Micro-XRF performed on same meteorite fragments after XCT"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnit": "Whole sample (one scan per meteorite specimen: NWA 8277, NWA 6963)",
  "ada:analyticalMode": [
    "Single-volume"
  ],
  "ada:reportedProperties": [
    "Density and porosity; proportions, volume, size, shape and spatial distribution of internal structure"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method"
    }
  ],
  "ada:applicableSampleDimensionRange": "missing",
  "ada:exposureTimePerProjectionDefault": -9999,
  "ada:minimumSubVolumeOverlap": -9999,
  "ada:numberOfProjectionsDefault": -9999,
  "ada:outputDataFormatDefault": "missing",
  "ada:reconstructionAlgorithm": "missing",
  "ada:rotationModeDefault": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:xRaySourceConfiguration": "missing",
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

ex:labxctTAPP-Dias2019 a cdi:Activity,
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
                    schema1:description "None stated (fragments purchased from IMCA member)" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/detectorArraySize>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/phaseIdentificationMethodDefault>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/rotationStepSizeDefault>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleMountingMethodDefault>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationThresholdValuesOrCriteriaDefault> ;
    schema1:datePublished "missing" ;
    schema1:description "labxctTAPP instance derived from Nascimento-Dias et al. 2019 (Appl. Radiat. Isot.) NWA 8277 + NWA 6963 Single-volume Bruker Skyscan 1173 (publication column of Lab-XCT_TAPP_v37.csv)." ;
    schema1:instrument <https://example.org/instrument/XCT> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Nuclear Instrumentation Lab, COPPE, UFRJ, Brazil" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Lab XCT" ] ;
    schema1:name "labxct protocol — Dias2019" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Lunar meteorite (NWA 8277); Martian meteorite (NWA 6963)" ],
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleDimensionsDefault> ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "Micro-XRF performed on same meteorite fragments after XCT" ;
                    schema1:name "Micro-XRF (same samples)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    schema1:variableMeasured [ schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analyticalMode "Single-volume" ;
    ada:applicableSampleDimensionRange "missing" ;
    ada:beamHardeningCorrectionMethod "Hardware filter (1.0 mm Al); software BHC in NRecon not mentioned" ;
    ada:detectorType "Flat panel detector (2240 × 2240 pixels)" ;
    ada:exposureTimePerProjectionDefault -9999 ;
    ada:minimumSubVolumeOverlap -9999 ;
    ada:numberOfProjectionsDefault -9999 ;
    ada:outputDataFormatDefault "missing" ;
    ada:reconstructionAlgorithm "missing" ;
    ada:reportedProperties "Density and porosity; proportions, volume, size, shape and spatial distribution of internal structure" ;
    ada:rotationModeDefault "missing" ;
    ada:rotationRangeDefault "360°" ;
    ada:samplingUnit "Whole sample (one scan per meteorite specimen: NWA 8277, NWA 6963)" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:segmentationMethodDefault "Adaptive (mean) thresholding" ;
    ada:targetFeature "Internal structure; porosity; density contrast" ;
    ada:xRaySourceConfiguration "missing" ;
    bios:computationalTool [ schema1:name "DataViewer; CTVox; CTAn (Bruker proprietary suite)" ;
            ada:toolRole "dataReduction" ] .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/phaseIdentificationMethodDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Three density regions: high, medium, low density; porosity separate" ;
    schema1:name "Phase Identification Method" ;
    schema1:valueName "phaseIdentificationMethodDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/rotationStepSizeDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 4e-01 ;
    schema1:description "0.4°/step" ;
    schema1:name "Rotation Step Size" ;
    schema1:valueName "rotationStepSizeDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleDimensionsDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "~4 mm fragments" ;
    schema1:name "Sample Dimensions (L × W × H)" ;
    schema1:valueName "sampleDimensionsDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleMountingMethodDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Polystyrene support" ;
    schema1:name "Sample Mounting Method" ;
    schema1:valueName "sampleMountingMethodDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationThresholdValuesOrCriteriaDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Adaptive mean threshold; total analyzed VOI for NWA 8277 = 5.39 mm³" ;
    schema1:name "Segmentation Threshold Values or Criteria" ;
    schema1:valueName "segmentationThresholdValuesOrCriteriaDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://example.org/instrument/XCT> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "XCT" ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Bruker" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Bruker/Skyscan 1173" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "50 kV" ;
    ada:tubeCurrentDefault "160 µA" ;
    ada:voxelSizeDefault "5.34 µm" ;
    ada:xRayPreFilterDefault "1.0 mm aluminum" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/detectorArraySize> a schema1:PropertyValue ;
    schema1:name "Detector Array Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/detectorArraySize> ;
    schema1:value "2240 × 2240 pixels" .


```


### labxctTAPP example Richard2019
labxctTAPP instance derived from Richard et al. 2019 (Chem. Geol.) Olivine (melt incl.) Single-volume Zeiss Xradia 510 Versa UNAM Mexico.
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
  "@id": "ex:labxctTAPP-Richard2019",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "labxct protocol — Richard2019",
  "schema:description": "labxctTAPP instance derived from Richard et al. 2019 (Chem. Geol.) Olivine (melt incl.) Single-volume Zeiss Xradia 510 Versa UNAM Mexico (publication column of Lab-XCT_TAPP_v37.csv).",
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
            "Olivine phenocryst with silicate melt inclusion"
          ]
        },
        {
          "@id": "ada:parameter/labxctTAPP/sampleDimensionsDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleDimensionsDefault",
          "schema:name": "Sample Dimensions (L × W × H)",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "~1 mm olivine"
        }
      ]
    }
  ],
  "ada:targetFeature": "Silicate melt inclusion morphology and phase volumes",
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "None stated for XCT; embedded in epoxy after XCT for microprobe",
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
  "ada:detectorType": "CCD ANDOR camera (1080 × 1080 px, 32-bit)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/labxctTAPP/detectorArraySize",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/detectorArraySize"
        }
      ],
      "schema:name": "Detector Array Size",
      "schema:value": "1080 × 1080 pixels"
    },
    {
      "@id": "ada:parameter/labxctTAPP/opticalObjective",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/opticalObjective"
        }
      ],
      "schema:name": "Optical Objective",
      "schema:value": "4.0× magnification"
    },
    {
      "@id": "ada:parameter/labxctTAPP/framesAveragedPerProjectionDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "framesAveragedPerProjectionDefault",
      "schema:name": "Frames Averaged per Projection",
      "ada:dataType": "integer",
      "ada:fieldScope": "session",
      "schema:defaultValue": 200,
      "schema:description": "~200 reference (blank) images taken; number of frames averaged per projection N"
    },
    {
      "@id": "ada:parameter/labxctTAPP/segmentationThresholdValuesOrCriteriaDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "segmentationThresholdValuesOrCriteriaDefault",
      "schema:name": "Segmentation Threshold Values or Criteria",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Threshold range selected to include all voxels of one phase while excluding adjacent phases; specific values N"
    },
    {
      "@id": "ada:parameter/labxctTAPP/phaseIdentificationMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "phaseIdentificationMethodDefault",
      "schema:name": "Phase Identification Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Phase identified by grayscale contrast (vapor vs. silicate/mineral)"
    },
    {
      "@id": "ada:parameter/labxctTAPP/outputBitDepthDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "outputBitDepthDefault",
      "schema:name": "Output Bit Depth",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "32-bit (ZEISS XRM output)"
    }
  ],
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "ImageJ; Avizo 9.2"
    }
  ],
  "schema:instrument": [
    {
      "schema:additionalType": [
        "XCT",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "30 kV",
      "ada:voxelSizeDefault": "2.06 µm/px",
      "schema:manufacturer": {
        "schema:name": "Zeiss",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "Zeiss Xradia 510 Versa",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/XCT",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:numberOfProjectionsDefault": "1601",
  "ada:exposureTimePerProjectionDefault": "8 s",
  "ada:segmentationMethodDefault": "Grayscale threshold range selection (ImageJ)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Lab XCT (nano-CT)"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Lab. de Microtomografía de Rayos X, UNAM, Mexico"
  },
  "ada:samplingUnit": "Region of interest (individual melt inclusion) > Phase (glass, clinopyroxene, spinel, vapour)",
  "ada:analyticalMode": [
    "Single-volume"
  ],
  "ada:reportedProperties": [
    "Phase volumes within the melt inclusion (glass, clinopyroxene, spinel, vapour)"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method"
    }
  ],
  "ada:applicableSampleDimensionRange": "missing",
  "ada:beamHardeningCorrectionMethod": "missing",
  "ada:minimumSubVolumeOverlap": -9999,
  "ada:outputDataFormatDefault": "missing",
  "ada:reconstructionAlgorithm": "missing",
  "ada:rotationModeDefault": "missing",
  "ada:rotationRangeDefault": -9999,
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:xRaySourceConfiguration": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XCT/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:labxctTAPP-Richard2019",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "labxct protocol \u2014 Richard2019",
  "schema:description": "labxctTAPP instance derived from Richard et al. 2019 (Chem. Geol.) Olivine (melt incl.) Single-volume Zeiss Xradia 510 Versa UNAM Mexico (publication column of Lab-XCT_TAPP_v37.csv).",
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
            "Olivine phenocryst with silicate melt inclusion"
          ]
        },
        {
          "@id": "ada:parameter/labxctTAPP/sampleDimensionsDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleDimensionsDefault",
          "schema:name": "Sample Dimensions (L \u00d7 W \u00d7 H)",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "~1 mm olivine"
        }
      ]
    }
  ],
  "ada:targetFeature": "Silicate melt inclusion morphology and phase volumes",
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "None stated for XCT; embedded in epoxy after XCT for microprobe",
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
  "ada:detectorType": "CCD ANDOR camera (1080 \u00d7 1080 px, 32-bit)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/labxctTAPP/detectorArraySize",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/detectorArraySize"
        }
      ],
      "schema:name": "Detector Array Size",
      "schema:value": "1080 \u00d7 1080 pixels"
    },
    {
      "@id": "ada:parameter/labxctTAPP/opticalObjective",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/opticalObjective"
        }
      ],
      "schema:name": "Optical Objective",
      "schema:value": "4.0\u00d7 magnification"
    },
    {
      "@id": "ada:parameter/labxctTAPP/framesAveragedPerProjectionDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "framesAveragedPerProjectionDefault",
      "schema:name": "Frames Averaged per Projection",
      "ada:dataType": "integer",
      "ada:fieldScope": "session",
      "schema:defaultValue": 200,
      "schema:description": "~200 reference (blank) images taken; number of frames averaged per projection N"
    },
    {
      "@id": "ada:parameter/labxctTAPP/segmentationThresholdValuesOrCriteriaDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "segmentationThresholdValuesOrCriteriaDefault",
      "schema:name": "Segmentation Threshold Values or Criteria",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Threshold range selected to include all voxels of one phase while excluding adjacent phases; specific values N"
    },
    {
      "@id": "ada:parameter/labxctTAPP/phaseIdentificationMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "phaseIdentificationMethodDefault",
      "schema:name": "Phase Identification Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Phase identified by grayscale contrast (vapor vs. silicate/mineral)"
    },
    {
      "@id": "ada:parameter/labxctTAPP/outputBitDepthDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "outputBitDepthDefault",
      "schema:name": "Output Bit Depth",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "32-bit (ZEISS XRM output)"
    }
  ],
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "ImageJ; Avizo 9.2"
    }
  ],
  "schema:instrument": [
    {
      "schema:additionalType": [
        "XCT",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "30 kV",
      "ada:voxelSizeDefault": "2.06 \u00b5m/px",
      "schema:manufacturer": {
        "schema:name": "Zeiss",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "Zeiss Xradia 510 Versa",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/XCT",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:numberOfProjectionsDefault": "1601",
  "ada:exposureTimePerProjectionDefault": "8 s",
  "ada:segmentationMethodDefault": "Grayscale threshold range selection (ImageJ)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Lab XCT (nano-CT)"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Lab. de Microtomograf\u00eda de Rayos X, UNAM, Mexico"
  },
  "ada:samplingUnit": "Region of interest (individual melt inclusion) > Phase (glass, clinopyroxene, spinel, vapour)",
  "ada:analyticalMode": [
    "Single-volume"
  ],
  "ada:reportedProperties": [
    "Phase volumes within the melt inclusion (glass, clinopyroxene, spinel, vapour)"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method"
    }
  ],
  "ada:applicableSampleDimensionRange": "missing",
  "ada:beamHardeningCorrectionMethod": "missing",
  "ada:minimumSubVolumeOverlap": -9999,
  "ada:outputDataFormatDefault": "missing",
  "ada:reconstructionAlgorithm": "missing",
  "ada:rotationModeDefault": "missing",
  "ada:rotationRangeDefault": -9999,
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:xRaySourceConfiguration": "missing",
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

ex:labxctTAPP-Richard2019 a cdi:Activity,
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
                    schema1:description "None stated for XCT; embedded in epoxy after XCT for microprobe" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/detectorArraySize>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/framesAveragedPerProjectionDefault>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/opticalObjective>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/outputBitDepthDefault>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/phaseIdentificationMethodDefault>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationThresholdValuesOrCriteriaDefault> ;
    schema1:datePublished "missing" ;
    schema1:description "labxctTAPP instance derived from Richard et al. 2019 (Chem. Geol.) Olivine (melt incl.) Single-volume Zeiss Xradia 510 Versa UNAM Mexico (publication column of Lab-XCT_TAPP_v37.csv)." ;
    schema1:instrument <https://example.org/instrument/XCT> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Lab. de Microtomografía de Rayos X, UNAM, Mexico" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Lab XCT (nano-CT)" ] ;
    schema1:name "labxct protocol — Richard2019" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Olivine phenocryst with silicate melt inclusion" ],
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleDimensionsDefault> ] ;
    schema1:variableMeasured [ schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analyticalMode "Single-volume" ;
    ada:applicableSampleDimensionRange "missing" ;
    ada:beamHardeningCorrectionMethod "missing" ;
    ada:detectorType "CCD ANDOR camera (1080 × 1080 px, 32-bit)" ;
    ada:exposureTimePerProjectionDefault "8 s" ;
    ada:minimumSubVolumeOverlap -9999 ;
    ada:numberOfProjectionsDefault "1601" ;
    ada:outputDataFormatDefault "missing" ;
    ada:reconstructionAlgorithm "missing" ;
    ada:reportedProperties "Phase volumes within the melt inclusion (glass, clinopyroxene, spinel, vapour)" ;
    ada:rotationModeDefault "missing" ;
    ada:rotationRangeDefault -9999 ;
    ada:samplingUnit "Region of interest (individual melt inclusion) > Phase (glass, clinopyroxene, spinel, vapour)" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:segmentationMethodDefault "Grayscale threshold range selection (ImageJ)" ;
    ada:targetFeature "Silicate melt inclusion morphology and phase volumes" ;
    ada:xRaySourceConfiguration "missing" ;
    bios:computationalTool [ schema1:name "ImageJ; Avizo 9.2" ;
            ada:toolRole "dataReduction" ] .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/framesAveragedPerProjectionDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 200 ;
    schema1:description "~200 reference (blank) images taken; number of frames averaged per projection N" ;
    schema1:name "Frames Averaged per Projection" ;
    schema1:valueName "framesAveragedPerProjectionDefault" ;
    ada:dataType "integer" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/outputBitDepthDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "32-bit (ZEISS XRM output)" ;
    schema1:name "Output Bit Depth" ;
    schema1:valueName "outputBitDepthDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/phaseIdentificationMethodDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Phase identified by grayscale contrast (vapor vs. silicate/mineral)" ;
    schema1:name "Phase Identification Method" ;
    schema1:valueName "phaseIdentificationMethodDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleDimensionsDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "~1 mm olivine" ;
    schema1:name "Sample Dimensions (L × W × H)" ;
    schema1:valueName "sampleDimensionsDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationThresholdValuesOrCriteriaDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Threshold range selected to include all voxels of one phase while excluding adjacent phases; specific values N" ;
    schema1:name "Segmentation Threshold Values or Criteria" ;
    schema1:valueName "segmentationThresholdValuesOrCriteriaDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://example.org/instrument/XCT> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "XCT" ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Zeiss" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Zeiss Xradia 510 Versa" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "30 kV" ;
    ada:voxelSizeDefault "2.06 µm/px" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/detectorArraySize> a schema1:PropertyValue ;
    schema1:name "Detector Array Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/detectorArraySize> ;
    schema1:value "1080 × 1080 pixels" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/opticalObjective> a schema1:PropertyValue ;
    schema1:name "Optical Objective" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/opticalObjective> ;
    schema1:value "4.0× magnification" .


```


### labxctTAPP example Richard2019-2
labxctTAPP instance derived from Richard et al. 2019 (Chem. Geol.) Synthetic quartz (fluid incl.) Whole sample (low-res) Nikon XTH 320/225 U. Strathclyde.
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
  "@id": "ex:labxctTAPP-Richard2019-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "labxct protocol — Richard2019-2",
  "schema:description": "labxctTAPP instance derived from Richard et al. 2019 (Chem. Geol.) Synthetic quartz (fluid incl.) Whole sample (low-res) Nikon XTH 320/225 U. Strathclyde (publication column of Lab-XCT_TAPP_v37.csv).",
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
            "Synthetic quartz monocrystal with aqueous fluid inclusions"
          ]
        },
        {
          "@id": "ada:parameter/labxctTAPP/sampleDimensionsDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleDimensionsDefault",
          "schema:name": "Sample Dimensions (L × W × H)",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "3 × 5 × 2 cm"
        },
        {
          "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "preAnalysisImagingAndScreeningDefault",
          "schema:name": "Pre-Analysis Imaging and Screening",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Optical photography of the sample showing the fluid inclusion array, with inclusions numbered for correspondence with the HRXCT reconstruction (Fig. 2)"
        }
      ]
    }
  ],
  "ada:targetFeature": "Fluid inclusion morphology and phase volumes",
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "None stated",
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
  "ada:xRaySourceConfiguration": "Microfocus multi-metal target (225 kV)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/labxctTAPP/xRayTubeAnodeMaterial",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/xRayTubeAnodeMaterial"
        }
      ],
      "schema:name": "X-ray Tube Anode Material",
      "schema:value": "Silver (for Sample B)"
    },
    {
      "@id": "ada:parameter/labxctTAPP/detectorArraySize",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/detectorArraySize"
        }
      ],
      "schema:name": "Detector Array Size",
      "schema:value": "2000 × 2000 pixels"
    },
    {
      "@id": "ada:parameter/labxctTAPP/detectorPixelSize",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/detectorPixelSize"
        }
      ],
      "schema:name": "Detector Pixel Size",
      "schema:value": 0.2,
      "schema:unitText": "example value",
      "schema:description": "0.2 × 0.2 mm cell size"
    },
    {
      "@id": "ada:parameter/labxctTAPP/xRayPowerDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "xRayPowerDefault",
      "schema:name": "X-ray Power",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 11.4,
      "schema:description": "11.4 W"
    },
    {
      "@id": "ada:parameter/labxctTAPP/framesAveragedPerProjectionDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "framesAveragedPerProjectionDefault",
      "schema:name": "Frames Averaged per Projection",
      "ada:dataType": "integer",
      "ada:fieldScope": "session",
      "schema:defaultValue": 1,
      "schema:description": "1 frame per projection"
    },
    {
      "@id": "ada:parameter/labxctTAPP/segmentationThresholdValuesOrCriteriaDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "segmentationThresholdValuesOrCriteriaDefault",
      "schema:name": "Segmentation Threshold Values or Criteria",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Manual threshold: vapor = darker, liquid = brighter pixels; specific values N"
    },
    {
      "@id": "ada:parameter/labxctTAPP/phaseIdentificationMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "phaseIdentificationMethodDefault",
      "schema:name": "Phase Identification Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Phase identified by grayscale contrast (vapor darker, liquid brighter)"
    }
  ],
  "ada:detectorType": "Flat panel photodetector (2000 × 2000 px, cell size 0.2 × 0.2 mm)",
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Avizo 9.2.0"
    }
  ],
  "schema:instrument": [
    {
      "schema:additionalType": [
        "XCT",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "160 kV",
      "ada:tubeCurrentDefault": "71 µA (Ag target)",
      "ada:xRayPreFilterDefault": "None (conditions did not require filtering)",
      "ada:voxelSizeDefault": "25 µm",
      "schema:manufacturer": {
        "schema:name": "Nikon",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "Nikon XTH 320/225",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/XCT",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:numberOfProjectionsDefault": "3141",
  "ada:exposureTimePerProjectionDefault": "0.708 s",
  "ada:samplingUnitSelectionCriteriaDefault": "No sectioning was carried out prior to HRXCT scanning; Sample B was scanned entirely",
  "ada:beamHardeningCorrectionMethod": "None (conditions did not saturate detector; not required)",
  "ada:segmentationMethodDefault": "Manual grayscale threshold",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Lab XCT"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "U. Strathclyde, Glasgow, UK"
  },
  "ada:samplingUnit": "Region of interest (individual fluid inclusion) > Phase (vapour, liquid)",
  "ada:analyticalMode": [
    "Single-volume"
  ],
  "ada:reportedProperties": [
    "Total fluid inclusion volume (mm3); vapour volume (mm3); liquid volume (mm3); vapour volumetric fraction phi_vap (%)"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method"
    }
  ],
  "ada:applicableSampleDimensionRange": "missing",
  "ada:minimumSubVolumeOverlap": -9999,
  "ada:outputDataFormatDefault": "missing",
  "ada:reconstructionAlgorithm": "missing",
  "ada:rotationModeDefault": "missing",
  "ada:rotationRangeDefault": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XCT/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:labxctTAPP-Richard2019-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "labxct protocol \u2014 Richard2019-2",
  "schema:description": "labxctTAPP instance derived from Richard et al. 2019 (Chem. Geol.) Synthetic quartz (fluid incl.) Whole sample (low-res) Nikon XTH 320/225 U. Strathclyde (publication column of Lab-XCT_TAPP_v37.csv).",
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
            "Synthetic quartz monocrystal with aqueous fluid inclusions"
          ]
        },
        {
          "@id": "ada:parameter/labxctTAPP/sampleDimensionsDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleDimensionsDefault",
          "schema:name": "Sample Dimensions (L \u00d7 W \u00d7 H)",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "3 \u00d7 5 \u00d7 2 cm"
        },
        {
          "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "preAnalysisImagingAndScreeningDefault",
          "schema:name": "Pre-Analysis Imaging and Screening",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Optical photography of the sample showing the fluid inclusion array, with inclusions numbered for correspondence with the HRXCT reconstruction (Fig. 2)"
        }
      ]
    }
  ],
  "ada:targetFeature": "Fluid inclusion morphology and phase volumes",
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "None stated",
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
  "ada:xRaySourceConfiguration": "Microfocus multi-metal target (225 kV)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/labxctTAPP/xRayTubeAnodeMaterial",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/xRayTubeAnodeMaterial"
        }
      ],
      "schema:name": "X-ray Tube Anode Material",
      "schema:value": "Silver (for Sample B)"
    },
    {
      "@id": "ada:parameter/labxctTAPP/detectorArraySize",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/detectorArraySize"
        }
      ],
      "schema:name": "Detector Array Size",
      "schema:value": "2000 \u00d7 2000 pixels"
    },
    {
      "@id": "ada:parameter/labxctTAPP/detectorPixelSize",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/detectorPixelSize"
        }
      ],
      "schema:name": "Detector Pixel Size",
      "schema:value": 0.2,
      "schema:unitText": "example value",
      "schema:description": "0.2 \u00d7 0.2 mm cell size"
    },
    {
      "@id": "ada:parameter/labxctTAPP/xRayPowerDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "xRayPowerDefault",
      "schema:name": "X-ray Power",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 11.4,
      "schema:description": "11.4 W"
    },
    {
      "@id": "ada:parameter/labxctTAPP/framesAveragedPerProjectionDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "framesAveragedPerProjectionDefault",
      "schema:name": "Frames Averaged per Projection",
      "ada:dataType": "integer",
      "ada:fieldScope": "session",
      "schema:defaultValue": 1,
      "schema:description": "1 frame per projection"
    },
    {
      "@id": "ada:parameter/labxctTAPP/segmentationThresholdValuesOrCriteriaDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "segmentationThresholdValuesOrCriteriaDefault",
      "schema:name": "Segmentation Threshold Values or Criteria",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Manual threshold: vapor = darker, liquid = brighter pixels; specific values N"
    },
    {
      "@id": "ada:parameter/labxctTAPP/phaseIdentificationMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "phaseIdentificationMethodDefault",
      "schema:name": "Phase Identification Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Phase identified by grayscale contrast (vapor darker, liquid brighter)"
    }
  ],
  "ada:detectorType": "Flat panel photodetector (2000 \u00d7 2000 px, cell size 0.2 \u00d7 0.2 mm)",
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Avizo 9.2.0"
    }
  ],
  "schema:instrument": [
    {
      "schema:additionalType": [
        "XCT",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "160 kV",
      "ada:tubeCurrentDefault": "71 \u00b5A (Ag target)",
      "ada:xRayPreFilterDefault": "None (conditions did not require filtering)",
      "ada:voxelSizeDefault": "25 \u00b5m",
      "schema:manufacturer": {
        "schema:name": "Nikon",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "Nikon XTH 320/225",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/XCT",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:numberOfProjectionsDefault": "3141",
  "ada:exposureTimePerProjectionDefault": "0.708 s",
  "ada:samplingUnitSelectionCriteriaDefault": "No sectioning was carried out prior to HRXCT scanning; Sample B was scanned entirely",
  "ada:beamHardeningCorrectionMethod": "None (conditions did not saturate detector; not required)",
  "ada:segmentationMethodDefault": "Manual grayscale threshold",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Lab XCT"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "U. Strathclyde, Glasgow, UK"
  },
  "ada:samplingUnit": "Region of interest (individual fluid inclusion) > Phase (vapour, liquid)",
  "ada:analyticalMode": [
    "Single-volume"
  ],
  "ada:reportedProperties": [
    "Total fluid inclusion volume (mm3); vapour volume (mm3); liquid volume (mm3); vapour volumetric fraction phi_vap (%)"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method"
    }
  ],
  "ada:applicableSampleDimensionRange": "missing",
  "ada:minimumSubVolumeOverlap": -9999,
  "ada:outputDataFormatDefault": "missing",
  "ada:reconstructionAlgorithm": "missing",
  "ada:rotationModeDefault": "missing",
  "ada:rotationRangeDefault": -9999,
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

ex:labxctTAPP-Richard2019-2 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "None stated" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/detectorArraySize>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/detectorPixelSize>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/framesAveragedPerProjectionDefault>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/phaseIdentificationMethodDefault>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationThresholdValuesOrCriteriaDefault>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayPowerDefault>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayTubeAnodeMaterial> ;
    schema1:datePublished "missing" ;
    schema1:description "labxctTAPP instance derived from Richard et al. 2019 (Chem. Geol.) Synthetic quartz (fluid incl.) Whole sample (low-res) Nikon XTH 320/225 U. Strathclyde (publication column of Lab-XCT_TAPP_v37.csv)." ;
    schema1:instrument <https://example.org/instrument/XCT> ;
    schema1:location [ a schema1:Place ;
            schema1:name "U. Strathclyde, Glasgow, UK" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Lab XCT" ] ;
    schema1:name "labxct protocol — Richard2019-2" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Synthetic quartz monocrystal with aqueous fluid inclusions" ],
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleDimensionsDefault>,
                <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> ] ;
    schema1:variableMeasured [ schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analyticalMode "Single-volume" ;
    ada:applicableSampleDimensionRange "missing" ;
    ada:beamHardeningCorrectionMethod "None (conditions did not saturate detector; not required)" ;
    ada:detectorType "Flat panel photodetector (2000 × 2000 px, cell size 0.2 × 0.2 mm)" ;
    ada:exposureTimePerProjectionDefault "0.708 s" ;
    ada:minimumSubVolumeOverlap -9999 ;
    ada:numberOfProjectionsDefault "3141" ;
    ada:outputDataFormatDefault "missing" ;
    ada:reconstructionAlgorithm "missing" ;
    ada:reportedProperties "Total fluid inclusion volume (mm3); vapour volume (mm3); liquid volume (mm3); vapour volumetric fraction phi_vap (%)" ;
    ada:rotationModeDefault "missing" ;
    ada:rotationRangeDefault -9999 ;
    ada:samplingUnit "Region of interest (individual fluid inclusion) > Phase (vapour, liquid)" ;
    ada:samplingUnitSelectionCriteriaDefault "No sectioning was carried out prior to HRXCT scanning; Sample B was scanned entirely" ;
    ada:segmentationMethodDefault "Manual grayscale threshold" ;
    ada:targetFeature "Fluid inclusion morphology and phase volumes" ;
    ada:xRaySourceConfiguration "Microfocus multi-metal target (225 kV)" ;
    bios:computationalTool [ schema1:name "Avizo 9.2.0" ;
            ada:toolRole "dataReduction" ] .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/framesAveragedPerProjectionDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:description "1 frame per projection" ;
    schema1:name "Frames Averaged per Projection" ;
    schema1:valueName "framesAveragedPerProjectionDefault" ;
    ada:dataType "integer" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/phaseIdentificationMethodDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Phase identified by grayscale contrast (vapor darker, liquid brighter)" ;
    schema1:name "Phase Identification Method" ;
    schema1:valueName "phaseIdentificationMethodDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleDimensionsDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "3 × 5 × 2 cm" ;
    schema1:name "Sample Dimensions (L × W × H)" ;
    schema1:valueName "sampleDimensionsDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationThresholdValuesOrCriteriaDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Manual threshold: vapor = darker, liquid = brighter pixels; specific values N" ;
    schema1:name "Segmentation Threshold Values or Criteria" ;
    schema1:valueName "segmentationThresholdValuesOrCriteriaDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayPowerDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1.14e+01 ;
    schema1:description "11.4 W" ;
    schema1:name "X-ray Power" ;
    schema1:valueName "xRayPowerDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Optical photography of the sample showing the fluid inclusion array, with inclusions numbered for correspondence with the HRXCT reconstruction (Fig. 2)" ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:valueName "preAnalysisImagingAndScreeningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://example.org/instrument/XCT> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "XCT" ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Nikon" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Nikon XTH 320/225" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "160 kV" ;
    ada:tubeCurrentDefault "71 µA (Ag target)" ;
    ada:voxelSizeDefault "25 µm" ;
    ada:xRayPreFilterDefault "None (conditions did not require filtering)" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/detectorArraySize> a schema1:PropertyValue ;
    schema1:name "Detector Array Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/detectorArraySize> ;
    schema1:value "2000 × 2000 pixels" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/detectorPixelSize> a schema1:PropertyValue ;
    schema1:description "0.2 × 0.2 mm cell size" ;
    schema1:name "Detector Pixel Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/detectorPixelSize> ;
    schema1:unitText "example value" ;
    schema1:value 2e-01 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayTubeAnodeMaterial> a schema1:PropertyValue ;
    schema1:name "X-ray Tube Anode Material" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayTubeAnodeMaterial> ;
    schema1:value "Silver (for Sample B)" .


```


### labxctTAPP example Richard2019-3
labxctTAPP instance derived from Richard et al. 2019 (Chem. Geol.) Synthetic quartz (fluid incl.) ROI scan (high-res) Nikon XTH 320/225 U. Strathclyde.
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
  "@id": "ex:labxctTAPP-Richard2019-3",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "labxct protocol — Richard2019-3",
  "schema:description": "labxctTAPP instance derived from Richard et al. 2019 (Chem. Geol.) Synthetic quartz (fluid incl.) ROI scan (high-res) Nikon XTH 320/225 U. Strathclyde (publication column of Lab-XCT_TAPP_v37.csv).",
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
            "Synthetic quartz monocrystal with aqueous fluid inclusions"
          ]
        },
        {
          "@id": "ada:parameter/labxctTAPP/sampleDimensionsDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleDimensionsDefault",
          "schema:name": "Sample Dimensions (L × W × H)",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "3 × 5 × 2 cm"
        },
        {
          "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "preAnalysisImagingAndScreeningDefault",
          "schema:name": "Pre-Analysis Imaging and Screening",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Optical photography identifying the fluid inclusion array; inclusion #3 targeted for the high-resolution region-of-interest scan (Fig. 2)"
        }
      ]
    }
  ],
  "ada:targetFeature": "Fluid inclusion morphology and phase volumes",
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "None stated",
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
  "ada:xRaySourceConfiguration": "Microfocus multi-metal target (225 kV)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/labxctTAPP/xRayTubeAnodeMaterial",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/xRayTubeAnodeMaterial"
        }
      ],
      "schema:name": "X-ray Tube Anode Material",
      "schema:value": "Silver (for Sample B)"
    },
    {
      "@id": "ada:parameter/labxctTAPP/detectorArraySize",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/detectorArraySize"
        }
      ],
      "schema:name": "Detector Array Size",
      "schema:value": "2000 × 2000 pixels"
    },
    {
      "@id": "ada:parameter/labxctTAPP/detectorPixelSize",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/detectorPixelSize"
        }
      ],
      "schema:name": "Detector Pixel Size",
      "schema:value": 0.2,
      "schema:unitText": "example value",
      "schema:description": "0.2 × 0.2 mm cell size"
    },
    {
      "@id": "ada:parameter/labxctTAPP/xRayPowerDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "xRayPowerDefault",
      "schema:name": "X-ray Power",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 7.4,
      "schema:description": "7.4 W"
    },
    {
      "@id": "ada:parameter/labxctTAPP/framesAveragedPerProjectionDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "framesAveragedPerProjectionDefault",
      "schema:name": "Frames Averaged per Projection",
      "ada:dataType": "integer",
      "ada:fieldScope": "session",
      "schema:defaultValue": 1,
      "schema:description": "1 frame per projection"
    },
    {
      "@id": "ada:parameter/labxctTAPP/segmentationThresholdValuesOrCriteriaDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "segmentationThresholdValuesOrCriteriaDefault",
      "schema:name": "Segmentation Threshold Values or Criteria",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Manual threshold: vapor = darker, liquid = brighter pixels; specific values N"
    },
    {
      "@id": "ada:parameter/labxctTAPP/phaseIdentificationMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "phaseIdentificationMethodDefault",
      "schema:name": "Phase Identification Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Phase identified by grayscale contrast (vapor darker, liquid brighter)"
    }
  ],
  "ada:detectorType": "Flat panel photodetector (2000 × 2000 px, cell size 0.2 × 0.2 mm)",
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Avizo 9.2.0"
    }
  ],
  "schema:instrument": [
    {
      "schema:additionalType": [
        "XCT",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "160 kV",
      "ada:tubeCurrentDefault": "46 µA (Ag target)",
      "ada:xRayPreFilterDefault": "None (conditions did not require filtering)",
      "ada:voxelSizeDefault": "7.7 µm",
      "schema:manufacturer": {
        "schema:name": "Nikon",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "Nikon XTH 320/225",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/XCT",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:numberOfProjectionsDefault": "3141",
  "ada:exposureTimePerProjectionDefault": "1.415 s",
  "ada:samplingUnitSelectionCriteriaDefault": "1.4 x 1.4 x 1.4 mm region of interest containing fluid inclusion #3, scanned at higher resolution after the whole-sample scan",
  "ada:beamHardeningCorrectionMethod": "None (conditions did not saturate detector; not required)",
  "ada:segmentationMethodDefault": "Manual grayscale threshold",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Lab XCT"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "U. Strathclyde, Glasgow, UK"
  },
  "ada:samplingUnit": "Region of interest (individual fluid inclusion) > Phase (vapour, liquid)",
  "ada:analyticalMode": [
    "Single-volume"
  ],
  "ada:reportedProperties": [
    "Total fluid inclusion volume (mm3); vapour volume (mm3); liquid volume (mm3); vapour volumetric fraction phi_vap (%)"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method"
    }
  ],
  "ada:applicableSampleDimensionRange": "missing",
  "ada:minimumSubVolumeOverlap": -9999,
  "ada:outputDataFormatDefault": "missing",
  "ada:reconstructionAlgorithm": "missing",
  "ada:rotationModeDefault": "missing",
  "ada:rotationRangeDefault": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XCT/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:labxctTAPP-Richard2019-3",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "labxct protocol \u2014 Richard2019-3",
  "schema:description": "labxctTAPP instance derived from Richard et al. 2019 (Chem. Geol.) Synthetic quartz (fluid incl.) ROI scan (high-res) Nikon XTH 320/225 U. Strathclyde (publication column of Lab-XCT_TAPP_v37.csv).",
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
            "Synthetic quartz monocrystal with aqueous fluid inclusions"
          ]
        },
        {
          "@id": "ada:parameter/labxctTAPP/sampleDimensionsDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleDimensionsDefault",
          "schema:name": "Sample Dimensions (L \u00d7 W \u00d7 H)",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "3 \u00d7 5 \u00d7 2 cm"
        },
        {
          "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "preAnalysisImagingAndScreeningDefault",
          "schema:name": "Pre-Analysis Imaging and Screening",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Optical photography identifying the fluid inclusion array; inclusion #3 targeted for the high-resolution region-of-interest scan (Fig. 2)"
        }
      ]
    }
  ],
  "ada:targetFeature": "Fluid inclusion morphology and phase volumes",
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "None stated",
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
  "ada:xRaySourceConfiguration": "Microfocus multi-metal target (225 kV)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/labxctTAPP/xRayTubeAnodeMaterial",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/xRayTubeAnodeMaterial"
        }
      ],
      "schema:name": "X-ray Tube Anode Material",
      "schema:value": "Silver (for Sample B)"
    },
    {
      "@id": "ada:parameter/labxctTAPP/detectorArraySize",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/detectorArraySize"
        }
      ],
      "schema:name": "Detector Array Size",
      "schema:value": "2000 \u00d7 2000 pixels"
    },
    {
      "@id": "ada:parameter/labxctTAPP/detectorPixelSize",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/detectorPixelSize"
        }
      ],
      "schema:name": "Detector Pixel Size",
      "schema:value": 0.2,
      "schema:unitText": "example value",
      "schema:description": "0.2 \u00d7 0.2 mm cell size"
    },
    {
      "@id": "ada:parameter/labxctTAPP/xRayPowerDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "xRayPowerDefault",
      "schema:name": "X-ray Power",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 7.4,
      "schema:description": "7.4 W"
    },
    {
      "@id": "ada:parameter/labxctTAPP/framesAveragedPerProjectionDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "framesAveragedPerProjectionDefault",
      "schema:name": "Frames Averaged per Projection",
      "ada:dataType": "integer",
      "ada:fieldScope": "session",
      "schema:defaultValue": 1,
      "schema:description": "1 frame per projection"
    },
    {
      "@id": "ada:parameter/labxctTAPP/segmentationThresholdValuesOrCriteriaDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "segmentationThresholdValuesOrCriteriaDefault",
      "schema:name": "Segmentation Threshold Values or Criteria",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Manual threshold: vapor = darker, liquid = brighter pixels; specific values N"
    },
    {
      "@id": "ada:parameter/labxctTAPP/phaseIdentificationMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "phaseIdentificationMethodDefault",
      "schema:name": "Phase Identification Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Phase identified by grayscale contrast (vapor darker, liquid brighter)"
    }
  ],
  "ada:detectorType": "Flat panel photodetector (2000 \u00d7 2000 px, cell size 0.2 \u00d7 0.2 mm)",
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Avizo 9.2.0"
    }
  ],
  "schema:instrument": [
    {
      "schema:additionalType": [
        "XCT",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "160 kV",
      "ada:tubeCurrentDefault": "46 \u00b5A (Ag target)",
      "ada:xRayPreFilterDefault": "None (conditions did not require filtering)",
      "ada:voxelSizeDefault": "7.7 \u00b5m",
      "schema:manufacturer": {
        "schema:name": "Nikon",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "Nikon XTH 320/225",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/XCT",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:numberOfProjectionsDefault": "3141",
  "ada:exposureTimePerProjectionDefault": "1.415 s",
  "ada:samplingUnitSelectionCriteriaDefault": "1.4 x 1.4 x 1.4 mm region of interest containing fluid inclusion #3, scanned at higher resolution after the whole-sample scan",
  "ada:beamHardeningCorrectionMethod": "None (conditions did not saturate detector; not required)",
  "ada:segmentationMethodDefault": "Manual grayscale threshold",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Lab XCT"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "U. Strathclyde, Glasgow, UK"
  },
  "ada:samplingUnit": "Region of interest (individual fluid inclusion) > Phase (vapour, liquid)",
  "ada:analyticalMode": [
    "Single-volume"
  ],
  "ada:reportedProperties": [
    "Total fluid inclusion volume (mm3); vapour volume (mm3); liquid volume (mm3); vapour volumetric fraction phi_vap (%)"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method"
    }
  ],
  "ada:applicableSampleDimensionRange": "missing",
  "ada:minimumSubVolumeOverlap": -9999,
  "ada:outputDataFormatDefault": "missing",
  "ada:reconstructionAlgorithm": "missing",
  "ada:rotationModeDefault": "missing",
  "ada:rotationRangeDefault": -9999,
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

ex:labxctTAPP-Richard2019-3 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "None stated" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/detectorArraySize>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/detectorPixelSize>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/framesAveragedPerProjectionDefault>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/phaseIdentificationMethodDefault>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationThresholdValuesOrCriteriaDefault>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayPowerDefault>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayTubeAnodeMaterial> ;
    schema1:datePublished "missing" ;
    schema1:description "labxctTAPP instance derived from Richard et al. 2019 (Chem. Geol.) Synthetic quartz (fluid incl.) ROI scan (high-res) Nikon XTH 320/225 U. Strathclyde (publication column of Lab-XCT_TAPP_v37.csv)." ;
    schema1:instrument <https://example.org/instrument/XCT> ;
    schema1:location [ a schema1:Place ;
            schema1:name "U. Strathclyde, Glasgow, UK" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Lab XCT" ] ;
    schema1:name "labxct protocol — Richard2019-3" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Synthetic quartz monocrystal with aqueous fluid inclusions" ],
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleDimensionsDefault>,
                <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> ] ;
    schema1:variableMeasured [ schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analyticalMode "Single-volume" ;
    ada:applicableSampleDimensionRange "missing" ;
    ada:beamHardeningCorrectionMethod "None (conditions did not saturate detector; not required)" ;
    ada:detectorType "Flat panel photodetector (2000 × 2000 px, cell size 0.2 × 0.2 mm)" ;
    ada:exposureTimePerProjectionDefault "1.415 s" ;
    ada:minimumSubVolumeOverlap -9999 ;
    ada:numberOfProjectionsDefault "3141" ;
    ada:outputDataFormatDefault "missing" ;
    ada:reconstructionAlgorithm "missing" ;
    ada:reportedProperties "Total fluid inclusion volume (mm3); vapour volume (mm3); liquid volume (mm3); vapour volumetric fraction phi_vap (%)" ;
    ada:rotationModeDefault "missing" ;
    ada:rotationRangeDefault -9999 ;
    ada:samplingUnit "Region of interest (individual fluid inclusion) > Phase (vapour, liquid)" ;
    ada:samplingUnitSelectionCriteriaDefault "1.4 x 1.4 x 1.4 mm region of interest containing fluid inclusion #3, scanned at higher resolution after the whole-sample scan" ;
    ada:segmentationMethodDefault "Manual grayscale threshold" ;
    ada:targetFeature "Fluid inclusion morphology and phase volumes" ;
    ada:xRaySourceConfiguration "Microfocus multi-metal target (225 kV)" ;
    bios:computationalTool [ schema1:name "Avizo 9.2.0" ;
            ada:toolRole "dataReduction" ] .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/framesAveragedPerProjectionDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:description "1 frame per projection" ;
    schema1:name "Frames Averaged per Projection" ;
    schema1:valueName "framesAveragedPerProjectionDefault" ;
    ada:dataType "integer" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/phaseIdentificationMethodDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Phase identified by grayscale contrast (vapor darker, liquid brighter)" ;
    schema1:name "Phase Identification Method" ;
    schema1:valueName "phaseIdentificationMethodDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleDimensionsDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "3 × 5 × 2 cm" ;
    schema1:name "Sample Dimensions (L × W × H)" ;
    schema1:valueName "sampleDimensionsDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationThresholdValuesOrCriteriaDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Manual threshold: vapor = darker, liquid = brighter pixels; specific values N" ;
    schema1:name "Segmentation Threshold Values or Criteria" ;
    schema1:valueName "segmentationThresholdValuesOrCriteriaDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayPowerDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 7.4e+00 ;
    schema1:description "7.4 W" ;
    schema1:name "X-ray Power" ;
    schema1:valueName "xRayPowerDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Optical photography identifying the fluid inclusion array; inclusion #3 targeted for the high-resolution region-of-interest scan (Fig. 2)" ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:valueName "preAnalysisImagingAndScreeningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://example.org/instrument/XCT> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "XCT" ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Nikon" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Nikon XTH 320/225" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "160 kV" ;
    ada:tubeCurrentDefault "46 µA (Ag target)" ;
    ada:voxelSizeDefault "7.7 µm" ;
    ada:xRayPreFilterDefault "None (conditions did not require filtering)" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/detectorArraySize> a schema1:PropertyValue ;
    schema1:name "Detector Array Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/detectorArraySize> ;
    schema1:value "2000 × 2000 pixels" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/detectorPixelSize> a schema1:PropertyValue ;
    schema1:description "0.2 × 0.2 mm cell size" ;
    schema1:name "Detector Pixel Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/detectorPixelSize> ;
    schema1:unitText "example value" ;
    schema1:value 2e-01 .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayTubeAnodeMaterial> a schema1:PropertyValue ;
    schema1:name "X-ray Tube Anode Material" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayTubeAnodeMaterial> ;
    schema1:value "Silver (for Sample B)" .


```


### labxctTAPP example Richard2019-4
labxctTAPP instance derived from Richard et al. 2019 (Chem. Geol.) Fluid incl. minerals (C-I) Single-volume Phoenix Nanotom S U. Lorraine.
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
  "@id": "ex:labxctTAPP-Richard2019-4",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "labxct protocol — Richard2019-4",
  "schema:description": "labxctTAPP instance derived from Richard et al. 2019 (Chem. Geol.) Fluid incl. minerals (C-I) Single-volume Phoenix Nanotom S U. Lorraine (publication column of Lab-XCT_TAPP_v37.csv).",
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
            "Minerals with fluid inclusions (quartz, garnet, emerald, wolframite, feldspar)"
          ]
        },
        {
          "@id": "ada:parameter/labxctTAPP/sampleDimensionsDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleDimensionsDefault",
          "schema:name": "Sample Dimensions (L × W × H)",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Varies: 0.3×0.4 to 11×11×7 mm"
        },
        {
          "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "preAnalysisImagingAndScreeningDefault",
          "schema:name": "Pre-Analysis Imaging and Screening",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Optical microscopy under UV illumination, used to identify hydrocarbon-bearing phases within the inclusions (Fig. 9)"
        }
      ]
    }
  ],
  "ada:targetFeature": "Fluid inclusion morphology and phase volumes",
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "None stated",
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
  "ada:detectorType": "CCD Hamamatsu (2300 × 2300 px)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/labxctTAPP/detectorArraySize",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/detectorArraySize"
        }
      ],
      "schema:name": "Detector Array Size",
      "schema:value": "2300 × 2300 pixels"
    },
    {
      "@id": "ada:parameter/labxctTAPP/sourceToObjectDistanceDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "sourceToObjectDistanceDefault",
      "schema:name": "Source-to-Object Distance (SOD)",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 6,
      "schema:description": "6–55 mm (varies by sample)"
    },
    {
      "@id": "ada:parameter/labxctTAPP/framesAveragedPerProjectionDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "framesAveragedPerProjectionDefault",
      "schema:name": "Frames Averaged per Projection",
      "ada:dataType": "integer",
      "ada:fieldScope": "session",
      "schema:defaultValue": 3,
      "schema:description": "3–6 (varies by sample)"
    },
    {
      "@id": "ada:parameter/labxctTAPP/ringArtifactCorrectionMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "ringArtifactCorrectionMethodDefault",
      "schema:name": "Ring Artifact Correction Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Software ring artifact correction filter applied during analysis"
    },
    {
      "@id": "ada:parameter/labxctTAPP/segmentationThresholdValuesOrCriteriaDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "segmentationThresholdValuesOrCriteriaDefault",
      "schema:name": "Segmentation Threshold Values or Criteria",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Manual threshold per phase; specific values N"
    },
    {
      "@id": "ada:parameter/labxctTAPP/phaseIdentificationMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "phaseIdentificationMethodDefault",
      "schema:name": "Phase Identification Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Phases by grayscale contrast; minerals by differential attenuation"
    }
  ],
  "schema:instrument": [
    {
      "schema:additionalType": [
        "XCT",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "90–115 kV (varies by sample)",
      "ada:tubeCurrentDefault": "65–115 µA (varies by sample)",
      "ada:voxelSizeDefault": "0.77–3.5 µm (varies by sample)",
      "schema:manufacturer": {
        "schema:name": "GE / Waygate",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "Phoenix Nanotom S",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/XCT",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:numberOfProjectionsDefault": "1200–2000 (varies by sample)",
  "ada:exposureTimePerProjectionDefault": "750–1250 ms (varies by sample)",
  "ada:beamHardeningCorrectionMethod": "Software BHC applied per respective software",
  "ada:segmentationMethodDefault": "Manual grayscale threshold per phase",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Lab XCT (nano-CT)"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Université de Lorraine, France"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Confocal laser scanning microscopy (Sample I)",
        "schema:description": "CLSM performed on same inclusion for volumetric cross-validation"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnit": "Region of interest (individual fluid inclusion) > Phase (vapour, liquid, oil, solid bitumen)",
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Avizo 9.2.0"
    }
  ],
  "ada:analyticalMode": [
    "Single-volume"
  ],
  "ada:reportedProperties": [
    "Total fluid inclusion volume (mm3); phase volumes (mm3); vapour volumetric fraction phi_vap (%)"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method"
    }
  ],
  "ada:applicableSampleDimensionRange": "missing",
  "ada:minimumSubVolumeOverlap": -9999,
  "ada:outputDataFormatDefault": "missing",
  "ada:reconstructionAlgorithm": "missing",
  "ada:rotationModeDefault": "missing",
  "ada:rotationRangeDefault": -9999,
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:xRaySourceConfiguration": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XCT/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:labxctTAPP-Richard2019-4",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "labxct protocol \u2014 Richard2019-4",
  "schema:description": "labxctTAPP instance derived from Richard et al. 2019 (Chem. Geol.) Fluid incl. minerals (C-I) Single-volume Phoenix Nanotom S U. Lorraine (publication column of Lab-XCT_TAPP_v37.csv).",
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
            "Minerals with fluid inclusions (quartz, garnet, emerald, wolframite, feldspar)"
          ]
        },
        {
          "@id": "ada:parameter/labxctTAPP/sampleDimensionsDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleDimensionsDefault",
          "schema:name": "Sample Dimensions (L \u00d7 W \u00d7 H)",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Varies: 0.3\u00d70.4 to 11\u00d711\u00d77 mm"
        },
        {
          "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "preAnalysisImagingAndScreeningDefault",
          "schema:name": "Pre-Analysis Imaging and Screening",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Optical microscopy under UV illumination, used to identify hydrocarbon-bearing phases within the inclusions (Fig. 9)"
        }
      ]
    }
  ],
  "ada:targetFeature": "Fluid inclusion morphology and phase volumes",
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "None stated",
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
  "ada:detectorType": "CCD Hamamatsu (2300 \u00d7 2300 px)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/labxctTAPP/detectorArraySize",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/labxctTAPP/detectorArraySize"
        }
      ],
      "schema:name": "Detector Array Size",
      "schema:value": "2300 \u00d7 2300 pixels"
    },
    {
      "@id": "ada:parameter/labxctTAPP/sourceToObjectDistanceDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "sourceToObjectDistanceDefault",
      "schema:name": "Source-to-Object Distance (SOD)",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 6,
      "schema:description": "6\u201355 mm (varies by sample)"
    },
    {
      "@id": "ada:parameter/labxctTAPP/framesAveragedPerProjectionDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "framesAveragedPerProjectionDefault",
      "schema:name": "Frames Averaged per Projection",
      "ada:dataType": "integer",
      "ada:fieldScope": "session",
      "schema:defaultValue": 3,
      "schema:description": "3\u20136 (varies by sample)"
    },
    {
      "@id": "ada:parameter/labxctTAPP/ringArtifactCorrectionMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "ringArtifactCorrectionMethodDefault",
      "schema:name": "Ring Artifact Correction Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Software ring artifact correction filter applied during analysis"
    },
    {
      "@id": "ada:parameter/labxctTAPP/segmentationThresholdValuesOrCriteriaDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "segmentationThresholdValuesOrCriteriaDefault",
      "schema:name": "Segmentation Threshold Values or Criteria",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Manual threshold per phase; specific values N"
    },
    {
      "@id": "ada:parameter/labxctTAPP/phaseIdentificationMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "phaseIdentificationMethodDefault",
      "schema:name": "Phase Identification Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Phases by grayscale contrast; minerals by differential attenuation"
    }
  ],
  "schema:instrument": [
    {
      "schema:additionalType": [
        "XCT",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "90\u2013115 kV (varies by sample)",
      "ada:tubeCurrentDefault": "65\u2013115 \u00b5A (varies by sample)",
      "ada:voxelSizeDefault": "0.77\u20133.5 \u00b5m (varies by sample)",
      "schema:manufacturer": {
        "schema:name": "GE / Waygate",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "Phoenix Nanotom S",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/XCT",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:numberOfProjectionsDefault": "1200\u20132000 (varies by sample)",
  "ada:exposureTimePerProjectionDefault": "750\u20131250 ms (varies by sample)",
  "ada:beamHardeningCorrectionMethod": "Software BHC applied per respective software",
  "ada:segmentationMethodDefault": "Manual grayscale threshold per phase",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Lab XCT (nano-CT)"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Universit\u00e9 de Lorraine, France"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Confocal laser scanning microscopy (Sample I)",
        "schema:description": "CLSM performed on same inclusion for volumetric cross-validation"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnit": "Region of interest (individual fluid inclusion) > Phase (vapour, liquid, oil, solid bitumen)",
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Avizo 9.2.0"
    }
  ],
  "ada:analyticalMode": [
    "Single-volume"
  ],
  "ada:reportedProperties": [
    "Total fluid inclusion volume (mm3); phase volumes (mm3); vapour volumetric fraction phi_vap (%)"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method"
    }
  ],
  "ada:applicableSampleDimensionRange": "missing",
  "ada:minimumSubVolumeOverlap": -9999,
  "ada:outputDataFormatDefault": "missing",
  "ada:reconstructionAlgorithm": "missing",
  "ada:rotationModeDefault": "missing",
  "ada:rotationRangeDefault": -9999,
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:xRaySourceConfiguration": "missing",
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

ex:labxctTAPP-Richard2019-4 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "None stated" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/detectorArraySize>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/framesAveragedPerProjectionDefault>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/phaseIdentificationMethodDefault>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/ringArtifactCorrectionMethodDefault>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationThresholdValuesOrCriteriaDefault>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/sourceToObjectDistanceDefault> ;
    schema1:datePublished "missing" ;
    schema1:description "labxctTAPP instance derived from Richard et al. 2019 (Chem. Geol.) Fluid incl. minerals (C-I) Single-volume Phoenix Nanotom S U. Lorraine (publication column of Lab-XCT_TAPP_v37.csv)." ;
    schema1:instrument <https://example.org/instrument/XCT> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Université de Lorraine, France" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Lab XCT (nano-CT)" ] ;
    schema1:name "labxct protocol — Richard2019-4" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Minerals with fluid inclusions (quartz, garnet, emerald, wolframite, feldspar)" ],
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleDimensionsDefault>,
                <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "CLSM performed on same inclusion for volumetric cross-validation" ;
                    schema1:name "Confocal laser scanning microscopy (Sample I)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    schema1:variableMeasured [ schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analyticalMode "Single-volume" ;
    ada:applicableSampleDimensionRange "missing" ;
    ada:beamHardeningCorrectionMethod "Software BHC applied per respective software" ;
    ada:detectorType "CCD Hamamatsu (2300 × 2300 px)" ;
    ada:exposureTimePerProjectionDefault "750–1250 ms (varies by sample)" ;
    ada:minimumSubVolumeOverlap -9999 ;
    ada:numberOfProjectionsDefault "1200–2000 (varies by sample)" ;
    ada:outputDataFormatDefault "missing" ;
    ada:reconstructionAlgorithm "missing" ;
    ada:reportedProperties "Total fluid inclusion volume (mm3); phase volumes (mm3); vapour volumetric fraction phi_vap (%)" ;
    ada:rotationModeDefault "missing" ;
    ada:rotationRangeDefault -9999 ;
    ada:samplingUnit "Region of interest (individual fluid inclusion) > Phase (vapour, liquid, oil, solid bitumen)" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:segmentationMethodDefault "Manual grayscale threshold per phase" ;
    ada:targetFeature "Fluid inclusion morphology and phase volumes" ;
    ada:xRaySourceConfiguration "missing" ;
    bios:computationalTool [ schema1:name "Avizo 9.2.0" ;
            ada:toolRole "dataReduction" ] .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/framesAveragedPerProjectionDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 3 ;
    schema1:description "3–6 (varies by sample)" ;
    schema1:name "Frames Averaged per Projection" ;
    schema1:valueName "framesAveragedPerProjectionDefault" ;
    ada:dataType "integer" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/phaseIdentificationMethodDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Phases by grayscale contrast; minerals by differential attenuation" ;
    schema1:name "Phase Identification Method" ;
    schema1:valueName "phaseIdentificationMethodDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/ringArtifactCorrectionMethodDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Software ring artifact correction filter applied during analysis" ;
    schema1:name "Ring Artifact Correction Method" ;
    schema1:valueName "ringArtifactCorrectionMethodDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleDimensionsDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Varies: 0.3×0.4 to 11×11×7 mm" ;
    schema1:name "Sample Dimensions (L × W × H)" ;
    schema1:valueName "sampleDimensionsDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationThresholdValuesOrCriteriaDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Manual threshold per phase; specific values N" ;
    schema1:name "Segmentation Threshold Values or Criteria" ;
    schema1:valueName "segmentationThresholdValuesOrCriteriaDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/sourceToObjectDistanceDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 6 ;
    schema1:description "6–55 mm (varies by sample)" ;
    schema1:name "Source-to-Object Distance (SOD)" ;
    schema1:valueName "sourceToObjectDistanceDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Optical microscopy under UV illumination, used to identify hydrocarbon-bearing phases within the inclusions (Fig. 9)" ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:valueName "preAnalysisImagingAndScreeningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://example.org/instrument/XCT> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "XCT" ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "GE / Waygate" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Phoenix Nanotom S" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "90–115 kV (varies by sample)" ;
    ada:tubeCurrentDefault "65–115 µA (varies by sample)" ;
    ada:voxelSizeDefault "0.77–3.5 µm (varies by sample)" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/detectorArraySize> a schema1:PropertyValue ;
    schema1:name "Detector Array Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/detectorArraySize> ;
    schema1:value "2300 × 2300 pixels" .


```


### labxctTAPP example Tait2014
labxctTAPP instance derived from Tait 2014 (Thesis) Watson 012 H7 chondrite Single-volume XRADIA XRM500 CSIRO Kensington.
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
  "@id": "ex:labxctTAPP-Tait2014",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "labxct protocol — Tait2014",
  "schema:description": "labxctTAPP instance derived from Tait 2014 (Thesis) Watson 012 H7 chondrite Single-volume XRADIA XRM500 CSIRO Kensington (publication column of Lab-XCT_TAPP_v37.csv).",
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
            "H7 ordinary chondrite (Watson 012)"
          ]
        },
        {
          "@id": "ada:parameter/labxctTAPP/sampleDimensionsDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleDimensionsDefault",
          "schema:name": "Sample Dimensions (L × W × H)",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "8 mm diameter core"
        }
      ]
    }
  ],
  "ada:targetFeature": "Plagioclase network connectivity; partial melt evidence",
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "8 mm diameter core drilled from meteorite prior to XCT",
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
        "XCT",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "70 kV",
      "ada:tubeCurrentDefault": "86 µA",
      "ada:voxelSizeDefault": "1.923 µm",
      "schema:manufacturer": {
        "schema:name": "Zeiss",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "XRADIA XRM500",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/XCT",
      "schema:name": "example instrumentName"
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/labxctTAPP/xRayPowerDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "xRayPowerDefault",
      "schema:name": "X-ray Power",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 7,
      "schema:description": "7 W"
    },
    {
      "@id": "ada:parameter/labxctTAPP/segmentationThresholdValuesOrCriteriaDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "segmentationThresholdValuesOrCriteriaDefault",
      "schema:name": "Segmentation Threshold Values or Criteria",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Dedicated workflow; specific threshold values N"
    },
    {
      "@id": "ada:parameter/labxctTAPP/phaseIdentificationMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "phaseIdentificationMethodDefault",
      "schema:name": "Phase Identification Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Plagioclase targeted; olivine + pyroxene not separately resolved; troilite/oxyhydroxide indistinguishable"
    }
  ],
  "ada:rotationRangeDefault": "360°",
  "ada:numberOfProjectionsDefault": "2000",
  "ada:segmentationMethodDefault": "Dedicated workflow (Godel 2013) modified for plagioclase network segmentation",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Lab XCT (nano-CT)"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "CSIRO, Kensington, Western Australia"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Optical microscopy; EBSD",
        "schema:description": "XCT qualitatively compared with thin sections and EBSD"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnit": "Whole sample (8 mm core) > Phase (plagioclase network)",
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "AvizoFire 8.0; Matlab; Drishti 2.0"
    }
  ],
  "ada:analyticalMode": [
    "Single-volume"
  ],
  "ada:reportedProperties": [
    "Plagioclase network interconnectivity"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method"
    }
  ],
  "ada:applicableSampleDimensionRange": "missing",
  "ada:beamHardeningCorrectionMethod": "missing",
  "ada:detectorType": "missing",
  "ada:exposureTimePerProjectionDefault": -9999,
  "ada:minimumSubVolumeOverlap": -9999,
  "ada:outputDataFormatDefault": "missing",
  "ada:reconstructionAlgorithm": "missing",
  "ada:rotationModeDefault": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:xRaySourceConfiguration": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XCT/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:labxctTAPP-Tait2014",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "labxct protocol \u2014 Tait2014",
  "schema:description": "labxctTAPP instance derived from Tait 2014 (Thesis) Watson 012 H7 chondrite Single-volume XRADIA XRM500 CSIRO Kensington (publication column of Lab-XCT_TAPP_v37.csv).",
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
            "H7 ordinary chondrite (Watson 012)"
          ]
        },
        {
          "@id": "ada:parameter/labxctTAPP/sampleDimensionsDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleDimensionsDefault",
          "schema:name": "Sample Dimensions (L \u00d7 W \u00d7 H)",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "8 mm diameter core"
        }
      ]
    }
  ],
  "ada:targetFeature": "Plagioclase network connectivity; partial melt evidence",
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "8 mm diameter core drilled from meteorite prior to XCT",
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
        "XCT",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "70 kV",
      "ada:tubeCurrentDefault": "86 \u00b5A",
      "ada:voxelSizeDefault": "1.923 \u00b5m",
      "schema:manufacturer": {
        "schema:name": "Zeiss",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "XRADIA XRM500",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/XCT",
      "schema:name": "example instrumentName"
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/labxctTAPP/xRayPowerDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "xRayPowerDefault",
      "schema:name": "X-ray Power",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 7,
      "schema:description": "7 W"
    },
    {
      "@id": "ada:parameter/labxctTAPP/segmentationThresholdValuesOrCriteriaDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "segmentationThresholdValuesOrCriteriaDefault",
      "schema:name": "Segmentation Threshold Values or Criteria",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Dedicated workflow; specific threshold values N"
    },
    {
      "@id": "ada:parameter/labxctTAPP/phaseIdentificationMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "phaseIdentificationMethodDefault",
      "schema:name": "Phase Identification Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Plagioclase targeted; olivine + pyroxene not separately resolved; troilite/oxyhydroxide indistinguishable"
    }
  ],
  "ada:rotationRangeDefault": "360\u00b0",
  "ada:numberOfProjectionsDefault": "2000",
  "ada:segmentationMethodDefault": "Dedicated workflow (Godel 2013) modified for plagioclase network segmentation",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "Lab XCT (nano-CT)"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "CSIRO, Kensington, Western Australia"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Optical microscopy; EBSD",
        "schema:description": "XCT qualitatively compared with thin sections and EBSD"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnit": "Whole sample (8 mm core) > Phase (plagioclase network)",
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "AvizoFire 8.0; Matlab; Drishti 2.0"
    }
  ],
  "ada:analyticalMode": [
    "Single-volume"
  ],
  "ada:reportedProperties": [
    "Plagioclase network interconnectivity"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method"
    }
  ],
  "ada:applicableSampleDimensionRange": "missing",
  "ada:beamHardeningCorrectionMethod": "missing",
  "ada:detectorType": "missing",
  "ada:exposureTimePerProjectionDefault": -9999,
  "ada:minimumSubVolumeOverlap": -9999,
  "ada:outputDataFormatDefault": "missing",
  "ada:reconstructionAlgorithm": "missing",
  "ada:rotationModeDefault": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:xRaySourceConfiguration": "missing",
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

ex:labxctTAPP-Tait2014 a cdi:Activity,
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
                    schema1:description "8 mm diameter core drilled from meteorite prior to XCT" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/phaseIdentificationMethodDefault>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationThresholdValuesOrCriteriaDefault>,
        <https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayPowerDefault> ;
    schema1:datePublished "missing" ;
    schema1:description "labxctTAPP instance derived from Tait 2014 (Thesis) Watson 012 H7 chondrite Single-volume XRADIA XRM500 CSIRO Kensington (publication column of Lab-XCT_TAPP_v37.csv)." ;
    schema1:instrument <https://example.org/instrument/XCT> ;
    schema1:location [ a schema1:Place ;
            schema1:name "CSIRO, Kensington, Western Australia" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "Lab XCT (nano-CT)" ] ;
    schema1:name "labxct protocol — Tait2014" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "H7 ordinary chondrite (Watson 012)" ],
                <https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleDimensionsDefault> ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "XCT qualitatively compared with thin sections and EBSD" ;
                    schema1:name "Optical microscopy; EBSD" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    schema1:variableMeasured [ schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analyticalMode "Single-volume" ;
    ada:applicableSampleDimensionRange "missing" ;
    ada:beamHardeningCorrectionMethod "missing" ;
    ada:detectorType "missing" ;
    ada:exposureTimePerProjectionDefault -9999 ;
    ada:minimumSubVolumeOverlap -9999 ;
    ada:numberOfProjectionsDefault "2000" ;
    ada:outputDataFormatDefault "missing" ;
    ada:reconstructionAlgorithm "missing" ;
    ada:reportedProperties "Plagioclase network interconnectivity" ;
    ada:rotationModeDefault "missing" ;
    ada:rotationRangeDefault "360°" ;
    ada:samplingUnit "Whole sample (8 mm core) > Phase (plagioclase network)" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:segmentationMethodDefault "Dedicated workflow (Godel 2013) modified for plagioclase network segmentation" ;
    ada:targetFeature "Plagioclase network connectivity; partial melt evidence" ;
    ada:xRaySourceConfiguration "missing" ;
    bios:computationalTool [ schema1:name "AvizoFire 8.0; Matlab; Drishti 2.0" ;
            ada:toolRole "dataReduction" ] .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/phaseIdentificationMethodDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Plagioclase targeted; olivine + pyroxene not separately resolved; troilite/oxyhydroxide indistinguishable" ;
    schema1:name "Phase Identification Method" ;
    schema1:valueName "phaseIdentificationMethodDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/sampleDimensionsDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "8 mm diameter core" ;
    schema1:name "Sample Dimensions (L × W × H)" ;
    schema1:valueName "sampleDimensionsDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/segmentationThresholdValuesOrCriteriaDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Dedicated workflow; specific threshold values N" ;
    schema1:name "Segmentation Threshold Values or Criteria" ;
    schema1:valueName "segmentationThresholdValuesOrCriteriaDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/xRayPowerDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 7 ;
    schema1:description "7 W" ;
    schema1:name "X-ray Power" ;
    schema1:valueName "xRayPowerDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://example.org/instrument/XCT> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "XCT" ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Zeiss" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "XRADIA XRM500" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "70 kV" ;
    ada:tubeCurrentDefault "86 µA" ;
    ada:voxelSizeDefault "1.923 µm" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Lab-XCT Technique-Aligned Protocol Profile (labxctTAPP)
description: 'Laboratory X-ray computed tomography (polychromatic cone-beam) extension
  of the base TAPP definition. Basic protocol-tier fields are required top-level ada:
  properties; Advanced protocol-tier fields are schema:additionalProperty[] PropertyValueSpecification
  entries. XCT has no per-element analyte axis, so no ada:analyteTemplate is defined.
  Generated from tapp/Current TAPPs/Lab-XCT_TAPP_v37.csv by tools/build_tapp.py.'
allOf:
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/calibrationFactor/schema.yaml#/$defs/ProcedureIdentification
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
                              - Chondrite meteorite
                              - Achondrite meteorite
                              - Lunar sample
                              - Mission-returned sample
                              - Drill core (rock)
                              - Sediment core
                              - Terrestrial rock
                              - Cosmic spherule
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
                    title: "Sample Dimensions (L \xD7 W \xD7 H)"
                    description: "Physical dimensions of the sample in mm, reported
                      as length \xD7 width \xD7 height (or equivalent three orthogonal
                      measurements)."
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/labxctTAPP/sampleDimensionsDefault
                      '@type':
                        const:
                        - schema:PropertyValueSpecification
                      schema:valueName:
                        const: sampleDimensionsDefault
                      schema:name:
                        const: "Sample Dimensions (L \xD7 W \xD7 H)"
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
    ada:targetFeature:
      description: The 3D internal features or properties the procedure is designed
        to characterize.
      type: string
      readOnly: true
    ada:applicableSampleDimensionRange:
      description: "The range of sample sizes compatible with this procedure at the
        target voxel size and geometric configuration. The upper bound is a hard constraint
        set by the instrument field of view (FOV) at the procedure's target magnification:
        FOV \u2248 detector array width \xD7 pixel size / geometric magnification
        (divide additionally by optical objective multiplier for Versa-class systems
        using optical magnification). For Mode A (single-volume): all three sample
        dimensions must fall within the FOV. For Mode B (multi-volume stitching):
        sample diameter must fall within the FOV; sample length along the rotation
        axis is effectively unlimited through stitching. The lower bound is a practical
        guideline: ~10 voxels across the smallest dimension."
      type: string
      readOnly: true
    schema:additionalProperty:
      type: array
      items:
        anyOf:
        - title: Sample Mounting Method
          description: "Method used to mount or hold the sample on the instrument
            rotation stage. Mounting material should transmit X-rays at the selected
            voltage without dominating beam attenuation. Report the holder CLASS from
            the list and name the specific vessel or material alongside it \u2014
            'Tube or vial \u2014 1 cm plastic straw', not 'Tube or vial'. Where the
            sample is sealed or bagged inside a further holder for contamination control,
            record both layers. Report any adhesive, support material and alignment
            aids used."
          type: object
          properties:
            '@id':
              const: ada:parameter/labxctTAPP/sampleMountingMethodDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: sampleMountingMethodDefault
            schema:name:
              const: Sample Mounting Method
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
        - title: X-ray Tube Anode Material
          description: Material of the X-ray tube anode (target).
          type: object
          properties:
            '@id':
              const: ada:parameter/labxctTAPP/xRayTubeAnodeMaterial
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/labxctTAPP/xRayTubeAnodeMaterial
            schema:name:
              const: X-ray Tube Anode Material
            schema:value:
              type: string
          required:
          - '@id'
          - '@type'
          - schema:propertyID
          - schema:name
          - schema:value
          readOnly: true
        - title: Detector Array Size
          description: "Number of pixels in the detector array (width \xD7 height)."
          type: object
          properties:
            '@id':
              const: ada:parameter/labxctTAPP/detectorArraySize
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/labxctTAPP/detectorArraySize
            schema:name:
              const: Detector Array Size
            schema:value:
              type: string
          required:
          - '@id'
          - '@type'
          - schema:propertyID
          - schema:name
          - schema:value
          readOnly: true
        - title: Detector Pixel Size
          description: Physical size of a single pixel on the detector in micrometres.
            This is a fixed hardware property of the detector array, distinct from
            the reconstructed voxel size (which depends on geometric magnification
            and binning).
          type: object
          properties:
            '@id':
              const: ada:parameter/labxctTAPP/detectorPixelSize
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/labxctTAPP/detectorPixelSize
            schema:name:
              const: Detector Pixel Size
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
        - title: Optical Objective
          description: Optical magnification objective installed between the scintillator
            and CCD/CMOS detector. Applies only to instruments using optical magnification
            (e.g., Zeiss Xradia Versa series). For systems using only geometric magnification,
            report "Not applicable".
          type: object
          properties:
            '@id':
              const: ada:parameter/labxctTAPP/opticalObjective
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/labxctTAPP/opticalObjective
            schema:name:
              const: Optical Objective
            schema:value:
              type: string
          required:
          - '@id'
          - '@type'
          - schema:propertyID
          - schema:name
          - schema:value
          readOnly: true
        - title: X-ray Power
          description: "X-ray tube power in watts (W). Derivable as voltage (kV) \xD7
            current (mA) = kV \xD7 \xB5A / 1000. If power was varied across samples
            within the session, report the full range applied (e.g., 7\u201313 W)."
          type: object
          properties:
            '@id':
              const: ada:parameter/labxctTAPP/xRayPowerDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: xRayPowerDefault
            schema:name:
              const: X-ray Power
            ada:dataType:
              const: number
            ada:fieldScope:
              const: session
            schema:readonlyValue:
              const: false
            ada:tier:
              const: R
            schema:unitText:
              const: W
          required:
          - '@id'
          - '@type'
          - schema:valueName
          - schema:name
          - ada:dataType
          - ada:fieldScope
        - title: Source-to-Object Distance (SOD)
          description: Distance from the X-ray source focal spot to the centre of
            the sample rotation axis, in mm.
          type: object
          properties:
            '@id':
              const: ada:parameter/labxctTAPP/sourceToObjectDistanceDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: sourceToObjectDistanceDefault
            schema:name:
              const: Source-to-Object Distance (SOD)
            ada:dataType:
              const: number
            ada:fieldScope:
              const: session
            schema:readonlyValue:
              const: false
            ada:tier:
              const: R
            schema:unitText:
              const: mm
          required:
          - '@id'
          - '@type'
          - schema:valueName
          - schema:name
          - ada:dataType
          - ada:fieldScope
        - title: Source-to-Detector Distance (SDD)
          description: "Distance from the X-ray source focal spot to the detector
            surface, in mm. Voxel size \u2248 detector pixel size / M (before binning;
            divide additionally by optical objective for Versa-class systems)."
          type: object
          properties:
            '@id':
              const: ada:parameter/labxctTAPP/sourceToDetectorDistanceDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: sourceToDetectorDistanceDefault
            schema:name:
              const: Source-to-Detector Distance (SDD)
            ada:dataType:
              const: number
            ada:fieldScope:
              const: session
            schema:readonlyValue:
              const: false
            ada:tier:
              const: R
            schema:unitText:
              const: mm
          required:
          - '@id'
          - '@type'
          - schema:valueName
          - schema:name
          - ada:dataType
          - ada:fieldScope
        - title: Rotation Step Size
          description: Angular increment between successive projection images, in
            degrees. Equal to Rotation Range divided by Number of Projections when
            both are reported; however, some sources report step size as the primary
            rotation parameter without stating the total number of projections explicitly.
          type: object
          properties:
            '@id':
              const: ada:parameter/labxctTAPP/rotationStepSizeDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: rotationStepSizeDefault
            schema:name:
              const: Rotation Step Size
            ada:dataType:
              const: number
            ada:fieldScope:
              const: session
            schema:readonlyValue:
              const: false
            ada:tier:
              const: R
            schema:unitText:
              const: "\xB0"
          required:
          - '@id'
          - '@type'
          - schema:valueName
          - schema:name
          - ada:dataType
          - ada:fieldScope
        - title: Frames Averaged per Projection
          description: "Number of individual detector frames acquired and averaged
            to produce each saved projection image. The effective exposure per projection
            = exposure time per frame \xD7 frames averaged."
          type: object
          properties:
            '@id':
              const: ada:parameter/labxctTAPP/framesAveragedPerProjectionDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: framesAveragedPerProjectionDefault
            schema:name:
              const: Frames Averaged per Projection
            ada:dataType:
              const: integer
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
        - title: Detector Binning
          description: "Detector pixel binning factor applied during acquisition.
            Binning combines adjacent pixels (e.g., 2\xD72 combines 4 pixels into
            one)."
          type: object
          properties:
            '@id':
              const: ada:parameter/labxctTAPP/detectorBinningDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: detectorBinningDefault
            schema:name:
              const: Detector Binning
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
        - title: Reconstruction Convolution Filter
          description: Convolution (apodization) filter kernel applied during back-projection
            reconstruction.
          type: object
          properties:
            '@id':
              const: ada:parameter/labxctTAPP/reconstructionConvolutionFilterDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: reconstructionConvolutionFilterDefault
            schema:name:
              const: Reconstruction Convolution Filter
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
        - title: Beam Hardening Correction Parameter
          description: Numerical value or setting applied in the software beam hardening
            correction algorithm for this specific analysis. Companion to Beam Hardening
            Correction Method.
          type: object
          properties:
            '@id':
              const: ada:parameter/labxctTAPP/beamHardeningCorrectionParameterDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: beamHardeningCorrectionParameterDefault
            schema:name:
              const: Beam Hardening Correction Parameter
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
        - title: Ring Artifact Correction Method
          description: Procedure specification for how ring artifacts are handled.
            Whether correction was applied and its outcome are recorded separately
            in Group 6.
          type: object
          properties:
            '@id':
              const: ada:parameter/labxctTAPP/ringArtifactCorrectionMethodDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: ringArtifactCorrectionMethodDefault
            schema:name:
              const: Ring Artifact Correction Method
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
        - title: CT Number Calibration
          description: Whether the raw CT grayscale values have been calibrated to
            physically meaningful units using reference materials.
          type: object
          properties:
            '@id':
              const: ada:parameter/labxctTAPP/ctNumberCalibrationDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: ctNumberCalibrationDefault
            schema:name:
              const: CT Number Calibration
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
        - title: Segmentation Threshold Values or Criteria
          description: "Specific CT number range(s) or quantitative criteria used
            to define each segmented phase or feature. For LAC-calibrated datasets,
            report values in cm\u207B\xB9."
          type: object
          properties:
            '@id':
              const: ada:parameter/labxctTAPP/segmentationThresholdValuesOrCriteriaDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: segmentationThresholdValuesOrCriteriaDefault
            schema:name:
              const: Segmentation Threshold Values or Criteria
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
        - title: Phase Identification Method
          description: Method used to assign reconstructed CT number ranges to specific
            mineral phases or material types. Approaches include comparison to calculated
            linear attenuation coefficients (LAC), cross-validation with independent
            analytical techniques, or empirical calibration.
          type: object
          properties:
            '@id':
              const: ada:parameter/labxctTAPP/phaseIdentificationMethodDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: phaseIdentificationMethodDefault
            schema:name:
              const: Phase Identification Method
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
        - title: VOI Selection Criteria
          description: Rules specifying how the Volume of Interest (VOI) is to be
            defined for quantitative analysis. Common criteria exclude cone-beam artifact
            zones at sample edges, beam hardening halos near dense inclusions, and
            sample holder signal. The actual VOI applied in a specific analysis is
            recorded separately at analysis level.
          type: object
          properties:
            '@id':
              const: ada:parameter/labxctTAPP/voiSelectionCriteriaDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: voiSelectionCriteriaDefault
            schema:name:
              const: VOI Selection Criteria
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
        - title: Output Bit Depth
          description: Bit depth of the reconstructed 3D volume (number of bits used
            to encode each voxel's grayscale value). Common values are 8-bit (256
            gray levels), 16-bit (65,536 gray levels), or 32-bit floating point. A
            required output bit depth may be specified if downstream analysis workflows
            depend on a consistent grayscale range.
          type: object
          properties:
            '@id':
              const: ada:parameter/labxctTAPP/outputBitDepthDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: outputBitDepthDefault
            schema:name:
              const: Output Bit Depth
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
        - title: Partial Volume Effect Criteria
          description: "Specification of how partial volume effects (PVE) are managed
            in quantitative analysis. PVE correction can be implemented via PSF-based
            deconvolution tools such as Blob3D. Record the minimum feature size criterion
            adopted for the procedure (in voxels or \xB5m), the basis for it, the
            treatment of boundary voxels in modal abundance or size distribution calculations,
            and whether PVE correction is required or optional. State whether the
            criterion follows the Withers et al. (2021) convention \u2014 a feature
            must span at least 3 voxels to be positively identified and at least 10
            for reliable shape and volume characterisation \u2014 or is SNR-limited,
            PVE-limited or analyst-defined."
          type: object
          properties:
            '@id':
              const: ada:parameter/labxctTAPP/partialVolumeEffectCriteriaDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: partialVolumeEffectCriteriaDefault
            schema:name:
              const: Partial Volume Effect Criteria
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
        - title: Cross-Validation Procedure Requirement
          description: Specification of what independent analytical validation is
            required to confirm CT segmentation results, phase identification, or
            quantitative measurements. Common approaches include BSE imaging, SEM-EDS
            or EPMA modal analysis, He pycnometry for bulk porosity, and Raman or
            SIMS phase mapping. Record the required validation method(s) and the sampling
            fraction (e.g., every sample, one per session, or a representative subset).
          type: object
          properties:
            '@id':
              const: ada:parameter/labxctTAPP/crossValidationProcedureRequirementDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: crossValidationProcedureRequirementDefault
            schema:name:
              const: Cross-Validation Procedure Requirement
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
          title: Sample Mounting Method
          description: "Method used to mount or hold the sample on the instrument
            rotation stage. Mounting material should transmit X-rays at the selected
            voltage without dominating beam attenuation. Report the holder CLASS from
            the list and name the specific vessel or material alongside it \u2014
            'Tube or vial \u2014 1 cm plastic straw', not 'Tube or vial'. Where the
            sample is sealed or bagged inside a further holder for contamination control,
            record both layers. Report any adhesive, support material and alignment
            aids used."
          type: object
          properties:
            '@id':
              const: ada:parameter/labxctTAPP/sampleMountingMethodDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: sampleMountingMethodDefault
            schema:name:
              const: Sample Mounting Method
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
          title: X-ray Tube Anode Material
          description: Material of the X-ray tube anode (target).
          type: object
          properties:
            '@id':
              const: ada:parameter/labxctTAPP/xRayTubeAnodeMaterial
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/labxctTAPP/xRayTubeAnodeMaterial
            schema:name:
              const: X-ray Tube Anode Material
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
          title: Detector Array Size
          description: "Number of pixels in the detector array (width \xD7 height)."
          type: object
          properties:
            '@id':
              const: ada:parameter/labxctTAPP/detectorArraySize
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/labxctTAPP/detectorArraySize
            schema:name:
              const: Detector Array Size
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
          title: Detector Pixel Size
          description: Physical size of a single pixel on the detector in micrometres.
            This is a fixed hardware property of the detector array, distinct from
            the reconstructed voxel size (which depends on geometric magnification
            and binning).
          type: object
          properties:
            '@id':
              const: ada:parameter/labxctTAPP/detectorPixelSize
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/labxctTAPP/detectorPixelSize
            schema:name:
              const: Detector Pixel Size
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
          title: Optical Objective
          description: Optical magnification objective installed between the scintillator
            and CCD/CMOS detector. Applies only to instruments using optical magnification
            (e.g., Zeiss Xradia Versa series). For systems using only geometric magnification,
            report "Not applicable".
          type: object
          properties:
            '@id':
              const: ada:parameter/labxctTAPP/opticalObjective
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/labxctTAPP/opticalObjective
            schema:name:
              const: Optical Objective
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
          title: X-ray Power
          description: "X-ray tube power in watts (W). Derivable as voltage (kV) \xD7
            current (mA) = kV \xD7 \xB5A / 1000. If power was varied across samples
            within the session, report the full range applied (e.g., 7\u201313 W)."
          type: object
          properties:
            '@id':
              const: ada:parameter/labxctTAPP/xRayPowerDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: xRayPowerDefault
            schema:name:
              const: X-ray Power
            ada:dataType:
              const: number
            ada:fieldScope:
              const: session
            schema:readonlyValue:
              const: false
            ada:tier:
              const: R
            schema:unitText:
              const: W
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
          title: Source-to-Object Distance (SOD)
          description: Distance from the X-ray source focal spot to the centre of
            the sample rotation axis, in mm.
          type: object
          properties:
            '@id':
              const: ada:parameter/labxctTAPP/sourceToObjectDistanceDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: sourceToObjectDistanceDefault
            schema:name:
              const: Source-to-Object Distance (SOD)
            ada:dataType:
              const: number
            ada:fieldScope:
              const: session
            schema:readonlyValue:
              const: false
            ada:tier:
              const: R
            schema:unitText:
              const: mm
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
          title: Source-to-Detector Distance (SDD)
          description: "Distance from the X-ray source focal spot to the detector
            surface, in mm. Voxel size \u2248 detector pixel size / M (before binning;
            divide additionally by optical objective for Versa-class systems)."
          type: object
          properties:
            '@id':
              const: ada:parameter/labxctTAPP/sourceToDetectorDistanceDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: sourceToDetectorDistanceDefault
            schema:name:
              const: Source-to-Detector Distance (SDD)
            ada:dataType:
              const: number
            ada:fieldScope:
              const: session
            schema:readonlyValue:
              const: false
            ada:tier:
              const: R
            schema:unitText:
              const: mm
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
          title: Rotation Step Size
          description: Angular increment between successive projection images, in
            degrees. Equal to Rotation Range divided by Number of Projections when
            both are reported; however, some sources report step size as the primary
            rotation parameter without stating the total number of projections explicitly.
          type: object
          properties:
            '@id':
              const: ada:parameter/labxctTAPP/rotationStepSizeDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: rotationStepSizeDefault
            schema:name:
              const: Rotation Step Size
            ada:dataType:
              const: number
            ada:fieldScope:
              const: session
            schema:readonlyValue:
              const: false
            ada:tier:
              const: R
            schema:unitText:
              const: "\xB0"
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
          title: Frames Averaged per Projection
          description: "Number of individual detector frames acquired and averaged
            to produce each saved projection image. The effective exposure per projection
            = exposure time per frame \xD7 frames averaged."
          type: object
          properties:
            '@id':
              const: ada:parameter/labxctTAPP/framesAveragedPerProjectionDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: framesAveragedPerProjectionDefault
            schema:name:
              const: Frames Averaged per Projection
            ada:dataType:
              const: integer
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
          title: Detector Binning
          description: "Detector pixel binning factor applied during acquisition.
            Binning combines adjacent pixels (e.g., 2\xD72 combines 4 pixels into
            one)."
          type: object
          properties:
            '@id':
              const: ada:parameter/labxctTAPP/detectorBinningDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: detectorBinningDefault
            schema:name:
              const: Detector Binning
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
          title: Reconstruction Convolution Filter
          description: Convolution (apodization) filter kernel applied during back-projection
            reconstruction.
          type: object
          properties:
            '@id':
              const: ada:parameter/labxctTAPP/reconstructionConvolutionFilterDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: reconstructionConvolutionFilterDefault
            schema:name:
              const: Reconstruction Convolution Filter
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
          title: Beam Hardening Correction Parameter
          description: Numerical value or setting applied in the software beam hardening
            correction algorithm for this specific analysis. Companion to Beam Hardening
            Correction Method.
          type: object
          properties:
            '@id':
              const: ada:parameter/labxctTAPP/beamHardeningCorrectionParameterDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: beamHardeningCorrectionParameterDefault
            schema:name:
              const: Beam Hardening Correction Parameter
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
          title: Ring Artifact Correction Method
          description: Procedure specification for how ring artifacts are handled.
            Whether correction was applied and its outcome are recorded separately
            in Group 6.
          type: object
          properties:
            '@id':
              const: ada:parameter/labxctTAPP/ringArtifactCorrectionMethodDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: ringArtifactCorrectionMethodDefault
            schema:name:
              const: Ring Artifact Correction Method
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
          title: CT Number Calibration
          description: Whether the raw CT grayscale values have been calibrated to
            physically meaningful units using reference materials.
          type: object
          properties:
            '@id':
              const: ada:parameter/labxctTAPP/ctNumberCalibrationDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: ctNumberCalibrationDefault
            schema:name:
              const: CT Number Calibration
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
          title: Segmentation Threshold Values or Criteria
          description: "Specific CT number range(s) or quantitative criteria used
            to define each segmented phase or feature. For LAC-calibrated datasets,
            report values in cm\u207B\xB9."
          type: object
          properties:
            '@id':
              const: ada:parameter/labxctTAPP/segmentationThresholdValuesOrCriteriaDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: segmentationThresholdValuesOrCriteriaDefault
            schema:name:
              const: Segmentation Threshold Values or Criteria
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
          title: Phase Identification Method
          description: Method used to assign reconstructed CT number ranges to specific
            mineral phases or material types. Approaches include comparison to calculated
            linear attenuation coefficients (LAC), cross-validation with independent
            analytical techniques, or empirical calibration.
          type: object
          properties:
            '@id':
              const: ada:parameter/labxctTAPP/phaseIdentificationMethodDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: phaseIdentificationMethodDefault
            schema:name:
              const: Phase Identification Method
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
          title: VOI Selection Criteria
          description: Rules specifying how the Volume of Interest (VOI) is to be
            defined for quantitative analysis. Common criteria exclude cone-beam artifact
            zones at sample edges, beam hardening halos near dense inclusions, and
            sample holder signal. The actual VOI applied in a specific analysis is
            recorded separately at analysis level.
          type: object
          properties:
            '@id':
              const: ada:parameter/labxctTAPP/voiSelectionCriteriaDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: voiSelectionCriteriaDefault
            schema:name:
              const: VOI Selection Criteria
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
          title: Output Bit Depth
          description: Bit depth of the reconstructed 3D volume (number of bits used
            to encode each voxel's grayscale value). Common values are 8-bit (256
            gray levels), 16-bit (65,536 gray levels), or 32-bit floating point. A
            required output bit depth may be specified if downstream analysis workflows
            depend on a consistent grayscale range.
          type: object
          properties:
            '@id':
              const: ada:parameter/labxctTAPP/outputBitDepthDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: outputBitDepthDefault
            schema:name:
              const: Output Bit Depth
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
          title: Partial Volume Effect Criteria
          description: "Specification of how partial volume effects (PVE) are managed
            in quantitative analysis. PVE correction can be implemented via PSF-based
            deconvolution tools such as Blob3D. Record the minimum feature size criterion
            adopted for the procedure (in voxels or \xB5m), the basis for it, the
            treatment of boundary voxels in modal abundance or size distribution calculations,
            and whether PVE correction is required or optional. State whether the
            criterion follows the Withers et al. (2021) convention \u2014 a feature
            must span at least 3 voxels to be positively identified and at least 10
            for reliable shape and volume characterisation \u2014 or is SNR-limited,
            PVE-limited or analyst-defined."
          type: object
          properties:
            '@id':
              const: ada:parameter/labxctTAPP/partialVolumeEffectCriteriaDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: partialVolumeEffectCriteriaDefault
            schema:name:
              const: Partial Volume Effect Criteria
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
          title: Cross-Validation Procedure Requirement
          description: Specification of what independent analytical validation is
            required to confirm CT segmentation results, phase identification, or
            quantitative measurements. Common approaches include BSE imaging, SEM-EDS
            or EPMA modal analysis, He pycnometry for bulk porosity, and Raman or
            SIMS phase mapping. Record the required validation method(s) and the sampling
            fraction (e.g., every sample, one per session, or a representative subset).
          type: object
          properties:
            '@id':
              const: ada:parameter/labxctTAPP/crossValidationProcedureRequirementDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: crossValidationProcedureRequirementDefault
            schema:name:
              const: Cross-Validation Procedure Requirement
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
                  schema:description:
                    description: Any preparation steps applied to the sample before
                      scanning, including cleaning, trimming, consolidation, or drying.
                      Note any exceptions.
                    anyOf:
                    - type: string
                    - type: array
                      items:
                        type: string
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
                      - title: Flat Field Correction
                        description: Whether dark-field (detector read with X-ray
                          source off; electronic noise baseline) and bright-field
                          (source on, no sample; gain calibration) reference images
                          are acquired and applied to normalize detector response
                          before reconstruction.
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/labxctTAPP/flatFieldCorrectionDefault
                          '@type':
                            const:
                            - schema:PropertyValueSpecification
                          schema:valueName:
                            const: flatFieldCorrectionDefault
                          schema:name:
                            const: Flat Field Correction
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
                      - title: Sub-volume Stitching and Registration Method
                        description: Method used to register adjacent sub-volume datasets
                          to each other and stitch them into a single continuous 3D
                          volume. Report the alignment strategy (manual, automated,
                          fiducial-based), the software used, and any correction steps
                          applied. Where rotational mismatch has been corrected via
                          raw projection re-alignment, document it here.
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/labxctTAPP/subVolumeStitchingAndRegistrationMethodDefault
                          '@type':
                            const:
                            - schema:PropertyValueSpecification
                          schema:valueName:
                            const: subVolumeStitchingAndRegistrationMethodDefault
                          schema:name:
                            const: Sub-volume Stitching and Registration Method
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
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Procedure_constantsReferenceValues
                    allOf:
                    - contains:
                        title: Flat Field Correction
                        description: Whether dark-field (detector read with X-ray
                          source off; electronic noise baseline) and bright-field
                          (source on, no sample; gain calibration) reference images
                          are acquired and applied to normalize detector response
                          before reconstruction.
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/labxctTAPP/flatFieldCorrectionDefault
                          '@type':
                            const:
                            - schema:PropertyValueSpecification
                          schema:valueName:
                            const: flatFieldCorrectionDefault
                          schema:name:
                            const: Flat Field Correction
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
                        title: Sub-volume Stitching and Registration Method
                        description: Method used to register adjacent sub-volume datasets
                          to each other and stitch them into a single continuous 3D
                          volume. Report the alignment strategy (manual, automated,
                          fiducial-based), the software used, and any correction steps
                          applied. Where rotational mismatch has been corrected via
                          raw projection re-alignment, document it here.
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/labxctTAPP/subVolumeStitchingAndRegistrationMethodDefault
                          '@type':
                            const:
                            - schema:PropertyValueSpecification
                          schema:valueName:
                            const: subVolumeStitchingAndRegistrationMethodDefault
                          schema:name:
                            const: Sub-volume Stitching and Registration Method
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
    ada:xRaySourceConfiguration:
      description: Focal spot geometry and scale of the X-ray tube.
      anyOf:
      - type: string
        enum:
        - Reflection target, microfocal
        - Reflection target, rotating (high-power)
        - Transmission target, nanofocal
        - N/A
        - None
        - missing
      - type: string
      readOnly: true
    ada:detectorType:
      description: Type of X-ray detector used to record projection images.
      anyOf:
      - type: string
        enum:
        - Flat-panel (amorphous silicon, a-Si)
        - CCD + scintillator (with optical objective)
        - CMOS + scintillator
        - N/A
        - None
        - missing
      - type: string
      readOnly: true
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
                description: Software used to reconstruct 2D projection images into
                  a 3D CT volume, including version number.
                anyOf:
                - type: string
                - type: array
                  items:
                    type: string
        required:
        - ada:toolRole
    schema:instrument:
      type: array
      items:
        type: object
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
              ada:acceleratingVoltageDefault:
                description: "X-ray tube accelerating voltage in kilovolts (kV). If
                  the voltage was varied across samples within the same procedure
                  or session, report the full range applied (e.g., 90\u2013115 kV).
                  Note: some sources report this parameter as 'X keV' (maximum Bremsstrahlung
                  photon energy) rather than 'X kV' (tube voltage). For polychromatic
                  lab XCT, these are numerically equivalent: E_max [keV] = V [kV].
                  Record the value as originally reported, and add a parenthetical
                  note if the unit used is keV."
                anyOf:
                - type: number
                - type: string
              ada:tubeCurrentDefault:
                description: "X-ray tube current in microamperes (\xB5A). If the current
                  was varied across samples within the same procedure or session,
                  report the full range applied (e.g., 65\u2013115 \xB5A)."
                anyOf:
                - type: number
                - type: string
              ada:xRayPreFilterDefault:
                description: Material and thickness of the beam-hardening filter placed
                  between the X-ray source and the sample. Both filter material and
                  thickness must be reported. Instrument-proprietary filter codes
                  should be decoded where possible.
                anyOf:
                - type: string
                - type: array
                  items:
                    type: string
              ada:voxelSizeDefault:
                description: "Isotropic voxel edge length of the reconstructed 3D
                  volume in micrometres. The target voxel size is set based on the
                  smallest feature to be resolved (target voxel size \u2264 ~1/3 of
                  that feature size; see the criterion recorded under Partial Volume
                  Effect Criteria). Record the achieved voxel size as reported by
                  the reconstruction software, which may differ slightly from the
                  target due to final geometric calibration."
                anyOf:
                - type: number
                - type: string
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
                    - Nikon
                    - Zeiss
                    - Bruker
                    - GE / Waygate
                    - North Star Imaging
                    - RX Solutions
                    - Custom-built
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
      allOf:
      - contains:
          properties:
            schema:additionalType:
              contains:
                const: XCT
              schema:inDefinedTermSet: ada:vocab/instrumentType
          required:
          - schema:additionalType
    ada:rotationRangeDefault:
      description: Total angular range over which projection images are acquired,
        in degrees.
      anyOf:
      - type: number
      - type: string
    ada:numberOfProjectionsDefault:
      description: Total number of equally-spaced projection images acquired over
        the full rotation range. For Mode B (multi-volume stitching), this is the
        number per sub-volume.
      anyOf:
      - type: integer
      - type: string
    ada:exposureTimePerProjectionDefault:
      description: "Duration of X-ray exposure for each individual projection image
        frame, in seconds. Adjustment is warranted for samples that are unusually
        dense or unusually transparent. If the exposure time was varied across samples
        within the same procedure or session, report the full range applied (e.g.,
        0.5\u20132 s)."
      anyOf:
      - type: number
      - type: string
    ada:rotationModeDefault:
      description: Whether projection images are acquired during continuous sample
        rotation (faster; may introduce slight motion blur at high rotation speeds)
        or at discrete step positions with the stage stationary during each exposure
        (stop-and-shoot; eliminates motion blur).
      type: string
      enum:
      - Step rotation (stop-and-shoot)
      - Continuous rotation
      - N/A
      - None
      - missing
    ada:minimumSubVolumeOverlap:
      description: Minimum number of reconstructed slices that must overlap between
        adjacent sub-volumes in a stitched dataset.
      anyOf:
      - type: integer
      - type: string
      readOnly: true
    ada:reconstructionAlgorithm:
      description: Mathematical algorithm used to reconstruct the 3D CT volume from
        2D projection images.
      anyOf:
      - type: string
        enum:
        - FDK (Feldkamp-Davis-Kress, cone-beam)
        - FBP (filtered back-projection, parallel-beam)
        - Iterative reconstruction
        - SART
        - N/A
        - None
        - missing
      - type: string
      readOnly: true
    ada:beamHardeningCorrectionMethod:
      description: Strategy used to reduce beam hardening artifacts caused by preferential
        attenuation of low-energy photons in polychromatic cone-beam XCT. The specific
        correction parameter value is recorded separately.
      anyOf:
      - type: string
        enum:
        - Hardware pre-filtering only (no software correction)
        - Software polynomial correction (instrument-specific algorithm)
        - Ketcham & Hanna (2014) iterative BH correction
        - None applied
        - N/A
        - missing
      - type: string
      readOnly: true
    ada:outputDataFormatDefault:
      description: File format of the reconstructed CT volume as output by the reconstruction
        software. Bit depth is recorded separately in Output Bit Depth.
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
    ada:segmentationMethodDefault:
      description: Method and software used to separate distinct phases or features
        in the reconstructed 3D volume, turning the grayscale volume into labelled
        regions.
      anyOf:
      - type: string
        enum:
        - Global threshold (single grayscale boundary)
        - Multi-threshold (separate range per phase)
        - Manual threshold per phase
        - 'Semi-automated: threshold + morphological filtering'
        - Region growing
        - Manual tracing
        - N/A
        - None
        - missing
      - type: string
    ada:analyticalMode:
      type: array
      items:
        type: string
        enum:
        - Single-volume
        - Multi-volume stitching
  required:
  - ada:targetFeature
  - ada:applicableSampleDimensionRange
  - ada:xRaySourceConfiguration
  - ada:detectorType
  - ada:rotationRangeDefault
  - ada:numberOfProjectionsDefault
  - ada:exposureTimePerProjectionDefault
  - ada:rotationModeDefault
  - ada:minimumSubVolumeOverlap
  - ada:reconstructionAlgorithm
  - ada:beamHardeningCorrectionMethod
  - ada:outputDataFormatDefault
  - ada:segmentationMethodDefault

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XCT/tapp/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XCT/tapp/schema.yaml)


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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XCT/tapp/context.jsonld)

## Sources

* [Lab-XCT_TAPP_v8.xlsx (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/XCT/tapp`

