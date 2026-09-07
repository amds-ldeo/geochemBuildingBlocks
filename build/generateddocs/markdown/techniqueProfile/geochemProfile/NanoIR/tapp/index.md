
# Nanoscale Infrared Mapping Technique-Aligned Procedure Profile (nanoirTAPP) (Schema)

`ogch.techniqueProfile.geochemProfile.NanoIR.tapp` *v0.1*

Nanoscale Infrared Mapping extension of the base TAPP definition. CORE-ONLY DRAFT: the native technique layer is empty. NanoIR has no ADA detail schema and no technique-specific property in any ADA record, so there was nothing to seed one from and none was invented. This registers the procedure skeleton and needs Phase 0 seed papers before it says anything NanoIR-specific. Generated from draftTAPPs/NanoIR_TAPP_draft_v2.csv by tools/build_tapp.py.

[*Status*](http://www.opengis.net/def/status): Under development

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Nanoscale Infrared Mapping Technique-Aligned Procedure Profile (nanoirTAPP)
description: 'Nanoscale Infrared Mapping extension of the base TAPP definition. CORE-ONLY
  DRAFT: the native technique layer is empty. NanoIR has no ADA detail schema and
  no technique-specific property in any ADA record, so there was nothing to seed one
  from and none was invented. This registers the procedure skeleton and needs Phase
  0 seed papers before it says anything NanoIR-specific. Generated from draftTAPPs/NanoIR_TAPP_draft_v2.csv
  by tools/build_tapp.py.'
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
                  $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Procedure_preAnalysisImagingAndScreening
                allOf:
                - contains:
                    $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Procedure_preAnalysisImagingAndScreening
                  minContains: 0
                  maxContains: 1
    ada:instrumentManufacturer:
      description: Manufacturer of the instrument that performs the measurement, recorded
        as a controlled value. Where a procedure couples a sample-introduction system
        to an analysing instrument, this records the analysing instrument. Instrument
        Model gives the specific designation.
      type: string
      enum:
      - WITec
      - Renishaw
      - HORIBA
      - Bruker
      - Thermo Fisher Scientific
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
    ada:constantsAndReferenceValuesUsedDefault:
      description: Physical constants and reference values used in data reduction
        to calculate the final reported quantity (e.g., decay constants for age calculation,
        standard isotope ratios, or other citable reference values used in a correction
        or calculation), together with their source. Distinct from the Group 6 reference-material
        fields, which document accepted values for specific calibration/validation
        materials rather than universal physical constants. Record "None" if no citable,
        revisable physical constants feed into this procedure's data reduction.
      type: string
  required:
  - ada:targetMaterial
  - ada:instrumentManufacturer
  - ada:instrumentModel
  - ada:constantsAndReferenceValuesUsedDefault

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/NanoIR/tapp/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/NanoIR/tapp/schema.yaml)


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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/NanoIR/tapp/context.jsonld)

## Sources

* [NanoIR_TAPP_draft_v2.csv (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/NanoIR/tapp`

