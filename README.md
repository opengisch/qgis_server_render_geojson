# qgis_server_render_geojson

A **QGIS Server Plugin** to render **GEOJSON** with **QML styling**.

With this plugin installed, your QGIS server will be able to render a geojson file to a PNG image. The geojson file can be a **local file or downloaded from a network service**. A qml file can be provided to define the rendering style of the geojson.

It works almost like WMS, except that the source of the data and the symbology are dynamic and must be provided as url parameter. There is also no such thing as `GetCapabilities`.

## Quick start guide: docker-compose

```sh
git clone https://github.com/opengisch/qgis_server_render_geojson.git
cd qgis_server_render_geojson
docker-compose up
```

And navigate to

```
http://localhost:8080/ogc/?SERVICE=RenderGeojson&STYLE=polygon_outline.qml&WIDTH=300&HEIGHT=600&GEOJSON=polygon.geojson&BBOX=2689574,1283976,2689673,1284099
```

## Quick start guide: existing qgis server infrastructure

1. Download https://github.com/opengisch/qgis_server_render_geojson/archive/master.zip
2. Unzip and copy the `qgis_server_render_geojson` folder to a local qgis server plugin path (check: metadata.txt must be in `[plugin_path]/qgis_server_render_geojson/metadata.txt`)
3. Configure the local plugin path by setting it in apache, nginx, (your favorite webserver) `QGIS_PLUGINPATH=[plugin_path]`
4. Restart server

## Request

### Parameters
The request supports the following parameters:

#### `GEOJSON`

Path to the GeoJson file. May be a URI or relative to the prefix in the configuration.

##### Examples

Relative to configured prefix path:

```
GEOJSON=naturgefahren%2Fdata.json
```

Absolute path (url encoded `https://api.sh.ch/v1/get_geojson?topic=naturgefahren`):

```
GEOJSON=https%3A%2F%2Fapi.sh.ch%2Fv1%2Fget_geojson%3Ftopic%3Dnaturgefahren
```


#### `STYLE`

Path to a qml file. May be a URI or relative to the prefix in the configuration.

The substitution variable `$type` is available which will be replaced with `points`, `lines` or `polygons`.

##### Examples

Static:

```
STYLE=naturgefahren%2Fbase.qml
```

Dynamic:

```
STYLE=naturgefahren%2F$type.qml
```

This will lookup up to 3 styles:

 - `naturgefahren/points.qml`
 - `naturgefahren/lines.qml`
 - `naturgefahren/polygons.qml`

#### `BBOX`

The bounding box to render. Needs to match the CRS of the data in the provided GeoJSON file.

##### Example

```
BBOX=2689634.3,1283792.7,2690062.1,1284004.8
```

#### `WIDTH`

The width of the result image in pixels.

##### Example

```
WIDTH=640
```

#### `HEIGHT`

The height of the result image in pixels.

##### Example

```
HEIGHT=480
```

#### `DPI`

The dpi used to render the symbology.

##### Example

```
DPI=96
```

### Examples

Basic request that will search data and style in the prefix directory (see configuration)

```
GET /ogc/?SERVICE=RenderGeojson&GEOJSON=data.json&STYLE=style.qml&BBOX=2689634.3,1283792.7,2690062.1,1284004.8&WIDTH=606&HEIGHT=300&DPI=96
```

Basic request that will search data and style in the prefix directory (see configuration)

```
GET /ogc/?SERVICE=RenderGeojson&GEOJSON=data.json&STYLE=$type.qml&BBOX=2689634.3,1283792.7,2690062.1,1284004.8&WIDTH=606&HEIGHT=300&DPI=96
```

Basic request that will create another request to collect data from another resource

```
GET /ogc/?SERVICE=RenderGeojson&GEOJSON=https%3A%2F%2Fapi.sh.ch%2Fv1%2Fget_geojson%3Fregion%3Dschaffhausen&STYLE=https%3A%2F%2Fapi.sh.ch%2Fstyle%3Fnaturgefahren.qml%26type%3F$type&BBOX=2689634.3,1283792.7,2690062.1,1284004.8&WIDTH=606&HEIGHT=300&DPI=96
```

## Configuration

The prefix path where local (sytle and geojson) files are provided can be defined throug an environment variable `QGIS_RENDERGEOJSON_PREFIX`.
