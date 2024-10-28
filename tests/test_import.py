# Copyright 2024 Beijing ColorfulClouds Technology Co., Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
