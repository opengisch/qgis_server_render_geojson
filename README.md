# qgis_server_render_geojson
A QGIS Server Plugin to render GeoJSON with a QML styling

## Request

### Parameters
The request supports the following parameters:

#### `GEOJSON`

Path to the GeoJson file. May be a URI or relative to the prefix in the configuration.

Examples:

Relative to configured prefix path:

```
GEOJSON=naturgefahren/data.json
```

Absolute path (url encoded `https://api.sh.ch/v1/get_geojson?topic=naturgefahren`):

```
GEOJSON=https%3A%2F%2Fapi.sh.ch%2Fv1%2Fget_geojson%3Ftopic%3Dnaturgefahren
```


#### `STYLE`

Path to a qml file. May be a URI or relative to the prefix in the configuration.
May be overwritten by `POLYGONSTYLE`, `LINESTYLE` or `POINTSTYLE`.

Example:

```
STYLE=naturgefahren/base.qml
```

#### `POLYGONSTYLE`

Path to a qml file used for every polygon in the data. May be a URI or relative to the prefix in the configuration.

Example:

```
POLYGONSTYLE=naturgefahren/polygons.qml
```

#### `LINESTYLE`

Path to a qml file used for every line in the data. May be a URI or relative to the prefix in the configuration.

Example:

```
LINESTYLE=naturgefahren/lines.qml
```

#### `POINTSTYLE`

Path to a qml file used for every point in the data. May be a URI or relative to the prefix in the configuration.

Example:

```
POINTSTYLE=naturgefahren/points.qml
```

#### `BBOX`

The bounding box to render. Needs to match the CRS of the data in the provided GeoJSON file.

Example:

```
BBOX=2689634.3,1283792.7,2690062.1,1284004.8
```

#### `WIDTH`

The width of the result image in pixels.

Example:

```
WIDTH=640
```

#### `HEIGHT`

The height of the result image in pixels.

Example:

```
HEIGHT=480
```

#### `DPI`

The dpi used to render the symbology.

Example:

```
DPI=96
```

### Examples

Basic request that will search data and style in the prefix directory (see configuration)

```
GET /rendergeojson?GeoJson=data.json&style=style.qml&BBOX=2689634.3,1283792.7,2690062.1,1284004.8&WIDTH=606&HEIGHT=300&DPI=96
```

Basic request that will search data and style in the prefix directory (see configuration)

```
GET /rendergeojson?GeoJson=data.json&style=style.qml&BBOX=2689634.3,1283792.7,2690062.1,1284004.8&WIDTH=606&HEIGHT=300&DPI=96
```

Basic request that will create another request to collect data from another resource

```
GET /rendergeojson?GeoJson=https%3A%2F%2Fapi.sh.ch/v1/%2Fget_geojson%3Fregion%3Dschaffhausen&style=https%3A%2F%2Fapi.sh.ch%2Fstyle%3Fmystyle.qml&BBOX=2689634.3,1283792.7,2690062.1,1284004.8&WIDTH=606&HEIGHT=300&DPI=96
```

## Configuration

```ini
[RenderGeoJson]
Prefix=D:\data\rendergeojson
```
