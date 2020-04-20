import unittest

from yoti_python_sdk.doc_scan.session.retrieve.face_map_response import FaceMapResponse
from yoti_python_sdk.doc_scan.session.retrieve.liveness_resource_response import (
    ZoomLivenessResourceResponse,
)


class LivenessResourceResponseTest(unittest.TestCase):
    SOME_ID = "someId"
    SOME_FRAMES = [{"first": "frame"}, {"second": "frame"}]

    def test_zoom_liveness_should_parse_correctly(self):
        data = {"id": self.SOME_ID, "facemap": {}, "frames": self.SOME_FRAMES}

        result = ZoomLivenessResourceResponse(data)

        assert result.id is self.SOME_ID
        assert isinstance(result.facemap, FaceMapResponse)
        assert len(result.frames) == 2

    def test_should_parse_with_none(self):
        result = ZoomLivenessResourceResponse(None)

        assert result.id is None
        assert len(result.tasks) == 0
        assert result.facemap is None
        assert len(result.frames) == 0


if __name__ == "__main__":
    unittest.main()
