# -*- coding: utf-8 -*-
"""
 This script initializes the plugin, making it known to QGIS.
"""


def classFactory(iface):
    from qgis.PyQt.QtWidgets import QMessageBox

    class Nothing:

        def __init__(self, iface):
            self.iface = iface

        def initGui(self):
            QMessageBox.warning(
                self.iface.mainWindow(),
                'qgis_server_render_geojson plugin',
                'qgis_server_render_geojson is a plugin for QGIS Server. There is nothing in QGIS Desktop.',
            )

        def unload(self):
            pass

    return Nothing(iface)

def serverClassFactory(serverIface):
    from .render_geojson import RenderGeojsonServer
    return RenderGeojsonServer(serverIface)
