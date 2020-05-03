# -*- coding: utf-8 -*-
"""
 This script initializes the plugin, making it known to QGIS.
"""


def serverClassFactory(serverIface):
    from .render_geojson import RenderGeojsonServer
    return RenderGeojsonServer(serverIface)
