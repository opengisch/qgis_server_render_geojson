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

    def __init__(self, serverIface=None):
        if serverIface:
            super().__init__(serverIface)

        self.prefix_path = os.environ.get('QGIS_RENDERGEOJSON_PREFIX')

    def requestReady(self):
        pass

    def sendResponse(self):
        pass

    def _resolve_url(self, url):
        """If the path exists locally, relative to the prefix path, return this. If not, try downloading the file."""

        if self.prefix_path:
            local_path = os.path.join(self.prefix_path, url)
        else:
            local_path = None

        if not local_path or not os.path.exists(local_path):
            try:
                local_path, headers = urllib.request.urlretrieve(url)
            except ValueError:
                raise ParameterError('The file `{}` could not be found locally and not be retrieved as download.'.format(url))

        return local_path

    def _load_style(self, layer, style):
        f = QFile(style)
        f.open(QIODevice.ReadOnly)
        d = QDomDocument()
        d.setContent(f)
        doc = d.documentElement()
        rw_context = QgsReadWriteContext()
        layer.readStyle(doc, '', rw_context)

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

                if '$type' in style:
                    polygon_style = self._resolve_url(style.replace('$type', 'polygons'))
                    line_style = self._resolve_url(style.replace('$type', 'lines'))
                    point_style = self._resolve_url(style.replace('$type', 'points'))
                else:
                    polygon_style = self._resolve_url(style)
                    line_style = polygon_style
                    point_style = polygon_style

                polygon_layer = QgsVectorLayer(
                    geojson_file_name + '|geometrytype=Polygon', 'polygons', 'ogr')
                self._load_style(polygon_layer, polygon_style)
                line_layer = QgsVectorLayer(
                    geojson_file_name + '|geometrytype=Line', 'lines', 'ogr')
                self._load_style(line_layer, line_style)
                point_layer = QgsVectorLayer(
                    geojson_file_name + '|geometrytype=Point', 'points', 'ogr')
                self._load_style(point_layer, point_style)

                settings = QgsMapSettings()
                settings.setOutputSize(QSize(width, height))
                settings.setOutputDpi(dpi)
                settings.setExtent(bbox)
                settings.setLayers([polygon_layer, line_layer, point_layer])
                settings.setBackgroundColor(QColor(Qt.transparent))
                renderer = QgsMapRendererParallelJob(settings)

                event_loop = QEventLoop()
                renderer.finished.connect(event_loop.quit)
                renderer.start()

                event_loop.exec_()

                img = renderer.renderedImage()
                img.setDotsPerMeterX(dpi * 39.37)
                img.setDotsPerMeterY(dpi * 39.37);
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
                request.appendBody(b'Unhandled error')
                request.appendBody(traceback.format_exc().encode('utf-8'))


class RenderGeojsonServer:
    """Render Geojson"""

    def __init__(self, serverIface):
        self.serverIface = serverIface
        serverIface.registerFilter(RenderGeojsonFilter(serverIface), 1)
