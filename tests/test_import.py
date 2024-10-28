def test_import_viewport():
    from google.geo.type import (
        viewport_pb2 as google_dot_geo_dot_type_dot_viewport__pb2,
    )  # noqa

    assert google_dot_geo_dot_type_dot_viewport__pb2.Viewport is not None


def test_import_http():
    from google.api import http_pb2 as google_dot_api_dot_http__pb2  # noqa

    assert google_dot_api_dot_http__pb2.Http is not None


def test_import_latlng():
    from google.type import latlng_pb2 as google_dot_type_dot_latlng__pb2  # noqa

    assert google_dot_type_dot_latlng__pb2.LatLng is not None
