import io, tempfile
import cv2
import requests


class AlertLVM:
    def __init__(self, token, url="https://xbrain-lvm.dianzeai.com/api/v1/analyses"):
        self.url = url
        self.token = token

    def __call_api(self, key, path):
        headers = {"Authorization": f"Bearer {self.token}"}
        data = {"key": key}
        if isinstance(path, str):
            with open(path, "rb") as file:
                files = {"image": file}
                response = requests.request(
                    method="POST", url=self.url, headers=headers, data=data, files=files
                )
        elif isinstance(path, io.IOBase):
            files = {"image": path}
            response = requests.request(
                method="POST", url=self.url, headers=headers, data=data, files=files
            )
        else:
            raise ValueError("Invalid path type. Expected string or file object.")
        return response

    def analyze(self, scenario_key, path):
        resp = self.__call_api(scenario_key, path)
        return (
            resp.json()
            if resp.status_code == 200
            else {"error": True, "error_message": resp.text, "code": resp.status_code}
        )

    def analyzeVideo(
        self, scenario_key, path, filter=lambda index, frame: index % 750 == 0
    ):
        capture = cv2.VideoCapture(path)
        isOpened = capture.isOpened()
        if not isOpened:
            raise Exception("Failed to open video file")
        while capture.isOpened():
            index = int(capture.get(cv2.CAP_PROP_POS_FRAMES))
            ret, frame = capture.read()
            if not ret:
                break
            if not filter(index, frame):
                continue
            _, buffer = cv2.imencode(".jpg", frame)
            jpeg = buffer.tobytes()
            resp = self.__call_api(scenario_key, io.BytesIO(jpeg))
            result = (
                resp.json()
                if resp.status_code == 200
                else {
                    "error": True,
                    "error_message": resp.text,
                    "code": resp.status_code,
                }
            )
            with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as temp:
                cv2.imwrite(temp.name, frame)
                result["frame"] = temp.name
            yield result
