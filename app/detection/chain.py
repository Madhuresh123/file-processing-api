class DetectorChain:

    def __init__(self, detectors: list):
        self.detectors = detectors

    def detect(self, file_path: str) -> dict:
        context = {}

        for detector in self.detectors:
            result = detector.detect(file_path, context)
            if result.get("category") != "unknown":
                return {**context, **result}

        return {**context, "category": "unknown"}
