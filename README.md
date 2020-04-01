# qgis_server_render_geojson
A QGIS Server Plugin to render GeoJSON with a QML styling

## Request

### Parameters
The request supports the following parameters:

#### GEOJSON

Path to the GeoJson file. May be a URI or relative to the prefix in the configuration.

#### STYLE

Path to a qml file. May be a URI or relative to the prefix in the configuration.
May be overwritten by `STYLEPOLYGON`, `STYLELINE` or `STYLEPOINT`.

#### STYLEPOLYGON

Path to a qml file used for every polygon in the data. May be a URI or relative to the prefix in the configuration.

#### STYLELINE

Path to a qml file used for every line in the data. May be a URI or relative to the prefix in the configuration.

#### STYLEPOINT

Path to a qml file used for every point in the data. May be a URI or relative to the prefix in the configuration.

#### BBOX

The bounding box to render. Needs to match the CRS of the data in the provided GeoJSON file.

#### WIDTH

The width of the result image.

#### HEIGHT

The height of the result image.

#### DPI

The dpi used to render the symbology.

### Examples

Basic request that will search data and style in the prefix directory (see configuration)

```
GET /rendergeojson?GeoJson=data.json&style=style.qml&BBOX=-432786,4372992,3358959,7513746&WIDTH=665&HEIGHT=551&DPI=300
```

Basic request that will search data and style in the prefix directory (see configuration)

```
GET /rendergeojson?GeoJson=data.json&style=style.qml&BBOX=-432786,4372992,3358959,7513746&WIDTH=665&HEIGHT=551&DPI=300
```

Basic request that will create another request to collect data from another resource

```
GET /rendergeojson?GeoJson=https%3A%2F%2Fapi.sh.ch/v1/%2Fget_geojson%3Fregion%3Dschaffhausen&style=https%3A%2F%2Fapi.sh.ch%2Fstyle%3Fmystyle.qml&BBOX=-432786,4372992,3358959,7513746&WIDTH=665&HEIGHT=551&DPI=300
```

## Configuration

```ini
[RenderGeoJson]
Prefix=D:\data\rendergeojson
```
