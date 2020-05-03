from qgis_server_render_geojson.render_geojson import RenderGeojsonFilter
from qgis.server import QgsServerInterface, QgsRequestHandler
import pytest
import mock
import types
import os

@pytest.fixture
def gj_filter(test_data_path):
    if test_data_path:
        os.environ['QGIS_RENDERGEOJSON_PREFIX'] = test_data_path
    filt = RenderGeojsonFilter()
    if test_data_path:
        os.environ.pop('QGIS_RENDERGEOJSON_PREFIX')
    filt._response = bytes()
    filt._headers = dict()
    si = mock.Mock(spec = QgsServerInterface)
    def get_si(self):
        return si
    filt.serverInterface = types.MethodType(get_si, filt)
    si.requestHandler.return_value = mock.Mock(spec = QgsRequestHandler)

    def parameters_map(self):
        return filt._parameters

    si.requestHandler().parameterMap.side_effect = types.MethodType(parameters_map, si.requestHandler())

    def clear_request(self):
        filt._response = bytes()

    def set_header(self, key, value):
        filt._headers[key] = value

    def append_body(self, content):
        filt._response += content

    si.requestHandler().clear.side_effect = types.MethodType(clear_request, si.requestHandler())
    si.requestHandler().setResponseHeader.side_effect = types.MethodType(set_header, si.requestHandler())
    si.requestHandler().appendBody.side_effect = types.MethodType(append_body, si.requestHandler())

    def test_request(self, params):
        self._parameters = params
        self.responseComplete()
        return filt._headers, filt._response

    filt.test_request = test_request
    return filt

@pytest.mark.parametrize('mandatory_param', ['GEOJSON', 'STYLE', 'WIDTH', 'HEIGHT', 'BBOX'])
def test_mandatory_params(gj_filter, mandatory_param):
    params = {
            'SERVICE': 'RENDERGEOJSON',
            'GEOJSON': 'polygon.geojson',
            'STYLE': 'polygons.qml',
            'WIDTH': '800',
            'HEIGHT': '600',
            'BBOX': '1000,2000,1500,2500',
            }
    params.pop(mandatory_param)
    headers, response = gj_filter.test_request(gj_filter, params)

    assert mandatory_param.encode('utf-8') in response

def test_bad_bbox(gj_filter):
    headers, response = gj_filter.test_request(gj_filter, {
            'SERVICE': 'RENDERGEOJSON',
            'GEOJSON': 'polygons.geojson',
            'STYLE': 'style.qml',
            'WIDTH': '800',
            'HEIGHT': '600',
            'BBOX': '1000,2000 : 1500,2500',
            })

    assert b'BBOX' in response

@pytest.mark.parametrize('test_data_path', [None])
def test_get_no_prefix_path(gj_filter):
    headers, response = gj_filter.test_request(gj_filter, {
            'SERVICE': 'RENDERGEOJSON',
            'GEOJSON': 'polygon.geojson',
            'STYLE': 'polygons.qml',
            'WIDTH': '800',
            'HEIGHT': '600',
            'BBOX': '1000,2000,1500,2500',
            })

    assert b'download' in response

def test_get(gj_filter):
    headers, response = gj_filter.test_request(gj_filter, {
            'SERVICE': 'RENDERGEOJSON',
            'GEOJSON': 'polygon.geojson',
            'STYLE': 'polygons.qml',
            'WIDTH': '800',
            'HEIGHT': '600',
            'BBOX': '1000,2000,1500,2500',
            })

    assert b'download' in response
