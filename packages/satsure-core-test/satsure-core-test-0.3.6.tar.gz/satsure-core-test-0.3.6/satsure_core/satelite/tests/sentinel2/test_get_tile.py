from satsure_core.satelite.sentinel2 import GetTiles
from satsure_core.satelite.config import DBSession


class TestGetTiles:

    def test_get_tile_from_geom(self, monkeypatch):
        """testcase to get tile from geom"""
        geom = [{
            "type": "Polygon",
            "coordinates": [
                [
                    [74.66218437999487, 19.46556170905807],
                    [74.6629598736763, 19.466339343697722],
                    [74.6640371158719, 19.4667885366414],
                    [74.66395296156406, 19.46614872872264],
                    [74.66376889497042, 19.466150941501425],
                    [74.66369077563286, 19.46577508478787],
                    [74.6635865047574, 19.465278788212864],
                    [74.66282073408365, 19.46540270444271],
                    [74.66218437999487, 19.46556170905807],
                ]
            ],
        }]

        def session_mock():
            def mock_attribute():
                pass

            mock_attribute.close = lambda: True

            return mock_attribute

        monkeypatch.setattr(DBSession, "create", session_mock)
        monkeypatch.setattr(GetTiles, "fetch_tile_from_db",
                            lambda x, y, z: [("gwfhg",), ("3basg",)])

        result = GetTiles().get_tile_from_geom(geom)

        assert len(result) == 2
