# qgis_server_render_geojson
A QGIS Server Plugin to render GeoJSON with a QML styling

## Request

Basic request that will search data and style in the prefix directory (see configuration)

```
GET /rendergeojson?GeoJson=data.json&style=style.qml&BBOX=-432786,4372992,3358959,7513746&WIDTH=665&HEIGHT=551&DPI=300
```

Basic request that will create another request to collect data from another resource

```
GET /rendergeojson?GeoJson=https%3A%2F%2Fapi.sh.ch/v1/%2Fget_geojson%3Fregion%3Dschaffhausen&style=https%3A%2F%2Fapi.sh.ch%2Fstyle%3Fmystyle.qml&BBOX=-432786,4372992,3358959,7513746&WIDTH=665&HEIGHT=551&DPI=300
```

# Configuration

```ini
[RenderGeoJson]
Prefix=D:\data\rendergeojson
```
