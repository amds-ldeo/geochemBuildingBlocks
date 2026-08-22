
# Lab-XCT Analysis Detail (Schema)

`ogch.techniqueProfile.geochemProfile.XCT.detail` *v0.1*

Laboratory X-ray computed tomography analysis-specific detail properties. Discriminates on ada:componentType (XCTVolume, XCTProjectionImageSet, XCTSegmentationVolume, XCTRenderedImage, XCTQuantitativeTabular), carries analysis-level required properties (analyst, dates, sample, VOI) and per-dataset schema:additionalProperty values referencing the labxctTAPP parameterValues registry.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### detail example Eckley2024
detail instance derived from Eckley 2024 (JSC Scan Record) Bennu particle Single-volume Nikon XTH 320 NASA JSC X-FaCT.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Eckley2024",
  "@type": [
    "ada:XCTVolume"
  ],
  "ada:componentType": "ada:XCTVolume",
  "schema:measurementTechnique": [
    {
      "@id": "ex:labxctTAPP-Eckley2024"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "Scott Eckley",
  "ada:analysisStartDate": "2024-10-29",
  "ada:analysisEndDate": "missing",
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "missing"
    }
  ],
  "ada:sampleDimensions": "missing",
  "ada:sampleName": "OREX-800099-0",
  "ada:samplingUnit": "missing",
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
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Eckley2024",
  "@type": [
    "ada:XCTVolume"
  ],
  "ada:componentType": "ada:XCTVolume",
  "schema:measurementTechnique": [
    {
      "@id": "ex:labxctTAPP-Eckley2024"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "Scott Eckley",
  "ada:analysisStartDate": "2024-10-29",
  "ada:analysisEndDate": "missing",
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "missing"
    }
  ],
  "ada:sampleDimensions": "missing",
  "ada:sampleName": "OREX-800099-0",
  "ada:samplingUnit": "missing",
  "ada:voiApplied": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .

ex:detail-Eckley2024 a ada:XCTVolume ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:labxctTAPP-Eckley2024 ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "2024-10-29" ;
    ada:analyst "Scott Eckley" ;
    ada:componentType "ada:XCTVolume" ;
    ada:sampleDimensions "missing" ;
    ada:sampleName "OREX-800099-0" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voiApplied "missing" .


```


### detail example Genge2025
detail instance derived from Genge et al. 2025 (Nat. Commun.) Ryugu particle (A0180) Single-volume Zeiss Versa Not stated.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Genge2025",
  "@type": [
    "ada:XCTVolume"
  ],
  "ada:componentType": "ada:XCTVolume",
  "schema:measurementTechnique": [
    {
      "@id": "ex:labxctTAPP-Genge2025"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "missing"
    }
  ],
  "ada:sampleDimensions": "1.592 × 0.756 × 0.985 mm",
  "ada:sampleName": "A0180 (A0180-A and A0180-B)",
  "ada:samplingUnit": "missing",
  "ada:voiApplied": "Full scan volume",
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
    }
  ]
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
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Genge2025",
  "@type": [
    "ada:XCTVolume"
  ],
  "ada:componentType": "ada:XCTVolume",
  "schema:measurementTechnique": [
    {
      "@id": "ex:labxctTAPP-Genge2025"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "missing"
    }
  ],
  "ada:sampleDimensions": "1.592 \u00d7 0.756 \u00d7 0.985 mm",
  "ada:sampleName": "A0180 (A0180-A and A0180-B)",
  "ada:samplingUnit": "missing",
  "ada:voiApplied": "Full scan volume",
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
    }
  ]
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .

ex:detail-Genge2025 a ada:XCTVolume ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:labxctTAPP-Genge2025 ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:componentType "ada:XCTVolume" ;
    ada:sampleDimensions "1.592 × 0.756 × 0.985 mm" ;
    ada:sampleName "A0180 (A0180-A and A0180-B)" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voiApplied "Full scan volume" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> a schema1:PropertyValue ;
    schema1:name "Effective Spatial Resolution (PSF/MTF)" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> ;
    schema1:value "N — the paper's \"spatial resolutions (in voxels)\" are the voxel sizes (0.625 / 0.672 µm); no effective (PSF/MTF) resolution reported" .


```


### detail example Neuman2025
detail instance derived from Neuman et al. 2025 / Shearer et al. 2024 (JGR / Space Sci. Rev.) Apollo 17 core 73002 Multi-volume stitching NSI custom, UTCT.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Neuman2025",
  "@type": [
    "ada:XCTVolume"
  ],
  "ada:componentType": "ada:XCTVolume",
  "schema:measurementTechnique": [
    {
      "@id": "ex:labxctTAPP-Neuman2025"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "missing"
    }
  ],
  "ada:sampleDimensions": "~35 cm length core",
  "ada:sampleName": "Apollo 17 core 73002",
  "ada:samplingUnit": "missing",
  "ada:numberOfSubVolumes": 6,
  "ada:voiApplied": "Full core length per sub-volume",
  "ada:subVolumeOverlap": "~380 slices per sub-volume overlap"
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
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Neuman2025",
  "@type": [
    "ada:XCTVolume"
  ],
  "ada:componentType": "ada:XCTVolume",
  "schema:measurementTechnique": [
    {
      "@id": "ex:labxctTAPP-Neuman2025"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "missing"
    }
  ],
  "ada:sampleDimensions": "~35 cm length core",
  "ada:sampleName": "Apollo 17 core 73002",
  "ada:samplingUnit": "missing",
  "ada:numberOfSubVolumes": 6,
  "ada:voiApplied": "Full core length per sub-volume",
  "ada:subVolumeOverlap": "~380 slices per sub-volume overlap"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Neuman2025 a ada:XCTVolume ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:labxctTAPP-Neuman2025 ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:componentType "ada:XCTVolume" ;
    ada:numberOfSubVolumes 6 ;
    ada:sampleDimensions "~35 cm length core" ;
    ada:sampleName "Apollo 17 core 73002" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:subVolumeOverlap "~380 slices per sub-volume overlap" ;
    ada:voiApplied "Full core length per sub-volume" .


```


### detail example Neuman2025-2
detail instance derived from Neuman et al. 2025 (JGR Planets) Apollo 17 core 73001 Multi-volume stitching NSI custom, UTCT.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Neuman2025-2",
  "@type": [
    "ada:XCTVolume"
  ],
  "ada:componentType": "ada:XCTVolume",
  "schema:measurementTechnique": [
    {
      "@id": "ex:labxctTAPP-Neuman2025-2"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "missing"
    }
  ],
  "ada:sampleDimensions": "~35 cm length core",
  "ada:sampleName": "Apollo 17 core 73001",
  "ada:samplingUnit": "missing",
  "ada:numberOfSubVolumes": 9,
  "ada:voiApplied": "Full core length per sub-volume"
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
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Neuman2025-2",
  "@type": [
    "ada:XCTVolume"
  ],
  "ada:componentType": "ada:XCTVolume",
  "schema:measurementTechnique": [
    {
      "@id": "ex:labxctTAPP-Neuman2025-2"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "missing"
    }
  ],
  "ada:sampleDimensions": "~35 cm length core",
  "ada:sampleName": "Apollo 17 core 73001",
  "ada:samplingUnit": "missing",
  "ada:numberOfSubVolumes": 9,
  "ada:voiApplied": "Full core length per sub-volume"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Neuman2025-2 a ada:XCTVolume ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:labxctTAPP-Neuman2025-2 ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:componentType "ada:XCTVolume" ;
    ada:numberOfSubVolumes 9 ;
    ada:sampleDimensions "~35 cm length core" ;
    ada:sampleName "Apollo 17 core 73001" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voiApplied "Full core length per sub-volume" .


```


### detail example Shearer2024
detail instance derived from Shearer et al. 2024 (Space Sci. Rev.) Apollo 17 73001 CSVC Single-volume Nikon XTH 320 NASA JSC.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Shearer2024",
  "@type": [
    "ada:XCTVolume"
  ],
  "ada:componentType": "ada:XCTVolume",
  "schema:measurementTechnique": [
    {
      "@id": "ex:labxctTAPP-Shearer2024"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "missing"
    }
  ],
  "ada:sampleDimensions": "missing",
  "ada:sampleName": "73001 CSVC",
  "ada:samplingUnit": "missing",
  "ada:voiApplied": "missing",
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
  ]
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
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Shearer2024",
  "@type": [
    "ada:XCTVolume"
  ],
  "ada:componentType": "ada:XCTVolume",
  "schema:measurementTechnique": [
    {
      "@id": "ex:labxctTAPP-Shearer2024"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "missing"
    }
  ],
  "ada:sampleDimensions": "missing",
  "ada:sampleName": "73001 CSVC",
  "ada:samplingUnit": "missing",
  "ada:voiApplied": "missing",
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
  ]
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .

ex:detail-Shearer2024 a ada:XCTVolume ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:labxctTAPP-Shearer2024 ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:componentType "ada:XCTVolume" ;
    ada:sampleDimensions "missing" ;
    ada:sampleName "73001 CSVC" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voiApplied "missing" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> a schema1:PropertyValue ;
    schema1:name "Effective Spatial Resolution (PSF/MTF)" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> ;
    schema1:value "N — voxel size only (38.49 µm); no effective resolution reported. The paper's \"spatial resolution of 60 µm\" is the multispectral core imager, not this XCT scan" .


```


### detail example Shearer2024-2
detail instance derived from Shearer et al. 2024 (Space Sci. Rev.) Apollo 17 particles Single-volume Nikon XTH 320 NASA JSC X-FaCT.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Shearer2024-2",
  "@type": [
    "ada:XCTVolume"
  ],
  "ada:componentType": "ada:XCTVolume",
  "schema:measurementTechnique": [
    {
      "@id": "ex:labxctTAPP-Shearer2024-2"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "missing"
    }
  ],
  "ada:sampleDimensions": "missing",
  "ada:sampleName": "Multiple particles from 73001 and 73002",
  "ada:samplingUnit": "missing",
  "ada:voiApplied": "missing",
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
  ]
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
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Shearer2024-2",
  "@type": [
    "ada:XCTVolume"
  ],
  "ada:componentType": "ada:XCTVolume",
  "schema:measurementTechnique": [
    {
      "@id": "ex:labxctTAPP-Shearer2024-2"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "missing"
    }
  ],
  "ada:sampleDimensions": "missing",
  "ada:sampleName": "Multiple particles from 73001 and 73002",
  "ada:samplingUnit": "missing",
  "ada:voiApplied": "missing",
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
  ]
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .

ex:detail-Shearer2024-2 a ada:XCTVolume ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:labxctTAPP-Shearer2024-2 ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:componentType "ada:XCTVolume" ;
    ada:sampleDimensions "missing" ;
    ada:sampleName "Multiple particles from 73001 and 73002" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voiApplied "missing" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> a schema1:PropertyValue ;
    schema1:name "Effective Spatial Resolution (PSF/MTF)" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> ;
    schema1:value "N — voxel size only (2.8–20.6 µm); no effective resolution reported. The paper's \"spatial resolution of 60 µm\" is the multispectral core imager, not this XCT scan" .


```


### detail example Tomkinson2015
detail instance derived from Tomkinson et al. 2015 (MAPS) NWA 5790 nakhlite Single-volume Nikon Metris XTH 225 U. Manchester.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Tomkinson2015",
  "@type": [
    "ada:XCTVolume"
  ],
  "ada:componentType": "ada:XCTVolume",
  "schema:measurementTechnique": [
    {
      "@id": "ex:labxctTAPP-Tomkinson2015"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "missing"
    }
  ],
  "ada:sampleDimensions": "~1.1 × 1.2 × 0.8 cm",
  "ada:sampleName": "NWA 5790",
  "ada:samplingUnit": "missing",
  "ada:voiApplied": "Entire chip volume (~250 thin-section equivalents); six interspaced 2D slices at ~1 mm spacing for modal mineralogy",
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
    }
  ]
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
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Tomkinson2015",
  "@type": [
    "ada:XCTVolume"
  ],
  "ada:componentType": "ada:XCTVolume",
  "schema:measurementTechnique": [
    {
      "@id": "ex:labxctTAPP-Tomkinson2015"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "missing"
    }
  ],
  "ada:sampleDimensions": "~1.1 \u00d7 1.2 \u00d7 0.8 cm",
  "ada:sampleName": "NWA 5790",
  "ada:samplingUnit": "missing",
  "ada:voiApplied": "Entire chip volume (~250 thin-section equivalents); six interspaced 2D slices at ~1 mm spacing for modal mineralogy",
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
    }
  ]
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .

ex:detail-Tomkinson2015 a ada:XCTVolume ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:labxctTAPP-Tomkinson2015 ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:componentType "ada:XCTVolume" ;
    ada:sampleDimensions "~1.1 × 1.2 × 0.8 cm" ;
    ada:sampleName "NWA 5790" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voiApplied "Entire chip volume (~250 thin-section equivalents); six interspaced 2D slices at ~1 mm spacing for modal mineralogy" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> a schema1:PropertyValue ;
    schema1:name "Effective Spatial Resolution (PSF/MTF)" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> ;
    schema1:value "N — the paper states \"a resolution of 10.3 x 10.3 x 10.3 µm³ per voxel\", i.e. the voxel size; no effective resolution reported" .


```


### detail example Glavin2023
detail instance derived from Glavin et al. 2023 (MAPS) Murchison CM2 Single-volume Nikon XTH 320 NASA JSC X-FaCT.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Glavin2023",
  "@type": [
    "ada:XCTVolume"
  ],
  "ada:componentType": "ada:XCTVolume",
  "schema:measurementTechnique": [
    {
      "@id": "ex:labxctTAPP-Glavin2023"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "Scott A. Eckley",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "missing"
    }
  ],
  "ada:sampleDimensions": "missing",
  "ada:sampleName": "Murchison B (USNM 5453,1)",
  "ada:samplingUnit": "missing",
  "ada:voiApplied": "Full vial volume (2000 × 2000 × 2000 voxels)",
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
    }
  ]
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
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Glavin2023",
  "@type": [
    "ada:XCTVolume"
  ],
  "ada:componentType": "ada:XCTVolume",
  "schema:measurementTechnique": [
    {
      "@id": "ex:labxctTAPP-Glavin2023"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "Scott A. Eckley",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "missing"
    }
  ],
  "ada:sampleDimensions": "missing",
  "ada:sampleName": "Murchison B (USNM 5453,1)",
  "ada:samplingUnit": "missing",
  "ada:voiApplied": "Full vial volume (2000 \u00d7 2000 \u00d7 2000 voxels)",
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
    }
  ]
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .

ex:detail-Glavin2023 a ada:XCTVolume ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:labxctTAPP-Glavin2023 ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "Scott A. Eckley" ;
    ada:componentType "ada:XCTVolume" ;
    ada:sampleDimensions "missing" ;
    ada:sampleName "Murchison B (USNM 5453,1)" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voiApplied "Full vial volume (2000 × 2000 × 2000 voxels)" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> a schema1:PropertyValue ;
    schema1:name "Effective Spatial Resolution (PSF/MTF)" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> ;
    schema1:value "~30 µm — stated as \"resolution limits of ~30 µm (around 3x the voxel size)\" against an 11.54 µm voxel. Rule-of-thumb estimate; no PSF or MTF measurement" .


```


### detail example Dias2019
detail instance derived from Nascimento-Dias et al. 2019 (Appl. Radiat. Isot.) NWA 8277 + NWA 6963 Single-volume Bruker Skyscan 1173.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Dias2019",
  "@type": [
    "ada:XCTVolume"
  ],
  "ada:componentType": "ada:XCTVolume",
  "schema:measurementTechnique": [
    {
      "@id": "ex:labxctTAPP-Dias2019"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "missing"
    }
  ],
  "ada:sampleDimensions": "~4 mm fragments",
  "ada:sampleName": "NWA 8277; NWA 6963",
  "ada:samplingUnit": "missing",
  "ada:voiApplied": "5.39 mm³ total analyzed volume (NWA 8277)",
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
    }
  ]
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
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Dias2019",
  "@type": [
    "ada:XCTVolume"
  ],
  "ada:componentType": "ada:XCTVolume",
  "schema:measurementTechnique": [
    {
      "@id": "ex:labxctTAPP-Dias2019"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "missing"
    }
  ],
  "ada:sampleDimensions": "~4 mm fragments",
  "ada:sampleName": "NWA 8277; NWA 6963",
  "ada:samplingUnit": "missing",
  "ada:voiApplied": "5.39 mm\u00b3 total analyzed volume (NWA 8277)",
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
    }
  ]
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .

ex:detail-Dias2019 a ada:XCTVolume ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:labxctTAPP-Dias2019 ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:componentType "ada:XCTVolume" ;
    ada:sampleDimensions "~4 mm fragments" ;
    ada:sampleName "NWA 8277; NWA 6963" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voiApplied "5.39 mm³ total analyzed volume (NWA 8277)" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> a schema1:PropertyValue ;
    schema1:name "Effective Spatial Resolution (PSF/MTF)" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> ;
    schema1:value "N — voxel size only (5.34 µm); the paper describes resolution only generically (\"of the order of microns\")" .


```


### detail example Richard2019
detail instance derived from Richard et al. 2019 (Chem. Geol.) Olivine (melt incl.) Single-volume Zeiss Xradia 510 Versa UNAM Mexico.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Richard2019",
  "@type": [
    "ada:XCTVolume"
  ],
  "ada:componentType": "ada:XCTVolume",
  "schema:measurementTechnique": [
    {
      "@id": "ex:labxctTAPP-Richard2019"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "missing"
    }
  ],
  "ada:sampleDimensions": "~1 mm olivine",
  "ada:sampleName": "Sample A (olivine)",
  "ada:samplingUnit": "missing",
  "ada:voiApplied": "Full scan volume",
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
    }
  ]
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
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Richard2019",
  "@type": [
    "ada:XCTVolume"
  ],
  "ada:componentType": "ada:XCTVolume",
  "schema:measurementTechnique": [
    {
      "@id": "ex:labxctTAPP-Richard2019"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "missing"
    }
  ],
  "ada:sampleDimensions": "~1 mm olivine",
  "ada:sampleName": "Sample A (olivine)",
  "ada:samplingUnit": "missing",
  "ada:voiApplied": "Full scan volume",
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
    }
  ]
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .

ex:detail-Richard2019 a ada:XCTVolume ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:labxctTAPP-Richard2019 ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:componentType "ada:XCTVolume" ;
    ada:sampleDimensions "~1 mm olivine" ;
    ada:sampleName "Sample A (olivine)" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voiApplied "Full scan volume" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> a schema1:PropertyValue ;
    schema1:name "Effective Spatial Resolution (PSF/MTF)" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> ;
    schema1:value "N — the paper's \"spatial resolution of 2.06 µm/px (8.7 µm³/vx)\" is the voxel size; no effective resolution reported" .


```


### detail example Richard2019-2
detail instance derived from Richard et al. 2019 (Chem. Geol.) Synthetic quartz (fluid incl.) Whole sample (low-res) Nikon XTH 320/225 U. Strathclyde.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Richard2019-2",
  "@type": [
    "ada:XCTVolume"
  ],
  "ada:componentType": "ada:XCTVolume",
  "schema:measurementTechnique": [
    {
      "@id": "ex:labxctTAPP-Richard2019-2"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "missing"
    }
  ],
  "ada:sampleDimensions": "3 × 5 × 2 cm",
  "ada:sampleName": "Sample B (synthetic quartz)",
  "ada:samplingUnit": "missing",
  "ada:voiApplied": "Full scan volume",
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
    }
  ]
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
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Richard2019-2",
  "@type": [
    "ada:XCTVolume"
  ],
  "ada:componentType": "ada:XCTVolume",
  "schema:measurementTechnique": [
    {
      "@id": "ex:labxctTAPP-Richard2019-2"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "missing"
    }
  ],
  "ada:sampleDimensions": "3 \u00d7 5 \u00d7 2 cm",
  "ada:sampleName": "Sample B (synthetic quartz)",
  "ada:samplingUnit": "missing",
  "ada:voiApplied": "Full scan volume",
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
    }
  ]
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .

ex:detail-Richard2019-2 a ada:XCTVolume ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:labxctTAPP-Richard2019-2 ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:componentType "ada:XCTVolume" ;
    ada:sampleDimensions "3 × 5 × 2 cm" ;
    ada:sampleName "Sample B (synthetic quartz)" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voiApplied "Full scan volume" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> a schema1:PropertyValue ;
    schema1:name "Effective Spatial Resolution (PSF/MTF)" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> ;
    schema1:value "N — the paper's \"spatial resolution\" figures are given in µm/px with voxel volumes, i.e. the voxel size (25 µm); no effective resolution reported" .


```


### detail example Richard2019-3
detail instance derived from Richard et al. 2019 (Chem. Geol.) Synthetic quartz (fluid incl.) ROI scan (high-res) Nikon XTH 320/225 U. Strathclyde.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Richard2019-3",
  "@type": [
    "ada:XCTVolume"
  ],
  "ada:componentType": "ada:XCTVolume",
  "schema:measurementTechnique": [
    {
      "@id": "ex:labxctTAPP-Richard2019-3"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "missing"
    }
  ],
  "ada:sampleDimensions": "3 × 5 × 2 cm",
  "ada:sampleName": "Sample B (synthetic quartz)",
  "ada:samplingUnit": "missing",
  "ada:voiApplied": "Full scan volume",
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
    }
  ]
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
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Richard2019-3",
  "@type": [
    "ada:XCTVolume"
  ],
  "ada:componentType": "ada:XCTVolume",
  "schema:measurementTechnique": [
    {
      "@id": "ex:labxctTAPP-Richard2019-3"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "missing"
    }
  ],
  "ada:sampleDimensions": "3 \u00d7 5 \u00d7 2 cm",
  "ada:sampleName": "Sample B (synthetic quartz)",
  "ada:samplingUnit": "missing",
  "ada:voiApplied": "Full scan volume",
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
    }
  ]
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .

ex:detail-Richard2019-3 a ada:XCTVolume ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:labxctTAPP-Richard2019-3 ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:componentType "ada:XCTVolume" ;
    ada:sampleDimensions "3 × 5 × 2 cm" ;
    ada:sampleName "Sample B (synthetic quartz)" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voiApplied "Full scan volume" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> a schema1:PropertyValue ;
    schema1:name "Effective Spatial Resolution (PSF/MTF)" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> ;
    schema1:value "N — the paper's \"spatial resolution\" figures are given in µm/px with voxel volumes, i.e. the voxel size (7.7 µm); no effective resolution reported" .


```


### detail example Richard2019-4
detail instance derived from Richard et al. 2019 (Chem. Geol.) Fluid incl. minerals (C-I) Single-volume Phoenix Nanotom S U. Lorraine.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Richard2019-4",
  "@type": [
    "ada:XCTVolume"
  ],
  "ada:componentType": "ada:XCTVolume",
  "schema:measurementTechnique": [
    {
      "@id": "ex:labxctTAPP-Richard2019-4"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "missing"
    }
  ],
  "ada:sampleDimensions": "Varies: 0.3×0.4 to 11×11×7 mm",
  "ada:sampleName": "Samples C–I (various)",
  "ada:samplingUnit": "missing",
  "ada:voiApplied": "Full scan volume per sample",
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
    }
  ]
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
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Richard2019-4",
  "@type": [
    "ada:XCTVolume"
  ],
  "ada:componentType": "ada:XCTVolume",
  "schema:measurementTechnique": [
    {
      "@id": "ex:labxctTAPP-Richard2019-4"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "missing"
    }
  ],
  "ada:sampleDimensions": "Varies: 0.3\u00d70.4 to 11\u00d711\u00d77 mm",
  "ada:sampleName": "Samples C\u2013I (various)",
  "ada:samplingUnit": "missing",
  "ada:voiApplied": "Full scan volume per sample",
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
    }
  ]
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .

ex:detail-Richard2019-4 a ada:XCTVolume ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:labxctTAPP-Richard2019-4 ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:componentType "ada:XCTVolume" ;
    ada:sampleDimensions "Varies: 0.3×0.4 to 11×11×7 mm" ;
    ada:sampleName "Samples C–I (various)" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voiApplied "Full scan volume per sample" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> a schema1:PropertyValue ;
    schema1:name "Effective Spatial Resolution (PSF/MTF)" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> ;
    schema1:value "N — the paper's \"spatial resolution\" figures are given in µm/px with voxel volumes, i.e. the voxel size (0.77–3.5 µm); no effective resolution reported" .


```


### detail example Tait2014
detail instance derived from Tait 2014 (Thesis) Watson 012 H7 chondrite Single-volume XRADIA XRM500 CSIRO Kensington.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Tait2014",
  "@type": [
    "ada:XCTVolume"
  ],
  "ada:componentType": "ada:XCTVolume",
  "schema:measurementTechnique": [
    {
      "@id": "ex:labxctTAPP-Tait2014"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "missing"
    }
  ],
  "ada:sampleDimensions": "8 mm diameter core",
  "ada:sampleName": "Watson 012",
  "ada:samplingUnit": "missing",
  "ada:voiApplied": "Full 8 mm core volume",
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
    }
  ]
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
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Tait2014",
  "@type": [
    "ada:XCTVolume"
  ],
  "ada:componentType": "ada:XCTVolume",
  "schema:measurementTechnique": [
    {
      "@id": "ex:labxctTAPP-Tait2014"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "missing"
    }
  ],
  "ada:sampleDimensions": "8 mm diameter core",
  "ada:sampleName": "Watson 012",
  "ada:samplingUnit": "missing",
  "ada:voiApplied": "Full 8 mm core volume",
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
    }
  ]
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .

ex:detail-Tait2014 a ada:XCTVolume ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:labxctTAPP-Tait2014 ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:componentType "ada:XCTVolume" ;
    ada:sampleDimensions "8 mm diameter core" ;
    ada:sampleName "Watson 012" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voiApplied "Full 8 mm core volume" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> a schema1:PropertyValue ;
    schema1:name "Effective Spatial Resolution (PSF/MTF)" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> ;
    schema1:value "N — voxel size only (1.923 µm); no spatial resolution reported" .


```


### detail example Charles2018
detail instance derived from Charles et al. 2018 (MAPS) NWA 801 CR2 chondrite Single-volume GE eXplore speCZT U. Western Ontario.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Charles2018",
  "@type": [
    "ada:XCTVolume"
  ],
  "ada:componentType": "ada:XCTVolume",
  "schema:measurementTechnique": [
    {
      "@id": "ex:labxctTAPP-Charles2018"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "missing"
    }
  ],
  "ada:sampleDimensions": "Analysis zone ~3 × 0.7 × 4.1 cm",
  "ada:sampleName": "NWA 801",
  "ada:samplingUnit": "missing",
  "ada:voiApplied": "~8.6 cm³ parallelepiped (three neighboring zones)",
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
      "schema:value": "N — voxel size only (49.8 µm); no spatial resolution reported"
    }
  ]
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
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Charles2018",
  "@type": [
    "ada:XCTVolume"
  ],
  "ada:componentType": "ada:XCTVolume",
  "schema:measurementTechnique": [
    {
      "@id": "ex:labxctTAPP-Charles2018"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "missing"
    }
  ],
  "ada:sampleDimensions": "Analysis zone ~3 \u00d7 0.7 \u00d7 4.1 cm",
  "ada:sampleName": "NWA 801",
  "ada:samplingUnit": "missing",
  "ada:voiApplied": "~8.6 cm\u00b3 parallelepiped (three neighboring zones)",
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
      "schema:value": "N \u2014 voxel size only (49.8 \u00b5m); no spatial resolution reported"
    }
  ]
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .

ex:detail-Charles2018 a ada:XCTVolume ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:labxctTAPP-Charles2018 ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:componentType "ada:XCTVolume" ;
    ada:sampleDimensions "Analysis zone ~3 × 0.7 × 4.1 cm" ;
    ada:sampleName "NWA 801" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voiApplied "~8.6 cm³ parallelepiped (three neighboring zones)" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> a schema1:PropertyValue ;
    schema1:name "Effective Spatial Resolution (PSF/MTF)" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> ;
    schema1:value "N — voxel size only (49.8 µm); no spatial resolution reported" .


```


### detail example Treiman2022
detail instance derived from Treiman et al. 2022 (MAPS) EET 87503 howardite Single-volume NIST-NeXT (NXCT) NCNR-NIST.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Treiman2022",
  "@type": [
    "ada:XCTVolume"
  ],
  "ada:componentType": "ada:XCTVolume",
  "schema:measurementTechnique": [
    {
      "@id": "ex:labxctTAPP-Treiman2022"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "missing"
    }
  ],
  "ada:sampleDimensions": "missing",
  "ada:sampleName": "EET 87503,73; GRA 06100,84",
  "ada:samplingUnit": "missing",
  "ada:voiApplied": "Full sample volumes; GRA 06100 cropped to remove plastic region",
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
      "schema:value": "N for XCT — the paper's only resolution statement (\"reconstructed voxel dimension of 15 µm with a minimum resolution of 30 µm\") is explicitly for the NCT (neutron) tomograms; no XCT resolution is reported"
    }
  ]
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
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Treiman2022",
  "@type": [
    "ada:XCTVolume"
  ],
  "ada:componentType": "ada:XCTVolume",
  "schema:measurementTechnique": [
    {
      "@id": "ex:labxctTAPP-Treiman2022"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "missing"
    }
  ],
  "ada:sampleDimensions": "missing",
  "ada:sampleName": "EET 87503,73; GRA 06100,84",
  "ada:samplingUnit": "missing",
  "ada:voiApplied": "Full sample volumes; GRA 06100 cropped to remove plastic region",
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
      "schema:value": "N for XCT \u2014 the paper's only resolution statement (\"reconstructed voxel dimension of 15 \u00b5m with a minimum resolution of 30 \u00b5m\") is explicitly for the NCT (neutron) tomograms; no XCT resolution is reported"
    }
  ]
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .

ex:detail-Treiman2022 a ada:XCTVolume ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:labxctTAPP-Treiman2022 ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:componentType "ada:XCTVolume" ;
    ada:sampleDimensions "missing" ;
    ada:sampleName "EET 87503,73; GRA 06100,84" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voiApplied "Full sample volumes; GRA 06100 cropped to remove plastic region" .

<https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> a schema1:PropertyValue ;
    schema1:name "Effective Spatial Resolution (PSF/MTF)" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/labxctTAPP/effectiveSpatialResolution> ;
    schema1:value "N for XCT — the paper's only resolution statement (\"reconstructed voxel dimension of 15 µm with a minimum resolution of 30 µm\") is explicitly for the NCT (neutron) tomograms; no XCT resolution is reported" .


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
                            orthogonal measurements). The maximum dimension constrains
                            the minimum achievable field of view and therefore the
                            coarsest achievable voxel size. The minimum dimension
                            determines how many voxels span the smallest feature of
                            interest."
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
                        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/targetSelection/schema.yaml#/$defs/Param_Analysis_preAnalysisImagingAndScreening
                        - title: Sample Mass
                          description: 'Mass of the sample in grams, recorded for
                            curatorial tracking of precious or limited materials.
                            Particularly important for meteorite, mission-returned,
                            and other restricted samples. This is an analysis-level
                            field: the actual sample mass depends on the specific
                            sample being scanned, not on the procedure design.'
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
                            orthogonal measurements). The maximum dimension constrains
                            the minimum achievable field of view and therefore the
                            coarsest achievable voxel size. The minimum dimension
                            determines how many voxels span the smallest feature of
                            interest."
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
                          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/targetSelection/schema.yaml#/$defs/Param_Analysis_preAnalysisImagingAndScreening
                        minContains: 0
                        maxContains: 1
                      - contains:
                          title: Sample Mass
                          description: 'Mass of the sample in grams, recorded for
                            curatorial tracking of precious or limited materials.
                            Particularly important for meteorite, mission-returned,
                            and other restricted samples. This is an analysis-level
                            field: the actual sample mass depends on the specific
                            sample being scanned, not on the procedure design.'
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
                description: Method used to mount or hold the sample on the instrument
                  rotation stage. Mounting material should transmit X-rays at the
                  selected voltage without dominating beam attenuation. Report the
                  holder type, adhesive or support material, and any alignment aids
                  used.
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
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              - title: X-ray Power
                description: "X-ray tube power in watts (W) registered by the procedure.
                  Derivable as voltage (kV) \xD7 current (mA) = kV \xD7 \xB5A / 1000.
                  Power constrains the achievable focal spot size for microfocal tubes:
                  higher power requires a larger focal spot, trading spatial resolution
                  for SNR. Retained as a standalone field because it is routinely
                  reported in the literature and directly constrains instrument operating
                  limits. If power was varied across samples within the session, report
                  the full range applied (e.g., 7\u201313 W)."
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
                  of the sample rotation axis, in mm, as registered by the procedure.
                  Together with SDD, determines geometric magnification (M = SDD/SOD).
                  Shorter SOD increases magnification and reduces voxel size.
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
                  surface, in mm, as registered by the procedure. Together with SOD,
                  determines geometric magnification M = SDD/SOD. Voxel size \u2248
                  detector pixel size / M (before binning; divide additionally by
                  optical objective for Versa-class systems)."
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
                description: "Total angular range over which projection images are
                  acquired, in degrees. Full 360\xB0 rotation is standard for cone-beam
                  lab XCT. 180\xB0 rotation (half-scan) is sometimes used for faster
                  acquisition but may introduce additional artifacts."
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
                  over the full rotation range. More projections improve reconstruction
                  quality by reducing under-sampling streak artifacts but increase
                  scan time. For Mode B (multi-volume stitching), this is the number
                  per sub-volume.
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
                  of projections explicitly. Finer step sizes improve angular sampling
                  and reduce streak artifacts at the cost of longer scan time.
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
                  image frame, in seconds, as registered by the procedure. Set as
                  a deliberate choice for the target sample type and voxel size: longer
                  exposures increase SNR at the cost of total scan time. May be adjusted
                  within procedure-allowed bounds for samples that are unusually dense
                  or unusually transparent. If the exposure time was varied across
                  samples within the same procedure or session, report the full range
                  applied (e.g., 0.5\u20132 s)."
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
                  to produce each saved projection image, as registered by the procedure.
                  Frame averaging reduces random electronic noise. The effective exposure
                  per projection = exposure time per frame \xD7 frames averaged."
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
                  into one), reducing effective resolution while increasing per-pixel
                  SNR and reducing file size. 1\xD71 indicates no binning."
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
                  during each exposure (stop-and-shoot; eliminates motion blur). Continuous
                  rotation has been associated with sub-volume rotational mismatch
                  artifacts in multi-volume stitching workflows (Eckley et al. 2025).
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
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/targetSelection/schema.yaml#/$defs/Param_Analysis_targetSelectionCriteria
              - title: Reconstruction Convolution Filter
                description: Convolution (apodization) filter kernel applied during
                  back-projection reconstruction. Sharper filters (Ram-Lak) enhance
                  edge definition but amplify high-frequency noise; smoother filters
                  (Hann, Hamming) reduce noise at the cost of edge sharpness. The
                  choice represents a deliberate procedure-level tradeoff.
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
                  hardening correction algorithm for this specific analysis. May be
                  tuned empirically per material type or per scan session. Analysis-level
                  companion to Beam Hardening Correction Method.
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
                  Ring artifacts appear as concentric circular bands centred on the
                  rotation axis and arise from defective or miscalibrated detector
                  pixels. Method is the procedure-level specification; whether correction
                  was applied and its outcome are recorded at analysis level in Group
                  6.
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
                  to physically meaningful units using reference materials. Calibrated
                  CT numbers enable cross-instrument and cross-session comparison
                  and support phase identification by comparison to calculated linear
                  attenuation coefficient (LAC) values (e.g., using MuCalc; Hanna
                  & Ketcham 2017). Uncalibrated grayscale values are instrument- and
                  session-specific.
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
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              - title: Segmentation Method
                description: General approach used to separate distinct phases or
                  features in the reconstructed CT volume. The method must be reported
                  for any quantitative result to be reproducible.
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
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              - title: Segmentation Threshold Values or Criteria
                description: "Specific CT number range(s) or quantitative criteria
                  used to define each segmented phase or feature. Documenting these
                  values enables reproducibility assessment and cross-study comparison.
                  For LAC-calibrated datasets, report values in cm\u207B\xB9."
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
                description: Procedure-level rules specifying how the Volume of Interest
                  (VOI) is to be defined for quantitative analysis. Common criteria
                  exclude cone-beam artifact zones at sample edges, beam hardening
                  halos near dense inclusions, and sample holder signal. The actual
                  VOI applied in a specific analysis is recorded separately at analysis
                  level.
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
                  floating point. Bit depth affects the dynamic range available for
                  phase segmentation and quantitative attenuation analysis. The procedure
                  may specify a required output bit depth if downstream analysis workflows
                  depend on a consistent grayscale range; the analyst confirms or
                  adjusts at analysis time.
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
                  all sub-volumes (not including setup or reconstruction time). Useful
                  for assessing beam stability and sample integrity concerns over
                  long scans.
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
                description: "Procedure-level specification of how partial volume
                  effects (PVE) are managed in quantitative analysis. PVE produces
                  intermediate CT numbers at phase boundaries and at the surfaces
                  of small features, because each voxel integrates the attenuation
                  of all material within its volume. PVE correction can be implemented
                  via PSF-based deconvolution tools such as Blob3D. Record the minimum
                  feature size criterion adopted for the procedure (in voxels or \xB5m),
                  the basis for it, the treatment of boundary voxels in modal abundance
                  or size distribution calculations, and whether PVE correction is
                  required or optional. Per Withers et al. (2021) a feature must span
                  at least 3 voxels to be positively identified and at least 10 for
                  reliable shape and volume characterisation; state whether the criterion
                  follows that convention or is SNR-limited, PVE-limited or analyst-defined.
                  The criterion materially changes reported modal abundances and size
                  distributions, so two datasets are not comparable without it."
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
                description: Procedure-level specification of what independent analytical
                  validation is required to confirm CT segmentation results, phase
                  identification, or quantitative measurements. Cross-validation is
                  relevant where CT grey-values alone cannot uniquely distinguish
                  phases with similar attenuation coefficients. Common approaches
                  include BSE imaging, SEM-EDS or EPMA modal analysis, He pycnometry
                  for bulk porosity, and Raman or SIMS phase mapping. Record the required
                  validation method(s) and the sampling fraction (e.g., every sample,
                  one per session, or a representative subset).
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
                description: Method used to mount or hold the sample on the instrument
                  rotation stage. Mounting material should transmit X-rays at the
                  selected voltage without dominating beam attenuation. Report the
                  holder type, adhesive or support material, and any alignment aids
                  used.
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
                description: "X-ray tube power in watts (W) registered by the procedure.
                  Derivable as voltage (kV) \xD7 current (mA) = kV \xD7 \xB5A / 1000.
                  Power constrains the achievable focal spot size for microfocal tubes:
                  higher power requires a larger focal spot, trading spatial resolution
                  for SNR. Retained as a standalone field because it is routinely
                  reported in the literature and directly constrains instrument operating
                  limits. If power was varied across samples within the session, report
                  the full range applied (e.g., 7\u201313 W)."
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
                  of the sample rotation axis, in mm, as registered by the procedure.
                  Together with SDD, determines geometric magnification (M = SDD/SOD).
                  Shorter SOD increases magnification and reduces voxel size.
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
                  surface, in mm, as registered by the procedure. Together with SOD,
                  determines geometric magnification M = SDD/SOD. Voxel size \u2248
                  detector pixel size / M (before binning; divide additionally by
                  optical objective for Versa-class systems)."
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
                description: "Total angular range over which projection images are
                  acquired, in degrees. Full 360\xB0 rotation is standard for cone-beam
                  lab XCT. 180\xB0 rotation (half-scan) is sometimes used for faster
                  acquisition but may introduce additional artifacts."
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
                  over the full rotation range. More projections improve reconstruction
                  quality by reducing under-sampling streak artifacts but increase
                  scan time. For Mode B (multi-volume stitching), this is the number
                  per sub-volume.
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
                  of projections explicitly. Finer step sizes improve angular sampling
                  and reduce streak artifacts at the cost of longer scan time.
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
                  image frame, in seconds, as registered by the procedure. Set as
                  a deliberate choice for the target sample type and voxel size: longer
                  exposures increase SNR at the cost of total scan time. May be adjusted
                  within procedure-allowed bounds for samples that are unusually dense
                  or unusually transparent. If the exposure time was varied across
                  samples within the same procedure or session, report the full range
                  applied (e.g., 0.5\u20132 s)."
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
                  to produce each saved projection image, as registered by the procedure.
                  Frame averaging reduces random electronic noise. The effective exposure
                  per projection = exposure time per frame \xD7 frames averaged."
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
                  into one), reducing effective resolution while increasing per-pixel
                  SNR and reducing file size. 1\xD71 indicates no binning."
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
                  during each exposure (stop-and-shoot; eliminates motion blur). Continuous
                  rotation has been associated with sub-volume rotational mismatch
                  artifacts in multi-volume stitching workflows (Eckley et al. 2025).
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
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/targetSelection/schema.yaml#/$defs/Param_Analysis_targetSelectionCriteria
              minContains: 0
              maxContains: 1
            - contains:
                title: Reconstruction Convolution Filter
                description: Convolution (apodization) filter kernel applied during
                  back-projection reconstruction. Sharper filters (Ram-Lak) enhance
                  edge definition but amplify high-frequency noise; smoother filters
                  (Hann, Hamming) reduce noise at the cost of edge sharpness. The
                  choice represents a deliberate procedure-level tradeoff.
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
                  hardening correction algorithm for this specific analysis. May be
                  tuned empirically per material type or per scan session. Analysis-level
                  companion to Beam Hardening Correction Method.
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
                  Ring artifacts appear as concentric circular bands centred on the
                  rotation axis and arise from defective or miscalibrated detector
                  pixels. Method is the procedure-level specification; whether correction
                  was applied and its outcome are recorded at analysis level in Group
                  6.
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
                  to physically meaningful units using reference materials. Calibrated
                  CT numbers enable cross-instrument and cross-session comparison
                  and support phase identification by comparison to calculated linear
                  attenuation coefficient (LAC) values (e.g., using MuCalc; Hanna
                  & Ketcham 2017). Uncalibrated grayscale values are instrument- and
                  session-specific.
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
                description: General approach used to separate distinct phases or
                  features in the reconstructed CT volume. The method must be reported
                  for any quantitative result to be reproducible.
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
                  used to define each segmented phase or feature. Documenting these
                  values enables reproducibility assessment and cross-study comparison.
                  For LAC-calibrated datasets, report values in cm\u207B\xB9."
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
                description: Procedure-level rules specifying how the Volume of Interest
                  (VOI) is to be defined for quantitative analysis. Common criteria
                  exclude cone-beam artifact zones at sample edges, beam hardening
                  halos near dense inclusions, and sample holder signal. The actual
                  VOI applied in a specific analysis is recorded separately at analysis
                  level.
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
                  floating point. Bit depth affects the dynamic range available for
                  phase segmentation and quantitative attenuation analysis. The procedure
                  may specify a required output bit depth if downstream analysis workflows
                  depend on a consistent grayscale range; the analyst confirms or
                  adjusts at analysis time.
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
                  all sub-volumes (not including setup or reconstruction time). Useful
                  for assessing beam stability and sample integrity concerns over
                  long scans.
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
                description: "Procedure-level specification of how partial volume
                  effects (PVE) are managed in quantitative analysis. PVE produces
                  intermediate CT numbers at phase boundaries and at the surfaces
                  of small features, because each voxel integrates the attenuation
                  of all material within its volume. PVE correction can be implemented
                  via PSF-based deconvolution tools such as Blob3D. Record the minimum
                  feature size criterion adopted for the procedure (in voxels or \xB5m),
                  the basis for it, the treatment of boundary voxels in modal abundance
                  or size distribution calculations, and whether PVE correction is
                  required or optional. Per Withers et al. (2021) a feature must span
                  at least 3 voxels to be positively identified and at least 10 for
                  reliable shape and volume characterisation; state whether the criterion
                  follows that convention or is SNR-limited, PVE-limited or analyst-defined.
                  The criterion materially changes reported modal abundances and size
                  distributions, so two datasets are not comparable without it."
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
                description: Procedure-level specification of what independent analytical
                  validation is required to confirm CT segmentation results, phase
                  identification, or quantitative measurements. Cross-validation is
                  relevant where CT grey-values alone cannot uniquely distinguish
                  phases with similar attenuation coefficients. Common approaches
                  include BSE imaging, SEM-EDS or EPMA modal analysis, He pycnometry
                  for bulk porosity, and Raman or SIMS phase mapping. Record the required
                  validation method(s) and the sampling fraction (e.g., every sample,
                  one per session, or a representative subset).
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
                          description: Any preparation steps applied to the sample
                            before scanning, including cleaning, trimming, consolidation,
                            or drying. XCT is typically non-destructive with no surface
                            preparation required; note any exceptions.
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
                              description: Whether dark-field (detector read with
                                X-ray source off; electronic noise baseline) and bright-field
                                (source on, no sample; gain calibration) reference
                                images are acquired and applied to normalize detector
                                response before reconstruction. Standard practice
                                in all quantitative lab XCT;.
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
                              required:
                              - '@id'
                              - '@type'
                              - schema:propertyID
                              - schema:name
                              - schema:value
                            - title: Sub-volume Stitching and Registration Method
                              description: "Method used to register adjacent sub-volume
                                datasets to each other and stitch them into a single
                                continuous 3D volume. Report the alignment strategy
                                (manual, automated, fiducial-based), the software
                                used, and any correction steps applied. Note: rotational
                                mismatch artifacts have been identified in continuous-rotation
                                acquisitions (~0.35\xB0 misalignment in Eckley et
                                al. 2025); their correction via raw projection re-alignment
                                should be documented here."
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
                                response before reconstruction. Standard practice
                                in all quantitative lab XCT;.
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
                              description: "Method used to register adjacent sub-volume
                                datasets to each other and stitch them into a single
                                continuous 3D volume. Report the alignment strategy
                                (manual, automated, fiducial-based), the software
                                used, and any correction steps applied. Note: rotational
                                mismatch artifacts have been identified in continuous-rotation
                                acquisitions (~0.35\xB0 misalignment in Eckley et
                                al. 2025); their correction via raw projection re-alignment
                                should be documented here."
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
                        const: Data reduction
                    required:
                    - schema:name
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
                        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/geochemProduct/schema.yaml#/$defs/UsedComputationalTool
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
                                    number. Often bundled with the instrument and
                                    proprietary to the manufacturer.
                                  anyOf:
                                  - type: string
                                  - type: array
                                    items:
                                      type: string
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
                                        in kilovolts (kV) registered by the procedure.
                                        Determines the maximum X-ray photon energy
                                        and controls penetration depth and phase contrast.
                                        Higher voltages provide greater penetration
                                        for dense or large samples; lower voltages
                                        improve contrast between low-density phases.
                                        If the voltage was varied across samples within
                                        the same procedure or session, report the
                                        full range applied (e.g., 90\u2013115 kV).
                                        Note: some sources report this parameter as
                                        'X keV' (maximum Bremsstrahlung photon energy)
                                        rather than 'X kV' (tube voltage). For polychromatic
                                        lab XCT, these are numerically equivalent:
                                        E_max [keV] = V [kV]. Record the value as
                                        originally reported, and add a parenthetical
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
                                        (\xB5A) registered by the procedure. Controls
                                        photon flux and therefore projection image
                                        SNR. Higher current improves SNR but increases
                                        thermal loading on the source and may increase
                                        focal spot size. If the current was varied
                                        across samples within the same procedure or
                                        session, report the full range applied (e.g.,
                                        65\u2013115 \xB5A)."
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
                                        the sample. Hardens the beam by attenuating
                                        low-energy photons, reducing beam hardening
                                        artifacts and improving CT number stability
                                        across the sample. Both filter material and
                                        thickness must be reported. Instrument-proprietary
                                        filter codes should be decoded where possible.
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
                                        The procedure registers the target voxel size,
                                        set based on the smallest feature to be resolved
                                        (target voxel size \u2264 ~1/3 of that feature
                                        size; see the criterion recorded under Partial
                                        Volume Effect Criteria). At analysis level,
                                        record the achieved voxel size as reported
                                        by the reconstruction software, which may
                                        differ slightly from the target due to final
                                        geometric calibration."
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
                                        in kilovolts (kV) registered by the procedure.
                                        Determines the maximum X-ray photon energy
                                        and controls penetration depth and phase contrast.
                                        Higher voltages provide greater penetration
                                        for dense or large samples; lower voltages
                                        improve contrast between low-density phases.
                                        If the voltage was varied across samples within
                                        the same procedure or session, report the
                                        full range applied (e.g., 90\u2013115 kV).
                                        Note: some sources report this parameter as
                                        'X keV' (maximum Bremsstrahlung photon energy)
                                        rather than 'X kV' (tube voltage). For polychromatic
                                        lab XCT, these are numerically equivalent:
                                        E_max [keV] = V [kV]. Record the value as
                                        originally reported, and add a parenthetical
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
                                        (\xB5A) registered by the procedure. Controls
                                        photon flux and therefore projection image
                                        SNR. Higher current improves SNR but increases
                                        thermal loading on the source and may increase
                                        focal spot size. If the current was varied
                                        across samples within the same procedure or
                                        session, report the full range applied (e.g.,
                                        65\u2013115 \xB5A)."
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
                                        the sample. Hardens the beam by attenuating
                                        low-energy photons, reducing beam hardening
                                        artifacts and improving CT number stability
                                        across the sample. Both filter material and
                                        thickness must be reported. Instrument-proprietary
                                        filter codes should be decoded where possible.
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
                                        The procedure registers the target voxel size,
                                        set based on the smallest feature to be resolved
                                        (target voxel size \u2264 ~1/3 of that feature
                                        size; see the criterion recorded under Partial
                                        Volume Effect Criteria). At analysis level,
                                        record the achieved voxel size as reported
                                        by the reconstruction software, which may
                                        differ slightly from the target due to final
                                        geometric calibration."
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
    schema:additionalProperty:
      type: array
      items:
        anyOf:
        - title: Effective Spatial Resolution (PSF/MTF)
          description: "Effective spatial resolution of the reconstructed CT volume,
            which typically differs from (and is coarser than) the voxel size due
            to the detector point spread function (PSF), geometric unsharpness, and
            the reconstruction filter. The Nyquist limit sets a theoretical floor
            at 2\xD7 the voxel size. Formal measurement uses the PSF method described
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
          description: 'Total number of overlapping sub-volume scans acquired to cover
            the full sample length. This is an analysis-level parameter: the number
            of sub-volumes depends on the length of the specific sample being scanned
            and cannot be fixed in the procedure in advance. Applies only to Mode
            B (multi-volume stitching).'
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
          description: Actual Volume of Interest used in this specific analysis, including
            dimensions or defining criteria. Analysis-level companion to VOI Selection
            Criteria.
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
            sub-volumes as used in this analysis. May differ from the minimum sub-volume
            overlap required specified in the procedure (Group 4) if sample geometry
            or operator decisions resulted in greater or lesser overlap.
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
            the reconstruction filter. The Nyquist limit sets a theoretical floor
            at 2\xD7 the voxel size. Formal measurement uses the PSF method described
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
          description: 'Total number of overlapping sub-volume scans acquired to cover
            the full sample length. This is an analysis-level parameter: the number
            of sub-volumes depends on the length of the specific sample being scanned
            and cannot be fixed in the procedure in advance. Applies only to Mode
            B (multi-volume stitching).'
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
          description: Actual Volume of Interest used in this specific analysis, including
            dimensions or defining criteria. Analysis-level companion to VOI Selection
            Criteria.
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
            sub-volumes as used in this analysis. May differ from the minimum sub-volume
            overlap required specified in the procedure (Group 4) if sample geometry
            or operator decisions resulted in greater or lesser overlap.
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
                  applied during reconstruction. Beam hardening in polychromatic lab
                  XCT produces a characteristic darker interior and brighter edges
                  in the reconstructed CT number profile, even in compositionally
                  uniform material. Record whether this artifact is detectable in
                  the final dataset, what correction or mitigation was applied (e.g.,
                  linearisation, pre-filtering, iterative correction), and whether
                  any residual effect influences the analysis region.
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
                  image intensity in narrow annular bands; in samples containing linear
                  geological features oriented tangentially to the rotation axis,
                  ring correction can alter or introduce spurious linear features
                  in those orientations. Record whether rings were present, whether
                  correction was applied, and whether any residual rings or correction
                  artifacts fall within the analysis volume of interest."
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
                description: Analysis-level record of PVE severity and how it was
                  handled in this specific analysis. Documents the minimum feature
                  size relative to the voxel size, the fraction of the feature population
                  affected, and any PVE correction method applied (e.g., PSF-based
                  deconvolution via Blob3D).
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
                  (e.g., an inclusion-free zone of the matrix). SNR is controlled
                  by photon flux (source power, exposure time, number of projections)
                  and sample attenuation. Record the measured value and the region
                  used for measurement, or note if SNR was not formally measured.
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
                description: Analysis-level record of what independent validation
                  was performed and its result. Report the validation method(s) used,
                  the quantitative agreement achieved (e.g., relative difference in
                  modal abundance, porosity), and any discrepancies and their likely
                  causes. Where BSE imaging is the validation method, note that BSE
                  provides a 2D section while CT provides a 3D volume.
                anyOf:
                - type: string
                - type: array
                  items:
                    type: string

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
    "wd": "https://www.wikidata.org/entity/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "cdif": "https://w3id.org/cdif/",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
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

