
# LA-SF-ICP-MS Analysis Detail (Schema)

`ogch.techniqueProfile.geochemProfile.LA-SF-ICPMS.detail` *v0.1*

Dataset-level analysis-instance detail for LA-SF-ICP-MS, reusing CDIF/schema.org slots on the schema:Dataset root.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### detail example Zhang2022
detail instance derived from Zhang et al. 2022 (GCA 323) Iron meteorites Raster mapping + Spot (Ge) ns-LA-SF-ICP-MS Florida State University.
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
  "@id": "ex:laSficpmsTAPP-detail-Zhang2022",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
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
          "schema:value": "Electron-microprobe mapping, for the pallasites only — \"Quantitative analysis, mixed WDS/EDS element mapping, and characterization of the mineral phases from NWA 1911 and Zinder were performed\" on the Bruker instrument, producing Si, Al, Cr, Fe, Mg, Ca, Na, P and Ni maps \"along with backscattered electron (BSE) maps\" at 6 μm per pixel (pp.5–6); for the irons the paper states only that the rasters were \"taken on polished surfaces\" (p.5)"
        },
        {
          "@id": "ada:parameter/module/LaserAblation/transectRateMappingRateOrStepSize",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/LaserAblation/transectRateMappingRateOrStepSize"
            }
          ],
          "schema:name": "Transect Rate Mapping Rate or Step Size",
          "schema:value": "raster: 10 µm/s; Ge spots: N/A — 'scanned at 10 µm/s' (§2.2)"
        },
        {
          "@id": "ada:parameter/laSficpmsTAPP/numberOfReplicates",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laSficpmsTAPP/numberOfReplicates"
            }
          ],
          "schema:name": "Number of Replicates",
          "schema:value": 150,
          "schema:description": "N — 'a set of five 150 µm spots were analyzed ... on five of the irons, including both slabs of Klamath Falls' (§2.2)"
        },
        {
          "@id": "ada:parameter/module/LaserAblation/mappingArea",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/LaserAblation/mappingArea"
            }
          ],
          "schema:name": "Mapping Area",
          "schema:value": "Raster over \"a few millimeters\" of polished iron slab surface (area not precisely stated)"
        },
        {
          "@id": "ada:parameter/module/ICPMS/signalIntegrationTime",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/ICPMS/signalIntegrationTime"
            }
          ],
          "schema:name": "Signal Integration Time",
          "schema:value": 20,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "N — the Ge spots were ablated for 20 s (§2.2)"
        }
      ],
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "ICPMS",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/module/ICPMS/massResolutionSetting",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/module/ICPMS/massResolutionSetting"
                    }
                  ],
                  "schema:name": "Mass Resolution Setting",
                  "schema:value": "Low resolution (M/ΔM ≈ 400)"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:laSficpmsTAPP-detail-Zhang2022/instrument/ICPMS"
            },
            {
              "schema:additionalType": [
                "Laser Ablation System",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "ada:laserSpotGeometry": "raster: 50 µm beam spot; Ge spots: 150 µm — §2.2",
              "ada:laserRepetitionRate": "raster: 50 Hz; Ge spots: 50 Hz — §2.2",
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:laSficpmsTAPP-detail-Zhang2022/instrument/Laser-Ablation-System"
            }
          ]
        },
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "N — paper only states \"standardization techniques followed those of Humayun (2012)\"; no software named",
              "@type": [
                "schema:SoftwareApplication"
              ]
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
                "@id": "ada:parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection"
                  }
                ],
                "schema:name": "Pulse Analog Detector Nonlinearity Correction",
                "schema:value": "N — 'triple mode detection at 65% duty cycle' (§2.2); a cross-calibration is not described"
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
            "schema:description": "Polished slabs of the irons; a mount of Zinder and a section of NWA 1911 for the pallasites (§2.1); no acid treatment is described for the LA-ICP-MS specimens",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          }
        ]
      },
      "ada:combinedResults": [
        {}
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Plasma Analytical Facility, Florida State University, Tallahassee FL, USA"
      },
      "schema:description": "The raster pass gives the 23-element dataset; a separate set of 150 µm spots on five irons gives more precise Ge, since the raster 'failed to yield useful Ge abundances for Klamath Falls' (§2.2)",
      "ada:ablationSpotDuration": "20 s for the Ge spots — 'analyzed at 50 Hz for 20 s' (§2.2); the raster duration is not stated",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:proceduralBlankLevel": "no value available: ada:proceduralBlankLevel"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "N — compared with NAA on the same irons rather than a standard: differences 'mostly ... within the range of ±40%', within ±10% for Ni, Co and Ga, up to 30% for Au and As, and W in Cerro del Inca 4.39 ng/g by LA-ICP-MS against 1.06 ng/g by INAA (§2.3)"
    },
    {
      "dqv:isMeasurementOf": "Oxide production ratio",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Between-Session Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NASA Grants 80NSSC19K1238 (BZ), 80NSSC19K1613 (NLC), 80NSSC18K0595 (MH), NNX17AE77G (AER); NSF Cooperative Agreement DMR-1644779 and State of Florida [Acknowledgements]"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "EPMA (Brown University CAMECA SX-100)",
        "schema:description": "Quantitative analysis, mixed WDS/EDS element mapping, and characterization of mineral phases from NWA 1911 and Zinder [Section 2.5]"
      }
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA Grants 80NSSC19K1238 (BZ), 80NSSC19K1613 (NLC), 80NSSC18K0595 (MH), NNX17AE77G (AER); NSF Cooperative Agreement DMR-1644779 and State of Florida [Acknowledgements]",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Labelled by specimen within each meteorite: \"Cerro del Inca (museum number USNM 7062), Clark County (USNM 1304-a), Fitzwater Pass (CML 0413-6), Klamath Falls (USNM 7008-a and AMNH 4926-psl), Moonbi (USNM 1457-a), Nelson County (USNM 674-b), Oakley (iron) (USNM 780-d), and St. Genevieve County (USNM 454-a)\", plus a mount of Zinder and a thin section of NWA 1911 (p.4). Individual spots and lines \"are shown in Appendix 4\" (p.6), not in the archived PDF",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:transectLength": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:detectionLimit": "N — 'Concentrations below detection limits are not shown' (Table 3); the limits are not given",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:spotDiameterMeasured": -9999
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-SF-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:laSficpmsTAPP-detail-Zhang2022",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
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
          "schema:value": "Electron-microprobe mapping, for the pallasites only \u2014 \"Quantitative analysis, mixed WDS/EDS element mapping, and characterization of the mineral phases from NWA 1911 and Zinder were performed\" on the Bruker instrument, producing Si, Al, Cr, Fe, Mg, Ca, Na, P and Ni maps \"along with backscattered electron (BSE) maps\" at 6 \u03bcm per pixel (pp.5\u20136); for the irons the paper states only that the rasters were \"taken on polished surfaces\" (p.5)"
        },
        {
          "@id": "ada:parameter/module/LaserAblation/transectRateMappingRateOrStepSize",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/LaserAblation/transectRateMappingRateOrStepSize"
            }
          ],
          "schema:name": "Transect Rate Mapping Rate or Step Size",
          "schema:value": "raster: 10 \u00b5m/s; Ge spots: N/A \u2014 'scanned at 10 \u00b5m/s' (\u00a72.2)"
        },
        {
          "@id": "ada:parameter/laSficpmsTAPP/numberOfReplicates",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laSficpmsTAPP/numberOfReplicates"
            }
          ],
          "schema:name": "Number of Replicates",
          "schema:value": 150,
          "schema:description": "N \u2014 'a set of five 150 \u00b5m spots were analyzed ... on five of the irons, including both slabs of Klamath Falls' (\u00a72.2)"
        },
        {
          "@id": "ada:parameter/module/LaserAblation/mappingArea",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/LaserAblation/mappingArea"
            }
          ],
          "schema:name": "Mapping Area",
          "schema:value": "Raster over \"a few millimeters\" of polished iron slab surface (area not precisely stated)"
        },
        {
          "@id": "ada:parameter/module/ICPMS/signalIntegrationTime",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/ICPMS/signalIntegrationTime"
            }
          ],
          "schema:name": "Signal Integration Time",
          "schema:value": 20,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "N \u2014 the Ge spots were ablated for 20 s (\u00a72.2)"
        }
      ],
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "ICPMS",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/module/ICPMS/massResolutionSetting",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/module/ICPMS/massResolutionSetting"
                    }
                  ],
                  "schema:name": "Mass Resolution Setting",
                  "schema:value": "Low resolution (M/\u0394M \u2248 400)"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:laSficpmsTAPP-detail-Zhang2022/instrument/ICPMS"
            },
            {
              "schema:additionalType": [
                "Laser Ablation System",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "ada:laserSpotGeometry": "raster: 50 \u00b5m beam spot; Ge spots: 150 \u00b5m \u2014 \u00a72.2",
              "ada:laserRepetitionRate": "raster: 50 Hz; Ge spots: 50 Hz \u2014 \u00a72.2",
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:laSficpmsTAPP-detail-Zhang2022/instrument/Laser-Ablation-System"
            }
          ]
        },
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "N \u2014 paper only states \"standardization techniques followed those of Humayun (2012)\"; no software named",
              "@type": [
                "schema:SoftwareApplication"
              ]
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
                "@id": "ada:parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection"
                  }
                ],
                "schema:name": "Pulse Analog Detector Nonlinearity Correction",
                "schema:value": "N \u2014 'triple mode detection at 65% duty cycle' (\u00a72.2); a cross-calibration is not described"
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
            "schema:description": "Polished slabs of the irons; a mount of Zinder and a section of NWA 1911 for the pallasites (\u00a72.1); no acid treatment is described for the LA-ICP-MS specimens",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          }
        ]
      },
      "ada:combinedResults": [
        {}
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Plasma Analytical Facility, Florida State University, Tallahassee FL, USA"
      },
      "schema:description": "The raster pass gives the 23-element dataset; a separate set of 150 \u00b5m spots on five irons gives more precise Ge, since the raster 'failed to yield useful Ge abundances for Klamath Falls' (\u00a72.2)",
      "ada:ablationSpotDuration": "20 s for the Ge spots \u2014 'analyzed at 50 Hz for 20 s' (\u00a72.2); the raster duration is not stated",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:proceduralBlankLevel": "no value available: ada:proceduralBlankLevel"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "N \u2014 compared with NAA on the same irons rather than a standard: differences 'mostly ... within the range of \u00b140%', within \u00b110% for Ni, Co and Ga, up to 30% for Au and As, and W in Cerro del Inca 4.39 ng/g by LA-ICP-MS against 1.06 ng/g by INAA (\u00a72.3)"
    },
    {
      "dqv:isMeasurementOf": "Oxide production ratio",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Between-Session Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NASA Grants 80NSSC19K1238 (BZ), 80NSSC19K1613 (NLC), 80NSSC18K0595 (MH), NNX17AE77G (AER); NSF Cooperative Agreement DMR-1644779 and State of Florida [Acknowledgements]"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "EPMA (Brown University CAMECA SX-100)",
        "schema:description": "Quantitative analysis, mixed WDS/EDS element mapping, and characterization of mineral phases from NWA 1911 and Zinder [Section 2.5]"
      }
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA Grants 80NSSC19K1238 (BZ), 80NSSC19K1613 (NLC), 80NSSC18K0595 (MH), NNX17AE77G (AER); NSF Cooperative Agreement DMR-1644779 and State of Florida [Acknowledgements]",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Labelled by specimen within each meteorite: \"Cerro del Inca (museum number USNM 7062), Clark County (USNM 1304-a), Fitzwater Pass (CML 0413-6), Klamath Falls (USNM 7008-a and AMNH 4926-psl), Moonbi (USNM 1457-a), Nelson County (USNM 674-b), Oakley (iron) (USNM 780-d), and St. Genevieve County (USNM 454-a)\", plus a mount of Zinder and a thin section of NWA 1911 (p.4). Individual spots and lines \"are shown in Appendix 4\" (p.6), not in the archived PDF",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:transectLength": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:detectionLimit": "N \u2014 'Concentrations below detection limits are not shown' (Table 3); the limits are not given",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:spotDiameterMeasured": -9999
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

ex:laSficpmsTAPP-detail-Zhang2022 a schema1:Dataset,
        schema1:Product ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "NASA Grants 80NSSC19K1238 (BZ), 80NSSC19K1613 (NLC), 80NSSC18K0595 (MH), NNX17AE77G (AER); NSF Cooperative Agreement DMR-1644779 and State of Florida [Acknowledgements]" ] ;
    schema1:relatedLink [ schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "Quantitative analysis, mixed WDS/EDS element mapping, and characterization of mineral phases from NWA 1911 and Zinder [Section 2.5]" ;
                    schema1:name "EPMA (Brown University CAMECA SX-100)" ] ] ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Analytical Accuracy" ;
            dqv:value "N — compared with NAA on the same irons rather than a standard: differences 'mostly ... within the range of ±40%', within ±10% for Ni, Co and Ga, up to 30% for Au and As, and W in Cerro del Inca 4.39 ng/g by LA-ICP-MS against 1.06 ng/g by INAA (§2.3)" ],
        [ dqv:isMeasurementOf "Between-Session Analytical Precision" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Within-Session Analytical Precision" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Oxide production ratio" ;
            dqv:value "no value available: dqv:value" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Polished slabs of the irons; a mount of Zinder and a section of NWA 1911 for the pallasites (§2.1); no acid treatment is described for the LA-ICP-MS specimens" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 2 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection> ;
                            schema1:name "Data processing" ;
                            schema1:position 1 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/numberOfReplicates>,
                <https://ada.astromat.org/metadata/parameter/module/ICPMS/signalIntegrationTime>,
                <https://ada.astromat.org/metadata/parameter/module/LaserAblation/mappingArea>,
                <https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSize>,
                <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
            schema1:description "The raster pass gives the 23-element dataset; a separate set of 150 µm spots on five irons gives more precise Ge, since the raster 'failed to yield useful Ge abundances for Klamath Falls' (§2.2)" ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Plasma Analytical Facility, Florida State University, Tallahassee FL, USA" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ bios:computationalTool [ a schema1:SoftwareApplication ;
                            schema1:name "N — paper only states \"standardization techniques followed those of Humayun (2012)\"; no software named" ;
                            ada:toolRole "dataReduction" ] ],
                [ schema1:instrument <https://example.org/laSficpmsTAPP-detail-Zhang2022/instrument/ICPMS>,
                        <https://example.org/laSficpmsTAPP-detail-Zhang2022/instrument/Laser-Ablation-System> ] ;
            ada:ablationSpotDuration "20 s for the Ge spots — 'analyzed at 50 Hz for 20 s' (§2.2); the raster duration is not stated" ;
            ada:combinedResults [ ] ;
            ada:proceduralBlankLevel "no value available: ada:proceduralBlankLevel" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:detectionLimit "N — 'Concentrations below detection limits are not shown' (Table 3); the limits are not given" ;
    ada:fundingSourceForAnalysis "NASA Grants 80NSSC19K1238 (BZ), 80NSSC19K1613 (NLC), 80NSSC18K0595 (MH), NNX17AE77G (AER); NSF Cooperative Agreement DMR-1644779 and State of Florida [Acknowledgements]" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Labelled by specimen within each meteorite: \"Cerro del Inca (museum number USNM 7062), Clark County (USNM 1304-a), Fitzwater Pass (CML 0413-6), Klamath Falls (USNM 7008-a and AMNH 4926-psl), Moonbi (USNM 1457-a), Nelson County (USNM 674-b), Oakley (iron) (USNM 780-d), and St. Genevieve County (USNM 454-a)\", plus a mount of Zinder and a thin section of NWA 1911 (p.4). Individual spots and lines \"are shown in Appendix 4\" (p.6), not in the archived PDF" ;
    ada:sessionIdentifier "missing" ;
    ada:spotDiameter -9999 ;
    ada:spotDiameterMeasured -9999 ;
    ada:transectLength -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<https://example.org/laSficpmsTAPP-detail-Zhang2022/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSetting> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS" ;
    schema1:name "no value available: schema:name" .

<https://example.org/laSficpmsTAPP-detail-Zhang2022/instrument/Laser-Ablation-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Laser Ablation System" ;
    schema1:name "no value available: schema:name" ;
    ada:laserRepetitionRate "raster: 50 Hz; Ge spots: 50 Hz — §2.2" ;
    ada:laserSpotGeometry "raster: 50 µm beam spot; Ge spots: 150 µm — §2.2" .

<https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/numberOfReplicates> a schema1:PropertyValue ;
    schema1:description "N — 'a set of five 150 µm spots were analyzed ... on five of the irons, including both slabs of Klamath Falls' (§2.2)" ;
    schema1:name "Number of Replicates" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/numberOfReplicates> ;
    schema1:value 150 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSetting> a schema1:PropertyValue ;
    schema1:name "Mass Resolution Setting" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSetting> ;
    schema1:value "Low resolution (M/ΔM ≈ 400)" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/signalIntegrationTime> a schema1:PropertyValue ;
    schema1:description "N — the Ge spots were ablated for 20 s (§2.2)" ;
    schema1:name "Signal Integration Time" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/signalIntegrationTime> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 20 .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/mappingArea> a schema1:PropertyValue ;
    schema1:name "Mapping Area" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/LaserAblation/mappingArea> ;
    schema1:value "Raster over \"a few millimeters\" of polished iron slab surface (area not precisely stated)" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSize> a schema1:PropertyValue ;
    schema1:name "Transect Rate Mapping Rate or Step Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSize> ;
    schema1:value "raster: 10 µm/s; Ge spots: N/A — 'scanned at 10 µm/s' (§2.2)" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "Electron-microprobe mapping, for the pallasites only — \"Quantitative analysis, mixed WDS/EDS element mapping, and characterization of the mineral phases from NWA 1911 and Zinder were performed\" on the Bruker instrument, producing Si, Al, Cr, Fe, Mg, Ca, Na, P and Ni maps \"along with backscattered electron (BSE) maps\" at 6 μm per pixel (pp.5–6); for the irons the paper states only that the rasters were \"taken on polished surfaces\" (p.5)" .

<https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection> a schema1:PropertyValue ;
    schema1:name "Pulse Analog Detector Nonlinearity Correction" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection> ;
    schema1:value "N — 'triple mode detection at 65% duty cycle' (§2.2); a cross-calibration is not described" .


```


### detail example Chernonozhkin2021
detail instance derived from Chernonozhkin et al. 2021 (Chem Geol 562) Pallasite olivine Raster mapping (2D) ns-LA-SF-ICP-MS Ghent University.
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
  "@id": "ex:laSficpmsTAPP-detail-Chernonozhkin2021",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
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
          "schema:value": "μXRF mapping of larger sections, on which the ablation is sited — Fe Kα intensity maps identify the mineral phases \"based on the intensities of the Kα lines of the constituent major elements (Fe, Mg, Ni, Cr, S, Ca and P)\", and the LA-ICP-MS areas correspond \"to the locations indicated on the larger μXRF maps as black rectangles\" (p.4). The instrument is a Bruker M4 Tornado with a Rh-anode source at 50 kV and 150 μA, focused to \"a 25 μm spot (measured for Mo Kα)\" (p.3)"
        },
        {
          "@id": "ada:parameter/module/LaserAblation/transectRateMappingRateOrStepSize",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/LaserAblation/transectRateMappingRateOrStepSize"
            }
          ],
          "schema:name": "Transect Rate Mapping Rate or Step Size",
          "schema:value": "all: 9 µm/s — translation speed (§2.2.2)"
        },
        {
          "@id": "ada:parameter/module/ICPMS/makeUpGasAndFlowRate",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/ICPMS/makeUpGasAndFlowRate"
            }
          ],
          "schema:name": "Make-up Gas and Flow Rate",
          "schema:value": 0.81,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "Ar, 0.81–0.99 L/min — Table B1; 'No N2 was blent into ICP to avoid elevated nitrogen-based spectral interferences'"
        },
        {
          "@id": "ada:parameter/module/LaserAblation/mappingArea",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/LaserAblation/mappingArea"
            }
          ],
          "schema:name": "Mapping Area",
          "schema:value": "Each map: 1450×600 µm = 870,000 µm²; total of 8 PMG olivines mapped"
        },
        {
          "@id": "ada:parameter/module/ICPMS/signalIntegrationTime",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/ICPMS/signalIntegrationTime"
            }
          ],
          "schema:name": "Signal Integration Time",
          "schema:value": "N/A — mapping",
          "schema:unitText": "no value available: unnamed property"
        }
      ],
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "ICPMS",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/module/ICPMS/massResolutionSetting",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/module/ICPMS/massResolutionSetting"
                    }
                  ],
                  "schema:name": "Mass Resolution Setting",
                  "schema:value": "Low (M/ΔM = 300) — §2.2.2"
                },
                {
                  "@id": "ada:parameter/module/ICPMS/icpTuning",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/module/ICPMS/icpTuning"
                    }
                  ],
                  "schema:name": "ICP Tuning",
                  "schema:value": "N — oxide-based interferences 'were further minimized during tuning' (App. C4); no tuning procedure is described"
                },
                {
                  "@id": "ada:parameter/module/ICPMS/memoryEffectMitigation",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/module/ICPMS/memoryEffectMitigation"
                    }
                  ],
                  "schema:name": "Memory Effect Mitigation",
                  "schema:value": "Washout typically less than 1 s — §2.2.2"
                }
              ],
              "schema:hasPart": [
                {
                  "schema:additionalType": [
                    "ICP Source",
                    {
                      "@id": "https://www.wikidata.org/wiki/Q3099911"
                    }
                  ],
                  "schema:additionalProperty": [
                    {
                      "@id": "ada:parameter/module/ICPMS/coolantPlasmaGasFlowRate",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/ICPMS/coolantPlasmaGasFlowRate"
                        }
                      ],
                      "schema:name": "Coolant Plasma Gas Flow Rate",
                      "schema:value": 15,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "Ar, 15 L/min — Table B1"
                    },
                    {
                      "@id": "ada:parameter/module/ICPMS/auxiliaryGasFlowRate",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/ICPMS/auxiliaryGasFlowRate"
                        }
                      ],
                      "schema:name": "Auxiliary Gas Flow Rate",
                      "schema:value": 0.81,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "Ar, 0.81 L/min — Table B1"
                    },
                    {
                      "@id": "ada:parameter/module/ICPMS/rfPower",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/ICPMS/rfPower"
                        }
                      ],
                      "schema:name": "RF Power",
                      "schema:value": 800,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "800 W — cool plasma (§2.2.2, Table B1)"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:laSficpmsTAPP-detail-Chernonozhkin2021/instrument/ICPMS/part/ICP-Source"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:laSficpmsTAPP-detail-Chernonozhkin2021/instrument/ICPMS"
            },
            {
              "schema:additionalType": [
                "Laser Ablation System",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "ada:laserSpotGeometry": "all: 20 µm × 20 µm square-masked — §2.2.2",
              "ada:laserFluence": "5–7 J cm⁻²",
              "ada:laserRepetitionRate": "all: 20 Hz",
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:laSficpmsTAPP-detail-Chernonozhkin2021/instrument/Laser-Ablation-System"
            }
          ]
        },
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "In-house MatLab script (Appendix C1)",
              "@type": [
                "schema:SoftwareApplication"
              ]
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
                "@id": "ada:parameter/module/ICPMS/filteringApproach",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/ICPMS/filteringApproach"
                  }
                ],
                "schema:name": "Filtering Approach",
                "schema:value": "P-rich veinlet pixels masked: P2O5 above the best-fitting Gaussian of each map's P2O5 histogram plus 3 standard deviations — §3.1; 'A MATLAB script was applied to mask pixels representing veinlets'"
              },
              {
                "@id": "ada:parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection"
                  }
                ],
                "schema:name": "Pulse Analog Detector Nonlinearity Correction",
                "schema:value": "N — 'Triple' detection (Table B1); a cross-calibration is not described"
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
            "schema:description": "Flat polished thick sections (§2.1)",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          }
        ]
      },
      "ada:combinedResults": [
        {}
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Dept. of Chemistry, Atomic & Mass Spectrometry, Ghent University, Belgium"
      },
      "schema:description": "Cool plasma (800 W) mapping with a lateral resolution of approximately 20 µm; P-rich veinlets masked before averaging (§2.2.2, §3.1)",
      "ada:ablationSpotDuration": "N/A — mapping mode",
      "ada:rasterLineSpacing": "Adjacent lines — 'a grid of parallel, adjacent lines using a 20 µm × 20 µm square-masked laser spot' (§2.2.2)",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:proceduralBlankLevel": "no value available: ada:proceduralBlankLevel"
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "Planet Topers (BELSPO); FWO; Alexander von Humboldt Foundation; FWO/BOF-UGent"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "Planet Topers (BELSPO); FWO; Alexander von Humboldt Foundation; FWO/BOF-UGent",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only — \"Springwater, ... Brenham, Brahin and Seymchan, and ... Imilac, Cumulus Peak 04071, Esquel and Fukang\" (p.2); maps and line scans are not given labels of their own in the paper",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:detectionLimit": "all: per-pixel LODs, averaged over the map — Table E1 (Na = 1, Nb = 10), App. C5",
  "ada:limitOfQuantificationMethod": "all: as the LOD, with 10 SD instead of 3 SD — App. C5",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "missing",
  "ada:spotDiameterMeasured": -9999
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-SF-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:laSficpmsTAPP-detail-Chernonozhkin2021",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
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
          "schema:value": "\u03bcXRF mapping of larger sections, on which the ablation is sited \u2014 Fe K\u03b1 intensity maps identify the mineral phases \"based on the intensities of the K\u03b1 lines of the constituent major elements (Fe, Mg, Ni, Cr, S, Ca and P)\", and the LA-ICP-MS areas correspond \"to the locations indicated on the larger \u03bcXRF maps as black rectangles\" (p.4). The instrument is a Bruker M4 Tornado with a Rh-anode source at 50 kV and 150 \u03bcA, focused to \"a 25 \u03bcm spot (measured for Mo K\u03b1)\" (p.3)"
        },
        {
          "@id": "ada:parameter/module/LaserAblation/transectRateMappingRateOrStepSize",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/LaserAblation/transectRateMappingRateOrStepSize"
            }
          ],
          "schema:name": "Transect Rate Mapping Rate or Step Size",
          "schema:value": "all: 9 \u00b5m/s \u2014 translation speed (\u00a72.2.2)"
        },
        {
          "@id": "ada:parameter/module/ICPMS/makeUpGasAndFlowRate",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/ICPMS/makeUpGasAndFlowRate"
            }
          ],
          "schema:name": "Make-up Gas and Flow Rate",
          "schema:value": 0.81,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "Ar, 0.81\u20130.99 L/min \u2014 Table B1; 'No N2 was blent into ICP to avoid elevated nitrogen-based spectral interferences'"
        },
        {
          "@id": "ada:parameter/module/LaserAblation/mappingArea",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/LaserAblation/mappingArea"
            }
          ],
          "schema:name": "Mapping Area",
          "schema:value": "Each map: 1450\u00d7600 \u00b5m = 870,000 \u00b5m\u00b2; total of 8 PMG olivines mapped"
        },
        {
          "@id": "ada:parameter/module/ICPMS/signalIntegrationTime",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/ICPMS/signalIntegrationTime"
            }
          ],
          "schema:name": "Signal Integration Time",
          "schema:value": "N/A \u2014 mapping",
          "schema:unitText": "no value available: unnamed property"
        }
      ],
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "ICPMS",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/module/ICPMS/massResolutionSetting",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/module/ICPMS/massResolutionSetting"
                    }
                  ],
                  "schema:name": "Mass Resolution Setting",
                  "schema:value": "Low (M/\u0394M = 300) \u2014 \u00a72.2.2"
                },
                {
                  "@id": "ada:parameter/module/ICPMS/icpTuning",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/module/ICPMS/icpTuning"
                    }
                  ],
                  "schema:name": "ICP Tuning",
                  "schema:value": "N \u2014 oxide-based interferences 'were further minimized during tuning' (App. C4); no tuning procedure is described"
                },
                {
                  "@id": "ada:parameter/module/ICPMS/memoryEffectMitigation",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/module/ICPMS/memoryEffectMitigation"
                    }
                  ],
                  "schema:name": "Memory Effect Mitigation",
                  "schema:value": "Washout typically less than 1 s \u2014 \u00a72.2.2"
                }
              ],
              "schema:hasPart": [
                {
                  "schema:additionalType": [
                    "ICP Source",
                    {
                      "@id": "https://www.wikidata.org/wiki/Q3099911"
                    }
                  ],
                  "schema:additionalProperty": [
                    {
                      "@id": "ada:parameter/module/ICPMS/coolantPlasmaGasFlowRate",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/ICPMS/coolantPlasmaGasFlowRate"
                        }
                      ],
                      "schema:name": "Coolant Plasma Gas Flow Rate",
                      "schema:value": 15,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "Ar, 15 L/min \u2014 Table B1"
                    },
                    {
                      "@id": "ada:parameter/module/ICPMS/auxiliaryGasFlowRate",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/ICPMS/auxiliaryGasFlowRate"
                        }
                      ],
                      "schema:name": "Auxiliary Gas Flow Rate",
                      "schema:value": 0.81,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "Ar, 0.81 L/min \u2014 Table B1"
                    },
                    {
                      "@id": "ada:parameter/module/ICPMS/rfPower",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/ICPMS/rfPower"
                        }
                      ],
                      "schema:name": "RF Power",
                      "schema:value": 800,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "800 W \u2014 cool plasma (\u00a72.2.2, Table B1)"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:laSficpmsTAPP-detail-Chernonozhkin2021/instrument/ICPMS/part/ICP-Source"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:laSficpmsTAPP-detail-Chernonozhkin2021/instrument/ICPMS"
            },
            {
              "schema:additionalType": [
                "Laser Ablation System",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "ada:laserSpotGeometry": "all: 20 \u00b5m \u00d7 20 \u00b5m square-masked \u2014 \u00a72.2.2",
              "ada:laserFluence": "5\u20137 J cm\u207b\u00b2",
              "ada:laserRepetitionRate": "all: 20 Hz",
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:laSficpmsTAPP-detail-Chernonozhkin2021/instrument/Laser-Ablation-System"
            }
          ]
        },
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "In-house MatLab script (Appendix C1)",
              "@type": [
                "schema:SoftwareApplication"
              ]
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
                "@id": "ada:parameter/module/ICPMS/filteringApproach",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/ICPMS/filteringApproach"
                  }
                ],
                "schema:name": "Filtering Approach",
                "schema:value": "P-rich veinlet pixels masked: P2O5 above the best-fitting Gaussian of each map's P2O5 histogram plus 3 standard deviations \u2014 \u00a73.1; 'A MATLAB script was applied to mask pixels representing veinlets'"
              },
              {
                "@id": "ada:parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection"
                  }
                ],
                "schema:name": "Pulse Analog Detector Nonlinearity Correction",
                "schema:value": "N \u2014 'Triple' detection (Table B1); a cross-calibration is not described"
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
            "schema:description": "Flat polished thick sections (\u00a72.1)",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          }
        ]
      },
      "ada:combinedResults": [
        {}
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Dept. of Chemistry, Atomic & Mass Spectrometry, Ghent University, Belgium"
      },
      "schema:description": "Cool plasma (800 W) mapping with a lateral resolution of approximately 20 \u00b5m; P-rich veinlets masked before averaging (\u00a72.2.2, \u00a73.1)",
      "ada:ablationSpotDuration": "N/A \u2014 mapping mode",
      "ada:rasterLineSpacing": "Adjacent lines \u2014 'a grid of parallel, adjacent lines using a 20 \u00b5m \u00d7 20 \u00b5m square-masked laser spot' (\u00a72.2.2)",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:proceduralBlankLevel": "no value available: ada:proceduralBlankLevel"
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "Planet Topers (BELSPO); FWO; Alexander von Humboldt Foundation; FWO/BOF-UGent"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "Planet Topers (BELSPO); FWO; Alexander von Humboldt Foundation; FWO/BOF-UGent",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only \u2014 \"Springwater, ... Brenham, Brahin and Seymchan, and ... Imilac, Cumulus Peak 04071, Esquel and Fukang\" (p.2); maps and line scans are not given labels of their own in the paper",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:detectionLimit": "all: per-pixel LODs, averaged over the map \u2014 Table E1 (Na = 1, Nb = 10), App. C5",
  "ada:limitOfQuantificationMethod": "all: as the LOD, with 10 SD instead of 3 SD \u2014 App. C5",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "missing",
  "ada:spotDiameterMeasured": -9999
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

ex:laSficpmsTAPP-detail-Chernonozhkin2021 a schema1:Dataset,
        schema1:Product ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "Planet Topers (BELSPO); FWO; Alexander von Humboldt Foundation; FWO/BOF-UGent" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Flat polished thick sections (§2.1)" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 2 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproach>,
                                <https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection> ;
                            schema1:name "Data processing" ;
                            schema1:position 1 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRate>,
                <https://ada.astromat.org/metadata/parameter/module/ICPMS/signalIntegrationTime>,
                <https://ada.astromat.org/metadata/parameter/module/LaserAblation/mappingArea>,
                <https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSize>,
                <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
            schema1:description "Cool plasma (800 W) mapping with a lateral resolution of approximately 20 µm; P-rich veinlets masked before averaging (§2.2.2, §3.1)" ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Dept. of Chemistry, Atomic & Mass Spectrometry, Ghent University, Belgium" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ bios:computationalTool [ a schema1:SoftwareApplication ;
                            schema1:name "In-house MatLab script (Appendix C1)" ;
                            ada:toolRole "dataReduction" ] ],
                [ schema1:instrument <https://example.org/laSficpmsTAPP-detail-Chernonozhkin2021/instrument/ICPMS>,
                        <https://example.org/laSficpmsTAPP-detail-Chernonozhkin2021/instrument/Laser-Ablation-System> ] ;
            ada:ablationSpotDuration "N/A — mapping mode" ;
            ada:combinedResults [ ] ;
            ada:proceduralBlankLevel "no value available: ada:proceduralBlankLevel" ;
            ada:rasterLineSpacing "Adjacent lines — 'a grid of parallel, adjacent lines using a 20 µm × 20 µm square-masked laser spot' (§2.2.2)" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "missing" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:detectionLimit "all: per-pixel LODs, averaged over the map — Table E1 (Na = 1, Nb = 10), App. C5" ;
    ada:fundingSourceForAnalysis "Planet Topers (BELSPO); FWO; Alexander von Humboldt Foundation; FWO/BOF-UGent" ;
    ada:limitOfQuantificationMethod "all: as the LOD, with 10 SD instead of 3 SD — App. C5" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Sample name only — \"Springwater, ... Brenham, Brahin and Seymchan, and ... Imilac, Cumulus Peak 04071, Esquel and Fukang\" (p.2); maps and line scans are not given labels of their own in the paper" ;
    ada:sessionIdentifier "missing" ;
    ada:spotDiameter -9999 ;
    ada:spotDiameterMeasured -9999 ;
    ada:transectLength -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<https://example.org/laSficpmsTAPP-detail-Chernonozhkin2021/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSetting>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS" ;
    schema1:hasPart <https://example.org/laSficpmsTAPP-detail-Chernonozhkin2021/instrument/ICPMS/part/ICP-Source> ;
    schema1:name "no value available: schema:name" .

<https://example.org/laSficpmsTAPP-detail-Chernonozhkin2021/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRate>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<https://example.org/laSficpmsTAPP-detail-Chernonozhkin2021/instrument/Laser-Ablation-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Laser Ablation System" ;
    schema1:name "no value available: schema:name" ;
    ada:laserFluence "5–7 J cm⁻²" ;
    ada:laserRepetitionRate "all: 20 Hz" ;
    ada:laserSpotGeometry "all: 20 µm × 20 µm square-masked — §2.2.2" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRate> a schema1:PropertyValue ;
    schema1:description "Ar, 0.81 L/min — Table B1" ;
    schema1:name "Auxiliary Gas Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 8.1e-01 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate> a schema1:PropertyValue ;
    schema1:description "Ar, 15 L/min — Table B1" ;
    schema1:name "Coolant Plasma Gas Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 15 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproach> a schema1:PropertyValue ;
    schema1:name "Filtering Approach" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproach> ;
    schema1:value "P-rich veinlet pixels masked: P2O5 above the best-fitting Gaussian of each map's P2O5 histogram plus 3 standard deviations — §3.1; 'A MATLAB script was applied to mask pixels representing veinlets'" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning> a schema1:PropertyValue ;
    schema1:name "ICP Tuning" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning> ;
    schema1:value "N — oxide-based interferences 'were further minimized during tuning' (App. C4); no tuning procedure is described" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRate> a schema1:PropertyValue ;
    schema1:description "Ar, 0.81–0.99 L/min — Table B1; 'No N2 was blent into ICP to avoid elevated nitrogen-based spectral interferences'" ;
    schema1:name "Make-up Gas and Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 8.1e-01 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSetting> a schema1:PropertyValue ;
    schema1:name "Mass Resolution Setting" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSetting> ;
    schema1:value "Low (M/ΔM = 300) — §2.2.2" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> a schema1:PropertyValue ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> ;
    schema1:value "Washout typically less than 1 s — §2.2.2" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> a schema1:PropertyValue ;
    schema1:description "800 W — cool plasma (§2.2.2, Table B1)" ;
    schema1:name "RF Power" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 800 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/signalIntegrationTime> a schema1:PropertyValue ;
    schema1:name "Signal Integration Time" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/signalIntegrationTime> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value "N/A — mapping" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/mappingArea> a schema1:PropertyValue ;
    schema1:name "Mapping Area" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/LaserAblation/mappingArea> ;
    schema1:value "Each map: 1450×600 µm = 870,000 µm²; total of 8 PMG olivines mapped" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSize> a schema1:PropertyValue ;
    schema1:name "Transect Rate Mapping Rate or Step Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSize> ;
    schema1:value "all: 9 µm/s — translation speed (§2.2.2)" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "μXRF mapping of larger sections, on which the ablation is sited — Fe Kα intensity maps identify the mineral phases \"based on the intensities of the Kα lines of the constituent major elements (Fe, Mg, Ni, Cr, S, Ca and P)\", and the LA-ICP-MS areas correspond \"to the locations indicated on the larger μXRF maps as black rectangles\" (p.4). The instrument is a Bruker M4 Tornado with a Rh-anode source at 50 kV and 150 μA, focused to \"a 25 μm spot (measured for Mo Kα)\" (p.3)" .

<https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection> a schema1:PropertyValue ;
    schema1:name "Pulse Analog Detector Nonlinearity Correction" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection> ;
    schema1:value "N — 'Triple' detection (Table B1); a cross-calibration is not described" .


```


### detail example Chernonozhkin2021-2
detail instance derived from Chernonozhkin et al. 2021 (Chem Geol 562) Pallasite olivine Line scan (Run 1: major) + Spot (Run 2: trace) [Multi-run] ns-LA-SF-ICP-MS Ghent University.
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
  "@id": "ex:laSficpmsTAPP-detail-Chernonozhkin2021-2",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:additionalProperty": [
              {
                "@id": "ada:parameter/module/LaserAblation/preAblationSurfaceTreatment",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/LaserAblation/preAblationSurfaceTreatment"
                  }
                ],
                "schema:name": "Pre Ablation Surface Treatment",
                "schema:value": "Pre-ablation before each analysis: 2 J/cm², 20 Hz, 150 µm square-masked spot, 300 µm/s — 'to avoid bias in the trace element concentrations due to re-deposition of ablated sample material after previous analyses' (§2.2.3)"
              }
            ],
            "schema:description": "Flat polished thick sections (§2.1)",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:additionalProperty": [
              {
                "@id": "ada:parameter/module/ICPMS/filteringApproach",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/ICPMS/filteringApproach"
                  }
                ],
                "schema:name": "Filtering Approach",
                "schema:value": "Surface-impurity spikes removed with a 3 sigma filter; results with significant spikes not included in Table 1; Pb and U not presented because of multiple spikes — §3.3"
              },
              {
                "@id": "ada:parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection"
                  }
                ],
                "schema:name": "Pulse Analog Detector Nonlinearity Correction",
                "schema:value": "N — 'Triple' detection (Table B1); at the 130 µm spot, major elements saturate the detector 'even when using the triple detection mode' (App. C2)"
              }
            ],
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          }
        ]
      },
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
          "schema:value": "μXRF mapping of larger sections, on which the ablation is sited — Fe Kα intensity maps identify the mineral phases \"based on the intensities of the Kα lines of the constituent major elements (Fe, Mg, Ni, Cr, S, Ca and P)\", and the LA-ICP-MS areas correspond \"to the locations indicated on the larger μXRF maps as black rectangles\" (p.4). The instrument is a Bruker M4 Tornado with a Rh-anode source at 50 kV and 150 μA, focused to \"a 25 μm spot (measured for Mo Kα)\" (p.3)"
        },
        {
          "@id": "ada:parameter/module/LaserAblation/transectRateMappingRateOrStepSize",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/LaserAblation/transectRateMappingRateOrStepSize"
            }
          ],
          "schema:name": "Transect Rate Mapping Rate or Step Size",
          "schema:value": "run 1: 10 µm/s; run 2: 10 µm/s"
        },
        {
          "@id": "ada:parameter/module/ICPMS/makeUpGasAndFlowRate",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/ICPMS/makeUpGasAndFlowRate"
            }
          ],
          "schema:name": "Make-up Gas and Flow Rate",
          "schema:value": 0.947,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "Ar, 0.947 L/min (both runs) — Table B1; no N2 added"
        },
        {
          "@id": "ada:parameter/laSficpmsTAPP/numberOfReplicates",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laSficpmsTAPP/numberOfReplicates"
            }
          ],
          "schema:name": "Number of Replicates",
          "schema:value": 3,
          "schema:description": "3 — 'Every analysis was carried out 3 times' (§2.2.3); Table B1 '400 µm lines, n = 3'"
        },
        {
          "@id": "ada:parameter/module/LaserAblation/transectLength",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/LaserAblation/transectLength"
            }
          ],
          "schema:name": "Transect Length",
          "schema:value": 400,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "Line scan length: 400 µm (runs 1 and 2; 34 runs adjusted to measure 400 µm line + blank + washout)"
        },
        {
          "@id": "ada:parameter/module/LaserAblation/mappingArea",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/LaserAblation/mappingArea"
            }
          ],
          "schema:name": "Mapping Area",
          "schema:value": "N/A — line scan + spot; not 2D raster"
        },
        {
          "@id": "ada:parameter/module/ICPMS/signalIntegrationTime",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/ICPMS/signalIntegrationTime"
            }
          ],
          "schema:name": "Signal Integration Time",
          "schema:value": 50,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "N — 50 s of sample ablation per line (Table B1); the integration window is not stated"
        }
      ],
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "ICPMS",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/module/ICPMS/massResolutionSetting",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/module/ICPMS/massResolutionSetting"
                    }
                  ],
                  "schema:name": "Mass Resolution Setting",
                  "schema:value": "run 1: medium (M/ΔM = 4000); run 2: low (M/ΔM = 300) — §2.2.3"
                },
                {
                  "@id": "ada:parameter/module/ICPMS/memoryEffectMitigation",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/module/ICPMS/memoryEffectMitigation"
                    }
                  ],
                  "schema:name": "Memory Effect Mitigation",
                  "schema:value": "11 s of washout per run — Table B1"
                }
              ],
              "schema:hasPart": [
                {
                  "schema:additionalType": [
                    "ICP Source",
                    {
                      "@id": "https://www.wikidata.org/wiki/Q3099911"
                    }
                  ],
                  "schema:additionalProperty": [
                    {
                      "@id": "ada:parameter/module/ICPMS/coolantPlasmaGasFlowRate",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/ICPMS/coolantPlasmaGasFlowRate"
                        }
                      ],
                      "schema:name": "Coolant Plasma Gas Flow Rate",
                      "schema:value": 15,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "Ar, 15 L/min — Table B1"
                    },
                    {
                      "@id": "ada:parameter/module/ICPMS/auxiliaryGasFlowRate",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/ICPMS/auxiliaryGasFlowRate"
                        }
                      ],
                      "schema:name": "Auxiliary Gas Flow Rate",
                      "schema:value": 0.9,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "Ar, 0.90 L/min — Table B1"
                    },
                    {
                      "@id": "ada:parameter/module/ICPMS/rfPower",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/ICPMS/rfPower"
                        }
                      ],
                      "schema:name": "RF Power",
                      "schema:value": 1000,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "1000 W (run 1 major elements + run 2 trace elements)"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:laSficpmsTAPP-detail-Chernonozhkin2021-2/instrument/ICPMS/part/ICP-Source"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:laSficpmsTAPP-detail-Chernonozhkin2021-2/instrument/ICPMS"
            },
            {
              "schema:additionalType": [
                "Laser Ablation System",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "ada:laserSpotGeometry": "run 1: 30 µm diameter circular-masked; run 2: 130 µm diameter — §2.2.3",
              "ada:laserFluence": "4.72 J/cm² (both runs) — §2.2.3",
              "ada:laserRepetitionRate": "run 1: 20 Hz; run 2: 40 Hz",
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:laSficpmsTAPP-detail-Chernonozhkin2021-2/instrument/Laser-Ablation-System"
            }
          ]
        },
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "In-house MatLab script (Appendix C2)",
              "@type": [
                "schema:SoftwareApplication"
              ]
            }
          ]
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Dept. of Chemistry, Atomic & Mass Spectrometry, Ghent University, Belgium"
      },
      "schema:description": "Two line-scan runs on the same line after pre-ablation: run 1 (30 µm, medium resolution) gives the major elements and Cr, which normalises run 2 (130 µm, low resolution) for the trace elements (§2.2.3, App. C2)",
      "ada:ablationSpotDuration": "50 s of sample ablation per 400 µm line, both runs — Table B1",
      "ada:rasterLineSpacing": "N/A — line scan + spot; not 2D mapping",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:proceduralBlankLevel": "no value available: ada:proceduralBlankLevel"
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "Planet Topers (BELSPO); FWO; Alexander von Humboldt Foundation; FWO/BOF-UGent"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "all: 1 standard deviation — Table 1: 'the uncertainty corresponds to 1 standard deviation'"
    },
    {
      "dqv:isMeasurementOf": "Oxide production ratio",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Between-Session Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "Planet Topers (BELSPO); FWO; Alexander von Humboldt Foundation; FWO/BOF-UGent",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only — \"Springwater, ... Brenham, Brahin and Seymchan, and ... Imilac, Cumulus Peak 04071, Esquel and Fukang\" (p.2); maps and line scans are not given labels of their own in the paper",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:detectionLimit": "Cu: 0.28 ng/g; Cs: 4.9 ng/g; Ba: 16 ng/g; W: 5.4 ng/g; Re: 0.42 ng/g; Ir: 0.95 ng/g; Pt: 0.73 ng/g; Au: 1.8 ng/g; Nb: 0.61 ng/g; other: Table 1 — stated in §3.3; LODs averaged over analyses (Na = 24, Nb = 5). §3.3 also gives 33 ng/g for Sr, which is not among the measured nuclides",
  "ada:limitOfQuantificationMethod": "all: as the LOD, with 10 SD instead of 3 SD — App. C5",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "missing",
  "ada:spotDiameterMeasured": -9999
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-SF-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:laSficpmsTAPP-detail-Chernonozhkin2021-2",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:additionalProperty": [
              {
                "@id": "ada:parameter/module/LaserAblation/preAblationSurfaceTreatment",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/LaserAblation/preAblationSurfaceTreatment"
                  }
                ],
                "schema:name": "Pre Ablation Surface Treatment",
                "schema:value": "Pre-ablation before each analysis: 2 J/cm\u00b2, 20 Hz, 150 \u00b5m square-masked spot, 300 \u00b5m/s \u2014 'to avoid bias in the trace element concentrations due to re-deposition of ablated sample material after previous analyses' (\u00a72.2.3)"
              }
            ],
            "schema:description": "Flat polished thick sections (\u00a72.1)",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:additionalProperty": [
              {
                "@id": "ada:parameter/module/ICPMS/filteringApproach",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/ICPMS/filteringApproach"
                  }
                ],
                "schema:name": "Filtering Approach",
                "schema:value": "Surface-impurity spikes removed with a 3 sigma filter; results with significant spikes not included in Table 1; Pb and U not presented because of multiple spikes \u2014 \u00a73.3"
              },
              {
                "@id": "ada:parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection"
                  }
                ],
                "schema:name": "Pulse Analog Detector Nonlinearity Correction",
                "schema:value": "N \u2014 'Triple' detection (Table B1); at the 130 \u00b5m spot, major elements saturate the detector 'even when using the triple detection mode' (App. C2)"
              }
            ],
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          }
        ]
      },
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
          "schema:value": "\u03bcXRF mapping of larger sections, on which the ablation is sited \u2014 Fe K\u03b1 intensity maps identify the mineral phases \"based on the intensities of the K\u03b1 lines of the constituent major elements (Fe, Mg, Ni, Cr, S, Ca and P)\", and the LA-ICP-MS areas correspond \"to the locations indicated on the larger \u03bcXRF maps as black rectangles\" (p.4). The instrument is a Bruker M4 Tornado with a Rh-anode source at 50 kV and 150 \u03bcA, focused to \"a 25 \u03bcm spot (measured for Mo K\u03b1)\" (p.3)"
        },
        {
          "@id": "ada:parameter/module/LaserAblation/transectRateMappingRateOrStepSize",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/LaserAblation/transectRateMappingRateOrStepSize"
            }
          ],
          "schema:name": "Transect Rate Mapping Rate or Step Size",
          "schema:value": "run 1: 10 \u00b5m/s; run 2: 10 \u00b5m/s"
        },
        {
          "@id": "ada:parameter/module/ICPMS/makeUpGasAndFlowRate",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/ICPMS/makeUpGasAndFlowRate"
            }
          ],
          "schema:name": "Make-up Gas and Flow Rate",
          "schema:value": 0.947,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "Ar, 0.947 L/min (both runs) \u2014 Table B1; no N2 added"
        },
        {
          "@id": "ada:parameter/laSficpmsTAPP/numberOfReplicates",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laSficpmsTAPP/numberOfReplicates"
            }
          ],
          "schema:name": "Number of Replicates",
          "schema:value": 3,
          "schema:description": "3 \u2014 'Every analysis was carried out 3 times' (\u00a72.2.3); Table B1 '400 \u00b5m lines, n = 3'"
        },
        {
          "@id": "ada:parameter/module/LaserAblation/transectLength",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/LaserAblation/transectLength"
            }
          ],
          "schema:name": "Transect Length",
          "schema:value": 400,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "Line scan length: 400 \u00b5m (runs 1 and 2; 34 runs adjusted to measure 400 \u00b5m line + blank + washout)"
        },
        {
          "@id": "ada:parameter/module/LaserAblation/mappingArea",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/LaserAblation/mappingArea"
            }
          ],
          "schema:name": "Mapping Area",
          "schema:value": "N/A \u2014 line scan + spot; not 2D raster"
        },
        {
          "@id": "ada:parameter/module/ICPMS/signalIntegrationTime",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/ICPMS/signalIntegrationTime"
            }
          ],
          "schema:name": "Signal Integration Time",
          "schema:value": 50,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "N \u2014 50 s of sample ablation per line (Table B1); the integration window is not stated"
        }
      ],
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "ICPMS",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/module/ICPMS/massResolutionSetting",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/module/ICPMS/massResolutionSetting"
                    }
                  ],
                  "schema:name": "Mass Resolution Setting",
                  "schema:value": "run 1: medium (M/\u0394M = 4000); run 2: low (M/\u0394M = 300) \u2014 \u00a72.2.3"
                },
                {
                  "@id": "ada:parameter/module/ICPMS/memoryEffectMitigation",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/module/ICPMS/memoryEffectMitigation"
                    }
                  ],
                  "schema:name": "Memory Effect Mitigation",
                  "schema:value": "11 s of washout per run \u2014 Table B1"
                }
              ],
              "schema:hasPart": [
                {
                  "schema:additionalType": [
                    "ICP Source",
                    {
                      "@id": "https://www.wikidata.org/wiki/Q3099911"
                    }
                  ],
                  "schema:additionalProperty": [
                    {
                      "@id": "ada:parameter/module/ICPMS/coolantPlasmaGasFlowRate",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/ICPMS/coolantPlasmaGasFlowRate"
                        }
                      ],
                      "schema:name": "Coolant Plasma Gas Flow Rate",
                      "schema:value": 15,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "Ar, 15 L/min \u2014 Table B1"
                    },
                    {
                      "@id": "ada:parameter/module/ICPMS/auxiliaryGasFlowRate",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/ICPMS/auxiliaryGasFlowRate"
                        }
                      ],
                      "schema:name": "Auxiliary Gas Flow Rate",
                      "schema:value": 0.9,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "Ar, 0.90 L/min \u2014 Table B1"
                    },
                    {
                      "@id": "ada:parameter/module/ICPMS/rfPower",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/ICPMS/rfPower"
                        }
                      ],
                      "schema:name": "RF Power",
                      "schema:value": 1000,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "1000 W (run 1 major elements + run 2 trace elements)"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:laSficpmsTAPP-detail-Chernonozhkin2021-2/instrument/ICPMS/part/ICP-Source"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:laSficpmsTAPP-detail-Chernonozhkin2021-2/instrument/ICPMS"
            },
            {
              "schema:additionalType": [
                "Laser Ablation System",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "ada:laserSpotGeometry": "run 1: 30 \u00b5m diameter circular-masked; run 2: 130 \u00b5m diameter \u2014 \u00a72.2.3",
              "ada:laserFluence": "4.72 J/cm\u00b2 (both runs) \u2014 \u00a72.2.3",
              "ada:laserRepetitionRate": "run 1: 20 Hz; run 2: 40 Hz",
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:laSficpmsTAPP-detail-Chernonozhkin2021-2/instrument/Laser-Ablation-System"
            }
          ]
        },
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "In-house MatLab script (Appendix C2)",
              "@type": [
                "schema:SoftwareApplication"
              ]
            }
          ]
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Dept. of Chemistry, Atomic & Mass Spectrometry, Ghent University, Belgium"
      },
      "schema:description": "Two line-scan runs on the same line after pre-ablation: run 1 (30 \u00b5m, medium resolution) gives the major elements and Cr, which normalises run 2 (130 \u00b5m, low resolution) for the trace elements (\u00a72.2.3, App. C2)",
      "ada:ablationSpotDuration": "50 s of sample ablation per 400 \u00b5m line, both runs \u2014 Table B1",
      "ada:rasterLineSpacing": "N/A \u2014 line scan + spot; not 2D mapping",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:proceduralBlankLevel": "no value available: ada:proceduralBlankLevel"
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "Planet Topers (BELSPO); FWO; Alexander von Humboldt Foundation; FWO/BOF-UGent"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "all: 1 standard deviation \u2014 Table 1: 'the uncertainty corresponds to 1 standard deviation'"
    },
    {
      "dqv:isMeasurementOf": "Oxide production ratio",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Between-Session Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "Planet Topers (BELSPO); FWO; Alexander von Humboldt Foundation; FWO/BOF-UGent",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only \u2014 \"Springwater, ... Brenham, Brahin and Seymchan, and ... Imilac, Cumulus Peak 04071, Esquel and Fukang\" (p.2); maps and line scans are not given labels of their own in the paper",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:detectionLimit": "Cu: 0.28 ng/g; Cs: 4.9 ng/g; Ba: 16 ng/g; W: 5.4 ng/g; Re: 0.42 ng/g; Ir: 0.95 ng/g; Pt: 0.73 ng/g; Au: 1.8 ng/g; Nb: 0.61 ng/g; other: Table 1 \u2014 stated in \u00a73.3; LODs averaged over analyses (Na = 24, Nb = 5). \u00a73.3 also gives 33 ng/g for Sr, which is not among the measured nuclides",
  "ada:limitOfQuantificationMethod": "all: as the LOD, with 10 SD instead of 3 SD \u2014 App. C5",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "missing",
  "ada:spotDiameterMeasured": -9999
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

ex:laSficpmsTAPP-detail-Chernonozhkin2021-2 a schema1:Dataset,
        schema1:Product ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "Planet Topers (BELSPO); FWO; Alexander von Humboldt Foundation; FWO/BOF-UGent" ] ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Oxide production ratio" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Goodness-of-Fit" ;
            dqv:value "all: 1 standard deviation — Table 1: 'the uncertainty corresponds to 1 standard deviation'" ],
        [ dqv:isMeasurementOf "Analytical Accuracy" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Within-Session Analytical Precision" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Between-Session Analytical Precision" ;
            dqv:value "no value available: dqv:value" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/LaserAblation/preAblationSurfaceTreatment> ;
                            schema1:description "Flat polished thick sections (§2.1)" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproach>,
                                <https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection> ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/numberOfReplicates>,
                <https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRate>,
                <https://ada.astromat.org/metadata/parameter/module/ICPMS/signalIntegrationTime>,
                <https://ada.astromat.org/metadata/parameter/module/LaserAblation/mappingArea>,
                <https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectLength>,
                <https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSize>,
                <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
            schema1:description "Two line-scan runs on the same line after pre-ablation: run 1 (30 µm, medium resolution) gives the major elements and Cr, which normalises run 2 (130 µm, low resolution) for the trace elements (§2.2.3, App. C2)" ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Dept. of Chemistry, Atomic & Mass Spectrometry, Ghent University, Belgium" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ schema1:instrument <https://example.org/laSficpmsTAPP-detail-Chernonozhkin2021-2/instrument/ICPMS>,
                        <https://example.org/laSficpmsTAPP-detail-Chernonozhkin2021-2/instrument/Laser-Ablation-System> ],
                [ bios:computationalTool [ a schema1:SoftwareApplication ;
                            schema1:name "In-house MatLab script (Appendix C2)" ;
                            ada:toolRole "dataReduction" ] ] ;
            ada:ablationSpotDuration "50 s of sample ablation per 400 µm line, both runs — Table B1" ;
            ada:combinedResults [ ] ;
            ada:proceduralBlankLevel "no value available: ada:proceduralBlankLevel" ;
            ada:rasterLineSpacing "N/A — line scan + spot; not 2D mapping" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "missing" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:detectionLimit "Cu: 0.28 ng/g; Cs: 4.9 ng/g; Ba: 16 ng/g; W: 5.4 ng/g; Re: 0.42 ng/g; Ir: 0.95 ng/g; Pt: 0.73 ng/g; Au: 1.8 ng/g; Nb: 0.61 ng/g; other: Table 1 — stated in §3.3; LODs averaged over analyses (Na = 24, Nb = 5). §3.3 also gives 33 ng/g for Sr, which is not among the measured nuclides" ;
    ada:fundingSourceForAnalysis "Planet Topers (BELSPO); FWO; Alexander von Humboldt Foundation; FWO/BOF-UGent" ;
    ada:limitOfQuantificationMethod "all: as the LOD, with 10 SD instead of 3 SD — App. C5" ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Sample name only — \"Springwater, ... Brenham, Brahin and Seymchan, and ... Imilac, Cumulus Peak 04071, Esquel and Fukang\" (p.2); maps and line scans are not given labels of their own in the paper" ;
    ada:sessionIdentifier "missing" ;
    ada:spotDiameter -9999 ;
    ada:spotDiameterMeasured -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<https://example.org/laSficpmsTAPP-detail-Chernonozhkin2021-2/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSetting>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS" ;
    schema1:hasPart <https://example.org/laSficpmsTAPP-detail-Chernonozhkin2021-2/instrument/ICPMS/part/ICP-Source> ;
    schema1:name "no value available: schema:name" .

<https://example.org/laSficpmsTAPP-detail-Chernonozhkin2021-2/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRate>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<https://example.org/laSficpmsTAPP-detail-Chernonozhkin2021-2/instrument/Laser-Ablation-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Laser Ablation System" ;
    schema1:name "no value available: schema:name" ;
    ada:laserFluence "4.72 J/cm² (both runs) — §2.2.3" ;
    ada:laserRepetitionRate "run 1: 20 Hz; run 2: 40 Hz" ;
    ada:laserSpotGeometry "run 1: 30 µm diameter circular-masked; run 2: 130 µm diameter — §2.2.3" .

<https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/numberOfReplicates> a schema1:PropertyValue ;
    schema1:description "3 — 'Every analysis was carried out 3 times' (§2.2.3); Table B1 '400 µm lines, n = 3'" ;
    schema1:name "Number of Replicates" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/numberOfReplicates> ;
    schema1:value 3 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRate> a schema1:PropertyValue ;
    schema1:description "Ar, 0.90 L/min — Table B1" ;
    schema1:name "Auxiliary Gas Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 9e-01 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate> a schema1:PropertyValue ;
    schema1:description "Ar, 15 L/min — Table B1" ;
    schema1:name "Coolant Plasma Gas Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 15 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproach> a schema1:PropertyValue ;
    schema1:name "Filtering Approach" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproach> ;
    schema1:value "Surface-impurity spikes removed with a 3 sigma filter; results with significant spikes not included in Table 1; Pb and U not presented because of multiple spikes — §3.3" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRate> a schema1:PropertyValue ;
    schema1:description "Ar, 0.947 L/min (both runs) — Table B1; no N2 added" ;
    schema1:name "Make-up Gas and Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 9.47e-01 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSetting> a schema1:PropertyValue ;
    schema1:name "Mass Resolution Setting" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSetting> ;
    schema1:value "run 1: medium (M/ΔM = 4000); run 2: low (M/ΔM = 300) — §2.2.3" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> a schema1:PropertyValue ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> ;
    schema1:value "11 s of washout per run — Table B1" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> a schema1:PropertyValue ;
    schema1:description "1000 W (run 1 major elements + run 2 trace elements)" ;
    schema1:name "RF Power" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1000 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/signalIntegrationTime> a schema1:PropertyValue ;
    schema1:description "N — 50 s of sample ablation per line (Table B1); the integration window is not stated" ;
    schema1:name "Signal Integration Time" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/signalIntegrationTime> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 50 .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/mappingArea> a schema1:PropertyValue ;
    schema1:name "Mapping Area" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/LaserAblation/mappingArea> ;
    schema1:value "N/A — line scan + spot; not 2D raster" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/preAblationSurfaceTreatment> a schema1:PropertyValue ;
    schema1:name "Pre Ablation Surface Treatment" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/LaserAblation/preAblationSurfaceTreatment> ;
    schema1:value "Pre-ablation before each analysis: 2 J/cm², 20 Hz, 150 µm square-masked spot, 300 µm/s — 'to avoid bias in the trace element concentrations due to re-deposition of ablated sample material after previous analyses' (§2.2.3)" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectLength> a schema1:PropertyValue ;
    schema1:description "Line scan length: 400 µm (runs 1 and 2; 34 runs adjusted to measure 400 µm line + blank + washout)" ;
    schema1:name "Transect Length" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectLength> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 400 .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSize> a schema1:PropertyValue ;
    schema1:name "Transect Rate Mapping Rate or Step Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSize> ;
    schema1:value "run 1: 10 µm/s; run 2: 10 µm/s" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "μXRF mapping of larger sections, on which the ablation is sited — Fe Kα intensity maps identify the mineral phases \"based on the intensities of the Kα lines of the constituent major elements (Fe, Mg, Ni, Cr, S, Ca and P)\", and the LA-ICP-MS areas correspond \"to the locations indicated on the larger μXRF maps as black rectangles\" (p.4). The instrument is a Bruker M4 Tornado with a Rh-anode source at 50 kV and 150 μA, focused to \"a 25 μm spot (measured for Mo Kα)\" (p.3)" .

<https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection> a schema1:PropertyValue ;
    schema1:name "Pulse Analog Detector Nonlinearity Correction" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection> ;
    schema1:value "N — 'Triple' detection (Table B1); at the 130 µm spot, major elements saturate the detector 'even when using the triple detection mode' (App. C2)" .


```


### detail example Chernonozhkin2021-3
detail instance derived from Chernonozhkin et al. 2021 (Chem Geol 562) Pallasite phosphate Spot analysis ns-LA-SF-ICP-MS Ghent University.
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
  "@id": "ex:laSficpmsTAPP-detail-Chernonozhkin2021-3",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
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
          "schema:value": "μXRF mapping of larger sections, on which the ablation is sited — Fe Kα intensity maps identify the mineral phases \"based on the intensities of the Kα lines of the constituent major elements (Fe, Mg, Ni, Cr, S, Ca and P)\", and the LA-ICP-MS areas correspond \"to the locations indicated on the larger μXRF maps as black rectangles\" (p.4). The instrument is a Bruker M4 Tornado with a Rh-anode source at 50 kV and 150 μA, focused to \"a 25 μm spot (measured for Mo Kα)\" (p.3)"
        },
        {
          "@id": "ada:parameter/module/LaserAblation/transectRateMappingRateOrStepSize",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/LaserAblation/transectRateMappingRateOrStepSize"
            }
          ],
          "schema:name": "Transect Rate Mapping Rate or Step Size",
          "schema:value": "N/A — spot mode"
        },
        {
          "@id": "ada:parameter/module/ICPMS/makeUpGasAndFlowRate",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/ICPMS/makeUpGasAndFlowRate"
            }
          ],
          "schema:name": "Make-up Gas and Flow Rate",
          "schema:value": 0.96,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "Ar make-up: 0.96 l min⁻¹; N₂ not added"
        },
        {
          "@id": "ada:parameter/laSficpmsTAPP/numberOfReplicates",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laSficpmsTAPP/numberOfReplicates"
            }
          ],
          "schema:name": "Number of Replicates",
          "schema:value": 2,
          "schema:description": "N — Table 2 lists each 'single parallel measurement' per grain; 'Parallel analyses of single phosphate grains are highly reproducible' (§3.4)"
        },
        {
          "@id": "ada:parameter/module/ICPMS/signalIntegrationTime",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/ICPMS/signalIntegrationTime"
            }
          ],
          "schema:name": "Signal Integration Time",
          "schema:value": 20,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "N — 20 s of spot ablation (§2.2.4)"
        }
      ],
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "ICPMS",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/module/ICPMS/massResolutionSetting",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/module/ICPMS/massResolutionSetting"
                    }
                  ],
                  "schema:name": "Mass Resolution Setting",
                  "schema:value": "Low resolution (M/ΔM = 300)"
                },
                {
                  "@id": "ada:parameter/module/ICPMS/memoryEffectMitigation",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/module/ICPMS/memoryEffectMitigation"
                    }
                  ],
                  "schema:name": "Memory Effect Mitigation",
                  "schema:value": "10 s washout time after 20 s spot ablation (specified in acquisition protocol)"
                }
              ],
              "schema:hasPart": [
                {
                  "schema:additionalType": [
                    "ICP Source",
                    {
                      "@id": "https://www.wikidata.org/wiki/Q3099911"
                    }
                  ],
                  "schema:additionalProperty": [
                    {
                      "@id": "ada:parameter/module/ICPMS/coolantPlasmaGasFlowRate",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/ICPMS/coolantPlasmaGasFlowRate"
                        }
                      ],
                      "schema:name": "Coolant Plasma Gas Flow Rate",
                      "schema:value": 15,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "Ar, 15 L/min — Table B1"
                    },
                    {
                      "@id": "ada:parameter/module/ICPMS/auxiliaryGasFlowRate",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/ICPMS/auxiliaryGasFlowRate"
                        }
                      ],
                      "schema:name": "Auxiliary Gas Flow Rate",
                      "schema:value": 0.85,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "Ar, 0.85 L/min — Table B1"
                    },
                    {
                      "@id": "ada:parameter/module/ICPMS/rfPower",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/ICPMS/rfPower"
                        }
                      ],
                      "schema:name": "RF Power",
                      "schema:value": 1000,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "1000 W"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:laSficpmsTAPP-detail-Chernonozhkin2021-3/instrument/ICPMS/part/ICP-Source"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:laSficpmsTAPP-detail-Chernonozhkin2021-3/instrument/ICPMS"
            },
            {
              "schema:additionalType": [
                "Laser Ablation System",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "ada:laserSpotGeometry": "all: 110 µm diameter circular-masked — §2.2.4",
              "ada:laserFluence": "3.5 J cm⁻²",
              "ada:laserRepetitionRate": "all: 20 Hz",
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:laSficpmsTAPP-detail-Chernonozhkin2021-3/instrument/Laser-Ablation-System"
            }
          ]
        },
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "In-house MatLab script (Appendix C3)",
              "@type": [
                "schema:SoftwareApplication"
              ]
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
                "@id": "ada:parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection"
                  }
                ],
                "schema:name": "Pulse Analog Detector Nonlinearity Correction",
                "schema:value": "N — 'Triple' detection (Table B1)"
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
            "schema:description": "Flat polished thick sections (§2.1)",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          }
        ]
      },
      "ada:combinedResults": [
        {}
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Dept. of Chemistry, Atomic & Mass Spectrometry, Ghent University, Belgium"
      },
      "schema:description": "No phosphate reference material exists, so glasses calibrate (App. C3); grains identified as stanfieldite or merrillite from a Ca/(Ca + Mg) plot (§3.4)",
      "ada:ablationSpotDuration": "20 s spot ablation (plus 10 s washout); 25 cycles acquisition",
      "ada:rasterLineSpacing": "N/A — spot mode",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:proceduralBlankLevel": "no value available: ada:proceduralBlankLevel"
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "Planet Topers (BELSPO); FWO; Alexander von Humboldt Foundation; FWO/BOF-UGent"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "Planet Topers (BELSPO); FWO; Alexander von Humboldt Foundation; FWO/BOF-UGent",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Labelled: phosphate grains per pallasite, \"Ph1\", \"Ph2\", \"Ph3\", \"Ph4\" with mineral (\"stanf\", \"merr\"), and each \"single parallel measurement\" numbered (Table 2, p.10) — for Brahin, CMS 04071, Esquel and Seymchan",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "missing",
  "ada:spotDiameterMeasured": -9999
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-SF-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:laSficpmsTAPP-detail-Chernonozhkin2021-3",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
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
          "schema:value": "\u03bcXRF mapping of larger sections, on which the ablation is sited \u2014 Fe K\u03b1 intensity maps identify the mineral phases \"based on the intensities of the K\u03b1 lines of the constituent major elements (Fe, Mg, Ni, Cr, S, Ca and P)\", and the LA-ICP-MS areas correspond \"to the locations indicated on the larger \u03bcXRF maps as black rectangles\" (p.4). The instrument is a Bruker M4 Tornado with a Rh-anode source at 50 kV and 150 \u03bcA, focused to \"a 25 \u03bcm spot (measured for Mo K\u03b1)\" (p.3)"
        },
        {
          "@id": "ada:parameter/module/LaserAblation/transectRateMappingRateOrStepSize",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/LaserAblation/transectRateMappingRateOrStepSize"
            }
          ],
          "schema:name": "Transect Rate Mapping Rate or Step Size",
          "schema:value": "N/A \u2014 spot mode"
        },
        {
          "@id": "ada:parameter/module/ICPMS/makeUpGasAndFlowRate",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/ICPMS/makeUpGasAndFlowRate"
            }
          ],
          "schema:name": "Make-up Gas and Flow Rate",
          "schema:value": 0.96,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "Ar make-up: 0.96 l min\u207b\u00b9; N\u2082 not added"
        },
        {
          "@id": "ada:parameter/laSficpmsTAPP/numberOfReplicates",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laSficpmsTAPP/numberOfReplicates"
            }
          ],
          "schema:name": "Number of Replicates",
          "schema:value": 2,
          "schema:description": "N \u2014 Table 2 lists each 'single parallel measurement' per grain; 'Parallel analyses of single phosphate grains are highly reproducible' (\u00a73.4)"
        },
        {
          "@id": "ada:parameter/module/ICPMS/signalIntegrationTime",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/ICPMS/signalIntegrationTime"
            }
          ],
          "schema:name": "Signal Integration Time",
          "schema:value": 20,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "N \u2014 20 s of spot ablation (\u00a72.2.4)"
        }
      ],
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "ICPMS",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/module/ICPMS/massResolutionSetting",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/module/ICPMS/massResolutionSetting"
                    }
                  ],
                  "schema:name": "Mass Resolution Setting",
                  "schema:value": "Low resolution (M/\u0394M = 300)"
                },
                {
                  "@id": "ada:parameter/module/ICPMS/memoryEffectMitigation",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/module/ICPMS/memoryEffectMitigation"
                    }
                  ],
                  "schema:name": "Memory Effect Mitigation",
                  "schema:value": "10 s washout time after 20 s spot ablation (specified in acquisition protocol)"
                }
              ],
              "schema:hasPart": [
                {
                  "schema:additionalType": [
                    "ICP Source",
                    {
                      "@id": "https://www.wikidata.org/wiki/Q3099911"
                    }
                  ],
                  "schema:additionalProperty": [
                    {
                      "@id": "ada:parameter/module/ICPMS/coolantPlasmaGasFlowRate",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/ICPMS/coolantPlasmaGasFlowRate"
                        }
                      ],
                      "schema:name": "Coolant Plasma Gas Flow Rate",
                      "schema:value": 15,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "Ar, 15 L/min \u2014 Table B1"
                    },
                    {
                      "@id": "ada:parameter/module/ICPMS/auxiliaryGasFlowRate",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/ICPMS/auxiliaryGasFlowRate"
                        }
                      ],
                      "schema:name": "Auxiliary Gas Flow Rate",
                      "schema:value": 0.85,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "Ar, 0.85 L/min \u2014 Table B1"
                    },
                    {
                      "@id": "ada:parameter/module/ICPMS/rfPower",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/ICPMS/rfPower"
                        }
                      ],
                      "schema:name": "RF Power",
                      "schema:value": 1000,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "1000 W"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:laSficpmsTAPP-detail-Chernonozhkin2021-3/instrument/ICPMS/part/ICP-Source"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:laSficpmsTAPP-detail-Chernonozhkin2021-3/instrument/ICPMS"
            },
            {
              "schema:additionalType": [
                "Laser Ablation System",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "ada:laserSpotGeometry": "all: 110 \u00b5m diameter circular-masked \u2014 \u00a72.2.4",
              "ada:laserFluence": "3.5 J cm\u207b\u00b2",
              "ada:laserRepetitionRate": "all: 20 Hz",
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:laSficpmsTAPP-detail-Chernonozhkin2021-3/instrument/Laser-Ablation-System"
            }
          ]
        },
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "In-house MatLab script (Appendix C3)",
              "@type": [
                "schema:SoftwareApplication"
              ]
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
                "@id": "ada:parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection"
                  }
                ],
                "schema:name": "Pulse Analog Detector Nonlinearity Correction",
                "schema:value": "N \u2014 'Triple' detection (Table B1)"
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
            "schema:description": "Flat polished thick sections (\u00a72.1)",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          }
        ]
      },
      "ada:combinedResults": [
        {}
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Dept. of Chemistry, Atomic & Mass Spectrometry, Ghent University, Belgium"
      },
      "schema:description": "No phosphate reference material exists, so glasses calibrate (App. C3); grains identified as stanfieldite or merrillite from a Ca/(Ca + Mg) plot (\u00a73.4)",
      "ada:ablationSpotDuration": "20 s spot ablation (plus 10 s washout); 25 cycles acquisition",
      "ada:rasterLineSpacing": "N/A \u2014 spot mode",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:proceduralBlankLevel": "no value available: ada:proceduralBlankLevel"
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "Planet Topers (BELSPO); FWO; Alexander von Humboldt Foundation; FWO/BOF-UGent"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "Planet Topers (BELSPO); FWO; Alexander von Humboldt Foundation; FWO/BOF-UGent",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Labelled: phosphate grains per pallasite, \"Ph1\", \"Ph2\", \"Ph3\", \"Ph4\" with mineral (\"stanf\", \"merr\"), and each \"single parallel measurement\" numbered (Table 2, p.10) \u2014 for Brahin, CMS 04071, Esquel and Seymchan",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "missing",
  "ada:spotDiameterMeasured": -9999
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

ex:laSficpmsTAPP-detail-Chernonozhkin2021-3 a schema1:Dataset,
        schema1:Product ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "Planet Topers (BELSPO); FWO; Alexander von Humboldt Foundation; FWO/BOF-UGent" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection> ;
                            schema1:name "Data processing" ;
                            schema1:position 1 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Flat polished thick sections (§2.1)" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 2 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/numberOfReplicates>,
                <https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRate>,
                <https://ada.astromat.org/metadata/parameter/module/ICPMS/signalIntegrationTime>,
                <https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSize>,
                <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
            schema1:description "No phosphate reference material exists, so glasses calibrate (App. C3); grains identified as stanfieldite or merrillite from a Ca/(Ca + Mg) plot (§3.4)" ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Dept. of Chemistry, Atomic & Mass Spectrometry, Ghent University, Belgium" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ bios:computationalTool [ a schema1:SoftwareApplication ;
                            schema1:name "In-house MatLab script (Appendix C3)" ;
                            ada:toolRole "dataReduction" ] ],
                [ schema1:instrument <https://example.org/laSficpmsTAPP-detail-Chernonozhkin2021-3/instrument/ICPMS>,
                        <https://example.org/laSficpmsTAPP-detail-Chernonozhkin2021-3/instrument/Laser-Ablation-System> ] ;
            ada:ablationSpotDuration "20 s spot ablation (plus 10 s washout); 25 cycles acquisition" ;
            ada:combinedResults [ ] ;
            ada:proceduralBlankLevel "no value available: ada:proceduralBlankLevel" ;
            ada:rasterLineSpacing "N/A — spot mode" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "missing" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:detectionLimit -9999 ;
    ada:fundingSourceForAnalysis "Planet Topers (BELSPO); FWO; Alexander von Humboldt Foundation; FWO/BOF-UGent" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:mappingArea "missing" ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Labelled: phosphate grains per pallasite, \"Ph1\", \"Ph2\", \"Ph3\", \"Ph4\" with mineral (\"stanf\", \"merr\"), and each \"single parallel measurement\" numbered (Table 2, p.10) — for Brahin, CMS 04071, Esquel and Seymchan" ;
    ada:sessionIdentifier "missing" ;
    ada:spotDiameter -9999 ;
    ada:spotDiameterMeasured -9999 ;
    ada:transectLength -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<https://example.org/laSficpmsTAPP-detail-Chernonozhkin2021-3/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSetting>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS" ;
    schema1:hasPart <https://example.org/laSficpmsTAPP-detail-Chernonozhkin2021-3/instrument/ICPMS/part/ICP-Source> ;
    schema1:name "no value available: schema:name" .

<https://example.org/laSficpmsTAPP-detail-Chernonozhkin2021-3/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRate>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<https://example.org/laSficpmsTAPP-detail-Chernonozhkin2021-3/instrument/Laser-Ablation-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Laser Ablation System" ;
    schema1:name "no value available: schema:name" ;
    ada:laserFluence "3.5 J cm⁻²" ;
    ada:laserRepetitionRate "all: 20 Hz" ;
    ada:laserSpotGeometry "all: 110 µm diameter circular-masked — §2.2.4" .

<https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/numberOfReplicates> a schema1:PropertyValue ;
    schema1:description "N — Table 2 lists each 'single parallel measurement' per grain; 'Parallel analyses of single phosphate grains are highly reproducible' (§3.4)" ;
    schema1:name "Number of Replicates" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/numberOfReplicates> ;
    schema1:value 2 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRate> a schema1:PropertyValue ;
    schema1:description "Ar, 0.85 L/min — Table B1" ;
    schema1:name "Auxiliary Gas Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 8.5e-01 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate> a schema1:PropertyValue ;
    schema1:description "Ar, 15 L/min — Table B1" ;
    schema1:name "Coolant Plasma Gas Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 15 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRate> a schema1:PropertyValue ;
    schema1:description "Ar make-up: 0.96 l min⁻¹; N₂ not added" ;
    schema1:name "Make-up Gas and Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 9.6e-01 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSetting> a schema1:PropertyValue ;
    schema1:name "Mass Resolution Setting" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSetting> ;
    schema1:value "Low resolution (M/ΔM = 300)" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> a schema1:PropertyValue ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> ;
    schema1:value "10 s washout time after 20 s spot ablation (specified in acquisition protocol)" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> a schema1:PropertyValue ;
    schema1:description "1000 W" ;
    schema1:name "RF Power" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1000 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/signalIntegrationTime> a schema1:PropertyValue ;
    schema1:description "N — 20 s of spot ablation (§2.2.4)" ;
    schema1:name "Signal Integration Time" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/signalIntegrationTime> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 20 .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSize> a schema1:PropertyValue ;
    schema1:name "Transect Rate Mapping Rate or Step Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSize> ;
    schema1:value "N/A — spot mode" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "μXRF mapping of larger sections, on which the ablation is sited — Fe Kα intensity maps identify the mineral phases \"based on the intensities of the Kα lines of the constituent major elements (Fe, Mg, Ni, Cr, S, Ca and P)\", and the LA-ICP-MS areas correspond \"to the locations indicated on the larger μXRF maps as black rectangles\" (p.4). The instrument is a Bruker M4 Tornado with a Rh-anode source at 50 kV and 150 μA, focused to \"a 25 μm spot (measured for Mo Kα)\" (p.3)" .

<https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection> a schema1:PropertyValue ;
    schema1:name "Pulse Analog Detector Nonlinearity Correction" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection> ;
    schema1:value "N — 'Triple' detection (Table B1)" .


```


### detail example Mittlefehldt2024
detail instance derived from Mittlefehldt 2024 Appendix A Pallasite olivine Spot analysis ns-LA-SF-ICP-MS Johnson Space Center.
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
  "@id": "ex:laSficpmsTAPP-detail-Mittlefehldt2024",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:additionalProperty": [
              {
                "@id": "ada:parameter/module/LaserAblation/preAblationSurfaceTreatment",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/LaserAblation/preAblationSurfaceTreatment"
                  }
                ],
                "schema:name": "Pre Ablation Surface Treatment",
                "schema:value": "N — grains imaged by SEM to locate inclusion-free regions"
              }
            ],
            "schema:description": "Olivine grain fragments repeatedly washed in dilute HCl and triply distilled H₂O, hand-picked, polished grain mounts",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:additionalProperty": [
              {
                "@id": "ada:parameter/module/LaserAblation/signalSmoothing",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/LaserAblation/signalSmoothing"
                  }
                ],
                "schema:name": "Signal Smoothing",
                "schema:value": "N — parameters lost"
              },
              {
                "@id": "ada:parameter/module/ICPMS/filteringApproach",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/ICPMS/filteringApproach"
                  }
                ],
                "schema:name": "Filtering Approach",
                "schema:value": "Time steps with enhanced count rates from inclusions or heterogeneity excluded from the data reduction — §3.3"
              },
              {
                "@id": "ada:parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection"
                  }
                ],
                "schema:name": "Pulse Analog Detector Nonlinearity Correction",
                "schema:value": "N — parameters lost"
              }
            ],
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          }
        ]
      },
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
          "schema:value": "SEM imaging of the grain mounts, used to place the spots — \"The grains were first imaged using a scanning electron microscope (SEM) to locate regions for analysis. Regions containing surface inclusions were avoided for analysis\" (p.5); the grains are the same mounts already used for EMPA (p.5)"
        },
        {
          "@id": "ada:parameter/module/LaserAblation/transectRateMappingRateOrStepSize",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/LaserAblation/transectRateMappingRateOrStepSize"
            }
          ],
          "schema:name": "Transect Rate Mapping Rate or Step Size",
          "schema:value": "N/A — spot mode"
        },
        {
          "@id": "ada:parameter/module/ICPMS/makeUpGasAndFlowRate",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/ICPMS/makeUpGasAndFlowRate"
            }
          ],
          "schema:name": "Make-up Gas and Flow Rate",
          "schema:value": "N — parameters lost",
          "schema:unitText": "no value available: unnamed property"
        },
        {
          "@id": "ada:parameter/laSficpmsTAPP/numberOfReplicates",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laSficpmsTAPP/numberOfReplicates"
            }
          ],
          "schema:name": "Number of Replicates",
          "schema:value": "N — variable number of spots per sample"
        },
        {
          "@id": "ada:parameter/module/ICPMS/signalIntegrationTime",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/ICPMS/signalIntegrationTime"
            }
          ],
          "schema:name": "Signal Integration Time",
          "schema:value": "N — parameters lost",
          "schema:unitText": "no value available: unnamed property"
        }
      ],
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "ICPMS",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/module/ICPMS/massResolutionSetting",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/module/ICPMS/massResolutionSetting"
                    }
                  ],
                  "schema:name": "Mass Resolution Setting",
                  "schema:value": "Medium (m/Δm of 4000) — §3.3"
                },
                {
                  "@id": "ada:parameter/module/ICPMS/icpTuning",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/module/ICPMS/icpTuning"
                    }
                  ],
                  "schema:name": "ICP Tuning",
                  "schema:value": "N — parameters lost"
                },
                {
                  "@id": "ada:parameter/module/ICPMS/memoryEffectMitigation",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/module/ICPMS/memoryEffectMitigation"
                    }
                  ],
                  "schema:name": "Memory Effect Mitigation",
                  "schema:value": "N — parameters lost"
                }
              ],
              "schema:hasPart": [
                {
                  "schema:additionalType": [
                    "ICP Source",
                    {
                      "@id": "https://www.wikidata.org/wiki/Q3099911"
                    }
                  ],
                  "schema:additionalProperty": [
                    {
                      "@id": "ada:parameter/module/ICPMS/rfPower",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/ICPMS/rfPower"
                        }
                      ],
                      "schema:name": "RF Power",
                      "schema:value": "N — parameters lost",
                      "schema:unitText": "no value available: unnamed property"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:laSficpmsTAPP-detail-Mittlefehldt2024/instrument/ICPMS/part/ICP-Source"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:laSficpmsTAPP-detail-Mittlefehldt2024/instrument/ICPMS"
            },
            {
              "schema:additionalType": [
                "Laser Ablation System",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "ada:laserSpotGeometry": "all: 75 µm spot size — §3.3",
              "ada:laserFluence": "N — parameters lost",
              "ada:laserRepetitionRate": "N — parameters lost",
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:laSficpmsTAPP-detail-Mittlefehldt2024/instrument/Laser-Ablation-System"
            }
          ]
        },
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "Excel spreadsheets developed by C.-T. A. Lee (Rice University)",
              "@type": [
                "schema:SoftwareApplication"
              ]
            }
          ]
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "ICP-MS Laboratory, NASA Johnson Space Center, Houston TX, USA"
      },
      "schema:description": "The files documenting the analysis parameters (gas flows, laser power, etc.) were lost during an extended shutdown of the JSC ICP-MS laboratory; the grains are the EMPA grain mounts, 'low in inclusions, [but] not devoid of them' (§3.3)",
      "ada:ablationSpotDuration": "N — parameters lost",
      "ada:rasterLineSpacing": "N/A — spot mode",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:proceduralBlankLevel": "no value available: ada:proceduralBlankLevel"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "N — within-session precision not formally assessed"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "N — LA-ICP-MS Sc agrees with INAA 'with scatter of roughly ±0.5 µg/g'; Cr scatters more (§6.1)"
    },
    {
      "dqv:isMeasurementOf": "Oxide production ratio",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Between-Session Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "N — no funding section in this appendix document; funding would be in the parent paper which was not assessed"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "N — no funding section in this appendix document; funding would be in the parent paper which was not assessed",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Labelled: samples within each pallasite, e.g. \"Ac-1\", \"Ad-1\", \"Ah-1\", \"Ah-2\", \"Ah-3\", \"Al-1\", \"Br-1\" (Table S1, p.14); laser spots carry labels such as \"laser spot 059-Pa-1\" (p.8)",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:detectionLimit": "N — LODs not stated; concentrations reported for all nuclides above background",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:spotDiameterMeasured": -9999
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-SF-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:laSficpmsTAPP-detail-Mittlefehldt2024",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:additionalProperty": [
              {
                "@id": "ada:parameter/module/LaserAblation/preAblationSurfaceTreatment",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/LaserAblation/preAblationSurfaceTreatment"
                  }
                ],
                "schema:name": "Pre Ablation Surface Treatment",
                "schema:value": "N \u2014 grains imaged by SEM to locate inclusion-free regions"
              }
            ],
            "schema:description": "Olivine grain fragments repeatedly washed in dilute HCl and triply distilled H\u2082O, hand-picked, polished grain mounts",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          },
          {
            "schema:name": "Data processing",
            "schema:additionalProperty": [
              {
                "@id": "ada:parameter/module/LaserAblation/signalSmoothing",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/LaserAblation/signalSmoothing"
                  }
                ],
                "schema:name": "Signal Smoothing",
                "schema:value": "N \u2014 parameters lost"
              },
              {
                "@id": "ada:parameter/module/ICPMS/filteringApproach",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/ICPMS/filteringApproach"
                  }
                ],
                "schema:name": "Filtering Approach",
                "schema:value": "Time steps with enhanced count rates from inclusions or heterogeneity excluded from the data reduction \u2014 \u00a73.3"
              },
              {
                "@id": "ada:parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection"
                  }
                ],
                "schema:name": "Pulse Analog Detector Nonlinearity Correction",
                "schema:value": "N \u2014 parameters lost"
              }
            ],
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          }
        ]
      },
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
          "schema:value": "SEM imaging of the grain mounts, used to place the spots \u2014 \"The grains were first imaged using a scanning electron microscope (SEM) to locate regions for analysis. Regions containing surface inclusions were avoided for analysis\" (p.5); the grains are the same mounts already used for EMPA (p.5)"
        },
        {
          "@id": "ada:parameter/module/LaserAblation/transectRateMappingRateOrStepSize",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/LaserAblation/transectRateMappingRateOrStepSize"
            }
          ],
          "schema:name": "Transect Rate Mapping Rate or Step Size",
          "schema:value": "N/A \u2014 spot mode"
        },
        {
          "@id": "ada:parameter/module/ICPMS/makeUpGasAndFlowRate",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/ICPMS/makeUpGasAndFlowRate"
            }
          ],
          "schema:name": "Make-up Gas and Flow Rate",
          "schema:value": "N \u2014 parameters lost",
          "schema:unitText": "no value available: unnamed property"
        },
        {
          "@id": "ada:parameter/laSficpmsTAPP/numberOfReplicates",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laSficpmsTAPP/numberOfReplicates"
            }
          ],
          "schema:name": "Number of Replicates",
          "schema:value": "N \u2014 variable number of spots per sample"
        },
        {
          "@id": "ada:parameter/module/ICPMS/signalIntegrationTime",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/ICPMS/signalIntegrationTime"
            }
          ],
          "schema:name": "Signal Integration Time",
          "schema:value": "N \u2014 parameters lost",
          "schema:unitText": "no value available: unnamed property"
        }
      ],
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "ICPMS",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/module/ICPMS/massResolutionSetting",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/module/ICPMS/massResolutionSetting"
                    }
                  ],
                  "schema:name": "Mass Resolution Setting",
                  "schema:value": "Medium (m/\u0394m of 4000) \u2014 \u00a73.3"
                },
                {
                  "@id": "ada:parameter/module/ICPMS/icpTuning",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/module/ICPMS/icpTuning"
                    }
                  ],
                  "schema:name": "ICP Tuning",
                  "schema:value": "N \u2014 parameters lost"
                },
                {
                  "@id": "ada:parameter/module/ICPMS/memoryEffectMitigation",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/module/ICPMS/memoryEffectMitigation"
                    }
                  ],
                  "schema:name": "Memory Effect Mitigation",
                  "schema:value": "N \u2014 parameters lost"
                }
              ],
              "schema:hasPart": [
                {
                  "schema:additionalType": [
                    "ICP Source",
                    {
                      "@id": "https://www.wikidata.org/wiki/Q3099911"
                    }
                  ],
                  "schema:additionalProperty": [
                    {
                      "@id": "ada:parameter/module/ICPMS/rfPower",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/ICPMS/rfPower"
                        }
                      ],
                      "schema:name": "RF Power",
                      "schema:value": "N \u2014 parameters lost",
                      "schema:unitText": "no value available: unnamed property"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:laSficpmsTAPP-detail-Mittlefehldt2024/instrument/ICPMS/part/ICP-Source"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:laSficpmsTAPP-detail-Mittlefehldt2024/instrument/ICPMS"
            },
            {
              "schema:additionalType": [
                "Laser Ablation System",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "ada:laserSpotGeometry": "all: 75 \u00b5m spot size \u2014 \u00a73.3",
              "ada:laserFluence": "N \u2014 parameters lost",
              "ada:laserRepetitionRate": "N \u2014 parameters lost",
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:laSficpmsTAPP-detail-Mittlefehldt2024/instrument/Laser-Ablation-System"
            }
          ]
        },
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "Excel spreadsheets developed by C.-T. A. Lee (Rice University)",
              "@type": [
                "schema:SoftwareApplication"
              ]
            }
          ]
        }
      ],
      "ada:combinedResults": [
        {}
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "ICP-MS Laboratory, NASA Johnson Space Center, Houston TX, USA"
      },
      "schema:description": "The files documenting the analysis parameters (gas flows, laser power, etc.) were lost during an extended shutdown of the JSC ICP-MS laboratory; the grains are the EMPA grain mounts, 'low in inclusions, [but] not devoid of them' (\u00a73.3)",
      "ada:ablationSpotDuration": "N \u2014 parameters lost",
      "ada:rasterLineSpacing": "N/A \u2014 spot mode",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:proceduralBlankLevel": "no value available: ada:proceduralBlankLevel"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "N \u2014 within-session precision not formally assessed"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "N \u2014 LA-ICP-MS Sc agrees with INAA 'with scatter of roughly \u00b10.5 \u00b5g/g'; Cr scatters more (\u00a76.1)"
    },
    {
      "dqv:isMeasurementOf": "Oxide production ratio",
      "dqv:value": "no value available: dqv:value"
    },
    {
      "dqv:isMeasurementOf": "Between-Session Analytical Precision",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "N \u2014 no funding section in this appendix document; funding would be in the parent paper which was not assessed"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "N \u2014 no funding section in this appendix document; funding would be in the parent paper which was not assessed",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Labelled: samples within each pallasite, e.g. \"Ac-1\", \"Ad-1\", \"Ah-1\", \"Ah-2\", \"Ah-3\", \"Al-1\", \"Br-1\" (Table S1, p.14); laser spots carry labels such as \"laser spot 059-Pa-1\" (p.8)",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:detectionLimit": "N \u2014 LODs not stated; concentrations reported for all nuclides above background",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:spotDiameterMeasured": -9999
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

ex:laSficpmsTAPP-detail-Mittlefehldt2024 a schema1:Dataset,
        schema1:Product ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "N — no funding section in this appendix document; funding would be in the parent paper which was not assessed" ] ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Between-Session Analytical Precision" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Oxide production ratio" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Analytical Accuracy" ;
            dqv:value "N — LA-ICP-MS Sc agrees with INAA 'with scatter of roughly ±0.5 µg/g'; Cr scatters more (§6.1)" ],
        [ dqv:isMeasurementOf "Within-Session Analytical Precision" ;
            dqv:value "N — within-session precision not formally assessed" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproach>,
                                <https://ada.astromat.org/metadata/parameter/module/LaserAblation/signalSmoothing>,
                                <https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection> ;
                            schema1:name "Data processing" ;
                            schema1:position 2 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/LaserAblation/preAblationSurfaceTreatment> ;
                            schema1:description "Olivine grain fragments repeatedly washed in dilute HCl and triply distilled H₂O, hand-picked, polished grain mounts" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/numberOfReplicates>,
                <https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRate>,
                <https://ada.astromat.org/metadata/parameter/module/ICPMS/signalIntegrationTime>,
                <https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSize>,
                <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
            schema1:description "The files documenting the analysis parameters (gas flows, laser power, etc.) were lost during an extended shutdown of the JSC ICP-MS laboratory; the grains are the EMPA grain mounts, 'low in inclusions, [but] not devoid of them' (§3.3)" ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "ICP-MS Laboratory, NASA Johnson Space Center, Houston TX, USA" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ schema1:instrument <https://example.org/laSficpmsTAPP-detail-Mittlefehldt2024/instrument/ICPMS>,
                        <https://example.org/laSficpmsTAPP-detail-Mittlefehldt2024/instrument/Laser-Ablation-System> ],
                [ bios:computationalTool [ a schema1:SoftwareApplication ;
                            schema1:name "Excel spreadsheets developed by C.-T. A. Lee (Rice University)" ;
                            ada:toolRole "dataReduction" ] ] ;
            ada:ablationSpotDuration "N — parameters lost" ;
            ada:combinedResults [ ] ;
            ada:proceduralBlankLevel "no value available: ada:proceduralBlankLevel" ;
            ada:rasterLineSpacing "N/A — spot mode" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:detectionLimit "N — LODs not stated; concentrations reported for all nuclides above background" ;
    ada:fundingSourceForAnalysis "N — no funding section in this appendix document; funding would be in the parent paper which was not assessed" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:mappingArea "missing" ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Labelled: samples within each pallasite, e.g. \"Ac-1\", \"Ad-1\", \"Ah-1\", \"Ah-2\", \"Ah-3\", \"Al-1\", \"Br-1\" (Table S1, p.14); laser spots carry labels such as \"laser spot 059-Pa-1\" (p.8)" ;
    ada:sessionIdentifier "missing" ;
    ada:spotDiameter -9999 ;
    ada:spotDiameterMeasured -9999 ;
    ada:transectLength -9999 .

<https://example.org/laSficpmsTAPP-detail-Mittlefehldt2024/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSetting>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS" ;
    schema1:hasPart <https://example.org/laSficpmsTAPP-detail-Mittlefehldt2024/instrument/ICPMS/part/ICP-Source> ;
    schema1:name "no value available: schema:name" .

<https://example.org/laSficpmsTAPP-detail-Mittlefehldt2024/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<https://example.org/laSficpmsTAPP-detail-Mittlefehldt2024/instrument/Laser-Ablation-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Laser Ablation System" ;
    schema1:name "no value available: schema:name" ;
    ada:laserFluence "N — parameters lost" ;
    ada:laserRepetitionRate "N — parameters lost" ;
    ada:laserSpotGeometry "all: 75 µm spot size — §3.3" .

<https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/numberOfReplicates> a schema1:PropertyValue ;
    schema1:name "Number of Replicates" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/numberOfReplicates> ;
    schema1:value "N — variable number of spots per sample" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproach> a schema1:PropertyValue ;
    schema1:name "Filtering Approach" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproach> ;
    schema1:value "Time steps with enhanced count rates from inclusions or heterogeneity excluded from the data reduction — §3.3" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning> a schema1:PropertyValue ;
    schema1:name "ICP Tuning" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning> ;
    schema1:value "N — parameters lost" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRate> a schema1:PropertyValue ;
    schema1:name "Make-up Gas and Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value "N — parameters lost" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSetting> a schema1:PropertyValue ;
    schema1:name "Mass Resolution Setting" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSetting> ;
    schema1:value "Medium (m/Δm of 4000) — §3.3" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> a schema1:PropertyValue ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigation> ;
    schema1:value "N — parameters lost" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> a schema1:PropertyValue ;
    schema1:name "RF Power" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value "N — parameters lost" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/signalIntegrationTime> a schema1:PropertyValue ;
    schema1:name "Signal Integration Time" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/signalIntegrationTime> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value "N — parameters lost" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/preAblationSurfaceTreatment> a schema1:PropertyValue ;
    schema1:name "Pre Ablation Surface Treatment" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/LaserAblation/preAblationSurfaceTreatment> ;
    schema1:value "N — grains imaged by SEM to locate inclusion-free regions" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/signalSmoothing> a schema1:PropertyValue ;
    schema1:name "Signal Smoothing" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/LaserAblation/signalSmoothing> ;
    schema1:value "N — parameters lost" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSize> a schema1:PropertyValue ;
    schema1:name "Transect Rate Mapping Rate or Step Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSize> ;
    schema1:value "N/A — spot mode" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "SEM imaging of the grain mounts, used to place the spots — \"The grains were first imaged using a scanning electron microscope (SEM) to locate regions for analysis. Regions containing surface inclusions were avoided for analysis\" (p.5); the grains are the same mounts already used for EMPA (p.5)" .

<https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection> a schema1:PropertyValue ;
    schema1:name "Pulse Analog Detector Nonlinearity Correction" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection> ;
    schema1:value "N — parameters lost" .


```


### detail example Navarro2024
detail instance derived from Navarro et al. 2024 (ACS ESC 8) Iron meteorites Spot analysis ns-LA-SF-ICP-MS University of Campinas.
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
  "@id": "ex:laSficpmsTAPP-detail-Navarro2024",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
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
          "schema:value": "N — the preparation is stated without an imaging step: \"Before analyses, fragments about 1 cm were mounted in epoxy resin, polished, and cleaned with ultrapure water\" (p.3). The meteorites' structural classes were known beforehand (Table 1, p.2) but no screening of this material is described"
        },
        {
          "@id": "ada:parameter/module/LaserAblation/transectRateMappingRateOrStepSize",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/LaserAblation/transectRateMappingRateOrStepSize"
            }
          ],
          "schema:name": "Transect Rate Mapping Rate or Step Size",
          "schema:value": "N/A — spot mode"
        },
        {
          "@id": "ada:parameter/module/ICPMS/makeUpGasAndFlowRate",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/ICPMS/makeUpGasAndFlowRate"
            }
          ],
          "schema:name": "Make-up Gas and Flow Rate",
          "schema:value": 2,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "Ar makeup gas, combined via a T-piece near the torch; Table 2 lists a nebulizer gas flow rate of 1.1 L/min — Table 2"
        },
        {
          "@id": "ada:parameter/laSficpmsTAPP/numberOfReplicates",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laSficpmsTAPP/numberOfReplicates"
            }
          ],
          "schema:name": "Number of Replicates",
          "schema:value": 20,
          "schema:description": "20 spots in Arraias; n per meteorite in Table 3 — 'the mean value of 20 spot measurements in the Arraias meteorite'"
        },
        {
          "@id": "ada:parameter/module/ICPMS/signalIntegrationTime",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/ICPMS/signalIntegrationTime"
            }
          ],
          "schema:name": "Signal Integration Time",
          "schema:value": 40,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "40 s (full ablation interval used; background subtracted separately)"
        }
      ],
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "ICPMS",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/module/ICPMS/massResolutionSetting",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/module/ICPMS/massResolutionSetting"
                    }
                  ],
                  "schema:name": "Mass Resolution Setting",
                  "schema:value": "Low resolution (M/ΔM = 300)"
                },
                {
                  "@id": "ada:parameter/module/ICPMS/icpTuning",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/module/ICPMS/icpTuning"
                    }
                  ],
                  "schema:name": "ICP Tuning",
                  "schema:value": "ICP-MS and laser settings optimised daily 'to achieve the compromise between optimum signal intensity and low oxide formation, as specified by the factory'; mass calibration and detector cross-calibration 'systematically checked and redone if required' — Experimental section"
                }
              ],
              "schema:hasPart": [
                {
                  "schema:additionalType": [
                    "ICP Source",
                    {
                      "@id": "https://www.wikidata.org/wiki/Q3099911"
                    }
                  ],
                  "schema:additionalProperty": [
                    {
                      "@id": "ada:parameter/module/ICPMS/coolantPlasmaGasFlowRate",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/ICPMS/coolantPlasmaGasFlowRate"
                        }
                      ],
                      "schema:name": "Coolant Plasma Gas Flow Rate",
                      "schema:value": 16,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "16 L/min — Table 2 'plasma gas flow rate'"
                    },
                    {
                      "@id": "ada:parameter/module/ICPMS/auxiliaryGasFlowRate",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/ICPMS/auxiliaryGasFlowRate"
                        }
                      ],
                      "schema:name": "Auxiliary Gas Flow Rate",
                      "schema:value": 0.9,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "0.9 L/min — Table 2"
                    },
                    {
                      "@id": "ada:parameter/module/ICPMS/rfPower",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/ICPMS/rfPower"
                        }
                      ],
                      "schema:name": "RF Power",
                      "schema:value": 1200,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "1200 W"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:laSficpmsTAPP-detail-Navarro2024/instrument/ICPMS/part/ICP-Source"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:laSficpmsTAPP-detail-Navarro2024/instrument/ICPMS"
            },
            {
              "schema:additionalType": [
                "Laser Ablation System",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "ada:laserSpotGeometry": "all: 150 µm — Table 2 'spot diameter'",
              "ada:laserFluence": "7 J cm⁻²",
              "ada:laserRepetitionRate": "all: 10 Hz",
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:laSficpmsTAPP-detail-Navarro2024/instrument/Laser-Ablation-System"
            }
          ]
        },
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "iolite 4.5.7 with 3D Trace Elements DRS",
              "@type": [
                "schema:SoftwareApplication"
              ]
            }
          ]
        },
        {
          "bios:reagent": [
            {
              "ada:reagentRole": "referenceMaterial",
              "schema:name": "North Chile — 'also measured as an unknown sample several times, on different days, over four months', for intermediate precision; eight other known iron meteorites validate against published INAA values",
              "@type": [
                "schema:DefinedTerm"
              ]
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
                "@id": "ada:parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection"
                  }
                ],
                "schema:name": "Pulse Analog Detector Nonlinearity Correction",
                "schema:value": "N — 'detector cross-calibration were systematically checked and redone if required'; Fe and Ni measured on low-abundance isotopes in analog mode"
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
            "schema:description": "Fragments ~1 cm mounted in epoxy resin, polished, cleaned with ultrapure water",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          }
        ]
      },
      "ada:combinedResults": [
        {}
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Isotope Geology Laboratory, University of Campinas (UNICAMP), Brazil"
      },
      "schema:description": "Two measurement standards complement each other: North Chile for matrix similarity and NIST SRM 612 for its well-known composition; Fe + Ni + Co = 100% normalisation removes the need for an internal standard",
      "ada:ablationSpotDuration": "40 s — '20 s of blank measurement (laser-firing with the shutter closed), followed by 40 s of sample ablation'",
      "ada:rasterLineSpacing": "N/A — spot mode",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:proceduralBlankLevel": "no value available: ada:proceduralBlankLevel"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "N — precision is stated for samples: RSD <15% for 20 spots in Arraias except Cr (20%), Ir (16%) and Os (20%), and better than 20% for the other meteorites"
    },
    {
      "dqv:isMeasurementOf": "Between-Session Analytical Precision",
      "dqv:value": "North Chile [all: RSD 20% at worst] — measured as an unknown over four months; its RSD represents 'the laboratory reproducibility or intermediate precision conditions'"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "N — assessed on eight known iron meteorites, not a standard: 'More than 75% of published values are within the respective LA-ICP-MS result ±2s'; relative differences 'almost always within ±20%' (Fig. 2)"
    },
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "all: s, standard deviation of n measured values, and RSD — data table for Figs 2 and 3"
    },
    {
      "dqv:isMeasurementOf": "Oxide production ratio",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "M.S.N.: Educorp (Unicamp) and International Association of Geoanalysts for Geoanalysis 2022 presentation; J.E.: CNPq grant 316191/2021-3"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "M.S.N.: Educorp (Unicamp) and International Association of Geoanalysts for Geoanalysis 2022 presentation; J.E.: CNPq grant 316191/2021-3",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only — iron meteorites by name (Table 1, p.2), each analysed as \"fragments about 1 cm\" (p.3); spots and mapped areas are counted (\"points 176\", p.12), not labelled",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:detectionLimit": "As: 2; Au: 0.1; Co: 2; Cr: 19; Cu: 0.8; Fe: 60; Ga: 0.3; Ge: 3; Ir: 0.2; Ni: 36; Os: 0.2; Pd: 0.5; Pt: 0.3; Re: 0.1; Rh: 0.1; Ru: 1; W: 1 — µg/g, median values (Table 3 'LOD')",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:spotDiameterMeasured": -9999
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-SF-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:laSficpmsTAPP-detail-Navarro2024",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
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
          "schema:value": "N \u2014 the preparation is stated without an imaging step: \"Before analyses, fragments about 1 cm were mounted in epoxy resin, polished, and cleaned with ultrapure water\" (p.3). The meteorites' structural classes were known beforehand (Table 1, p.2) but no screening of this material is described"
        },
        {
          "@id": "ada:parameter/module/LaserAblation/transectRateMappingRateOrStepSize",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/LaserAblation/transectRateMappingRateOrStepSize"
            }
          ],
          "schema:name": "Transect Rate Mapping Rate or Step Size",
          "schema:value": "N/A \u2014 spot mode"
        },
        {
          "@id": "ada:parameter/module/ICPMS/makeUpGasAndFlowRate",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/ICPMS/makeUpGasAndFlowRate"
            }
          ],
          "schema:name": "Make-up Gas and Flow Rate",
          "schema:value": 2,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "Ar makeup gas, combined via a T-piece near the torch; Table 2 lists a nebulizer gas flow rate of 1.1 L/min \u2014 Table 2"
        },
        {
          "@id": "ada:parameter/laSficpmsTAPP/numberOfReplicates",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laSficpmsTAPP/numberOfReplicates"
            }
          ],
          "schema:name": "Number of Replicates",
          "schema:value": 20,
          "schema:description": "20 spots in Arraias; n per meteorite in Table 3 \u2014 'the mean value of 20 spot measurements in the Arraias meteorite'"
        },
        {
          "@id": "ada:parameter/module/ICPMS/signalIntegrationTime",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/ICPMS/signalIntegrationTime"
            }
          ],
          "schema:name": "Signal Integration Time",
          "schema:value": 40,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "40 s (full ablation interval used; background subtracted separately)"
        }
      ],
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "ICPMS",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/module/ICPMS/massResolutionSetting",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/module/ICPMS/massResolutionSetting"
                    }
                  ],
                  "schema:name": "Mass Resolution Setting",
                  "schema:value": "Low resolution (M/\u0394M = 300)"
                },
                {
                  "@id": "ada:parameter/module/ICPMS/icpTuning",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/module/ICPMS/icpTuning"
                    }
                  ],
                  "schema:name": "ICP Tuning",
                  "schema:value": "ICP-MS and laser settings optimised daily 'to achieve the compromise between optimum signal intensity and low oxide formation, as specified by the factory'; mass calibration and detector cross-calibration 'systematically checked and redone if required' \u2014 Experimental section"
                }
              ],
              "schema:hasPart": [
                {
                  "schema:additionalType": [
                    "ICP Source",
                    {
                      "@id": "https://www.wikidata.org/wiki/Q3099911"
                    }
                  ],
                  "schema:additionalProperty": [
                    {
                      "@id": "ada:parameter/module/ICPMS/coolantPlasmaGasFlowRate",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/ICPMS/coolantPlasmaGasFlowRate"
                        }
                      ],
                      "schema:name": "Coolant Plasma Gas Flow Rate",
                      "schema:value": 16,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "16 L/min \u2014 Table 2 'plasma gas flow rate'"
                    },
                    {
                      "@id": "ada:parameter/module/ICPMS/auxiliaryGasFlowRate",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/ICPMS/auxiliaryGasFlowRate"
                        }
                      ],
                      "schema:name": "Auxiliary Gas Flow Rate",
                      "schema:value": 0.9,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "0.9 L/min \u2014 Table 2"
                    },
                    {
                      "@id": "ada:parameter/module/ICPMS/rfPower",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/ICPMS/rfPower"
                        }
                      ],
                      "schema:name": "RF Power",
                      "schema:value": 1200,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "1200 W"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:laSficpmsTAPP-detail-Navarro2024/instrument/ICPMS/part/ICP-Source"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:laSficpmsTAPP-detail-Navarro2024/instrument/ICPMS"
            },
            {
              "schema:additionalType": [
                "Laser Ablation System",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "ada:laserSpotGeometry": "all: 150 \u00b5m \u2014 Table 2 'spot diameter'",
              "ada:laserFluence": "7 J cm\u207b\u00b2",
              "ada:laserRepetitionRate": "all: 10 Hz",
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:laSficpmsTAPP-detail-Navarro2024/instrument/Laser-Ablation-System"
            }
          ]
        },
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "iolite 4.5.7 with 3D Trace Elements DRS",
              "@type": [
                "schema:SoftwareApplication"
              ]
            }
          ]
        },
        {
          "bios:reagent": [
            {
              "ada:reagentRole": "referenceMaterial",
              "schema:name": "North Chile \u2014 'also measured as an unknown sample several times, on different days, over four months', for intermediate precision; eight other known iron meteorites validate against published INAA values",
              "@type": [
                "schema:DefinedTerm"
              ]
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
                "@id": "ada:parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection"
                  }
                ],
                "schema:name": "Pulse Analog Detector Nonlinearity Correction",
                "schema:value": "N \u2014 'detector cross-calibration were systematically checked and redone if required'; Fe and Ni measured on low-abundance isotopes in analog mode"
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
            "schema:description": "Fragments ~1 cm mounted in epoxy resin, polished, cleaned with ultrapure water",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          }
        ]
      },
      "ada:combinedResults": [
        {}
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Isotope Geology Laboratory, University of Campinas (UNICAMP), Brazil"
      },
      "schema:description": "Two measurement standards complement each other: North Chile for matrix similarity and NIST SRM 612 for its well-known composition; Fe + Ni + Co = 100% normalisation removes the need for an internal standard",
      "ada:ablationSpotDuration": "40 s \u2014 '20 s of blank measurement (laser-firing with the shutter closed), followed by 40 s of sample ablation'",
      "ada:rasterLineSpacing": "N/A \u2014 spot mode",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:proceduralBlankLevel": "no value available: ada:proceduralBlankLevel"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Within-Session Analytical Precision",
      "dqv:value": "N \u2014 precision is stated for samples: RSD <15% for 20 spots in Arraias except Cr (20%), Ir (16%) and Os (20%), and better than 20% for the other meteorites"
    },
    {
      "dqv:isMeasurementOf": "Between-Session Analytical Precision",
      "dqv:value": "North Chile [all: RSD 20% at worst] \u2014 measured as an unknown over four months; its RSD represents 'the laboratory reproducibility or intermediate precision conditions'"
    },
    {
      "dqv:isMeasurementOf": "Analytical Accuracy",
      "dqv:value": "N \u2014 assessed on eight known iron meteorites, not a standard: 'More than 75% of published values are within the respective LA-ICP-MS result \u00b12s'; relative differences 'almost always within \u00b120%' (Fig. 2)"
    },
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "all: s, standard deviation of n measured values, and RSD \u2014 data table for Figs 2 and 3"
    },
    {
      "dqv:isMeasurementOf": "Oxide production ratio",
      "dqv:value": "no value available: dqv:value"
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "M.S.N.: Educorp (Unicamp) and International Association of Geoanalysts for Geoanalysis 2022 presentation; J.E.: CNPq grant 316191/2021-3"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "M.S.N.: Educorp (Unicamp) and International Association of Geoanalysts for Geoanalysis 2022 presentation; J.E.: CNPq grant 316191/2021-3",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only \u2014 iron meteorites by name (Table 1, p.2), each analysed as \"fragments about 1 cm\" (p.3); spots and mapped areas are counted (\"points 176\", p.12), not labelled",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:detectionLimit": "As: 2; Au: 0.1; Co: 2; Cr: 19; Cu: 0.8; Fe: 60; Ga: 0.3; Ge: 3; Ir: 0.2; Ni: 36; Os: 0.2; Pd: 0.5; Pt: 0.3; Re: 0.1; Rh: 0.1; Ru: 1; W: 1 \u2014 \u00b5g/g, median values (Table 3 'LOD')",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:spotDiameterMeasured": -9999
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

ex:laSficpmsTAPP-detail-Navarro2024 a schema1:Dataset,
        schema1:Product ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "M.S.N.: Educorp (Unicamp) and International Association of Geoanalysts for Geoanalysis 2022 presentation; J.E.: CNPq grant 316191/2021-3" ] ;
    dqv:hasQualityMeasurement [ dqv:isMeasurementOf "Oxide production ratio" ;
            dqv:value "no value available: dqv:value" ],
        [ dqv:isMeasurementOf "Analytical Accuracy" ;
            dqv:value "N — assessed on eight known iron meteorites, not a standard: 'More than 75% of published values are within the respective LA-ICP-MS result ±2s'; relative differences 'almost always within ±20%' (Fig. 2)" ],
        [ dqv:isMeasurementOf "Goodness-of-Fit" ;
            dqv:value "all: s, standard deviation of n measured values, and RSD — data table for Figs 2 and 3" ],
        [ dqv:isMeasurementOf "Within-Session Analytical Precision" ;
            dqv:value "N — precision is stated for samples: RSD <15% for 20 spots in Arraias except Cr (20%), Ir (16%) and Os (20%), and better than 20% for the other meteorites" ],
        [ dqv:isMeasurementOf "Between-Session Analytical Precision" ;
            dqv:value "North Chile [all: RSD 20% at worst] — measured as an unknown over four months; its RSD represents 'the laboratory reproducibility or intermediate precision conditions'" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Fragments ~1 cm mounted in epoxy resin, polished, cleaned with ultrapure water" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 2 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection> ;
                            schema1:name "Data processing" ;
                            schema1:position 1 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/numberOfReplicates>,
                <https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRate>,
                <https://ada.astromat.org/metadata/parameter/module/ICPMS/signalIntegrationTime>,
                <https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSize>,
                <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
            schema1:description "Two measurement standards complement each other: North Chile for matrix similarity and NIST SRM 612 for its well-known composition; Fe + Ni + Co = 100% normalisation removes the need for an internal standard" ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Isotope Geology Laboratory, University of Campinas (UNICAMP), Brazil" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "North Chile — 'also measured as an unknown sample several times, on different days, over four months', for intermediate precision; eight other known iron meteorites validate against published INAA values" ;
                            ada:reagentRole "referenceMaterial" ] ],
                [ schema1:instrument <https://example.org/laSficpmsTAPP-detail-Navarro2024/instrument/ICPMS>,
                        <https://example.org/laSficpmsTAPP-detail-Navarro2024/instrument/Laser-Ablation-System> ],
                [ bios:computationalTool [ a schema1:SoftwareApplication ;
                            schema1:name "iolite 4.5.7 with 3D Trace Elements DRS" ;
                            ada:toolRole "dataReduction" ] ] ;
            ada:ablationSpotDuration "40 s — '20 s of blank measurement (laser-firing with the shutter closed), followed by 40 s of sample ablation'" ;
            ada:combinedResults [ ] ;
            ada:proceduralBlankLevel "no value available: ada:proceduralBlankLevel" ;
            ada:rasterLineSpacing "N/A — spot mode" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:detectionLimit "As: 2; Au: 0.1; Co: 2; Cr: 19; Cu: 0.8; Fe: 60; Ga: 0.3; Ge: 3; Ir: 0.2; Ni: 36; Os: 0.2; Pd: 0.5; Pt: 0.3; Re: 0.1; Rh: 0.1; Ru: 1; W: 1 — µg/g, median values (Table 3 'LOD')" ;
    ada:fundingSourceForAnalysis "M.S.N.: Educorp (Unicamp) and International Association of Geoanalysts for Geoanalysis 2022 presentation; J.E.: CNPq grant 316191/2021-3" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:mappingArea "missing" ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Sample name only — iron meteorites by name (Table 1, p.2), each analysed as \"fragments about 1 cm\" (p.3); spots and mapped areas are counted (\"points 176\", p.12), not labelled" ;
    ada:sessionIdentifier "missing" ;
    ada:spotDiameter -9999 ;
    ada:spotDiameterMeasured -9999 ;
    ada:transectLength -9999 .

<https://example.org/laSficpmsTAPP-detail-Navarro2024/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSetting> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS" ;
    schema1:hasPart <https://example.org/laSficpmsTAPP-detail-Navarro2024/instrument/ICPMS/part/ICP-Source> ;
    schema1:name "no value available: schema:name" .

<https://example.org/laSficpmsTAPP-detail-Navarro2024/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRate>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<https://example.org/laSficpmsTAPP-detail-Navarro2024/instrument/Laser-Ablation-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Laser Ablation System" ;
    schema1:name "no value available: schema:name" ;
    ada:laserFluence "7 J cm⁻²" ;
    ada:laserRepetitionRate "all: 10 Hz" ;
    ada:laserSpotGeometry "all: 150 µm — Table 2 'spot diameter'" .

<https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/numberOfReplicates> a schema1:PropertyValue ;
    schema1:description "20 spots in Arraias; n per meteorite in Table 3 — 'the mean value of 20 spot measurements in the Arraias meteorite'" ;
    schema1:name "Number of Replicates" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/numberOfReplicates> ;
    schema1:value 20 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRate> a schema1:PropertyValue ;
    schema1:description "0.9 L/min — Table 2" ;
    schema1:name "Auxiliary Gas Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 9e-01 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate> a schema1:PropertyValue ;
    schema1:description "16 L/min — Table 2 'plasma gas flow rate'" ;
    schema1:name "Coolant Plasma Gas Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 16 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning> a schema1:PropertyValue ;
    schema1:name "ICP Tuning" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning> ;
    schema1:value "ICP-MS and laser settings optimised daily 'to achieve the compromise between optimum signal intensity and low oxide formation, as specified by the factory'; mass calibration and detector cross-calibration 'systematically checked and redone if required' — Experimental section" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRate> a schema1:PropertyValue ;
    schema1:description "Ar makeup gas, combined via a T-piece near the torch; Table 2 lists a nebulizer gas flow rate of 1.1 L/min — Table 2" ;
    schema1:name "Make-up Gas and Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 2 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSetting> a schema1:PropertyValue ;
    schema1:name "Mass Resolution Setting" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSetting> ;
    schema1:value "Low resolution (M/ΔM = 300)" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> a schema1:PropertyValue ;
    schema1:description "1200 W" ;
    schema1:name "RF Power" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1200 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/signalIntegrationTime> a schema1:PropertyValue ;
    schema1:description "40 s (full ablation interval used; background subtracted separately)" ;
    schema1:name "Signal Integration Time" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/signalIntegrationTime> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 40 .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSize> a schema1:PropertyValue ;
    schema1:name "Transect Rate Mapping Rate or Step Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSize> ;
    schema1:value "N/A — spot mode" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "N — the preparation is stated without an imaging step: \"Before analyses, fragments about 1 cm were mounted in epoxy resin, polished, and cleaned with ultrapure water\" (p.3). The meteorites' structural classes were known beforehand (Table 1, p.2) but no screening of this material is described" .

<https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection> a schema1:PropertyValue ;
    schema1:name "Pulse Analog Detector Nonlinearity Correction" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection> ;
    schema1:value "N — 'detector cross-calibration were systematically checked and redone if required'; Fe and Ni measured on low-abundance isotopes in analog mode" .


```


### detail example Navarro2024-2
detail instance derived from Navarro et al. 2024 (ACS ESC 8) Iron meteorites Raster mapping (2D) ns-LA-SF-ICP-MS University of Campinas.
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
  "@id": "ex:laSficpmsTAPP-detail-Navarro2024-2",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
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
          "schema:value": "Chemical etching to reveal the phases before mapping — \"For the mapping experiment, the polished surface of the Augusto Pestana sample was etched with freshly prepared Nital solution (2% v/v HNO3 ... in 99.5% absolute ethanol) to reveal the presence of different phases (in this case, kamacite and plessite)\" (p.3). Not imaging, but the screening step that sites the map"
        },
        {
          "@id": "ada:parameter/module/LaserAblation/transectRateMappingRateOrStepSize",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/LaserAblation/transectRateMappingRateOrStepSize"
            }
          ],
          "schema:name": "Transect Rate Mapping Rate or Step Size",
          "schema:value": "all: 10 µm/s — 'scanning at a speed of 10 μm s−1'"
        },
        {
          "@id": "ada:parameter/module/ICPMS/makeUpGasAndFlowRate",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/ICPMS/makeUpGasAndFlowRate"
            }
          ],
          "schema:name": "Make-up Gas and Flow Rate",
          "schema:value": 2,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "Ar makeup gas, combined via a T-piece near the torch; Table 2 lists a nebulizer gas flow rate of 1.1 L/min — Table 2"
        },
        {
          "@id": "ada:parameter/module/LaserAblation/mappingArea",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/LaserAblation/mappingArea"
            }
          ],
          "schema:name": "Mapping Area",
          "schema:value": "Augusto Pestana: 30 min mapping session (area not explicitly stated; 150 µm spot at 10 µm s⁻¹)"
        },
        {
          "@id": "ada:parameter/module/ICPMS/signalIntegrationTime",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/ICPMS/signalIntegrationTime"
            }
          ],
          "schema:name": "Signal Integration Time",
          "schema:value": "N/A — mapping",
          "schema:unitText": "no value available: unnamed property"
        }
      ],
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "ICPMS",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/module/ICPMS/massResolutionSetting",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/module/ICPMS/massResolutionSetting"
                    }
                  ],
                  "schema:name": "Mass Resolution Setting",
                  "schema:value": "Low resolution (M/ΔM = 300)"
                },
                {
                  "@id": "ada:parameter/module/ICPMS/icpTuning",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/module/ICPMS/icpTuning"
                    }
                  ],
                  "schema:name": "ICP Tuning",
                  "schema:value": "ICP-MS and laser settings optimised daily 'to achieve the compromise between optimum signal intensity and low oxide formation, as specified by the factory'; mass calibration and detector cross-calibration 'systematically checked and redone if required' — Experimental section"
                }
              ],
              "schema:hasPart": [
                {
                  "schema:additionalType": [
                    "ICP Source",
                    {
                      "@id": "https://www.wikidata.org/wiki/Q3099911"
                    }
                  ],
                  "schema:additionalProperty": [
                    {
                      "@id": "ada:parameter/module/ICPMS/coolantPlasmaGasFlowRate",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/ICPMS/coolantPlasmaGasFlowRate"
                        }
                      ],
                      "schema:name": "Coolant Plasma Gas Flow Rate",
                      "schema:value": 16,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "16 L/min — Table 2 'plasma gas flow rate'"
                    },
                    {
                      "@id": "ada:parameter/module/ICPMS/auxiliaryGasFlowRate",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/ICPMS/auxiliaryGasFlowRate"
                        }
                      ],
                      "schema:name": "Auxiliary Gas Flow Rate",
                      "schema:value": 0.9,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "0.9 L/min — Table 2"
                    },
                    {
                      "@id": "ada:parameter/module/ICPMS/rfPower",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/ICPMS/rfPower"
                        }
                      ],
                      "schema:name": "RF Power",
                      "schema:value": 1200,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "1200 W"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:laSficpmsTAPP-detail-Navarro2024-2/instrument/ICPMS/part/ICP-Source"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:laSficpmsTAPP-detail-Navarro2024-2/instrument/ICPMS"
            },
            {
              "schema:additionalType": [
                "Laser Ablation System",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "ada:laserSpotGeometry": "all: 150 µm² square spot — as written: 'targeting a 150 μm2 square spot'",
              "ada:laserFluence": "7 J cm⁻²",
              "ada:laserRepetitionRate": "all: 10 Hz",
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:laSficpmsTAPP-detail-Navarro2024-2/instrument/Laser-Ablation-System"
            }
          ]
        },
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "iolite 4.5.7 with 3D Trace Elements DRS",
              "@type": [
                "schema:SoftwareApplication"
              ]
            }
          ]
        },
        {
          "bios:reagent": [
            {
              "ada:reagentRole": "referenceMaterial",
              "schema:name": "North Chile — 'also measured as an unknown sample several times, on different days, over four months', for intermediate precision; eight other known iron meteorites validate against published INAA values",
              "@type": [
                "schema:DefinedTerm"
              ]
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
                "@id": "ada:parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection"
                  }
                ],
                "schema:name": "Pulse Analog Detector Nonlinearity Correction",
                "schema:value": "N — 'detector cross-calibration were systematically checked and redone if required'; Fe and Ni measured on low-abundance isotopes in analog mode"
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
            "schema:description": "Same Augusto Pestana fragment etched with Nital solution (2% v/v HNO₃ in ethanol) to reveal kamacite and plessite",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          }
        ]
      },
      "ada:combinedResults": [
        {}
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Isotope Geology Laboratory, University of Campinas (UNICAMP), Brazil"
      },
      "schema:description": "Mapping over regions with diverse phases of Augusto Pestana; Fe + Ni + Co = 100% normalisation 'is mandatory when acquiring elemental maps of multiphasic samples'",
      "ada:ablationSpotDuration": "N/A — mapping mode",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:proceduralBlankLevel": "no value available: ada:proceduralBlankLevel"
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "M.S.N.: Educorp (Unicamp) and International Association of Geoanalysts; J.E.: CNPq grant 316191/2021-3"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "M.S.N.: Educorp (Unicamp) and International Association of Geoanalysts; J.E.: CNPq grant 316191/2021-3",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only — iron meteorites by name (Table 1, p.2), each analysed as \"fragments about 1 cm\" (p.3); spots and mapped areas are counted (\"points 176\", p.12), not labelled",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "missing",
  "ada:spotDiameterMeasured": -9999
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-SF-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:laSficpmsTAPP-detail-Navarro2024-2",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
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
          "schema:value": "Chemical etching to reveal the phases before mapping \u2014 \"For the mapping experiment, the polished surface of the Augusto Pestana sample was etched with freshly prepared Nital solution (2% v/v HNO3 ... in 99.5% absolute ethanol) to reveal the presence of different phases (in this case, kamacite and plessite)\" (p.3). Not imaging, but the screening step that sites the map"
        },
        {
          "@id": "ada:parameter/module/LaserAblation/transectRateMappingRateOrStepSize",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/LaserAblation/transectRateMappingRateOrStepSize"
            }
          ],
          "schema:name": "Transect Rate Mapping Rate or Step Size",
          "schema:value": "all: 10 \u00b5m/s \u2014 'scanning at a speed of 10 \u03bcm s\u22121'"
        },
        {
          "@id": "ada:parameter/module/ICPMS/makeUpGasAndFlowRate",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/ICPMS/makeUpGasAndFlowRate"
            }
          ],
          "schema:name": "Make-up Gas and Flow Rate",
          "schema:value": 2,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "Ar makeup gas, combined via a T-piece near the torch; Table 2 lists a nebulizer gas flow rate of 1.1 L/min \u2014 Table 2"
        },
        {
          "@id": "ada:parameter/module/LaserAblation/mappingArea",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/LaserAblation/mappingArea"
            }
          ],
          "schema:name": "Mapping Area",
          "schema:value": "Augusto Pestana: 30 min mapping session (area not explicitly stated; 150 \u00b5m spot at 10 \u00b5m s\u207b\u00b9)"
        },
        {
          "@id": "ada:parameter/module/ICPMS/signalIntegrationTime",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/module/ICPMS/signalIntegrationTime"
            }
          ],
          "schema:name": "Signal Integration Time",
          "schema:value": "N/A \u2014 mapping",
          "schema:unitText": "no value available: unnamed property"
        }
      ],
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "ICPMS",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/module/ICPMS/massResolutionSetting",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/module/ICPMS/massResolutionSetting"
                    }
                  ],
                  "schema:name": "Mass Resolution Setting",
                  "schema:value": "Low resolution (M/\u0394M = 300)"
                },
                {
                  "@id": "ada:parameter/module/ICPMS/icpTuning",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/module/ICPMS/icpTuning"
                    }
                  ],
                  "schema:name": "ICP Tuning",
                  "schema:value": "ICP-MS and laser settings optimised daily 'to achieve the compromise between optimum signal intensity and low oxide formation, as specified by the factory'; mass calibration and detector cross-calibration 'systematically checked and redone if required' \u2014 Experimental section"
                }
              ],
              "schema:hasPart": [
                {
                  "schema:additionalType": [
                    "ICP Source",
                    {
                      "@id": "https://www.wikidata.org/wiki/Q3099911"
                    }
                  ],
                  "schema:additionalProperty": [
                    {
                      "@id": "ada:parameter/module/ICPMS/coolantPlasmaGasFlowRate",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/ICPMS/coolantPlasmaGasFlowRate"
                        }
                      ],
                      "schema:name": "Coolant Plasma Gas Flow Rate",
                      "schema:value": 16,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "16 L/min \u2014 Table 2 'plasma gas flow rate'"
                    },
                    {
                      "@id": "ada:parameter/module/ICPMS/auxiliaryGasFlowRate",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/ICPMS/auxiliaryGasFlowRate"
                        }
                      ],
                      "schema:name": "Auxiliary Gas Flow Rate",
                      "schema:value": 0.9,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "0.9 L/min \u2014 Table 2"
                    },
                    {
                      "@id": "ada:parameter/module/ICPMS/rfPower",
                      "@type": [
                        "schema:PropertyValue"
                      ],
                      "schema:propertyID": [
                        {
                          "@id": "ada:parameter/module/ICPMS/rfPower"
                        }
                      ],
                      "schema:name": "RF Power",
                      "schema:value": 1200,
                      "schema:unitText": "no value available: unnamed property",
                      "schema:description": "1200 W"
                    }
                  ],
                  "@type": [
                    "schema:Product",
                    "schema:Thing"
                  ],
                  "schema:name": "missing",
                  "@id": "ex:laSficpmsTAPP-detail-Navarro2024-2/instrument/ICPMS/part/ICP-Source"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:laSficpmsTAPP-detail-Navarro2024-2/instrument/ICPMS"
            },
            {
              "schema:additionalType": [
                "Laser Ablation System",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "ada:laserSpotGeometry": "all: 150 \u00b5m\u00b2 square spot \u2014 as written: 'targeting a 150 \u03bcm2 square spot'",
              "ada:laserFluence": "7 J cm\u207b\u00b2",
              "ada:laserRepetitionRate": "all: 10 Hz",
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:laSficpmsTAPP-detail-Navarro2024-2/instrument/Laser-Ablation-System"
            }
          ]
        },
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "iolite 4.5.7 with 3D Trace Elements DRS",
              "@type": [
                "schema:SoftwareApplication"
              ]
            }
          ]
        },
        {
          "bios:reagent": [
            {
              "ada:reagentRole": "referenceMaterial",
              "schema:name": "North Chile \u2014 'also measured as an unknown sample several times, on different days, over four months', for intermediate precision; eight other known iron meteorites validate against published INAA values",
              "@type": [
                "schema:DefinedTerm"
              ]
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
                "@id": "ada:parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection",
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:propertyID": [
                  {
                    "@id": "ada:parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection"
                  }
                ],
                "schema:name": "Pulse Analog Detector Nonlinearity Correction",
                "schema:value": "N \u2014 'detector cross-calibration were systematically checked and redone if required'; Fe and Ni measured on low-abundance isotopes in analog mode"
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
            "schema:description": "Same Augusto Pestana fragment etched with Nital solution (2% v/v HNO\u2083 in ethanol) to reveal kamacite and plessite",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 2
          }
        ]
      },
      "ada:combinedResults": [
        {}
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Isotope Geology Laboratory, University of Campinas (UNICAMP), Brazil"
      },
      "schema:description": "Mapping over regions with diverse phases of Augusto Pestana; Fe + Ni + Co = 100% normalisation 'is mandatory when acquiring elemental maps of multiphasic samples'",
      "ada:ablationSpotDuration": "N/A \u2014 mapping mode",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier",
      "schema:startTime": "no value available: schema:startTime",
      "ada:proceduralBlankLevel": "no value available: ada:proceduralBlankLevel"
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "M.S.N.: Educorp (Unicamp) and International Association of Geoanalysts; J.E.: CNPq grant 316191/2021-3"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "M.S.N.: Educorp (Unicamp) and International Association of Geoanalysts; J.E.: CNPq grant 316191/2021-3",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only \u2014 iron meteorites by name (Table 1, p.2), each analysed as \"fragments about 1 cm\" (p.3); spots and mapped areas are counted (\"points 176\", p.12), not labelled",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "missing",
  "ada:spotDiameterMeasured": -9999
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

ex:laSficpmsTAPP-detail-Navarro2024-2 a schema1:Dataset,
        schema1:Product ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "M.S.N.: Educorp (Unicamp) and International Association of Geoanalysts; J.E.: CNPq grant 316191/2021-3" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "Same Augusto Pestana fragment etched with Nital solution (2% v/v HNO₃ in ethanol) to reveal kamacite and plessite" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 2 ],
                        [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection> ;
                            schema1:name "Data processing" ;
                            schema1:position 1 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRate>,
                <https://ada.astromat.org/metadata/parameter/module/ICPMS/signalIntegrationTime>,
                <https://ada.astromat.org/metadata/parameter/module/LaserAblation/mappingArea>,
                <https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSize>,
                <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
            schema1:description "Mapping over regions with diverse phases of Augusto Pestana; Fe + Ni + Co = 100% normalisation 'is mandatory when acquiring elemental maps of multiphasic samples'" ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "Isotope Geology Laboratory, University of Campinas (UNICAMP), Brazil" ] ;
            schema1:startTime "no value available: schema:startTime" ;
            prov:used [ bios:reagent [ a schema1:DefinedTerm ;
                            schema1:name "North Chile — 'also measured as an unknown sample several times, on different days, over four months', for intermediate precision; eight other known iron meteorites validate against published INAA values" ;
                            ada:reagentRole "referenceMaterial" ] ],
                [ bios:computationalTool [ a schema1:SoftwareApplication ;
                            schema1:name "iolite 4.5.7 with 3D Trace Elements DRS" ;
                            ada:toolRole "dataReduction" ] ],
                [ schema1:instrument <https://example.org/laSficpmsTAPP-detail-Navarro2024-2/instrument/ICPMS>,
                        <https://example.org/laSficpmsTAPP-detail-Navarro2024-2/instrument/Laser-Ablation-System> ] ;
            ada:ablationSpotDuration "N/A — mapping mode" ;
            ada:combinedResults [ ] ;
            ada:proceduralBlankLevel "no value available: ada:proceduralBlankLevel" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "missing" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:detectionLimit -9999 ;
    ada:fundingSourceForAnalysis "M.S.N.: Educorp (Unicamp) and International Association of Geoanalysts; J.E.: CNPq grant 316191/2021-3" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Sample name only — iron meteorites by name (Table 1, p.2), each analysed as \"fragments about 1 cm\" (p.3); spots and mapped areas are counted (\"points 176\", p.12), not labelled" ;
    ada:sessionIdentifier "missing" ;
    ada:spotDiameter -9999 ;
    ada:spotDiameterMeasured -9999 ;
    ada:transectLength -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<https://example.org/laSficpmsTAPP-detail-Navarro2024-2/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSetting> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS" ;
    schema1:hasPart <https://example.org/laSficpmsTAPP-detail-Navarro2024-2/instrument/ICPMS/part/ICP-Source> ;
    schema1:name "no value available: schema:name" .

<https://example.org/laSficpmsTAPP-detail-Navarro2024-2/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRate>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<https://example.org/laSficpmsTAPP-detail-Navarro2024-2/instrument/Laser-Ablation-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Laser Ablation System" ;
    schema1:name "no value available: schema:name" ;
    ada:laserFluence "7 J cm⁻²" ;
    ada:laserRepetitionRate "all: 10 Hz" ;
    ada:laserSpotGeometry "all: 150 µm² square spot — as written: 'targeting a 150 μm2 square spot'" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRate> a schema1:PropertyValue ;
    schema1:description "0.9 L/min — Table 2" ;
    schema1:name "Auxiliary Gas Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 9e-01 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate> a schema1:PropertyValue ;
    schema1:description "16 L/min — Table 2 'plasma gas flow rate'" ;
    schema1:name "Coolant Plasma Gas Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 16 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning> a schema1:PropertyValue ;
    schema1:name "ICP Tuning" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuning> ;
    schema1:value "ICP-MS and laser settings optimised daily 'to achieve the compromise between optimum signal intensity and low oxide formation, as specified by the factory'; mass calibration and detector cross-calibration 'systematically checked and redone if required' — Experimental section" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRate> a schema1:PropertyValue ;
    schema1:description "Ar makeup gas, combined via a T-piece near the torch; Table 2 lists a nebulizer gas flow rate of 1.1 L/min — Table 2" ;
    schema1:name "Make-up Gas and Flow Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 2 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSetting> a schema1:PropertyValue ;
    schema1:name "Mass Resolution Setting" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSetting> ;
    schema1:value "Low resolution (M/ΔM = 300)" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> a schema1:PropertyValue ;
    schema1:description "1200 W" ;
    schema1:name "RF Power" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPower> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1200 .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/signalIntegrationTime> a schema1:PropertyValue ;
    schema1:name "Signal Integration Time" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/ICPMS/signalIntegrationTime> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value "N/A — mapping" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/mappingArea> a schema1:PropertyValue ;
    schema1:name "Mapping Area" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/LaserAblation/mappingArea> ;
    schema1:value "Augusto Pestana: 30 min mapping session (area not explicitly stated; 150 µm spot at 10 µm s⁻¹)" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSize> a schema1:PropertyValue ;
    schema1:name "Transect Rate Mapping Rate or Step Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSize> ;
    schema1:value "all: 10 µm/s — 'scanning at a speed of 10 μm s−1'" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreening> ;
    schema1:value "Chemical etching to reveal the phases before mapping — \"For the mapping experiment, the polished surface of the Augusto Pestana sample was etched with freshly prepared Nital solution (2% v/v HNO3 ... in 99.5% absolute ethanol) to reveal the presence of different phases (in this case, kamacite and plessite)\" (p.3). Not imaging, but the screening step that sites the map" .

<https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection> a schema1:PropertyValue ;
    schema1:name "Pulse Analog Detector Nonlinearity Correction" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrection> ;
    schema1:value "N — 'detector cross-calibration were systematically checked and redone if required'; Fe and Ni measured on low-abundance isotopes in analog mode" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: LA-SF-ICP-MS Analysis Detail
description: Dataset-level analysis-instance detail for LA-SF-ICP-MS, reusing CDIF/schema.org
  slots on the schema:Dataset root.
allOf:
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/AnalysisIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/AnalysisIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/calibrationFactor/schema.yaml#/$defs/AnalysisIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/aggregation/schema.yaml#/$defs/AnalysisIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/AnalysisIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/compositionQC/schema.yaml#/$defs/AnalysisIdentification
- type: object
  properties:
    prov:wasGeneratedBy:
      type: array
      items:
        type: object
        properties:
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
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_fusionFluxAndDilutionRatio
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_preAblationSurfaceTreatment
                          allOf:
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_fusionFluxAndDilutionRatio
                            minContains: 0
                            maxContains: 1
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_preAblationSurfaceTreatment
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
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_signalSmoothing
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_filteringApproach
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/singleCollector/schema.yaml#/$defs/Param_Analysis_pulseAnalogDetectorNonlinearityCorrection
                          allOf:
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_signalSmoothing
                            minContains: 0
                            maxContains: 1
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_filteringApproach
                            minContains: 0
                            maxContains: 1
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/singleCollector/schema.yaml#/$defs/Param_Analysis_pulseAnalogDetectorNonlinearityCorrection
                            minContains: 0
                            maxContains: 1
          schema:additionalProperty:
            type: array
            items:
              anyOf:
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Analysis_samplingUnitSelectionCriteria
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Analysis_preAnalysisImagingAndScreening
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_transectRateMappingRateOrStepSize
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_carrierGasAndFlowRate
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_makeUpGasAndFlowRate
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_analysisSequence
              - title: Ion Counter Dead Time
                description: Dead time of the ion-counting detector(s), used in the
                  dead-time correction applied to high count rates. Distinct from
                  pulse/analog cross-calibration, which relates the two detector modes
                  rather than correcting counting losses within the pulse-counting
                  mode.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laSficpmsTAPP/ionCounterDeadTime
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laSficpmsTAPP/ionCounterDeadTime
                  schema:name:
                    const: Ion Counter Dead Time
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
              - title: Total Integration Time per Output Data Point
                description: "Total duty-cycle time for one complete mass-scan sweep
                  \u2014 the sum of all per-isotope dwell times plus inter-mass settling
                  times. Not recoverable from Dwell Time per Mass alone, because settling
                  time is not captured there. Applies to sequential (quadrupole and
                  single-collector sector-field) acquisition."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laSficpmsTAPP/totalIntegrationTimePerOutputDataPoint
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laSficpmsTAPP/totalIntegrationTimePerOutputDataPoint
                  schema:name:
                    const: Total Integration Time per Output Data Point
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
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_backgroundCountTime
              - title: Number of Replicates
                description: Number of replicate measurements performed on the same
                  sample, or on the same nominal location where the technique is spatially
                  resolved. For spot analysis this is the number of individual spots
                  per grain or location; for transects, the number of replicate lines;
                  for mapping, the number of map acquisitions of the same area; for
                  solution work, the number of discrete replicate measurements acquired
                  per sample solution.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laSficpmsTAPP/numberOfReplicates
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laSficpmsTAPP/numberOfReplicates
                  schema:name:
                    const: Number of Replicates
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
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_transectLength
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_mappingArea
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_signalIntegrationTime
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Analysis_constantsReferenceValues
            allOf:
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Analysis_samplingUnitSelectionCriteria
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Analysis_preAnalysisImagingAndScreening
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_transectRateMappingRateOrStepSize
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_carrierGasAndFlowRate
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_makeUpGasAndFlowRate
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_analysisSequence
              minContains: 0
              maxContains: 1
            - contains:
                title: Ion Counter Dead Time
                description: Dead time of the ion-counting detector(s), used in the
                  dead-time correction applied to high count rates. Distinct from
                  pulse/analog cross-calibration, which relates the two detector modes
                  rather than correcting counting losses within the pulse-counting
                  mode.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laSficpmsTAPP/ionCounterDeadTime
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laSficpmsTAPP/ionCounterDeadTime
                  schema:name:
                    const: Ion Counter Dead Time
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
                title: Total Integration Time per Output Data Point
                description: "Total duty-cycle time for one complete mass-scan sweep
                  \u2014 the sum of all per-isotope dwell times plus inter-mass settling
                  times. Not recoverable from Dwell Time per Mass alone, because settling
                  time is not captured there. Applies to sequential (quadrupole and
                  single-collector sector-field) acquisition."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laSficpmsTAPP/totalIntegrationTimePerOutputDataPoint
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laSficpmsTAPP/totalIntegrationTimePerOutputDataPoint
                  schema:name:
                    const: Total Integration Time per Output Data Point
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
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_backgroundCountTime
              minContains: 0
              maxContains: 1
            - contains:
                title: Number of Replicates
                description: Number of replicate measurements performed on the same
                  sample, or on the same nominal location where the technique is spatially
                  resolved. For spot analysis this is the number of individual spots
                  per grain or location; for transects, the number of replicate lines;
                  for mapping, the number of map acquisitions of the same area; for
                  solution work, the number of discrete replicate measurements acquired
                  per sample solution.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laSficpmsTAPP/numberOfReplicates
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laSficpmsTAPP/numberOfReplicates
                  schema:name:
                    const: Number of Replicates
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
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_transectLength
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_mappingArea
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_signalIntegrationTime
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Analysis_constantsReferenceValues
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
                                    const: ICPMS
                                  schema:inDefinedTermSet: ada:vocab/instrumentType
                              required:
                              - schema:additionalType
                            then:
                              properties:
                                schema:hasPart:
                                  type: array
                                  items:
                                    type: object
                                    allOf:
                                    - if:
                                        properties:
                                          schema:additionalType:
                                            contains:
                                              const: Torch
                                            schema:inDefinedTermSet: ada:vocab/instrumentComponentType
                                        required:
                                        - schema:additionalType
                                      then:
                                        properties:
                                          schema:additionalProperty:
                                            type: array
                                            items:
                                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_torchDepth
                                            allOf:
                                            - contains:
                                                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_torchDepth
                                              minContains: 0
                                              maxContains: 1
                                    - if:
                                        properties:
                                          schema:additionalType:
                                            contains:
                                              const: ICP Source
                                            schema:inDefinedTermSet: ada:vocab/instrumentComponentType
                                        required:
                                        - schema:additionalType
                                      then:
                                        properties:
                                          schema:additionalProperty:
                                            type: array
                                            items:
                                              anyOf:
                                              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_coolantPlasmaGasFlowRate
                                              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_auxiliaryGasFlowRate
                                              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_rfPower
                                            allOf:
                                            - contains:
                                                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_coolantPlasmaGasFlowRate
                                              minContains: 0
                                              maxContains: 1
                                            - contains:
                                                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_auxiliaryGasFlowRate
                                              minContains: 0
                                              maxContains: 1
                                            - contains:
                                                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_rfPower
                                              minContains: 0
                                              maxContains: 1
                                  allOf:
                                  - contains:
                                      properties:
                                        schema:additionalType:
                                          contains:
                                            const: ICP Source
                                          schema:inDefinedTermSet: ada:vocab/instrumentComponentType
                                      required:
                                      - schema:additionalType
                                schema:additionalProperty:
                                  type: array
                                  items:
                                    anyOf:
                                    - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_massResolutionSetting
                                    - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_icpTuning
                                    - title: Doubly-Charged Species Monitor
                                      description: "The mass ratio monitored to estimate
                                        doubly-charged ion (M\xB2\u207A) formation
                                        during instrument tuning. The monitor species
                                        and the mass positions monitored should be
                                        stated explicitly. Analogous to Oxide Production
                                        Method and Threshold for oxide monitoring."
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/laSficpmsTAPP/doublyChargedSpeciesMonitor
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/laSficpmsTAPP/doublyChargedSpeciesMonitor
                                        schema:name:
                                          const: Doubly-Charged Species Monitor
                                        schema:value:
                                          type: string
                                      required:
                                      - '@id'
                                      - '@type'
                                      - schema:propertyID
                                      - schema:name
                                      - schema:value
                                    - title: Doubly-Charged Species Production
                                      description: Measured percentage of doubly-charged
                                        ion production for the monitored species at
                                        the time of instrument tuning. The acceptable
                                        threshold is typically <1% or <3%. Record
                                        both the threshold and the measured value.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/laSficpmsTAPP/doublyChargedSpeciesProduction
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/laSficpmsTAPP/doublyChargedSpeciesProduction
                                        schema:name:
                                          const: Doubly-Charged Species Production
                                        schema:value:
                                          type: string
                                      required:
                                      - '@id'
                                      - '@type'
                                      - schema:propertyID
                                      - schema:name
                                      - schema:value
                                    - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_memoryEffectMitigation
                                  allOf:
                                  - contains:
                                      $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_massResolutionSetting
                                    minContains: 0
                                    maxContains: 1
                                  - contains:
                                      $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_icpTuning
                                    minContains: 0
                                    maxContains: 1
                                  - contains:
                                      title: Doubly-Charged Species Monitor
                                      description: "The mass ratio monitored to estimate
                                        doubly-charged ion (M\xB2\u207A) formation
                                        during instrument tuning. The monitor species
                                        and the mass positions monitored should be
                                        stated explicitly. Analogous to Oxide Production
                                        Method and Threshold for oxide monitoring."
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/laSficpmsTAPP/doublyChargedSpeciesMonitor
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/laSficpmsTAPP/doublyChargedSpeciesMonitor
                                        schema:name:
                                          const: Doubly-Charged Species Monitor
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
                                      title: Doubly-Charged Species Production
                                      description: Measured percentage of doubly-charged
                                        ion production for the monitored species at
                                        the time of instrument tuning. The acceptable
                                        threshold is typically <1% or <3%. Record
                                        both the threshold and the measured value.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/laSficpmsTAPP/doublyChargedSpeciesProduction
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/laSficpmsTAPP/doublyChargedSpeciesProduction
                                        schema:name:
                                          const: Doubly-Charged Species Production
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
                                      $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_memoryEffectMitigation
                                    minContains: 0
                                    maxContains: 1
                          - if:
                              properties:
                                schema:additionalType:
                                  contains:
                                    const: Laser Ablation System
                                  schema:inDefinedTermSet: ada:vocab/instrumentType
                              required:
                              - schema:additionalType
                            then:
                              properties:
                                schema:additionalProperty:
                                  type: array
                                  items:
                                    $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_laserEnergy
                                  allOf:
                                  - contains:
                                      $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_laserEnergy
                                    minContains: 0
                                    maxContains: 1
                      allOf:
                      - contains:
                          properties:
                            schema:additionalType:
                              contains:
                                const: ICPMS
                              schema:inDefinedTermSet: ada:vocab/instrumentType
                          required:
                          - schema:additionalType
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
                        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_mappedAreaDescription
                      allOf:
                      - contains:
                          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_mappedAreaDescription
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
                const: Within-Session Analytical Precision
            required:
            - dqv:isMeasurementOf
          then:
            properties:
              dqv:value:
                description: Precision of repeated measurements within a single analytical
                  session and the method used to assess it. Report both the assessment
                  method and the precision values. The assessment method must specify
                  the reference material or standard measured, the number of replicates
                  n, and the statistic reported (1s RSD, 2s RSD, 2SD, 2SE, 95% CI).
                  Distinct from the internal precision of a single measurement, which
                  derives from counting statistics over the cycles of that measurement
                  rather than from repeated analyses.
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
                const: Between-Session Analytical Precision
            required:
            - dqv:isMeasurementOf
          then:
            properties:
              dqv:value:
                description: "Precision of measurements across multiple analytical
                  sessions over weeks to months \u2014 long-term or intermediate precision
                  \u2014 and the method used to assess it. Report both the assessment
                  method and the precision values, specifying the reference material,
                  the number of measurements and sessions, the time span covered,
                  and the statistic reported."
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
                description: Offset between measured and accepted values for secondary
                  reference materials, and the method used to assess it. Specify the
                  reference material and the source of its accepted values, the number
                  of analyses, and the quantities assessed. Report systematic biases
                  and their likely causes. Express the offset in the form appropriate
                  to what the procedure reports - percent relative bias for concentrations,
                  or deviation in delta or ratio units for isotopic quantities.
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
              const: Within-Session Analytical Precision
          required:
          - dqv:isMeasurementOf
      - contains:
          properties:
            dqv:isMeasurementOf:
              const: Between-Session Analytical Precision
          required:
          - dqv:isMeasurementOf
      - contains:
          properties:
            dqv:isMeasurementOf:
              const: Analytical Accuracy
          required:
          - dqv:isMeasurementOf
      title: Quality Measurements
x-bblocks-metadata:
  itemIdentifier: ogch.techniqueProfile.geochemProfile.LA-SF-ICPMS.detail
  register: https://amds-ldeo.github.io/geochemBuildingBlocks/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-11-09'

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-SF-ICPMS/detail/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-SF-ICPMS/detail/schema.yaml)


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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-SF-ICPMS/detail/context.jsonld)

## Sources

* [LA-SF-ICP-MS_TAPP_v16.csv (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/LA-SF-ICPMS/detail`

