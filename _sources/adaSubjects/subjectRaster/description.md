# ADA Subject — raster image component

| key | schemas |
|---|---|
| `channel1` | 18 |
| `numPixelsX`, `numPixelsY`, `pixelScaleX`, `pixelScaleY`, `pixelUnits`, `coordUnits` | 10 each |
| `imageType` | 8 |
| `channel2`, `channel3` | 7 each |

## Types declared are dominant; variants are normalisation work

| key | stored as | declared here |
|---|---|---|
| `pixelScaleX`, `pixelScaleY` | number 9, **`[array,number]` 1** | `number` |
| `imageType` | array 4, **`[array,string]` 4** | `array` of string |
| `channel2`, `channel3` | string 5, null 1, `[null,string]` 1 | `string` |

`imageType` is the weakest of these: it is an even 4/4 split between array and
array-or-string, so "dominant" is a coin toss. Declared as an array because that is the shape
a multi-valued type needs, but it is worth Stephen's eye.

## Mapping is partial on purpose

`numPixelsX`/`numPixelsY` map to `cdif:countColumns`/`cdif:countRows` — a raster's pixel
dimensions ARE its column and row counts, which is the same pair the tabular fragment uses.

**Unmapped:** `pixelScaleX`, `pixelScaleY`, `coordUnits`, `channel1..3`. Pixel scale is a
geospatial-style affine term with no CDIF equivalent, and the channel keys name which measured
quantity each band holds — closer to an InstanceVariable reference than to any property, and
not worth inventing a term for.
