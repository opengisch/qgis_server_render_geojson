# -*- coding: utf-8 -*-

"""
***************************************************************************
    render_geojson.py
    ---------------------
    Date                 : May 2020
    Copyright            : (C) 2020 by OPENGIS.ch
    Email                : info@opengis.ch
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

__author__ = 'Matthias Kuhn'
__date__ = 'May 2020'
__copyright__ = '(C) 2020, Matthias Kuhn - OPENGIS.ch'

import sys
import os
import shutil
import tempfile
import urllib.request
import traceback

from qgis.server import QgsServerFilter
from qgis.core import QgsMapSettings, QgsMapRendererParallelJob, QgsVectorLayer, QgsMessageLog, Qgis, QgsReadWriteContext, QgsRectangle

from PyQt5.QtCore import QSize, QByteArray, QBuffer, QIODevice, QEventLoop, Qt, QFile
from PyQt5.QtGui import QColor
from PyQt5.QtXml import QDomDocument


class ParameterError(Exception):
    """A parameter exception that is raised will be forwarded to the client."""
    pass


class RenderGeojsonFilter(QgsServerFilter):

    def __init__(self, serverIface):
        super().__init__(serverIface)

        self.prefix_path = os.environ.get('QGIS_RENDERGEOJSON_PREFIX')


    def requestReady(self):
        pass

    def sendResponse(self):
        pass

    def _resolve_url(self, url):
        """If the path exists locally, relative to the prefix path, return this. If not, try downloading the file."""
        local_path = os.path.join(self.prefix_path, url)
        if not os.path.exists(local_path):
            try:
                local_path, headers = urllib.request.urlretrieve(url)
            except ValueError:
                raise ParameterException('The file `url` could not be found locally and not be retrieved as download.')

        return local_path

    def responseComplete(self):
        request = self.serverInterface().requestHandler()
        params = request.parameterMap()

        # SERVICE=RENDERGEOJSON -- we are taking over
        if params.get('SERVICE', '').upper() == 'RENDERGEOJSON':
            request.clear()
            try:
                # Parse parameters
                geojson = params.get('GEOJSON')
                if not geojson:
                    raise ParameterError('Parameter GEOJSON must be set.')

                style = params.get('STYLE')
                if not style:
                    raise ParameterError('Parameter STYLE must be set.')

                try:
                    width = int(params.get('WIDTH'))
                except TypeError:
                    raise ParameterError('Parameter WIDTH must be integer.')
                try:
                    height = int(params.get('HEIGHT'))
                except TypeError:
                    raise ParameterError('Parameter HEIGHT must be integer.')

                try:
                    dpi = int(params.get('DPI', 96))
                except TypeError:
                    raise ParameterError('Parameter DPI must be integer.')

                try:
                    minx, miny, maxx, maxy = params.get('BBOX').split(',')
                    bbox = QgsRectangle(float(minx), float(miny), float(maxx), float(maxy))
                except (ValueError, AttributeError):
                    raise ParameterError('Parameter BBOX must be specified in the form `min_x,min_y,max_x,max_y`.')

                
                url = geojson
                geojson_file_name = self._resolve_url(geojson)
                QgsMessageLog.logMessage(
                    "RenderGeojson.responseComplete :: Rendering file {}".format(url))
                polygon_layer = QgsVectorLayer(
                    geojson_file_name, 'polygons', 'ogr')
                style_path = self._resolve_url(style)
                QgsMessageLog.logMessage(
                    "RenderGeojson.responseComplete :: QML file {}".format(style_path))
                f = QFile(style_path)
                f.open(QIODevice.ReadOnly)
                d = QDomDocument()
                d.setContent(f)
                doc = d.documentElement()
                rw_context = QgsReadWriteContext()
                polygon_layer.readStyle(doc, '', rw_context)
                settings = QgsMapSettings()
                settings.setOutputSize(QSize(width, height))
                settings.setExtent(bbox)
                settings.setLayers([polygon_layer])
                settings.setBackgroundColor(QColor(Qt.transparent))
                renderer = QgsMapRendererParallelJob(settings)

                event_loop = QEventLoop()
                renderer.finished.connect(event_loop.quit)
                renderer.start()

                event_loop.exec_()

                img = renderer.renderedImage()
                image_data = QByteArray()
                buf = QBuffer(image_data)
                buf.open(QIODevice.WriteOnly)
                img.save(buf, 'PNG')

                request.setResponseHeader('Content-type', 'image/png')
                request.appendBody(image_data)
            except ParameterError as e:
                QgsMessageLog.logMessage(
                    "RenderGeojson.responseComplete :: ParameterError")
                request.setResponseHeader('Content-type', 'text/plain')
                request.appendBody(str(e).encode('utf-8'))
            except:
                QgsMessageLog.logMessage(
                    "RenderGeojson.responseComplete :: Exception")
                QgsMessageLog.logMessage(
                    "RenderGeojson.responseComplete ::   {}".format(traceback.format_exc()))
                request.setResponseHeader('Content-type', 'text/plain')
                request.appendBody('Error: {}'.format(str(e)).encode('utf-8'))


class RenderGeojsonServer:
    """Render Geojson"""

    def __init__(self, serverIface):
        self.serverIface = serverIface
        serverIface.registerFilter(RenderGeojsonFilter(serverIface), 1)
